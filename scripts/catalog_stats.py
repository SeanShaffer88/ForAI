"""Print (and optionally write) one canonical set of catalog statistics.

Every human-facing document that quotes counts should read them from
`index/catalog-stats.json` instead of hard-coding a number, so the count can
never drift from `resources.json` again.

Usage:
    python scripts/catalog_stats.py            # print the summary
    python scripts/catalog_stats.py --write    # write index/catalog-stats.json
    python scripts/catalog_stats.py --check     # fail if the file is stale
"""
import argparse
import collections
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "resources.json"
OUTPUT = ROOT / "index" / "catalog-stats.json"
STATS_URL = "index/catalog-stats.json"


def slug(value):
    import re
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def build(rows):
    categories = collections.Counter(row["category"] for row in rows)
    groups_path = ROOT / "index" / "category-groups.json"
    domains = []
    if groups_path.exists():
        groups = json.loads(groups_path.read_text(encoding="utf-8"))["groups"]
        for name, group in sorted(groups.items(), key=lambda pair: (-pair[1]["resource_count"], pair[0])):
            domains.append({
                "domain": name,
                "resource_count": group["resource_count"],
                "category_count": group["category_count"],
            })
    canonical_bytes = RESOURCES.stat().st_size
    compact_bytes = (ROOT / "index" / "resources.compact.json").stat().st_size
    windows = {name: count for name, count in categories.items() if name.startswith("Windows /")}
    return {
        "version": 1,
        "description": (
            "Generated counts for the whole repository. Documentation should quote these values "
            "instead of hard-coding them; regenerate with scripts/catalog_stats.py --write and "
            "verify with scripts/catalog_stats.py --check."
        ),
        "generated_from": "resources.json",
        "records": len(rows),
        "distinct_urls": len({row["url"].rstrip("/").casefold() for row in rows}),
        "distinct_projects": len({row["project_id"] for row in rows if row.get("project_id")}),
        "categories": len(categories),
        "windows_categories": len(windows),
        "windows_records": sum(windows.values()),
        "domains": len(domains),
        "domain_rollup": domains,
        "by_source": dict(sorted(collections.Counter(row["source"] for row in rows).items())),
        "by_resource_type": dict(sorted(collections.Counter(row["resource_type"] for row in rows).items())),
        "largest_categories": [
            {"category": name, "category_id": slug(name), "count": count}
            for name, count in sorted(categories.items(), key=lambda pair: (-pair[1], pair[0].casefold()))[:15]
        ],
        "sizes_bytes": {
            "resources.json": canonical_bytes,
            "index/resources.compact.json": compact_bytes,
            "llms-full.txt": (ROOT / "llms-full.txt").stat().st_size if (ROOT / "llms-full.txt").exists() else 0,
            "compact_percent_of_canonical": round(100 * compact_bytes / canonical_bytes, 1),
        },
    }


START = "<!-- BEGIN GENERATED STATS -->"
END = "<!-- END GENERATED STATS -->"
SYNCED = ("README.md", "AI_INDEX.md", "llms.txt")


def sentence(stats):
    return (
        f"**{stats['records']:,} catalog entries** · **{stats['distinct_urls']:,} distinct URLs** · "
        f"**{stats['categories']} categories** · **{stats['domains']} domains** · "
        f"**{stats['distinct_projects']:,} project identities**"
    )


def block(stats):
    return f"{START}\n{sentence(stats)}\n{END}"


def sync_documents(stats):
    """Replace the generated stats block in every synced document."""
    import re
    changed = []
    for relative in SYNCED:
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if START not in text:
            continue
        updated = re.sub(re.escape(START) + r".*?" + re.escape(END), block(stats), text, count=1, flags=re.S)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed.append(relative)
    return changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true", help="write index/catalog-stats.json")
    group.add_argument("--check", action="store_true", help="fail if index/catalog-stats.json is stale")
    args = parser.parse_args()

    rows = json.loads(RESOURCES.read_text(encoding="utf-8"))
    stats = build(rows)
    if args.write:
        OUTPUT.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {STATS_URL}.")
    if args.check:
        current = json.loads(OUTPUT.read_text(encoding="utf-8")) if OUTPUT.exists() else None
        if current != stats:
            sys.exit(f"{STATS_URL} is stale; run python scripts/catalog_stats.py --write")
        print(f"{STATS_URL} is current.")

    size_mb = stats["sizes_bytes"]["resources.json"] / (1024 * 1024)
    print(
        f"{stats['records']:,} records · {stats['distinct_urls']:,} distinct URLs · "
        f"{stats['categories']} categories · {stats['domains']} domains · "
        f"{stats['distinct_projects']:,} project identities"
    )
    print(
        f"resources.json {size_mb:.1f} MB; compact view "
        f"{stats['sizes_bytes']['compact_percent_of_canonical']}% of canonical size; "
        f"llms-full.txt {stats['sizes_bytes']['llms-full.txt'] / (1024 * 1024):.1f} MB"
    )


if __name__ == "__main__":
    main()
