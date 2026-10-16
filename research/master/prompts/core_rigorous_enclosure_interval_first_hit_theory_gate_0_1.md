# MASTER Prompt — CORE Rigorous Enclosure & Interval First-Hit Certification Theory Gate 0.1

## Purpose

Close the main theoretical gap exposed by RB-023:

RB-022 proves first-hit/no-hit certification under convergent outward-valid enclosures and strict margins, while RB-023 validates finite float64 consistency but does not provide outward-rounded interval rigor.

Develop a mathematically explicit rigorous enclosure framework that can later be implemented and validated numerically.

This is a THEORY gate only.

No numerical execution is authorized here.

## Mandatory authorities

Read and use as premises:

- \`PROJECT_GOVERNANCE.md\`
- \`research/master/command_protocol_v0_2.md\`
- RB-004 Mathematical Freeze 0.1
- RB-012 Consolidated C1 Theory Freeze 0.1
- RB-019 Numerical Engineering Freeze 0.1
- RB-020 v0.27c Execution Contract Freeze 0.1
- RB-021 Numerical Engineering Freeze 0.2
- RB-022 Event-Chart Regularity & Certified First-Hit Theory Freeze 0.1
- RB-023 Theory-Derived Certification Validation Freeze 0.3
- current MASTER / CORE / NUM-ENG STATUS files.

RB-015 remains immutable SCIENTIFIC FAIL.

## Main goals

### I1 — interval representation

Define a finite outward-valid interval representation for:

- real scalars;
- alpha states;
- phase gaps;
- response values;
- accumulated phase gain.

State exactly which arithmetic operations require directed/outward rounding.

Do not assume exact real arithmetic once the gate begins discussing implementable floating-point certificates.

### I2 — interval alpha propagation

For arrival-free propagation,

\[
q(s)=e^{-\alpha s}q_0,
\qquad
\psi(s)=e^{-\alpha s}(\psi_0+s q_0),
\]

derive interval enclosures that remain inclusion-valid under:

- interval initial data;
- interval \(\alpha\);
- finite floating-point evaluation;
- segment subdivision.

Where monotonicity or finite analytic extrema can sharpen the enclosure, prove the conditions.

### I3 — rigorous response enclosure

For

\[
S_{r,h}(x),
\]

derive an interval extension compatible with the threshold splice and the frozen smoothness theory.

Handle intervals that:

- lie fully below \(h\);
- lie fully above \(h\);
- straddle \(h\).

State whether monotonicity is sufficient for sharp endpoint bounds and what changes for derivative enclosures.

### I4 — rigorous phase-gain enclosure

Construct a valid inclusion method for

\[
G([a,b])
=
\int_a^b S(\psi(s))\,ds.
\]

Possible admissible routes include:

- interval Riemann/Darboux sums from rigorous \(\psi\) extrema;
- interval quadrature with proved remainder bounds;
- Taylor-model or validated ODE integration if fully specified.

Choose one primary route and justify it.

Do not freeze multiple alternative solver families unless logically necessary.

### I5 — finite termination under strict margin

Strengthen the RB-022 finite-certification statement into an implementable theorem:

under explicit continuity/smoothness and strict-margin assumptions, a specified deterministic subdivision/refinement procedure terminates after finitely many steps with one of:

- CERTIFIED NO-HIT;
- CERTIFIED REGULAR HIT + bracket;
- UNCERTIFIED because resource limit reached.

Distinguish mathematical eventual termination from finite-budget software policy.

### I6 — certified transversality

Provide a rigorous lower enclosure for

\[
S(\psi(T^-))
\]

on a certified first-hit bracket sufficient to prove positive transversality.

State how bracket width and input enclosure interact.

### I7 — event-separation / boundary certification

Develop rigorous sufficient certificates for:

- event-time ordering;
- arrival/spike separation;
- horizon boundary separation;
- structural-zero labelled arrival separation.

Be explicit about what is possible before exact event times are known.

### I8 — local chart-radius lower bound

Investigate whether explicit conservative lower bounds on parameter-space chart validity can be derived from:

- transversality margin;
- event-separation margin;
- boundary margin;
- bounds on event-time sensitivities.

If a fully computable nontrivial lower bound cannot be proved, state a weaker proposition and leave the sharp-radius problem OPEN.

Do not manufacture a chart-radius theorem without sufficient control.

### I9 — structural-zero interval semantics

Carry RB-022 structural-zero semantics through interval certification:

- topology remains fixed when \(w_e\) interval contains zero;
- the labelled arrival is retained;
- the jump enclosure includes identity at \(w_e=0\);
- parameter intervals crossing zero do not trigger topology changes.

### I10 — certification failure taxonomy

Mathematically distinguish:

- theorem assumptions violated;
- strict margin absent;
- interval enclosure too wide;
- resource budget exhausted;
- physical ordinary-chart invalidity;
- true mathematical contradiction.

This taxonomy must be compatible with future fail-closed software.

## Constructive output requirement

The gate must end with one finite algorithm specification suitable for a later NUM-ENG implementation gate.

That specification must include:

1. input assumptions;
2. interval primitives required;
3. deterministic refinement order;
4. stopping rules;
5. outcome labels;
6. proof obligations for every positive certificate;
7. structural-zero handling;
8. event-order handling;
9. no-hit / first-hit certificate output data;
10. explicit unsupported cases.

## Claim discipline

Every statement must be labelled:

- THEOREM / PROVED
- PROPOSITION
- LEMMA
- ASSUMPTION
- CONJECTURE
- INTERPRETATION
- OPEN QUESTION.

No empirical statement from RB-023 becomes theorem merely because all finite fixtures passed.

## Forbidden

- no numerical execution;
- no interval-library benchmarking;
- no tolerance tuning;
- no TR-27C execution;
- no \`2711xxx\` RNG;
- no APP-3;
- no v0.28 effect-bearing science;
- no novelty/manuscript claims.

## Required output

Create:

\`research/core/rigorous_enclosure_interval_first_hit_theory_gate_0_1.md\`

and update:

\`research/core/STATUS.md\`

to RETURN TO MASTER or BLOCKED.

The report must include:

- precise arithmetic assumptions;
- proved inclusion lemmas;
- first-hit/no-hit certification theorem;
- rigorous transversality treatment;
- event-order/boundary treatment;
- chart-radius result or explicit non-result;
- structural-zero treatment;
- finite constructive algorithm specification;
- explicit open problems;
- recommendation for a theory freeze or repair gate.

## Decision

PASS only if a coherent rigorous-enclosure theory layer and one implementable deterministic certification algorithm are specified without hidden numerical assumptions.

CONDITIONAL/BLOCKED if outward-validity, finite termination, or event-order logic remains materially unresolved.

## STOP

STOP — RETURN TO MASTER
