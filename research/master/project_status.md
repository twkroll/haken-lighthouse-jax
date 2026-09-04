# Lighthouse-JAX — Canonical Project Status

Version: 0.2
Date: 2026-09-04

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

Governance Initialization 0.1 is complete and stable. No scientific result is frozen yet. The first scientific gate is authorized but has not yet been executed in the Git single source of truth.

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
- Scientific model definition: OPEN
- Numerical specification: OPEN
- Application candidates: NOT YET AUTHORIZED
- Claims / novelty: OPEN

## Freeze check

OK. No effect inspection, parameter tuning, objective change, application execution, or post-hoc retuning has occurred. The README-only commit `948dedbc5294fbe864b940060ee6b2053020347f` was reviewed and does not alter the scientific freeze state.

## Branching check

No unauthorized scientific branch execution detected. Application branches remain PROTECTED / WAIT. Literature and manuscript remain WAIT.

## Branch-independent results

- Governance process 0.1: STABLE.

## Branch-dependent results

None.

## Active blocker

The canonical mathematical scope of the baseline Lighthouse model has not yet been established and frozen.

## Rollback points

1. RB-001 Governance Initialization 0.1 — STABLE

## Manuscript

No manuscript claim freeze, draft, figure, or supplement is authorized.

## Cross-branch integration

Not yet needed; no scientific branch result exists to integrate.

## Next global step

Execute `CORE Mathematical Scope Gate 0.1` in `10 – CORE` by issuing `GO` there.

The task is limited to defining and sourcing the baseline mathematical model, notation, admissible variants for later comparison, analytical validation targets, and explicit exclusions. No JAX implementation, parameter optimization, application benchmarking, learning experiments, or effect-driven model modification is allowed in this gate.

After CORE completes and updates Git, return to MASTER and issue `Status?`.

## STOP

STOP — AWAIT CORE GO
