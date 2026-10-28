# Cloud infrastructure and deployment

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs, one library per service; prefer these official clients over hand-rolled REST calls, and mind per-service versioning. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs (DNS, Workers, rules, zones) for automation; token-scoped — grant least-privilege permissions per zone or account. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment optimised for Next.js and frontend frameworks, with preview deployments per commit; serverless limits and pricing shape backend choices. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |

## AI expansion additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [Kubernetes documentation](https://kubernetes.io/docs/home/) | Concepts, kubectl reference, API reference. |

## AI expansion round 3 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [Modal](https://modal.com/docs) | Serverless GPU compute in Python: deploy model inference, batch jobs, and sandboxes without managing servers. |
| [RunPod](https://docs.runpod.io/) | GPU cloud (Pods and Serverless endpoints) commonly used for model hosting and fine-tuning runs. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [Argo CD](https://github.com/argoproj/argo-cd) | Reconcile Kubernetes applications from Git; protect repository credentials and synchronization policy. |
| [Flux](https://github.com/fluxcd/flux2) | GitOps controllers for Kubernetes; plan bootstrap, secret handling and reconciliation ownership. |
| [Kustomize](https://github.com/kubernetes-sigs/kustomize) | Compose Kubernetes configuration overlays; review generated manifests before applying them. |
| [Talos Linux](https://github.com/siderolabs/talos) | API-managed operating system for Kubernetes nodes; validate hardware and recovery procedures. |
| [Cilium](https://github.com/cilium/cilium) | Linux eBPF networking and policy for clusters; verify kernel and datapath requirements. |
| [Linkerd](https://github.com/linkerd/linkerd2) | Kubernetes service mesh capabilities; distinguish project code from supported binary distributions. |
| [cert-manager](https://github.com/cert-manager/cert-manager) | Automate Kubernetes certificate issuance and renewal; configure issuer access and renewal monitoring. |
| [Crossplane](https://github.com/crossplane/crossplane) | Manage infrastructure through Kubernetes APIs; review provider permissions and lifecycle policies. |
| [KEDA](https://github.com/kedacore/keda) | Scale Kubernetes workloads from event metrics; validate scaler authentication and queue semantics. |
| [Caddy](https://github.com/caddyserver/caddy) | HTTP serving and reverse proxying with certificate automation; review module trust and configuration. |

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [chroma](https://github.com/chroma-core/chroma) | Search infrastructure for AI: an open-source embedding database for retrieval (RAG) with a simple API; runs embedded for prototypes or as a server. |
| [memvid](https://github.com/memvid/memvid) | Memory layer for AI Agents. Replace complex RAG pipelines with a serverless, single-file memory layer. Give your agents instant retrieval and long-term memory. |
| [curvine](https://github.com/CurvineIO/curvine) | AI-Native & Cloud-Native FS: A high-performance file semantic layer for cloud object storage, integrated with high-speed cache. CNCF Sandbox Project. |
| [go-zero](https://github.com/zeromicro/go-zero) | A cloud-native Go microservices framework with cli tool for productivity. |
| [podinfo](https://github.com/stefanprodan/podinfo) | Go microservice template for Kubernetes |
| [dragonfly](https://github.com/dragonflyoss/dragonfly) | Delivers efficient, stable, and secure data distribution and acceleration powered by P2P technology, with an optional content‑addressable filesystem that accelerates OCI container launch. |
| [cli](https://github.com/create-go-app/cli) | ✨ A complete and self-contained solution for developers of any qualification to create a production-ready project with backend (Go), frontend (JavaScript, TypeScript) and deploy automation (Ansible, Docker) by running only one CLI command. |
| [orleans](https://github.com/dotnet/orleans) | Cloud Native application framework for .NET |
| [kamal](https://github.com/basecamp/kamal) | Deploy web apps anywhere: zero-downtime Docker deploys to plain servers from Basecamp; an alternative to managed PaaS and full Kubernetes. |
| [bosh](https://github.com/cloudfoundry/bosh) | Cloud Foundry BOSH is an open source tool chain for release engineering, deployment and lifecycle management of large scale distributed services. |
| [lazydocker](https://github.com/jesseduffield/lazydocker) | The lazier way to manage everything docker |
| [harbor](https://github.com/goharbor/harbor) | An open source trusted cloud native registry project that stores, signs, and scans content. |
| [docker-bench-security](https://github.com/docker/docker-bench-security) | The Docker Bench for Security is a script that checks for dozens of common best-practices around deploying Docker containers in production. |
| [falco](https://github.com/falcosecurity/falco) | Cloud Native Runtime Security: detects unexpected behaviour in Linux hosts and containers via system-call rules (CNCF project); a detection layer, not prevention. |
| [cri-o](https://github.com/cri-o/cri-o) | Open Container Initiative-based implementation of Kubernetes Container Runtime Interface |
| [acme-companion](https://github.com/nginx-proxy/acme-companion) | Automated ACME SSL certificate generation for nginx-proxy |
| [openwhisk](https://github.com/apache/openwhisk) | Apache OpenWhisk is an open source serverless cloud platform |
| [kraken](https://github.com/uber/kraken) | P2P Docker registry capable of distributing TBs of data in seconds |
| [docker-curriculum](https://github.com/prakhar1989/docker-curriculum) | :dolphin: A comprehensive tutorial on getting started with Docker! |
| [img](https://github.com/genuinetools/img) | Standalone, daemon-less, unprivileged Dockerfile and OCI compatible container image builder. |
| [nomad](https://github.com/hashicorp/nomad) | Nomad is an easy-to-use, flexible, and performant workload orchestrator that can deploy a mix of microservice, batch, containerized, and non-containerized applications. Nomad is easy to operate and scale and has native Consul and Vault integrations. |
| [gosu](https://github.com/tianon/gosu) | Simple Go-based setuid+setgid+setgroups+exec |
| [werf](https://github.com/werf/werf) | A solution for implementing efficient and consistent software delivery to Kubernetes facilitating best practices. |
| [preevy](https://github.com/livecycle/preevy) | Quickly deploy preview environments to the cloud! |
| [ofelia](https://github.com/mcuadros/ofelia) | A docker job scheduler (aka. crontab for docker) |
| [vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs |
| [copyparty](https://github.com/9001/copyparty) | Portable file server with accelerated resumable uploads, dedup, WebDAV, SFTP, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file |
| [glance](https://github.com/glanceapp/glance) | A self-hosted dashboard that puts all your feeds in one place |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 PDF Application on GitHub that lets you edit PDFs on any device anywhere |
| [apprise](https://github.com/caronc/apprise) | Apprise - Push Notifications that work with just about every platform! |
| [seerr](https://github.com/seerr-team/seerr) | Open-source media request and discovery manager for Jellyfin, Plex, and Emby. |
| [homer](https://github.com/bastienwirtz/homer) | A very simple static homepage for your server. |
| [2FAuth](https://github.com/Bubka/2FAuth) | A Web app to manage your Two-Factor Authentication (2FA) accounts and generate their security codes |
| [librephotos](https://github.com/LibrePhotos/librephotos) | A self-hosted open source photo management service. |
| [sanic](https://github.com/sanic-org/sanic) | Accelerate your web app development Build fast. Run fast. |
| [serverless](https://github.com/serverless/serverless) | ⚡ Serverless Framework – Effortlessly build apps that auto-scale, incur zero costs when idle, and require minimal maintenance using AWS Lambda and other managed cloud services. |
| [hyperf](https://github.com/hyperf/hyperf) | 🚀 A coroutine framework that focuses on hyperspeed and flexibility. Building microservice or middleware with ease. |
| [dex](https://github.com/dexidp/dex) | OpenID Connect (OIDC) identity and OAuth 2.0 provider with pluggable connectors |
| [nameko](https://github.com/nameko/nameko) | Python framework for building microservices |
| [swoft](https://github.com/swoft-cloud/swoft) | 🚀 PHP Microservice Full Coroutine Framework |
| [spin](https://github.com/spinframework/spin) | Spin is the open source developer tool for building and running serverless applications powered by WebAssembly. |
| [favbox](https://github.com/dd3v/favbox) | 🔖 FavBox is a local-first experimental browser extension that enhances and simplifies bookmark management without cloud storage or third-party services. |
