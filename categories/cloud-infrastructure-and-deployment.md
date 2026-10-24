# Cloud infrastructure and deployment

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
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
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
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
