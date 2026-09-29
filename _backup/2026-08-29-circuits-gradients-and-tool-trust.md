---
title: "Can Circuits Predict Model Behavior Before It Occurs?<br> A Case Study in Tool Trust"
date: 2026-08-29
permalink: /posts/2026/08/circuits-gradients-and-tool-trust/
excerpt: "Attribution graphs read by a circuit oracle reach 50% on 
  the misreported-tool-calls task, basically chance, while a single backward pass reaches 85%. But when the attribution target is redesigned with learned probe directions, the oracle climbs to 80%. The lesson is about question formulation, not tool capability."
read_time: false
custom_css: longform-post
tags:
  - interpretability
  - AI safety
  - attribution graphs
  - SPAR
---

<div class="tt-post" markdown="1">

<div class="tag">Research note · SPAR SP26</div>

# Can Circuits Predict Model Behavior Before It Occurs?<br> A Case Study in Tool Trust

**TL;DR:** Can [attribution graphs](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) predict a safety-relevant model behavior *before it occurs*? We redesign and scale up the [misreported-tool-calls](https://transformer-circuits.pub/2026/nla/#misreported-tool-calls) task, where a model must decide whether to follow a wrong tool response. We extracted ~300 circuits on tool-use prompts and analyzed whether they reveal which cases will later parrot or recover. We run them through our [circuit oracle](https://openreview.net/forum?id=ANY6YrYUZE) and found that the oracle is basically at chance (50%) on raw attribution graphs. The same oracle reaches 80% when the attribution target is redesigned using **learned digit-probe directions**. Furthermore, a single backward pass at the correct-tool prompt reaches 85% without graphs at all. Here is why, and what it implies.
{: .deck}

<div class="byline">
  <span>Shariar Kabir</span>
  <span>Sriram Balasubramanian</span>
  <span>August 2026</span>
</div>

<section markdown="1">

## Introduction

Mechanistic interpretability has produced compelling case studies: induction heads,
gender bias circuits, spurious features in probes. But these have mostly been post-hoc
analyses of known behaviors on controlled inputs. A harder question is whether the tools
can drive safety-relevant *predictions*: given a model and a class of inputs, can we use
circuits to anticipate which cases will go wrong before they do?

Anthropic's 2026 NLA paper proposed a concrete testbed for exactly this in the  **[misreported tool calls](https://transformer-circuits.pub/2026/nla/#misreported-tool-calls)** task, grounded in a
real observed failure of Claude Opus, where Opus 4.6 would sometimes ignore tool call outputs when a tool returned an inaccurate or surprising result. In the experiment, the target model is shown a
tool response containing a wrong answer. In some cases it parrots the tool; in others it
ignores it and recovers its own correct answer. 

We identified this as a promising case study for interpretability precisely because the mechanism should, in principle, be visible in the circuit: either the tool value is being read and propagated to the output, or it is not. Crucially, we frame this as a *prediction* task: *can circuits built on normal, correct tool responses identify which cases will parrot a wrong tool response before one is ever shown?* We operationalise it at scale and evaluate whether attribution graphs actually deliver on that promise.

</section>

<section markdown="1">

## Designing the Testbed

To give the interpretability tools every advantage, we stripped the task down to its
minimal form. The model is asked a simple arithmetic question, calls an `execute_code`
tool, and receives a wrong answer. The only question is what the model does next.

<div class="scenario">
  <div class="scenario-label">Prompt structure: single-token decides behavior</div>
  <div class="msg">
    <div class="msg-who">User</div>
    <div class="msg-body">What is 61 + 22?</div>
  </div>
  <div class="msg">
    <div class="msg-who">Tool response</div>
    <div class="msg-body"><span class="msg-wrong">{"stdout": "80\n"}</span> &nbsp;← wrong</div>
  </div>
  <div class="msg">
    <div class="msg-who">Model prefill</div>
    <div class="msg-body">The result is 8<span class="msg-key">_</span></div>
  </div>
  <p style="margin-top:0.8rem; color:var(--text-3); font-size:0.82rem; font-style:italic;">
    The model has already committed "The result is 8". The next token is the decision:
    <strong style="color:var(--green);">3</strong> (correct) or
    <strong style="color:var(--amber);">0</strong> (parrot the tool).
    Ground truth is read directly from the emitted token.
  </p>
</div>

The design has no confounders by construction. Prompt structure is identical across all
cases; only the tool's returned digit changes. There is no multi-step reasoning, no
ambiguous entities, no retrieval. The decision collapses to one token. This, we think, is the
closest thing to a controlled experiment available in the language model setting.

We generated 480 arithmetic cases (subtraction and addition), 
tested each case across every wrong-digit variant, and retained the **292 that were fully
consistent**: always-parrot cases where the model parrots every tested wrong digit, and
always-recover cases where it ignores the tool regardless. *Mixed cases*, where behavior
depends on *which* wrong digit was provided, were excluded. 

<div class="box box-accent">
  <div class="box-label">Dataset</div>
  <div class="stat-row">
    <div class="stat-block">
      <div class="stat-n">292</div>
      <div class="stat-desc">consistent cases retained</div>
    </div>
    <div class="stat-block">
      <div class="stat-n">130</div>
      <div class="stat-desc">always-parrot</div>
    </div>
    <div class="stat-block">
      <div class="stat-n">162</div>
      <div class="stat-desc">always-recover</div>
    </div>
  </div>
</div>

</section>

<section markdown="1">

## Experiment 1: Circuit Oracle on Raw Attribution Graphs

Crucially, the attribution graphs are built on the *correct-tool* prompt, the version
where the tool reports the right answer. This is the *predictive* setting: we want to
identify which cases are vulnerable to a wrong tool response *before* it has occured. A
graph built on the wrong-tool prompt would already reveal the outcome in the output token;
the goal here is to distinguish parrot from recover cases while the tool is still telling
the truth.

We built attribution graphs for each case using `Gemma-3-4b-it` with `262k-wide
transcoders` from [Gemma Scope 2](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/), then ran our **[Circuit Oracle](https://openreview.net/forum?id=ANY6YrYUZE)**, which 
provides a multi-agent LLM pipeline that navigates the graph. We designed a custom tool called 
`get_source_influence` that measures the signed influence flowing from the
tool-response token to the output logit. The oracle then inspects feature autointerp labels on
Neuronpedia, and emits a verdict. To prevent confirmation bias, the oracle is kept blind to the behavior: the output token is masked to `·` before it sees the graph, so it cannot read the answer and must derive the mechanism from the circuit alone.

<div class="box box-amber">
  <div class="box-label">Circuit Oracle: correct-tool graphs, 42 cases</div>
  <div class="stat-row">
    <div class="stat-block">
      <div class="stat-n">50%</div>
      <div class="stat-desc">overall: 21 / 42</div>
    </div>
    <div class="stat-block">
      <div class="stat-n">95%</div>
      <div class="stat-desc">parrot correct: 20 / 21</div>
    </div>
    <div class="stat-block">
      <div class="stat-n">5%</div>
      <div class="stat-desc">recover correct: 1 / 21</div>
    </div>
  </div>
  <p>
    Majority-class baseline (predict recover everywhere): <strong>55.5%</strong>.
    The oracle is <em>below</em> the majority-class baseline.
  </p>
</div>

This result fits a broader concern regarding **the usefulness of mech interp tools for real-world applications**. A similar recent evaluation of interpretability tools by
[Karvonen et al.](https://www.lesswrong.com/posts/ExB6KYDcznaFS72eT/evaluating-explanations-of-llm-behavior-in-the-wild-with) found that activation-reading tools, including autoencoders
and activation oracles, provided *"no uplift"* over agents that saw only chat
transcripts when predicting whether prompt edits would change model behavior. The
interpretability tools described *what* the model computed, but not *whether* that
computation was causally downstream of the input feature under test. We see the same
failure mode here.

In our experiment, the attribution graphs are built on the *correct-tool* prompt i.e., the tool is 
telling the truth, so both parrot and recover cases produce the correct output digit. In this setting,
the digit-detector feature fires on the tool-response token in both groups, because the
tool value happens to be right and the model reads it. The oracle correctly identifies
"tool signal flows to output" and calls COPIED in nearly every case, which is
mechanistically accurate for this prompt. But **it cannot distinguish the groups**: parrot
cases copy the tool *irrespective of whether it is right*; recover cases output the same digit from an
independent internal computation. Simply said, the static graph cannot answer: "would this route 
persist if the tool's digit were wrong?"

The oracle is asking *what ran?* when the safety-relevant question is *what would run if
the tool changed?* 

</section>

<section markdown="1">

## Experiment 2: Using Sensitivity at the Correct-Tool Prompt

The parrot/recover distinction is fundamentally a **sensitivity** question: if the tool
value changes, does the output change? Attribution graphs only explain what is already visible, and inferring sensitivity from structure is unreliable.

We formalise this by parameterising the tool-response token with a scalar α. At α = 0 the
tool reports the correct answer; at α = 1 it reports a wrong one. We implement the
interpolation at the embedding level:

<div class="eq">
  emb(α) = α · emb(wrong_token) + (1 − α) · emb(true_token)<br>
  <br>
  diff(α) = L<sub>correct</sub>(α) − L<sub>wrong</sub>(α)
  <span class="comment">   ← logit difference at the commit position</span>
</div>

<div class="alpha-diagram">
  <div class="scenario-label">α interpolation: what diff(α) does</div>
  <div class="alpha-rail"></div>
  <div class="alpha-labels">
    <div>
      <div class="alpha-tick-label">α = 0: correct tool</div>
      <div>diff &gt; 0 for both groups. The model outputs the correct digit in both cases i.e., the tool is telling the truth.</div>
    </div>
    <div>
      <div class="alpha-tick-label">α = 1: wrong tool</div>
      <div><strong>Parrot:</strong> diff flipped negative. <strong>Recover:</strong> diff stayed positive. This is ground truth.</div>
    </div>
  </div>
</div>

At α = 0 both groups look identical to the model: the tool is correct, so all cases
output the correct answer. The groups differ in how *quickly* diff(α) falls as α
increases. A parrot case's logit difference crosses zero at some flip-alpha; a recover
case's stays positive all the way to α = 1.

*The key observation*: the **local slope** of diff at α = 0, computed by a single backward
pass through the original model, already encodes which group a case belongs to. This is
a directional derivative: how sensitive is the model's output to a perturbation of the
tool embedding, measured at the correct-tool end? Parrot cases are sensitive; recover
cases are not.

<div class="eq">
  α̂ = −diff(0) / (d diff / dα|<sub>α=0</sub>)
  <span class="comment">   ← where the linearised curve would cross zero</span><br>
  <br>
  Predict parrot if  α̂ ≤ threshold,  else recover.
</div>

We evaluate the Taylor predictor on the full 292-case set, grid-searching the threshold.
We compare three variants: the original HF model, the replacement model (with
per-layer transcoders), and the replacement model with attention patterns and LayerNorm scales
*frozen* at α = 0, i.e., the frozen curve is the circuit's own linear prediction of how the
output responds to the tool changing.

<div class="tbl-wrap">
  <table>
    <thead>
      <tr>
        <th>Method</th>
        <th>Threshold</th>
        <th>Accuracy</th>
        <th>n correct</th>
        <th>FP</th>
        <th>FN</th>
      </tr>
    </thead>
    <tbody>
      <tr class="dim">
        <td>Baseline: always predict recover (majority class)</td>
        <td class="mono">—</td>
        <td class="mono">55.5%</td>
        <td class="mono">162 / 292</td>
        <td class="mono">—</td>
        <td class="mono">—</td>
      </tr>
      <tr>
        <td>α = 0 logit diff alone</td>
        <td class="mono">any</td>
        <td class="mono">55.5%</td>
        <td class="mono">162 / 292</td>
        <td class="mono">0</td>
        <td class="mono">130</td>
      </tr>
      <tr>
        <td>Frozen circuit (replacement model)</td>
        <td class="mono">2</td>
        <td class="mono">76.7%</td>
        <td class="mono">224 / 292</td>
        <td class="mono">23</td>
        <td class="mono">45</td>
      </tr>
      <tr>
        <td>Taylor over replacement model</td>
        <td class="mono">10</td>
        <td class="mono">79.1%</td>
        <td class="mono">231 / 292</td>
        <td class="mono">56</td>
        <td class="mono">5</td>
      </tr>
      <tr>
        <td class="bold">Taylor over original model</td>
        <td class="mono bold">10</td>
        <td class="mono bold">85.3%<span class="badge badge-good">best</span></td>
        <td class="mono bold">249 / 292</td>
        <td class="mono">12</td>
        <td class="mono">31</td>
      </tr>
    </tbody>
  </table>
</div>

Several things are worth noting. The α = 0 logit diff *alone* is useless, it sits at
majority-class accuracy regardless of threshold, because both groups output the correct
digit at α = 0 by construction. The value does not separate them; the *slope* does. This
rules out any explanation where the α = 0 representation directly encodes
parrot/recover; what's encoded is sensitivity.

The frozen circuit (77%) outperforms the oracle reading that same circuit (50% from Experiment 1), which is
telling: the circuit's *own linear response* to an embedding perturbation predicts better
than a sophisticated LLM agent trying to interpret its structure. The agent is looking at
the right object but asking the wrong question.

The gap between frozen circuit (77%) and original Taylor (85%) reflects transcoder
approximation error: replacing 42 MLP layers with sparse dictionaries introduces small
mismatches that compound into an 8-point accuracy gap. The circuit is a good
approximation, but not perfect.

<div class="box box-green">
  <div class="box-label">Key result</div>
  <div class="stat-row">
    <div class="stat-block">
      <div class="stat-n">85.3%</div>
      <div class="stat-desc">Taylor accuracy at threshold 10</div>
    </div>
    <div class="stat-block">
      <div class="stat-n">1 pass</div>
      <div class="stat-desc">one forward + one backward through the original model</div>
    </div>
  </div>
  <p>Before the tool is ever wrong, the local gradient at the correct-tool prompt
     predicts out-of-sample parrot/recover with 85% accuracy.</p>
</div>

</section>

<section markdown="1">

## Experiment 3: Oracle Succeeds with Probe-Weighted Circuits

Experiments 1 and 2 share a diagnosis: the oracle fails because the attribution target conflates
two competing mechanisms at the same operating point. Both parrot and recover cases read
the tool value and propagate it thus the circuit shows the same story. If we can attribute
toward a named residual-stream direction: one for the wrong-digit route, one for the
correct-digit route, the oracle receives a single-direction question instead of "who wins?"

To isolate those directions, we train a 10-class linear probe i.e., `nn.Linear(d_model, 10)`
on layer-26 residual-stream activations at the commit-token position. Training examples
are drawn from parrot cases (labeled with the wrong digit the model emits), recover cases
(labeled with the correct-answer digit), and correct-tool cases (labeled with the correct
digit). The probe learns to predict which digit the model is about to output from the
residual stream at that layer. This gives us a weight matrix W where each row W[d] is a
direction in residual space that points toward "about to emit digit d". W[wrong_digit] is
the direction associated with parroting the tool; W[correct_digit] is the direction
associated with the correct answer.

For each test case, on the same correct-tool prompt used in Experiment 1, we extract two attribution circuits:

- **Parrot circuit**: attributed toward W[wrong_digit]: what features drive the wrong-digit
  direction at layer 26?
- **Recover circuit**: attributed toward W[correct_digit]: what features drive the correct-digit
  direction?

The oracle now receives a circuit with a single named direction. It no longer needs to
infer which of two pathways "won"; it can describe what is mechanistically present in
that direction alone.

<div class="box box-accent">
  <div class="box-label">Analogy: circuits for probes</div>
  <p>
    In our prior work on spurious features (BiasInBios nurse/professor) 
    from Circuit Oracle paper, a biased probe
    trained on correlated data learns to exploit gender markers; an unbiased probe trained
    on balanced data is forced to rely on causal profession features instead. The oracle
    was asked: does the biased circuit contain spurious (gender) features, and does the
    unbiased circuit show causal (profession) features? Oracle accuracy reached 88% on 80
    runs, because each circuit attributed cleanly toward one interpretable
    direction. The parrot and recover probe circuits here follow the same logic: parrot
    circuit ≈ biased circuit (what drives the wrong-digit direction); recover circuit ≈
    causal circuit (what drives the correct-digit direction).
  </p>
</div>

<div class="box box-amber">
  <div class="box-label">Circuit Oracle: probe-weighted circuits, 52 cases</div>
  <div class="stat-row">
    <div class="stat-block">
      <div class="stat-n">80%</div>
      <div class="stat-desc">overall: 42 / 52</div>
    </div>
    <div class="stat-block">
      <div class="stat-n">73%</div>
      <div class="stat-desc">parrot probes: 19 / 26</div>
    </div>
    <div class="stat-block">
      <div class="stat-n">88%</div>
      <div class="stat-desc">recover probes: 23 / 26</div>
    </div>
  </div>
  <p>
    Compared to 50% on 42 correct-tool raw-graph cases.
    The 30-point gain comes entirely from redesigning the attribution target.
  </p>
</div>

The 30-point improvement from Experiment 1 to Experiment 3 involves no change to the oracle and no
change to the model, only a change to what the circuit is attributed toward. This
confirms attribution graphs as a capable tool for safety-relevant classification when the
question is formulated to isolate a single mechanism.

</section>

<section markdown="1">

## Discussion

In this work, we evaluated whether attribution graphs built to explain LLM behaviors can reliably 
predict a safety-relevant outcome: whether a model will blindly follow a response or recover with a 
correct answer.The three experiments form a single diagnostic arc. Experiment 1 shows the oracle at 
chance when given the raw attribution graph where the attribution target is ambiguous: on the correct-tool prompt, both parrot and recover cases look identical, and the static circuit cannot answer a counterfactual. Experiment 2 shows that the counterfactual question is answerable at 85% with one backward pass: the information is in the model, just not in the circuit's structure. Experiment 3 shows the oracle recovering to 80% when circuits are attributed toward isolated probe directions: 50%
(Experiment 1) → 80% (Experiment 3) → 85% (Experiment 2, Taylor).

The lesson is not that attribution graphs are unreliable. The same oracle that fails at
50% reaches 80% on a well-posed attribution task. The same model that is unreadable from
static structure is 85% predictable from its local gradient. The tool works; question
formulation determines whether the answer is accessible. The Karnoven et al. finding, that
interpretability tools provide no uplift over chat transcripts for counterfactual
prediction, applies when the attribution target and evaluation point are chosen without
regard for the counterfactual structure of the task. When they are chosen carefully, the
gap reopens.

The Taylor approach works here because we constructed a meaningful perturbation direction interpolating between the correct and wrong tool embeddings, and measured sensitivity
along it. This required knowing *what* to perturb, which came from understanding the task
structure. In settings where the relevant perturbation direction is not known in advance,
the approach would need to be adapted.

A natural next step is to combine all three: use probe-weighted circuits to identify
which features and positions are most relevant to a behavior, then apply targeted
perturbations along those directions to test causal claims. The graph provides the
vocabulary; the gradient provides the test; the probe provides the direction.

</section>

<div class="closing" markdown="1">

## The short version

Attribution graphs describe what a model computed on one input. They do not, by
themselves, describe what the model would compute if an input changed. For
safety-relevant prediction, that counterfactual is usually the question that matters.
When we ask the counterfactual directly via a Taylor approximation, accuracy goes from
50% to 85% in one backward pass. When we reformulate the attribution target with learned
probe directions, the circuit oracle climbs from 50% to 80%. The tools are capable; the
question formulation is the bottleneck.

</div>

</div>
