"""Generate the category directory and its llms.txt navigation from resources.json."""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "resources.json"
CATEGORY_INDEX = ROOT / "index" / "categories.json"
LLMS = ROOT / "llms.txt"
START = "<!-- BEGIN GENERATED CATEGORY INDEX -->"
END = "<!-- END GENERATED CATEGORY INDEX -->"


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def render(rows):
    groups = defaultdict(list)
    for row in rows:
        groups[row["category"]].append(row)
    categories = []
    for title, resources in sorted(groups.items(), key=lambda pair: pair[0].casefold()):
        category_id = slug(title)
        categories.append({
            "category_id": category_id,
            "title": title,
            "count": len(resources),
            "path": f"categories/{category_id}.md",
            "resource_ids": sorted(row["resource_id"] for row in resources),
        })
    content = (
        "## Categories\n\n"
        "The linked JSON catalog is canonical; category pages are human-readable navigation views.\n\n"
        f"{START}\n"
        + "".join(f"- [{item['title']}]({item['path']}) ({item['count']})\n" for item in categories)
        + f"{END}\n"
    )
    return categories, content


def main():
    rows = json.loads(RESOURCES.read_text(encoding="utf-8"))
    categories, section = render(rows)
    index = {
        "version": 1,
        "catalog": "../resources.json",
        "description": "Generated category navigation and stable resource membership for agents and local tools.",
        "categories": categories,
    }
    CATEGORY_INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    text = LLMS.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if pattern.search(text):
        text = pattern.sub(section.rstrip(), text, count=1)
    else:
        heading = "## Categories"
        position = text.find(heading)
        if position < 0:
            raise SystemExit("llms.txt has no '## Categories' section")
        next_section = text.find("\n## ", position + len(heading))
        if next_section < 0:
            next_section = len(text)
        text = text[:position] + section + "\n" + text[next_section:].lstrip("\n")
    LLMS.write_text(text.rstrip() + "\n", encoding="utf-8")
    print(f"Generated index/categories.json and llms.txt navigation for {len(categories)} categories.")


if __name__ == "__main__":
    main()
