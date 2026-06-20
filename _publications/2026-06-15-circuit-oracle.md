---
title: "Circuit Oracle: Automating Attribution Graph Analysis via Natural-Language Queries"
collection: publications
category: conferences
permalink: /publication/2026-06-15-circuit-oracle
excerpt: 'A multi-agent system that automates mechanistic-interpretability analysis by autonomously answering natural-language questions about a model through multi-hop traversal of its attribution graph.'
date: 2026-06-15
venue: 'MechInterp & CompLearn Workshops @ ICML 2026'
citation: 'Hong Kiat Tan, Shariar Kabir, Swastik Agrawal, Sai Chereddy, Sriram Balasubramanian. (2026). &quot;Circuit Oracle: Automating Attribution Graph Analysis via Natural-Language Queries.&quot; <i>MechInterp &amp; CompLearn Workshops at ICML 2026</i>.'
---

Authors: Hong Kiat Tan\*, **Shariar Kabir**\*, Swastik Agrawal, Sai Chereddy, Sriram Balasubramanian &nbsp; <small>(\* equal contribution; ordered alphabetically by first name )</small>

Accepted at the **Mechanistic Interpretability (MechInterp)** and **Computational Learning (CompLearn)** workshops at **ICML 2026**.

Attribution graphs, an emerging tool in mechanistic interpretability, use transcoders to decompose language model computations into sparse interpretable features connected by causal edges. However, turning a graph into a safety-relevant insight requires hours of manual analysis by experts. We introduce **Circuit Oracle**, a multi-agent system that automates this analysis by autonomously answering natural-language questions about a target model (e.g., "Is this prediction driven by spurious features?") through multi-hop traversal of the attribution graph. We evaluate Circuit Oracle on three safety-relevant proxy tasks: detecting spurious features in probe circuits, eliciting hidden knowledge from taboo-finetuned models, and jailbreaking via causal interventions. On all three tasks, the oracle is comparable to or exceeds task-specific baselines that do not use the attribution graph. The circuit oracle requires no fine-tuning, as each task is specified by a modular *skill* (a natural-language prompt) paired with task-specific tools such as transcoder-feature steering, making the framework extensible by construction. Our results suggest that off-the-shelf agents reading attribution graphs through tool calls offer a practical, general-purpose route to automated mechanistic interpretability.

[[Paper]](https://drive.google.com/file/d/1U-XkHeH6XfvY2D8KiuqdTK15dsXoLqt3/view?usp=sharing)