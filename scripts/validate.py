"""Validate local catalog consistency without network access."""
import csv, json, re
from pathlib import Path
from urllib.parse import urlsplit, unquote
root = Path(__file__).resolve().parents[1]
rows = json.loads((root / "resources.json").read_text(encoding="utf-8"))
with (root / "resources.csv").open(encoding="utf-8", newline="") as f:
    assert list(csv.DictReader(f)) == rows, "CSV and JSON differ"
assert rows, "Empty catalog"
seen = set()
for r in rows:
    assert all(r.get(k) for k in ("name", "url", "category", "purpose", "source", "checked_on", "review")), r
    u = urlsplit(r["url"])
    assert u.scheme == "https" and u.netloc, r
    key = (r["source"], r["name"], r["url"])
    assert key not in seen, key
    seen.add(key)
    slug = re.sub("[^a-z0-9]+", "-", r["category"].lower()).strip("-")
    page = root / "categories" / (slug + ".md")
    assert r["url"] in page.read_text(encoding="utf-8"), r
for path in root.rglob("*.md"):
    content = path.read_text(encoding="utf-8")
    assert not re.search(r"[A-Za-z]:[/\\]Users[/\\]", content), path
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
        if "://" in target or target.startswith("#") or target.startswith("mailto:"):
            continue
        local = unquote(target.split("#")[0])
        assert (path.parent / local).exists(), (path, target)
print(f"Validated {len(rows)} entries, {len({r['category'] for r in rows})} categories, CSV/JSON agreement and local links.")
