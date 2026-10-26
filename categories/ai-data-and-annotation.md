# AI data and annotation

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Added 2026-10-23 in AI expansion round 2. Primary-source pointers; every entry link-checked at entry (all reachable). Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Label Studio](https://labelstud.io/guide/) | Multi-type data labeling platform (text, image, audio) for training and evaluation datasets; open-source core with a hosted tier. |
| [Argilla](https://docs.argilla.io/) | Data curation and human-feedback platform for LLM datasets (now part of Hugging Face); pairs with Distilabel. |
| [Distilabel (Argilla)](https://distilabel.argilla.io/) | Framework for synthetic data generation and AI feedback pipelines for fine-tuning and evaluation. |

## AI expansion round 3 additions — 2026-10-23

| Resource | Useful for / constraints |
|---|---|
| [NeMo Curator](https://github.com/NVIDIA-NeMo/Curator) | GPU-accelerated data curation for LLM training: filtering, deduplication, and quality scoring at scale. |
| [DataTrove (Hugging Face)](https://github.com/huggingface/datatrove) | HF's library for large-scale text data processing — how datasets like FineWeb were built. |
| [Dolma (AI2)](https://huggingface.co/datasets/allenai/dolma) | AI2's 3T-token open pretraining corpus with its curation toolkit and documentation. |

## 2026-10-26 expansion — 1000 AI resources (includes skills.sh directory)

| Resource | Useful for / constraints |
|---|---|
| [Scale AI Platform](https://docs.scale.com/docs) | Scale AI for data labeling, RLHF, and model evaluation at scale. |
| [Labelbox](https://docs.labelbox.com/docs) | Labelbox platform for data labeling and model-assisted annotation. |
| [Label Studio](https://labelstud.io/guide/get_started) | Open-source Label Studio for flexible annotation with ML-assisted workflows. |
| [Argilla](https://argilla.io/docs/practical-guides/practical-guides) | Argilla for human-in-the-loop feedback and dataset curation. |
| [Prodigy (Explosion)](https://prodi.gy/docs) | Prodigy annotation tool with active learning for NLP. |
| [Doccano](https://github.com/doccano/doccano) | Open-source Doccano for text annotation. |
| [CVAT](https://docs.cvat.ai/docs/enterprise/) | CVAT for image/video annotation — self-hosted. |
| [Roboflow](https://docs.roboflow.com/) | Roboflow for dataset management and computer vision annotation. |
| [Hugging Face AutoTrain](https://huggingface.co/docs/autotrain/index) | AutoTrain for no-code fine-tuning on your data. |
| [Snorkel AI](https://docs.snorkel.ai/) | Snorkel programmatic labeling with labeling functions. |
| [Cleanlab Studio](https://cleanlab.ai/blog/cleanlab-studio) | Cleanlab Studio for finding and fixing label errors. |
| [Great Expectations](https://docs.greatexpectations.io/docs/core/introduction/) | GE for data validation in ML pipelines. |
| [WhyLogs (WhyLabs)](https://whylabs.github.io/whylogs/) | WhyLogs for data logging and drift detection. |
| [Evidently AI Data Drift](https://docs.evidentlyai.com/user-guide/monitoring/data_drift) | Evidently for data drift and data quality. |
| [Monte Carlo](https://docs.getmontecarlo.com/docs) | Monte Carlo data observability for pipeline reliability. |
| [dbt](https://docs.getdbt.com/docs/introduction) | dbt for transforming data in warehouse for ML features. |
| [Airbyte](https://docs.airbyte.com/) | Airbyte for ELT connectors to feed RAG and training data. |
| [Fivetran](https://fivetran.com/docs) | Fivetran managed connectors for data ingestion. |
| [Dagster Assets](https://docs.dagster.io/concepts/assets/software-defined-assets) | Dagster software-defined assets for data pipelines. |
| [Prefect Dataflows](https://docs.prefect.io/latest/concepts/flows/) | Prefect flows for data ingestion for LLMs. |
| [Hugging Face Datasets Server](https://huggingface.co/docs/datasets-server) | Datasets Server for previewing 10k datasets. |
| [Kaggle Datasets](https://www.kaggle.com/docs/datasets) | Kaggle datasets hub for training and eval data. |
| [Anthropic HH-RLHF](https://github.com/anthropics/hh-rlhf) | Anthropic HH-RLHF dataset for helpful/harmless training. |
| [UltraFeedback](https://github.com/OpenBMB/UltraFeedback) | UltraFeedback for RLHF preference data. |
| [ShareGPT](https://sharegpt.com/) | ShareGPT dataset (check license) for instruction tuning. |
| [OpenOrca](https://huggingface.co/datasets/Open-Orca/OpenOrca) | OpenOrca dataset for instruction fine-tuning. |
| [Dolly 15k](https://github.com/databrickslabs/dolly) | Databricks Dolly 15k open instruction dataset. |
| [Alpaca Dataset](https://github.com/tatsu-lab/stanford_alpaca) | Stanford Alpaca 52k instruction dataset. |
| [Self-Instruct](https://github.com/yizhongw/self-instruct) | Self-Instruct paper code for generating instruction data. |
| [Label Studio Documentation (Heartex)](https://labelstud.io/guide#fallback-61) | Label Studio docs: RLHF and eval annotation workflows — flexible open-source labeling. |
| [Argilla: Iterative Approach for Building Datasets](https://github.com/argilla-io/argilla) | Argilla repo: human-in-the-loop dataset curation for eval and RLHF. |
| [DVC: Data Version Control for ML](https://dvc.org/doc#fallback-63) | DVC docs: Git for data and models — versioning for training pipelines. |
| [Hugging Face Datasets: A Community Library](https://arxiv.org/abs/2109.02846) | Datasets paper: 10k datasets library with Arrow and streaming — standard for data ingestion. |
| [Cleaning Data with Cleanlab](https://github.com/cleanlab/cleanlab) | Cleanlab repo: find label errors in datasets for eval cleaning. |
