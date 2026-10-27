"""Rank catalog resources using only the Python standard library.

Free-text search covers descriptive fields and curated facets only. Review notes,
HTTP checks, and collection provenance are intentionally excluded to prevent
boilerplate from making unrelated records look relevant.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r"[a-z0-9][a-z0-9+#.-]*", re.I)
WEIGHTS = {
    "name": 10,
    "purpose": 5,
    "category": 4,
    "topics": 3,
    "use_cases": 3,
    "resource_type": 2,
    "languages": 2,
    "platforms": 2,
    "audiences": 1,
}


def field_text(resource, field):
    value = resource.get(field, "")
    if isinstance(value, list):
        return " ".join(str(item) for item in value).casefold()
    return str(value).casefold()


def contains_term(term, text):
    tokens = TOKEN.findall(text)
    return any(token == term or (min(len(token), len(term)) >= 4 and (token.startswith(term) or term.startswith(token))) for token in tokens)


def facet_values(resource, field):
    value = resource.get(field, [])
    return [value] if isinstance(value, str) else value or []


def rank_results(rows, query, *, category="", topic="", resource_type="", use_case="", language="", platform=""):
    """Filter and rank results; all query terms must match searchable fields."""
    terms = [term.casefold() for term in TOKEN.findall(query)]
    if not terms:
        return []
    filters = {
        "topics": topic,
        "resource_type": resource_type,
        "use_cases": use_case,
        "languages": language,
        "platforms": platform,
    }
    results = []
    for row in rows:
        if category and category.casefold() not in field_text(row, "category"):
            continue
        if any(value and value.casefold() not in {str(v).casefold() for v in facet_values(row, field)} for field, value in filters.items()):
            continue
        searchable = {field: field_text(row, field) for field in WEIGHTS}
        if any(not any(contains_term(term, text) for text in searchable.values()) for term in terms):
            continue
        score = sum(max((weight for field, weight in WEIGHTS.items() if contains_term(term, searchable[field])), default=0) for term in terms)
        results.append((score, row))
    results.sort(key=lambda item: (-item[0], item[1].get("name", "").casefold(), item[1].get("resource_id", "")))
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="all terms must match searchable catalog fields")
    parser.add_argument("--category", default="", help="category name substring")
    parser.add_argument("--topic", default="", help="exact topic facet")
    parser.add_argument("--type", dest="resource_type", default="", help="exact resource type facet")
    parser.add_argument("--use-case", default="", help="exact use-case facet")
    parser.add_argument("--language", default="", help="exact language facet")
    parser.add_argument("--platform", default="", help="exact platform facet")
    parser.add_argument("--limit", type=int, default=0, help="maximum results; 0 means no limit")
    parser.add_argument("--json", action="store_true", help="print matching resource records as JSON")
    args = parser.parse_args()
    if args.limit < 0:
        parser.error("--limit must be zero or greater")
    rows = json.loads((ROOT / "resources.json").read_text(encoding="utf-8"))
    results = rank_results(
        rows, args.query, category=args.category, topic=args.topic,
        resource_type=args.resource_type, use_case=args.use_case,
        language=args.language, platform=args.platform,
    )
    if args.limit:
        results = results[:args.limit]
    records = [row for _, row in results]
    if args.json:
        print(json.dumps(records, indent=2, ensure_ascii=False))
    else:
        for score, row in results:
            print(f"{row['name']} [{row['category']}] (relevance {score})\n  {row['url']}\n  {row['purpose']}")
        print(f"{len(results)} matching entries")


if __name__ == "__main__":
    main()
