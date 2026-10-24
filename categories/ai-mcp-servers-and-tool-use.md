# AI MCP servers and tool use

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Added 2026-10-23 in the AI expansion. Primary-source pointers compiled from official documentation and project repositories; not individually re-fetched in this pass. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Model Context Protocol](https://modelcontextprotocol.io/) | Protocol spec, concepts (tools/resources/prompts), transports, and security guidance. Read this first. |
| [MCP specification (GitHub)](https://github.com/modelcontextprotocol/modelcontextprotocol) | Spec source, schemas, and proposals. |
| [Official MCP servers](https://github.com/modelcontextprotocol/servers) | Reference servers: filesystem, fetch, git, memory, sequential-thinking, time, everything (test server), plus archived servers list. |
| [MCP Registry](https://registry.modelcontextprotocol.io/) | Official community registry for discovering public MCP servers. |
| [MCP Registry (GitHub)](https://github.com/modelcontextprotocol/registry) | Registry API and publishing process. |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | Official Python SDK (FastMCP-style server/client) for building MCP servers. |
| [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | Official TypeScript SDK for servers and clients. |
| [MCP C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) | Official .NET SDK, maintained with Microsoft. |
| [MCP Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) | Official Rust SDK (rmcp). |
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
