---
title: "When Models Refuse: Political Steerability and Feature Richness as Measures of Ideological Depth"
collection: publications
category: preprints
permalink: /publication/2025-08-29-ideological-depth
excerpt: 'Defines ideological depth as a model''s steerability and the feature richness of its internal political representations measured with sparse autoencoders.'
date: 2025-08-29
venue: 'arXiv preprint arXiv:2508.21448'
paperurl: 'https://arxiv.org/pdf/2508.21448'
citation: 'Shariar Kabir, Kevin Esterling, Yue Dong. (2025). &quot;When Models Refuse: Political Steerability and Feature Richness as Measures of Ideological Depth.&quot; <i>arXiv preprint arXiv:2508.21448</i>.'
---

Authors: **Shariar Kabir**, [Kevin Esterling](https://profiles.ucr.edu/app/home/profile/kevine), [Yue Dong](https://yuedong.us/)

Large language models (LLMs) sometimes refuse to follow benign instructions, such as declining to argue a political position or adopt a stated persona, and such refusals are commonly read as safety guardrails at work. We ask whether they can instead signal a **capability deficit**: a shortage of the internal representations a model needs to reason from the instructed perspective. To investigate, we introduce **ideological depth**, a property with two components: (i) a model's ability to follow political instructions without *failure* (steerability), and (ii) the **feature richness** of its internal political representations, measured with sparse autoencoders (SAEs). Using two widely used openweight LLMs as candidates, we compare interventions based on prompts and activation-steering, and probe political features with publicly available SAEs. We find large, systematic differences: a model that is more steerable in both ideological directions activates **~7.3x** more distinct political features, while the other model instead responds with increased refusals. Causally ablating a small, targeted set of political features from the former model reproduces the same feature-poor behavior and drives up refusals. Together, these results indicate that refusals on benign prompts can arise from **capability deficits** rather than fixed safety rules, and that ideological depth is a measurable property of LLMs that helps predict when a model will refuse.

[[PDF]](https://arxiv.org/pdf/2508.21448) &nbsp; [[arXiv]](https://arxiv.org/abs/2508.21448)
