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

## 2026-10-26 expansion — 1000 AI resources (includes skills.sh directory)

| Resource | Useful for / constraints |
|---|---|
| [Milvus Lite](https://milvus.io/docs/milvus_lite.md) | Milvus Lite for embedded vector search without server. |
| [Weaviate Cloud](https://weaviate.io/developers/weaviate) | Weaviate Cloud with hybrid, rerank, and generative modules. |
| [Pinecone Serverless](https://docs.pinecone.io/guides/get-started/quickstart) | Pinecone serverless: autoscaling vectors with namespaces. |
| [Upstash Vector](https://upstash.com/docs/vector/overall/getstarted) | Serverless vector DB with REST API for edge functions. |
| [Supabase Vector (pgvector)](https://supabase.com/docs/guides/ai/vector-columns) | Supabase guide to pgvector: hybrid search with Postgres. |
| [Neon Vector](https://neon.tech/docs/extensions/pgvector) | Neon Postgres with pgvector for serverless RAG. |
| [MongoDB Atlas Vector Search](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/) | Atlas Vector Search with $vectorSearch aggregation. |
| [Rockset (OpenAI)](https://docs.rockset.com/documentation/) | Rockset for realtime search and analytics — now part of OpenAI. |
| [Typesense](https://typesense.org/docs/guide/) | Typesense open-source search with vector and hybrid modes. |
| [Vespa](https://docs.vespa.ai/) | Vespa: big-data serving for search, recommendation, and RAG. |
| [Sphinx](https://sphinxsearch.com/docs/current.html) | Sphinx search engine for full-text — legacy but integrated in some RAG stacks. |
| [OpenSearch k-NN](https://opensearch.org/docs/latest/search-plugins/knn/index/) | OpenSearch k-NN plugin for vector search at AWS scale. |
| [Redis Vector Library](https://redis.io/docs/latest/develop/interact/search-and-query/query/vector-search/) | Redis vector search with RediSearch — hybrid queries. |
| [Turbopuffer](https://turbopuffer.com/docs/quickstart) | Turbopuffer serverless vector+FTS on object storage. |
| [Vald](https://vald.vdaas.org/docs/) | Vald: highly scalable distributed vector search engine. |
| [Vearch](https://github.com/vearch/vearch) | Vearch: distributed vector search from JD.com. |
| [Milvus Operators](https://milvus.io/docs/install_cluster-milvusoperator.md) | Milvus operator for Kubernetes deployments. |
| [Haystack Document Stores](https://docs.haystack.deepset.ai/docs/document_store) | Haystack document stores for RAG pipelines. |
| [LlamaIndex Vector Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/) | LlamaIndex integrations for 30+ vector stores. |
| [LangChain Vector Stores](https://python.langchain.com/docs/integrations/vectorstores/) | LangChain vector store integrations list. |
| [Spring AI Vector Stores](https://docs.spring.io/spring-ai/reference/api/vectordbs.html) | Spring AI vector DB abstractions for Java. |
| [BERTopic](https://maartengr.github.io/BERTopic/) | Topic modeling with embeddings — useful for corpus exploration before RAG. |
| [Embeddings Benchmark (MTEB)](https://huggingface.co/spaces/mteb/leaderboard) | MTEB leaderboard for embedding and rerank models. |
| [BEIR](https://github.com/beir-cellar/beir) | BEIR heterogeneous retrieval benchmark. |
| [MS MARCO](https://microsoft.github.io/msmarco/) | MS MARCO passage ranking dataset — foundation for many retrievers. |
| [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Google Natural Questions benchmark for open-domain QA. |
| [HotpotQA](https://hotpotqa.github.io/) | Multi-hop QA requiring retrieval over multiple docs. |
| [CoQA](https://stanfordnlp.github.io/coqa/) | Conversational QA dataset for retrieval+conversation. |
| [SQuAD 2.0](https://rajpurkar.github.io/SQuAD-explorer/) | SQuAD 2.0 reading comprehension with unanswerable questions. |
| [TREC RAG Track](https://trec.nist.gov/data/t14_rag.html) | TREC RAG evaluation track for retrieval quality. |
| [Cohere Rerank](https://docs.cohere.com/docs/rerank) | Cohere Rerank 3.5 for improving retrieval precision. |
| [Voyage Rerank](https://docs.voyageai.com/docs/reranker) | Voyage rerankers optimized for RAG. |
| [FlagEmbedding Reranker](https://github.com/FlagOpen/FlagEmbedding/tree/master/FlagEmbedding/reranker) | BGE reranker for cross-encoder reranking. |
| [ColBERTv2](https://github.com/stanford-futuredata/ColBERT) | Late-interaction retrieval with ColBERTv2 — fine-grained token search. |
| [SPLADE](https://github.com/naver/splade) | Sparse learned retrieval via SPLADE — neural sparse vectors. |
| [BM25S](https://github.com/xhluca/bm25s) | Fast BM25 with numba — strong baseline for hybrid retrieval. |
| [Rank-BM25](https://github.com/dorianbrown/rank_bm25) | Simple Python BM25 for hybrid RAG prototypes. |
| [Pyserini](https://github.com/castorini/pyserini) | Reproducible IR toolkit with BM25, dense, and hybrid retrieval. |
| [Haystack Retrievers](https://docs.haystack.deepset.ai/docs/retriever) | Haystack retrievers: BM25, embedding, and hybrid. |
| [R2R (SciPhi)](https://r2r-docs.sciphi.ai/) | SciPhi R2R: open-source RAG ingestion, retrieval, and analytics. |
| [Verba (Weaviate)](https://github.com/weaviate/Verba) | Weaviate Verba RAG app: ingest, retrieve, chat. |
| [Khoj](https://khoj.dev/docs/) | Khoj: self-hosted personal AI with semantic search over notes. |
| [Mem0 Vector (long-term)](https://docs.mem0.ai/platform/quickstart) | Mem0 platform docs for long-term memory API. |
| [Letta Cloud](https://docs.letta.com/guides/agents) | Letta agent platform with stateful memory. |
| [Cognee Knowledge Graph](https://docs.cognee.ai/) | Cognee docs for graph memory pipeline. |
| [LangMem](https://langchain-ai.github.io/langmem/) | LangMem docs for LangGraph memory extraction. |
| [LlamaIndex Memory](https://docs.llamaindex.ai/en/stable/module_guides/agent/memory/) | LlamaIndex memory primitives for agents. |
| [RedisVL](https://docs.redisvl.com/en/latest/) | RedisVL: Python client for Redis vector search with LLM patterns. |
| [pgai (Timescale)](https://github.com/timescale/pgai) | pgai: bring AI workflows inside Postgres with pgvector. |
| [Supabase pgvector guide](https://supabase.com/docs/guides/ai/semantic-search) | Supabase semantic search tutorial end-to-end. |
| [Cloudflare Vectorize](https://developers.cloudflare.com/vectorize/) | Cloudflare Vectorize: edge vector DB with Workers AI. |
| [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) | Azure AI Search with vector, semantic ranker, and hybrid. |
| [AWS OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html) | OpenSearch Serverless with vector engine. |
| [A Survey on Retrieval-Augmented Generation](https://arxiv.org/abs/2312.10997) | Comprehensive RAG survey: retrievers, generators, and evaluation — guide for vector DB selection. |
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG)](https://arxiv.org/abs/2005.11401) | Original RAG paper: retrieve-and-generate architecture for knowledge-intensive tasks. |
| [Dense Passage Retrieval for Open-Domain QA (DPR)](https://arxiv.org/abs/2004.04906) | DPR: dense retriever training for QA — foundation for modern embedding models. |
| [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction](https://arxiv.org/abs/2004.12832) | ColBERT: late interaction for fine-grained token-level retrieval quality. |
| [SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking](https://arxiv.org/abs/2107.05720) | SPLADE: learned sparse retrieval combining BM25 sparsity with neural expansion. |
| [GraphRAG: Graph-based Retrieval-Augmented Generation](https://arxiv.org/abs/2404.16130) | GraphRAG paper: building knowledge graphs for global, theme-level questions naive RAG misses. |
