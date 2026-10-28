# Security identity and supply chain

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference: the OWASP API Security Top 10 and guidance; a checklist for design reviews, not a scanner. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation server (OIDC, SAML, social login) from Red Hat; powerful, but you own its hosting, upgrades, and database. |
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

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | A list of useful payloads and bypass for Web Application Security and Pentest/CTF |
| [maigret](https://github.com/soxoj/maigret) | 🕵️‍♂️ Collect a dossier on a person by username from 6K websites |
| [fingerprintjs](https://github.com/fingerprintjs/fingerprintjs) | The most advanced free and open-source browser fingerprinting library |
| [RustScan](https://github.com/bee-san/RustScan) | The modern port scanner (Rust): finds open ports fast, then hands off to Nmap for service detection; scan only systems you own or are authorised to test. |
| [android-security-awesome](https://github.com/ashishb/android-security-awesome) | A collection of android security related resources |
| [mastg](https://github.com/OWASP/mastg) | The OWASP Mobile Application Security Testing Guide (MASTG) is a comprehensive manual for mobile app security testing and reverse engineering. It describes technical processes for verifying the OWASP Mobile Security Weakness Enumeration (MASWE) weaknesses, which are in alignment with the OWASP MASVS. |
| [crowdsec](https://github.com/crowdsecurity/crowdsec) | Open-source IDS/IPS, WAF and bot detection for Linux, Windows, Docker and Kubernetes, with a crowdsourced blocklist of malicious IPs. |
| [arkime](https://github.com/arkime/arkime) | Arkime is an open source, large scale, full packet capturing, indexing, and database system. |
| [bunkerweb](https://github.com/bunkerity/bunkerweb) | 🛡️ Open-source and cloud-native Web Application Firewall (WAF) |
| [firezone](https://github.com/firezone/firezone) | Blazing-fast remote access: a WireGuard-based VPN/ZTNA alternative to legacy corporate VPNs; self-hostable, with a managed cloud option. |
| [Sublist3r](https://github.com/aboul3la/Sublist3r) | Fast subdomains enumeration tool for penetration testers |
| [tfsec](https://github.com/aquasecurity/tfsec) | tfsec is now part of Trivy: Terraform security scanning has moved into Trivy — use Trivy for new work and treat tfsec as archived guidance. |
| [SecretScanner](https://github.com/deepfence/SecretScanner) | :unlock: :unlock: Find secrets and passwords in container images and file systems :unlock: :unlock: |
| [axiom](https://github.com/pry0cc/axiom) | The dynamic infrastructure framework for everybody! Distribute the workload of many different scanning tools with ease, including nmap, ffuf, masscan, nuclei, meg and many more! |
| [recon-ng](https://github.com/lanmaster53/recon-ng) | Open Source Intelligence gathering tool aimed at reducing the time spent harvesting information from open sources. |
| [monkey](https://github.com/guardicore/monkey) | Infection Monkey - An open-source adversary emulation platform |
| [frida](https://github.com/frida/frida) | Frida main repo for hosting release binaries: a dynamic instrumentation toolkit for observing and modifying running apps; use only on software you own or are authorised to test. |
| [kics](https://github.com/Checkmarx/kics) | Find security vulnerabilities, compliance issues, and infrastructure misconfigurations early in the development cycle of your infrastructure-as-code with KICS by Checkmarx. |
| [ThreatMapper](https://github.com/deepfence/ThreatMapper) | Open Source Cloud Native Application Protection Platform (CNAPP) |
| [grr](https://github.com/google/grr) | GRR Rapid Response: remote live forensics for incident response |
| [boofuzz](https://github.com/jtpereyda/boofuzz) | A fork and successor of the Sulley Fuzzing Framework |
| [is-website-vulnerable](https://github.com/lirantal/is-website-vulnerable) | finds publicly known security vulnerabilities in a website's frontend JavaScript libraries |
| [Network-segmentation-cheat-sheet](https://github.com/sergiomarotco/Network-segmentation-cheat-sheet) | Best practices for segmentation of the corporate network of any company |
| [openappsec](https://github.com/openappsec/openappsec) | open-appsec is a machine learning security engine that preemptively and automatically prevents threats against Web Application & APIs. This repo include the main code and logic. |
| [teller](https://github.com/tellerops/teller) | Cloud native secrets management for developers - never leave your command line for secrets. |
| [matano](https://github.com/matanolabs/matano) | Open source security data lake for threat hunting, detection & response, and cybersecurity analytics at petabyte scale on AWS |
| [openrasp](https://github.com/baidu/openrasp) | 🔥Open source RASP solution |
| [intelmq](https://github.com/certtools/intelmq) | IntelMQ is a solution for IT security teams for collecting and processing security feeds using a message queuing protocol. |
| [ptf](https://github.com/trustedsec/ptf) | The Penetration Testers Framework (PTF) is a way for modular support for up-to-date tools. |
| [Dshell](https://github.com/USArmyResearchLab/Dshell) | Dshell is a network forensic analysis framework. |
| [nuclei](https://github.com/projectdiscovery/nuclei) | Nuclei is a fast, customizable vulnerability scanner powered by the global security community and built on a simple YAML-based DSL, enabling collaboration to tackle trending vulnerabilities on the internet. It helps you find vulnerabilities in your applications, APIs, networks, DNS, and cloud configurations. |
| [ctf-tools](https://github.com/zardus/ctf-tools) | Some setup scripts for security research tools. |
| [tsunami-security-scanner](https://github.com/google/tsunami-security-scanner) | Tsunami is a general purpose network security scanner with an extensible plugin system for detecting high severity vulnerabilities with high confidence. |
| [binwalk](https://github.com/ReFirmLabs/binwalk) | Firmware analysis tool: scan and extract embedded file systems and images from firmware binaries; a staple first step in embedded-device research on images you have the right to inspect. |
| [gobuster](https://github.com/OJ/gobuster) | Directory/File, DNS and VHost busting tool written in Go |
| [testssl.sh](https://github.com/testssl/testssl.sh) | Testing TLS/SSL encryption anywhere on any port |
| [ssh-audit](https://github.com/jtesta/ssh-audit) | SSH server & client security auditing (banner, key exchange, encryption, mac, compression, compatibility, security, etc) |
| [Raccoon](https://github.com/evyatarmeged/Raccoon) | A high performance offensive security tool for reconnaissance and vulnerability scanning |
| [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool) | RSA attack tool (mainly for ctf) - retrieve private key from weak public key and/or uncipher data |
| [routersploit](https://github.com/threat9/routersploit) | Exploitation Framework for Embedded Devices |
| [WinPwn](https://github.com/S3cur3Th1sSh1t/WinPwn) | Automation for internal Windows Penetrationtest / AD-Security |
| [android](https://github.com/cSploit/android) | cSploit - The most complete and advanced IT security professional toolkit on Android. |
| [public-pentesting-reports](https://github.com/juliocesarfort/public-pentesting-reports) | A list of public penetration test reports published by several consulting firms and academic security groups. |
| [amass](https://github.com/owasp-amass/amass) | In-depth attack surface mapping and asset discovery |
| [CloudFail](https://github.com/m0rtem/CloudFail) | Utilize misconfigured DNS and old database records to find hidden IP's behind the CloudFlare network |
| [sslyze](https://github.com/nabla-c0d3/sslyze) | Fast and powerful SSL/TLS scanning library. |
| [github-dorks](https://github.com/techgaun/github-dorks) | Find leaked secrets via github search |
| [AutoSploit](https://github.com/NullArray/AutoSploit) | Automated Mass Exploiter |
| [PRET](https://github.com/RUB-NDS/PRET) | Printer Exploitation Toolkit - The tool that made dumpster diving obsolete. |
| [nikto](https://github.com/sullo/nikto) | Nikto web server scanner: checks for known dangerous files, outdated software, and misconfigurations; noisy and unauthenticated by design — scan only authorised targets. |
| [Inveigh](https://github.com/Kevin-Robertson/Inveigh) | .NET IPv4/IPv6 machine-in-the-middle tool for penetration testers |
| [MailSniper](https://github.com/dafthack/MailSniper) | MailSniper is a penetration testing tool for searching through email in a Microsoft Exchange environment for specific terms (passwords, insider intel, network architecture information, etc.). It can be used as a non-administrative user to search their own email, or by an administrator to search the mailboxes of every user in a domain. |
| [avet](https://github.com/govolution/avet) | AntiVirus Evasion Tool |
| [commix](https://github.com/commixproject/commix) | Automated Αll-in-One OS command injection exploitation tool. |
| [plasma](https://github.com/plasma-disassembler/plasma) | Plasma is an interactive disassembler for x86/ARM/MIPS. It can generates indented pseudo-code with colored syntax. |
