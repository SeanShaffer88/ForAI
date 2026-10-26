# AI machine learning and local inference

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |

## AI expansion additions — 2026-10-23

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

## AI expansion round 2 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [ComfyUI](https://github.com/comfy-org/ComfyUI) | Node-graph interface and engine for diffusion/image (and video/audio) generation; the standard power-user local image stack. |
| [Hugging Face Diffusers](https://huggingface.co/docs/diffusers) | Pipelines and building blocks for diffusion models (image/video/audio) in PyTorch; model licenses vary per model. |
| [InvokeAI](https://github.com/invoke-ai/InvokeAI) | Polished local image-generation studio (canvas, workflows) built on Diffusers; AGPL — check license fit. |
| [Transformers.js](https://huggingface.co/docs/transformers.js) | Run Transformers models in the browser (WebGPU/WASM) — on-device inference with no server; model size is the constraint. |
| [WebLLM (MLC)](https://webllm.mlc.ai/) | Run LLMs entirely in-browser via WebGPU with an OpenAI-compatible API; part of the MLC stack. |
| [ExecuTorch](https://docs.pytorch.org/executorch/stable/) | PyTorch's on-device runtime for phones, embedded, and edge; export from PyTorch to a lean device binary. |
| [tiktoken (OpenAI)](https://github.com/openai/tiktoken) | Fast BPE tokenizer for OpenAI models; use it to count tokens/cost before calls instead of estimating from characters. |

## AI expansion round 3 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [Open WebUI](https://docs.openwebui.com/) | Self-hosted ChatGPT-style interface for Ollama/OpenAI-compatible backends, with RAG and user management. |
| [text-generation-webui](https://github.com/oobabooga/textgen) | The long-standing Gradio UI for running local LLMs (llama.cpp/Transformers/ExLlama backends). |
| [MLC LLM](https://github.com/mlc-ai/mlc-llm) | Compile and deploy LLMs across GPUs, phones, and browsers from one stack (the engine behind WebLLM). |
| [OpenVINO](https://docs.openvino.ai/) | Intel's toolkit for optimizing and deploying inference on Intel CPUs, GPUs, and NPUs. |
| [Hugging Face Accelerate](https://huggingface.co/docs/accelerate) | Train PyTorch models on any hardware setup (single GPU to clusters) with minimal code changes; under most HF training. |
| [DeepSpeed](https://www.deepspeed.ai/) | Microsoft's distributed training library (ZeRO sharding) for very large models; also inference kernels. |
| [torchtune](https://meta-pytorch.org/torchtune/) | PyTorch-native library of hackable fine-tuning recipes for popular LLMs (LoRA, full, QAT). |
| [mergekit (Arcee)](https://github.com/arcee-ai/mergekit) | Merge and evolve model weights (SLERP, TIES, DARE and more) — how many community model variants are made. |
| [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) | 8-bit/4-bit optimizers and quantization for PyTorch — the library behind most QLoRA setups. |
| [AWQ (MIT Han Lab)](https://github.com/mit-han-lab/llm-awq) | Activation-aware weight quantization for LLMs: 4-bit models with small quality loss, widely deployed. |
| [Safetensors](https://huggingface.co/docs/safetensors) | The safe, fast tensor file format that replaced pickle-based checkpoints across the HF ecosystem. |
| [GGUF format specification](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md) | The GGUF file-format spec (successor to GGML) used by llama.cpp-ecosystem models and quantization levels. |
| [Ray](https://docs.ray.io/) | Distributed compute framework behind many training/serving stacks (Ray Train, Ray Serve, vLLM deployments). |
| [Ultralytics YOLO](https://docs.ultralytics.com/) | The YOLO object-detection family and tooling; the default starting point for applied computer vision. |
| [Segment Anything (Meta)](https://github.com/facebookresearch/segment-anything) | Meta's promptable segmentation model (SAM) and dataset tooling; a foundation block for vision pipelines. |
| [OpenPipe ART](https://github.com/OpenPipe/ART) | Agent Reinforcement Trainer: RL training (GRPO) for multi-step agents on your own data and backends. |

## 2026-10-26 expansion — 1000 AI resources (includes skills.sh directory)

| Resource | Useful for / constraints |
|---|---|
| [Llama.cpp](https://github.com/ggerganov/llama.cpp) | Efficient C++ inference for Llama-family models on CPU/GPU with quantization — the backbone for many local tools. |
| [GGML](https://github.com/ggerganov/ggml) | Tensor library for machine learning — underpins llama.cpp and whisper.cpp. |
| [Transformers (Hugging Face)](https://github.com/huggingface/transformers) | State-of-the-art transformers in PyTorch/TensorFlow/JAX — model zoo and training recipes. |
| [Diffusers](https://github.com/huggingface/diffusers) | Diffusion models: Stable Diffusion, Flux, SDXL pipelines and training scripts. |
| [PEFT](https://github.com/huggingface/peft) | Parameter-efficient fine-tuning: LoRA, QLoRA, AdaLoRA, prefix tuning for LLMs. |
| [TRL](https://github.com/huggingface/trl) | Transformer reinforcement learning: SFT, DPO, PPO, and GRPO post-training for LLMs. |
| [Accelerate](https://github.com/huggingface/accelerate) | Run PyTorch training at scale across distributed setups with minimal code changes. |
| [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) | GPTQ quantization for LLMs — 4-bit inference with minimal quality loss. |
| [GPTQModel](https://github.com/ModelCloud/GPTQModel) | Modern GPTQ library supporting latest models and Marlin kernels. |
| [ExLlama v2](https://github.com/turboderp/exllamav2) | Fast inference for GPTQ/EXL2 quants with high throughput. |
| [vLLM](https://github.com/vllm-project/vllm) | PagedAttention LLM serving with continuous batching — throughput-optimized inference server. |
| [Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference) | Hugging Face's Rust+Python LLM serving with tensor parallelism and quantization. |
| [MLX-LM](https://github.com/ml-explore/mlx-examples) | MLX examples: LLM inference and fine-tuning on Apple Silicon. |
| [TVM](https://tvm.apache.org/docs/) | Compiler for ML models across hardware backends (TVM/VTA). |
| [Triton Inference Server](https://github.com/triton-inference-server/server) | NVIDIA Triton for serving any model (PyTorch, ONNX, TensorRT) with dynamic batching. |
| [Ray Serve](https://docs.ray.io/en/latest/serve/index.html) | Scalable model serving on Ray for Python models and LLM chains. |
| [BentoML](https://docs.bentoml.com/) | Model serving framework: package any model into REST/gRPC service with adaptive batching. |
| [KServe](https://kserve.github.io/website/) | Kubernetes-native model inference platform (K8s CRDs for model serving). |
| [Kubeflow](https://www.kubeflow.org/docs/) | ML workflows on Kubernetes: training, pipelines, Katib, and KServe integration. |
| [ClearML](https://clear.ml/docs) | Open-source MLOps: experiment manager, data, and orchestration. |
| [Neptune.ai](https://docs.neptune.ai/) | Experiment tracking for ML/ LLM experiments with rich visualizations. |
| [Comet ML](https://www.comet.com/docs/) | Experiment tracking and model production monitoring. |
| [Optuna](https://optuna.org/) | Hyperparameter optimization framework — pruning and distributed search. |
| [Ray Tune](https://docs.ray.io/en/latest/tune/index.html) | Scalable hyperparameter tuning built on Ray. |
| [PyTorch](https://pytorch.org/docs/stable/index.html) | PyTorch 2.x core, torch.compile, and distributed docs. |
| [JAX](https://jax.readthedocs.io/en/latest/) | JAX: composable transforms for NumPy on accelerators; powers Gemma and many research models. |
| [Flax](https://flax.readthedocs.io/en/latest/) | Flax (JAX) for high-performance neural nets. |
| [Keras 3](https://keras.io/) | Keras 3 with PyTorch/JAX/TensorFlow backends — multi-backend model authoring. |
| [Lightning AI](https://lightning.ai/docs/overview) | PyTorch Lightning and Lightning Fabric for scale training without boilerplate. |
| [DeepSpeed](https://www.deepspeed.ai/docs/) | Microsoft DeepSpeed for large-model training: ZeRO, offload, and inference optimizations. |
| [Colossal-AI](https://colossalai.org/docs/) | Large-model training system with heterogeneous parallelism. |
| [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) | NVIDIA's large language model training with tensor/pipeline parallelism. |
| [Liger Kernel](https://github.com/linkedin/Liger-Kernel) | Efficient Triton kernels for LLM training (RoPE, SwiGLU, RMSNorm). |
| [FlashAttention](https://github.com/Dao-AILab/flash-attention) | IO-aware exact attention — enables long-context training and inference. |
| [xFormers](https://github.com/facebookresearch/xformers) | Meta's transformer building blocks: memory-efficient attention and kernels. |
| [Hugging Face Optimum](https://huggingface.co/docs/optimum/index) | Optimize transformers for ONNX, OpenVINO, Habana — quantization and pruning. |
| [Neural Compressor (Intel)](https://github.com/intel/neural-compressor) | Intel's tool for quantization, pruning, and distillation on Intel hardware. |
| [OpenLLM](https://github.com/bentoml/OpenLLM) | Serve any open LLM with BentoML backend — OpenAI-compatible API. |
| [LocalAI](https://localai.io/docs/) | Drop-in OpenAI-compatible API for running many models locally (Llama.cpp, Diffusers). |
| [LM Studio](https://lmstudio.ai/docs) | Desktop app for discovering and running local LLMs with OpenAI-compatible server. |
| [Jan](https://jan.ai/docs) | Open-source ChatGPT alternative that runs 100% offline with extension ecosystem. |
| [GPT4All](https://docs.gpt4all.io/) | Run open LLMs locally via Python and desktop chat — offline RAG support. |
| [KoboldCpp](https://github.com/LostRuins/koboldcpp) | Easy local LLM server with KoboldAI UI and API, optimized for storytelling. |
| [Aphrodite Engine](https://github.com/PygmalionAI/aphrodite-engine) | Large-scale LLM inference fork optimized for roleplay and Pygmalion models. |
| [Tabby](https://tabby.tabbyml.com/docs/welcome) | Self-hosted AI coding assistant (like Copilot) with OpenAPI spec. |
| [Whisper.cpp](https://github.com/ggerganov/whisper.cpp) | Port of OpenAI Whisper for efficient speech-to-text locally. |
| [Piper TTS](https://github.com/rhasspy/piper) | Fast local neural TTS — excellent for offline voice agents. |
| [Stable Diffusion WebUI (AUTOMATIC1111)](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Feature-rich Gradio UI for Stable Diffusion with extensions. |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | Node-based UI for Stable Diffusion, Flux, and video workflows. |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Simple, Midjourney-like UI for SDXL — great for non-technical users. |
| [InvokeAI](https://invoke-ai.github.io/InvokeAI/) | Professional Stable Diffusion toolkit with canvas and batch features. |
| [Oobabooga TextGen WebUI](https://github.com/oobabooga/text-generation-webui) | Gradio UI for many LLM backends (Transformers, llama.cpp, ExLlama). |
| [Hugging Face Datasets](https://huggingface.co/docs/datasets) | Datasets library: 10k+ datasets with streaming and Arrow backend. |
| [Datasets Hub](https://huggingface.co/datasets) | Browse and filter datasets by task, license, and size. |
| [OpenAI Whisper](https://github.com/openai/whisper) | OpenAI's robust multilingual speech recognition — base for many STT pipelines. |
| [PyAnnote](https://github.com/pyannote/pyannote-audio) | Speaker diarization and segmentation — standard for meeting transcription. |
| [SpeechBrain](https://speechbrain.readthedocs.io/en/latest/) | PyTorch speech toolkit: ASR, speaker, enhancement, separation. |
| [NeMo (NVIDIA)](https://docs.nvidia.com/nemo-framework/user-guide/latest/) | NVIDIA NeMo for building ASR, TTS, and LLM on GPU. |
| [Coqui TTS](https://github.com/coqui-ai/TTS) | Coqui's open TTS and voice cloning (check fork maintenance). |
| [Edge Impulse](https://docs.edgeimpulse.com/docs) | TinyML platform for deploying models to edge devices. |
| [TensorFlow Lite](https://ai.google.dev/edge/litert) | LiteRT (TFLite) for on-device ML on mobile and microcontrollers. |
| [Core ML](https://developer.apple.com/documentation/coreml) | Apple Core ML for on-device inference on iPhone/Mac. |
| [ONNX Model Zoo](https://github.com/onnx/models) | Pretrained ONNX models across vision, NLP, and speech. |
| [Hugging Face Hub Python](https://huggingface.co/docs/huggingface_hub/index) | Hub Python library: push, download, and manage models/datasets programmatically. |
| [DVC](https://dvc.org/doc) | Data version control for ML experiments — Git for data and models. |
| [Great Expectations](https://docs.greatexpectations.io/docs/) | Data validation for ML pipelines — expectations and data docs. |
| [WhyLabs LangKit](https://github.com/whylabs/langkit) | Open-source LLM monitoring: prompt injection, toxicity, and quality signals. |
| [Giskard](https://docs.giskard.ai/) | Open-source LLM testing: robustness, bias, and vulnerability scans. |
| [DeepEval](https://docs.confident-ai.com/) | LLM evaluation framework with 15+ metrics and LLM-as-judge. |
| [Ragas](https://docs.ragas.io/en/latest/) | RAG evaluation: faithfulness, answer relevancy, context recall/precision. |
| [LangSmith](https://docs.smith.langchain.com/) | LangChain's observability and evaluation platform for LLM apps. |
| [Helicone](https://docs.helicone.ai/) | LLM observability proxy: logging, caching, rate limits, and cost tracking. |
| [PromptLayer](https://docs.promptlayer.com/) | Prompt management, versioning, and analytics for LLMs. |
| [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135) | FlashAttention: IO-aware exact attention for long-context training/inference efficiency. |
| [DeepSpeed: System Optimizations Enable Training Deep Learning Models with Over 100 Billion Parameters](https://arxiv.org/abs/1910.02054) | DeepSpeed paper: ZeRO and offload for large-model training on limited GPUs. |
| [vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180) | vLLM paper: PagedAttention and continuous batching for high-throughput serving. |
| [QLoRA 4-bit Finetuning already covered but use AWQ paper](https://arxiv.org/abs/2306.00978) | AWQ paper: activation-aware quantization for 4-bit LLM inference with quality. |
