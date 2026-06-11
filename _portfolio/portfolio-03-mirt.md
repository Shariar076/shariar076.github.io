---
title: "Mapping LLM Ideology with Multidimensional IRT"
excerpt: "Psychometrics · LLM Evaluation · Bayesian Modeling<br/><img src='/images/mirt_dwnominate.png' style='max-width:400px;'>"
collection: portfolio
---

**Tags:** Psychometrics · LLM Evaluation · Bayesian Modeling

A Bayesian multidimensional Item Response Theory (IRT) model, implemented in Stan, that places large language models in a latent ideological space — estimating each model's position (ability θ) alongside item discrimination (α) and difficulty (β). Validated against DW-NOMINATE, the standard human benchmark for political ideology, the model reaches **0.98 correlation** on the primary dimension.

A methodological finding: an improper uniform prior on the discrimination correlations recovers the latent structure far better than structured priors (≈56% correlation, versus ≈40% for an LKJ(0.1) prior and ≈10% for independent parameters), letting the likelihood determine the correlation structure without Bayesian shrinkage.

[Validation report (PDF)](https://github.com/Shariar076/llm-ideological-depth/blob/main/MIRT_Val_Report.pdf) · [Model report](https://github.com/Shariar076/llm-ideological-depth/blob/main/MIRT_Report.md) · [Code on GitHub](https://github.com/Shariar076/llm-ideological-depth)

This is the psychometric backbone of our paper *When Models Refuse* ([arXiv:2508.21448](https://arxiv.org/abs/2508.21448)).
