---
title: "Can Attribution Graphs Predict Model Behavior? A Case Study Using Misreporting Tool Calls"
date: 2026-08-29
permalink: /posts/2026/08/circuits-gradients-and-tool-trust/
excerpt: "Scaling mechanistic interpretability to a real safety task: when a model must decide whether to trust a wrong tool response, attribution graphs read by a circuit oracle reach 67% accuracy, while a single backward pass at the correct-tool prompt reaches 85%."
read_time: false
tags:
  - interpretability
  - AI safety
  - attribution graphs
  - SPAR
---

*This work was produced as part of the SPAR Program - Spring 2026 Cohort, with support from Sriram Balasubramanian.*

**TL;DR:** Can [attribution graphs](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) predict a safety-relevant model behavior *before it occurs*? We redesign and scale up the [misreported-tool-calls](https://transformer-circuits.pub/2026/nla/#misreported-tool-calls) task from Anthropic's NLA paper, where a model must decide whether to follow a wrong tool response. We extracted ~300 attribution graphs using prompts with tool calls and analyzed whether they can reveal or distinguish between a model's blind trust in tool output vs. its independent internal calculation. We ran them through our [circuit oracle](https://openreview.net/forum?id=ANY6YrYUZE): An agentic pipeline that automates the analysis of attribution graphs and builds a pruned subgraph explaining the behavior. We found that the oracle is basically at chance (50%) on raw attribution graphs. The same oracle reaches 80% when we change the attribution target from the output logit to a *custom*  *probe direction*, where the probe is a linear classifier trained to predict which digit the model is about to emit from its residual stream. Furthermore, a single backward pass at the correct-tool prompt reaches 85% without graphs at all. Here is why, and what it implies.

Introduction
------------

Mechanistic interpretability has produced compelling case studies: induction heads, gender bias circuits, spurious features in probes. But these have mostly been post-hoc analyses of known behaviors on controlled inputs. A harder question is whether the tools can drive safety-relevant *predictions*: given a model and a class of inputs, can we use circuits to anticipate which cases will go wrong before they do?

A concrete instance from our prior work on secret elicitation: a model fine-tuned to know a secret word but must not reveal it. A naive ranking of features by their influence on the visible output recovers the correct secret in only ~33% of cases. The secret-bearing features are present in the graph but buried under chat-template and formatting features that have stronger influence scores on the current output. Even after re-ranking by cross-graph difference against a base model's graph with no secret knowledge, accuracy only lifts up to ~68%. This technique should cancel template scaffold features shared with the base and surface what the taboo LoRA drives specifically, but the relevant suppressed features remain difficult to isolate from other differentially-active ones. This shows that the circuits can explain what the model already did; it does not automatically surface what the model did not say or chose to hide.

Anthropic's 2026 NLA paper proposed a concrete testbed for exactly this in the [misreported tool calls](https://transformer-circuits.pub/2026/nla/#misreported-tool-calls) task, grounded in a real observed failure of Claude Opus, where Opus 4.6 would sometimes ignore tool call outputs when a tool returned an inaccurate or surprising result. In the experiment, the target model is shown a tool response containing a wrong answer. In some cases it parrots the tool; in others it ignores it and recovers its own correct answer.

We identified this as a promising case study for interpretability precisely because the mechanism should, in principle, be visible in the circuit: either the tool value is being read and propagated to the output, or it is not. We frame this as a *prediction* task: *can circuits built on normal, correct tool responses identify which cases will parrot a wrong tool response before one is ever shown?* We operationalise it at scale and evaluate whether attribution graphs actually deliver on that promise.

Designing the Testbed
---------------------

To give the interpretability tools a clean signal to read, we stripped the task down to its minimal form. The model is asked a simple arithmetic question, calls an `execute_code` tool, and receives a wrong answer. The only question is what the model does next.

<iframe src="/assets/widgets/mHLR4TifG9dzSAGKJ.html" class="lw-widget" loading="lazy" scrolling="no" style="width:100%;border:0;height:400px" onload="var d=this.contentDocument;this.style.height=(d.documentElement.scrollHeight+4)+'px'"></iframe>

Prompt structure is identical across all cases; only the tool's returned digit changes. There is no multi-step reasoning, no ambiguous entities, no retrieval. The decision collapses to one token. This, we think, is the closest thing to a controlled experiment available in the language model setting.

We generated 480 arithmetic cases (subtraction and addition), tested each case across every wrong-digit variant, and retained the **292 that were fully consistent**: always-parrot cases where the model parrots every tested wrong digit, and always-recover cases where it ignores the tool regardless. *Mixed cases*, where behavior depends on *which* wrong digit was provided, were excluded.

<iframe src="/assets/widgets/NyDEnzmfhTZcG6o7D.html" class="lw-widget" loading="lazy" scrolling="no" style="width:100%;border:0;height:400px" onload="var d=this.contentDocument;this.style.height=(d.documentElement.scrollHeight+4)+'px'"></iframe>

Experiment 1: Circuit Oracle on Raw Attribution Graphs
------------------------------------------------------

Note that the attribution graphs are built on the *correct-tool* prompt, the version where the tool reports the right answer. This is the *predictive* setting: we want to identify which cases are vulnerable to a wrong tool response *before* it has occurred. A graph built on the wrong-tool prompt would already reveal the outcome in the output token; our goal here is to distinguish parrot from recover cases before the failure happens, i.e., while the tool is still telling the truth.

We built attribution graphs for each case using `Gemma-3-4b-it` with `262k-wide transcoders` from [Gemma Scope 2](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/), then ran our [**Circuit Oracle**](https://openreview.net/forum?id=ANY6YrYUZE), which provides a multi-agent LLM pipeline that navigates the graph. We designed a custom tool called `get_source_influence` that measures the signed influence flowing from the tool-response token to the output logit. The oracle then inspects feature autointerp labels on Neuronpedia and emits a verdict. To prevent confirmation bias, the oracle is kept blind to the behavior: the output token is masked to `·` before it sees the graph, so it cannot read the answer and must derive the mechanism from the circuit alone.

<iframe src="/assets/widgets/ubrnSru9kSDzikv4C.html" class="lw-widget" loading="lazy" scrolling="no" style="width:100%;border:0;height:400px" onload="var d=this.contentDocument;this.style.height=(d.documentElement.scrollHeight+4)+'px'"></iframe>

This result fits a broader concern regarding **the usefulness of mech interp tools for real-world applications**. A similar recent evaluation of interpretability tools by [Karvonen et al.](https://www.lesswrong.com/posts/ExB6KYDcznaFS72eT) found that activation-reading tools, including autoencoders and activation oracles, provided *"no uplift"* over agents that saw only chat transcripts when predicting whether prompt edits would change model behavior. The interpretability tools described *what* the model computed, but not *whether* that computation was causally downstream of the input feature under test. We see the same failure mode here.

In our experiment, the attribution graphs are built on the *correct-tool* prompt, i.e., the tool is telling the truth, so both parrot and recover cases produce the correct output digit. In this setting, the digit-detector feature fires on the tool-response token in both groups, because the tool value happens to be right and the model reads it. The oracle correctly identifies "tool signal flows to output" and calls COPIED in nearly every case, which is mechanistically accurate for this prompt. But **it cannot distinguish the groups**: parrot cases copy the tool *irrespective of whether it is right*; recover cases output the same digit from an independent internal computation. Simply said, the static graph cannot answer: "Would this route persist if the tool's digit were wrong?"

The oracle is asking *what ran?* When the safety-relevant question is *what would run if the tool changed?*

We verified this directly. On *wrong-tool* graphs, where the outcome is no longer counterfactual, a simple tool that calculates a signed tool-to-output influence score separates parrot from recover cases perfectly (18/18). The same oracle reading those graphs achieves only 11/18, because it was guided to inspect feature dominance rather than directional influence.

Experiment 2: Using Sensitivity at the Correct-Tool Prompt
----------------------------------------------------------

The parrot/recover distinction is fundamentally a **sensitivity** question where we ask: if the tool value changes, does the output change? So far, attribution graphs were only able to explain what was already visible. However, we are interested in the underlying mechanism that can tell us whether the model is relying more on the tool-call or its own calculation for its output, irrespective of what the tool-call output is. We hypothesize, there should be a certain state when the model changes into either relying on it's own calculation vs. mimicking what the tool says. To surface this, we changed the input embedding gradually from correct to wrong tool-output token using **linear interpolation** and try to identify if there is a consistent behaviour guiding this and if we can separate it.

We formalise this by parameterising the tool-response token with a scalar α. At α = 0, the tool reports the correct answer; at α = 1, it reports a wrong one. We implement the interpolation at the embedding level for the single correct/wrong token:

<iframe src="/assets/widgets/fYPkSjyAREh8sizLh.html" class="lw-widget" loading="lazy" scrolling="no" style="width:100%;border:0;height:400px" onload="var d=this.contentDocument;this.style.height=(d.documentElement.scrollHeight+4)+'px'"></iframe>

<iframe src="/assets/widgets/cTybEtRjM9DsWZQgE.html" class="lw-widget" loading="lazy" scrolling="no" style="width:100%;border:0;height:400px" onload="var d=this.contentDocument;this.style.height=(d.documentElement.scrollHeight+4)+'px'"></iframe>

The idea here is that, at α = 0, the tool is correct, so all cases output the correct answer. But the groups must differ in how *quickly* diff(α) falls as α increases. A parrot case's logit difference crosses zero at some flip-alpha; a recover case's stays positive all the way to α = 1. We noticed that the change happens suddenly and the output logit diff over the interpolation shows a softmax curve, as illustrated below.

<iframe src="/assets/widgets/Xg74bp4vi3TkJDBbd.html" class="lw-widget" loading="lazy" scrolling="no" style="width:100%;border:0;height:400px" onload="var d=this.contentDocument;this.style.height=(d.documentElement.scrollHeight+4)+'px'"></iframe>

In practice, the predictor uses only a single quantity: the gradient of diff at α = 0, available from one backward pass. Our key observation here was  that the **local slope** of diff at α = 0, which was computed by a single backward pass through the original model, already encodes which group a case belongs to. This is a directional derivative: how sensitive is the model's output to a perturbation of the tool embedding, measured at the correct-tool end? Parrot cases are sensitive; recover cases are not.

<iframe src="/assets/widgets/jkXhfuRoG55FFjuCL.html" class="lw-widget" loading="lazy" scrolling="no" style="width:100%;border:0;height:400px" onload="var d=this.contentDocument;this.style.height=(d.documentElement.scrollHeight+4)+'px'"></iframe>

We evaluate the Taylor predictor on the full 292-case set, grid-searching the threshold. We compare three variants: the original HF model, the replacement model (with per-layer transcoders), and the replacement model with attention patterns and LayerNorm scales *frozen* at α = 0, i.e., the frozen curve is the circuit's own linear prediction of how the output responds to the tool changing. The "replacement model" here is Gemma-3-4b-it with each of its 42 MLP layers swapped for the corresponding sparse transcoder dictionary, so a forward pass through it is equivalent to running the circuit.

| Method | Threshold | Accuracy | n correct | FP  | FN  |
| --- | --- | --- | --- | --- | --- |
| *Baseline: always predict recovery (majority class)* | *—* | *55.5%* | *162 / 292* | *—* | *—* |
| α = 0 logit diff alone | any | 55.5% | 162 / 292 | 0   | 130 |
| Frozen circuit (replacement model) | 2   | 76.7% | 224 / 292 | 23  | 45  |
| Taylor over replacement model | 10  | 79.1% | 231 / 292 | 56  | 5   |
| **Taylor over original model** | **10** | **85.3% (best)** | **249 / 292** | **12** | **31** |

Several things are worth noting. The α = 0 logit diff *alone* is useless; it sits at majority-class accuracy regardless of threshold, because both groups output the correct digit at α = 0 by construction. The value does not separate them; the *slope* does. This rules out any explanation where the α = 0 representation directly encodes parrot/recover; what's encoded is sensitivity.

The frozen circuit (77%) outperforms the oracle reading that same circuit (50% from Experiment 1), which is telling: the circuit's *own linear response* to an embedding perturbation predicts better than a sophisticated LLM agent trying to interpret its structure. The agent is looking at the right object but asking the wrong question.

The gap between frozen circuit (77%) and original Taylor (85%) reflects transcoder approximation error: replacing 42 MLP layers with sparse dictionaries introduces small mismatches that compound into an 8-point accuracy gap. The circuit is a good approximation, but not perfect.

<iframe src="/assets/widgets/egXq3zzM6TqNc7dQF.html" class="lw-widget" loading="lazy" scrolling="no" style="width:100%;border:0;height:400px" onload="var d=this.contentDocument;this.style.height=(d.documentElement.scrollHeight+4)+'px'"></iframe>

Experiment 3: Oracle Succeeds with Probe-Weighted Circuits
----------------------------------------------------------

Experiments 1 and 2 share a diagnosis: the oracle fails because the attribution target conflates two competing mechanisms at the same operating point. Both parrot and recover cases read the tool value and propagate it; thus, the circuit shows the same story. If we can attribute toward a named residual-stream direction - one for the wrong-digit route, one for the correct-digit route - the oracle receives a single-direction question instead of "who wins?"

To isolate those directions, we train a 10-class linear probe, i.e., `nn.Linear(d_model, 10)` on layer-26 residual-stream activations at the commit-token position. Training examples are drawn from parrot cases (labeled with the wrong digit the model emits), recover cases (labeled with the correct-answer digit), and correct-tool cases (labeled with the correct digit). The probe learns to predict which digit the model is about to output from the residual stream at that layer. This gives us a weight matrix W where each row W[d] is a direction in residual space that points toward "about to emit digit d". W[wrong\_digit] is the direction associated with parroting the tool; W[correct\_digit] is the direction associated with the correct answer.

For each test case, on the same correct-tool prompt used in Experiment 1, we extract two attribution circuits:

*   **Parrot circuit**: attributed toward W[wrong_digit\]: what features drive the wrong-digit direction at layer 26?
*   **Recover circuit**: attributed toward W[correct_digit\]: what features drive the correct-digit direction?

The oracle now receives a circuit with a single named direction. It no longer needs to infer which of two pathways "won"; it can describe what is mechanistically present in that direction alone.

<iframe src="/assets/widgets/3fyFXyc5mZ8KvLGJS.html" class="lw-widget" loading="lazy" scrolling="no" style="width:100%;border:0;height:400px" onload="var d=this.contentDocument;this.style.height=(d.documentElement.scrollHeight+4)+'px'"></iframe>

<iframe src="/assets/widgets/g3sMwsysQ5rYGjhMs.html" class="lw-widget" loading="lazy" scrolling="no" style="width:100%;border:0;height:400px" onload="var d=this.contentDocument;this.style.height=(d.documentElement.scrollHeight+4)+'px'"></iframe>

The 30-point improvement from Experiment 1 to Experiment 3 involves no change to the oracle and no change to the model, only a change to what the circuit is attributed toward. This confirms attribution graphs as a capable tool for safety-relevant classification when the question is formulated to isolate a single mechanism.

Discussion
----------

In this work, we evaluated whether attribution graphs built to explain LLM behaviors can reliably predict a safety-relevant outcome: whether a model will blindly follow a response or recover with a correct answer. The three experiments form a single diagnostic arc. Experiment 1 shows the oracle at chance when given the raw attribution graph where the attribution target is ambiguous: on the correct-tool prompt, both parrot and recover cases look identical, and the static circuit cannot answer a counterfactual. Experiment 2 shows that the counterfactual question is answerable at 85% with one backward pass: the information is in the model, just not in the circuit's structure. Experiment 3 shows the oracle recovering to 80% when circuits are attributed toward isolated probe directions: 50% (Experiment 1) → 80% (Experiment 3) → 85% (Experiment 2, Taylor).

The lesson is not that attribution graphs are unreliable. The same oracle that fails at 50% reaches 80% on a well-posed attribution task. The same model that is unreadable from static structure is 85% predictable from its local gradient. The tool works; question formulation determines whether the answer is accessible. The [Karvonen et al.](https://www.lesswrong.com/posts/ExB6KYDcznaFS72eT) finding that interpretability tools provide no uplift over chat transcripts for counterfactual prediction applies when the attribution target and evaluation point are chosen without regard for the counterfactual structure of the task. When they are chosen carefully, the gap reopens.

The Taylor approach works here because we constructed a meaningful perturbation direction interpolating between the correct and wrong tool embeddings, and measured sensitivity along it. This required knowing *what* to perturb, which came from understanding the task structure. In settings where the relevant perturbation direction is not known in advance, the approach would need to be adapted.

A natural next step is to combine all three: use probe-weighted circuits to identify which features and positions are most relevant to a behavior, then apply targeted perturbations along those directions to test causal claims. The graph provides the vocabulary; the gradient provides the test; the probe provides the direction.

Conclusion
----------

Attribution graphs describe what a model computed on one input. They do not, by themselves, describe what the model would compute if an input changed. For safety-relevant prediction, that counterfactual is usually the question that matters. When we ask the counterfactual directly via a Taylor approximation, accuracy goes from 50% to 85% in one backward pass. When we reformulate the attribution target with learned probe directions, the circuit oracle climbs from 50% to 80%. The tools are capable; the question formulation is the bottleneck.

Acknowledgments
---------------

This work was produced as part of the [Supervised Program for Alignment Research (SPAR)](https://sparai.org/) \- Spring 2026 Cohort. We thank Sriram Balasubramanian for mentoring this project.

### Navigation

*   [Front page](https://www.lesswrong.com/api/home)
*   [Markdown API documentation](https://www.lesswrong.com/api/SKILL.md)