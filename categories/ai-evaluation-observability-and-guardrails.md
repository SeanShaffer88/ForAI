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

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | A framework for few-shot evaluation of language models. |
| [evidently](https://github.com/evidentlyai/evidently) | Evidently is ​​an open-source ML and LLM observability framework. Evaluate, test, and monitor any AI-powered system or data pipeline. From tabular data to Gen AI. 100+ metrics. |
| [giskard-oss](https://github.com/Giskard-AI/giskard-oss) | 🐢 Open-Source Evaluation & Testing library for LLM Agents |
| [langwatch](https://github.com/langwatch/langwatch) | Open-Source Agent Observability & Evals for AI Platform teams. Trace, test, route and govern every agent & coding assistant in the company. |

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

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
<!-- expansion-2026-11-11:end -->
