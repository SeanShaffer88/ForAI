# Expansion — 2026-11-11

**653 additions across 38 categories.** Discovered from GitHub topic
searches (AI agents, MCP, LLMs, prompts and skills, reverse engineering, plus 140
more topics), [gittrend.io/hidden-gems](https://gittrend.io/hidden-gems), and the
[AwesomeHub](https://awesomehub.js.org/) topic indexes, then filtered against the
existing catalog by GitHub identity, URL, and repository name.

Every entry was checked through the GitHub REST repository endpoint on 2026-11-11
(HTTP 200). That is reachability and metadata evidence only — **not** a README
review, release or maintenance audit, licensing opinion, security assessment,
compatibility test, or adoption recommendation. Star counts are time-bound
popularity signals, not quality scores.

What was missing before this pass: the 2026-11-10 expansion added the written
conventions and everyday tooling, but the catalog still had no entries for whole
families of actively used software — mainstream ORMs and database servers,
message queues and workflow engines, OpenTelemetry SDKs and log pipelines,
container and Kubernetes operating tools, i18n libraries, OCR and document
extraction, rich-text and note-taking engines, editor extension ecosystems,
.NET application blocks, Android libraries, and the newer AI-agent layer:
skills, memory, MCP clients, guardrail and red-teaming tools.

## Evidence and limits

- **Scope of each entry:** the `review` field in `resources.json` records exactly
  what was checked, with the repository id in
  [`docs/expansion-2026-11-11-checks.json`](../docs/expansion-2026-11-11-checks.json).
- **GitHub license detection** is often `NOASSERTION` or empty. Where a license
  matters for redistribution the entry says so and you must read the license.
  Copyleft and source-available entries carry the trade-off inline.
- **No package was installed, no build was run, and no service was exercised.**
- Dual-use security and reverse-engineering tools are listed for systems and
  binaries you own or are explicitly authorized to analyze.
- Several entries are deliberately *not* recommended for every use: they are
  listed with their real trade-off so you can decide. A catalog entry is not an
  endorsement.

## How to use this page

Read the category heading, then the entry's constraint sentence. If a constraint
conflicts with your project (an AGPL component in a closed product, a
source-available license, a hosted dependency where you need self-hosting), stop
there and look at the alternative named in the same row.

| Category | Additions |
|---|---|
| .NET application building blocks | 27 |
| AI MCP servers and tool use | 8 |
| AI agent frameworks and orchestration | 8 |
| AI agent memory and context | 6 |
| AI agent protocols and interoperability | 3 |
| AI coding agents and assistants | 10 |
| AI evaluation observability and guardrails | 11 |
| AI learning and references | 6 |
| AI machine learning and local inference | 8 |
| AI models and API providers | 6 |
| AI prompt and context engineering | 12 |
| AI retrieval and vector search | 8 |
| API contracts clients and networking | 30 |
| Accessibility internationalization and documentation | 23 |
| Android APK development and analysis | 22 |
| Builds packages and environments | 22 |
| Cloud infrastructure and deployment | 24 |
| Collaboration local state and rich text | 29 |
| Data science and engineering tools | 18 |
| Databases data access and analytics | 27 |
| Desktop mobile and device SDKs | 28 |
| Documents OCR and file formats | 22 |
| Editor and terminal extensions | 20 |
| Feature flags configuration and secrets | 13 |
| Game creation assets and automation | 22 |
| Graphics multimedia scientific and geospatial | 34 |
| Infrastructure as code and cloud-native operations | 26 |
| Languages and runtimes | 24 |
| Linux and Unix tooling | 18 |
| Observability debugging and operations | 20 |
| Optimization scheduling and operational tooling | 6 |
| Platform SDKs and Windows | 13 |
| Reverse engineering malware analysis and binary inspection | 22 |
| Search messaging and durable work | 29 |
| Software architecture and API design patterns | 14 |
| Test automation and quality engineering | 17 |
| Testing verification and performance | 4 |
| Windows / Graphics | 13 |

## .NET application building blocks

| Resource | Useful for / constraints |
|---|---|
| [abp](https://github.com/abpframework/abp) | Open-source web application framework for ASP.NET Core! Offers an opinionated architecture to build enterprise software solutions with best practices on top of the .NET. LGPL-3.0: dynamic linking is permitted, static linking has obligations. |
| [aspnet api versioning](https://github.com/dotnet/aspnet-api-versioning) | Provides a set of libraries which add service API versioning to ASP.NET Core Minimal APIs, Controllers, gRPC, OData, and Web API (Classic). |
| [aspnetcore](https://github.com/dotnet/aspnetcore) | ASP.NET Core is a cross-platform .NET framework for building modern cloud-based web applications on Windows, Mac, or Linux. |
| [AutoMapper](https://github.com/LuckyPennySoftware/AutoMapper) | A convention-based object-object mapper in .NET. License not detected by GitHub; check the repository license before use. |
| [CleanArchitecture](https://github.com/ardalis/CleanArchitecture) | Clean Architecture Solution Template: A proven Clean Architecture Template for ASP.NET Core 10. |
| [CleanArchitecture (jasontaylordev)](https://github.com/jasontaylordev/CleanArchitecture) | Clean Architecture Solution Template for ASP.NET Core. |
| [command line api](https://github.com/dotnet/command-line-api) | Command line parsing, invocation, and rendering of terminal output. |
| [DotNetCorePlugins](https://github.com/natemcmaster/DotNetCorePlugins) | .NET Core library for dynamically loading code. |
| [efcore](https://github.com/dotnet/efcore) | EF Core is a modern object-database mapper for .NET. It supports LINQ queries, change tracking, updates, and schema migrations. |
| [elsa core](https://github.com/elsa-workflows/elsa-core) | The Workflow Engine for .NET. |
| [eShopOnContainers](https://github.com/dotnet-architecture/eShopOnContainers) | Cross-platform .NET sample microservices and container based application that runs on Linux Windows and macOS. Powered by .NET 7, Docker Containers and Azure Kubernetes Services. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [eShopOnWeb](https://github.com/dotnet-architecture/eShopOnWeb) | Sample ASP.NET Core 8.0 reference application, now community supported: https://github.com/NimblePros/eShopOnWeb. |
| [jellyfin](https://github.com/jellyfin/jellyfin) | The Free Software Media System - Server Backend & API. GPL-2.0: derivative works must stay under the GPL. |
| [LiteDB](https://github.com/litedb-org/LiteDB) | LiteDB - A .NET NoSQL Document Store in a single data file. |
| [maui](https://github.com/dotnet/maui) | .NET MAUI is the .NET Multi-platform App UI, a framework for building native device applications spanning mobile, tablet, and desktop. |
| [maui samples](https://github.com/dotnet/maui-samples) | Samples for .NET Multi-Platform App UI (.NET MAUI). |
| [MediatR](https://github.com/LuckyPennySoftware/MediatR) | Simple, unambitious mediator implementation in .NET. License not detected by GitHub; check the repository license before use. |
| [mono](https://github.com/mono/mono) | Mono open source ECMA CLI, C# and .NET implementation. License not detected by GitHub; check the repository license before use. |
| [MQTTnet](https://github.com/dotnet/MQTTnet) | MQTTnet is a high performance .NET library for MQTT based communication. It provides a MQTT client and a MQTT server (broker). The implementation is based on the documentation from http://mqtt.org/. |
| [nlog](https://github.com/NLog/NLog) | NLog - Flexible and Structured Logging for various .NET Platforms. |
| [NSwag](https://github.com/RicoSuter/NSwag) | The Swagger/OpenAPI toolchain for .NET, ASP.NET Core and TypeScript. |
| [NuGet.Client](https://github.com/NuGet/NuGet.Client) | Client Tools for NuGet - including Visual Studio extensions, command line tools, and msbuild support. (Open issues on https://github.com/nuget/home/issues). License not detected by GitHub; check the repository license before use. |
| [Ocelot](https://github.com/ThreeMammals/Ocelot) | .NET API Gateway. |
| [OrchardCore](https://github.com/OrchardCMS/OrchardCore) | Orchard Core is an open-source modular and multi-tenant application framework built with ASP.NET Core, and a content management system (CMS) built on top of that framework. |
| [reverse proxy](https://github.com/dotnet/yarp) | A toolkit for developing high-performance HTTP reverse proxy applications. |
| [Silk.NET](https://github.com/dotnet/Silk.NET) | The high-speed OpenGL, OpenCL, OpenAL, OpenXR, GLFW, SDL, Vulkan, Assimp, WebGPU, and DirectX bindings library your mother warned you about. |
| [Templates](https://github.com/Dotnet-Boxed/Templates) | .NET project templates with batteries included, providing the minimum amount of code required to get you going faster. |

## AI MCP servers and tool use

| Resource | Useful for / constraints |
|---|---|
| [exa mcp server](https://github.com/exa-labs/exa-mcp-server) | Exa MCP for web search and web crawling! |
| [excel mcp server](https://github.com/haris-musa/excel-mcp-server) | Excel MCP server: let AI (Claude, Cursor, Codex) create and edit Excel files with charts, PivotTables, slicers and formulas. No Excel required. |
| [firecrawl mcp server](https://github.com/firecrawl/firecrawl-mcp-server) | Official Firecrawl MCP server, the context API for AI agents: search, scrape, and interact with the web, plus parse, crawl, map, Agent and Monitor, from any MCP client. |
| [mcp](https://github.com/BrowserMCP/mcp) | Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser. |
| [mcp for beginners](https://github.com/microsoft/mcp-for-beginners) | This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. |
| [mcpo](https://github.com/open-webui/mcpo) | A simple, secure MCP-to-OpenAPI proxy server. |
| [n8n mcp](https://github.com/czlonkowski/n8n-mcp) | A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you. |
| [zotero mcp](https://github.com/54yyyu/zotero-mcp) | Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more. |

## AI agent frameworks and orchestration

| Resource | Useful for / constraints |
|---|---|
| [agenticSeek](https://github.com/Fosowl/agenticSeek) | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. GPL-3.0: derivative works must stay under the GPL. |
| [agents course](https://github.com/huggingface/agents-course) | This repository contains the Hugging Face Agents Course. |
| [ai agents for beginners](https://github.com/microsoft/ai-agents-for-beginners) | 18 Lessons to Get Started Building AI Agents. |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters. License not detected by GitHub; check the repository license before use. |
| [DocsGPT](https://github.com/arc53/DocsGPT) | Private AI platform for agents, assistants and enterprise search. Built-in Agent Builder, Deep research, Document analysis, Multi-model support, and API connectivity for agents. |
| [PocketFlow](https://github.com/The-Pocket/PocketFlow) | Pocket Flow: 100-line LLM framework. Let Agents build Agents! |
| [RagaAI Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) | Python SDK for Agent AI Observability, Monitoring and Evaluation Framework. Includes features like agent, llm and tools tracing, debugging multi-agentic system,. |
| [swarm](https://github.com/openai/swarm) | Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team. |

## AI agent memory and context

| Resource | Useful for / constraints |
|---|---|
| [agentmemory](https://github.com/rohitg00/agentmemory) | #1 Persistent memory for AI coding agents based on real-world benchmarks. |
| [EverOS](https://github.com/EverMind-AI/EverOS) | One portable memory layer for every AI agent: local-first, Markdown-native, user-owned, and self-evolving across apps, tools, and workflows. |
| [hindsight](https://github.com/vectorize-io/hindsight) | Hindsight: Agent Memory That Learns. |
| [memobase](https://github.com/memodb-io/memobase) | User Profile-Based Long-Term Memory for AI Chatbot Applications. |
| [Memori](https://github.com/MemoriLabs/Memori) | Memori is agent-native memory infrastructure. A LLM-agnostic layer that turns agent execution and conversation into structured, persistent state for production systems. License not detected by GitHub; check the repository license before use. |
| [supermemory](https://github.com/supermemoryai/supermemory) | Memory and context engine + app that is extremely fast, scalable, and can be run fully locally. The Memory API for the AI era. |

## AI agent protocols and interoperability

| Resource | Useful for / constraints |
|---|---|
| [bifrost](https://github.com/maximhq/bifrost) | Open-source, high-performance AI gateway that works as your LLM gateway, MCP gateway and agent gateway. One OpenAI-compatible API for 10,000+ models, with failover, load balancing, semantic caching, virtual keys,. |
| [unity mcp](https://github.com/CoplayDev/unity-mcp) | Unity MCP acts as a bridge between AI assistants and your Unity Editor. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity. |
| [x64dbg mcp server](https://github.com/duty1g/x64dbg-mcp-server) | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. |

## AI coding agents and assistants

| Resource | Useful for / constraints |
|---|---|
| [assistant ui](https://github.com/assistant-ui/assistant-ui) | Typescript/React Library for AI Chat. |
| [claude howto](https://github.com/luongnv89/claude-howto) | A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value. |
| [claude seo](https://github.com/AgriciDaniel/claude-seo) | Universal SEO skill for Claude Code. 26 sub-skills + 19 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, agent readiness (Lighthouse Agentic Browsing, WebMCP, llms.txt), backlinks, local SEO, e-commerce,. |
| [claude skills](https://github.com/Jeffallan/claude-skills) | 67 Specialized Skills for Full-Stack Developers. Transform Claude Code into your expert pair programmer. |
| [claude squad](https://github.com/smtg-ai/claude-squad) | Manage multiple AI terminal agents like Claude Code, Codex, OpenCode, and Amp. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [CodexBar](https://github.com/steipete/CodexBar) | Show usage stats for OpenAI Codex and Claude Code, without having to login. |
| [crush](https://github.com/charmbracelet/crush) | Glamourous agentic coding for all. License not detected by GitHub; check the repository license before use. |
| [DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities. |
| [open design](https://github.com/nexu-io/open-design) | The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create motion, prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. |
| [planning with files](https://github.com/OthmanAdi/planning-with-files) | Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. |

## AI evaluation observability and guardrails

| Resource | Useful for / constraints |
|---|---|
| [agentdojo](https://github.com/ethz-spylab/agentdojo) | A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents. |
| [AI Infra Guard](https://github.com/Tencent/AI-Infra-Guard) | A full-stack AI Red Teaming platform securing AI ecosystems via Agent Scan, Skills Scan, MCP scan, AI Infra scan and LLM jailbreak evaluation. |
| [guardrails](https://github.com/guardrails-ai/guardrails) | Adding guardrails to large language models. |
| [helicone](https://github.com/Helicone/helicone) | Open source LLM observability platform. One line of code to monitor, evaluate, and experiment. YC W23. |
| [langfuse](https://github.com/langfuse/langfuse) | Open source agent evals & observability: Trace, evaluate, and improve LLM applications with one open platform. License not detected by GitHub; check the repository license before use. |
| [langkit](https://github.com/whylabs/langkit) | LangKit: An open-source toolkit for monitoring Large Language Models (LLMs). Extracts signals from prompts & responses, ensuring safety & security. Features include text quality, relevance metrics, & sentiment analysis. |
| [opik](https://github.com/comet-ml/opik) | Debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, automated evaluations, and production-ready dashboards. |
| [presidio](https://github.com/data-privacy-stack/presidio) | An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines. |
| [promptmap](https://github.com/utkusen/promptmap) | a security scanner for custom LLM applications. GPL-3.0: derivative works must stay under the GPL. |
| [PyRIT](https://github.com/microsoft/PyRIT) | Open-source AI red teaming toolkit from Microsoft. Test generative AI systems with automated scans, adaptive multi-turn attacks, and a web UI. |
| [superagent](https://github.com/superagent-ai/superagent) | Superagent protects your AI applications against prompt injections, data leaks, and harmful outputs. Embed safety directly into your app and prove compliance to your customers. |

## AI learning and references

| Resource | Useful for / constraints |
|---|---|
| [Awesome AITools](https://github.com/ikaijua/Awesome-AITools) | This repo collects awesome AI tools. Welcome everyone to recommend more awesome AI tools together! |
| [awesome startup](https://github.com/KrishMunot/awesome-startup) | sunglasses: All the required resources to build your own startup. |
| [best of Agent Harnesses](https://github.com/RyanAlberts/best-of-Agent-Harnesses) | Ranked list of 187 AI agent harnesses, plus templates, playbooks, MCP, and learning resources. Rescored weekly. |
| [generative ai](https://github.com/GoogleCloudPlatform/generative-ai) | Sample code and notebooks for Generative AI on Google Cloud, with Gemini platform. |
| [Made With ML](https://github.com/GokuMohandas/Made-With-ML) | Learn how to develop, deploy and iterate on production-grade ML applications. |
| [ML YouTube Courses](https://github.com/dair-ai/ML-YouTube-Courses) | Discover the latest machine learning / AI courses on YouTube. |

## AI machine learning and local inference

| Resource | Useful for / constraints |
|---|---|
| [graphrag](https://github.com/microsoft/graphrag) | A modular graph-based Retrieval-Augmented Generation (RAG) system. |
| [Hands On Large Language Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) | Official code repo for the O'Reilly Book - "Hands-On Large Language Models". |
| [kotaemon](https://github.com/Cinnamon/kotaemon) | An open-source RAG-based tool for chatting with your documents. |
| [langextract](https://github.com/google/langextract) | A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization. |
| [llmfit](https://github.com/AlexsJones/llmfit) | Hundreds of models & providers. One command to find what runs on your hardware. |
| [lms](https://github.com/lmstudio-ai/lms) | LM Studio CLI. |
| [peft](https://github.com/huggingface/peft) | PEFT: State-of-the-art Parameter-Efficient Fine-Tuning. |
| [SillyTavern](https://github.com/SillyTavern/SillyTavern) | LLM Frontend for Power Users. AGPL-3.0: network use can trigger source-disclosure obligations. |

## AI models and API providers

| Resource | Useful for / constraints |
|---|---|
| [ClawRouter](https://github.com/BlockRunAI/ClawRouter) | The agent-native LLM router for autonomous agents. Every frontier model behind one wallet, <1ms local routing, USDC payments on Base & Solana via x402. |
| [fragments](https://github.com/e2b-dev/fragments) | Open-source Next.js template for building apps that are fully generated by AI. By E2B. |
| [gpt load](https://github.com/tbphp/gpt-load) | Self-hosted AI gateway for multi-channel, multi-credential setups — API keys and subscription accounts, scheduling, failover, request logs and usage. 自托管 AI 网关：多渠道多凭据统一接入，含密钥与订阅账号、调度容错、日志与用量。. |
| [one api](https://github.com/songquanpeng/one-api) | LLM API 管理 & 分发系统，支持 OpenAI、Azure、Anthropic Claude、Google Gemini、DeepSeek、字节豆包、ChatGLM、文心一言、讯飞星火、通义千问、360 智脑、腾讯混元等主流模型，统一 API 适配，可用于 key 管理与二次分发。单可执行文件，提供 Docker 镜像，一键部署，开箱即用。LLM API management & key redistribution system,. |
| [openai node](https://github.com/openai/openai-node) | Official JavaScript / TypeScript library for the OpenAI API. |
| [openai python](https://github.com/openai/openai-python) | The official Python library for the OpenAI API. |

## AI prompt and context engineering

| Resource | Useful for / constraints |
|---|---|
| [awesome agent skills](https://github.com/VoltAgent/awesome-agent-skills) | A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more. |
| [awesome claude code](https://github.com/hesreallyhim/awesome-claude-code) | A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC (no affiliation). License not detected by GitHub; check the repository license before use. |
| [Awesome Prompt Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering) | This repository contains a hand-curated resources for Prompt Engineering with a focus on Generative Pre-trained Transformer (GPT), ChatGPT, PaLM etc. |
| [chatgpt system prompt](https://github.com/LouisShark/chatgpt_system_prompt) | A collection of GPT system prompts and various prompt injection/leaking knowledge. |
| [claude code system prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | All parts of Claude Code's system prompt, 27 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact, statusline, magic docs, WebFetch, Bash cmd, security review, agent creation). |
| [code2prompt](https://github.com/mufeedvh/code2prompt) | A CLI tool to convert your codebase into a single LLM prompt with source tree, prompt templating, and token counting. |
| [dev browser](https://github.com/SawyerHood/dev-browser) | A Claude Skill to give your agent the ability to use a web browser. |
| [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents. |
| [promptflow](https://github.com/microsoft/promptflow) | Build high-quality LLM apps - from prototyping, testing to production deployment and monitoring. |
| [skills](https://github.com/google/skills) | Agent Skills for Google products and technologies. |
| [system prompts and models of ai tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev,. GPL-3.0: derivative works must stay under the GPL. |
| [ui skills](https://github.com/ibelick/ui-skills) | Skills for Design Engineers. |

## AI retrieval and vector search

| Resource | Useful for / constraints |
|---|---|
| [FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) | Retrieval and Retrieval-augmented LLMs. |
| [hnswlib](https://github.com/nmslib/hnswlib) | Header-only C++/python library for fast approximate nearest neighbors. |
| [milvus](https://github.com/milvus-io/milvus) | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search. |
| [mteb](https://github.com/embeddings-benchmark/mteb) | MTEB: State-of-the-art evaluation of embeddings across languages and modalities. |
| [postgresml](https://github.com/postgresml/postgresml) | Postgres with GPUs for ML/AI apps. |
| [SPTAG](https://github.com/microsoft/SPTAG) | A distributed approximate nearest neighborhood search (ANN) library which provides a high quality vector index build, search and distributed online serving toolkits for large scale vector search scenario. |
| [text embeddings inference](https://github.com/huggingface/text-embeddings-inference) | A blazing fast inference solution for text embeddings models. |
| [USearch](https://github.com/unum-cloud/USearch) | One proximity graph for vector search, sparse products & attention across RAM, VRAM & NVMe, over dense vectors, sequences, shapes & geospatial sets in 14 languages. |

## API contracts clients and networking

| Resource | Useful for / constraints |
|---|---|
| [apollo client](https://github.com/apollographql/apollo-client) | The industry-leading GraphQL client for TypeScript, JavaScript, React, Vue, Angular, and more. Apollo Client delivers powerful caching, intuitive APIs, and comprehensive developer tools to accelerate your app development. |
| [apollo server](https://github.com/apollographql/apollo-server) | Spec-compliant and production ready JavaScript GraphQL server that lets you develop in a schema-first way. Built for Express, Connect, Hapi, Koa, and more. |
| [async graphql](https://github.com/async-graphql/async-graphql) | A GraphQL server library implemented in Rust. |
| [axios](https://github.com/axios/axios) | Promise based HTTP client for the browser and node.js. |
| [federation](https://github.com/apollographql/federation) | Build and scale a single data graph across multiple services with Apollo's federation gateway. License not detected by GitHub; check the repository license before use. |
| [go swagger](https://github.com/go-swagger/go-swagger) | Swagger 2.0 implementation for go. |
| [googleapis](https://github.com/googleapis/googleapis) | Public interface definitions of Google APIs. |
| [got](https://github.com/sindresorhus/got) | Human-friendly and powerful HTTP request library for Node.js. |
| [gqlgen](https://github.com/99designs/gqlgen) | go generate based graphql server library. |
| [graphql apis](https://github.com/APIs-guru/graphql-apis) | A collective list of public GraphQL APIs. |
| [graphql js](https://github.com/graphql/graphql-js) | A reference implementation of GraphQL for JavaScript. |
| [graphql mesh](https://github.com/ardatan/graphql-mesh) | GraphQL Federation Framework for any API services such as REST, OpenAPI, Swagger, SOAP, gRPC and more... |
| [graphql spec](https://github.com/graphql/graphql-spec) | GraphQL is a query language and execution engine tied to any backend service. License not detected by GitHub; check the repository license before use. |
| [graphql tools](https://github.com/ardatan/graphql-tools) | wrench: Utility library for GraphQL to build, stitch and mock GraphQL schemas in the SDL-first approach. |
| [graphql voyager](https://github.com/APIs-guru/graphql-voyager) | Represent any GraphQL API as an interactive graph. |
| [graphql yoga](https://github.com/graphql-hive/graphql-yoga) | Rewrite of a fully-featured GraphQL Server with focus on easy setup, performance & great developer experience. The core of Yoga implements WHATWG Fetch API and can run/deploy on any JS environment. |
| [grpc go](https://github.com/grpc/grpc-go) | The Go language implementation of gRPC. HTTP/2 based RPC. |
| [grpc java](https://github.com/grpc/grpc-java) | The Java gRPC implementation. HTTP/2 based RPC. |
| [kin openapi](https://github.com/getkin/kin-openapi) | OpenAPI 3.0 and 3.1 and 3.2 (and Swagger v2) implementation for Go (parsing, converting, validation, and more). |
| [node fetch](https://github.com/node-fetch/node-fetch) | A light-weight module that brings the Fetch API to Node.js. |
| [openapi diff](https://github.com/OpenAPITools/openapi-diff) | Utility for comparing two OpenAPI specifications. |
| [openapi generator (OpenAPITools)](https://github.com/OpenAPITools/openapi-generator) | OpenAPI Generator allows generation of API client libraries (SDK generation), server stubs, documentation and configuration automatically given an OpenAPI Spec (v2, v3). |
| [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) | The OpenAPI Specification Repository. |
| [prism](https://github.com/stoplightio/prism) | Turn any OpenAPI2/3 and Postman Collection file into an API server with mocking, transformations and validations. |
| [protobuf](https://github.com/protocolbuffers/protobuf) | Protocol Buffers - Google's data interchange format. License not detected by GitHub; check the repository license before use. |
| [public apis](https://github.com/public-apis/public-apis) | A collective list of free APIs. |
| [rest api description](https://github.com/github/rest-api-description) | An OpenAPI description for GitHub's REST API. |
| [spectral](https://github.com/stoplightio/spectral) | A flexible JSON/YAML linter for creating automated style guides, with baked in support for OpenAPI (v3.1, v3.0, and v2.0), Arazzo v1.0, as well as AsyncAPI v2.x. |
| [swagger ui](https://github.com/swagger-api/swagger-ui) | Swagger UI is a collection of HTML, JavaScript, and CSS assets that dynamically generate beautiful documentation from a Swagger-compliant API. |
| [vulcain](https://github.com/dunglas/vulcain) | Fast and idiomatic client-driven REST APIs. AGPL-3.0: network use can trigger source-disclosure obligations. |

## Accessibility internationalization and documentation

| Resource | Useful for / constraints |
|---|---|
| [a11y.css](https://github.com/ffoodd/a11y.css) | This CSS file intends to warn developers about possible risks and mistakes that exist in HTML code. It can also be used to roughly evaluate a site's quality by simply including it as an external stylesheet. |
| [a11yproject.com](https://github.com/a11yproject/a11yproject.com) | The A11Y Project is a community-driven effort to make digital accessibility easier. |
| [aria practices](https://github.com/w3c/aria-practices) | WAI-ARIA Authoring Practices Guide (APG). License not detected by GitHub; check the repository license before use. |
| [babel](https://github.com/python-babel/babel) | The official repository for Babel, the Python Internationalization Library. |
| [content](https://github.com/mdn/content) | The official source for MDN Web Docs content. Home to over 14,000 pages of documentation about HTML, CSS, JS, HTTP, Web APIs, and more. License not detected by GitHub; check the repository license before use. |
| [docsify](https://github.com/docsifyjs/docsify) | A magical documentation site generator. |
| [ever traduora](https://github.com/ever-co/ever-traduora) | Ever® Traduora™ - Open Translation Management Platform - https://traduora.co. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [fluent](https://github.com/projectfluent/fluent) | Fluent — planning, spec and documentation. |
| [fluent rs](https://github.com/projectfluent/fluent-rs) | Rust implementation of Project Fluent. |
| [globalize](https://github.com/globalizejs/globalize) | A JavaScript library for internationalization and localization that leverages the official Unicode CLDR JSON data. |
| [go i18n](https://github.com/nicksnyder/go-i18n) | Translate your Go program into multiple languages. |
| [gt](https://github.com/generaltranslation/gt) | Full-stack localization for every framework. |
| [hugo](https://github.com/gohugoio/hugo) | The world’s fastest framework for building websites. |
| [intl](https://github.com/symfony/intl) | Provides access to the localization data of the ICU library. |
| [jupyter book](https://github.com/jupyter-book/jupyter-book) | Create beautiful, publication-quality books and documents from computational content. |
| [just the docs](https://github.com/just-the-docs/just-the-docs) | A modern, high customizable, responsive Jekyll theme for documentation with built-in search. |
| [lyricist](https://github.com/adrielcafe/lyricist) | The missing I18N/L10N (internationalization/localization) multiplatform library for Compose Multiplatform! |
| [mkdocs material](https://github.com/squidfunk/mkdocs-material) | Documentation that simply works. |
| [mystmd](https://github.com/jupyter-book/mystmd) | Command line tools for working with MyST Markdown. |
| [readthedocs.org](https://github.com/readthedocs/readthedocs.org) | The source code that powers readthedocs.org. |
| [svelte i18n](https://github.com/kaisermann/svelte-i18n) | Internationalization library for Svelte. |
| [transloco](https://github.com/jsverse/transloco) | The internationalization (i18n) library for Angular. |
| [www](https://github.com/writethedocs/www) | The main website for Write the Docs. License not detected by GitHub; check the repository license before use. |

## Android APK development and analysis

| Resource | Useful for / constraints |
|---|---|
| [AAA](https://github.com/Psyhackological/AAA) | iphone: Curated list of THE BEST FOSS Android apps to maximize your freedom & privacy! |
| [accompanist](https://github.com/google/accompanist) | A collection of extension libraries for Jetpack Compose. |
| [android emulator container scripts](https://github.com/google/android-emulator-container-scripts) | This is a set of minimal scripts to run the emulator in a container for various systems such as Docker, for external consumption. |
| [androidx](https://github.com/androidx/androidx) | Development environment for Android Jetpack extension libraries under the androidx namespace. Synchronized with Android Jetpack's primary development branch on AOSP. |
| [architecture samples](https://github.com/android/architecture-samples) | A collection of samples to discuss and showcase different architectural tools and patterns for Android apps. |
| [awesome android ui](https://github.com/wasabeef/awesome-android-ui) | A curated list of awesome Android UI/UX libraries. |
| [awesome flutter](https://github.com/Solido/awesome-flutter) | An awesome list that curates the best Flutter libraries, tools, tutorials, articles and more. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [coil](https://github.com/coil-kt/coil) | Image loading for Android and Compose Multiplatform. |
| [compose samples](https://github.com/android/compose-samples) | Official Jetpack Compose samples. |
| [dex2jar](https://github.com/pxb1988/dex2jar) | Tools to work with android .dex and java .class files. |
| [firefox android](https://github.com/mozilla-mobile/firefox-android) | warning: This repository hosts the Firefox for Android (Fenix), Focus for Android, and Mozilla Android Components projects. It is now developed and maintained as part of Mozilla Central. MPL-2.0: file-level copyleft; modified files must be published. |
| [koin](https://github.com/InsertKoinIO/koin) | Koin - pragmatic dependency injection for Kotlin & Kotlin Multiplatform. Koin DSL or Koin Annotations (JSR-330), compile safe with the Koin Compiler Plugin. |
| [kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines) | Library support for Kotlin coroutines. |
| [leakcanary](https://github.com/square/leakcanary) | A memory leak detection library for Android. |
| [NewPipe](https://github.com/TeamNewPipe/NewPipe) | A libre lightweight streaming front-end for Android. GPL-3.0: derivative works must stay under the GPL. |
| [okhttp](https://github.com/lysine-dev/okhttp) | A meticulous HTTP client for the JVM, Android, and GraalVM. |
| [pokedex](https://github.com/skydoves/Pokedex) | Pokedex demonstrates modern Android development with Hilt, Material Motion, Coroutines, Flow, Jetpack (Room, ViewModel) based on MVVM architecture. |
| [RepoStore](https://github.com/samyak2403/RepoStore) | Explore apps published on GitHub, view release details, and install APKs instantly — all in one place. Developed using pure Kotlin, optimized for modern Android devices. |
| [retrofit](https://github.com/lysine-dev/retrofit) | A type-safe HTTP client for Android and the JVM. |
| [SAI](https://github.com/Aefyr/SAI) | Android split APKs installer. GPL-3.0: derivative works must stay under the GPL. |
| [scrcpy](https://github.com/Genymobile/scrcpy) | Display and control your Android device. |
| [universal android debloater](https://github.com/0x192/universal-android-debloater) | Cross-platform GUI written in Rust using ADB to debloat non-rooted android devices. Improve your privacy, the security and battery life of your device. GPL-3.0: derivative works must stay under the GPL. |

## Builds packages and environments

| Resource | Useful for / constraints |
|---|---|
| [babel (babel)](https://github.com/babel/babel) | Babel is a compiler for writing next generation JavaScript. |
| [berry](https://github.com/yarnpkg/berry) | Active development trunk for Yarn. |
| [brew](https://github.com/Homebrew/brew) | The Package Manager for Everywhere. |
| [cargo](https://github.com/rust-lang/cargo) | The Rust package manager. |
| [farm](https://github.com/farm-fe/farm) | Extremely fast Vite-compatible web build tool written in Rust. |
| [grunt](https://github.com/gruntjs/grunt) | Grunt: The JavaScript Task Runner. |
| [hatch](https://github.com/pypa/hatch) | Modern, extensible Python project management. |
| [home manager](https://github.com/nix-community/home-manager) | Manage a user environment using Nix [maintainer=@khaneliman, @rycee]. |
| [lightningcss](https://github.com/parcel-bundler/lightningcss) | An extremely fast CSS parser, transformer, bundler, and minifier written in Rust. MPL-2.0: file-level copyleft; modified files must be published. |
| [miniforge](https://github.com/conda-forge/miniforge) | A conda-forge distribution. License not detected by GitHub; check the repository license before use. |
| [nix](https://github.com/NixOS/nix) | Nix, the purely functional package manager. LGPL-2.1: dynamic linking is permitted, static linking has obligations. |
| [nixpkgs](https://github.com/NixOS/nixpkgs) | Nix Packages collection & NixOS. |
| [parcel](https://github.com/parcel-bundler/parcel) | The zero configuration build tool for the web. |
| [pdm](https://github.com/pdm-project/pdm) | A modern Python package and dependency manager supporting the latest PEP standards. |
| [peru](https://github.com/buildinspace/peru) | a generic package manager, for including other people's code in your projects. |
| [pip](https://github.com/pypa/pip) | The Python package installer. |
| [pyenv](https://github.com/pyenv/pyenv) | Simple Python version management. |
| [rollup](https://github.com/rollup/rollup) | Next-generation ES module bundler. License not detected by GitHub; check the repository license before use. |
| [rspack](https://github.com/web-infra-dev/rspack) | Fast Rust-based bundler for the web with a modernized webpack API. |
| [sbt](https://github.com/sbt/sbt) | sbt, the interactive build tool. |
| [spack](https://github.com/spack/spack) | A flexible package manager that supports multiple versions, configurations, platforms, and compilers. |
| [webpack](https://github.com/webpack/webpack) | A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. |

## Cloud infrastructure and deployment

| Resource | Useful for / constraints |
|---|---|
| [chalice](https://github.com/aws/chalice) | Python Serverless Microframework for AWS. |
| [compose](https://github.com/docker/compose) | Define and run multi-container applications with Docker. |
| [containerd](https://github.com/containerd/containerd) | An open and reliable container runtime. |
| [devspace](https://github.com/devspace-sh/devspace) | DevSpace - The Fastest Developer Tool for Kubernetes Automate your deployment workflow with DevSpace and develop software directly inside Kubernetes. |
| [dockge](https://github.com/louislam/dockge) | A fancy, easy-to-use and reactive self-hosted docker compose.yaml stack-oriented manager. |
| [dozzle](https://github.com/amir20/dozzle) | Realtime log viewer for containers. Supports Docker, Swarm and K8s. |
| [faas](https://github.com/openfaas/faas) | OpenFaaS - Serverless Functions Made Simple. License not detected by GitHub; check the repository license before use. |
| [fission](https://github.com/fission/fission) | Fast and Simple Serverless Functions for Kubernetes. |
| [functions samples](https://github.com/firebase/functions-samples) | Collection of sample apps showcasing popular use cases using Cloud Functions for Firebase. |
| [k3s](https://github.com/k3s-io/k3s) | Lightweight Kubernetes. |
| [ko](https://github.com/ko-build/ko) | Build and deploy Go applications. |
| [kubeedge](https://github.com/kubeedge/kubeedge) | Kubernetes Native Edge Computing Framework (project under CNCF). |
| [kubernetes goat](https://github.com/madhuakula/kubernetes-goat) | Kubernetes Goat is a "Vulnerable by Design" cluster environment to learn and practice Kubernetes security using an interactive hands-on playground. |
| [linkding](https://github.com/sissbruecker/linkding) | Self-hosted bookmark manager that is designed be to be minimal, fast, and easy to set up using Docker. |
| [moby](https://github.com/moby/moby) | The Moby Project - a collaborative project for the container ecosystem to assemble container-based systems. |
| [nginx](https://github.com/nginx/nginx) | The official NGINX Open Source repository. |
| [nuclio](https://github.com/nuclio/nuclio) | High-Performance Serverless event and data processing platform. |
| [pipeline](https://github.com/tektoncd/pipeline) | A cloud-native Pipeline resource. |
| [podman desktop](https://github.com/podman-desktop/podman-desktop) | Podman Desktop is the best free and open source tool to work with Containers and Kubernetes for developers. Get an intuitive and user-friendly interface to effortlessly build, manage,. |
| [rancher](https://github.com/rancher/rancher) | Complete container management platform. |
| [serverless application model](https://github.com/aws/serverless-application-model) | The AWS Serverless Application Model (AWS SAM) transform is a AWS CloudFormation macro that transforms SAM templates into CloudFormation templates. |
| [serving](https://github.com/knative/serving) | Kubernetes-based, scale-to-zero, request-driven compute. |
| [traefik](https://github.com/traefik/traefik) | The Cloud Native Application Proxy. |
| [workers sdk](https://github.com/cloudflare/workers-sdk) | Home to Wrangler, the CLI for Cloudflare Workers®. |

## Collaboration local state and rich text

| Resource | Useful for / constraints |
|---|---|
| [AFFiNE](https://github.com/toeverything/AFFiNE) | There can be more than Notion and Miro. AFFiNE(pronounced [ə‘fain]) is a next-gen knowledge base that brings planning, sorting and creating all together. Privacy first, open-source, customizable and ready to use. License not detected by GitHub; check the repository license before use. |
| [ckeditor5](https://github.com/ckeditor/ckeditor5) | Powerful rich text editor framework with a modular architecture, modern integrations, and features like collaborative editing. License not detected by GitHub; check the repository license before use. |
| [commonmark spec](https://github.com/commonmark/commonmark-spec) | CommonMark spec, with reference implementations in C and JavaScript. License not detected by GitHub; check the repository license before use. |
| [excalidraw](https://github.com/excalidraw/excalidraw) | Virtual whiteboard for sketching hand-drawn like diagrams. |
| [foam](https://github.com/foambubble/foam) | A personal knowledge management and sharing system for VSCode. License not detected by GitHub; check the repository license before use. |
| [freeplane](https://github.com/freeplane/freeplane) | Application for Mind Mapping, Knowledge Management, Project Management. Develop, organize and communicate your ideas and knowledge in the most effective way. GPL-2.0: derivative works must stay under the GPL. |
| [GitJournal](https://github.com/GitJournal/GitJournal) | Mobile first Note Taking integrated with Git. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [hedgedoc](https://github.com/hedgedoc/hedgedoc) | HedgeDoc - Ideas grow better together. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [joplin](https://github.com/laurent22/joplin) | Joplin - the privacy-focused note taking app with sync capabilities for Windows, macOS, Linux, Android and iOS. License not detected by GitHub; check the repository license before use. |
| [jupytext](https://github.com/jupytext/jupytext) | Jupyter Notebooks as Markdown Documents, Julia, Python or R scripts. |
| [logseq](https://github.com/logseq/logseq) | A privacy-first, open-source platform for knowledge management and collaboration. Download link: http://github.com/logseq/logseq/releases. roadmap: https://logseq.io/p/NX4mc_ggEV. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [markdown it](https://github.com/markdown-it/markdown-it) | Markdown parser, done right. 100% CommonMark support, extensions, syntax plugins & high speed. |
| [marksman](https://github.com/artempyanykh/marksman) | Write Markdown with code assist and intelligence in the comfort of your favourite editor. |
| [markup](https://github.com/github/markup) | Determines which markup library to use to render a content file (e.g. README) on GitHub. |
| [mdast](https://github.com/syntax-tree/mdast) | Markdown Abstract Syntax Tree format. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [MiaoYan](https://github.com/tw93/MiaoYan) | A light, native Markdown notebook for Mac, iPhone and iPad. |
| [Notepads](https://github.com/0x7c13/Notepads) | A modern, lightweight text editor with a minimalist design. |
| [overleaf](https://github.com/overleaf/overleaf) | A web-based collaborative LaTeX editor. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [penpot](https://github.com/penpot/penpot) | Penpot: The open-source design platform for Product teams that need scalable collaboration. MPL-2.0: file-level copyleft; modified files must be published. |
| [plantuml](https://github.com/plantuml/plantuml) | Generate diagrams from textual description. LGPL-3.0: dynamic linking is permitted, static linking has obligations. |
| [QOwnNotes](https://github.com/pbek/QOwnNotes) | QOwnNotes is a plain-text file notepad and todo-list manager with Markdown support and Nextcloud / ownCloud integration. GPL-2.0: derivative works must stay under the GPL. |
| [quill](https://github.com/slab/quill) | Quill is a modern WYSIWYG editor built for compatibility and extensibility. |
| [remark](https://github.com/remarkjs/remark) | markdown processor powered by plugins part of the @unifiedjs collective. |
| [roomGPT](https://github.com/Nutlope/roomGPT) | Upload a photo of your room to generate your dream room with AI. |
| [sharelatex](https://github.com/overleaf/overleaf) | A web-based collaborative LaTeX editor. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [silverbullet](https://github.com/silverbulletmd/silverbullet) | The malleable knowledge base for you and your team. Powered by Markdown and Lua. |
| [tldraw](https://github.com/tldraw/tldraw) | Build infinite canvas apps in React with the tldraw SDK. World's best, top-most agent recommended #1 five star SDK. License not detected by GitHub; check the repository license before use. |
| [vnote](https://github.com/vnotex/vnote) | A pleasant note-taking platform with native speed, majoring in Markdown, MindMap, Typst, and plain text. LGPL-3.0: dynamic linking is permitted, static linking has obligations. |
| [Zettlr](https://github.com/Zettlr/Zettlr) | Your One-Stop Publication Workbench. GPL-3.0: derivative works must stay under the GPL. |

## Data science and engineering tools

| Resource | Useful for / constraints |
|---|---|
| [altair](https://github.com/vega/altair) | Declarative visualization library for Python. |
| [arrow](https://github.com/apache/arrow) | Apache Arrow is the universal columnar format and multi-language toolbox for fast data interchange and in-memory analytics. |
| [cudf](https://github.com/NVIDIA/cudf) | cuDF - GPU DataFrame Library. |
| [datasets](https://github.com/huggingface/datasets) | The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools. |
| [datasette](https://github.com/simonw/datasette) | An open source multi-tool for exploring and publishing data. |
| [ipython](https://github.com/ipython/ipython) | Official repository for IPython itself. Other repos in the IPython organization contain things like the website, documentation builds, etc. |
| [jupyter](https://github.com/jupyter/jupyter) | Jupyter metapackage for installation and documentation. |
| [kubeflow](https://github.com/kubeflow/kubeflow) | The Cloud Native AI Platform. |
| [modin](https://github.com/modin-project/modin) | Modin: Scale your Pandas workflows by changing a single line of code. |
| [openml](https://github.com/openml/OpenML) | Open Machine Learning. |
| [plot](https://github.com/observablehq/plot) | A concise API for exploratory data visualization implementing a layered grammar of graphics. |
| [spaghetti](https://github.com/pysal/spaghetti) | SPAtial GrapHs: nETworks, Topology, & Inference. |
| [spark](https://github.com/apache/spark) | Apache Spark - A unified analytics engine for large-scale data processing. |
| [sqlite utils](https://github.com/simonw/sqlite-utils) | Python CLI utility and library for manipulating SQLite databases. |
| [tensorflow](https://github.com/tensorflow/tensorflow) | An Open Source Machine Learning Framework for Everyone. |
| [vaex](https://github.com/vaexio/vaex) | Out-of-Core hybrid Apache Arrow/NumPy DataFrame for Python, ML, visualization and exploration of big tabular data at a billion rows per second. |
| [vega lite](https://github.com/vega/vega-lite) | A concise grammar of interactive graphics, built on Vega. |
| [xarray](https://github.com/pydata/xarray) | N-D labeled arrays and datasets in Python. |

## Databases data access and analytics

| Resource | Useful for / constraints |
|---|---|
| [asyncpg](https://github.com/MagicStack/asyncpg) | A fast PostgreSQL Database Client Library for Python/asyncio. |
| [chartdb](https://github.com/chartdb/chartdb) | Database diagrams editor that allows you to visualize and design your DB with a single query. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [cockroach](https://github.com/cockroachdb/cockroach) | CockroachDB — the cloud native, distributed SQL database designed for high availability, effortless scale, and control over data placement. License not detected by GitHub; check the repository license before use. |
| [dbal](https://github.com/doctrine/dbal) | Doctrine Database Abstraction Layer. |
| [dbeaver](https://github.com/dbeaver/dbeaver) | Free universal database tool and SQL client. |
| [diesel](https://github.com/diesel-rs/diesel) | A safe, extensible ORM and Query Builder for Rust. |
| [dolt](https://github.com/dolthub/dolt) | Dolt – Git for Data. |
| [doris](https://github.com/apache/doris) | Apache Doris is a real-time analytics and hybrid search database for AI agents. |
| [drizzle orm](https://github.com/drizzle-team/drizzle-orm) | ORM. |
| [ent](https://github.com/ent/ent) | An entity framework for Go. |
| [gorm](https://github.com/go-gorm/gorm) | The fantastic ORM library for Golang, aims to be developer friendly. |
| [HeidiSQL](https://github.com/HeidiSQL/HeidiSQL) | A lightweight client for managing MariaDB, MySQL, SQL Server, PostgreSQL, SQLite, Interbase and Firebird, written in Delphi and Lazarus/FreePascal. GPL-2.0: derivative works must stay under the GPL. |
| [knex](https://github.com/knex/knex) | A query builder for PostgreSQL, MySQL, CockroachDB, SQL Server, SQLite3 and Oracle, designed to be flexible, portable, and fun to use. |
| [kysely](https://github.com/kysely-org/kysely) | A type-safe TypeScript SQL query builder. |
| [mongo](https://github.com/mongodb/mongo) | The MongoDB Database. License not detected by GitHub; check the repository license before use. |
| [neo4j](https://github.com/neo4j/neo4j) | Graphs for Everyone. GPL-3.0: derivative works must stay under the GPL. |
| [node postgres](https://github.com/brianc/node-postgres) | PostgreSQL client for node.js. |
| [octosql](https://github.com/cube2222/octosql) | OctoSQL is a query tool that allows you to join, analyse and transform data from multiple databases and file formats using SQL. MPL-2.0: file-level copyleft; modified files must be published. |
| [postgres](https://github.com/postgres/postgres) | Mirror of the official PostgreSQL GIT repository. Note that this is just a *mirror* - we don't work with pull requests on github. To contribute, please see https://wiki.postgresql.org/wiki/Submitting_a_Patch. License not detected by GitHub; check the repository license before use. |
| [postgres (porsager)](https://github.com/porsager/postgres) | Postgres.js - The Fastest full featured PostgreSQL client. |
| [questdb](https://github.com/questdb/questdb) | QuestDB is a high performance, open-source, time-series database. |
| [sequelize](https://github.com/sequelize/sequelize) | Feature-rich ORM for modern Node.js and TypeScript, it supports PostgreSQL (with JSON and JSONB support), MySQL, MariaDB, SQLite, MS SQL Server, Snowflake, Oracle DB, DB2 and DB2 for IBM i. |
| [sql studio](https://github.com/frectonz/sql-studio) | SQL Database Explorer [SQLite, libSQL, PostgreSQL, MySQL/MariaDB, ClickHouse, DuckDB, Microsoft SQL Server]. |
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | Automatic SQL injection and database takeover tool. License not detected by GitHub; check the repository license before use. |
| [tidb](https://github.com/pingcap/tidb) | TiDB is built for agentic workloads that grow unpredictably, with ACID guarantees and native support for transactions, analytics, and vector search. No data silos. No noisy neighbors. No infrastructure ceiling. |
| [tortoise orm](https://github.com/tortoise/tortoise-orm) | Familiar asyncio ORM for python, built with relations in mind. |
| [typeorm](https://github.com/typeorm/typeorm) | TypeScript & JavaScript ORM for Node.js — supports PostgreSQL, MySQL, MariaDB, SQLite, SQL Server, Oracle, and more. |

## Desktop mobile and device SDKs

| Resource | Useful for / constraints |
|---|---|
| [arduino esp32](https://github.com/espressif/arduino-esp32) | Arduino core for the ESP32 family of SoCs. LGPL-2.1: dynamic linking is permitted, static linking has obligations. |
| [arduino ide](https://github.com/arduino/arduino-ide) | Arduino IDE 2.x. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [capacitor](https://github.com/ionic-team/capacitor) | Build cross-platform Native Progressive Web Apps for iOS, Android, and the Web. |
| [cordova android](https://github.com/apache/cordova-android) | Apache Cordova Android. |
| [create react native app](https://github.com/expo/create-react-native-app) | Create React Native apps that run on iOS, Android, and web. |
| [egui](https://github.com/emilk/egui) | egui: an easy-to-use immediate mode GUI in Rust that runs on both web and native. |
| [engine](https://github.com/flutter-team-archive/engine) | The Flutter engine. |
| [expo](https://github.com/expo/expo) | An open-source framework for making universal native apps with React. Expo runs on Android, iOS, and the web. |
| [fiddle](https://github.com/electron/fiddle) | electron: The easiest way to get started with Electron. |
| [flet](https://github.com/flet-dev/flet) | Build realtime web, mobile and desktop apps in Python only. No frontend experience required. |
| [fluent reader](https://github.com/yang991178/fluent-reader) | Modern desktop RSS reader built with Electron, React, and Fluent UI. |
| [flutter boost](https://github.com/alibaba/flutter_boost) | FlutterBoost is a Flutter plugin which enables hybrid integration of Flutter for your existing native apps with minimum efforts. |
| [flutter server box](https://github.com/lollipopkit/flutter_server_box) | ServerBox - high performance server toolbox app & server written in Flutter & Rust. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [flutter webrtc](https://github.com/flutter-webrtc/flutter-webrtc) | WebRTC plugin for Flutter Mobile/Desktop/Web. |
| [go flutter](https://github.com/go-flutter-desktop/go-flutter) | Flutter on Windows, MacOS and Linux - based on Flutter Embedding, Go and GLFW. |
| [iced](https://github.com/iced-rs/iced) | A cross-platform GUI library for Rust, inspired by Elm. |
| [micropython](https://github.com/micropython/micropython) | MicroPython - a lean and efficient Python implementation for microcontrollers and constrained systems. License not detected by GitHub; check the repository license before use. |
| [PakePlus](https://github.com/Sjj1024/PakePlus) | Turn any webpage/HTML/Vue/React and so on into desktop and mobile app under 5M with easy in few minutes. 轻松将任意网站/HTML/Vue/React等项目构建为轻量级(小于5M)多端桌面应用和手机应用仅需几分钟. https://ppofficial.netlify.app. |
| [pico sdk](https://github.com/raspberrypi/pico-sdk) | Repository with no description on GitHub. |
| [platformio core](https://github.com/platformio/platformio-core) | Your Gateway to Embedded Software Development Excellence :alien. |
| [pyglet](https://github.com/pyglet/pyglet) | pyglet is a cross-platform windowing and multimedia library for Python, for developing games and other visually rich applications. |
| [pyside setup](https://github.com/pyside/pyside-setup) | Git super project for PySide. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [qtbase](https://github.com/qt/qtbase) | Qt Base (Core, Gui, Widgets, Network, ...). No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [react native (facebook)](https://github.com/react/react-native) | A framework for building native applications using React. |
| [react native windows](https://github.com/microsoft/react-native-windows) | A framework for building native Windows apps with React. License not detected by GitHub; check the repository license before use. |
| [rubick](https://github.com/rubickCenter/rubick) | Electron based open source toolbox, free integration of rich plug-ins. 基于 electron 的开源工具箱，自由集成丰富插件。. |
| [slint](https://github.com/slint-ui/slint) | Slint is an open-source declarative GUI toolkit to build native user interfaces for Rust, C++, JavaScript, or Python apps. License not detected by GitHub; check the repository license before use. |
| [termux app](https://github.com/termux/termux-app) | Termux - a terminal emulator application for Android OS extendible by variety of packages. License not detected by GitHub; check the repository license before use. |

## Documents OCR and file formats

| Resource | Useful for / constraints |
|---|---|
| [DesktopEditors](https://github.com/ONLYOFFICE/DesktopEditors) | Open-source office suite pack that comprises all the tools you need to work with documents, spreadsheets, presentations, PDFs, and PDF forms on Windows, Linux, and macOS. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [doctr](https://github.com/mindee/doctr) | docTR (Document Text Recognition) - a seamless, high-performing & accessible library for OCR-related tasks powered by Deep Learning. Ongoing development and maintenance by t2k. |
| [docx](https://github.com/dolanmiu/docx) | Easily generate and modify .docx files with JS/TS with a nice declarative API. Works for Node and on the Browser. |
| [donut](https://github.com/clovaai/donut) | Official Implementation of OCR-free Document Understanding Transformer (Donut) and Synthetic Document Generator (SynthDoG), ECCV 2022. |
| [file](https://github.com/file/file) | Read-only mirror of file CVS repository, updated every half hour. NOTE: do not make pull requests here, nor comment any commits, submit them usual way to bug tracker or to the mailing list. License not detected by GitHub; check the repository license before use. |
| [grobid](https://github.com/grobidOrg/grobid) | A machine learning software for extracting information from scholarly documents. |
| [kcc](https://github.com/ciromattia/kcc) | KCC (a.k.a. Kindle Comic Converter) is a comic and manga converter for ebook readers. |
| [layout parser](https://github.com/Layout-Parser/layout-parser) | A Unified Toolkit for Deep Learning Based Document Image Analysis. |
| [libyal](https://github.com/libyal/libyal) | Yet another library library (and tools). |
| [liteparse](https://github.com/run-llama/liteparse) | A fast, helpful, and open-source document parser. |
| [MinerU](https://github.com/opendatalab/MinerU) | Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows. License not detected by GitHub; check the repository license before use. |
| [noteshrink](https://github.com/mzucker/noteshrink) | Convert scans of handwritten notes to beautiful, compact PDFs. |
| [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched. MPL-2.0: file-level copyleft; modified files must be published. |
| [Parsr](https://github.com/axa-group/Parsr) | Transforms PDF, Documents and Images into Enriched Structured Data. |
| [pdf lib](https://github.com/Hopding/pdf-lib) | Create and modify PDF documents in any JavaScript environment. |
| [pdfarranger](https://github.com/pdfarranger/pdfarranger) | Small python-gtk application, which helps the user to merge or split PDF documents and rotate, crop and rearrange their pages using an interactive and intuitive graphical interface. GPL-3.0: derivative works must stay under the GPL. |
| [pdfminer.six](https://github.com/pdfminer/pdfminer.six) | Community maintained fork of pdfminer - we fathom PDF. |
| [percollate](https://github.com/danburzo/percollate) | A command-line tool to turn web pages into readable PDF, EPUB, HTML, or Markdown docs. |
| [PyMuPDF](https://github.com/pymupdf/PyMuPDF) | PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [tesseract](https://github.com/tesseract-ocr/tesseract) | Tesseract Open Source OCR Engine (main repository). |
| [tika](https://github.com/apache/tika) | The Apache Tika toolkit detects and extracts metadata and text from over a thousand different file types (such as PPT, XLS, and PDF). |
| [zerox](https://github.com/getomni-ai/zerox) | OCR & Document Extraction using vision models. |

## Editor and terminal extensions

| Resource | Useful for / constraints |
|---|---|
| [ale](https://github.com/dense-analysis/ale) | Check syntax in Vim/Neovim asynchronously and fix files, with Language Server Protocol (LSP) support. |
| [awesome emacs](https://github.com/emacs-tw/awesome-emacs) | A community driven list of useful Emacs packages, libraries and other items. |
| [awesome neovim](https://github.com/rockerBOO/awesome-neovim) | Collections of awesome neovim plugins. |
| [coc.nvim](https://github.com/neoclide/coc.nvim) | Nodejs extension host for vim & neovim, load extensions like VSCode and host language servers. |
| [codetour](https://github.com/microsoft/codetour) | VS Code extension that allows you to record and play back guided tours of codebases, directly within the editor. |
| [glow](https://github.com/charmbracelet/glow) | Render markdown on the CLI, with pizzazz! |
| [lazy.nvim](https://github.com/folke/lazy.nvim) | A modern plugin manager for Neovim. |
| [LazyVim](https://github.com/LazyVim/LazyVim) | Neovim config for the lazy. |
| [lsp mode](https://github.com/emacs-lsp/lsp-mode) | Emacs client/library for the Language Server Protocol. GPL-3.0: derivative works must stay under the GPL. |
| [nerd fonts](https://github.com/ryanoasis/nerd-fonts) | Iconic font aggregator, collection, & patcher. 3,600+ icons, 50+ patched fonts: Hack, Source Code Pro, more. Glyph collections: Font Awesome, Material Design Icons, Octicons, & more. License not detected by GitHub; check the repository license before use. |
| [NvChad](https://github.com/NvChad/NvChad) | Blazing fast Neovim framework providing solid defaults and a beautiful UI, enhancing your neovim experience. GPL-3.0: derivative works must stay under the GPL. |
| [nvim treesitter](https://github.com/nvim-treesitter/nvim-treesitter) | Nvim Treesitter configurations and abstraction layer. |
| [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (rails, git, macOS, hub, docker, homebrew, node, php, python, etc),. |
| [oil.nvim](https://github.com/stevearc/oil.nvim) | Neovim file explorer: edit your filesystem like a buffer. |
| [spacemacs](https://github.com/syl20bnr/spacemacs) | A community-driven Emacs distribution - The best editor is neither Emacs nor Vim, it's Emacs *and* Vim! GPL-3.0: derivative works must stay under the GPL. |
| [telescope.nvim](https://github.com/nvim-telescope/telescope.nvim) | Find, Filter, Preview, Pick. All lua, all the time. |
| [vim](https://github.com/vim/vim) | The official Vim repository. |
| [vim galore](https://github.com/mhinz/vim-galore) | mortar_board: All things Vim! |
| [vim plug](https://github.com/junegunn/vim-plug) | hibiscus: Minimalist Vim Plugin Manager. |
| [zellij](https://github.com/zellij-org/zellij) | A terminal workspace with batteries included. |

## Feature flags configuration and secrets

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

## Game creation assets and automation

| Resource | Useful for / constraints |
|---|---|
| [awesome bevy](https://github.com/bevyengine/bevy-assets) | A collection of Bevy assets, plugins, learning resources, and apps made by the community. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [awesome godot](https://github.com/Calinou/awesome-godot) | A curated list of free/libre plugins, scripts and add-ons for Godot. |
| [beehave](https://github.com/bitbrain/beehave) | behavior tree AI for Godot Engine. |
| [bullet3](https://github.com/bulletphysics/bullet3) | Bullet Physics SDK: real-time collision detection and multi-physics simulation for VR, games, visual effects, robotics, machine learning etc. License not detected by GitHub; check the repository license before use. |
| [dialogic](https://github.com/dialogic-godot/dialogic) | Create Dialogs, Visual Novels, RPGs, and manage Characters with Godot to create your Game! |
| [entt](https://github.com/skypjack/entt) | Gaming meets modern C++ - a fast and reliable entity component system (ECS) and much more. |
| [FNA](https://github.com/FNA-XNA/FNA) | FNA - Accuracy-focused XNA4 reimplementation for open platforms. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [FXGL](https://github.com/AlmasB/FXGL) | Java / JavaFX / Kotlin Game Library (Engine). |
| [GameDev Resources](https://github.com/Kavex/GameDev-Resources) | video_game: :game_die: A wonderful list of Game Development resources. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [GameFramework](https://github.com/EllanJiang/GameFramework) | This is literally a game framework, based on Unity game engine. It encapsulates commonly used game modules during development, and, to a large degree, standardises the process,. |
| [godot demo projects](https://github.com/godotengine/godot-demo-projects) | Demonstration and Template Projects. |
| [godot jolt](https://github.com/godot-jolt/godot-jolt) | Godot Jolt is a Godot extension that integrates the Jolt physics engine. |
| [libgdx](https://github.com/libgdx/libgdx) | Desktop/Android/HTML5/iOS Java game development framework. |
| [love](https://github.com/love2d/love) | LÖVE is an awesome 2D game framework for Lua. License not detected by GitHub; check the repository license before use. |
| [macroquad](https://github.com/not-fl3/macroquad) | Cross-platform game engine in Rust. |
| [magictools](https://github.com/ellisonleao/magictools) | video_game: :pencil: A list of Game Development resources to make magic happen. |
| [MonoGame](https://github.com/MonoGame/MonoGame) | One framework for creating powerful cross-platform games. License not detected by GitHub; check the repository license before use. |
| [PankuConsole](https://github.com/Ark2000/PankuConsole) | Feature-packed real-time debugging toolkit for Godot Engine. |
| [QFramework](https://github.com/liangxiegame/QFramework) | Godot/Unity3D System Design Architecture. |
| [redot engine](https://github.com/Redot-Engine/redot-engine) | Redot Engine – Multi-platform 2D and 3D game engine. |
| [Terrain3D](https://github.com/TokisanGames/Terrain3D) | A high performance, editable terrain system for Godot 4. |
| [UnityCsReference](https://github.com/Unity-Technologies/UnityCsReference) | Unity C# reference source code. License not detected by GitHub; check the repository license before use. |

## Graphics multimedia scientific and geospatial

| Resource | Useful for / constraints |
|---|---|
| [aseprite](https://github.com/aseprite/aseprite) | Animated sprite editor & pixel art tool (Windows, macOS, Linux). No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [bokeh](https://github.com/bokeh/bokeh) | Interactive Data Visualization in the browser, from Python. |
| [d3](https://github.com/d3/d3) | Bring data to life with SVG, Canvas and HTML. :bar_chart::chart_with_upwards_trend::tada. |
| [digital video introduction](https://github.com/leandromoreira/digital_video_introduction) | A hands-on introduction to video technology: image, video, codec (av1, vp9, h265) and more (ffmpeg encoding). Translations. |
| [editly](https://github.com/mifi/editly) | Slick, declarative command line video editing & API. |
| [engine (playcanvas)](https://github.com/playcanvas/engine) | Powerful web graphics runtime built on WebGL, WebGPU, WebXR and glTF. |
| [ffmpeg libav tutorial](https://github.com/leandromoreira/ffmpeg-libav-tutorial) | FFmpeg libav tutorial - learn how media works from basic to transmuxing, transcoding and more. Translations. |
| [ffsubsync](https://github.com/smacke/ffsubsync) | Automagically synchronize subtitles with video. |
| [filament](https://github.com/google/filament) | Filament is a real-time physically based rendering engine for Android, iOS, Windows, Linux, macOS, WebGPU, and WebGL2. |
| [gfx](https://github.com/gfx-rs/gfx) | [maintenance mode] A low-overhead Vulkan-like GPU API for Rust. |
| [gifify](https://github.com/vvo/gifify) | Convert any video file to an optimized animated GIF. |
| [glTF](https://github.com/KhronosGroup/glTF) | glTF – Runtime 3D Asset Delivery. License not detected by GitHub; check the repository license before use. |
| [HandBrake](https://github.com/HandBrake/HandBrake) | HandBrake's development repository. License not detected by GitHub; check the repository license before use. |
| [inkscape](https://github.com/inkscape/inkscape) | Project Website: https://inkscape.org - Code Repository: https://gitlab.com/inkscape/inkscape - Draw freely. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [krita](https://github.com/KDE/krita) | Krita is a free and open source cross-platform application that offers an end-to-end solution for creating digital art files from scratch built on the KDE and Qt frameworks. GPL-3.0: derivative works must stay under the GPL. |
| [lossless cut](https://github.com/mifi/lossless-cut) | The swiss army knife of lossless video/audio editing. GPL-2.0: derivative works must stay under the GPL. |
| [lwjgl3](https://github.com/LWJGL/lwjgl3) | LWJGL is a Java library that enables cross-platform access to popular native APIs useful in the development of graphics (OpenGL, Vulkan, bgfx), audio (OpenAL, Opus), parallel computing (OpenCL, CUDA) and XR (OpenVR, LibOVR,. |
| [mapbox gl js](https://github.com/mapbox/mapbox-gl-js) | Interactive, thoroughly customizable maps in the browser, powered by vector tiles and WebGL. License not detected by GitHub; check the repository license before use. |
| [matplotlib](https://github.com/matplotlib/matplotlib) | matplotlib: plotting with Python. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [mini3d](https://github.com/skywind3000/mini3d) | 3D Software Renderer in 700 Lines !! |
| [model viewer](https://github.com/google/model-viewer) | Easily display interactive 3D models on the web and in AR! |
| [mpv](https://github.com/mpv-player/mpv) | Command line media player. License not detected by GitHub; check the repository license before use. |
| [mypaint](https://github.com/mypaint/mypaint) | MyPaint is a simple drawing and painting program that works well with Wacom-style graphics tablets. GPL-2.0: derivative works must stay under the GPL. |
| [proj4js](https://github.com/proj4js/proj4js) | JavaScript library to transform coordinates from one coordinate system to another, including datum transformations. License not detected by GitHub; check the repository license before use. |
| [pyvista](https://github.com/pyvista/pyvista) | 3D visualization and mesh analysis for science and engineering. |
| [QGIS](https://github.com/qgis/QGIS) | QGIS is a free, open source, cross platform (lin/win/mac) geographical information system (GIS). GPL-2.0: derivative works must stay under the GPL. |
| [react three fiber](https://github.com/pmndrs/react-three-fiber) | A React renderer for Three.js. |
| [SFML](https://github.com/SFML/SFML) | Simple and Fast Multimedia Library. |
| [SPIRV Cross](https://github.com/KhronosGroup/SPIRV-Cross) | SPIRV-Cross is a practical tool and library for performing reflection on SPIR-V and disassembling SPIR-V back to high level languages. |
| [vega](https://github.com/vega/vega) | A visualization grammar. |
| [Vulkan Samples](https://github.com/KhronosGroup/Vulkan-Samples) | One stop solution for all Vulkan samples. |
| [Vulkan ValidationLayers](https://github.com/KhronosGroup/Vulkan-ValidationLayers) | Vulkan Validation Layers (VVL). License not detected by GitHub; check the repository license before use. |
| [wgpu](https://github.com/gfx-rs/wgpu) | A cross-platform, safe, pure-Rust graphics API. |
| [WickedEngine](https://github.com/turanszkij/WickedEngine) | 3D engine with modern graphics. |

## Infrastructure as code and cloud-native operations

| Resource | Useful for / constraints |
|---|---|
| [awesome tf](https://github.com/shuaibiyy/awesome-tf) | Curated list of resources on HashiCorp's Terraform and OpenTofu. |
| [awx](https://github.com/ansible/awx) | AWX provides a web-based user interface, REST API, and task engine built on top of Ansible. It is one of the upstream projects for Red Hat Ansible Automation Platform. License not detected by GitHub; check the repository license before use. |
| [boilerplates](https://github.com/ChristianLempa/boilerplates) | Create reusable templates and turn them into configurable workloads for homelabs and self-hosted infrastructure. Free and Open-Source. |
| [cloudformation guard](https://github.com/aws-cloudformation/cloudformation-guard) | Guard offers a policy-as-code domain-specific language (DSL) to write rules and validate JSON- and YAML-formatted data such as CloudFormation Templates, K8s configurations,. |
| [cluster api](https://github.com/kubernetes-sigs/cluster-api) | Home for Cluster API, a subproject of sig-cluster-lifecycle. |
| [consul](https://github.com/hashicorp/consul) | Consul is a distributed, highly available, and data center aware solution to connect and configure applications across dynamic, distributed infrastructure. License not detected by GitHub; check the repository license before use. |
| [external secrets](https://github.com/external-secrets/external-secrets) | External Secrets Operator reads information from a third-party service like AWS Secrets Manager and automatically injects the values as Kubernetes Secrets. |
| [gatekeeper](https://github.com/open-policy-agent/gatekeeper) | Policy Controller for Kubernetes. |
| [istio](https://github.com/istio/istio) | Connect, secure, control, and observe services. |
| [kind](https://github.com/kubernetes-sigs/kind) | Kubernetes IN Docker - local clusters for testing Kubernetes. |
| [kops](https://github.com/kubernetes/kops) | Kubernetes Operations (kOps) - Production Grade k8s Installation, Upgrades and Management. |
| [kube hunter](https://github.com/aquasecurity/kube-hunter) | Hunt for security weaknesses in Kubernetes clusters. |
| [kubespray](https://github.com/kubernetes-sigs/kubespray) | Deploy a Production Ready Kubernetes Cluster. |
| [kubevirt](https://github.com/kubevirt/kubevirt) | Kubernetes Virtualization API and runtime in order to define and manage virtual machines. |
| [metrics server](https://github.com/kubernetes-sigs/metrics-server) | Scalable and efficient source of container resource metrics for Kubernetes built-in autoscaling pipelines. |
| [minikube](https://github.com/kubernetes/minikube) | Run Kubernetes locally. |
| [opa](https://github.com/open-policy-agent/opa) | Open Policy Agent (OPA) is an open source, general-purpose policy engine. |
| [packer](https://github.com/hashicorp/packer) | Packer is a tool for creating identical machine images for multiple platforms from a single source configuration. License not detected by GitHub; check the repository license before use. |
| [polaris](https://github.com/FairwindsOps/polaris) | Validation of best practices in your Kubernetes clusters. |
| [Reloader](https://github.com/stakater/Reloader) | A Kubernetes controller to watch changes in ConfigMap and Secrets and do rolling upgrades on Pods with their associated Deployment, StatefulSet, DaemonSet and DeploymentConfig – [Star] if you're using it! |
| [semaphore](https://github.com/semaphoreui/semaphore) | Modern UI and powerful API for Ansible, Terraform/OpenTofu/Terragrunt, PowerShell and other DevOps tools. |
| [terraform inventory](https://github.com/adammck/terraform-inventory) | Terraform State Ansible Dynamic Inventory. |
| [terraform provider kubernetes](https://github.com/hashicorp/terraform-provider-kubernetes) | Terraform Kubernetes provider. MPL-2.0: file-level copyleft; modified files must be published. |
| [typhoon](https://github.com/poseidon/typhoon) | Minimal and free Kubernetes distribution with Terraform. |
| [vagrant](https://github.com/hashicorp/vagrant) | Vagrant is a tool for building and distributing development environments. |
| [vcluster](https://github.com/loft-sh/vcluster) | vCluster creates tenant clusters: fully isolated environments delivered as managed Kubernetes, or as the foundation for Slurm, Ray, Run:ai and inference clusters. |

## Languages and runtimes

| Resource | Useful for / constraints |
|---|---|
| [assemblyscript](https://github.com/AssemblyScript/assemblyscript) | A TypeScript-like language for WebAssembly. |
| [binaryen](https://github.com/WebAssembly/binaryen) | Optimizer and compiler/toolchain library for WebAssembly. |
| [book](https://github.com/rust-lang/book) | The Rust Programming Language. License not detected by GitHub; check the repository license before use. |
| [crystal](https://github.com/crystal-lang/crystal) | The Crystal Programming Language. |
| [dmd](https://github.com/d-lang-zz/dmd) | D Compiler. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [elixir](https://github.com/elixir-lang/elixir) | Simple from zero to scale. |
| [emscripten](https://github.com/emscripten-core/emscripten) | Emscripten: An LLVM-to-WebAssembly Compiler. License not detected by GitHub; check the repository license before use. |
| [gofumpt](https://github.com/mvdan/gofumpt) | A stricter gofmt. |
| [guide](https://github.com/uber-go/guide) | The Uber Go Style Guide. |
| [jdk](https://github.com/openjdk/jdk) | JDK main-line development https://openjdk.org/projects/jdk. GPL-2.0: derivative works must stay under the GPL. |
| [julia](https://github.com/JuliaLang/julia) | The Julia Programming Language. |
| [lua](https://github.com/lua/lua) | A copy of the Lua development repository, as seen by the Lua team. Mirrored irregularly. All communication should be through the Lua mailing list https://www.lua.org/lua-l.html. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [Nim](https://github.com/nim-lang/Nim) | Nim is a statically typed compiled systems programming language. It combines successful concepts from mature languages like Python, Ada and Modula. License not detected by GitHub; check the repository license before use. |
| [otp](https://github.com/erlang/otp) | Erlang/OTP. |
| [perl5](https://github.com/Perl/perl5) | The Perl programming language. License not detected by GitHub; check the repository license before use. |
| [php src](https://github.com/php/php-src) | The PHP Interpreter. |
| [rust analyzer](https://github.com/rust-lang/rust-analyzer) | A Rust compiler front-end for IDEs. |
| [rustlings](https://github.com/rust-lang/rustlings) | crab: Small exercises to get you used to reading and writing Rust code! |
| [RustPython](https://github.com/RustPython/RustPython) | A Python Interpreter written in Rust. |
| [rustup](https://github.com/rust-lang/rustup) | The Rust toolchain installer. |
| [tools](https://github.com/golang/tools) | [mirror] Go Tools. |
| [wabt](https://github.com/WebAssembly/wabt) | The WebAssembly Binary Toolkit. |
| [ziglings](https://github.com/ratfactor/ziglings) | Learn the Zig programming language by fixing tiny broken programs. |
| [zls](https://github.com/zigtools/zls) | A language server for Zig supporting developers with features like autocomplete and goto definition. |

## Linux and Unix tooling

| Resource | Useful for / constraints |
|---|---|
| [Bash Oneliner](https://github.com/onceupon/Bash-Oneliner) | A collection of handy Bash One-Liners and terminal tricks for data processing and Linux system maintenance. |
| [bubbles](https://github.com/charmbracelet/bubbles) | TUI components for Bubble Tea. |
| [console](https://github.com/symfony/console) | Eases the creation of beautiful and testable command line interfaces. |
| [dotdrop](https://github.com/deadc0de6/dotdrop) | Save your dotfiles once, deploy them everywhere. GPL-3.0: derivative works must stay under the GPL. |
| [fastfetch](https://github.com/fastfetch-cli/fastfetch) | A maintained, feature-rich and performance oriented, neofetch like system information tool. |
| [fisher](https://github.com/jorgebucaran/fisher) | A plugin manager for Fish. |
| [FTXUI](https://github.com/ArthurSonzogni/FTXUI) | computer: C++ Functional Terminal User Interface. :heart. |
| [hstr](https://github.com/dvorka/hstr) | Bash and Zsh shell history TUI suggest box - easily view, navigate, search and manage your command history. |
| [inshellisense](https://github.com/microsoft/inshellisense) | IDE style command line auto complete. |
| [lynis](https://github.com/CISOfy/lynis) | Lynis - Security auditing tool for Linux, macOS, and UNIX-based systems. Assists with compliance testing (HIPAA/ISO27001/PCI DSS) and system hardening. Agentless, and installation optional. GPL-3.0: derivative works must stay under the GPL. |
| [modern unix](https://github.com/ibraheemdev/modern-unix) | A collection of modern/faster/saner alternatives to common unix commands. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [nvm](https://github.com/nvm-sh/nvm) | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions. |
| [terminalizer](https://github.com/faressoft/terminalizer) | Record your terminal and generate animated gif images or share a web player. |
| [terminals are sexy](https://github.com/k4m4/terminals-are-sexy) | A curated list of Terminal frameworks, plugins & resources for CLI lovers. |
| [the art of command line](https://github.com/jlevy/the-art-of-command-line) | Master the command line, in one page. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [tldr](https://github.com/tldr-pages/tldr) | Collaborative cheatsheets for console commands . License not detected by GitHub; check the repository license before use. |
| [yadm](https://github.com/yadm-dev/yadm) | Yet Another Dotfiles Manager. GPL-3.0: derivative works must stay under the GPL. |
| [yazi](https://github.com/sxyazi/yazi) | Blazing fast terminal file manager written in Rust, based on async I/O. |

## Observability debugging and operations

| Resource | Useful for / constraints |
|---|---|
| [btrace](https://github.com/btraceio/btrace) | Production-safe dynamic tracing and diagnostics for Java applications—attach to live JVMs with no restart or recompilation. |
| [coroot](https://github.com/coroot/coroot) | Coroot is an open-source observability and APM tool with AI-powered Root Cause Analysis. It combines metrics, logs, traces, continuous profiling, and SLO-based alerting with predefined dashboards and inspections. |
| [datadog agent](https://github.com/DataDog/datadog-agent) | Main repository for Datadog Agent. |
| [FlameGraph](https://github.com/brendangregg/FlameGraph) | Stack trace visualizer. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [fluent bit (fluent)](https://github.com/fluent/fluent-bit) | Fast and Lightweight Logs, Metrics and Traces processor for Linux, BSD, OSX and Windows. |
| [highlight](https://github.com/highlight/highlight) | highlight.io: The open source, full-stack monitoring platform. Error monitoring, session replay, logging, distributed tracing, and more. License not detected by GitHub; check the repository license before use. |
| [kibana](https://github.com/elastic/kibana) | Your window into all of your data. License not detected by GitHub; check the repository license before use. |
| [logstash](https://github.com/elastic/logstash) | Logstash - transport and process your logs, events, or other data. License not detected by GitHub; check the repository license before use. |
| [minitrace rust](https://github.com/tikv/minitrace-rust) | Extremely fast tracing library for Rust. |
| [netdata](https://github.com/netdata/netdata) | The fastest path to AI-powered full stack observability, even for lean teams. GPL-3.0: derivative works must stay under the GPL. |
| [opentelemetry cpp](https://github.com/open-telemetry/opentelemetry-cpp) | The OpenTelemetry C++ Client. |
| [opentelemetry dotnet](https://github.com/open-telemetry/opentelemetry-dotnet) | The OpenTelemetry .NET Client. |
| [opentelemetry go](https://github.com/open-telemetry/opentelemetry-go) | OpenTelemetry Go API and SDK. |
| [opentelemetry java](https://github.com/open-telemetry/opentelemetry-java) | OpenTelemetry Java SDK. |
| [opentelemetry js](https://github.com/open-telemetry/opentelemetry-js) | OpenTelemetry JavaScript Client. |
| [opentelemetry python](https://github.com/open-telemetry/opentelemetry-python) | OpenTelemetry Python API and SDK. |
| [opentelemetry rust](https://github.com/open-telemetry/opentelemetry-rust) | The Rust OpenTelemetry implementation. |
| [pprof](https://github.com/google/pprof) | pprof is a tool for visualization and analysis of profiling data. |
| [self hosted](https://github.com/getsentry/self-hosted) | Sentry, feature-complete and packaged up for low-volume deployments and proofs-of-concept. License not detected by GitHub; check the repository license before use. |
| [uptrace](https://github.com/uptrace/uptrace) | Open source APM: OpenTelemetry traces, metrics, and logs. AGPL-3.0: network use can trigger source-disclosure obligations. |

## Optimization scheduling and operational tooling

| Resource | Useful for / constraints |
|---|---|
| [autoscaler](https://github.com/kubernetes/autoscaler) | Autoscaling components for Kubernetes. |
| [cron](https://github.com/robfig/cron) | a cron library for go. |
| [descheduler](https://github.com/kubernetes-sigs/descheduler) | Descheduler for Kubernetes. |
| [gocron](https://github.com/jasonlvhit/gocron) | A Golang Job Scheduling Package. |
| [gronx](https://github.com/adhocore/gronx) | Lightweight, fast and dependency-free Cron expression parser (due checker, next/prev due date finder), task runner, job scheduler and/or daemon for Golang (tested on v1.13+) and standalone usage. |
| [healthchecks](https://github.com/healthchecks/healthchecks) | Open-source cron job and background task monitoring service, written in Python & Django. |

## Platform SDKs and Windows

| Resource | Useful for / constraints |
|---|---|
| [AutoHotkey](https://github.com/AutoHotkey/AutoHotkey) | AutoHotkey - macro-creation and automation-oriented scripting utility for Windows. GPL-2.0: derivative works must stay under the GPL. |
| [calculator](https://github.com/microsoft/calculator) | Windows Calculator: A simple yet powerful calculator that ships with Windows. |
| [DevHome](https://github.com/microsoft/devhome) | The new Dev Home experience for Windows! |
| [Files](https://github.com/files-community/Files) | A modern file manager that helps users organize their files and folders. |
| [fluentui system icons](https://github.com/microsoft/fluentui-system-icons) | Fluent System Icons are a collection of familiar, friendly and modern icons from Microsoft. |
| [MicaForEveryone](https://github.com/MicaForEveryone/MicaForEveryone) | Mica For Everyone is a tool to enable backdrop effects on the title bars of Win32 apps on Windows 11. |
| [nappgui src](https://github.com/frang75/nappgui_src) | SDK for building cross-platform desktop apps in ANSI-C. |
| [qwindowkit](https://github.com/stdware/qwindowkit) | Cross-platform frameless window framework for Qt. Support Windows, macOS, Linux. |
| [swift win32](https://github.com/compnerd/swift-win32) | A Windows application framework for Swift. |
| [windigo](https://github.com/rodrigocfd/windigo) | Windows API and GUI in idiomatic Go. |
| [Windows.UI.Composition Win32 Samples](https://github.com/microsoft/Windows.UI.Composition-Win32-Samples) | Windows.UI.Composition Win32 Samples. |
| [winsafe](https://github.com/rodrigocfd/winsafe) | Windows API and GUI in safe, idiomatic Rust. |
| [workspacer](https://github.com/workspacer/workspacer) | a tiling window manager for Windows. |

## Reverse engineering malware analysis and binary inspection

| Resource | Useful for / constraints |
|---|---|
| [Awesome Android Reverse Engineering](https://github.com/user1342/Awesome-Android-Reverse-Engineering) | A curated list of awesome Android Reverse Engineering training, resources, and tools. |
| [awesome executable packing](https://github.com/packing-box/awesome-executable-packing) | A curated list of awesome resources related to executable packing. |
| [awesome list](https://github.com/0xor0ne/awesome-list) | Cybersecurity oriented awesome list. |
| [BinAbsInspector](https://github.com/KeenSecurityLab/BinAbsInspector) | BinAbsInspector: Vulnerability Scanner for Binaries. GPL-3.0: derivative works must stay under the GPL. |
| [bindiff](https://github.com/google/bindiff) | Quickly find differences and similarities in disassembled code. |
| [decompiler explorer](https://github.com/decompiler-explorer/decompiler-explorer) | Decompiler Explorer! Compare tools on the forefront of static analysis, now in your web browser! |
| [flare learning hub](https://github.com/mandiant/flare-learning-hub) | Free educational content on reverse engineering and malware analysis from the FLARE team. |
| [GDA android reversing Tool](https://github.com/charles2gan/GDA-android-reversing-Tool) | the fastest and most powerful android decompiler(native tool working without Java VM) for the APK, DEX, ODEX, OAT, JAR, AAR, and CLASS file. |
| [HyperDbg](https://github.com/HyperDbg/HyperDbg) | State-of-the-art native debugging tools. GPL-3.0: derivative works must stay under the GPL. |
| [osslsigncode](https://github.com/mtrojnar/osslsigncode) | OpenSSL-based Authenticode signing for PE, CAB, CAT, MSI, APPX, and script file. License not detected by GitHub; check the repository license before use. |
| [panda](https://github.com/panda-re/panda) | Platform for Architecture-Neutral Dynamic Analysis. License not detected by GitHub; check the repository license before use. |
| [pe bear](https://github.com/hasherezade/pe-bear) | Portable Executable reversing tool with a friendly GUI. GPL-2.0: derivative works must stay under the GPL. |
| [pe sieve](https://github.com/hasherezade/pe-sieve) | Scans a given process. Recognizes and dumps a variety of potentially malicious implants (replaced/injected PEs, shellcodes, hooks, in-memory patches). |
| [pwntools](https://github.com/Gallopsled/pwntools) | CTF framework and exploit development library. License not detected by GitHub; check the repository license before use. |
| [pycdc](https://github.com/zrax/pycdc) | C++ python bytecode disassembler and decompiler. GPL-3.0: derivative works must stay under the GPL. |
| [python uncompyle6](https://github.com/rocky/python-uncompyle6) | A cross-version Python bytecode decompiler. GPL-3.0: derivative works must stay under the GPL. |
| [qiling](https://github.com/qilingframework/qiling) | A True Instrumentable Binary Emulation Framework. GPL-2.0: derivative works must stay under the GPL. |
| [redasm](https://github.com/redasm-dev/redasm) | The Open Source Disassembler. GPL-3.0: derivative works must stay under the GPL. |
| [simplify](https://github.com/CalebFenton/simplify) | Android virtual machine and deobfuscator. |
| [speakeasy](https://github.com/mandiant/speakeasy) | Windows kernel and user mode emulation. |
| [Triton](https://github.com/JonathanSalwan/Triton) | Triton is a dynamic binary analysis library. Build your own program analysis tools, automate your reverse engineering, perform software verification or just emulate code. |
| [vineflower](https://github.com/Vineflower/vineflower) | Modern Java decompiler aiming to be as accurate as possible, with an emphasis on output quality. Fork of the Fernflower decompiler. |

## Search messaging and durable work

| Resource | Useful for / constraints |
|---|---|
| [activemq](https://github.com/apache/activemq) | Apache ActiveMQ. |
| [Activiti](https://github.com/Activiti/Activiti) | Activiti is a light-weight workflow and Business Process Management (BPM) Platform targeted at business people, developers and system admins. Its core is a super-fast and rock-solid BPMN 2 process engine for Java. |
| [asynq](https://github.com/hibiken/asynq) | Simple, reliable, and efficient distributed task queue in Go. |
| [bull](https://github.com/OptimalBits/bull) | Premium Queue package for handling distributed jobs and messages in NodeJS. License not detected by GitHub; check the repository license before use. |
| [cadence](https://github.com/cadence-workflow/cadence) | Cadence is a distributed, scalable, durable, and highly available orchestration engine to execute asynchronous long-running business logic in a scalable and resilient way. |
| [camunda](https://github.com/camunda/camunda) | Agentic Orchestration Platform. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [conductor](https://github.com/Netflix/conductor) | Conductor is a microservices orchestration engine. |
| [conductor (conductor-oss)](https://github.com/conductor-oss/conductor) | Conductor is an event driven agentic workflow engine providing durable and highly resilient execution engine for applications and AI Agents. |
| [elasticsearch](https://github.com/elastic/elasticsearch) | Free and Open Source, Distributed, RESTful Search Engine. License not detected by GitHub; check the repository license before use. |
| [flowable engine](https://github.com/flowable/flowable-engine) | A compact and highly efficient workflow and Business Process Management (BPM) platform for developers, system admins and business users. |
| [kafka](https://github.com/apache/kafka) | Apache Kafka - A distributed event streaming platform. |
| [nats server](https://github.com/nats-io/nats-server) | High-Performance server for NATS.io, the cloud and edge native messaging system. |
| [nsq](https://github.com/nsqio/nsq) | A realtime distributed messaging platform. |
| [pulsar](https://github.com/apache/pulsar) | Apache Pulsar - distributed pub-sub messaging system. |
| [quickwit](https://github.com/quickwit-oss/quickwit) | Cloud-native OSS search engine for observability. |
| [rabbitmq server](https://github.com/rabbitmq/rabbitmq-server) | Open source RabbitMQ: core server and tier 1 (built-in) plugins. License not detected by GitHub; check the repository license before use. |
| [redpanda](https://github.com/redpanda-data/redpanda) | Redpanda is a streaming data platform for developers. Kafka API compatible. 10x faster. No ZooKeeper. No JVM! No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [resque](https://github.com/resque/resque) | Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later. |
| [restate](https://github.com/restatedev/restate) | Restate is the platform for building resilient applications that tolerate all infrastructure faults w/o the need for a PhD. License not detected by GitHub; check the repository license before use. |
| [river](https://github.com/riverqueue/river) | The polyglot queue: Fast and reliable background jobs in Go, Java, JS, Ruby, and Rust on Postgres/SQLite. MPL-2.0: file-level copyleft; modified files must be published. |
| [rq](https://github.com/rq/rq) | Simple job queues for Python. License not detected by GitHub; check the repository license before use. |
| [schema registry](https://github.com/confluentinc/schema-registry) | Confluent Schema Registry for Kafka. License not detected by GitHub; check the repository license before use. |
| [seatunnel](https://github.com/apache/seatunnel) | SeaTunnel is a multimodal, high-performance, distributed, massive data integration tool. |
| [sidekiq](https://github.com/sidekiq/sidekiq) | Simple, efficient background processing for Ruby. License not detected by GitHub; check the repository license before use. |
| [solr](https://github.com/apache/solr) | Apache Solr open-source search software. |
| [tantivy](https://github.com/quickwit-oss/tantivy) | Tantivy is a full-text search engine library inspired by Apache Lucene and written in Rust. |
| [typesense](https://github.com/typesense/typesense) | Open Source alternative to Algolia + Pinecone and an Easier-to-Use alternative to ElasticSearch Fast, typo tolerant, in-memory fuzzy Search Engine for building delightful search experiences. GPL-3.0: derivative works must stay under the GPL. |
| [vespa](https://github.com/vespa-engine/vespa) | The AI search platform. |
| [zeebe](https://github.com/camunda/camunda) | Agentic Orchestration Platform. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |

## Software architecture and API design patterns

| Resource | Useful for / constraints |
|---|---|
| [aip](https://github.com/aip-dev/google.aip.dev) | API Improvement Proposals. https://aip.dev/. License not detected by GitHub; check the repository license before use. |
| [awesome architecture](https://github.com/study8677/awesome-architecture) | Architecture-first system design: 26 bilingual tutorials, 25 architecture templates, and 6 end-to-end cases covering distributed systems, AI-native systems, RAG, coding Agents, and production trade-offs. |
| [awesome software architecture](https://github.com/mehdihadeli/awesome-software-architecture) | A curated list of awesome articles, videos, and other resources to learn and practice software architecture, patterns, and principles. |
| [clean code dotnet](https://github.com/thangchung/clean-code-dotnet) | bathtub: Clean Code concepts and tools adapted for .NET. |
| [COLA](https://github.com/alibaba/COLA) | COLA: Clean Object-oriented & Layered Architecture. LGPL-2.1: dynamic linking is permitted, static linking has obligations. |
| [domain driven hexagon](https://github.com/Sairyss/domain-driven-hexagon) | Learn Domain-Driven Design, software architecture, design patterns, best practices. Code examples included. |
| [eventuate tram core](https://github.com/eventuate-tram/eventuate-tram-core) | Transactional messaging for microservices. License not detected by GitHub; check the repository license before use. |
| [library](https://github.com/ddd-by-examples/library) | A comprehensive Domain-Driven Design example with problem space strategic analysis and various tactical patterns. |
| [modular monolith with ddd](https://github.com/kgrzybek/modular-monolith-with-ddd) | Full Modular Monolith application with Domain-Driven Design approach. |
| [smithy](https://github.com/smithy-lang/smithy) | Smithy is a protocol-agnostic interface definition language and set of tools for generating clients, servers, and documentation for any programming language. |
| [software architecture books](https://github.com/mhadidg/software-architecture-books) | A comprehensive list of books on Software Architecture. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [system design](https://github.com/karanpratapsingh/system-design) | Learn how to design systems at scale and prepare for system design interviews. License not detected by GitHub; check the repository license before use. |
| [system design primer](https://github.com/donnemartin/system-design-primer) | Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. License not detected by GitHub; check the repository license before use. |
| [Systemizer](https://github.com/honzaap/Systemizer) | A system design tool that allows you to simulate data flow of distributed systems. GPL-3.0: derivative works must stay under the GPL. |

## Test automation and quality engineering

| Resource | Useful for / constraints |
|---|---|
| [allure2](https://github.com/allure-framework/allure2) | Allure Report is a flexible, lightweight multi-language test reporting tool. It provides clear graphical reports and allows everyone involved in the development process to extract the maximum of information from the everyday testi… |
| [ava](https://github.com/avajs/ava) | Node.js test runner that lets you develop with confidence. |
| [doctest](https://github.com/doctest/doctest) | The fastest feature-rich C++11/14/17/20/23 single-header testing framework. |
| [hey](https://github.com/rakyll/hey) | HTTP load generator, ApacheBench (ab) replacement. |
| [jmeter](https://github.com/apache/jmeter) | Apache JMeter open-source load testing tool for analyzing and measuring the performance of a variety of services. |
| [junit5](https://github.com/junit-team/junit-framework) | The programmer-friendly testing framework for Java and the JVM. |
| [karate](https://github.com/karatelabs/karate) | Test Automation Made Simple. |
| [karma](https://github.com/karma-runner/karma) | Spectacular Test Runner for JavaScript. |
| [mockito](https://github.com/mockito/mockito) | Most popular Mocking framework for unit tests written in Java. |
| [newman](https://github.com/postmanlabs/newman) | Newman is a command-line collection runner for Postman. |
| [puppeteer](https://github.com/puppeteer/puppeteer) | JavaScript API for Chrome and Firefox. |
| [reportportal](https://github.com/reportportal/reportportal) | Main Repository. ReportPortal starts here - see readme below. |
| [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) | Python APIs for web automation, testing, and bypassing bot-detection. |
| [serenity js](https://github.com/serenity-js/serenity-js) | A TypeScript-native acceptance testing framework that gives your Playwright Test, WebdriverIO, or Cucumber test suite the architecture it needs to scale. |
| [testcontainers java](https://github.com/testcontainers/testcontainers-java) | Testcontainers is a Java library that supports JUnit tests, providing lightweight, throwaway instances of common databases, Selenium web browsers, or anything else that can run in a Docker container. |
| [testcontainers python](https://github.com/testcontainers/testcontainers-python) | Testcontainers is a Python library that providing a friendly API to run Docker container. It is designed to create runtime environment to use during your automatic tests. |
| [testng](https://github.com/testng-team/testng) | TestNG testing framework. |

## Testing verification and performance

| Resource | Useful for / constraints |
|---|---|
| [AFLplusplus](https://github.com/AFLplusplus/AFLplusplus) | AFL++ is a state-of-the-art fuzzer, and #1 in benchmarks. It was originally based on AFL. Today it comes with qemu 5.1, collision-free coverage, enhanced laf-intel & redqueen, AFLfast++ power schedules, MOpt mutators,. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [ApplicationInspector](https://github.com/microsoft/ApplicationInspector) | A source code analyzer built for surfacing features of interest and other characteristics to answer the question 'What's in the code?' quickly using static analysis with a json based rules engine. |
| [oss fuzz](https://github.com/google/oss-fuzz) | OSS-Fuzz - continuous fuzzing for open source software. |
| [sanitizers](https://github.com/google/sanitizers) | AddressSanitizer, ThreadSanitizer, MemorySanitizer. License not detected by GitHub; check the repository license before use. |

## Windows / Graphics

| Resource | Useful for / constraints |
|---|---|
| [AMF](https://github.com/GPUOpen-LibrariesAndSDKs/AMF) | The Advanced Media Framework (AMF) SDK provides developers with optimal access to AMD devices for multimedia processing. License not detected by GitHub; check the repository license before use. |
| [ComputeSharp](https://github.com/Sergio0694/ComputeSharp) | A .NET library to run C# code in parallel on the GPU through DX12, D2D1, and dynamically generated HLSL compute and pixel shaders, with the goal of making GPU computing easy to use for all .NET developers! |
| [cuda samples](https://github.com/NVIDIA/cuda-samples) | Samples for CUDA Developers which demonstrates features in CUDA Toolkit. License not detected by GitHub; check the repository license before use. |
| [D3D12MemoryAllocator](https://github.com/GPUOpen-LibrariesAndSDKs/D3D12MemoryAllocator) | Easy to integrate memory allocation library for Direct3D 12. |
| [D3D12TranslationLayer](https://github.com/microsoft/D3D12TranslationLayer) | A library containing utilities for mapping higher-level graphics work to D3D12. |
| [DirectX Graphics Samples](https://github.com/microsoft/DirectX-Graphics-Samples) | This repo contains the DirectX Graphics samples that demonstrate how to build graphics intensive applications on Windows. |
| [GDK](https://github.com/microsoft/GDK) | Microsoft Public GDK. License not detected by GitHub; check the repository license before use. |
| [hlsl specs](https://github.com/microsoft/hlsl-specs) | HLSL Specifications. |
| [TensorRT](https://github.com/NVIDIA/TensorRT) | NVIDIA® TensorRT™ is an SDK for high-performance deep learning inference on NVIDIA GPUs. This repository contains the open source components of TensorRT. |
| [VQEngine](https://github.com/vilbeyli/VQEngine) | Multi-threaded DirectX12 renderer w/ HDR, PBR & Multi-monitor support. GPL-3.0: derivative works must stay under the GPL. |
| [Vulkan Headers](https://github.com/KhronosGroup/Vulkan-Headers) | Vulkan header files and API registry. License not detected by GitHub; check the repository license before use. |
| [VulkanMemoryAllocator](https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator) | Easy to integrate Vulkan memory allocation library. |
| [Xbox GDK Samples](https://github.com/microsoft/Xbox-GDK-Samples) | Game development samples published by the Xbox Advanced Technology Group using the Microsoft GDK. |
