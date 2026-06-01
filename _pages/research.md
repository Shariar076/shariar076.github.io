---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

I treat mechanistic interpretability as a practical tool for AI safety building methods that scale beyond toy settings and validating them on real model behaviors. I am especially interested in using LLM agents to automate interpretability (autointerp), turning circuit analysis from manual, single-prompt inspection into a scalable process. My work is organized around three intertwined directions.

Agents for Autointerp
======
Building agentic pipelines that discover, label, and validate circuits and features at scale, so interpretability keeps pace with model capability instead of lagging on isolated examples. Circuits are information-dense and inherently prompt-specific, making large-scale behavioral analysis laborious: while tools like *[circuit tracer](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)* construct circuits for arbitrary prompts, raw circuits still require heavy human effort to cluster into interpretable supernodes, and understanding a model's behavior on a *task* demands dataset-level analysis that manual inspection cannot scale to.

* **<span style="color:#bd5d38;">[Ongoing · SPAR]</span>** [**Circuit Oracle: Automating Attribution Graph Analysis via Natural-Language Queries**](https://sparai.org), mentored by [Sriram Balasubramanian](https://sriramb-98.github.io/). We introduce **Circuit Oracle**, a multi-agent system that automates this analysis by autonomously answering natural-language questions about a target model (e.g., "Is this prediction driven by spurious features?") through multi-hop traversal of the attribution graph. In the long term, I aim to extend these methods to long-context interactions, enabling both explanation and control over extended chains of thought. [Report](https://drive.google.com/file/d/1U-XkHeH6XfvY2D8KiuqdTK15dsXoLqt3/view?usp=drive_link).

Interpretability for Safety
======
Locating and editing the causal mechanisms behind undesirable behavior — systematic bias in sensitive domains, unstable reasoning — moving toward targeted, mechanism-level interventions. Modern interpretability methods remain underexplored for socially complex behaviors such as moral and political reasoning; I seek to identify the parameters and circuits responsible for specific behavioral traits.

* [**When Models Refuse: Political Steerability and Feature Richness as Measures of Ideological Depth**](https://arxiv.org/abs/2508.21448). Shariar Kabir, Kevin Esterling, Yue Dong. *arXiv preprint, 2025.* Isolates the components responsible for behavioral differences through targeted ablation, defining *ideological depth* via steerability and the feature richness of internal political representations measured with sparse autoencoders.

Reliability under Real use
======
LLMs shift stance and tone under minor prompt changes; I design benchmarks to measure their stability and build interpretable methods to improve it in multi-turn settings. Working with [Prof. Yue Dong](https://yuedong.us/) and [Prof. Kevin Esterling](https://profiles.ucr.edu/app/home/profile/kevine), I study LLM behavior using social science methods and stress-test model opinions on sensitive downstream tasks such as long-form, multifaceted summarization, where models can behave inconsistently when their intrinsic knowledge conflicts with the extrinsic input.

* [**PReSS: A Black-Box Framework for Evaluating Political Stance Stability in LLMs via Argumentative Pressure**](https://arxiv.org/abs/2504.17052). Shariar Kabir, Kevin Esterling, Yue Dong. *PoliticalNLP @ LREC-COLING 2026.* Stress-tests LLMs' stated opinions with argumentative challenges, classifying them as stable or unstable across political topics, with implications for controlled generation and alignment.

Applied ML
======
Previously, I also worked on applied ML across NLP, computer vision, and cloud systems, often for low-resource and underrepresented settings. It was through these systems that I realized the "black box" nature of ML models where fine-tuning offered limited control and little insight into *why* a model behaved as it did, and how their behavior changed. This got me interested in interpretability and safety.

* [**Automatic Speech Recognition for Biomedical Data in Bengali Language**](https://arxiv.org/abs/2406.12931). Shariar Kabir, Nazmun Nahar, Shyamasree Saha, Mamunur Rashid. *arXiv preprint, 2024.* A 46-hour Bengali biomedical speech corpus for medical ASR covering Bengali and Sylheti dialects, achieving 8% WER on a symptom-focused vocabulary.
* [**SynthNID: Synthetic Data to Improve End-to-end Bangla Document Key Information Extraction**](https://aclanthology.org/2023.banglalp-1.13/). Syed Monsur\*, Shariar Kabir\*, Sakib Chowdhury\*. *BLP @ EMNLP 2023.* Generates domain-specific synthetic document images to fine-tune transformer models for underrepresented languages. (\* co-first author)

Cloud computing and Distributed systems
======
During my academic years in BUET and much of in my early career, I worked on extensively on cloud computing and distributed systems. My work in this area focused on resource management and optimization for cloud workloads, including serverless computing and container orchestration. I also explored the application of machine learning techniques to predict workload performance and optimize resource allocation in cloud environments.

* [**AgnoSVD: Dynamic Resource Allocation for Serverless Workloads using Collaborative Filtering**](https://www.sciencedirect.com/science/article/pii/S2590005625002899). Shariar Kabir, Muhammad Abdullah Adnan. *Array, 2026.* A collaborative filtering framework using SVD to predict optimal resource configurations for serverless workloads, evaluated on AWS Lambda and Apache OpenWhisk across 99 workloads.