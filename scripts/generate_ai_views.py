"""Generate AI-optimized views from the canonical resources.json.

Outputs (derived only; resources.json stays canonical):
- index/resources.compact.json  one-line-per-record catalog with only the
  fields an AI needs to shortlist (id, name, url, category, purpose, facets).
  Drops review/source/checked_on/http_status boilerplate.
- index/by-category/<category_id>.json  the compact records for one
  category, so an agent can load a single topic instead of the whole catalog.
- index/category-groups.json  the 97 categories rolled up into broad
  domains for navigation.

Run after any catalog edit:  python scripts/generate_ai_views.py
"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEEP = ["resource_id", "name", "url", "category_id", "purpose",
        "resource_type", "topics", "use_cases", "languages", "platforms"]


def group_for(category_id):
    cid = category_id
    if cid.startswith("windows-"):
        return "windows"
    if cid.startswith("ai-"):
        return "ai"
    if "security" in cid:
        return "security"
    if "test" in cid:
        return "testing-quality"
    if any(k in cid for k in ("cloud", "infrastructure", "ci-", "builds-", "deployment")):
        return "cloud-infra-devops"
    if any(k in cid for k in ("data", "database", "search-messaging")):
        return "data"
    if any(k in cid for k in ("design", "ui-", "accessibility")):
        return "design-ux"
    if any(k in cid for k in ("language", "python-rust", "niche-language", "webassembly")):
        return "languages-runtimes"
    if any(k in cid for k in ("web-", "api-", "net-application", "integration-", "software-architecture")):
        return "web-api-architecture"
    if any(k in cid for k in ("desktop-mobile", "platform-sdks", "android")):
        return "desktop-mobile"
    if any(k in cid for k in ("game", "graphics", "documents", "collaboration", "world-of-warcraft")):
        return "media-games-docs"
    return "operations-tools"


def main():
    rows = json.loads((ROOT / "resources.json").read_text(encoding="utf-8"))
    compact = [{k: row[k] for k in KEEP} for row in rows]
    (ROOT / "index" / "resources.compact.json").write_text(
        json.dumps(compact, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8")

    by_category = defaultdict(list)
    for record in compact:
        by_category[record["category_id"]].append(record)
    shard_dir = ROOT / "index" / "by-category"
    shard_dir.mkdir(exist_ok=True)
    for stale in shard_dir.glob("*.json"):
        if stale.stem not in by_category:
            stale.unlink()
    for category_id, items in sorted(by_category.items()):
        (shard_dir / f"{category_id}.json").write_text(
            json.dumps(items, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8")

    groups = {}
    for record in rows:
        group = groups.setdefault(group_for(record["category_id"]),
                                  {"categories": set(), "count": 0})
        group["categories"].add(record["category_id"])
        group["count"] += 1
    doc = {
        "version": 1,
        "description": ("Rollup of the catalog categories into broad domains "
                        "for AI navigation. Pick a domain, then open only "
                        "that domain's category shards in index/by-category/. "
                        "Derived from resources.json by "
                        "scripts/generate_ai_views.py; adds grouping only."),
        "groups": {name: {"category_ids": sorted(g["categories"]),
                          "category_count": len(g["categories"]),
                          "resource_count": g["count"]}
                   for name, g in sorted(groups.items())},
    }
    (ROOT / "index" / "category-groups.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated compact catalog ({len(compact)} records), "
          f"{len(by_category)} category shards, "
          f"{len(doc['groups'])} domain groups.")


if __name__ == "__main__":
    main()
