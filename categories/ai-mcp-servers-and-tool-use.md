# AI MCP servers and tool use

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Added 2026-10-23 in the AI expansion. Primary-source pointers compiled from official documentation and project repositories; not individually re-fetched in this pass. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Model Context Protocol](https://modelcontextprotocol.io/) | Protocol spec, concepts (tools/resources/prompts), transports, and security guidance. Read this first. |
| [MCP specification (GitHub)](https://github.com/modelcontextprotocol/modelcontextprotocol) | MCP specification source, schemas, and proposals on GitHub; read the versioned spec site for normal use and this repo when tracking changes or proposing features. |
| [Official MCP servers](https://github.com/modelcontextprotocol/servers) | Reference servers: filesystem, fetch, git, memory, sequential-thinking, time, everything (test server), plus archived servers list. |
| [MCP Registry](https://registry.modelcontextprotocol.io/) | Official community registry for discovering public MCP servers. |
| [MCP Registry (GitHub)](https://github.com/modelcontextprotocol/registry) | MCP Registry source: the registry API and server publishing process; the registry site is the discovery surface, this repo is for publishers and implementers. |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | Official Python SDK (FastMCP-style server/client) for building MCP servers. |
| [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | Official TypeScript SDK for servers and clients. |
| [MCP C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) | Official .NET SDK, maintained with Microsoft. |
| [MCP Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) | Official Rust SDK (rmcp) for building MCP servers and clients; the reference Rust implementation, still evolving with the spec. |
| [MCP Go SDK](https://github.com/modelcontextprotocol/go-sdk) | Official Go SDK, maintained with Google. |
| [MCP Java SDK](https://github.com/modelcontextprotocol/java-sdk) | Official Java SDK, built on Spring AI infrastructure. |
| [GitHub MCP Server](https://github.com/github/github-mcp-server) | GitHub's official MCP server: repos, issues, PRs, Actions. Prefer this over scraping GitHub. |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Microsoft's MCP server for browser automation via Playwright accessibility snapshots. |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Official Chrome DevTools MCP server for debugging, traces, and network inspection. |
| [AWS MCP servers (awslabs)](https://github.com/awslabs/mcp) | AWS's suite of MCP servers for AWS services, docs, and architecture guidance. |
| [Cloudflare MCP servers](https://github.com/cloudflare/mcp-server-cloudflare) | Cloudflare's remote MCP servers for Workers, DNS, observability, and more. |
| [Stripe Agent Toolkit](https://github.com/stripe/ai) | Stripe's official tools for agents, including MCP integration for payments APIs. |
| [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) | Large community list of MCP servers by category; a discovery aid — verify each server before use. |
| [MCP.so](https://mcp.so/) | Community directory of MCP servers and clients with categories. |
| [Glama MCP directory](https://glama.ai/mcp/servers) | Searchable MCP server directory with listings and metadata. |
| [Smithery](https://smithery.ai/) | Hosted MCP server discovery and connection service. |
| [PulseMCP](https://www.pulsemcp.com/) | MCP server directory and weekly newsletter tracking the ecosystem. |
| [MCP clients list](https://modelcontextprotocol.io/clients) | Which clients support which MCP features. The standalone clients page now redirects into the versioned MCP documentation; client feature support is maintained there. |

## AI expansion round 2 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [MCP Inspector](https://github.com/modelcontextprotocol/inspector) | Official visual testing/debugging tool for MCP servers: inspect tools, resources, prompts, and notifications during development. |
| [FastMCP](https://gofastmcp.com/) | High-level Python framework for building MCP servers and clients; much of the ecosystem is built on it. Mind the version — FastMCP 1.x was merged into the official Python SDK lineage. |

## AI expansion round 3 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [Docker MCP Toolkit and Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) | Docker's curated MCP catalog and toolkit: run MCP servers as containers with isolation and secret handling. |
| [Kubernetes MCP Server](https://github.com/containers/kubernetes-mcp-server) | MCP server for Kubernetes and OpenShift operations via native API calls. |
| [Terraform MCP Server (HashiCorp)](https://github.com/hashicorp/terraform-mcp-server) | HashiCorp's MCP server for Terraform Registry modules, providers, and workspace operations. |
| [MongoDB MCP Server](https://github.com/mongodb-js/mongodb-mcp-server) | MongoDB's official MCP server for database exploration and operations (read-only modes available). |
| [Supabase MCP Server](https://github.com/supabase/mcp) | Supabase's official MCP server: manage tables, run SQL, and deploy functions from an agent. Use read-only mode for safety. |
| [Neon MCP Server](https://github.com/neondatabase/mcp-server-neon) | Neon's MCP server for managing serverless Postgres projects, branches, and queries. |
| [Redis MCP Server](https://github.com/redis/mcp-redis) | Redis's official MCP server for natural-language operations against Redis data. |
| [Sentry MCP Server](https://github.com/getsentry/toolkit) | Sentry's official MCP server (now developed in Sentry's toolkit monorepo): query issues, errors, and performance data from coding agents. |
| [Linear MCP Server](https://linear.app/docs/mcp) | Linear's official remote MCP server for issues and project data in agents. |
| [Figma MCP Server (Dev Mode)](https://developers.figma.com/docs/figma-mcp-server/) | Figma's official MCP server: bring design context (and code generation hints) into coding agents. |
| [ToolHive (Stacklok)](https://docs.stacklok.com/toolhive/) | Run and manage MCP servers in containers with a registry, proxy, and access controls. |
| [ContextForge MCP Gateway (IBM)](https://github.com/IBM/mcp-context-forge) | IBM's open-source MCP gateway and registry: federation, auth, and tool virtualization for teams. |
| [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters) | Adapters that turn MCP tools into LangChain/LangGraph tools; the standard bridge between the two ecosystems. |
| [mcp-use](https://github.com/mcp-use/mcp-use) | Framework to build full MCP agents (client + server) in Python/TypeScript, with a hosted inspector. |

## Niche expansion — 2026-10-27

Additional entries from a focused discovery pass; see the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-27-round-2.md). Repository API metadata was checked, but these links are not README, license, security, compatibility, or adoption audits.

| Resource | Useful for / constraints |
|---|---|
| [UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra |
| [MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP) | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. |
| [toolhive](https://github.com/stacklok/toolhive) | ToolHive is an enterprise-grade platform for running and managing Model Context Protocol (MCP) servers. |
| [slack-mcp-server](https://github.com/korotovsky/slack-mcp-server) | The most powerful MCP Slack Server with no permission requirements, Apps support, GovSlack, DMs, Group DMs and smart history fetch logic. |
| [ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) | A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Microsoft Office services through the Graph API |
| [octocode](https://github.com/bgauryy/octocode) | Code research platform for AI agents; find, understand, and prove context across your code and all of GitHub, in a fraction of the tokens. One toolset, MCP or CLI |
| [k8m](https://github.com/weibaohui/k8m) | 一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。 |
| [android-mcp-server](https://github.com/minhalvp/android-mcp-server) | An MCP server that provides control over Android devices via adb |
| [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | Meta Ads (Facebook/Instagram) MCP server for Claude, ChatGPT, Perplexity & Cursor — the Meta node of Pipeboard’s 5-platform family (+ Google, TikTok, Snap, Reddit). Hosted remote MCP, badged Meta Business Partner, free plan — no self-hosting required. |
| [qgis_mcp](https://github.com/jjsantos01/qgis_mcp) | Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop |
| [shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents) | Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI. Supports: MCPs, Remote and Local AI, Crypto and Payments. |
| [vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server) | Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks |
| [plane-mcp-server](https://github.com/makeplane/plane-mcp-server) | Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥 |
| [consult7](https://github.com/szeider/consult7) | MCP server to consult a language model with large context size |
| [gk-cli](https://github.com/gitkraken/gk-cli) | GitKraken CLI Releases and Documentation |
| [mux-ts](https://github.com/muxinc/mux-ts) | Official Mux API wrapper for Node projects, supporting both Mux Data and Mux Video. |
| [scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server) | Scrapeless Mcp Server |
| [mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast) | Quickly reads webpages and converts to markdown for fast, token efficient web scraping |
| [armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp) | The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more. |
| [BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI) | BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries. |
| [magg](https://github.com/sitbon/magg) | Magg: The MCP Aggregator |
| [fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) | FHIR MCP Server – helping you expose any FHIR Server or API as a MCP Server. |
| [FileScopeMCP](https://github.com/admica/FileScopeMCP) | Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua. |
| [reloaderoo](https://github.com/cameroncooke/reloaderoo) | Powerful MCP debugging proxy and CLI inspection tool. |
| [mcp-trino](https://github.com/tuannvm/mcp-trino) | A high-performance Model Context Protocol (MCP) server for Trino implemented in Go. |
