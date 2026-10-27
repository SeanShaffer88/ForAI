"""Validate local catalog, metadata, generated indexes, CSV, and links offline."""
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from export_csv import ARRAY_FIELDS, FIELDS  # noqa: E402
from generate_indexes import END, START, render  # noqa: E402


def fail(message):
    raise AssertionError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate():
    rows = read_json(ROOT / "resources.json")
    taxonomy = read_json(ROOT / "index" / "taxonomy.json")
    schema = read_json(ROOT / "index" / "resource-schema.json")
    assert rows, "Empty catalog"
    assert schema.get("$schema", "").endswith("2020-12/schema"), "Unexpected schema version"
    allowed = {
        "resource_type": set(taxonomy["resource_types"]),
        "topics": set(taxonomy["topics"]),
        "use_cases": set(taxonomy["use_cases"]),
        "languages": set(taxonomy["languages"]),
        "platforms": set(taxonomy["platforms"]),
        "audiences": set(taxonomy["audiences"]),
        "verification_level": set(taxonomy["verification_levels"]),
    }
    required = set(schema["required"])
    ids = set()
    tuple_keys = set()
    category_counts = {}
    for row in rows:
        missing = required - row.keys()
        assert not missing, f"{row.get('name')}: missing schema fields {sorted(missing)}"
        for field in ("name", "url", "category", "purpose", "source", "checked_on", "review"):
            assert isinstance(row[field], str) and row[field], f"Missing or invalid {field}: {row.get('name')}"
        try:
            date.fromisoformat(row["checked_on"])
        except ValueError:
            fail(f"Invalid checked_on date: {row['name']} {row['checked_on']}")
        parts = urlsplit(row["url"])
        assert parts.scheme == "https" and parts.netloc, row
        key = (row["source"], row["name"], row["url"])
        assert key not in tuple_keys, f"Duplicate record tuple: {key}"
        tuple_keys.add(key)
        rid = row["resource_id"]
        assert re.fullmatch(r"res-[a-z0-9-]+", rid), f"Invalid resource_id: {rid}"
        assert rid not in ids, f"Duplicate resource_id: {rid}"
        ids.add(rid)
        expected_category_id = re.sub(r"[^a-z0-9]+", "-", row["category"].casefold()).strip("-")
        assert row["category_id"] == expected_category_id, f"Incorrect category_id: {row['name']}"
        assert row["resource_type"] in allowed["resource_type"], f"Unknown resource_type: {row}"
        for field in ("topics", "use_cases", "languages", "platforms", "audiences", "related_resource_ids"):
            values = row[field]
            assert isinstance(values, list) and all(isinstance(value, str) and value for value in values), f"Invalid {field}: {row['name']}"
            assert len(values) == len(set(values)), f"Duplicate {field} value: {row['name']}"
            if field in allowed:
                unknown = set(values) - allowed[field]
                assert not unknown, f"Unknown {field} facets for {row['name']}: {sorted(unknown)}"
        assert row["verification_level"] in allowed["verification_level"], row
        assert row["related_resource_ids"] == sorted(row["related_resource_ids"]), f"Unsorted related IDs: {rid}"
        assert rid not in row["related_resource_ids"], f"Self-related resource: {rid}"
        if row.get("project_id"):
            assert re.fullmatch(r"[a-z0-9][a-z0-9:/._-]*", row["project_id"]), row
        category_counts[row["category"]] = category_counts.get(row["category"], 0) + 1

    by_id = {row["resource_id"]: row for row in rows}
    for row in rows:
        for related_id in row["related_resource_ids"]:
            assert related_id in ids, f"Dangling related_resource_id {related_id} in {row['resource_id']}"
            sibling = by_id[related_id]
            assert row["resource_id"] in sibling["related_resource_ids"], f"Asymmetric related-resource link: {row['resource_id']} and {related_id}"

    with (ROOT / "resources.csv").open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        csv_rows = list(reader)
        csv_fields = reader.fieldnames or []
    assert len(csv_rows) == len(rows), "CSV and JSON record counts differ"
    assert csv_fields == FIELDS, "CSV columns differ from export schema"
    decoded = []
    for record in csv_rows:
        item = {}
        for field in FIELDS:
            value = record[field]
            if field in ARRAY_FIELDS:
                item[field] = json.loads(value)
            elif field in ("project_id", "discovery_source") and not value:
                continue
            else:
                item[field] = value
        decoded.append(item)
    assert decoded == rows, "CSV and JSON differ"

    for category, count in category_counts.items():
        category_id = re.sub(r"[^a-z0-9]+", "-", category.casefold()).strip("-")
        page = ROOT / "categories" / f"{category_id}.md"
        assert page.exists(), f"Missing category page: {page}"
        content = page.read_text(encoding="utf-8")
        category_rows = [row for row in rows if row["category"] == category]
        for row in category_rows:
            assert row["url"] in content, f"Category page misses {row['url']}"

    groups = read_json(ROOT / "index" / "project-groups.json")
    urls = {row["url"].strip().rstrip("/").casefold() for row in rows}
    group_ids, grouped_urls = set(), set()
    for group in groups["groups"]:
        assert re.fullmatch(r"project-[a-z0-9-]+", group["project_id"]), group
        assert group["project_id"] not in group_ids, f"Duplicate project group: {group['project_id']}"
        group_ids.add(group["project_id"])
        assert len(group["urls"]) >= 2, group
        for url in group["urls"]:
            normalized = url.strip().rstrip("/").casefold()
            assert normalized in urls, f"Project-group URL missing from catalog: {url}"
            assert normalized not in grouped_urls, f"URL appears in multiple project groups: {url}"
            grouped_urls.add(normalized)
            matches = [r for r in rows if r["url"].strip().rstrip("/").casefold() == normalized]
            assert all(r.get("project_id") == group["project_id"] for r in matches), f"Project ID mismatch for {url}"

    expected_categories, generated_section = render(rows)
    category_index = read_json(ROOT / "index" / "categories.json")
    assert category_index["categories"] == expected_categories, "index/categories.json is stale; run scripts/generate_indexes.py"
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    marker = re.search(re.escape(START) + r".*?" + re.escape(END), llms, re.S)
    assert marker, "llms.txt lacks generated category markers; run scripts/generate_indexes.py"
    assert marker.group(0) == generated_section.split("\n\n", 2)[2].rstrip(), "llms.txt category navigation is stale; run scripts/generate_indexes.py"

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        content = path.read_text(encoding="utf-8")
        assert not re.search(r"[A-Za-z]:[/\\]Users[/\\]", content), path
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            local = unquote(target.split("#")[0])
            assert (path.parent / local).exists(), (path, target)
    print(f"Validated {len(rows)} records, {len(category_counts)} categories, stable IDs/facets/relationships, generated indexes, CSV/JSON agreement, and local Markdown links.")


if __name__ == "__main__":
    validate()
