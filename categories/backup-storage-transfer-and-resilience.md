# Backup storage transfer and resilience

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [restic](https://restic.readthedocs.io/en/stable/) | Encrypted versioned backups; test restores and protect repository credentials. |
| [rclone](https://rclone.org/docs/) | Transfer and synchronize data across storage providers; distinguish sync from versioned backup. |
| [Kopia](https://kopia.io/docs/) | Snapshot backup and encryption; validate retention and restore behavior. |
| [Litestream](https://litestream.io/) | Continuous SQLite replication for recovery; not multi-writer database replication. |
| [SQLite Online Backup API](https://www.sqlite.org/backup.html) | Consistent SQLite backup mechanism for application integration. |
| [Apache Iceberg](https://iceberg.apache.org/docs/latest/) | Analytical table format with schema/snapshot evolution; needs compatible engines and catalog. |
| [Delta Lake](https://docs.delta.io/) | Transactional analytical tables; check reader/writer protocol compatibility. |
| [Apache Parquet](https://parquet.apache.org/docs/) | Columnar file format and interoperability reference; check logical types and codecs. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [SeaweedFS](https://github.com/seaweedfs/seaweedfs) | Operate distributed file and object storage; test replication, consistency and recovery needs. |
| [JuiceFS](https://github.com/juicedata/juicefs) | Provide a filesystem backed by object storage; plan metadata services and cache behavior. |
| [Rook](https://github.com/rook/rook) | Operate storage systems through Kubernetes operators; understand the underlying storage engine. |
| [Longhorn](https://github.com/longhorn/longhorn) | Provide replicated Kubernetes block storage; validate disk, network and recovery requirements. |
| [Velero](https://github.com/velero-io/velero) | Back up and restore Kubernetes resources and volumes; test application-consistent recovery. |
| [BorgBackup](https://github.com/borgbackup/borg) | Deduplicated encrypted backups; the default-branch README warns that Borg2 is unstable beta and unsuitable for production backups. Select stable versioned releases and test restores. |
| [borgmatic](https://projects.torsion.org/borgmatic-collective/borgmatic) | Configure and automate Borg backups; use the primary Forgejo source. GitHub is an upstream-declared read-only mirror; review hooks and database consistency. |
| [Duplicati](https://github.com/duplicati/duplicati) | Encrypted remote backups; core source is MIT with proprietary-directory exceptions. Review bundled components and test restoration and retention. |
| [Syncthing](https://github.com/syncthing/syncthing) | Synchronize files between devices; synchronization needs a separate deletion and backup policy. |
| [bup](https://github.com/bup/bup) | Store incremental backups using content-addressed structures; verify platform and restore tooling. |
