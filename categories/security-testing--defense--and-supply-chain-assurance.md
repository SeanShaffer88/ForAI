# Security testing, defense, and supply-chain assurance

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Verify current upstream documentation, supported versions, license, security, and fit before adoption; catalog checks are not adoption audits.

| Resource | Useful for / constraints |
|---|---|

<!-- expansion-2026-11-10:begin -->
## Expansion — 2026-11-10

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-10.md).

| Resource | Useful for / constraints |
|---|---|
| [Bandit](https://github.com/PyCQA/bandit) | AST-based Python security linter for common unsafe patterns. Fast CI gate; tune the profile or it will drown you in low-signal findings. |
| [DefectDojo](https://github.com/DefectDojo/django-DefectDojo) | Vulnerability management and AppSec orchestration: import scanner findings, deduplicate, track remediation. Operationally non-trivial to self-host, and data quality depends on consistent imports. |
| [ffuf](https://github.com/ffuf/ffuf) | Fast HTTP fuzzer for content discovery and parameter testing with flexible filters. Dual-use: only run it against systems you own or are explicitly authorized to test. |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | Checks whether Kubernetes nodes and control-plane components match CIS benchmark recommendations. Requires cluster access and produces configuration findings, not exploitability proof. |
| [Kubescape](https://github.com/kubescape/kubescape) | Kubernetes posture scanning against NSA/CISA and MITRE frameworks for clusters, manifests, and images. Scans are a starting point; triage roles and exceptions explicitly. |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) | Free, lab-based training on injection, access control, request smuggling, and LLM attacks. Labs are hosted targets; do not reproduce the techniques against systems you do not own or have written authorization to test. |
| [Suricata](https://github.com/OISF/suricata) | IDS/IPS engine with rule-based detection, protocol parsing, and PCAP output. GPL-2.0; rule sources and false-positive tuning determine whether it is useful. |
| [Volatility 3](https://github.com/volatilityfoundation/volatility3) | Memory-forensics framework for analyzing RAM captures with a plugin architecture and symbol tables. The license is source-available (Volatility Software License), not OSI-approved; confirm terms before redistribution. |
| [Wazuh](https://github.com/wazuh/wazuh) | Open-source XDR/SIEM platform: log analysis, file integrity monitoring, compliance checks, and response. GPL-2.0 core with separate agent licensing details; expect real operational work to run it. |
| [Zeek](https://github.com/zeek/zeek) | Network security monitor that turns traffic into structured logs and events. Deep analysis requires sensor placement and storage planning; licensing mixes BSD-style terms with the University of California notice. |
<!-- expansion-2026-11-10:end -->
