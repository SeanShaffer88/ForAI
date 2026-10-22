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
