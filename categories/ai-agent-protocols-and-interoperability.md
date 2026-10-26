# AI agent protocols and interoperability

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Added 2026-10-23 in AI expansion round 2. Primary-source pointers; every entry link-checked at entry (all reachable). Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/latest/) | Linux Foundation protocol for agent-to-agent discovery, task delegation, and interoperability — the complement to MCP's tool access. Check version compatibility between implementations. |
| [A2A protocol (GitHub)](https://github.com/a2aproject/A2A) | Specification source, samples, and SDK links for Agent2Agent. |
| [AG-UI Protocol](https://docs.ag-ui.com/) | Event-based protocol connecting agent backends to user interfaces (streaming state, tool calls, human input). |
| [CopilotKit](https://docs.copilotkit.ai/) | React framework for agent-native UIs; creators/stewards of AG-UI. Use when the frontend must render agent state, not just chat text. |

## 2026-10-26 expansion — 1000 AI resources (includes skills.sh directory)

| Resource | Useful for / constraints |
|---|---|
| [Model Context Protocol Spec](https://modelcontextprotocol.io/specification/2025-03-26) | MCP 2025-03-26 spec: tools, resources, prompts, and transports. |
| [Agent-to-Agent (A2A) Google](https://google.github.io/A2A/) | Google's A2A protocol for agent interoperability: discovery and task delegation. |
| [Agent Communication Protocol (ACP) IBM Bee](https://github.com/i-am-bee/acp) | IBM Bee's ACP: REST-based protocol for agent communication. |
| [ANP — Agent Network Protocol](https://github.com/agent-network-protocol/anp) | ANP decentralized agent networking protocol. |
| [FIPA ACL](https://www.fipa.org/specs/fipa00061/) | FIPA ACL spec for agent communication — historical reference for A2A/ACP. |
| [OpenAPI for Agents](https://spec.openapis.org/oas/v3.1.0.html) | OpenAPI 3.1 for describing agent tool APIs — MCP tools often wrap OAS. |
| [JSON-RPC 2.0](https://www.jsonrpc.org/specification) | JSON-RPC 2.0 underlying MCP and many agent transports. |
| [CloudEvents](https://cloudevents.io/) | CloudEvents spec for agent event envelopes across systems. |
| [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model/) | VCs for agent identity and delegated authority. |
| [OAuth 2.1 for Agents](https://oauth.net/2.1/) | OAuth 2.1 for agent authentication to tools and MCP servers. |
| [SPIFFE/SPIRE](https://spiffe.io/docs/latest/spiffe-about/overview/) | SPIFFE for workload identity among agent services. |
| [OpenID Connect](https://openid.net/developers/how-connect-works/) | OIDC for agent user authentication flows. |
| [DID Spec (W3C)](https://www.w3.org/TR/did-core/) | Decentralized identifiers for agent identity. |
| [Agent Cards (A2A)](https://google.github.io/A2A/specification/#5-agent-card) | A2A Agent Card for capability discovery. |
| [MCP Authorization Spec](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) | MCP authorization for OAuth-protected servers. |
| [MCP Sampling Spec](https://modelcontextprotocol.io/specification/2025-03-26/server/sampling) | MCP sampling: servers request LLM completions via client. |
| [Tool Calling (OpenAI)](https://platform.openai.com/docs/guides/function-calling) | OpenAI tool calling spec for agent interoperability. |
| [Anthropic Tool Use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview) | Anthropic tool use spec for Claude agents. |
| [Google Function Calling](https://ai.google.dev/gemini-api/docs/function-calling) | Gemini function calling spec with parallel calls. |
| [Llama Stack](https://llama-stack.readthedocs.io/en/latest/) | Meta Llama Stack for standardized inference, safety, and agent APIs. |
| [Vercel AI SDK Tool Calling](https://sdk.vercel.ai/docs/ai-sdk-core/tools-and-tool-calling) | Vercel AI SDK tool calling patterns for TS agents. |
| [LangChain Tool Calling](https://python.langchain.com/docs/how_to/tool_calling/) | LangChain unified tool calling across providers. |
| [Semantic Kernel Plugins](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins) | SK plugins: OpenAPI and native functions as agent tools. |
| [AutoGen Tool Use](https://microsoft.github.io/autogen/docs/reference/agentchat/conversational_agent/) | AutoGen conversational agent tool-use docs. |
| [CrewAI Tools Spec](https://docs.crewai.com/tools/creating-tools) | CrewAI tool creation spec for custom agent tools. |
| [Pydantic AI Tools](https://ai.pydantic.dev/tools/) | Pydantic AI tool definition with validation. |
| [OpenAI Assistants API (legacy)](https://platform.openai.com/docs/assistants/overview) | Assistants API (legacy) tool and thread model — compare to new Responses API. |
| [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses) | OpenAI Responses API: stateful tool calling successor to Assistants. |
| [Anthropic Workspaces (beta)](https://docs.anthropic.com/en/docs/build-with-claude/workspaces) | Workspaces for multi-agent file collaboration (beta). |
| [Smolagents Tool Spec](https://huggingface.co/docs/smolagents/en/reference/tools) | Smolagents tool spec: Python functions as tools. |
| [Mastra Tools](https://mastra.ai/en/docs/tools/overview) | Mastra tool definitions for TS agents. |
| [BeeAI Framework Tools](https://framework.beeai.dev/tools) | BeeAI tool interface for IBM's agent framework. |
| [Strands Tools](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/tools/) | Strands tool spec for Bedrock agents. |
| [Google ADK Tools](https://google.github.io/adk-docs/tools/) | Google ADK tool definitions for Python/Go agents. |
| [Haystack Tools](https://docs.haystack.deepset.ai/docs/tools) | Haystack tool integration for agents. |
| [LlamaIndex Tools](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/) | LlamaIndex tool spec for query engines as tools. |
| [E2B Tool (Code Execution)](https://e2b.dev/docs/code-interpreting/overview) | E2B code execution tool: sandboxed Python for agents. |
| [Browserbase Tool](https://docs.browserbase.com/integrations/mcp) | Browserbase tool for browser control via MCP. |
