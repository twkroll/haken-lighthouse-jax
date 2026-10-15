# MASTER Prompt — NUM-ENG Robustness, Scaling & Differentiable Kernel Gate 0.2

## Purpose

Extend the RB-019 engineering baseline without changing frozen science. The gate must stress-test numerical robustness, quantify local engineering scaling, harden sparse/JAX kernels, and classify acceleration methods against the certified physical authority.

All outputs remain DEVELOPMENT EVIDENCE / ENGINEERING METRICS.

## Authorities

Read and obey:

- PROJECT_GOVERNANCE.md
- research/master/parallel_engineering_policy_v0_1.md
- RB-004 scientific baseline
- RB-019 Numerical Engineering Freeze 0.1
- RB-020 CORE v0.27c Execution Contract Freeze 0.1
- current MASTER/CORE/NUM-ENG STATUS files

Work only on engineering/numerics-v0.1.

## Frozen authority

The physical authority remains the RB-019 certified path:
NUMENG_PULSE_AWARE_REFERENCE_V1.

No accelerated scheduler may become authoritative merely by being faster.

## A — Robustness envelope

Before running tests, define a finite deterministic stress matrix spanning:
- alpha values including ordinary and narrow-pulse regimes;
- weak/strong weights within numerically safe ranges;
- short/long delays;
- near-threshold noncrossing and crossing cases;
- event-separation margins;
- structural zero-weight edges;
- sparse graph sizes/topologies.

Freeze the matrix before execution.

## B — First-hit and chart certification

Compare:
- certified physical authority;
- retained accelerated first-hit methods;
- dense/sparse paths;
- fixed-chart replay only after certified rerecording.

Track exact token agreement, event-time error, invalid/fail-closed behavior, and certification status.

Any disagreement with the physical authority is an engineering failure for that accelerated method, not a reason to retune the reference.

## C — Gradient robustness

On predetermined regular-chart fixtures:
- compare JAX AD/JVP/VJP or Jacobians to physically rerecorded finite differences;
- include weights, delays and initial-state coordinates;
- record chart exits separately from derivative disagreement;
- never finite-difference across a changed event itinerary.

## D — Sparse scaling

Measure deterministic local engineering metrics across a predeclared set of N/E sizes:
- state-memory footprint;
- event count/work counters;
- rerecord count;
- wall time as local machine metadata;
- JAX compile vs execution time separately;
- dense-vs-sparse storage/work ratios.

Do not promote empirical complexity exponents or universal speedup claims.

## E — Acceleration audit

For each first-hit acceleration path classify:
- ENGINEERING-APPROVED WITH DOMAIN;
- DEVELOPMENT COMPARATOR;
- REPAIR-REQUIRED;
- REJECTED.

Each approved domain must be explicit and must retain fail-closed fallback to the certified physical authority.

## F — Process/runtime robustness

Check:
- clean module/process teardown;
- deterministic repeated runs;
- CPU/x64 configuration;
- manifest and environment capture;
- no protected-seed use.

## Mandatory quality boundary

The gate may recommend a Numerical Engineering Freeze 0.2 only if:
- RB-019 physical authority remains unchanged or any proposed change is separately justified and validated prospectively;
- all new stress fixtures are fixed before results;
- no silent chart acceptance occurs;
- no protected 2701xxx/2711xxx namespace is used;
- all performance numbers are labelled local engineering metrics;
- failures are preserved.

## Forbidden

- no scientific effect search;
- no TR-27C execution;
- no 2711xxx RNG;
- no APP-3 training/benchmark;
- no retroactive promotion of smoke tests;
- no scientific scaling/speedup claim;
- no main executable-source merge;
- no novelty/manuscript claims.

## Required output

On engineering/numerics-v0.1 create:

research/numerical_engineering/robustness_scaling_differentiable_kernel_gate_0_2.md

and update research/numerical_engineering/STATUS.md to RETURN TO MASTER or BLOCKED.

Report:
- frozen stress matrix;
- robustness results;
- gradient results;
- local scaling/work results;
- acceleration classification;
- defects/limits;
- complete provenance;
- recommendation for Numerical Engineering Freeze 0.2 or follow-up repair.

## Decision

PASS only for an engineering-quality result. No scientific PASS is possible.

## STOP

STOP — RETURN TO MASTER
