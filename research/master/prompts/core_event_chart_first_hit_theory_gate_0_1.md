# MASTER Prompt — CORE Event-Chart Regularity & Certified First-Hit Theory Gate 0.1

## Purpose

Develop the next mathematical layer needed to connect the frozen Lighthouse hybrid dynamics to the RB-019 numerical baseline: explicit sufficient conditions and limitations for first-hit completeness, event-chart regularity, transversality, and local differentiability.

This is a THEORY gate. It must not execute effect-bearing science, generate confirmatory data, tune numerics against outcomes, or claim global correctness unless actually proved.

## Authorities

Read and use as premises:

- PROJECT_GOVERNANCE.md
- research/master/command_protocol_v0_2.md
- RB-004 Mathematical Freeze 0.1
- RB-007 Continuation Theory Freeze 0.1
- RB-010 Floquet Theory Freeze 0.1
- RB-012 Consolidated C1 Theory Freeze 0.1
- RB-019 Numerical Engineering Freeze 0.1
- RB-020 v0.27c Execution Contract Freeze 0.1
- current CORE/MASTER/NUM-ENG STATUS files

RB-015 remains immutable SCIENTIFIC FAIL.

## Questions to resolve

### T1 — First-hit existence/completeness on an inter-event interval

For the frozen alpha-state dynamics and response S, derive usable sufficient conditions under which all threshold crossings of the lifted phase on a fixed inter-event interval are either:
- absent and certifiably excluded, or
- uniquely bracketable as a first hit.

Distinguish mathematical completeness from finite numerical certification.

### T2 — Bounds for the response and phase accumulation

Derive explicit bounds for:
- S, S', and, where legitimately available, higher derivatives on regular regions;
- alpha-state decay and weighted input tails;
- accumulated phase error from truncating or approximating late alpha tails.

State the exact regularity assumptions needed.

### T3 — Event-chart regularity

Formalize sufficient local conditions for a regular event chart in terms of:
- positive transversality margin;
- event-separation/collision margin;
- fixed event ordering;
- delayed-arrival separation;
- non-boundary initial/horizon events.

Clarify what is merely sufficient, what is necessary, and what remains open.

### T4 — Local differentiability

Within a regular chart, state and prove/derive the differentiability of event times with respect to:
- initial phase/state;
- weights;
- fixed physical delays;
- admissible scalar parameters.

Separate:
- existence of a derivative;
- representation by fixed-chart replay/JAX;
- validity radius of the chart;
- numerical ability to certify that radius.

### T5 — Link to RB-019 engineering certification

Analyze which RB-019 rules can be justified mathematically and which remain engineering controls:
- pulse-aware segmentation;
- tail bounds;
- transversality thresholds;
- collision tolerances;
- tape certification;
- fail-closed invalidity.

Do not retroactively convert engineering tolerances into theorems.

### T6 — Theoretical stress cases

Construct a finite set of analytically motivated edge cases that a later numerical gate should test, such as:
- narrow alpha pulses;
- near-threshold but noncrossing input;
- nearly tangent first hit;
- nearly simultaneous spike/arrival;
- long-delay tail-dominated intervals;
- structural zero-weight edges.

These cases are theory-derived fixtures only. Do not execute them in CORE.

## Claim discipline

Every result must be labelled:
- THEOREM / PROVED
- PROPOSITION
- LEMMA
- ASSUMPTION
- CONJECTURE
- INTERPRETATION
- OPEN QUESTION

No blanket global theorem may be stated unless fully proved.

## Forbidden

- no TR-27C execution;
- no 2711xxx RNG;
- no v0.27c confirmatory execution;
- no APP-3 training or benchmark;
- no numerical parameter scan for favorable margins;
- no performance/scaling experiment;
- no v0.28 effect-bearing science;
- no novelty/manuscript claims.

## Required output

Create:

research/core/event_chart_first_hit_theory_gate_0_1.md

and update research/core/STATUS.md to RETURN TO MASTER or BLOCKED.

The deliverable must include:
- exact assumptions;
- proved statements;
- explicit non-results/open questions;
- implications for numerical certification;
- proposed next theory freeze if PASS;
- proposed finite theory-derived numerical validation requirements, without executing them.

## Decision

PASS if a coherent, internally consistent theory layer is established with explicit assumptions and boundaries.

CONDITIONAL/BLOCKED if key derivations remain unresolved.

## STOP

STOP — RETURN TO MASTER
