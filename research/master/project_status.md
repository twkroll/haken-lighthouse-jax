# Lighthouse-JAX — Canonical Project Status

Version: 0.5
Date: 2026-09-04

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

Governance Initialization 0.1 is complete and STABLE. MASTER PDF Snapshot v0.2 exists. No scientific result is frozen yet. The first scientific gate remains authorized but unexecuted in the Git single source of truth.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | governance oversight; awaiting CORE result |
| 10 CORE | READY | execute first mathematical scope gate |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | targeted literature audit only after MASTER authorization |
| 90 MANUSCRIPT | WAIT | no manuscript work before frozen scientific results |

## Current freezes

- Governance rules: STABLE 0.1
- MASTER report snapshot: STABLE v0.2
- Scientific model definition: OPEN
- Numerical specification: OPEN
- Application candidates: NOT YET AUTHORIZED
- Claims / novelty: OPEN

## Freeze check

OK. `research/core/STATUS.md` remains READY and the expected result `research/core/mathematical_scope_gate_0_1.md` is absent. No effect inspection, parameter tuning, objective change, application execution, post-hoc retuning, or scientific branch execution is present. No repository commits occurred after Status Audit 0.4 before this audit.

## Branching check

No unauthorized scientific branch execution detected. APP-1, APP-2, and APP-3 remain PROTECTED / WAIT. LIT and MANUSCRIPT remain WAIT. No additional branch is justified before the CORE scope gate result.

## Branch-independent results

- Governance process 0.1: STABLE.
- MASTER reporting process v0.2: STABLE administrative artifact; no scientific claim.

## Branch-dependent results

None.

## Active blocker

The canonical mathematical scope of the baseline Lighthouse model has not yet been established and frozen. `research/core/STATUS.md` remains READY and `research/core/mathematical_scope_gate_0_1.md` does not exist.

## Rollback points

1. RB-001 Governance Initialization 0.1 — STABLE

No scientific rollback point exists yet.

## Manuscript

No manuscript claim freeze, draft, figure, or supplement is authorized.

## Literature positioning

WAIT. No targeted novelty positioning is authorized before MASTER receives and evaluates the initial CORE gate result.

## Cross-branch integration

Not yet needed; no scientific branch result exists to integrate.

## Next global step

Execute `CORE Mathematical Scope Gate 0.1` in `10 – CORE` by issuing exactly `GO` there.

The task is limited to defining and sourcing the baseline mathematical model, notation, admissible variants for later comparison, analytical validation targets, and explicit exclusions. No JAX implementation, parameter optimization, application benchmarking, learning experiments, or effect-driven model modification is allowed in this gate.

After CORE completes, creates `research/core/mathematical_scope_gate_0_1.md`, updates `research/core/STATUS.md`, and stops, return to MASTER and issue `Status?`.

## STOP

STOP — AWAIT CORE GO
