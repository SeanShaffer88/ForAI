# AI speech voice and realtime

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Added 2026-10-23 in AI expansion round 2. Primary-source pointers; every entry link-checked at entry (all reachable). Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [LiveKit Agents](https://docs.livekit.io/agents/) | Framework for realtime voice/multimodal agents on LiveKit's WebRTC infrastructure; Python and Node SDKs. |
| [Pipecat](https://docs.pipecat.ai/) | Open-source Python framework for voice and multimodal conversational agents: pipelines of STT, LLM, TTS, and transports. |
| [Deepgram](https://developers.deepgram.com/) | Speech APIs: fast streaming speech-to-text, text-to-speech, and voice-agent API. Hosted; per-minute pricing. |
| [ElevenLabs](https://elevenlabs.io/docs) | Text-to-speech, voice cloning, and conversational agents API. Hosted service; voice-clone consent and terms matter. |

## AI expansion round 3 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [Faster Whisper](https://github.com/SYSTRAN/faster-whisper) | Whisper reimplemented on CTranslate2: up to 4x faster with less memory; the usual production Whisper choice. |
| [WhisperX](https://github.com/m-bain/whisperX) | Whisper with word-level timestamps, alignment, and speaker diarization for transcription pipelines. |
| [Kokoro TTS](https://github.com/hexgrad/kokoro) | Small (82M) open-weight text-to-speech model with fast CPU inference and an OpenAI-compatible server ecosystem. |
| [F5-TTS](https://github.com/SWivid/F5-TTS) | Diffusion-transformer TTS with zero-shot voice cloning from a short reference clip. |

## 2026-10-26 expansion — 1000 AI resources (includes skills.sh directory)

| Resource | Useful for / constraints |
|---|---|
| [Whisper Large v3](https://github.com/openai/whisper/blob/main/model-card.md) | OpenAI Whisper Large v3 model card: multilingual STT strengths/limits. |
| [Whisper.cpp Large](https://github.com/ggerganov/whisper.cpp#whisper-cpp) | whisper.cpp docs for quantized Whisper inference on CPU/GPU. |
| [Distil-Whisper](https://github.com/huggingface/distil-whisper) | Distilled Whisper: 6x faster, 49% smaller with near-parity accuracy. |
| [Wav2Vec 2.0](https://huggingface.co/docs/transformers/model_doc/wav2vec2) | Facebook Wav2Vec 2.0 for self-supervised speech representation. |
| [Parakeet (NVIDIA NeMo)](https://github.com/NVIDIA/NeMo) | NVIDIA Parakeet 0.6B for fast, accurate ASR via NeMo. |
| [Canary (NVIDIA)](https://huggingface.co/nvidia/canary-1b) | NVIDIA Canary multilingual ASR model card. |
| [AssemblyAI LeMUR](https://www.assemblyai.com/docs/lemur/custom-summary) | LeMUR LLM over transcripts: summarization and Q&A on audio. |
| [Deepgram Nova 3](https://developers.deepgram.com/docs/model/nova-3) | Deepgram Nova-3 streaming STT with low latency and code-switching. |
| [Cartesia Sonic](https://docs.cartesia.ai/getting-started/about-sonic) | Cartesia Sonic: 40ms latency TTS for realtime voice agents. |
| [ElevenLabs Conversational AI](https://elevenlabs.io/docs/conversational-ai/overview) | ElevenLabs agents: turn-taking, tools, and knowledge base for voice. |
| [PlayHT 3.0](https://docs.play.ht/reference/api-generate-tts) | PlayHT API for low-latency voice cloning and TTS. |
| [Respeecher](https://www.respeecher.com/docs) | Respeecher voice cloning docs — check licensing for commercial use. |
| [Piper Voices](https://github.com/rhasspy/piper/blob/master/VOICES.md) | Piper voice list: 50+ languages, offline TTS. |
| [Bark (Suno)](https://github.com/suno-ai/bark) | Suno Bark generative TTS with music and emotion. |
| [MMS (Meta)](https://github.com/facebookresearch/fairseq/tree/main/examples/mms) | Meta MMS for 1k+ language ASR/TTS. |
| [SeamlessM4T v2](https://github.com/facebookresearch/seamless_communication) | Meta Seamless for speech-to-speech translation. |
| [SpeechT5](https://huggingface.co/docs/transformers/model_doc/speecht5) | Microsoft SpeechT5 for TTS and voice conversion. |
| [VALL-E X](https://github.com/Plachtaa/VALL-E-X) | VALL-E X cross-lingual TTS — research code, check license. |
| [RVC (Retrieval-based Voice Conversion)](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) | RVC for voice conversion — popular for character voices. |
| [OpenVoice v2](https://github.com/myshell-ai/OpenVoice) | MyShell OpenVoice for instant voice cloning. |
| [Tortoise TTS](https://github.com/neonbjb/tortoise-tts) | Tortoise multi-voice TTS with expressive control. |
| [Fish Speech](https://github.com/fishaudio/fish-speech) | Fish Audio Fish Speech open TTS with voice cloning. |
| [Daily.co Docs](https://docs.daily.co/docs/introduction) | Daily WebRTC platform for voice agents (alternative to LiveKit). |
| [Agora Conversational AI](https://docs.agora.io/en/conversational-ai/overview/product-overview) | Agora for low-latency conversational AI engine. |
| [Twilio Voice Media Streams](https://www.twilio.com/docs/voice/media-streams) | Twilio media streams for telephony voice agents. |
| [Vonage Voice API](https://developer.vonage.com/en/voice/overview) | Vonage voice API for telephony integrations. |
| [Telnyx Voice API](https://developers.telnyx.com/docs/voice/programmable-voice) | Telnyx programmable voice for calling agents. |
| [WebRTC Native](https://webrtc.org/getting-started/) | WebRTC native docs for building low-latency media transport. |
| [OpenAI Realtime Transport](https://platform.openai.com/docs/guides/realtime/overview) | OpenAI realtime transport: WebRTC vs WebSocket tradeoffs. |
| [Azure Real-time Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/realtime-speech-to-text) | Azure realtime STT with push/streaming. |
| [Google Chirp 3](https://cloud.google.com/speech-to-text/docs/chirp-model) | Google Chirp 3 multilingual STT with 2B param model. |
| [NVIDIA Riva STT](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/asr/asr-overview.html) | Riva ASR streaming docs for GPU deployment. |
| [Picovoice](https://picovoice.ai/docs/) | Picovoice on-device wake word and STT for edge. |
| [Porcupine (Picovoice)](https://github.com/Picovoice/porcupine) | Picovoice Porcupine wake-word via SDK. |
| [Rhino (Picovoice)](https://github.com/Picovoice/rhino) | Rhino intent understanding for voice agents. |
| [Whisper: Robust Speech Recognition via Large-Scale Weak Supervision (OpenAI)](https://arxiv.org/abs/2212.04356) | Whisper paper: 680k hours weak supervision for robust STT across languages. |
| [VALL-E: Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers](https://arxiv.org/abs/2301.02111) | VALL-E: zero-shot TTS with acoustic prompts — foundation for voice cloning docs. |
| [SeamlessM4T: Massively Multilingual & Multimodal Machine Translation](https://arxiv.org/abs/2308.11596) | SeamlessM4T v2: speech-to-speech translation for 100+ languages. |
| [MMS: Scaling Speech Technology to 1,000+ Languages (Meta)](https://arxiv.org/abs/2305.13516) | Meta MMS: 1k-language ASR/TTS via self-supervised pretraining. |
| [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech](https://arxiv.org/abs/2006.04558) | FastSpeech 2: non-autoregressive TTS for low-latency voice agents. |
| [NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech Synthesizers](https://arxiv.org/abs/2304.09116) | NaturalSpeech 2: diffusion TTS for natural zero-shot cloning. |
