"""Export the canonical resources.json catalog to a lossless CSV representation."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "resources.json"
OUTPUT = ROOT / "resources.csv"
FIELDS = [
    "name", "url", "category", "purpose", "source", "checked_on", "review", "http_status",
    "resource_id", "category_id", "resource_type", "topics", "use_cases", "languages",
    "platforms", "audiences", "related_resource_ids", "project_id", "verification_level",
    "discovery_source",
]
ARRAY_FIELDS = {"topics", "use_cases", "languages", "platforms", "audiences", "related_resource_ids"}


def export(rows):
    with OUTPUT.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=FIELDS, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            serialized = {}
            for field in FIELDS:
                value = row.get(field, "")
                if field in ARRAY_FIELDS:
                    value = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
                serialized[field] = value
            writer.writerow(serialized)


def main():
    rows = json.loads(RESOURCES.read_text(encoding="utf-8"))
    export(rows)
    print(f"Exported {len(rows)} catalog entries to resources.csv.")


if __name__ == "__main__":
    main()
