---
title: "Beyond the Surface: Probing the Ideological Depth of Large Language Models"
collection: publications
category: preprints
permalink: /publication/2025-08-29-ideological-depth
excerpt: 'Defines ideological depth as a model''s steerability and the feature richness of its internal political representations measured with sparse autoencoders.'
date: 2025-08-29
venue: 'arXiv preprint arXiv:2508.21448'
paperurl: 'https://arxiv.org/pdf/2508.21448'
citation: 'Shariar Kabir, Kevin Esterling, Yue Dong. (2025). &quot;Beyond the Surface: Probing the Ideological Depth of Large Language Models.&quot; <i>arXiv preprint arXiv:2508.21448</i>.'
---

Authors: **Shariar Kabir**, [Kevin Esterling](https://profiles.ucr.edu/app/home/profile/kevine), [Yue Dong](https://yuedong.us/)

Large language models (LLMs) display recognizable political leanings, yet they vary significantly in their ability to represent a political orientation consistently. In this paper, we define ideological depth as (i) a model's ability to follow political instructions without failure (steerability), and (ii) the feature richness of its internal political representations measured with sparse autoencoders (SAEs), an unsupervised sparse dictionary learning (SDL) approach. Using Llama-3.1-8B-Instruct and Gemma-2-9B-IT as candidates, we compare prompt-based and activation-steering interventions and probe political features with publicly available SAEs. We find large, systematic differences: Gemma is more steerable in both directions and activates approximately 7.3x more distinct political features than Llama. Furthermore, causal ablations of a small targeted set of Gemma's political features to create a similar feature-poor setting induce consistent shifts in its behavior, with increased rates of refusals across topics. Together, these results indicate that refusals on benign political instructions or prompts can arise from capability deficits rather than safety guardrails. Ideological depth thus emerges as a measurable property of LLMs, and steerability serves as a window into their latent political architecture.

[[PDF]](https://arxiv.org/pdf/2508.21448) &nbsp; [[arXiv]](https://arxiv.org/abs/2508.21448)
