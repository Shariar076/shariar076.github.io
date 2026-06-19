---
title: "Finetuning LLMs for Mental Health Counsel"
excerpt: "Healthcare AI · NLP<br/><img src='/images/mental_health_llm.png' style='max-width:400px;'>"
collection: portfolio
---

**Tags:** Healthcare AI · NLP

Recognizing the inherent bias of most LLMs towards European languages and ethnicities and the low resources of structured Bengali data, I focused on refining open-source models like **LLaMA** using different [parameter-efficient fine-tuning (PEFT)](https://huggingface.co/docs/peft/en/index#peft) techniques (e.g., Adapter injections and LoRA). I successfully fine-tuned LLaMA for Bengali mental health consultation using **QLoRA**, resulting in a more optimized model that can be served on low GPU memory—ensuring equitable access to healthcare technologies across diverse linguistic communities.

[Live demo on Hugging Face](https://huggingface.co/spaces/MedAiHealth/mental-health-bengali-llm-chabot)
