# CORE Legacy Branch Recovery Input Snapshot 0.1

Date: 2026-09-07
Status: STABLE ADMINISTRATIVE SNAPSHOT / NON-CANONICAL SCIENCE

## Purpose

Preserve the exact legacy CORE working-state input discovered on the non-default branch `core/theory-v0.1` before any recovery, canonicalization, replay, merge, or further scientific execution.

This snapshot freezes provenance and branch identity only. It does **not** freeze, validate, authorize, or canonize any scientific result on the legacy branch.

## Repository state at discovery

- Repository: `twkroll/haken-lighthouse-jax`
- Canonical branch: `main`
- `main` HEAD at discovery: `c24e08cdb5e45f9fcc5f6ae88d671c26966b5efa`
- Legacy branch: `core/theory-v0.1`
- Legacy branch recovery HEAD: `287eae8a86560b78ed94f30a2786243714c33ac0`
- Recovery HEAD message: `CORE v0.26: document trial nuisance and calibration theory`
- Merge base with `main`: `948dedbc5294fbe864b940060ee6b2053020347f`
- Comparison at discovery: `diverged`, legacy branch 133 commits ahead and 34 commits behind `main`.

## Governance discrepancy

At the recovery HEAD, `research/core/STATUS.md` still states:

- Current Gate: `CORE Mathematical Scope Gate 0.1`
- Status: `READY`
- Latest canonical file: none yet
- Next instruction: `research/master/prompts/core_mathematical_scope_gate_0_1.md`

The legacy branch `research/master/STATUS.md` likewise still waits for `CORE Mathematical Scope Gate 0.1` and forbids implementation, parameter search, and further scientific execution before return.

Nevertheless, the branch contains a large downstream body of CORE work, including versioned mathematical, numerical, inference, active-design, JAX/reference, and benchmark artifacts through CORE v0.26.

Therefore this branch is classified for recovery as:

`NON-CANONICAL LEGACY CORE WORKING BRANCH — READ-ONLY RECOVERY INPUT`

## Key late-version anchors

### CORE v0.24

`docs/core/README_v0.24_status.md` and `docs/core/active_pulse_design_v0.24.md` describe chart-safe active pulse experiment design. The recorded next target is a two-probe experiment for identifying the full real two-dimensional q=1 synaptic subspace.

### CORE v0.25

`docs/core/README_v0.25_status.md` and `docs/core/full_q1_two_probe_v0.25.md` extend the active-design program to two complementary chart-safe trials and identify a full two-dimensional latent q=1 plane under a reproducible-preparation assumption.

### CORE v0.26

`docs/core/trial_nuisance_calibration_v0.26.md` introduces trial-specific preparation nuisance and pulse-calibration uncertainty, profiles nuisance directions for shared network parameters, and proposes a hierarchical repeated-trial nuisance model as the next CORE direction.

## Recovery rules

1. Audit the exact commit `287eae8a86560b78ed94f30a2786243714c33ac0`; do not use a moving branch head as the recovery authority.
2. Do not merge, rebase, squash, delete, or rewrite `core/theory-v0.1` during recovery.
3. Do not treat any v0.2–v0.26 statement as canonical merely because it is committed.
4. Do not discard a result merely because it was not integrated into `main`.
5. Distinguish mathematical/source-derived claims, numerical results, implementations, benchmark artifacts, exploratory designs, and interpretation statements.
6. Exact replay of committed reference calculations may be authorized only by the dedicated recovery gate; no tuning, new scans, new designs, or continuation beyond the recovery snapshot is allowed.
7. Any proposed scientific freeze remains a MASTER decision after the recovery report returns.

## Freeze semantics

This administrative snapshot establishes rollback point:

`RB-002 CORE Legacy Recovery Input Snapshot 0.1 — STABLE / NON-CANONICAL SCIENCE`

RB-002 protects the recovery input and provenance. It is **not** a CORE Mathematical Freeze and creates no scientific claim.

## STOP

STOP — RECOVERY INPUT FROZEN; AWAIT AUTHORIZED CORE RECOVERY GATE
