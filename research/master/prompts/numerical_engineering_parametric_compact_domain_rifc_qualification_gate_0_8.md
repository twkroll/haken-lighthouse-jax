# MASTER Prompt — NUM-ENG Parametric Compact-Domain RIFC Qualification Gate 0.8

## Purpose

Operationalize RB-029's Q-RIFC-K methodology on genuinely nontrivial compact parameter boxes rather than finite singleton fixture lists.

This is an engineering/theory-validation gate only.

It must not change frozen science or create effect-bearing results.

## Mandatory authorities

Read and obey:

- PROJECT_GOVERNANCE.md
- research/master/parallel_engineering_policy_v0_1.md
- RB-019
- RB-021
- RB-023
- RB-024
- RB-025
- RB-026
- RB-027
- RB-028
- RB-029
- current MASTER / CORE / NUM-ENG STATUS files.

Work only on:

`engineering/numerics-v0.1`.

Physical authority remains:

`NUMENG_PULSE_AWARE_REFERENCE_V1`.

## Pre-execution qualification contract

Before any new qualification output or validation result, create and commit:

`research/numerical_engineering/rifc_parametric_compact_domain_qualification_contract_0_8.md`.

The contract must prospectively freeze:

1. exact repaired RIFC source/backend identities;
2. at least three nontrivial compact parameter boxes with positive width in their declared varying coordinates;
3. exact branch-coverage target for each box;
4. exact semantic hull proof strategy;
5. exact threshold/divisor-margin proof strategy;
6. exact graph branch inventory;
7. exact primitive/backend constants;
8. exact local depth/count strategy;
9. exact symbolic \(B_K\) construction;
10. exact finite-source correspondence checks;
11. exact finite validation sampling scheme used only after analytical qualification;
12. exact outcome classes and negative controls.

No box may be shrunk, shifted or split after outputs are inspected to rescue PASS.

## Box-coverage requirements

The prospective compact boxes must collectively cover at least:

- one uniformly fully subthreshold/no-hit family;
- one uniformly regular positive-response/first-hit-capable family with a proved active threshold margin;
- one structural-zero weight-crossing family with fixed topology and labelled arrivals.

At least one box must vary more than one continuous coordinate.

Do not include arbitrary near-threshold positive branches unless a positive uniform margin can be proved prospectively.

## Q1 — semantic hull qualification

For each box \(K_j\), establish branchwise exact/rigorous semantic hull constants

\[
H_{K_j}.
\]

Do this before using the desired whole-expression arithmetic bound.

If a hull cannot be established, that box is NOT QUALIFIED.

## Q2 — divisor and threshold margins

For every active reciprocal/division path, derive a positive uniform

\[
\delta_{K_j}>0.
\]

Subthreshold and straddling branches must follow RB-029's branch semantics.

A box allowing the active above-threshold gap to collapse to zero is not qualified under the current source graph.

## Q3 — branch cover / graph audit

Enumerate all positive-certificate graph branches reachable on each box.

Verify the Gate-0.6 repaired source remains unchanged.

Any reachable unqualified branch is a blocker for that box.

## Q4 — instantiate RB-029 constants

For each qualified box, derive prospectively:

- primitive \(r_{v,b}\);
- endpoint Lipschitz constants \(L_{v,b}\);
- \(D_K,c_K,a_K,b_K\);
- \(C_{\rm cell}\);
- \(C_{\rm prefix}\);
- \(C_{\rm wrap}\);
- finite symbolic \(B_K\).

Do not fit \(B_K\) to observed numerical errors.

## Q5 — schedule qualification

Verify the chosen refinement/precision schedule satisfies RB-029's condition.

For dyadic refinement and

\[
p_n=128+8n,
\]

record that \(\gamma=8>1\).

Do not present this as a practical cost optimum.

## Q6 — finite-source correspondence

Verify that finite Gate-0.6 calls within resource caps correspond to the idealized arithmetic family used in each box proof.

Resource exits remain fail-closed.

## Q7 — post-proof deterministic validation

Only after a box has analytically qualified, run the prospectively fixed finite validation points.

For each point verify:

- exact source/backend identity;
- produced interval inclusion;
- arithmetic excess below the already proved symbolic bound where independently evaluable;
- correct positive/inconclusive classification;
- certificate replay/audit.

Finite validation may not define or tighten \(B_K\).

## Q8 — negative controls

Include prospectively:

- one box/case with collapsing active threshold margin that must be rejected as theorem-unqualified;
- one insufficient-resource case returning UNCERTIFIED/RESOURCE_EXHAUSTED;
- one branch-coverage mismatch or deliberately unsupported-domain control.

No negative control may be silently excluded after output.

## Q9 — classification

Each box must end as exactly one of:

- PARAMETRIC DOMAIN QUALIFIED;
- THEOREM ASSUMPTION FAILED;
- IMPLEMENTATION/GRAPH MISMATCH;
- FINITE VALIDATION FAILED;
- RESOURCE-LIMITED / QUALIFIED IDEALLY;
- DEFERRED.

The gate as a whole may PASS if at least the required three coverage boxes are analytically qualified and all required post-proof validations/negative controls behave as preregistered.

## Q10 — non-goals

Do not:

- modify executable RIFC source;
- implement sequential multi-event tape certification;
- implement NNE-A;
- run performance/scaling experiments;
- execute TR-27C;
- use protected RNG;
- execute APP-3;
- make scientific effect/novelty/manuscript claims.

## Required outputs

On `engineering/numerics-v0.1`, create:

1. `research/numerical_engineering/rifc_parametric_compact_domain_qualification_contract_0_8.md`;
2. `research/numerical_engineering/rifc_parametric_compact_domain_qualification_gate_0_8.md`;
3. symbolic per-box qualification artifacts/constants;
4. post-proof validation logs;
5. provenance/manifest.

Update NUM-ENG STATUS to RETURN TO MASTER or BLOCKED.

## Recommendation

If PASS, recommend a bounded engineering freeze for the specifically qualified compact boxes and the operational Q-RIFC-K workflow.

Do not claim global Lighthouse-domain qualification.

## STOP

STOP — RETURN TO MASTER
