# AI prompt and context engineering

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Added 2026-10-23 in the AI expansion. Primary-source pointers compiled from official documentation and project repositories; not individually re-fetched in this pass. Verify suitability before adoption.

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

## AI expansion round 2 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [Outlines](https://dottxt-ai.github.io/outlines/) | Structured generation library (dottxt): guarantee valid JSON/regex/grammar-constrained output from local and API models. |
| [XGrammar](https://xgrammar.mlc.ai/) | Fast, portable grammar engine for structured generation; used under several serving stacks for JSON/schema output. |
| [Guidance (Microsoft)](https://github.com/guidance-ai/guidance) | Constrain LLM generation with regex/grammar interleaved with generation; effective for strict formats with smaller models. |
| [BAML](https://docs.boundaryml.com/) | DSL for typed prompt functions with schema-aligned parsing; generates clients for Python/TS/Ruby/Go. |

## AI expansion round 3 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [TextGrad](https://github.com/zou-group/textgrad) | Automatic 'textual gradient' optimization of prompts and compound AI systems (Stanford; Nature-published). |

## 2026-10-26 expansion — 1000 AI resources (includes skills.sh directory)

| Resource | Useful for / constraints |
|---|---|
| [Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Anthropic's prompt engineering overview with tools, examples, and analysis toolkit. |
| [Google Prompt Design 101](https://ai.google.dev/gemini-api/docs/prompting-intro) | Google's prompt intro for Gemini with best practices and examples. |
| [Chain-of-Thought Paper](https://arxiv.org/abs/2201.11903) | Wei et al. Chain-of-Thought prompting elicits reasoning in LLMs. |
| [ReAct Paper](https://arxiv.org/abs/2210.03629) | ReAct: synergy of reasoning and acting in LLMs for tool use. |
| [Tree-of-Thought](https://arxiv.org/abs/2305.10601) | ToT: deliberate problem solving with tree search over thoughts. |
| [Graph-of-Thought](https://arxiv.org/abs/2308.09687) | GoT: graph-structured reasoning for LLMs beyond trees. |
| [DSPy Programming](https://dspy-docs.vercel.app/) | DSPy docs for programmatic prompting and optimization without manual prompt tuning. |
| [LMQL Query Language](https://lmql.ai/docs/) | LMQL for declarative prompt programs with constraints. |
| [Instructor Prompting](https://python.useinstructor.com/concepts/prompting/) | Instructor patterns for coupling prompts with Pydantic schemas. |
| [BAML Prompt Language](https://docs.boundaryml.com/docs/home/getting-started/baml-primer) | BAML's typed prompts compiled to LLM calls with error correction. |
| [LangChain Prompt Templates](https://python.langchain.com/docs/concepts/prompt_templates/) | LangChain prompt templates, few-shot, and partial formatting. |
| [LlamaIndex Prompts](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/) | LlamaIndex prompt customization for RAG synthesis and refinement. |
| [PromptLayer Registry](https://docs.promptlayer.com/features/prompt-registry/registry) | PromptLayer registry for versioned prompt management. |
| [HumanLoop Prompts](https://humanloop.com/docs/prompt-management) | HumanLoop prompt IDE with evals and feedback. |
| [Weights & Biases Prompts](https://weave-docs.wandb.ai/guides/core-types/prompts) | W&B Weave prompt versioning and lineage. |
| [Langfuse Prompt Management](https://langfuse.com/docs/prompts/get-started) | Langfuse prompt experiment and caching docs. |
| [Portkey Prompt Management](https://portkey.ai/docs/product/prompt-library) | Portkey prompt library with versioning and conditional caching. |
| [Context Engineering (Anthropic)](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) | Anthropic docs on context windows, caching, and chunking. |
| [Long Context RAG (Google)](https://cloud.google.com/blog/products/ai-machine-learning/long-context-rag) | Google long-context RAG with Gemini 2M tokens — when to stuff vs retrieve. |
| [RAG vs Long Context (Anthropic)](https://www.anthropic.com/research/long-context-rag) | Anthropic analysis of retrieval vs full-context prompting tradeoffs. |
| [Needle vs Haystack Blog](https://www.anyscale.com/blog/needle-in-a-haystack-evaluation) | Anyscale's needle test methodology for long-context eval. |
| [Semantic Prompt Caching (GPTCache)](https://github.com/zilliztech/GPTCache) | GPTCache for semantic caching of LLM responses with embedding lookups. |
| [LLMLingua](https://github.com/microsoft/LLMLingua) | Microsoft LLMLingua for prompt compression — keep quality, cut tokens. |
| [LongLLMLingua](https://github.com/microsoft/LongLLMLingua) | LongLLMLingua for compressing long contexts for RAG. |
| [Recursive Summarization](https://github.com/jerryjliu/llama_index/blob/main/docs/examples/prompt_engineering/advanced_prompts.md) | LlamaIndex recursive summarization pattern for long docs. |
| [Few-Shot Example Selection](https://python.langchain.com/docs/how_to/example_selectors/) | LangChain example selectors for dynamic few-shot prompting. |
| [AutoPrompt (Meta)](https://github.com/ucinlp/autoprompt) | AutoPrompt: gradient-guided search for prompts. |
| [PromptBreeder](https://github.com/vaishnav-mk/prompt-breeder) | Self-referential prompt evolution via LLM mutation. |
| [OPRO (Google)](https://arxiv.org/abs/2309.03409) | Optimization by PROmpting: LLMs as optimizers for prompts. |
| [Giskard Prompt Test](https://docs.giskard.ai/en/latest/knowledge/prompt_testing/index.html) | Giskard prompt testing for bias and hallucination. |
| [Promptfoo Red Team](https://www.promptfoo.dev/docs/red-team/) | Promptfoo red-teaming: prompt injections and jailbreak scans. |
| [Adversarial Prompt (JailbreakChat)](https://www.jailbreakchat.com/) | Community jailbreak prompts collection — use for red-teaming, not exploitation. |
| [Prompt Engineering Guide: Chain-of-Thought, ReAct, and Tool Use (DAIR)](https://www.promptingguide.ai/techniques/cot) | DAIR CoT guide: prompting technique reference with papers and examples. |
| [Learn Prompting: Advanced Techniques](https://learnprompting.org/docs/advanced/zero_shot) | Learn Prompting advanced: zero-shot, few-shot, and role prompting patterns. |
| [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714) | DSPy paper: programmatic LLM pipelines that optimize prompts without hand-tuning. |
