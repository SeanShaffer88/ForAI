"""Derive conservative related-entry links and fill empty topics.

Two derived-data passes over resources.json, both deliberately
conservative so the output stays trustworthy as AI navigation:

1. Empty `topics`: a record with no topics inherits a topic only when at
   least 60% of its category siblings that do carry topics carry it too
   (max 2 topics). Anything less clear is left empty.
2. `related_resource_ids`: records in the same category are scored by
   shared topics (x2), shared use cases (x1), and same resource type
   (x0.5). Each record keeps its top 3 neighbours scoring >= 3; edges are
   then made symmetric (the validator requires symmetry) and capped at
   6 per record, dropping asymmetric edges after the cap.

Existing non-empty topics and any pre-existing related links are kept;
this script only adds. Run after catalog edits, then regenerate the CSV
and AI views and run scripts/validate.py.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "resources.json"


def fill_topics(rows):
    by_cat = defaultdict(list)
    for row in rows:
        by_cat[row["category_id"]].append(row)
    filled = 0
    for members in by_cat.values():
        topical = [m for m in members if m["topics"]]
        if len(topical) < 3:
            continue
        counts = Counter(t for m in topical for t in m["topics"])
        majority = [t for t, c in counts.most_common()
                    if c / len(topical) >= 0.6][:2]
        if not majority:
            continue
        for m in members:
            if not m["topics"]:
                m["topics"] = majority
                filled += 1
    return filled


def score(a, b):
    return (2 * len(set(a["topics"]) & set(b["topics"]))
            + len(set(a["use_cases"]) & set(b["use_cases"]))
            + (0.5 if a["resource_type"] == b["resource_type"] else 0))


def build_related(rows):
    by_cat = defaultdict(list)
    for row in rows:
        by_cat[row["category_id"]].append(row)
    edges = defaultdict(dict)  # id -> {other_id: score}
    for members in by_cat.values():
        for a in members:
            scored = sorted(
                ((score(a, b), b["resource_id"]) for b in members
                 if b is not a),
                reverse=True)
            for s, other in scored[:3]:
                if s >= 3:
                    edges[a["resource_id"]][other] = s
    # Symmetrize by union, cap at 6 keeping strongest, then drop
    # any edge that is no longer mutual.
    sym = defaultdict(dict)
    for a, others in edges.items():
        for b, s in others.items():
            sym[a][b] = max(s, sym[a].get(b, 0))
            sym[b][a] = max(s, sym[b].get(a, 0))
    for a in list(sym):
        if len(sym[a]) > 6:
            keep = sorted(sym[a].items(), key=lambda kv: -kv[1])[:6]
            sym[a] = dict(keep)
    final = defaultdict(set)
    for a, others in sym.items():
        for b in others:
            if a in sym.get(b, {}):
                final[a].add(b)
    linked = 0
    for row in rows:
        merged = sorted(set(row["related_resource_ids"]) | final[row["resource_id"]])
        if merged != row["related_resource_ids"]:
            linked += 1
        row["related_resource_ids"] = merged
    return linked


def main():
    rows = json.loads(CATALOG.read_text(encoding="utf-8"))
    filled = fill_topics(rows)
    linked = build_related(rows)
    CATALOG.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
    total_related = sum(1 for r in rows if r["related_resource_ids"])
    print(f"Filled topics on {filled} records; related links now on "
          f"{total_related} records ({linked} changed).")


if __name__ == "__main__":
    main()
