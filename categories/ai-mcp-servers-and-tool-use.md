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

## 2026-10-26 expansion — 1000 AI resources (includes skills.sh directory)

| Resource | Useful for / constraints |
|---|---|
| [MCP Conformance Tests](https://github.com/modelcontextprotocol/conformance) | Official conformance suite to validate MCP server implementations. |
| [GitLab MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) | GitLab MCP: MRs, issues, pipelines for GitLab-hosted projects. |
| [Slack MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) | Slack MCP: channels, messages, and search for agent integrations. |
| [Notion MCP Server](https://github.com/makenotion/notion-mcp-server) | Notion's MCP for pages, databases, and search. |
| [Linear MCP Server](https://github.com/linear/linear-mcp) | Linear's official MCP for issues and project management. |
| [Atlassian MCP](https://github.com/sooperset/mcp-atlassian) | Jira and Confluence via MCP: issues, pages, and search. |
| [Postgres MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) | Postgres MCP: query, schema, and data exploration via MCP. |
| [SQLite MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) | SQLite MCP for local database tooling. |
| [BigQuery MCP Server](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/bigquery) | BigQuery MCP (archived): query and dataset inspection via MCP. |
| [Filesystem MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Reference filesystem MCP with sandboxing for safe file ops. |
| [Memory MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) | Knowledge-graph memory MCP for persistent agent memory. |
| [Brave Search MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) | Brave Search MCP for web search grounding. |
| [Puppeteer MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) | Puppeteer MCP for browser automation via MCP tools. |
| [Fetch MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) | Fetch MCP for URL retrieval and content extraction. |
| [Google Drive MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) | Google Drive MCP: files and search via OAuth. |
| [Google Maps MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) | Google Maps MCP for places, directions, and geocoding. |
| [Everart MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/everart) | EverArt MCP for image generation via EverArt API. |
| [AWS Docs MCP](https://github.com/awslabs/mcp/tree/main/src/aws-docs-mcp-server) | AWS docs MCP from awslabs: search AWS documentation via MCP. |
| [AWS Cost Explorer MCP](https://github.com/awslabs/mcp/tree/main/src/cost-explorer-mcp-server) | AWS Cost Explorer MCP for cost analysis via agent. |
| [Sentry MCP](https://github.com/getsentry/sentry-mcp) | Sentry MCP for issues, traces, and release health. |
| [Stripe MCP](https://github.com/stripe/agent-toolkit) | Stripe agent toolkit with MCP server for payments, customers, invoices. |
| [Twilio MCP](https://github.com/twilio-labs/mcp-twilio) | Twilio MCP for SMS, voice, and communications APIs. |
| [Resend MCP](https://github.com/resend/mcp-send) | Resend MCP for transactional email via agents. |
| [PostHog MCP](https://github.com/PostHog/mcp) | PostHog MCP for analytics and feature flag context. |
| [LaunchDarkly MCP](https://github.com/launchdarkly/mcp-server) | LaunchDarkly MCP for feature flags via agent tooling. |
| [Supabase MCP](https://github.com/supabase-community/supabase-mcp) | Supabase MCP for database, auth, and storage operations. |
| [Qdrant MCP Server](https://github.com/qdrant/mcp-server-qdrant) | Qdrant MCP for vector search via MCP tools. |
| [Pinecone MCP Assistant](https://github.com/pinecone-io/pinecone-mcp) | Pinecone's experimental MCP for vector DB operations. |
| [Tavily MCP Server](https://github.com/tavily-ai/tavily-mcp) | Tavily MCP for AI-optimized search and extraction. |
| [Exa MCP Server](https://github.com/exa-labs/exa-mcp-server) | Exa MCP for neural web search. |
| [Firecrawl MCP](https://github.com/mendable/firecrawl-mcp-server) | Firecrawl MCP for scraping and crawling via MCP. |
| [Apify MCP Server](https://github.com/apify/mcp-server-actors) | Apify Actors MCP: run 3k+ web scrapers as tools. |
| [Docker MCP Toolkit](https://github.com/docker/mcp-servers) | Docker's MCP catalog and gateway for containerized MCP servers. |
| [Kubernetes MCP Server](https://github.com/manusa/kubernetes-mcp-server) | Kubernetes MCP for pod, deployment, and logs access. |
| [Grafana MCP Server](https://github.com/grafana/mcp-grafana) | Grafana MCP for dashboards, alerts, and data sources. |
| [Datadog MCP Server](https://github.com/DataDog/mcp-server-datadog) | Datadog MCP for metrics, logs, and traces. |
| [New Relic MCP](https://github.com/newrelic/mcp-nr) | New Relic MCP for observability data. |
| [Pulumi MCP Server](https://github.com/pulumi/pulumi-mcp-server) | Pulumi MCP for infrastructure code generation and deployments. |
| [Vercel MCP](https://github.com/vercel/mcp-vercel) | Vercel MCP for deployments, logs, and project management. |
| [Netlify MCP](https://github.com/netlify/mcp-server-netlify) | Netlify MCP for deploys and site management. |
| [Heroku MCP](https://github.com/heroku/mcp-server-heroku) | Heroku MCP for app and dyno management. |
| [Figma MCP Server](https://github.com/figma/mcp-server-figma) | Figma MCP for design files, components, and comments. |
| [Canva MCP Server](https://github.com/canva/canva-mcp) | Canva MCP for design automation. |
| [Bluesky MCP](https://github.com/bluesky-social/mcp-bluesky) | Bluesky MCP for social posting and feeds. |
| [YouTube MCP Server](https://github.com/ZubeidHendricks/youtube-mcp-server) | YouTube MCP for transcripts, search, and metadata. |
| [Spotify MCP Server](https://github.com/varunneal/spotify-mcp) | Spotify MCP for playback and library access. |
| [Gmail MCP Server](https://github.com/GongRzhe/Gmail-MCP-Server) | Unofficial Gmail MCP for email search and drafts (OAuth). |
| [Zendesk MCP](https://github.com/zendesk/mcp-server-zendesk) | Zendesk MCP for tickets and help-center docs. |
| [Intercom MCP](https://github.com/intercom/mcp-server-intercom) | Intercom MCP for support conversations. |
| [HubSpot MCP](https://github.com/hubspot/mcp-server-hubspot) | HubSpot MCP for CRM contacts, deals, and tickets. |
| [Salesforce MCP (unofficial)](https://github.com/twilio-labs/mcp-salesforce) | Community Salesforce MCP for CRM via SOQL — verify OAuth. |
