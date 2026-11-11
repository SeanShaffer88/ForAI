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
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM: full control over SQL with a mature ecosystem; Alembic is its standard migration companion. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | Schema migrations for SQLAlchemy: autogenerates migration drafts from model changes — always review generated migrations before applying them to real data. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing: DataFrames for cleaning, joining, and analysing data in memory; very large data calls for Polars, DuckDB, or a database instead. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database for very fast aggregation queries over large event/analytics data; not a general-purpose transactional (OLTP) database. |

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

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [mikro-orm](https://github.com/mikro-orm/mikro-orm) | TypeScript ORM for Node.js based on Data Mapper, Unit of Work and Identity Map patterns. Supports MongoDB, MySQL, MariaDB, MS SQL Server, PostgreSQL and SQLite/libSQL databases. |
| [graphify](https://github.com/Graphify-Labs/graphify) | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store. |
| [zvec](https://github.com/alibaba/zvec) | A lightweight, lightning-fast, in-process vector database |
| [marimo](https://github.com/marimo-team/marimo) | A reactive notebook for Python — run reproducible experiments, query with SQL, execute as a script, deploy as an app, and version with git. Stored as pure Python. All in a modern, AI-native editor. |
| [sqlmodel](https://github.com/fastapi/sqlmodel) | SQL databases in Python, designed for simplicity, compatibility, and robustness. |
| [hydradb](https://github.com/hydra-db/hydradb) | HydraDB - fast graph database on object storage |
| [Better-Fullstack](https://github.com/Marve10s/Better-Fullstack) | Scaffold production-ready full-stack apps in TypeScript, Rust, Python, Go, and Java with a visual builder and CLI. Choose your frontend, backend, database, auth, AI, payments, and DevOps integrations, all wired together. |
| [acra](https://github.com/cossacklabs/acra) | Database security suite. Database proxy with field-level encryption, search through encrypted data, SQL injections prevention, intrusion detection, honeypots. Supports client-side and proxy-side ("transparent") encryption. SQL, NoSQL. |
| [go-sqlite3](https://github.com/ncruces/go-sqlite3) | Go bindings to SQLite using wasm2go |
| [requery](https://github.com/requery/requery) | requery - modern SQL based query & persistence for Java / Kotlin / Android |
| [arcadedb](https://github.com/ArcadeData/arcadedb) | ArcadeDB Multi-Model Database, one DBMS that supports SQL, Cypher, Gremlin, HTTP/JSON, MongoDB and Redis. ArcadeDB is a conceptual fork of OrientDB, the first Multi-Model DBMS. ArcadeDB supports Vector Embeddings. |
| [AnotherRedisDesktopManager](https://github.com/qishibo/AnotherRedisDesktopManager) | 🚀🚀🚀A faster, better and more stable Redis desktop manager [GUI client], compatible with Linux, Windows, Mac. |
| [SqlSugar](https://github.com/DotNetNext/SqlSugar) | .Net aot ORM SqlServer ORM Mongodb ORM MySql 瀚高 Postgresql ORM DB2 Hana 高斯 Duckdb C# VB.NET Sqlite ORM Oracle ORM Mysql Orm 虚谷数据库 达梦 ORM 人大金仓 ORM 神通ORM C# ORM , C# ORM .NET ORM NET9 ORM .NET8 ORM ClickHouse ORM QuestDb ,TDengine ORM,OceanBase ORM,GaussDB ORM,Tidb ORM Object/Relational Mapping |
| [DbUp](https://github.com/DbUp/DbUp) | DbUp is a .NET library that helps you to deploy changes to SQL Server databases. It tracks which SQL scripts have been run already, and runs the change scripts that are needed to get your database up to date. |
| [infinity](https://github.com/infiniflow/infinity) | The AI-native database built for LLM applications, providing incredibly fast hybrid search of dense vector, sparse vector, tensor (multi-vector), and full-text. |
| [kvrocks](https://github.com/apache/kvrocks) | Apache Kvrocks is a distributed key value NoSQL database that uses RocksDB as storage engine and is compatible with Redis protocol. |
| [codechecker](https://github.com/Ericsson/codechecker) | CodeChecker is an analyzer tooling, defect database and viewer extension for static and dynamic analyzer tools. |
| [trilogy](https://github.com/trilogy-libraries/trilogy) | Trilogy is a client library for MySQL-compatible database servers, designed for performance, flexibility, and ease of embedding. |
| [her](https://github.com/remi/her) | Her is an ORM (Object Relational Mapper) that maps REST resources to Ruby objects. It is designed to build applications that are powered by a RESTful API instead of a database. |
| [redis-objects](https://github.com/nateware/redis-objects) | Map Redis types directly to Ruby objects |
| [objectbox-dart](https://github.com/objectbox/objectbox-dart) | Flutter database for super-fast Dart object persistence |
| [laradock](https://github.com/laradock/laradock) | Full PHP development environment for Docker. Run Laravel, Symfony, CodeIgniter, Phalcon, WordPress, Drupal, Magento, Moodle, or any PHP project with 70+ pre-configured services: Nginx, Apache, PHP-FPM, MySQL, PostgreSQL, MongoDB, Redis, Elasticsearch & more. |
| [usql](https://github.com/xo/usql) | Universal command-line interface for SQL databases |
| [calibre-web](https://github.com/janeczku/calibre-web) | :books: Web app for browsing, reading and downloading eBooks stored in a Calibre database |
| [manticoresearch](https://github.com/manticoresoftware/manticoresearch) | Open-source search database for full-text, vector, and hybrid search with real-time indexing and SQL. |
| [warpgate](https://github.com/warp-tech/warpgate) | Fully transparent SSH, HTTPS, Kubernetes, database and RDP/VNC bastion/PAM that doesn't need additional client-side software |
| [wanderer](https://github.com/open-wanderer/wanderer) | wanderer is a self-hosted trail database. Save your adventures! |
| [redisson](https://github.com/redisson/redisson) | Redisson: Valkey & Redis Java Client and Real-Time Data Platform. Sync/Async/RxJava/Reactive API. Over 50 Valkey and Redis based Java objects and services: Set, Multimap, SortedSet, Map, List, Queue, Deque, Semaphore, Lock, AtomicLong, Map Reduce, Bloom filter, Spring, Tomcat, Scheduler, JCache API, Hibernate, RPC, local cache.. |
| [timescaledb](https://github.com/timescale/timescaledb) | A time-series database for high-performance real-time analytics packaged as a Postgres extension |
| [medis](https://github.com/luin/medis) | 💻 Medis is a beautiful, easy-to-use Mac database management application for Redis. |
| [beekeeper-studio](https://github.com/beekeeper-studio/beekeeper-studio) | Modern and easy to use SQL client for MySQL, Postgres, SQLite, SQL Server, and more. Linux, MacOS, and Windows. |

<!-- expansion-2026-11-10:begin -->
## Expansion — 2026-11-10

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-10.md).

| Resource | Useful for / constraints |
|---|---|
| [Trino](https://github.com/trinodb/trino) | Distributed SQL query engine over lakehouse, relational, and object-storage sources. Powerful for federated analytics; requires a cluster and connector-specific knowledge. |
| [Turso Database](https://github.com/tursodatabase/turso) | Rust rewrite of SQLite aiming for compatibility, with vector search and Postgres wire protocol as experimental work in progress. MIT; treat compatibility claims as target-state, not a drop-in guarantee. |
<!-- expansion-2026-11-10:end -->

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [asyncpg](https://github.com/MagicStack/asyncpg) | A fast PostgreSQL Database Client Library for Python/asyncio. |
| [chartdb](https://github.com/chartdb/chartdb) | Database diagrams editor that allows you to visualize and design your DB with a single query. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [cockroach](https://github.com/cockroachdb/cockroach) | CockroachDB — the cloud native, distributed SQL database designed for high availability, effortless scale, and control over data placement. License not detected by GitHub; check the repository license before use. |
| [dbal](https://github.com/doctrine/dbal) | Doctrine Database Abstraction Layer. |
| [dbeaver](https://github.com/dbeaver/dbeaver) | Free universal database tool and SQL client. |
| [diesel](https://github.com/diesel-rs/diesel) | A safe, extensible ORM and Query Builder for Rust. |
| [dolt](https://github.com/dolthub/dolt) | Dolt – Git for Data. |
| [doris](https://github.com/apache/doris) | Apache Doris is a real-time analytics and hybrid search database for AI agents. |
| [drizzle orm](https://github.com/drizzle-team/drizzle-orm) | ORM. |
| [ent](https://github.com/ent/ent) | An entity framework for Go. |
| [gorm](https://github.com/go-gorm/gorm) | The fantastic ORM library for Golang, aims to be developer friendly. |
| [HeidiSQL](https://github.com/HeidiSQL/HeidiSQL) | A lightweight client for managing MariaDB, MySQL, SQL Server, PostgreSQL, SQLite, Interbase and Firebird, written in Delphi and Lazarus/FreePascal. GPL-2.0: derivative works must stay under the GPL. |
| [knex](https://github.com/knex/knex) | A query builder for PostgreSQL, MySQL, CockroachDB, SQL Server, SQLite3 and Oracle, designed to be flexible, portable, and fun to use. |
| [kysely](https://github.com/kysely-org/kysely) | A type-safe TypeScript SQL query builder. |
| [mongo](https://github.com/mongodb/mongo) | The MongoDB Database. License not detected by GitHub; check the repository license before use. |
| [neo4j](https://github.com/neo4j/neo4j) | Graphs for Everyone. GPL-3.0: derivative works must stay under the GPL. |
| [node postgres](https://github.com/brianc/node-postgres) | PostgreSQL client for node.js. |
| [octosql](https://github.com/cube2222/octosql) | OctoSQL is a query tool that allows you to join, analyse and transform data from multiple databases and file formats using SQL. MPL-2.0: file-level copyleft; modified files must be published. |
| [postgres](https://github.com/postgres/postgres) | Mirror of the official PostgreSQL GIT repository. Note that this is just a *mirror* - we don't work with pull requests on github. To contribute, please see https://wiki.postgresql.org/wiki/Submitting_a_Patch. License not detected by GitHub; check the repository license before use. |
| [postgres (porsager)](https://github.com/porsager/postgres) | Postgres.js - The Fastest full featured PostgreSQL client. |
| [questdb](https://github.com/questdb/questdb) | QuestDB is a high performance, open-source, time-series database. |
| [sequelize](https://github.com/sequelize/sequelize) | Feature-rich ORM for modern Node.js and TypeScript, it supports PostgreSQL (with JSON and JSONB support), MySQL, MariaDB, SQLite, MS SQL Server, Snowflake, Oracle DB, DB2 and DB2 for IBM i. |
| [sql studio](https://github.com/frectonz/sql-studio) | SQL Database Explorer [SQLite, libSQL, PostgreSQL, MySQL/MariaDB, ClickHouse, DuckDB, Microsoft SQL Server]. |
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | Automatic SQL injection and database takeover tool. License not detected by GitHub; check the repository license before use. |
| [tidb](https://github.com/pingcap/tidb) | TiDB is built for agentic workloads that grow unpredictably, with ACID guarantees and native support for transactions, analytics, and vector search. No data silos. No noisy neighbors. No infrastructure ceiling. |
| [tortoise orm](https://github.com/tortoise/tortoise-orm) | Familiar asyncio ORM for python, built with relations in mind. |
| [typeorm](https://github.com/typeorm/typeorm) | TypeScript & JavaScript ORM for Node.js — supports PostgreSQL, MySQL, MariaDB, SQLite, SQL Server, Oracle, and more. |
<!-- expansion-2026-11-11:end -->
