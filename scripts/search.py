"""Search the catalog using only the Python standard library."""
import argparse, json
from pathlib import Path
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("query")
parser.add_argument("--category", default="")
parser.add_argument("--json", action="store_true")
args = parser.parse_args()
rows = json.loads((Path(__file__).resolve().parents[1] / "resources.json").read_text(encoding="utf-8"))
words = args.query.casefold().split()
results = [r for r in rows if args.category.casefold() in r["category"].casefold() and all(w in " ".join(r.values()).casefold() for w in words)]
if args.json:
    print(json.dumps(results, indent=2, ensure_ascii=False))
else:
    for r in results:
        print(f"{r['name']} [{r['category']}]\n  {r['url']}\n  {r['purpose']}")
    print(f"{len(results)} matching entries")
