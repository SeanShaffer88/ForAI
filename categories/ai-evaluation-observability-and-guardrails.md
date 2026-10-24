# AI evaluation observability and guardrails

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Added 2026-10-23 in the AI expansion. Primary-source pointers compiled from official documentation and project repositories; not individually re-fetched in this pass. Verify suitability before adoption.

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

## AI expansion round 2 additions — 2026-10-23

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

## AI expansion round 3 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [Opik (Comet)](https://www.comet.com/docs/opik/) | Open-source LLM evaluation and tracing platform from Comet: datasets, experiments, and production monitoring. |
| [Braintrust](https://www.braintrust.dev/docs) | Eval-first AI product platform: scoring, datasets, prompt playground, and production logging. |
| [Evidently AI](https://docs.evidentlyai.com/) | Open-source evaluation and monitoring for ML and LLM systems, with reports and a monitoring service. |
| [TensorZero](https://github.com/tensorzero/tensorzero) | Open-source stack unifying an LLM gateway, observability, evals, and optimization (prompts/models from data). |
| [OpenLLMetry (Traceloop)](https://github.com/traceloop/openllmetry) | OpenTelemetry-based instrumentation for LLM apps and frameworks; pairs with any OTel backend. |
| [AgentOps](https://docs.agentops.ai/) | Observability platform purpose-built for agents: session replays, cost/latency, and failure analysis. |
| [LLM Guard (Protect AI)](https://github.com/protectai/llm-guard) | Input/output scanners for LLM apps: prompt-injection, PII, toxicity, and secrets detection/mitigation. |
| [Lakera Guard](https://docs.lakera.ai/) | Hosted runtime defense against prompt injection and data leakage, with a public prompt-attack database (Gandalf lineage). |
