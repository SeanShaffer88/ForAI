# Feature flags configuration and secrets

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [OpenFeature](https://openfeature.dev/docs/reference/intro/) | Vendor-neutral feature-flag SDK interfaces; a provider supplies evaluation. |
| [Unleash](https://docs.getunleash.io/) | Feature-flag server and client SDKs; choose server/client evaluation boundaries. |
| [LaunchDarkly SDKs](https://launchdarkly.com/docs/sdk) | Hosted feature management SDKs; review account, pricing and data exposure. |
| [SOPS](https://getsops.io/) | Encrypted configuration files using key-management backends; plan key access and recovery. |
| [age](https://age-encryption.org/) | File encryption and recipient-based key tooling; manage private keys separately. |
| [Infisical](https://infisical.com/docs) | Secrets management and SDKs; review deployment model and edition boundaries. |
| [OpenBao](https://openbao.org/docs/) | Secrets and identity-based credential services; plan storage, unsealing and recovery. |
| [External Secrets Operator](https://external-secrets.io/) | Synchronize external secrets into Kubernetes; check refresh behavior and permissions. |
| [1Password SDKs](https://developer.1password.com/docs/sdks/) | Application access to vault items; confirm supported language and service-account scope. |

<!-- expansion-2026-11-10:begin -->
## Expansion — 2026-11-10

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-10.md).

| Resource | Useful for / constraints |
|---|---|
| [HashiCorp Vault](https://github.com/hashicorp/vault) | Secrets management, dynamic credentials, encryption as a service, and PKI. Business Source License since 2023 with OpenBao as the open fork; evaluate licensing before embedding it in a product. |
<!-- expansion-2026-11-10:end -->

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [clients](https://github.com/bitwarden/clients) | Bitwarden client apps (web, browser extension, desktop, and cli). License not detected by GitHub; check the repository license before use. |
| [detect secrets](https://github.com/Yelp/detect-secrets) | An enterprise friendly way of detecting and preventing secrets in code. |
| [dotenv](https://github.com/motdotla/dotenv) | Loads environment variables from .env for nodejs projects. |
| [dotenvx](https://github.com/dotenvx/dotenvx) | a secure dotenv—from the creator of `dotenv`. |
| [flagd](https://github.com/open-feature/flagd) | A feature flag daemon with a Unix philosophy. |
| [flagsmith](https://github.com/Flagsmith/flagsmith) | Flagsmith is an open-source feature flag platform with remote config, experimentation, and self-hosted or cloud deployment options. |
| [ggshield](https://github.com/GitGuardian/ggshield) | Detect and validate 500+ types of hardcoded secrets with advanced checks. Use it as a pre-commit hook, GitHub Action, or CLI for proactive secret detection and security. |
| [gopass](https://github.com/gopasspw/gopass) | The slightly more awesome standard unix password manager for teams. |
| [growthbook](https://github.com/growthbook/growthbook) | Open Source Feature Flags, Experimentation, and Product Analytics. License not detected by GitHub; check the repository license before use. |
| [posthog](https://github.com/PostHog/posthog) | hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs,. License not detected by GitHub; check the repository license before use. |
| [server](https://github.com/bitwarden/server) | Bitwarden infrastructure/backend (API, database, Docker, etc). License not detected by GitHub; check the repository license before use. |
| [spec](https://github.com/open-feature/spec) | OpenFeature specification. |
| [zookeeper](https://github.com/apache/zookeeper) | Apache ZooKeeper. |
<!-- expansion-2026-11-11:end -->
