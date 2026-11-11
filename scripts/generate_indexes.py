"""Generate the category directory and its llms.txt navigation from resources.json."""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "resources.json"
CATEGORY_INDEX = ROOT / "index" / "categories.json"
CATEGORY_README = ROOT / "categories" / "README.md"
LLMS = ROOT / "llms.txt"
START = "<!-- BEGIN GENERATED CATEGORY INDEX -->"
END = "<!-- END GENERATED CATEGORY INDEX -->"

README_HEADER = """# Browse by purpose

These categories preserve the saved collections and dated expansions. Resources may appear in more than one category.

- **Start with one domain.** `../index/category-groups.json` rolls these categories up into 13 broad domains with counts.
- **Want the machine-readable form?** `../index/by-category/<category_id>.json` holds one category's records.
- **Need provenance?** `../resources.json` is canonical; the `../catalogs/` files keep the long-form notes and cautions.
- **Counts** are entries, not distinct projects: the same project can appear once per interface or audience.
- **One source of counts.** `../index/catalog-stats.json` is generated from `../resources.json`; quote it instead of counting records yourself.
"""


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


def render_readme(categories):
    return README_HEADER + "\n" + "".join(
        f"- [{item['title']}]({item['category_id']}.md) ({item['count']})\n"
        for item in categories
    )


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
    CATEGORY_README.write_text(render_readme(categories), encoding="utf-8")
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
    # Older generation runs inserted the section repeatedly; keep the first block.
    while len(re.findall(re.escape(START), text)) > 1:
        first = text.find(START)
        duplicate = text.find(START, first + len(START))
        block_end = text.find(END, duplicate) + len(END)
        text = text[:duplicate].rstrip("\n") + "\n" + text[block_end:].lstrip("\n")
    text = re.sub(r"(?:^## Categories\n\nThe linked JSON catalog is canonical; category pages are human-readable navigation views\.\n\n)+(?="
                  + re.escape(START) + ")", "## Categories\n\n", text, flags=re.M)
    LLMS.write_text(text.rstrip() + "\n", encoding="utf-8")
    print(f"Generated index/categories.json, categories/README.md, and llms.txt navigation for {len(categories)} categories.")


if __name__ == "__main__":
    main()
