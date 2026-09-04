# Lighthouse-JAX — MASTER Project Report

Version: **0.2**  
Date: **2026-09-04**  
Repository: `twkroll/haken-lighthouse-jax`  
Canonical project status: **v0.3**  
Active scientific gate: **CORE Mathematical Scope Gate 0.1**  
Last stable rollback: **RB-001 Governance Initialization 0.1**

## Governance note

This report is a versioned snapshot of the canonical Git state. It introduces no new theory, no new scientific result, and no new scientific freeze. Non-authorized content remains explicitly OPEN, WAIT, PROTECTED, READY, or NONE YET.

## Executive Summary

Governance Initialization 0.1 is STABLE. The scientific core remains OPEN because `CORE Mathematical Scope Gate 0.1` has not yet been executed. Therefore JAX implementation, parameter studies, application benchmarking, targeted novelty positioning, and manuscript work remain blocked.

MASTER Status Audit 0.3 confirmed that changes since the previous audit were restricted to MASTER/reporting bookkeeping. No effect inspection, retuning, objective change, application execution, or unauthorized scientific branch execution was detected.

The single authorized next scientific action remains: switch to `10 – CORE – Haupttheorie / mathematischer Kern` and issue exactly `GO`. CORE must then create `research/core/mathematical_scope_gate_0_1.md`, update `research/core/STATUS.md`, and stop with `STOP — RETURN TO MASTER`.

## Central research question

> Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Workstream status

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | governance oversight; awaiting CORE result |
| 10 CORE | READY | execute first mathematical scope gate |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | targeted literature audit only after MASTER authorization |
| 90 MANUSCRIPT | WAIT | no manuscript work before frozen scientific results |

## Theoretical and mathematical freeze status

The project architecture currently distinguishes four planned layers:

1. historical mathematical core;
2. precise mathematical reconstruction;
3. modern extensions such as graph formulations, continuum limits, delays, noise, plasticity, and differentiable approximations;
4. reproducible, vectorized, accelerator-ready JAX implementation.

These layers are project architecture, not frozen scientific claims.

### OPEN mathematical content

The project has not yet frozen a canonical equation set, state definition, threshold function, synaptic kernel, or delay convention. Earlier chat ideas and README descriptions do not replace the missing CORE gate.

The only currently stable mathematical process statement is the governance sequence:

`Gate → Freeze → Execution → Result Freeze`

For the current project phase:

`CORE Mathematical Scope Gate 0.1 → CORE Mathematical Freeze 0.1 → later Numerical Specification`

The set of project-internal frozen CORE scientific results remains empty: `R_CORE,frozen = ∅`.

## CORE scope and validation targets

CORE result status: **NONE YET**. The required gate result file does not yet exist.

The authorized CORE gate must:

- distinguish primary Haken formulations from later reformulations;
- define notation for state, phase evolution, spike events, synaptic activation, coupling, thresholds, and delays;
- state the minimum baseline model for later numerical reproduction;
- register admissible variants without selecting by observed effect strength;
- distinguish source-derived statements, project assumptions, conjectures, and open questions;
- record analytical validation targets only where source-supported.

Potential validation categories to be assessed by CORE include synchronization, phase locking, delay effects, waves, bumps, stability, and continuum limits.

## Repository reference candidates

The current README lists the following core-reference candidates. This report does not constitute a completed literature audit:

1. H. Haken, *Quasi-discrete dynamics of a neural net: The Lighthouse model*, Discrete Dynamics in Nature and Society 4 (2000), 187–200. DOI: 10.1155/S1026022600000182.
2. H. Haken, *Phase Locking in the Lighthouse Model of a Neural Net with Several Delay Times*, Progress of Theoretical Physics Supplement 139 (2000), 96–111. DOI: 10.1143/PTPS.139.96.
3. H. Haken, *Brain Dynamics: Synchronization and Activity Patterns in Pulse-Coupled Neural Nets with Delays and Noise*, Springer (2002).
4. S. Coombes, *Revisiting the Haken Lighthouse model*, European Physical Journal Special Topics, version of record 2025, volume 235 (2026), 4571–4593. DOI: 10.1140/epjs/s11734-025-01841-3.
5. S. Coombes, R. Thul, S. Ruschel, R. Nicks, *Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks*, arXiv:2606.21508 (2026).

No SAME/CLOSE/RELATED classification or N0–N4 novelty level is frozen.

## Application branches

### APP-1 Computational Neuroscience

Status: **PROTECTED / WAIT**. Dependencies: CORE Mathematical Freeze plus later MASTER application gate. No candidate, parameter set, objective, execution, or result is frozen.

### APP-2 Neuromorphic Computing

Status: **PROTECTED / WAIT**. No hardware, energy, latency, or performance execution is authorized.

### APP-3 Differentiable Inference / Temporal Learning

Status: **PROTECTED / WAIT**. No loss, dataset, surrogate-gradient rule, event-differentiation method, or learning experiment is frozen.

## Literature branch

Status: **WAIT**. No targeted novelty audit is authorized before MASTER receives and evaluates the initial CORE gate result.

## Manuscript branch

Status: **WAIT**. No Claim Freeze, draft, figure, or supplement is authorized.

## Stable results and outcomes

### Branch-independent

- Governance Process 0.1 — STABLE.
- Git repository as Single Source of Truth — STABLE.
- MASTER Reporting Process v0.1 — STABLE administrative artifact; no scientific claim.
- MASTER Status Audit 0.3 — STABLE.

### Branch-dependent

None.

### STRONG / WEAK / NULL / FAIL

None yet. No frozen scientific execution has occurred.

## Freeze check

Status: **OK**.

No effect-guided parameter selection, post-hoc objective selection, parameter retuning, horizon switching, application execution, or omission of weak/null results has been documented.

## Branching check

Status: **OK**.

No unauthorized scientific branching is detected. No new branch is justified before the CORE scope-gate result.

## Rollback points

- **RB-001 Governance Initialization 0.1 — STABLE**.

No scientific rollback point exists yet.

## Decision & Branch Log summary

- DEC-001 — Governance prompt adopted — STABLE.
- DEC-002 — Git repository is Single Source of Truth — STABLE.
- DEC-003 — Workstreams 00/10/50/60/70/80/90 authorized — STABLE.
- DEC-004 — Application workstreams remain PROTECTED / WAIT until MASTER gate — FROZEN.
- DEC-005 — First scientific task is CORE Mathematical Scope Gate 0.1 — ACTIVE.
- DEC-006 — MASTER Status Audit 0.2; no CORE execution and no freeze violation — STABLE.
- DEC-007 — MASTER PDF Snapshot v0.1 generated without changing scientific state — STABLE.
- DEC-008 — MASTER Status Audit 0.3; CORE remains READY and no scientific branch execution detected — STABLE.

## Blocker and roadmap

Active blocker: the canonical mathematical scope of the baseline Lighthouse model has not yet been established and frozen.

Roadmap:

1. execute `CORE Mathematical Scope Gate 0.1`;
2. return to MASTER with `Status?`;
3. MASTER audits the gate result and decides whether `CORE Mathematical Freeze 0.1` can be authorized;
4. only afterward may Numerical / Structural Qualification and Pilot Specification be considered;
5. literature positioning follows a result freeze, not effect selection;
6. manuscript work follows frozen claims.

## Version history

- **v0.1** — based on canonical project status v0.2; first MASTER PDF snapshot.
- **v0.2** — based on canonical project status v0.3; incorporates Status Audit 0.3, reporting state, and updated version history. Scientific state remains unchanged.

## Rendered artifact manifest

Generated deliverables for v0.2:

- `haken_lighthouse_jax_master_report_v0.2.pdf`
- `haken_lighthouse_jax_master_report_current.pdf`

SHA-256 for both rendered PDFs at generation time:

`556c401d6014a7c4bfd1bcee509183a3fe3cbaa8c558af108d6b109534402a20`

Visual verification: 9 A4 pages rendered successfully; no visible clipping or overlapping text detected.

## Next global step

Switch to `10 – CORE – Haupttheorie / mathematischer Kern` and issue exactly:

`GO`

After CORE stops and updates Git, return to MASTER and issue:

`Status?`

**STOP — AWAIT CORE GO**
