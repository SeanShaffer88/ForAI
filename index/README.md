# Index artifacts

## Active catalog indexes

- [`../resources.json`](../resources.json) is the canonical resource catalog.
- [`resource-schema.json`](resource-schema.json) defines its active record contract.
- [`taxonomy.json`](taxonomy.json) defines the controlled discovery-facet vocabularies.
- [`categories.json`](categories.json) is generated navigation and resource membership, derived from the catalog.
- [`project-groups.json`](project-groups.json) records a small, explicitly reviewed set of non-GitHub URLs that refer to the same project. GitHub owner/repository identities are normalized by the enrichment script.

Regenerate the CSV and category navigation after catalog edits with `python scripts/export_csv.py` and `python scripts/generate_indexes.py`. Run `python scripts/validate.py` to check consistency. These scripts do not fetch URLs or certify current maintenance, security, license suitability, or compatibility.

## Retained legacy artifacts

The following files are preserved for provenance and historical reference. They do not define the active catalog and must not be merged into `resources.json` without record-by-record review:

- `../AI_INDEX.md` — references an older module layout, including paths that are not present.
- `master-manifest.json` — legacy manifest with stale counts and placeholder-like entries.
- `registry-schema.json` — describes an incompatible record model.
- `../manifests/resources.json` — a narrower historical Windows inventory referring to an older module layout.

Treat any legacy URLs, counts, paths, or classification as unverified until checked against current primary sources.
