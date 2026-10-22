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
