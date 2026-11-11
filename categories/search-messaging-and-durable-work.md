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

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [activemq](https://github.com/apache/activemq) | Apache ActiveMQ. |
| [Activiti](https://github.com/Activiti/Activiti) | Activiti is a light-weight workflow and Business Process Management (BPM) Platform targeted at business people, developers and system admins. Its core is a super-fast and rock-solid BPMN 2 process engine for Java. |
| [asynq](https://github.com/hibiken/asynq) | Simple, reliable, and efficient distributed task queue in Go. |
| [bull](https://github.com/OptimalBits/bull) | Premium Queue package for handling distributed jobs and messages in NodeJS. License not detected by GitHub; check the repository license before use. |
| [cadence](https://github.com/cadence-workflow/cadence) | Cadence is a distributed, scalable, durable, and highly available orchestration engine to execute asynchronous long-running business logic in a scalable and resilient way. |
| [camunda](https://github.com/camunda/camunda) | Agentic Orchestration Platform. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [conductor](https://github.com/Netflix/conductor) | Conductor is a microservices orchestration engine. |
| [conductor (conductor-oss)](https://github.com/conductor-oss/conductor) | Conductor is an event driven agentic workflow engine providing durable and highly resilient execution engine for applications and AI Agents. |
| [elasticsearch](https://github.com/elastic/elasticsearch) | Free and Open Source, Distributed, RESTful Search Engine. License not detected by GitHub; check the repository license before use. |
| [flowable engine](https://github.com/flowable/flowable-engine) | A compact and highly efficient workflow and Business Process Management (BPM) platform for developers, system admins and business users. |
| [kafka](https://github.com/apache/kafka) | Apache Kafka - A distributed event streaming platform. |
| [nats server](https://github.com/nats-io/nats-server) | High-Performance server for NATS.io, the cloud and edge native messaging system. |
| [nsq](https://github.com/nsqio/nsq) | A realtime distributed messaging platform. |
| [pulsar](https://github.com/apache/pulsar) | Apache Pulsar - distributed pub-sub messaging system. |
| [quickwit](https://github.com/quickwit-oss/quickwit) | Cloud-native OSS search engine for observability. |
| [rabbitmq server](https://github.com/rabbitmq/rabbitmq-server) | Open source RabbitMQ: core server and tier 1 (built-in) plugins. License not detected by GitHub; check the repository license before use. |
| [redpanda](https://github.com/redpanda-data/redpanda) | Redpanda is a streaming data platform for developers. Kafka API compatible. 10x faster. No ZooKeeper. No JVM! No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [resque](https://github.com/resque/resque) | Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later. |
| [restate](https://github.com/restatedev/restate) | Restate is the platform for building resilient applications that tolerate all infrastructure faults w/o the need for a PhD. License not detected by GitHub; check the repository license before use. |
| [river](https://github.com/riverqueue/river) | The polyglot queue: Fast and reliable background jobs in Go, Java, JS, Ruby, and Rust on Postgres/SQLite. MPL-2.0: file-level copyleft; modified files must be published. |
| [rq](https://github.com/rq/rq) | Simple job queues for Python. License not detected by GitHub; check the repository license before use. |
| [schema registry](https://github.com/confluentinc/schema-registry) | Confluent Schema Registry for Kafka. License not detected by GitHub; check the repository license before use. |
| [seatunnel](https://github.com/apache/seatunnel) | SeaTunnel is a multimodal, high-performance, distributed, massive data integration tool. |
| [sidekiq](https://github.com/sidekiq/sidekiq) | Simple, efficient background processing for Ruby. License not detected by GitHub; check the repository license before use. |
| [solr](https://github.com/apache/solr) | Apache Solr open-source search software. |
| [tantivy](https://github.com/quickwit-oss/tantivy) | Tantivy is a full-text search engine library inspired by Apache Lucene and written in Rust. |
| [typesense](https://github.com/typesense/typesense) | Open Source alternative to Algolia + Pinecone and an Easier-to-Use alternative to ElasticSearch Fast, typo tolerant, in-memory fuzzy Search Engine for building delightful search experiences. GPL-3.0: derivative works must stay under the GPL. |
| [vespa](https://github.com/vespa-engine/vespa) | The AI search platform. |
| [zeebe](https://github.com/camunda/camunda) | Agentic Orchestration Platform. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
<!-- expansion-2026-11-11:end -->
