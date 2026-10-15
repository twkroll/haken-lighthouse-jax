# MASTER Prompt — NUM-ENG Numerical Engineering Gate 0.1

## Purpose

Audit, reproduce, classify, and conditionally integrate the local Lighthouse Numerik v0.1-v0.10 implementation as a controlled software-engineering lineage. All outputs remain DEVELOPMENT EVIDENCE unless a later scientific gate explicitly promotes a claim.

## Mandatory authorities

Read and obey:

- `PROJECT_GOVERNANCE.md`
- `research/master/parallel_engineering_policy_v0_1.md`
- `research/master/numerical_engineering_v0_10_intake_snapshot_0_1.md` (RB-017)
- `research/master/STATUS.md`
- `research/master/project_status.md`
- `research/core/STATUS.md`
- RB-004 mathematical baseline
- RB-006 and RB-009 validation-result freezes where relevant to reference semantics
- RB-010 Floquet theory only as a mathematical interface if needed
- RB-012 consolidated C1 theory where relevant
- RB-015 scientific FAIL and RB-016 follow-up scope.

Use frozen work as premises. Do not re-derive frozen science merely to rebuild context.

## Git / branch rule

Work only on the MASTER-authorized development branch:

`engineering/numerics-v0.1`.

Do not merge to `main` and do not rewrite canonical CORE artifacts.

The exact intake package must match RB-017 SHA-256:

`e21202362fc9ead75a3e5d92736d38002eb75d4e4ec5b4dd1cfb3c0a7c88db53`.

If the exact bytes are not available in the execution environment/chat, STOP as BLOCKED and request that exact package; do not substitute reconstructed files.

## Allowed work

### A. Provenance and packaging audit

1. Verify archive identity and full file inventory.
2. Repair the incomplete/stale SHA256 manifest prospectively on the engineering branch; preserve the original defective manifest for audit history.
3. Record exact environment, dependency versions, CPU/backend metadata, and deterministic execution controls.
4. Separate raw intake, audited source, generated artifacts, benchmark outputs, and test logs.

### B. Numerical-semantic audit

Check implementation consistency with frozen semantics, including:

- lifted phase and first hitting;
- no below-threshold reset;
- normalized alpha-state propagation;
- fixed edge-delay semantics;
- prespike history handling;
- labelled spike/arrival ordering;
- collision/transversality/chart invalidity handling;
- physical rerecording as authority;
- fixed-chart JAX replay only on validated charts;
- zero-weight structural-coordinate semantics;
- dense/sparse equivalence where claimed.

Any deviation must be classified REPAIR, DEFER, or REJECT; never silently normalized away.

### C. Reproduction

Reproduce the v0.1-v0.10 deterministic test lineage under a captured environment.

Mandatory target:

- all 11 supplied pytest modules;
- total 180 reported cases;
- modulewise PASS **and clean exit code**;
- explicit audit of the previously reported aggregate-process teardown/hang behavior.

A PASS requires reproducible logs. If a module prints PASS but fails/hangs on process exit, report that separately; do not count it as clean-suite PASS.

Existing deterministic learning-smoke tests may be rerun solely as software-gradient/optimizer regression. They remain DEVELOPMENT EVIDENCE and are not an AI benchmark.

### D. Engineering-quality validation

Define and execute finite software QA for at least:

1. reference-vs-replay event/token equivalence;
2. dense-vs-sparse equivalence on predetermined fixtures;
3. JAX JVP/VJP or Jacobian agreement against physically rerecorded finite differences on regular charts;
4. deliberate chart-boundary negative controls;
5. first-hit acceleration equivalence against the reference solver;
6. exact silent-guard negative/positive controls;
7. deterministic profiling/work counters;
8. memory/state-scaling accounting;
9. reproducible teardown/process-isolation checks.

Performance timings may be recorded only as LOCAL ENGINEERING METRICS. No general speedup/scaling claim is scientific evidence in this gate.

### E. Controlled integration

After audit classification, integrate only components marked `ENGINEERING-APPROVED` into the development branch under a clean versioned software layout. Keep:

- an intake-provenance record;
- complete file hashes;
- tests;
- environment lock/capture;
- changelog;
- clear DEVELOPMENT EVIDENCE labels.

Do not cherry-pick branch-local scientific claims into CORE.

## Component classification

Every material component must end as exactly one of:

- `ENGINEERING-APPROVED`
- `REPAIR-REQUIRED`
- `DEFERRED`
- `REJECTED`.

A software PASS does not create a scientific result freeze.

## Mandatory quality criteria

The gate must propose a stable engineering baseline only if:

- frozen RB-004 semantics are preserved;
- all accepted test modules have reproducible clean exits;
- protected seed namespaces are unused;
- a complete manifest exists;
- chart invalidity is fail-closed rather than silently accepted;
- reference/replay/sparse comparisons pass predetermined tolerances;
- gradient checks are limited to regular fixed charts;
- benchmark evidence is labelled local/development;
- known limitations are explicit.

## Forbidden

- no `2711xxx` RNG creation;
- no use of RB-015 development data as fresh confirmation;
- no confirmatory v0.27c execution;
- no new scientific effect search;
- no new learning task or AI benchmark;
- no post-hoc promotion of v0.9 learning smoke metrics;
- no APP-3 scientific execution;
- no v0.28 science;
- no novelty or manuscript claims;
- no modification of RB-015.

## Required output

On `engineering/numerics-v0.1`, create:

`research/numerical_engineering/numerical_engineering_gate_0_1.md`

and update:

`research/numerical_engineering/STATUS.md`

to `RETURN TO MASTER` or `BLOCKED`.

The result must include:

- exact Git/intake/environment identity;
- complete reproduction matrix;
- manifest/provenance result;
- semantic audit;
- QA criteria/results;
- component classification;
- integrated development-tree inventory;
- remaining defects;
- recommendation for a Numerical Engineering Freeze 0.1 or repair gate;
- explicit statement that all numerical/performance/learning outputs remain DEVELOPMENT EVIDENCE.

## Gate decision

`PASS` only if a reproducible engineering baseline is freeze-ready.

`CONDITIONAL/BLOCKED` if closure is incomplete.

No scientific PASS/FAIL is possible in this gate.

## STOP

Return once to MASTER after the complete engineering audit. Do not self-authorize APP-3.
