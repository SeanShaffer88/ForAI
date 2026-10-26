# AI models and API providers

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Added 2026-10-23 in the AI expansion. Primary-source pointers compiled from official documentation and project repositories; not individually re-fetched in this pass. Verify suitability before adoption.

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

## AI expansion round 2 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [LiteLLM](https://docs.litellm.ai/) | OpenAI-compatible interface over 100+ model providers, as an SDK or self-hosted gateway with budgets, routing, and fallbacks. |
| [Portkey](https://portkey.ai/docs) | AI gateway with observability, guardrails, and routing across providers; hosted and self-hosted options. |

## AI expansion round 3 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/) | AWS's managed foundation-model service: model choice, Agents, Knowledge Bases, and guardrails inside AWS. |
| [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/) | Microsoft's AI platform: Azure OpenAI and a broad model catalog, agents, and evaluation tooling. |
| [NVIDIA NIM](https://docs.nvidia.com/nim/) | NVIDIA's optimized inference microservices for deploying models on NVIDIA GPUs, cloud or on-prem. |
| [xAI (Grok) API](https://docs.x.ai/) | xAI's API for Grok models, including realtime data features; OpenAI-compatible endpoints. |
| [Perplexity API](https://docs.perplexity.ai/) | Search-grounded answer APIs (Sonar) and chat completions with citations. |
| [DeepSeek API](https://api-docs.deepseek.com/) | DeepSeek's API platform for its chat and reasoning models; OpenAI/Anthropic-compatible formats. |
| [Cerebras Inference](https://inference-docs.cerebras.ai/) | Wafer-scale inference with very high tokens/sec for open models; OpenAI-compatible API. |
| [Voyage AI](https://docs.voyageai.com/) | Embeddings and rerankers (general, code, finance, law) — a common upgrade over default embedding models for RAG. |
| [Baseten](https://docs.baseten.co/) | Hosted inference for custom and open models with autoscaling GPUs and model APIs (Truss). |

## 2026-10-26 expansion — 1000 AI resources (includes skills.sh directory)

| Resource | Useful for / constraints |
|---|---|
| [Anthropic Claude API](https://docs.anthropic.com/claude/docs) | Claude 4 family: API, prompt engineering, tool use, and extended thinking. |
| [Vertex AI Generative AI](https://cloud.google.com/vertex-ai/generative-ai/docs) | Google Cloud's managed Gemini, Claude, and open-model APIs on Vertex AI. |
| [AWS Bedrock Models](https://docs.aws.amazon.com/bedrock/latest/userguide/models.html) | Managed foundation models on Bedrock: Anthropic, Meta, Mistral, Amazon Nova, and Cohere. |
| [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview) | Azure-hosted OpenAI models with enterprise controls, content filters, and VNet integration. |
| [OpenAI Models Overview](https://platform.openai.com/docs/models) | GPT-4o, o-series reasoning, and embedding models: capabilities, pricing, and rate limits. |
| [Cohere Platform](https://docs.cohere.com/v2/docs) | Command, Embed v3, Rerank 3.5, and Classify APIs for enterprise RAG. |
| [Mistral La Plateforme](https://docs.mistral.ai/capabilities) | Mistral Large, Medium, Codestral, and Pixtral via La Plateforme and Azure. |
| [GroqCloud Console](https://console.groq.com/docs/quickstart) | Ultra-fast LPU inference for Llama, Mixtral, and Gemma — check rate limits and context windows. |
| [Together AI Models](https://docs.together.ai/docs/inference-models) | Hosted open models: Llama 405B, Qwen, DeepSeek-R1 with batch and fine-tune options. |
| [Fireworks AI Models](https://docs.fireworks.ai/models) | Fast inference for 100+ open models with function calling and LoRA serving. |
| [Replicate Models](https://replicate.com/explore) | Community and official models (LLM, diffusion, audio) with one OpenAI-compatible API. |
| [OpenRouter Models](https://openrouter.ai/models) | Single API across 300+ models/ providers with automatic failover and pricing comparisons. |
| [DeepSeek Platform](https://api-docs.deepseek.com/quick_start) | DeepSeek-V3 and R1 reasoning models — OpenAI-compatible, check context and pricing. |
| [Perplexity Sonar API](https://docs.perplexity.ai/guides/getting-started) | Search-grounded answer APIs with citations for research agents. |
| [xAI Grok API](https://docs.x.ai/docs/models) | Grok 4 models with live X search grounding and OpenAI-compatible chat completions. |
| [Cerebras Inference](https://inference-docs.cerebras.ai/introduction) | Waferscale inference — highest tokens/sec for open models; check quota tiers. |
| [SambaNova Cloud](https://docs.sambanova.ai/cloud) | SambaNova's fast inference API for Llama 3.3 and Qwen with free tier. |
| [Lambda Labs Inference](https://docs.lambdalabs.com/inference) | Lambda inference API for open models on H100 clusters. |
| [Anyscale Endpoints](https://docs.anyscale.com/endpoints/overview) | Anyscale hosted open models on Ray — autoscaling and fine-tuning. |
| [OctoAI](https://octo.ai/docs) | Hosted open-model inference with media generation and efficient GPU sharing. |
| [Baseten Truss](https://docs.baseten.co/overview) | Hosted inference for custom models with autoscaling and dedicated deployments. |
| [RunPod Serverless](https://docs.runpod.io/serverless/overview) | Serverless GPU endpoints for any containerised model with autoscaling. |
| [CoreWeave Inference](https://docs.coreweave.com/inference) | CoreWeave cloud inference for large models on H100/GB200. |
| [AI21 Jamba](https://docs.ai21.com/docs/jamba-models) | AI21's Jamba (Mamba+Transformer) long-context models via AI21 Studio. |
| [Aleph Alpha Luminous](https://docs.aleph-alpha.com/docs/introduction) | Aleph Alpha's Luminous models hosted in EU with Pharia platform. |
| [Stability AI Platform](https://platform.stability.ai/docs/getting-started) | Stable Diffusion 3.5, SDXL, and Stable Audio/V Video via API. |
| [Midjourney API (unofficial docs)](https://docs.midjourney.com/docs) | Midjourney v6/v7 image generation — check official Discord/API access terms. |
| [Ideogram API](https://developer.ideogram.ai/docs) | Ideogram 2/3 for high-quality text-in-image generation. |
| [ElevenLabs API](https://elevenlabs.io/docs/api-reference/introduction) | Voice cloning, TTS, and sound effects — listed here for model provider completeness. |
| [Voyage AI Embeddings](https://docs.voyageai.com/docs/embeddings) | Voyage-3 family: general, code, finance, law embeddings and rerankers. |
| [Jina Embeddings](https://jina.ai/embeddings) | Jina embeddings v3: multilingual, code, and late-interaction ColBERT. |
| [Mixedbread AI](https://www.mixedbread.com/docs) | mxbai embeddings and rerank: strong RAG retrieval quality. |
| [Nomic Embed](https://docs.nomic.ai/atlas/embeddings) | Nomic Embed text and Atlas visualization; open weights. |
| [BAAI BGE](https://github.com/FlagOpen/FlagEmbedding) | BAAI General Embedding series: widely used open embedding and reranker models. |
| [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers/index) | Hosted inference via Hugging Face's provider fleet — one API across tasks. |
| [Together Fine-Tuning](https://docs.together.ai/docs/fine-tuning) | Fine-tune open models on Together with LoRA and full fine-tune recipes. |
| [Fireworks Fine-Tuning](https://docs.fireworks.ai/fine-tuning/quickstart) | Fine-tune and serve custom LoRA adapters on Fireworks. |
| [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library) | Curated prompts for Claude across tasks — good reference for prompt engineering. |
| [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) | OpenAI's official prompting patterns, function calling, and structured outputs. |
| [Azure AI Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/overview) | Azure AI Foundry model catalog: OpenAI, Meta, Mistral, Cohere, and open models in one place. |
| [NVIDIA NIM Microservices](https://docs.nvidia.com/nim/large-language-models/latest/introduction.html) | NVIDIA's optimized inference containers for LLMs, embedding, rerank, and vision on GPU. |
| [Hugging Face Model Cards](https://huggingface.co/docs/hub/model-cards) | How to read model cards for license, training data, and intended use. |
| [Papers With Code SOTA](https://paperswithcode.com/sota) | Leaderboards by task — check which dataset/split a SOTA claim uses. |
| [LMSYS Chatbot Arena](https://lmarena.ai/) | Human preference leaderboard for LLMs and vision models — Elo rankings. |
| [Vercel AI Gateway](https://vercel.com/docs/ai-sdk/gateway) | Vercel's gateway to 100+ models with observability and cost controls. |
| [Cloudflare AI](https://developers.cloudflare.com/workers-ai/) | Workers AI: 30+ open models at the edge with vectorize and R2 integration. |
| [Hugging Face Hub Inference](https://huggingface.co/docs/inference-endpoints/index) | Dedicated inference endpoints for private model deployments on HF. |
| [MiniMax API](https://www.minimax.io/platform) | MiniMax M2 and audio/video models — check pricing and language strengths. |
| [Qwen (Alibaba Cloud)](https://qwenlm.github.io/blog/) | Qwen2.5/3 family and Qwen-VL — strong open multilingual and code models. |
| [Gemma (Google)](https://ai.google.dev/gemma) | Gemma 3 open models from Google — efficient for local/edge inference. |
| [Phi-3 / Phi-4 (Microsoft)](https://azure.microsoft.com/en-us/products/phi) | Microsoft Phi small language models — excellent quality per size for edge. |
| [Llama 3.3 (Meta)](https://www.llama.com/docs/overview) | Meta Llama 3.3 models: 8B to 405B with instruct and tool-use variants. |
| [Command R+ (Cohere)](https://docs.cohere.com/docs/command-r-plus) | Cohere Command R/R+ for RAG and tool calling with long context. |
| [Claude Computer Use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) | Anthropic's computer-use API for agents that interact with desktops/browsers. |
| [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime) | Realtime voice API (WebRTC/WebSocket) for low-latency speech agents. |
| [Google Live API](https://ai.google.dev/api/live) | Gemini Live low-latency multimodal (speech/video) streaming API. |
| [Azure Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/) | Azure AI Speech: TTS, STT, translation, and custom voices. |
| [NVIDIA Riva](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/index.html) | NVIDIA Riva for on-prem speech AI: ASR, TTS, and translation on GPU. |
| [Stability Video](https://platform.stability.ai/docs/api-reference#tag/generate) | Stability AI video generation API reference. |
| [Runway API](https://docs.dev.runwayml.com/api) | Runway Gen-3/4 video generation and editing APIs for agents. |
| [FAL AI](https://fal.ai/models) | FAL's fast inference for diffusion, Flux, SDXL, and video models. |
| [CogVideo (Zhipu)](https://www.zhipuai.cn/devcenter) | Zhipu CogVideo and ChatGLM APIs for video and chat. |
| [Baichuan API](https://platform.baichuan-ai.com/docs) | Baichuan 2 models API for Chinese-centric tasks. |
| [Yi (01.AI)](https://platform.lingyiwanwu.com/docs) | Yi-Large 34B and Yi-Vision models via 01.AI platform. |
| [Moonshot (Kimi)](https://platform.moonshot.cn/docs) | Moonshot Kimi long-context (128k-200k) chat API. |
| [StepFun (Step)](https://platform.stepfun.com/docs) | Step 1/2 models from StepFun with vision and code strengths. |
| [MiniMax Audio](https://www.minimax.io/audio-api) | MiniMax voice cloning and TTS APIs. |
| [Hume AI](https://dev.hume.ai/docs) | Empathic voice and emotion measurement APIs for expressive speech. |
| [PlayHT](https://docs.play.ht/reference/api-getting-started) | PlayHT voice generation, cloning, and conversational agents. |
| [Cartesia](https://docs.cartesia.ai/) | Cartesia Sonic: ultra-low-latency TTS for realtime agents. |
| [Deepgram](https://developers.deepgram.com/docs) | ASR, streaming STT, and voice agent APIs with low latency. |
| [AssemblyAI](https://www.assemblyai.com/docs) | Speech-to-text with speaker diarization, sentiment, and LeMUR LLM. |
| [Replicate Flux](https://replicate.com/black-forest-labs/flux-schnell) | Flux Schnell/Pro on Replicate — fast, high-quality text-to-image. |
| [Black Forest Labs](https://docs.bfl.ml/) | BFL's Flux family technical docs and API. |
| [Ideogram 3.0](https://ideogram.ai/api) | Ideogram 3.0 API for text-accurate image generation. |
| [Leonardo AI](https://docs.leonardo.ai/docs) | Leonardo's image and motion generation APIs. |
| [Midjourney Documentation](https://docs.midjourney.com/docs/quick-start) | Midjourney quick start and parameter reference — verify API availability. |
| [Pika API](https://docs.pika.art/api) | Pika Labs video generation and editing. |
| [Luma Dream Machine](https://lumalabs.ai/dream-machine/api) | Luma AI video generation API for agents. |
| [Suno AI](https://suno.com/docs) | Suno AI music generation API (if available) — verify terms. |
| [Udio](https://www.udio.com/docs) | Udio music generation service docs. |
| [Kimi K2](https://platform.moonshot.cn/docs/api/chat) | Moonshot Kimi K2 frontier chat model API. |
| [Claude Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) | Anthropic prompt caching to reduce latency and cost for repeated contexts. |
| [Attention Is All You Need (Transformer)](https://arxiv.org/abs/1706.03762#fallback-0) | Foundational Transformer paper: attention mechanism underlying all modern LLMs — essential for model selection and architecture understanding. |
| [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) | BERT paper for understanding encoder models and masked LM pretraining — still relevant for embedding and classification models. |
| [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) | GPT-3 paper: scale, few-shot prompting, and emergent capabilities that define modern provider APIs. |
| [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) | GPT-4 report: multimodal capabilities, eval methodology, and alignment — reference for frontier model behavior. |
| [Llama 3 Herd of Models](https://arxiv.org/abs/2407.09288) | Meta Llama 3.1 405B report: training, instruction tuning, and tool use for open-model provider selection. |
| [Mistral 7B (Jiang et al.)](https://arxiv.org/abs/2310.06825) | Mistral 7B paper: sliding window attention and strong 7B baseline for local inference and provider routing. |
| [DeepSeek-V2: A Strong, Economical, and Efficient MoE](https://arxiv.org/abs/2405.04434) | DeepSeek-V2 MoE architecture: efficient inference for reasoning models via DeepSeek API. |
| [Phi-3 Technical Report: A Highly Capable Small Model](https://arxiv.org/abs/2404.14219) | Phi-3 small model report: quality per size for edge inference and cost-sensitive routing. |
| [Gemma 2: Improving Open Language Models](https://arxiv.org/abs/2408.00118) | Google Gemma 2 report: open models with distillation and safety — alternative to Llama for local use. |
| [Qwen2 Technical Report](https://arxiv.org/abs/2407.10671) | Alibaba Qwen2 report: multilingual and code strengths across 0.5B–72B sizes. |
| [Chinchilla: Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.02155) | Chinchilla scaling laws: optimal tokens vs parameters for training cost decisions. |
| [Scaling Laws for Neural Language Models (Kaplan)](https://arxiv.org/abs/2001.08361) | Early scaling laws paper: power-law for model size, data, and compute. |
| [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) | Anthropic Constitutional AI: RL from AI feedback for Claude alignment — provider policy context. |
| [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290) | DPO paper: simpler alignment without RLHF — used by many open-model fine-tunes. |
| [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | LoRA paper: efficient fine-tuning via low-rank adapters — basis for provider fine-tune APIs. |
| [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) | QLoRA paper: 4-bit quantization + LoRA for consumer-GPU fine-tuning — pattern for custom model deployment. |
| [Training language models to follow instructions with human feedback (InstructGPT)](https://arxiv.org/abs/2203.02155#fallback-16) | InstructGPT paper: RLHF recipe behind OpenAI and Anthropic alignment. |
