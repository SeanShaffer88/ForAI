# Index artifacts

## Active catalog indexes

- [`../resources.json`](../resources.json) is the canonical resource catalog.
- [`resource-schema.json`](resource-schema.json) defines its active record contract.
- [`taxonomy.json`](taxonomy.json) defines the controlled discovery-facet vocabularies.
- [`categories.json`](categories.json) is generated navigation and resource membership, derived from the catalog.
- [`catalog-stats.json`](catalog-stats.json) is the generated count summary (records, distinct URLs, categories, domains, per-source breakdowns). Documentation quotes it instead of hard-coding numbers; refresh with `python scripts/catalog_stats.py --write`.
- [`project-groups.json`](project-groups.json) records a small, explicitly reviewed set of non-GitHub URLs that refer to the same project. GitHub owner/repository identities are normalized by the enrichment script.
- [`resources.compact.json`](resources.compact.json) is the full catalog with shortlisting fields only (~35% of the canonical file's size), and `by-category/` holds one compact JSON shard per category. [`category-groups.json`](category-groups.json) rolls the 101 categories up into 13 broad domains for navigation. All three are derived views, regenerated with `python scripts/generate_ai_views.py`.

Regenerate the CSV and category navigation after catalog edits with `python scripts/export_csv.py` and `python scripts/generate_indexes.py`. Run `python scripts/validate.py` to check consistency. These scripts do not fetch URLs or certify current maintenance, security, license suitability, or compatibility.

## Retained legacy artifacts

The following files were moved to `../archive/legacy-template/` (see its README) and are preserved for provenance and historical reference only. They do not define the active catalog and must not be merged into `resources.json` without record-by-record review:

- `../archive/legacy-template/AI_INDEX-original.md` — references an older module layout, including paths that are not present.
- `../archive/legacy-template/master-manifest.json` — legacy manifest with stale counts and placeholder entries.
- `../archive/legacy-template/registry-schema.json` — describes an incompatible record model.
- `../archive/legacy-template/manifests-resources.json` — a narrower historical Windows inventory referring to an older module layout.

Treat any legacy URLs, counts, paths, or classification as unverified until checked against current primary sources.
