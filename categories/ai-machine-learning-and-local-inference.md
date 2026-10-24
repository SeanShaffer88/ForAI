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
