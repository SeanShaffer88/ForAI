# AI resources expansion — 2026-10-23

Expansion of the general catalog with AI-specific resources requested by Sean: toolchains, useful repositories, MCP servers and SDKs, agent frameworks, local inference, model providers, retrieval, evaluation, prompt/context engineering, coding agents, and learning references.

## Evidence and limits

Entries are primary-source pointers (official documentation, official registries, or the project's own repository) compiled 2026-10-23. Inclusion is discovery, not an adoption audit: maintenance, licensing, compatibility, pricing, and security were not individually re-verified in this pass, and every entry received an automated link check on 2026-10-23 whose result is recorded in `http_status` (403/302 mean the site limited the automated checker, not that the link is dead). Twenty URLs that had genuinely moved (repository renames, documentation domain moves) were updated to their current canonical locations. Verify at the primary source before relying on any entry — framework APIs, model names, and prices in this area change frequently.

**156 entries added** across 12 categories (8 new). 23 vault entries were not added because the catalog already covers the resource (exact or equivalent URL).

## AI MCP servers and tool use

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

## AI agent frameworks and orchestration

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

## AI coding agents and assistants

| Resource | Useful for / constraints |
|---|---|
| [Aider](https://aider.chat/docs/) | Terminal pair-programming with git integration and repo maps. |
| [Cline](https://github.com/cline/cline) | Autonomous coding agent for VS Code with MCP support. |
| [Continue](https://docs.continue.dev/) | Open-source AI code assistant for IDEs; bring-your-own-model, MCP support. |
| [OpenHands](https://github.com/OpenHands/OpenHands) | Open platform for autonomous software-development agents. |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent) | Princeton's agent that fixes GitHub issues; SWE-bench reference implementation. |
| [SWE-bench](https://www.swebench.com/) | The standard benchmark for issue-fixing agents; check which split (Lite/Verified) a claim uses. |
| [Muse documentation](https://docs.github.com/en/copilot) | Copilot features, agent mode, code review, and administration. |
| [Muse documentation](https://code.claude.com/docs/en/overview) | Anthropic's terminal coding agent: hooks, subagents, MCP, settings. |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Google's open-source terminal agent for Gemini, MCP-compatible. |
| [OpenCode](https://opencode.ai/docs) | Open-source terminal coding agent, provider-agnostic. |
| [Roo Code](https://github.com/RooCodeInc/Roo-Code) | VS Code agent (Cline fork) with modes and MCP marketplace. |

## AI evaluation observability and guardrails

| Resource | Useful for / constraints |
|---|---|
| [OpenAI Evals](https://github.com/openai/evals) | OpenAI's eval framework and registry of benchmarks. |
| [promptfoo](https://www.promptfoo.dev/docs/intro/) | CLI-first LLM evals and red-teaming; test prompts/RAG/agents in CI. |
| [LangSmith documentation](https://docs.langchain.com/langsmith) | LangChain's tracing, datasets, and evaluation platform (works with other frameworks too). |
| [Langfuse documentation](https://langfuse.com/docs) | Open-source LLM observability: traces, evals, prompt management. |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | Open-source AI observability and evaluation notebooks/platform. |
| [Weights & Biases documentation](https://docs.wandb.ai/) | Experiment tracking, W&B Weave for LLM tracing/evals. |
| [Ragas documentation](https://docs.ragas.io/) | RAG evaluation metrics: faithfulness, answer relevancy, context precision/recall. |
| [DeepEval](https://deepeval.com/docs/getting-started) | Unit-test-style LLM evaluation framework (Confident AI). |
| [Inspect AI (UK AISI)](https://inspect.aisi.org.uk/) | UK AI Security Institute's framework for rigorous model evaluations. |
| [Hugging Face Evaluate](https://huggingface.co/docs/evaluate) | Standard ML/NLP metrics library and leaderboard tooling. |
| [NVIDIA NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | Programmable guardrails (Colang) for LLM apps. |
| [Guardrails AI](https://www.guardrailsai.com/docs) | Output validation/retry framework with a validator hub. |
| [OWASP Top 10 for LLM Applications](https://owasp.org/projects/top-10-for-large-language-model-applications) | The security risk list for LLM apps: prompt injection, insecure output handling, training-data poisoning, etc. Read before shipping. |

## AI learning and references

| Resource | Useful for / constraints |
|---|---|
| [Karpathy](https://github.com/karpathy/nanoGPT) | nanoGPT: the simplest readable GPT training implementation; pair with the YouTube series of the same name. |
| [Karpathy](https://github.com/karpathy/llm.c) | GPT training in plain C/CUDA — what frameworks abstract away, made visible. |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) | Free course: Transformers, fine-tuning, datasets, sharing models. |
| [Microsoft](https://github.com/microsoft/AI-For-Beginners) | 12-week curriculum: neural networks, CV, NLP, ethics. |
| [Microsoft](https://github.com/microsoft/generative-ai-for-beginners) | 21-lesson course on building GenAI apps (Python/TypeScript/.NET tracks). |
| [Microsoft](https://github.com/microsoft/ML-For-Beginners) | Classical ML curriculum with projects. |
| [LLM Course (mlabonne)](https://github.com/mlabonne/llm-course) | Roadmap with notebooks: LLM fundamentals, scientist, and engineer tracks. |
| [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Jay Alammar's visual walkthrough of the Transformer architecture. |
| [Fast.ai](https://course.fast.ai/) | Top-down deep learning course (free). |
| [DeepLearning.AI short courses](https://www.deeplearning.ai/courses) | Short practitioner courses on RAG, agents, fine-tuning, and evals. |
| [Awesome LLM](https://github.com/Hannibal046/Awesome-LLM) | Papers, training frameworks, tools, and courses around LLMs. |
| [Awesome Generative AI](https://github.com/steven2358/awesome-generative-ai) | Broad GenAI tools and services index. |
| [Awesome Production LLM](https://github.com/jihoo-kim/awesome-production-llm) | Production LLM stack components and case studies. |
| [Applied ML (eugeneyan)](https://github.com/eugeneyan/applied-ml) | Papers and blog posts on production ML systems from real companies. |
| [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) | Agent frameworks and applications index. |

## AI machine learning and local inference

| Resource | Useful for / constraints |
|---|---|
| [Ollama](https://ollama.com/) | One-command local model runner (macOS/Windows/Linux) with an OpenAI-compatible API. |
| [Ollama (GitHub)](https://github.com/ollama/ollama) | Source, model library format, API reference. |
| [SGLang](https://github.com/sgl-project/sglang) | Fast serving framework with structured generation (RadixAttention). |
| [LM Studio](https://lmstudio.ai/) | Desktop app to discover, download, and serve local models with a GUI. |
| [MLX (Apple)](https://github.com/ml-explore/mlx) | Apple's array framework for ML on Apple silicon; mlx-lm runs LLMs locally on Macs. |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Port of OpenAI Whisper speech recognition in C/C++ for local transcription. |
| [GPT4All](https://www.nomic.ai/gpt4all) | Nomic's local chatbot app and ecosystem. |
| [Jan](https://jan.ai/) | Open-source offline ChatGPT alternative desktop app. |
| [NVIDIA TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | Optimized LLM inference on NVIDIA GPUs for production serving. |
| [Hugging Face Text Generation Inference](https://huggingface.co/docs/text-generation-inference) | Production inference server for open models (TGI). |
| [TensorFlow documentation](https://www.tensorflow.org/api_docs) | Keras-based training and deployment APIs. |
| [JAX documentation](https://docs.jax.dev/) | Composable transformations (grad/jit/vmap) for ML research. |
| [scikit-learn documentation](https://scikit-learn.org/stable/) | Classical ML: preprocessing, models, model evaluation — still the right tool for many tabular problems. |
| [Hugging Face PEFT](https://huggingface.co/docs/peft) | Parameter-efficient fine-tuning: LoRA and friends. |
| [Hugging Face TRL](https://huggingface.co/docs/trl) | SFT/DPO/RLHF training for Transformers models. |
| [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) | YAML-configured LLM fine-tuning (LoRA/full) across providers. |
| [LLaMA-Factory](https://github.com/hiyouga/LlamaFactory) | Fine-tuning toolkit with web UI for 100+ models. |
| [Unsloth](https://github.com/unslothai/unsloth) | Fast, memory-efficient LoRA/QLoRA fine-tuning notebooks and library. |
| [ONNX documentation](https://onnx.ai/onnx/) | Open model interchange format and ONNX Runtime for cross-platform inference. |
| [NumPy documentation](https://numpy.org/doc/stable/) | Array computing foundation of the Python ML stack. |

## AI models and API providers

| Resource | Useful for / constraints |
|---|---|
| [Hugging Face Hub](https://huggingface.co/models) | The model/dataset hub: model cards carry license, files, and usage snippets. Read the card before recommending a model. |
| [Hugging Face documentation](https://huggingface.co/docs) | Transformers, Datasets, Diffusers, PEFT, TRL, and Hub APIs. |
| [OpenAI platform documentation](https://developers.openai.com/api/docs) | API reference, models, reasoning, tools, and pricing links. |
| [Meta Llama](https://dev.meta.ai/) | Llama models, downloads, and responsible-use docs. |
| [Mistral AI documentation](https://docs.mistral.ai/) | Mistral models and API (chat, embeddings, OCR). |
| [Cohere documentation](https://docs.cohere.com/) | Command, Embed, and Rerank APIs — strong for enterprise RAG. |
| [Groq documentation](https://console.groq.com/docs) | Very fast inference API (LPU) for open models. |
| [Together AI](https://docs.together.ai/) | Hosted open-model inference, fine-tuning, and dedicated endpoints. |
| [Fireworks AI](https://docs.fireworks.ai/) | Fast hosted inference for open models and fine-tunes. |
| [Replicate](https://replicate.com/docs) | Run community and official models (LLMs, image, audio) via one API. |
| [OpenRouter](https://openrouter.ai/docs) | One API key routed to many providers/models; useful for comparison. |
| [arXiv](https://arxiv.org/) | Preprint server — where most model papers land first. A paper is a claim, not a benchmark result. |
| [Papers With Code](https://huggingface.co/papers/trending) | Papers linked to code and benchmark leaderboards (SOTA tables). |

## AI prompt and context engineering

| Resource | Useful for / constraints |
|---|---|
| [Anthropic prompt engineering guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | Claude prompting: clarity, examples, XML structure, extended thinking. |
| [OpenAI prompt engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering) | Strategy and tactics for GPT-class models, plus reasoning-model guidance. |
| [Google Gemini prompting strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) | Gemini-specific prompting and media prompting. |
| [DAIR Prompt Engineering Guide](https://www.promptingguide.ai/) | Comprehensive community guide: techniques, papers, RAG/agent prompting. |
| [Learn Prompting](https://learnprompting.org/docs/introduction) | Free course-style prompting documentation, including security topics. |
| [Awesome ChatGPT Prompts](https://github.com/f/prompts.chat) | Large prompt-pattern collection; useful as examples, not as verified best practice. |
| [Anthropic](https://www.anthropic.com/research/building-effective-agents) | Anthropic's patterns: workflows vs agents, prompt chaining, routing, orchestrator-workers, evaluator-optimizer. |
| [Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) | Context windows as a finite resource: compaction, note-taking, sub-agents. |
| [OpenAI](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) | OpenAI's practitioner guide: when to use agents, guardrails, orchestration patterns. |

## AI retrieval and vector search

| Resource | Useful for / constraints |
|---|---|
| [Pinecone documentation](https://docs.pinecone.io/) | Managed vector database; indexes, namespaces, metadata filtering. |
| [Weaviate documentation](https://docs.weaviate.io/) | Open-source vector database with hybrid search and built-in vectorizers. |
| [Milvus documentation](https://milvus.io/docs) | Large-scale open-source vector database from Zilliz. |
| [Chroma documentation](https://docs.trychroma.com/) | Lightweight embedding database popular for local RAG prototypes. |
| [FAISS](https://github.com/facebookresearch/faiss) | Meta's library for efficient similarity search and clustering of dense vectors. |
| [LanceDB](https://lancedb.github.io/lancedb/) | Embedded vector database on the Lance columnar format. |
| [sqlite-vec](https://github.com/asg017/sqlite-vec) | Vector search extension for SQLite — good for local/offline apps. |
| [Elasticsearch documentation](https://www.elastic.co/docs/reference/elasticsearch) | Full-text + vector (kNN) search; BM25 still matters for hybrid retrieval. |
| [OpenAI embeddings guide](https://developers.openai.com/api/docs/guides/embeddings) | How embeddings work and which model dimensions to expect. |
| [Sentence Transformers documentation](https://www.sbert.net/) | Open embedding models, training, and semantic search recipes. |
| [Unstructured](https://docs.unstructured.io/) | Parsing PDFs/Office/HTML into clean elements for ingestion pipelines. |
| [MarkItDown (Microsoft)](https://github.com/microsoft/markitdown) | Convert Office/PDF/etc. to Markdown for LLM ingestion. |
| [Docling (IBM)](https://github.com/docling-project/docling) | Document parsing to Markdown/JSON with layout and OCR support. |

## CI version control and releases

| Resource | Useful for / constraints |
|---|---|
| [GitHub Docs](https://docs.github.com/) | Actions, REST/GraphQL APIs, Copilot, code security. |

## Cloud infrastructure and deployment

| Resource | Useful for / constraints |
|---|---|
| [Kubernetes documentation](https://kubernetes.io/docs/home/) | Concepts, kubectl reference, API reference. |

## Languages and runtimes

| Resource | Useful for / constraints |
|---|---|
| [Rust](https://www.rust-lang.org/) | Language home; install via rustup, edition and release info. |
| [The Rust Book](https://doc.rust-lang.org/book/) | Canonical language tutorial; ownership, traits, error handling. |
| [crates.io](https://crates.io/) | Rust package registry; check downloads, docs link, and maintenance before recommending a crate. |
| [docs.rs](https://docs.rs/) | Rendered docs for nearly every crate and version. |
| [Cargo Book](https://doc.rust-lang.org/cargo/) | Workspaces, features, profiles, publishing. |
| [Python](https://www.python.org/) | Downloads, PEP index, release schedule. |
| [PyPI](https://pypi.org/) | Python package index; check version, requires-python, and project links. |
| [Node.js](https://nodejs.org/en/docs) | Runtime APIs, LTS schedule, globals. |
| [npm](https://www.npmjs.com/) | JavaScript package registry; verify package identity carefully — similar names are a supply-chain risk. |
| [Deno](https://docs.deno.com/) | Secure JS/TS runtime, standard library, JSR registry. |
| [Bun](https://bun.sh/docs) | JS runtime, bundler, test runner, package manager. |
| [NuGet Gallery](https://www.nuget.org/) | .NET package registry; check target frameworks and license per package. |
| [pkg.go.dev](https://pkg.go.dev/) | Discover and read docs for Go packages and the standard library. |
| [C++ reference (cppreference)](https://en.cppreference.com/) | De-facto C/C++ standard library and language reference. |
| [vcpkg](https://vcpkg.io/) | Microsoft C/C++ package manager; port list is searchable online. |
| [Conan](https://conan.io/center) | C/C++ package manager and Conan Center index. |
| [Java](https://dev.java/) | JDK tutorials, API docs, release information. |
| [Maven Central](https://central.sonatype.com/) | JVM artifact registry; verify group/artifact coordinates. |

## Round 2 additions — 2026-10-23

45 further entries, suggested from a gap analysis against the full catalog and approved by Sean. Every URL was link-checked before entry: **45/45 reachable (HTTP 200)**; two already-stale URLs were corrected pre-entry (Exa docs moved to exa.ai/docs; LMArena rebranded to Arena). This round also adds `llms.txt` at the repository root. The repository itself was renamed by Sean from `useful-dev-resources` to `ForAI` on 2026-10-23; older links redirect.

### AI MCP servers and tool use

| Resource | Useful for / constraints |
|---|---|
| [MCP Inspector](https://github.com/modelcontextprotocol/inspector) | Official visual testing/debugging tool for MCP servers: inspect tools, resources, prompts, and notifications during development. |
| [FastMCP](https://gofastmcp.com/) | High-level Python framework for building MCP servers and clients; much of the ecosystem is built on it. Mind the version — FastMCP 1.x was merged into the official Python SDK lineage. |

### AI agent frameworks and orchestration

| Resource | Useful for / constraints |
|---|---|
| [Browser Use](https://docs.browser-use.com/) | Library that lets an LLM control a real browser to complete tasks; Python. Powerful and fragile in the usual browser-automation ways. |
| [Stagehand (Browserbase)](https://docs.stagehand.dev/) | AI browser-automation SDK (act/extract/observe primitives) on Playwright; pairs with Browserbase's hosted browsers. |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | Automates browser workflows with LLMs and computer vision, including form filling and 2FA handling; AGPL — check license fit. |

### AI agent memory and context

| Resource | Useful for / constraints |
|---|---|
| [Mem0](https://docs.mem0.ai/) | Long-term memory layer for agents: extraction, storage, and retrieval of user/agent memories; self-host or use the hosted platform. |
| [Letta](https://docs.letta.com/) | Stateful-agent platform (the MemGPT lineage): agents with self-editing long-term memory and persistence. |
| [Zep](https://help.getzep.com/) | Long-term memory for AI agents built on a temporal knowledge graph (Graphiti); session/context assembly for production apps. |

### AI agent protocols and interoperability

| Resource | Useful for / constraints |
|---|---|
| [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/latest/) | Linux Foundation protocol for agent-to-agent discovery, task delegation, and interoperability — the complement to MCP's tool access. Check version compatibility between implementations. |
| [A2A protocol (GitHub)](https://github.com/a2aproject/A2A) | Specification source, samples, and SDK links for Agent2Agent. |
| [AG-UI Protocol](https://docs.ag-ui.com/) | Event-based protocol connecting agent backends to user interfaces (streaming state, tool calls, human input). |
| [CopilotKit](https://docs.copilotkit.ai/) | React framework for agent-native UIs; creators/stewards of AG-UI. Use when the frontend must render agent state, not just chat text. |

### AI data and annotation

| Resource | Useful for / constraints |
|---|---|
| [Label Studio](https://labelstud.io/guide/) | Multi-type data labeling platform (text, image, audio) for training and evaluation datasets; open-source core with a hosted tier. |
| [Argilla](https://docs.argilla.io/) | Data curation and human-feedback platform for LLM datasets (now part of Hugging Face); pairs with Distilabel. |
| [Distilabel (Argilla)](https://distilabel.argilla.io/) | Framework for synthetic data generation and AI feedback pipelines for fine-tuning and evaluation. |

### AI evaluation observability and guardrails

| Resource | Useful for / constraints |
|---|---|
| [LMArena (now Arena)](https://arena.ai/) | Crowdsourced blind-preference model arena — the LMSYS Chatbot Arena lineage, now Arena (lmarena.ai redirects here). Preference rankings are not task benchmarks — read both. |
| [Artificial Analysis](https://artificialanalysis.ai/) | Independent model/provider comparisons: quality indexes, speed, and price/performance measured the same way across providers. |
| [LiveBench](https://livebench.ai/) | Contamination-resistant benchmark refreshed with new questions; objective scoring across reasoning, coding, math, and language. |
| [Terminal-Bench](https://www.tbench.ai/) | Benchmark of real terminal tasks for agents (Stanford/Laude Institute); the reference for CLI-agent claims. |
| [Garak (NVIDIA)](https://github.com/NVIDIA/garak) | LLM vulnerability scanner: probes for jailbreaks, leakage, hallucination, toxicity, and injection weaknesses. |
| [PyRIT (Microsoft)](https://github.com/Azure/PyRIT) | Microsoft's Python Risk Identification Toolkit for automated red-teaming of generative AI systems. |
| [MITRE ATLAS](https://atlas.mitre.org/) | Knowledge base of adversary tactics and techniques against AI systems (the ATT&CK companion for ML threats). |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | US NIST's voluntary framework for governing, mapping, measuring, and managing AI risk; useful structure for compliance-minded work. |

### AI machine learning and local inference

| Resource | Useful for / constraints |
|---|---|
| [ComfyUI](https://github.com/comfy-org/ComfyUI) | Node-graph interface and engine for diffusion/image (and video/audio) generation; the standard power-user local image stack. |
| [Hugging Face Diffusers](https://huggingface.co/docs/diffusers) | Pipelines and building blocks for diffusion models (image/video/audio) in PyTorch; model licenses vary per model. |
| [InvokeAI](https://github.com/invoke-ai/InvokeAI) | Polished local image-generation studio (canvas, workflows) built on Diffusers; AGPL — check license fit. |
| [Transformers.js](https://huggingface.co/docs/transformers.js) | Run Transformers models in the browser (WebGPU/WASM) — on-device inference with no server; model size is the constraint. |
| [WebLLM (MLC)](https://webllm.mlc.ai/) | Run LLMs entirely in-browser via WebGPU with an OpenAI-compatible API; part of the MLC stack. |
| [ExecuTorch](https://docs.pytorch.org/executorch/stable/) | PyTorch's on-device runtime for phones, embedded, and edge; export from PyTorch to a lean device binary. |
| [tiktoken (OpenAI)](https://github.com/openai/tiktoken) | Fast BPE tokenizer for OpenAI models; use it to count tokens/cost before calls instead of estimating from characters. |

### AI models and API providers

| Resource | Useful for / constraints |
|---|---|
| [LiteLLM](https://docs.litellm.ai/) | OpenAI-compatible interface over 100+ model providers, as an SDK or self-hosted gateway with budgets, routing, and fallbacks. |
| [Portkey](https://portkey.ai/docs) | AI gateway with observability, guardrails, and routing across providers; hosted and self-hosted options. |

### AI prompt and context engineering

| Resource | Useful for / constraints |
|---|---|
| [Outlines](https://dottxt-ai.github.io/outlines/) | Structured generation library (dottxt): guarantee valid JSON/regex/grammar-constrained output from local and API models. |
| [XGrammar](https://xgrammar.mlc.ai/) | Fast, portable grammar engine for structured generation; used under several serving stacks for JSON/schema output. |
| [Guidance (Microsoft)](https://github.com/guidance-ai/guidance) | Constrain LLM generation with regex/grammar interleaved with generation; effective for strict formats with smaller models. |
| [BAML](https://docs.boundaryml.com/) | DSL for typed prompt functions with schema-aligned parsing; generates clients for Python/TS/Ruby/Go. |

### AI retrieval and vector search

| Resource | Useful for / constraints |
|---|---|
| [Tavily](https://docs.tavily.com/) | Search and extraction API built for LLM agents: search, extract, crawl, and research endpoints with LLM-ready output. |
| [Exa](https://exa.ai/docs) | Neural/keyword web search API designed for AI applications, with contents retrieval and research modes. |
| [Jina Reader](https://jina.ai/reader) | Fetch a URL as clean LLM-friendly Markdown via r.jina.ai; simple ingestion building block. Hosted service terms apply. |
| [Crawl4AI](https://github.com/unclecode/crawl4ai) | Open-source LLM-friendly web crawler: structured extraction and Markdown generation for RAG/agent pipelines. |
| [Marker (Datalab)](https://github.com/datalab-to/marker) | Convert PDFs and documents to Markdown/JSON quickly, with OCR and layout support; check model licenses for the Surya components. |

### AI speech voice and realtime

| Resource | Useful for / constraints |
|---|---|
| [LiveKit Agents](https://docs.livekit.io/agents/) | Framework for realtime voice/multimodal agents on LiveKit's WebRTC infrastructure; Python and Node SDKs. |
| [Pipecat](https://docs.pipecat.ai/) | Open-source Python framework for voice and multimodal conversational agents: pipelines of STT, LLM, TTS, and transports. |
| [Deepgram](https://developers.deepgram.com/) | Speech APIs: fast streaming speech-to-text, text-to-speech, and voice-agent API. Hosted; per-minute pricing. |
| [ElevenLabs](https://elevenlabs.io/docs) | Text-to-speech, voice cloning, and conversational agents API. Hosted service; voice-clone consent and terms matter. |
