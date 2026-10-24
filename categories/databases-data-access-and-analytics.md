# Databases data access and analytics

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [Ibis](https://github.com/ibis-project/ibis) | Portable Python expressions over analytic backends; check backend-specific operation support. |
| [Apache DataFusion](https://github.com/apache/datafusion) | Embed a Rust query engine using Arrow; assess query coverage and memory management. |
| [Dask](https://github.com/dask/dask) | Parallel Python arrays and dataframes; account for scheduler overhead and partition sizing. |
| [dlt](https://github.com/dlt-hub/dlt) | Python data ingestion with schema handling; inspect destination behavior and credential scopes. |
| [Great Expectations](https://github.com/fivetran/great_expectations) | Define data expectations and validation reports; distinguish core tooling from hosted services. |
| [Pandera](https://github.com/unionai-oss/pandera) | Validate dataframe schemas and properties; check the selected dataframe backend. |
| [dbt](https://github.com/dbt-labs/dbt) | Version and test SQL transformations; the renamed repository has Rust-based v2 on main and Python v1 on 1.latest. Check migration and adapter support. |
| [SQLFluff](https://github.com/sqlfluff/sqlfluff) | Lint and format SQL; configure the correct dialect and templating engine. |
| [Apache Flink](https://github.com/apache/flink) | Stateful stream and batch processing; plan checkpointing, state recovery and cluster operations. |
| [Apache Beam](https://github.com/apache/beam) | Portable data pipelines; runner capabilities and deployment requirements differ. |
