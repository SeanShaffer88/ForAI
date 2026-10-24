# Security identity and supply chain

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [Syft](https://github.com/anchore/syft) | Generate software bills of materials from images and filesystems; inspect package coverage. |
| [Grype](https://github.com/anchore/grype) | Match discovered packages against vulnerability data; triage findings and refresh the database. |
| [Checkov](https://github.com/bridgecrewio/checkov) | Static policy checks for infrastructure definitions; tune policies for the target environment. |
| [zizmor](https://github.com/zizmorcore/zizmor) | Audit GitHub Actions workflow security; inspect findings in the context of repository permissions. |
| [actionlint](https://github.com/rhysd/actionlint) | Check GitHub Actions workflow syntax and expressions; external action behavior still needs review. |
| [in-toto](https://github.com/in-toto/in-toto) | Record and verify software supply-chain steps; define trusted identities and verification policy. |
| [GUAC](https://github.com/guacsec/guac) | Connect software supply-chain metadata into a graph; ingestion quality affects conclusions. |
| [TruffleHog](https://github.com/trufflesecurity/trufflehog) | Detect exposed secrets in authorized sources; verification may contact external services. |
| [Dependency-Track](https://github.com/DependencyTrack/dependency-track) | Track component risk from SBOMs; the README places v4 in maintenance mode with December 2026 end-of-life. Review v5 migration and versioned docs. |
| [Kyverno](https://github.com/kyverno/kyverno) | Kubernetes admission and policy automation; test enforcement and failure behavior before rollout. |
| [step CLI](https://github.com/smallstep/cli) | Inspect certificates and work with PKI workflows; configure trust roots and key storage deliberately. |
| [OAuth2 Proxy](https://github.com/oauth2-proxy/oauth2-proxy) | Add identity-provider authentication in front of web services; validate proxy trust and cookie settings. |
| [Ory Kratos](https://github.com/ory/kratos) | Operate application identity and user-management flows; deployment still needs secure session configuration. |
| [Casbin](https://github.com/apache/casbin) | Embed authorization policy evaluation; model tenant boundaries and test permission rules. |
