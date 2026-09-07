# Lighthouse-JAX — Canonical Project Status

Version: 1.0
Date: 2026-09-07

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

Governance Initialization 0.1 remains STABLE. A previously unintegrated legacy CORE branch, `core/theory-v0.1`, has now been discovered and frozen as a read-only recovery input at commit `287eae8a86560b78ed94f30a2786243714c33ac0` (`CORE v0.26: document trial nuisance and calibration theory`).

The legacy branch contains a substantial scientific working state through CORE v0.26, including mathematical, numerical, inference, active-design, implementation, benchmark, and JAX/reference artifacts. These artifacts are **not canonical scientific results** because the branch's own `research/core/STATUS.md` remained at `CORE Mathematical Scope Gate 0.1 / READY` and its MASTER status continued to forbid downstream implementation and scientific execution.

MASTER therefore does not merge, discard, or retroactively freeze the legacy branch. Instead, `CORE Recovery & Canonicalization Gate 0.1` is now authorized to reconstruct, classify, and audit the branch before any further scientific execution.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | recovery oversight; awaiting CORE recovery result |
| 10 CORE | READY | execute Recovery & Canonicalization Gate 0.1 only |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | no independent novelty positioning before recovered CORE state is adjudicated |
| 90 MANUSCRIPT | WAIT | no manuscript claims before recovered scientific state is adjudicated and frozen |

## Current freezes

- Governance rules: STABLE 0.1
- MASTER report snapshot: STABLE v0.2 administrative artifact
- Communication briefings: NON-CANONICAL / PRE-CORE
- RB-002 CORE Legacy Recovery Input Snapshot 0.1: STABLE ADMINISTRATIVE SNAPSHOT
- Scientific model definition: OPEN
- Numerical specification: OPEN
- Legacy CORE v0.2–v0.26 scientific claims: NON-CANONICAL / NOT FROZEN
- Application candidates: NOT YET AUTHORIZED
- Claims / novelty: OPEN

## Recovery input

Canonical recovery record:

`research/master/core_legacy_recovery_snapshot_0_1.md`

Frozen recovery input:

- branch: `core/theory-v0.1`
- recovery HEAD: `287eae8a86560b78ed94f30a2786243714c33ac0`
- merge base with `main`: `948dedbc5294fbe864b940060ee6b2053020347f`
- state at discovery: diverged, 133 commits ahead and 34 commits behind `main`

The exact SHA, not a moving branch head, is the recovery authority.

## Branching check

Previous audits inspected the canonical `main` state but did not account for the scientific execution present on `core/theory-v0.1`. Therefore the prior statement that no unauthorized scientific branch execution was detected is now restricted to the then-audited `main` state and is not a complete repository-wide conclusion.

The legacy branch is now classified:

`NON-CANONICAL LEGACY CORE WORKING BRANCH — READ-ONLY RECOVERY INPUT`

It must not be merged, rebased, rewritten, deleted, or continued during the recovery gate.

APP-1, APP-2 and APP-3 remain PROTECTED / WAIT. LIT and MANUSCRIPT remain WAIT.

## Branch-independent results

- Governance process 0.1: STABLE.
- MASTER reporting process v0.2: STABLE administrative artifact; no scientific claim.
- Communication briefings v0.1: NON-CANONICAL / PRE-CORE; no scientific freeze effect.
- Legacy branch recovery provenance snapshot RB-002: STABLE administrative artifact; no scientific claim.

## Branch-dependent working evidence

A substantial non-canonical CORE lineage exists on `core/theory-v0.1` through v0.26.

Late-version anchors include:

- CORE v0.24: chart-safe active pulse experiment design; recorded information/conditioning improvements and a hard event-chart safety rule.
- CORE v0.25: two complementary chart-safe probes for full real q=1 latent-state identifiability under a shared-preparation assumption.
- CORE v0.26: trial-specific preparation nuisance, pulse-calibration ambiguity, nuisance-profiled identifiability of shared parameters, and a proposed hierarchical repeated-trial next direction.

These are working-state findings only until recovery classification and MASTER adjudication.

## Result classifications

No legacy CORE result is currently assigned a canonical STRONG, WEAK, NULL, FAIL, THEOREM freeze, or equivalent result-freeze status.

Recovery Gate 0.1 will classify recovered artifacts into canonicalization classes C1–C5 and distinguish mathematical/source-derived content from numerical, implementation, benchmark, exploratory, inference, and design results.

## Original CORE Mathematical Scope Gate 0.1

The original Scope Gate is **PARKED PENDING RECOVERY** rather than re-executed from scratch.

Recovery Gate 0.1 must determine whether the original scope requirements were satisfied in substance by legacy foundational artifacts and, if so, what can be reconstructed into a canonical scope result without silently accepting downstream legacy science.

## Active blocker

The project currently has two inconsistent histories:

1. canonical `main`, which still lacks a scientific CORE freeze;
2. a substantial legacy CORE working branch through v0.26 whose governance/status chain was not maintained.

No new scientific execution is allowed until this inconsistency is reconstructed and adjudicated.

## Rollback points

1. RB-001 Governance Initialization 0.1 — STABLE
2. RB-002 CORE Legacy Recovery Input Snapshot 0.1 — STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE

RB-002 freezes only recovery provenance and input identity; it is not a scientific CORE freeze.

## Manuscript

WAIT. No manuscript claim freeze, canonical draft, scientific figure, or supplement is authorized from the legacy branch. The existing communication briefings remain non-canonical.

## Literature positioning

WAIT. Targeted source verification needed by CORE Recovery Gate is allowed only as part of recovery provenance/source checking. Independent novelty positioning remains unauthorized.

## Cross-branch integration

Integration is now required but must occur through recovery, not direct merge.

Authorized integration mechanism:

`CORE Recovery & Canonicalization Gate 0.1`

Prompt:

`research/master/prompts/core_recovery_canonicalization_gate_0_1.md`

The gate must reconstruct the legacy lineage, audit original Scope Gate coverage, classify claims and artifacts, perform only exact committed replays where needed, audit design provenance/anti-cherry-picking, and recommend what is directly recoverable, replay-verifiable, requires a fresh preregistered rerun, remains legacy exploratory, or is unresolved.

## Next global step

Execute `CORE Recovery & Canonicalization Gate 0.1` in `10 – CORE – Haupttheorie / mathematischer Kern` by issuing exactly:

`GO`

The recovery input is fixed at `287eae8a86560b78ed94f30a2786243714c33ac0`.

Do not execute the historical v0.26 next step, do not begin v0.27, and do not merge `core/theory-v0.1`.

After CORE creates `research/core/recovery_canonicalization_gate_0_1.md`, updates `research/core/STATUS.md`, and stops, return to MASTER and issue `Status?`.

## STOP

STOP — AWAIT CORE RECOVERY GO
