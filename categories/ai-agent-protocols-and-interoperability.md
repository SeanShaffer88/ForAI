# AI agent protocols and interoperability

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Added 2026-10-23 in AI expansion round 2. Primary-source pointers; every entry link-checked at entry (all reachable). Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/latest/) | Linux Foundation protocol for agent-to-agent discovery, task delegation, and interoperability — the complement to MCP's tool access. Check version compatibility between implementations. |
| [A2A protocol (GitHub)](https://github.com/a2aproject/A2A) | Specification source, samples, and SDK links for Agent2Agent. |
| [AG-UI Protocol](https://docs.ag-ui.com/) | Event-based protocol connecting agent backends to user interfaces (streaming state, tool calls, human input). |
| [CopilotKit](https://docs.copilotkit.ai/) | React framework for agent-native UIs; creators/stewards of AG-UI. Use when the frontend must render agent state, not just chat text. |

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [bifrost](https://github.com/maximhq/bifrost) | Open-source, high-performance AI gateway that works as your LLM gateway, MCP gateway and agent gateway. One OpenAI-compatible API for 10,000+ models, with failover, load balancing, semantic caching, virtual keys,. |
| [unity mcp](https://github.com/CoplayDev/unity-mcp) | Unity MCP acts as a bridge between AI assistants and your Unity Editor. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity. |
| [x64dbg mcp server](https://github.com/duty1g/x64dbg-mcp-server) | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. |
<!-- expansion-2026-11-11:end -->
