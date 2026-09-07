# Lighthouse-JAX Research Governance

This repository uses a gated research workflow to prevent post-hoc retuning, cherry-picking, uncontrolled branching, and loss of frozen results.

Governance command protocol: `research/master/command_protocol_v0_2.md`.

## Canonical chat / workstream structure

- `00 – MASTER – Projektplan & Status`
- `10 – CORE – Haupttheorie / mathematischer Kern`
- `50 – APP-1 – Computational Neuroscience`
- `60 – APP-2 – Neuromorphic Computing`
- `70 – APP-3 – Differentiable Inference / Temporal Learning`
- `80 – LIT – Literatur & Neuheitspositionierung`
- `90 – MANUSCRIPT – Manuskript & Figuren`

Additional workstreams require explicit MASTER authorization.

## Core workflow

`GATE → FREEZE → EXECUTION → RESULT FREEZE`

A weak, null, or failed result is a valid scientific result. After effect inspection, no parameter retuning, objective replacement, horizon selection, geometry change, or candidate fishing is allowed unless MASTER explicitly opens a new, separately logged branch.

## Frozen-work reuse

`FROZEN / STABLE` scientific artifacts are canonical reusable premises.

A new or replacement chat reconstructs current state from Git, verifies the freeze/dependency chain, and starts at the first unresolved claim. It must not re-derive or re-execute frozen science merely to rebuild conversational context unless the current MASTER prompt explicitly requires an independent check or a concrete contradiction/provenance defect is discovered.

Canonical rule:

`Reconstruct state, not frozen science.`

## Commands

### `GO`
Execute only the currently authorized `Next instruction` of the current workstream after a fresh Git/STATUS check. Use FROZEN/STABLE dependencies as premises. If none exists, or status is WAIT/BLOCKED/FROZEN/RETURN TO MASTER/STOP, do no new scientific work and return to MASTER.

### `RESUME`
Preferred command for a new/replacement chat. Fresh-reconstruct Git state and, if the current workstream is READY with a `Next instruction`, execute that instruction in the same session without redundantly re-deriving frozen dependencies. Otherwise report the exact blocking state.

### `VERIFY-LEGACY`
CORE-only batch verification command. It is executable only when CORE STATUS explicitly authorizes a Legacy Verification Sweep. It executes the full authorized legacy sweep without returning to MASTER between individual legacy versions. It may audit, compare, classify and faithfully replay committed deterministic artifacts where possible, but it may not promote exploratory/post-hoc numerical effects without the required preregistered rerun.

### `Status?`
MASTER reconstructs global status, blockers, freezes, branching, rollback points, manuscript state, and selects exactly one next global step. MASTER should prefer consolidated verification/validation gates over serial micro-gates when existing material can be audited without weakening pre-specification or provenance controls.

### `PDF`
MASTER produces or updates the versioned canonical project report.

Detailed command semantics are frozen administratively in `research/master/command_protocol_v0_2.md`.

## Git as single source of truth

Canonical project state lives under `research/`.

Each workstream has a `STATUS.md` with:

- Current Gate
- Status
- Latest canonical file
- Dependencies
- Next instruction
- STOP boundary

MASTER owns:

- `research/master/STATUS.md`
- `research/master/project_status.md`
- `research/master/decision_branch_log.md`
- versioned task prompts in `research/master/prompts/`

Executed prompts and frozen results are versioned and never silently overwritten.

## Status vocabulary

Typical states: `ACTIVE`, `READY`, `WAIT`, `BLOCKED`, `QUALIFIED`, `COMPLETE`, `STABLE`, `FROZEN`, `PROTECTED`, `FAILED`, `RETURN TO MASTER`.

## Result vocabulary

Application results may be classified as `STRONG`, `WEAK`, `NULL`, or `FAIL` unless a task defines a more specific scheme.

## Rollback discipline

Every important freeze creates a rollback point. Later work may extend but must not rewrite earlier stable rollback points.

## Highest-level rule

If it is unclear whether a new scientific step, simulation, retuning, objective, branch, or manuscript change is authorized: do not proceed.

`STOP — RETURN TO MASTER`
