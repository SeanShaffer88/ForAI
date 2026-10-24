# AI agent frameworks and orchestration

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Added 2026-10-23 in the AI expansion. Primary-source pointers compiled from official documentation and project repositories; not individually re-fetched in this pass. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [LangChain documentation](https://docs.langchain.com/) | LangChain + LangGraph docs: agents, tools, retrieval, streaming. |
| [LangChain (GitHub)](https://github.com/langchain-ai/langchain) | Core LangChain monorepo. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Stateful, durable agent orchestration as graphs; persistence and human-in-the-loop. |
| [LlamaIndex documentation](https://developers.llamaindex.ai/) | Data framework for RAG and agents: ingestion, indexes, query engines, workflows. |
| [LlamaIndex (GitHub)](https://github.com/run-llama/llama_index) | LlamaIndex core and integrations. |
| [Microsoft Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) | .NET/Python/Java AI orchestration SDK from Microsoft. |
| [Microsoft AutoGen](https://github.com/microsoft/autogen) | Multi-agent conversation framework from Microsoft Research. |
| [CrewAI](https://docs.crewai.com/) | Role-based multi-agent crews and flows (Python). |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | OpenAI's lightweight agents SDK: agents, handoffs, guardrails, tracing. |
| [Claude Agent SDK (Anthropic docs)](https://code.claude.com/docs/en/agent-sdk/overview) | Anthropic's agent SDK for building agents on Muse. |
| [Google Agent Development Kit (ADK)](https://adk.dev/) | Google's open-source agent framework (Python/Java/Go). |
| [Haystack](https://docs.haystack.deepset.ai/docs/intro) | deepset's framework for production NLP/RAG pipelines and agents. |
| [DSPy](https://dspy.ai/) | Programmatic (compiled) LLM pipelines from Stanford NLP — declare, don't prompt-engineer by hand. |
| [Pydantic AI](https://pydantic.dev/docs/ai/overview/) | Type-safe Python agent framework from the Pydantic team. |
| [smolagents (Hugging Face)](https://huggingface.co/docs/smolagents) | Minimal agents library where agents write Python code as actions. |
| [Mastra](https://mastra.ai/docs) | TypeScript agent framework: agents, workflows, RAG, evals. |
| [Vercel AI SDK](https://ai-sdk.dev/docs) | TypeScript SDK for AI apps: streaming UI, tool calling, provider-agnostic models. |
| [Instructor](https://python.useinstructor.com/) | Structured outputs from LLMs via Pydantic validation and retries. |
| [Awesome LangChain](https://github.com/kyrolabs/awesome-langchain) | LangChain ecosystem projects and resources. |

## AI expansion round 2 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [Browser Use](https://docs.browser-use.com/) | Library that lets an LLM control a real browser to complete tasks; Python. Powerful and fragile in the usual browser-automation ways. |
| [Stagehand (Browserbase)](https://docs.stagehand.dev/) | AI browser-automation SDK (act/extract/observe primitives) on Playwright; pairs with Browserbase's hosted browsers. |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | Automates browser workflows with LLMs and computer vision, including form filling and 2FA handling; AGPL — check license fit. |

## AI expansion round 3 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [Dify](https://docs.dify.ai/) | Open-source LLM app platform: visual workflows, RAG, agent tools, and an API layer for shipping AI apps. |
| [Langflow](https://docs.langflow.org/) | Visual builder for LangChain-based agents and flows; exportable to code/API. |
| [Agno](https://docs.agno.com/) | Lightweight Python framework for multi-modal agents with memory, knowledge, and tools (the Phidata lineage). |
| [Strands Agents (AWS)](https://strandsagents.com/) | AWS's open-source, model-driven agent SDK (Python/TypeScript); Bedrock-first but provider-agnostic. |
| [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) | Microsoft's successor line uniting Semantic Kernel and AutoGen patterns for .NET/Python agents and workflows. |
| [BeeAI Framework](https://framework.beeai.dev/) | IBM-backed open framework for building agents in Python/TypeScript, with A2A/ACP interoperability work. |
| [n8n](https://docs.n8n.io/) | Workflow automation platform with first-class AI/agent nodes; self-hostable. Good for glue automations around models. |
| [Firebase Genkit](https://genkit.dev/) | Google's open-source framework for AI-powered apps (Go/JS/Python) with flows, tooling, and a dev UI. |
| [E2B](https://docs.e2b.dev/) | Secure cloud sandboxes for AI agents to run code — the standard isolated-execution layer for code agents. |
| [Daytona](https://www.daytona.io/docs/) | Sandboxes and dev environments for AI-generated code and agent workloads, with fast cold starts. |
| [Browserbase](https://docs.browserbase.com/) | Hosted headless browsers for agents: sessions, debugging, and stealth infrastructure under Stagehand and friends. |
| [Restack](https://docs.restack.io/) | Open-source framework for durable, long-running AI agents and workflows with deterministic replay. |
