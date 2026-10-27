# Contributing

Add resources that solve a concrete development need. Prefer canonical upstream links and concise original descriptions: what it is useful for, where it fits, and meaningful constraints. Inclusion is not an endorsement or adoption audit.

Update the appropriate full catalog and `resources.json`, preserving each existing record and its provenance. For new records, provide the original evidence and descriptions; generate stable IDs and conservative derived facets with `python scripts/enrich_resources.py --apply`, then regenerate `resources.csv` with `python scripts/export_csv.py` and navigation with `python scripts/generate_indexes.py`. Use `index/resource-schema.json` and `index/taxonomy.json` as the active metadata contract. Do not assign unsupported language/platform claims; leave uncertain facets empty or flag them for review. `scripts/enrich_resources.py --check` verifies the derived metadata is present; the explicit `--refresh-topics`, `--refresh-types`, and `--refresh-verification` modes recalculate only those derived fields when their rules change. Preserve different interfaces to the same project when they serve different purposes; do not count raw entries as unique projects. Category page names should be lowercase hyphenated names.

Record the date, source, and scope of actual verification. A successful HTTP request only verifies reachability. Label archived, dormant, unmaintained, mirrored, or service-bound resources honestly and cite upstream evidence. Describe a potential revival separately from a tested release. Keep existing WR task IDs stable; the included backlog is a dated snapshot, not a promise of ongoing project work.

Do not include credentials, private account information, local machine paths, copied upstream documentation, or dependencies themselves. Linked projects keep their own licenses.

Run `python scripts/validate.py` before proposing a change. It checks index agreement, required fields, URL syntax, category coverage, local Markdown links, and accidental local paths. It does not perform network or adoption audits.
