# CI version control and releases

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners built into GitLab (.gitlab-ci.yml); self-managed runners are an option when GitHub/GitLab hosted runners do not fit. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment: Microsoft's modern installer with clean uninstall and containerised file/registry views; some legacy installer behaviours are not supported. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |

Project additions checked 2026-10-22 (primary documentation only):

| Resource | Useful for / constraints |
|---|---|
| [GitHub private vulnerability reporting](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository) | Provide a repository-specific private security-reporting route separate from public bug reports. Requires appropriate public-repository administration; notification delivery depends on account preferences. |

## AI expansion additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [GitHub Docs](https://docs.github.com/) | Actions, REST/GraphQL APIs, Copilot, code security. |

<!-- expansion-2026-11-10:begin -->
## Expansion — 2026-11-10

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-10.md).

| Resource | Useful for / constraints |
|---|---|
| [act](https://github.com/nektos/act) | Run GitHub Actions workflows locally in containers to iterate on CI changes. Emulation is close but not identical to hosted runners; secrets, services, and matrix specifics can differ. |
| [Dagger](https://github.com/dagger/dagger) | Container-native pipelines defined in code, run locally or in CI with content-addressed caching. Solves CI lock-in and caching; requires container runtime and a real migration of existing pipelines. |
| [Git LFS](https://github.com/git-lfs/git-lfs) | Large-file storage extension that replaces big binaries with pointer files. Needed for game/ML assets; hosting quotas, mirroring, and clone behavior must be planned. |
| [GitHub CLI](https://github.com/cli/cli) | Official `gh` client covering pull requests, issues, releases, Actions, and the API. Scriptable with `--json` and `--jq`; token scopes determine what it can read or change. |
<!-- expansion-2026-11-10:end -->
