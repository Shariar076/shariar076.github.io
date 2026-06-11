---
title: "Constraint Programming for NP-hard Problems"
excerpt: "Constraint Programming · Automated Reasoning<br/><img src='/images/hidato_csp.png' style='max-width:400px;'>"
collection: portfolio
---

**Tags:** Constraint Programming · Automated Reasoning

Graduate coursework (CSE 6501: Advanced AI) modeling three NP-hard problems as constraint problems and solving them with constraint propagation, search heuristics, and IBM ILOG/CPLEX.

- **Hidato puzzle** — modeled as a constraint satisfaction problem and solved with backtracking search, forward checking, generalized arc consistency, and a minimum-remaining-value variable-ordering heuristic. (Notably hard for modern SAT solvers, which motivated the CSP formulation.)
- **Rehearsal scheduling** — a constraint optimization problem using dual/channelling variables, branch-and-bound on the objective, symmetry breaking, and implied (redundant) constraints to prune the search.
- **Open stacks problem** (2005 Constraint Modelling Challenge) — explored multiple formulations: base, graph-colouring, dual-viewpoint, and scheduling models, comparing how each propagates and bounds the search.

[Hidato report](https://drive.google.com/file/d/1pzAWhVSHUg1VaI_Krqao5myCcczqFkbi/view?usp=sharing) · [Rehearsal report](https://drive.google.com/file/d/1F5vhPsRjKCTumTDhFYyt_RGPiIZZ5w7r/view?usp=sharing) · [Open Stacks report](https://drive.google.com/file/d/1jMij6PIZn_rvCka1lGF6RxMGIdAkoQQl/view?usp=sharing)
