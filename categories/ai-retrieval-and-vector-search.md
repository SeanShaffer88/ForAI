# AI retrieval and vector search

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Added 2026-10-23 in the AI expansion. Primary-source pointers compiled from official documentation and project repositories; not individually re-fetched in this pass. Verify suitability before adoption.

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

## AI expansion round 2 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [Tavily](https://docs.tavily.com/) | Search and extraction API built for LLM agents: search, extract, crawl, and research endpoints with LLM-ready output. |
| [Exa](https://exa.ai/docs) | Neural/keyword web search API designed for AI applications, with contents retrieval and research modes. |
| [Jina Reader](https://jina.ai/reader) | Fetch a URL as clean LLM-friendly Markdown via r.jina.ai; simple ingestion building block. Hosted service terms apply. |
| [Crawl4AI](https://github.com/unclecode/crawl4ai) | Open-source LLM-friendly web crawler: structured extraction and Markdown generation for RAG/agent pipelines. |
| [Marker (Datalab)](https://github.com/datalab-to/marker) | Convert PDFs and documents to Markdown/JSON quickly, with OCR and layout support; check model licenses for the Surya components. |

## AI expansion round 3 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [GraphRAG (Microsoft)](https://microsoft.github.io/graphrag/) | Microsoft's graph-based RAG: build a knowledge graph from a corpus for global, theme-level questions naive RAG misses. |
| [LightRAG](https://github.com/HKUDS/LightRAG) | Lightweight graph-enhanced RAG framework (HKUDS) with incremental updates; simpler than full GraphRAG. |
| [RAGFlow](https://github.com/infiniflow/ragflow) | Open-source RAG engine with deep document understanding, chunking visualizations, and agent/canvas features. |
| [Onyx (formerly Danswer)](https://docs.onyx.app/) | Open-source enterprise search and AI chat over company knowledge (connectors, permissions-aware). |
| [Chonkie](https://github.com/feyninc/chonkie) | Fast, feathery text chunking library for RAG: many chunking strategies with a small footprint. |
| [RAGatouille](https://github.com/AnswerDotAI/RAGatouille) | Easy ColBERT late-interaction retrieval for RAG — strong quality per index size. |
| [Turbopuffer](https://turbopuffer.com/docs) | Serverless vector + full-text search built on object storage; cheap at large scale. |
| [Apify](https://docs.apify.com/) | Web scraping and automation platform (Actors) increasingly used as agent tooling and a data source for RAG. |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Baidu's multilingual OCR toolkit; a standard choice for document ingestion pipelines. |
| [Surya](https://github.com/datalab-to/surya) | OCR, layout analysis, and table recognition in 90+ languages; the engine under Marker. |

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain |
| [serviette](https://github.com/pathwaycom/serviette) | A no-code RAG server that keeps answers in sync with your documents. Works with 8 vector databases. Built on Pathway. |
