# MASTER Prompt — NUM-ENG MPFR IR-A4-R Qualification & Eventual-Certification Gate 0.5

## Purpose

Attempt to close the principal numerical proof obligation left open by RB-025:

establish, on a prospectively frozen compact finite RIFC domain and fixed expression family, the RB-024 / IR-A4-R whole-expression arithmetic excess-rate bound needed to justify eventual certification under

\[
p_n=128+8n.
\]

This gate is narrowly about arithmetic qualification and eventual-certification implementation semantics.

Do not broaden it into full multi-event tape certification, NNE-A, performance optimization or scientific experiments.

## Mandatory authorities

Read and obey:

- PROJECT_GOVERNANCE.md
- research/master/parallel_engineering_policy_v0_1.md
- RB-019
- RB-021
- RB-023
- RB-024
- RB-025
- current MASTER / CORE / NUM-ENG STATUS files.

Work only on:

`engineering/numerics-v0.1`.

The physical reference remains:

`NUMENG_PULSE_AWARE_REFERENCE_V1`.

The finite-soundness RIFC implementation frozen by RB-025 is the starting point.

## Pre-execution contract

Before any new Gate-0.5 validation output, create and commit:

`research/numerical_engineering/rifc_ir_a4r_qualification_contract_0_5.md`.

The contract must prospectively freeze:

1. exact MPFR version/library identity;
2. exact RIFC source identity;
3. compact admissible scalar domain K;
4. exact expression-graph inventory;
5. exact primitive-operation inventory;
6. exponent-range assumptions;
7. divisor-away-from-zero assumptions;
8. exact norm/width/error definitions;
9. derivation strategy for primitive \(C_K2^{-p}\) bounds;
10. derivation strategy for whole-expression \(B_KN2^{-p}\);
11. exact operation-count bound \(N_n\);
12. exact validation fixtures;
13. exact precision levels;
14. exact acceptance/rejection conditions;
15. exact artifact/proof format.

No domain or bound may be widened/narrowed after output inspection to rescue the gate.

## Q1 — primitive MPFR rounding-rate qualification

Derive a mathematically explicit bounded-domain excess-width estimate for every primitive used by RIFC:

- exact rational endpoint load;
- +;
- -;
- multiplication;
- permitted division;
- exponential;
- comparisons/hull/intersection where width-relevant.

Use MPFR's documented correct-rounding model as an assumption/source contract, not empirical measurements alone.

The result must state exact conditions under which a bound proportional to \(2^{-p}\) follows.

If exponent-range or magnitude terms enter the constant, include them explicitly in \(C_K\).

## Q2 — threshold-safe response graph

Derive a bounded-domain propagation estimate for the three response branches:

- fully below threshold;
- threshold-straddling monotone enclosure;
- fully above threshold.

For the above-threshold reciprocal/exponential branch, freeze an explicit positive lower bound on \(x-h\) over the compact domain used for the rate theorem.

Do not claim a uniform finite constant across a domain that permits arbitrarily small positive \(x-h\) unless actually proved.

## Q3 — alpha-state expression graph

Derive an explicit arithmetic excess propagation bound for:

\[
e^{-\alpha s}q_0,
\qquad
e^{-\alpha s}(\psi_0+s q_0),
\]

on the frozen compact domain.

Separate exact-range interval width from arithmetic excess width.

## Q4 — Darboux cell / prefix accumulation

Derive a whole-expression bound for:

- cell width;
- response enclosure;
- cell gain;
- prefix accumulation.

Show how the number of arithmetic operations grows with \(m_n=2^n\).

Prove an explicit finite

\[
N_n\le a2^n+b.
\]

## Q5 — whole-expression IR-A4-R theorem

Produce either:

### PASS route

A proved bound of the form

\[
E_{\rm arith}(n)
\le
B_KN_n2^{-p_n},
\]

with finite \(B_K\) on the prospectively frozen compact domain and

\[
p_n=128+8n,
\]

such that

\[
E_{\rm arith}(n)\to0.
\]

OR

### NO-GO route

A rigorous demonstration that the current source/backend/domain cannot justify IR-A4-R as frozen.

A NO-GO is a valid engineering result and must not be rescued by empirical fitting.

## Q6 — implementation correspondence audit

Show that the actual RB-025 source expression graph matches the graph used in the mathematical bound.

Every primitive/branch that can appear in a positive certificate must be accounted for.

If source behavior differs materially from the proved graph, return BLOCKED or repair prospectively before validation under a separately committed addendum.

## Q7 — precision/refinement validation

Only after the analytical bound is fixed, run deterministic validation at predeclared precision levels to check consistency of observed arithmetic excess with the proved upper bounds.

Observed errors may validate the proof implementation but may not define \(B_K\).

## Q8 — eventual-certification fixtures

Only if Q5 PASS is established, execute prospectively fixed strict-margin no-hit and regular-hit fixtures across increasing refinement levels.

Validate that the implementation eventually emits the expected positive finite certificate.

This is validation of the theorem implementation, not proof by experiment.

Include deliberately small finite \(N_{\max}\) controls returning:

`RESOURCE_EXHAUSTED / UNCERTIFIED`.

## Q9 — non-goals

Do not implement in Gate 0.5:

- full sequential multi-event tape certification;
- parameter-box NNE-A;
- general chart-radius algorithms;
- new acceleration/performance work;
- APP-3 or TR-27C.

Those remain separate future gates.

## Result classes

Every material result must be classified:

- IR-A4-R ESTABLISHED;
- FINITE SOUNDNESS PRESERVED;
- IR-A4-R NOT ESTABLISHED;
- IMPLEMENTATION/PROOF MISMATCH;
- REPAIR-REQUIRED;
- DEFERRED.

## PASS criteria

Full PASS requires:

1. prospectively frozen Gate-0.5 contract;
2. mathematically justified primitive rate bounds;
3. mathematically justified whole-expression propagation constant on the frozen compact domain;
4. source-expression correspondence;
5. \(N_n=O(2^n)\) bound;
6. \(E_{\rm arith}(n)\to0\) under \(p_n=128+8n\);
7. deterministic eventual-certification validation fixtures pass;
8. RB-025 finite-soundness tests remain compatible.

A bounded result `IR-A4-R NOT ESTABLISHED` is acceptable as a truthful return but is not a PASS for eventual certification.

## Forbidden

- no empirical fitting of \(B_K\) as proof;
- no post-output domain shrinking to force PASS;
- no protected RNG;
- no TR-27C;
- no APP-3;
- no stochastic benchmark;
- no scientific speedup/scaling claim;
- no executable main merge;
- no novelty/manuscript claims.

## Required outputs

On `engineering/numerics-v0.1` create:

1. `research/numerical_engineering/rifc_ir_a4r_qualification_contract_0_5.md`
2. `research/numerical_engineering/rifc_ir_a4r_qualification_gate_0_5.md`
3. versioned proof/calculation artifacts;
4. deterministic validation logs if Q5 PASS;
5. updated manifest/provenance.

Update NUM-ENG STATUS to RETURN TO MASTER or BLOCKED.

## Recommendation

If IR-A4-R is established, recommend a bounded:

`NUM-ENG RIFC Eventual-Certification Qualification Freeze 0.5`.

Do not fold full multi-event/NNE-A certification into that freeze.

## STOP

STOP — RETURN TO MASTER
