---
title: "Private LLM Platform for Company-wide Coding Assistant"
excerpt: "LLM Infrastructure · MLOps · Observability<br/><img src='/images/private_llm_platform.svg' style='max-width:400px;'>"
collection: portfolio
---

**Tags:** LLM Infrastructure · MLOps · Observability

A self-hosted, GPU-served coding assistant for a ~20-developer team, with full access control, usage analytics, and observability — running entirely on-premise. A 4-bit quantized 30B-parameter coding model is served on a single CUDA GPU via **llama.cpp** behind an OpenAI-compatible API.

All traffic flows through a **LiteLLM** gateway that authenticates users, enforces per-user keys, rate limits and budgets, and tracks spend, so every call is attributable to a person. Every prompt and response is captured in **Langfuse** for self-hosted usage analytics and topic modelling. A **Prometheus + Grafana + Loki** stack tracks throughput, queue depth, KV-cache pressure, and GPU/host health, with centralised searchable logs across every container. The raw model port and databases are bound to localhost only, leaving the keyed gateway as the single open surface — nothing leaves the infrastructure. The whole platform is reproducible as two Docker Compose stacks.

[Project report](/files/local-llm-project-report.html)
