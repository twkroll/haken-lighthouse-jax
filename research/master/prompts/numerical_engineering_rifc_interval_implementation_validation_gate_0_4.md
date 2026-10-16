# MASTER Prompt — NUM-ENG RIFC-0.1 Outward-Interval Implementation & Validation Gate 0.4

## Purpose

Implement and validate the RB-024 \`RIFC-0.1 — Rigorous Interval First-Hit Certifier\` on the isolated numerical-engineering branch.

This is a numerical-engineering / theory-validation gate.

It must not create effect-bearing science, protected stochastic data, AI-training evidence, or universal performance claims.

## Mandatory authorities

Read and obey:

- PROJECT_GOVERNANCE.md
- research/master/parallel_engineering_policy_v0_1.md
- RB-004
- RB-019
- RB-021
- RB-022
- RB-023
- RB-024
- current MASTER / CORE / NUM-ENG STATUS files.

Work only on:

\`engineering/numerics-v0.1\`.

The existing physical reference authority remains:

\`NUMENG_PULSE_AWARE_REFERENCE_V1\`.

RIFC-0.1 is a certification layer, not a replacement physical simulator unless a later MASTER gate explicitly changes that role.

## Pre-execution contract requirement

Before executing any new Gate-0.4 validation output, create and commit:

\`research/numerical_engineering/rifc_interval_implementation_validation_contract_0_4.md\`.

That contract must freeze:

1. chosen interval backend;
2. exact backend version/build;
3. directed-rounding semantics;
4. rigorous exponential inclusion contract;
5. proof/evidence for IR-A1–IR-A3 and IR-A5;
6. proof/evidence for IR-A4-R or an explicitly weaker declaration if only finite soundness is being tested;
7. compact admissible domains used for convergence claims;
8. exact fixture set;
9. exact refinement levels / \(N_{\max}\);
10. exact classification rules;
11. exact comparison criteria;
12. exact negative controls;
13. exact expected outcome category of each fixture;
14. artifact/log/manifest format.

No fixture, precision rule, tolerance or outcome criterion may be changed after Gate-0.4 outputs are inspected.

If the backend proof obligations cannot be frozen first, return BLOCKED.

## A. Backend qualification

### RI-01 — directed primitive inclusion

Validate or formally justify outward inclusion for:

- +;
- -;
- multiplication;
- permitted division;
- min/max/hull/intersection operations used by RIFC.

Ordinary round-to-nearest arithmetic is insufficient.

### RI-02 — rigorous exponential

The exponential interval must have an independently justified inclusion contract.

A plain platform \`exp\` followed by one \`nextafter\` step is not acceptable unless a proved worst-case error bound establishes inclusion.

Record exactly why the chosen backend is admissible.

### RI-03 — IR-A4-R rate obligation

If Gate 0.4 claims eventual-certification behavior under the frozen schedule

\[
p_n=128+8n,
\]

it must establish the bounded-domain excess-width/rate obligation required by RB-024.

If this cannot be justified, the implementation may still be validated for finite certificate soundness but must explicitly classify eventual-certification as \`DEFERRED / NOT ESTABLISHED\`.

Do not infer the rate from empirical convergence alone.

## B. RIFC implementation

Implement a versioned certification module that preserves RB-024 semantics for:

- interval state representation;
- interval alpha propagation;
- threshold-safe response enclosure;
- dyadic Darboux phase gain;
- prefix interval accumulation;
- deterministic no-hit test;
- deterministic regular-hit bracket search;
- transversality lower bound;
- event-order/horizon logic;
- structural-zero arrival semantics;
- finite resource limits;
- fail-closed taxonomy;
- certificate artifact generation.

Positive certificate objects must retain all RB-024 proof obligations sufficient for independent audit.

## C. Deterministic validation

### RI-04 — primitive exactness / containment fixtures

Use prospectively frozen analytically checkable scalar and alpha-propagation fixtures.

Verify exact values/ranges lie inside produced intervals.

### RI-05 — threshold-straddling response fixtures

Include cells:

- fully below \(h\);
- exactly touching \(h\);
- straddling \(h\);
- fully above \(h\).

No singular reciprocal evaluation at the threshold is allowed.

### RI-06 — Darboux gain inclusion

For prospectively fixed segments with independent high-precision reference integration, verify the exact/high-precision gain lies inside every claimed rigorous interval.

High-precision reference is a validation comparator, not the source of the certificate.

### RI-07 — certified no-hit

Use predetermined strict-margin no-hit fixtures including TH-FH-02/related RB-023 cases.

Require positive outward margin.

Include equality/near-equality controls that must remain inconclusive if strict certification does not close.

### RI-08 — certified regular first hit

Use predetermined strict regular-hit fixtures including the narrow-pulse TH-FH-01 family.

Require:

- rigorous hit bracket;
- contained physical-reference hit;
- positive transversality lower bound;
- correct next-event ordering.

### RI-09 — structural-zero

Use the RB-022/RB-023 topology-fixed structural-zero family.

Require:

- zero-weight arrival retained;
- identity jump at exact zero enclosed;
- interval weights crossing zero do not alter topology;
- event-order/collision logic still includes the structural arrival.

### RI-10 — event-order / boundary

Validate:

- spike before arrival;
- arrival before spike;
- overlapping inconclusive intervals;
- exact/symbolic collision invalidity;
- horizon boundary;
- initial boundary;
- simultaneous commuting arrivals remain ordinary-chart invalid unless a grouped-event theory exists.

### RI-11 — fail-closed taxonomy

Construct one deterministic control for every nonpositive outcome class that is practically implementable:

- ASSUMPTION_VIOLATED;
- STRICT_MARGIN_ABSENT;
- ENCLOSURE_INCONCLUSIVE;
- RESOURCE_EXHAUSTED;
- UNCERTIFIED_ARITHMETIC;
- ORDINARY_CHART_INVALID;
- UNSUPPORTED_CASE.

No control may silently fall through to a positive certificate.

### RI-12 — certificate replay/audit

Every positive certificate must be independently reloadable and checkable from its serialized proof data without rerunning the physical simulator.

The audit checker must verify strict inequalities and topology/event identities.

## D. Eventual-certification validation

Only if IR-A4-R is independently established:

### RI-13 — refinement monotonic study

On predetermined strict-margin deterministic fixtures, demonstrate that refinement eventually reaches the expected positive certificate.

This is implementation validation of the theorem, not proof of the theorem.

Do not require interval widths to be monotonically nested unless the backend mathematically guarantees nesting.

### RI-14 — finite-budget behavior

For deliberately insufficient \(N_{\max}\), return:

\`RESOURCE_EXHAUSTED / UNCERTIFIED\`

without a negative physical conclusion.

## E. Full-chart scope

Gate 0.4 does NOT need to solve general parameter-box NNE-A.

It may:

- implement deterministic sequential next-event certification;
- validate finite single-trajectory tape construction;
- optionally prototype family-valued segment certificates.

It may not claim a general full parameter-box chart radius unless independent NNE-A and indexed-event neighborhood obligations are actually implemented and validated under a separately frozen contract.

## F. Compatibility

Rerun a prospectively selected finite compatibility subset from RB-021/RB-023 sufficient to show that adding the interval-certification layer does not silently alter the physical reference/JAX guard semantics.

A full historical aggregate rerun is optional unless source changes touch existing physical/reference modules.

If existing source is modified, the contract must require the relevant broader regression suite before PASS.

## Component classification

Every material Gate-0.4 component must end as:

- ENGINEERING-APPROVED;
- ENGINEERING-APPROVED FOR FINITE SOUNDNESS ONLY;
- REPAIR-REQUIRED;
- DEFERRED;
- REJECTED.

## Gate decision

PASS only if:

- the pre-execution contract was committed before outputs;
- positive certificates are demonstrably outward-valid under the chosen backend contract;
- the fail-closed taxonomy is implemented;
- structural-zero/event-order semantics match RB-024;
- no positive certificate depends on ordinary unverified floating-point math;
- all required deterministic fixtures pass.

If IR-A4-R cannot be established, a bounded PASS may still be possible for finite-certificate soundness only, but the result must explicitly withhold eventual-certification claims.

Return BLOCKED if even finite outward inclusion cannot be justified.

## Forbidden

- no \`2711xxx\` RNG creation;
- no TR-27C execution;
- no v0.27c confirmatory execution;
- no APP-3 execution;
- no stochastic scientific benchmark;
- no scientific speedup/scaling claim;
- no post-output retuning;
- no executable merge to \`main\`;
- no novelty/manuscript claims.

## Required outputs

On \`engineering/numerics-v0.1\` create:

1. \`research/numerical_engineering/rifc_interval_implementation_validation_contract_0_4.md\`
2. \`research/numerical_engineering/rifc_interval_implementation_validation_gate_0_4.md\`
3. versioned implementation subtree and tests;
4. raw machine-readable certificate artifacts/logs;
5. complete manifest/provenance.

Update:

\`research/numerical_engineering/STATUS.md\`

to RETURN TO MASTER or BLOCKED.

## Recommendation

If PASS, recommend a bounded:

\`NUM-ENG RIFC-0.1 Interval Certification Freeze 0.4\`.

Do not claim global simulator correctness.

## STOP

STOP — RETURN TO MASTER
