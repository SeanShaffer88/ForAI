# Search messaging and durable work

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing, and analytics engine (the Apache-licensed fork of Elasticsearch 7.10); plan cluster sizing and memory before adopting for log or product search. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search API with typo-tolerant, fast indexing aimed at user-facing search boxes; simpler than Elasticsearch/OpenSearch, with fewer analytics features. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers for background jobs and scheduled tasks; needs a broker such as Redis or RabbitMQ and separate monitoring (e.g. Flower). |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing with retries, scheduling, and rate limiting; requires a running Redis instance. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET: runs jobs inside your app or a service with a dashboard; needs a SQL Server, Redis, or similar job store. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [Prefect](https://github.com/PrefectHQ/prefect) | Orchestrate Python workflows with retries and scheduling; distinguish local operation from hosted services. |
| [Dagster](https://github.com/dagster-io/dagster) | Model and operate data pipelines as assets; plan metadata storage and deployment. |
| [Apache Airflow](https://github.com/apache/airflow) | Schedule dependency-based workflows; Windows use is through WSL2 or Linux containers per upstream. Design idempotent tasks and operate the scheduler. |
| [Kestra](https://github.com/kestra-io/kestra) | Define event-driven workflows with declarative configuration; review plugin and edition requirements. |
| [Windmill](https://github.com/windmill-labs/windmill) | Turn scripts into jobs and workflows; licensing mixes AGPL, Apache and proprietary components, and distributed Community Edition binaries have additional terms. |
| [Hatchet](https://github.com/hatchet-dev/hatchet) | Run background tasks with durable orchestration; verify worker behavior and failure recovery. |
| [Inngest](https://github.com/inngest/inngest) | Event-driven durable functions; the server license includes SSPL-1.0 and an Apache future-license notice. Review server, SDK and hosted-service terms separately. |
| [Trigger.dev](https://github.com/triggerdotdev/trigger.dev) | Run background tasks from application code; evaluate worker deployment and resource limits. |
| [Argo Workflows](https://github.com/argoproj/argo-workflows) | Execute container workflows on Kubernetes; define artifact storage and service-account permissions. |
| [Luigi](https://github.com/spotify/luigi) | Build dependency-based batch pipelines in Python; design task completeness and idempotency. |

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [gulp](https://github.com/gulpjs/gulp) | A toolkit to automate & enhance your workflow |
| [enqueue-dev](https://github.com/php-enqueue/enqueue-dev) | Message Queue, Job Queue, Broadcasting, WebSockets packages for PHP, Symfony, Laravel, Magento. DEVELOPMENT REPOSITORY - provided by Forma-Pro |
