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

## 2026-10-26 expansion — 1000 AI resources (includes skills.sh directory)

| Resource | Useful for / constraints |
|---|---|
| [HELM (Stanford)](https://crfm.stanford.edu/helm/latest/) | HELM holistic evaluation for language models across scenarios. |
| [Open LLM Leaderboard v2](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | Hugging Face Open LLM Leaderboard v2 with contamination checks. |
| [Chatbot Arena Leaderboard](https://lmarena.ai/?leaderboard) | Human-vote Elo leaderboard — real preference over static benchmarks. |
| [MMLU (Hendrycks)](https://github.com/hendrycks/test) | MMLU 57-task benchmark for language understanding. |
| [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) | Harder MMLU-Pro with 10 options and reasoning. |
| [GPQA](https://github.com/idavidrein/gpqa) | GPQA: graduate-level science questions — hard for frontier models. |
| [MATH](https://github.com/hendrycks/math) | MATH dataset for quantitative reasoning. |
| [GSM8K](https://github.com/openai/grade-school-math) | GSM8K grade-school math word problems. |
| [LiveBench](https://livebench.ai/#/) | LiveBench: continuously updated, contamination-resistant benchmark. |
| [SimpleQA (OpenAI)](https://github.com/openai/simple-evals) | OpenAI SimpleQA for factuality. |
| [FACTS Grounding](https://www.kaggle.com/competitions/facts-grounding) | Kaggle FACTS grounding leaderboard for RAG. |
| [IFEval](https://github.com/google-research/google-research/tree/master/instruction_following_eval) | Instruction-following evaluation with verifiable constraints. |
| [WildBench](https://wildbench.github.io/) | WildBench for human-aligned evaluation on wild prompts. |
| [AlpacaEval 2](https://tatsu-lab.github.io/alpaca_eval/) | AlpacaEval 2: win-rate vs GPT-4 Turbo with length control. |
| [MixEval](https://mixeval.github.io/) | MixEval: mixed real-world benchmark with ground truth. |
| [BIG-Bench Hard](https://github.com/suzgunmirac/BIG-Bench-Hard) | BBH 23 challenging BIG-Bench tasks. |
| [ARC Prize](https://arcprize.org/) | ARC Prize for abstract reasoning — frontier for AGI claims. |
| [SEAL Leaderboards](https://scale.com/leaderboard) | Scale SEAL leaderboards: instruction following, tool use, etc. |
| [Scale Spellbook](https://scale.com/spellbook) | Scale Spellbook for evaluating and red-teaming models. |
| [Arize Phoenix Evals](https://docs.arize.com/phoenix/evaluation) | Phoenix evaluation templates: hallucination, QA, toxicity. |
| [WhyLabs LangKit UDFs](https://github.com/whylabs/langkit/blob/main/langkit/docs/features.md) | LangKit UDFs for injection, jailbreak, and sentiment. |
| [Giskard Scan](https://docs.giskard.ai/en/latest/guides/scan/index.html) | Giskard scan for LLM vulnerabilities: hallucination, bias. |
| [Deepchecks](https://docs.deepchecks.com/) | Deepchecks for continuous validation of LLM and ML pipelines. |
| [TruLens](https://www.trulens.org/trulens_eval/getting_started/) | TruLens for RAG triad: context relevance, groundedness, answer relevance. |
| [Promptfoo](https://www.promptfoo.dev/docs/getting-started/) | Promptfoo: open-source evals with red-teaming and CI. |
| [Inspect (UK AISI)](https://inspect.ai-safety-institute.org.uk/) | UK AISI Inspect for model safety evaluations. |
| [EleutherAI LM Harness](https://github.com/EleutherAI/lm-evaluation-harness) | Standard harness for 60+ LLM benchmarks. |
| [HELMET (RAG Long Context)](https://github.com/princeton-nlp/HELMET) | HELMET for long-context and RAG evaluation. |
| [RULER](https://github.com/NVIDIA/RULER) | NVIDIA RULER for long-context retrieval and reasoning. |
| [Needle in a Haystack (Greg Kamradt)](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) | NIAH synthetic recall benchmark for long context. |
| [LongBench](https://github.com/THUDM/LongBench) | LongBench for long-context understanding across tasks. |
| [ZeroSpan](https://github.com/mit-llm/zerospan) | Zero-span retrieval eval for RAG. |
| [ARES (Stanford)](https://github.com/stanford-futuredata/ARES) | ARES: automated RAG evaluation with synthetic data. |
| [Patronus FinanceBench](https://github.com/patronus-ai/FinanceBench) | FinanceBench for financial QA grounding. |
| [HaluEval](https://github.com/RUCAIBox/HaluEval) | HaluEval for hallucination detection across tasks. |
| [FaithScore](https://github.com/bwanglzu/FaithScore) | FaithScore for fine-grained faithfulness of LLM responses. |
| [Toxicity (Perspective API)](https://developers.perspectiveapi.com/s/docs) | Perspective API for toxicity scoring — guardrail primitive. |
| [Llama Guard 3](https://github.com/meta-llama/PurpleLlama/tree/main/Llama-Guard3) | Meta Llama Guard 3 for input/output safety classification. |
| [ShieldGemma](https://ai.google.dev/gemma/docs/shieldgemma) | Google ShieldGemma safety classifier for Gemma. |
| [WildGuard](https://github.com/allenai/wildguard) | AllenAI WildGuard for harm detection. |
| [NVIDIA NeMo Guardrails Toolkit](https://github.com/NVIDIA/Nemo-Guardrails) | Programmable rails: topical, execution, and moderation. |
| [Guardrails AI Hub](https://hub.guardrailsai.com/) | Guardrails Hub validators: PII, regex, and JSON schema enforcement. |
| [Pydantic Validations](https://docs.pydantic.dev/latest/concepts/validators/) | Pydantic validators for structured-output guardrails. |
| [Great Expectations for LLM](https://greatexpectations.io/blog/llm-validation) | GE patterns for LLM data validation. |
| [Cleanlab](https://cleanlab.ai/blog/data-centric-ai/) | Cleanlab for finding label errors — useful for eval dataset cleaning. |
| [Argilla](https://argilla.io/docs/) | Argilla for data annotation and human-in-the-loop evals. |
| [Label Studio](https://labelstud.io/guide) | Label Studio for RLHF and eval annotation workflows. |
| [HELM: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) | HELM paper: holistic scenarios for LLM evaluation beyond single benchmarks. |
| [MMLU: Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300) | MMLU: 57 tasks for broad language understanding — standard for model reports. |
| [GPQA: A Graduate-Level Google-Proof Q&A Benchmark](https://arxiv.org/abs/2311.12022) | GPQA: hard science questions that remain challenging for frontier models. |
| [MATH: Quantitative Reasoning (Hendrycks MATH)](https://arxiv.org/abs/2103.03874) | Hendrycks MATH: 12.5k competition problems for quantitative reasoning eval. |
| [GSM8K: Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168) | GSM8K: grade-school math word problems for reasoning and verifier training. |
| [IFEval: Instruction-Following Evaluation for Large Language Models](https://arxiv.org/abs/2311.07911) | IFEval: verifiable instruction following with constraints. |
| [SimpleQA: Measuring Short-Form Factuality (OpenAI)](https://arxiv.org/abs/2411.04368) | SimpleQA: short-form factuality with human-verified answers. |
| [WhyLabs LangKit Documentation (injection UDFs)](https://github.com/whylabs/langkit#fallback-57) | WhyLabs LangKit repo: injection, jailbreak, and quality UDFs for LLM monitoring. |
| [Giskard: Evaluation and Testing for ML Models](https://github.com/Giskard-AI/giskard) | Giskard open-source: LLM scan for hallucination, bias, and robustness. |
| [TruLens Eval: Feedback Functions for LLM Apps](https://github.com/truera/trulens) | TruLens repo: RAG triad evaluation with groundedness and relevance. |
| [Promptfoo: Test Your LLM App Locally (Red Team)](https://github.com/promptfoo/promptfoo) | Promptfoo repo: open-source evals with red-teaming and CI. |
