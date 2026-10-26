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

## 2026-10-26 expansion — 1000 AI resources (includes skills.sh directory)

| Resource | Useful for / constraints |
|---|---|
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | Pioneering autonomous agent that chains LLM thoughts to achieve goals — benchmark for agent evaluation. |
| [BabyAGI](https://github.com/yoheinakajima/babyagi) | Task-driven autonomous agent loop with vector memory — minimal reference implementation. |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | Open-source autonomous agent framework with toolkits and GUI. |
| [OpenDevin (OpenHands)](https://github.com/All-Hands-AI/OpenHands) | OpenHands (ex-OpenDevin) for autonomous software development — code execution via sandboxes. |
| [MetaGPT](https://github.com/geekan/MetaGPT) | Multi-agent framework that assigns roles (PM, architect, engineer) to build software. |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Chat-powered software development via multi-agent chat chain. |
| [CAMEL-AI](https://github.com/camel-ai/camel) | Communicative agents for mind exploration of LLM society and role-play. |
| [AutoGen Studio](https://microsoft.github.io/autogen/docs/autogen-studio/getting-started/) | Low-code UI for building and testing AutoGen multi-agent workflows. |
| [CrewAI Tools](https://docs.crewai.com/tools/overview) | Toolkit for CrewAI crews: search, code execution, and API integrations. |
| [LangGraph Cloud](https://langchain-ai.github.io/langgraph/cloud/) | Managed LangGraph deployment with durable execution and human-in-the-loop. |
| [Prefect](https://docs.prefect.io/latest/) | Workflow orchestration for agents: scheduling, retries, and observability. |
| [Airflow](https://airflow.apache.org/docs/) | Apache Airflow: battle-tested DAG orchestration for batch agent pipelines. |
| [Dagster](https://docs.dagster.io/) | Data and ML orchestration with strong typing and asset lineage for agent pipelines. |
| [Step Functions (AWS)](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) | AWS Step Functions for durable agent workflows with Bedrock integration. |
| [Azure Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview) | Durable Functions for stateful agent orchestrations on Azure. |
| [Google Workflows](https://cloud.google.com/workflows/docs) | Orchestrate GCP services and AI APIs into agent workflows. |
| [LangChain LCEL](https://python.langchain.com/docs/concepts/lcel) | LangChain Expression Language for composing chains, retries, and fallbacks. |
| [LlamaIndex Workflows](https://developers.llamaindex.ai/python/framework/workflows/) | Event-driven orchestration for LlamaIndex agents with human-in-the-loop. |
| [Semantic Kernel Planners](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planners) | Semantic Kernel planners for goal decomposition and function calling. |
| [LMQL](https://github.com/eth-sri/lmql) | Language model query language for constrained generation with logic constraints. |
| [Outlines](https://github.com/dottxt-ai/outlines) | Structured generation with JSON schema, regex, and CFG for LLMs (fast). |
| [Instructor (Structured Outputs)](https://github.com/jxnl/instructor) | Instructor for perfect structured outputs via function calling and schema validation. |
| [BAML](https://docs.boundaryml.com/home) | BAML: typed prompt language that compiles to LLM clients with structured outputs. |
| [EvoAgent](https://github.com/EvoAgentX/EvoAgentX) | Evolving agent workflows via optimization — auto-improve prompts and toolsets. |
| [ADaPT](https://github.com/archi-lab/adapt) | As-needed decomposition and planning for LLM agents. |
| [ReAct (LangChain)](https://python.langchain.com/docs/modules/agents/agent_types/react) | ReAct pattern: reason + act loops for tool-using agents. |
| [ReWOO](https://github.com/billxzy1215/ReWOO) | Modular reasoning with tool use decoupled from observation. |
| [Reflexion](https://github.com/noahshinn/reflexion) | Reflexion: verbal reinforcement for agents that learn from mistakes. |
| [Voyager (Minecraft)](https://github.com/MineDojo/Voyager) | Voyager: lifelong learning agent in Minecraft via curriculum and skill library. |
| [Generative Agents (Stanford)](https://github.com/joonspk-research/generative_agents) | Stanford smallville generative agents with memory and social simulation. |
| [Smallville (Park et al.)](https://arxiv.org/abs/2304.03442) | Paper: generative agents simulate human behavior — influencial for agent memory design. |
| [Toolformer Paper](https://arxiv.org/abs/2302.04761) | Paper: LLMs that teach themselves to use tools via self-supervision. |
| [Gorilla (Berkeley)](https://github.com/ShishirPatil/gorilla) | Berkeley's LLM for API calling with ToolBench evaluation. |
| [Functionary (MeetKai)](https://github.com/meetkai/functionary) | Open LLM fine-tuned for function calling — check Apache 2 license. |
| [Nexus Raven](https://github.com/nexusflowai/nexus-hub) | Nexus Raven: function calling model optimized for tool use. |
| [Hermes Function Calling](https://github.com/NousResearch/Hermes-Function-Calling) | Nous Hermes fine-tunes for function calling and system-prompt steering. |
| [OpenFunctions](https://github.com/OpenFunctions) | Open-source function-calling datasets and models. |
| [ToolLLaMA](https://github.com/open-compass/ToolLLaMA) | ToolLLaMA via ToolBench: large tool-use benchmark and models. |
| [AgentBench](https://github.com/THUDM/AgentBench) | Benchmark for LLM-as-agent across 8 environments (OS, DB, etc.). |
| [WebArena](https://github.com/web-arena-x/webarena) | WebArena: realistic web environment for autonomous agent evaluation. |
| [GAIA](https://huggingface.co/gaia-benchmark) | GAIA: General AI Assistants benchmark with real-world multi-step tasks. |
| [HumanEval](https://github.com/openai/human-eval) | OpenAI HumanEval for code generation correctness — still-cited coding benchmark. |
| [MBPP](https://github.com/google-research/google-research/tree/master/mbpp) | Mostly Basic Python Problems benchmark for code LLMs. |
| [BFCL (Berkeley Function Calling)](https://gorilla.cs.berkeley.edu/leaderboard.html) | Berkeley Function Calling Leaderboard: rigorous tool-use evaluation. |
| [ToolBench](https://github.com/open-compass/ToolBench) | Large-scale tool-use benchmark with 16k real APIs. |
| [T-Eval](https://github.com/open-compass/T-Eval) | Step-by-step tool-use evaluation for LLMs. |
| [AgentTuning](https://github.com/THUDM/AgentTuning) | AgentTuning: fine-tuning LLMs for agentic behavior with trajectory data. |
| [FireAct](https://github.com/THUDM/FireAct) | Fine-tuning agents with ReAct trajectories from GPT-4. |
| [TRICE](https://github.com/THUDM/TRICE) | Training agentic capabilities via intermediate chaining. |
| [Swarm (OpenAI)](https://github.com/openai/swarm) | OpenAI's lightweight multi-agent orchestration experiment: handoffs between agents. |
| [Magentic-One (Microsoft)](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one) | Microsoft's generalist multi-agent for web and file tasks (Orchestrator pattern). |
| [TaskWeaver (Microsoft)](https://github.com/microsoft/TaskWeaver) | TaskWeaver: code-first agent for data analytics with planner and code executor. |
| [JARVIS (Microsoft)](https://github.com/microsoft/JARVIS) | JARVIS (HuggingGPT) connects LLMs to Hugging Face models as tools. |
| [MM-REACT](https://github.com/microsoft/MM-REACT) | Microsoft's multimodal ReAct: reasoning with tools over vision/language. |
| [Visual ChatGPT](https://github.com/microsoft/visual-chatgpt) | Visual ChatGPT: ChatGPT with visual foundation models as tools. |
| [LLaVA](https://github.com/haotian-liu/LLaVA) | Large Language and Vision Assistant: open multimodal chat. |
| [Qwen-VL](https://github.com/QwenLM/Qwen-VL) | Alibaba's vision-language family for multimodal agents. |
| [CogVLM](https://github.com/THUDM/CogVLM) | THUDM's open visual language models with strong grounding. |
| [Kosmos-2](https://github.com/microsoft/unilm/tree/master/kosmos-2) | Microsoft Kosmos-2 for grounded multimodal language. |
| [Paligemma](https://github.com/google-research/big_vision/tree/main/big_vision/configs/proj/paligemma) | Google PaliGemma vision-language model family. |
| [Fuyu-8B](https://www.adept.ai/blog/fuyu-8b) | Adept Fuyu: high-res multimodal model for agent UIs. |
| [Claude Artifacts](https://docs.anthropic.com/en/docs/build-with-claude/artifacts) | Artifacts: Claude's interactive canvas for code and design — useful agent UX pattern. |
| [OpenAI Canvas](https://openai.com/index/introducing-canvas/) | ChatGPT Canvas: collaborative writing/coding surface — pattern for agent UX. |
| [Gemini Canvas](https://blog.google/products/gemini/gemini-canvas/) | Gemini Canvas for interactive creation and iteration. |
| [Perplexity Spaces](https://www.perplexity.ai/help-center/en/articles/10352995-what-is-a-space) | Perplexity Spaces: collaborative, source-grounded agent workspaces. |
| [Notion AI](https://www.notion.com/help/guides/category/notion-ai) | Notion AI skills: Q&A, writing, and automation over workspace. |
| [MemGPT (Letta)](https://github.com/cpacker/MemGPT) | Original MemGPT paper implementation — long-term memory for agents. |
| [Arize Phoenix](https://phoenix.arize.com/) | Open-source LLM observability: traces, evals, and experiments. |
| [HumanLoop](https://humanloop.com/docs) | Prompt management and LLM evaluation platform with human feedback. |
| [Comet Opik](https://www.comet.com/site/products/opik/) | Comet Opik: open-source LLM evaluation and observability. |
| [Weave (Weights & Biases)](https://weave-docs.wandb.ai/) | Weave: trace, evaluate, and improve LLM apps from W&B. |
| [LangWatch](https://docs.langwatch.ai/) | LLM monitoring: guardrails, analytics, and prompt optimization. |
| [Portkey Guardrails](https://portkey.ai/docs/product/guardrails) | Guardrails for LLM: PII, toxicity, and hallucination detection. |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | NVIDIA's programmable guardrails for conversational AI. |
| [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761#fallback-17) | Toolformer: self-supervised tool use via API calls — foundational for agent framework design. |
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629#fallback-18) | ReAct paper: interleaving reasoning and tool use that powers most agent frameworks. |
| [Chain-of-Thought Prompting Elicits Reasoning](https://arxiv.org/abs/2201.11903#fallback-19) | Chain-of-Thought: step-by-step reasoning that improves agent planning and decomposition. |
| [Tree of Thoughts: Deliberate Problem Solving](https://arxiv.org/abs/2305.10601#fallback-20) | Tree-of-Thoughts: search over thought trees for better planning than linear CoT. |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | Voyager: lifelong Minecraft agent with skill library — curriculum for evolving agents. |
| [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442#fallback-22) | Stanford Generative Agents: memory and social simulation patterns for agent design. |
| [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) | AutoGen paper: conversational multi-agent orchestration from Microsoft. |
| [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334) | Gorilla paper: function calling with ToolBench — evaluation driven framework selection. |
