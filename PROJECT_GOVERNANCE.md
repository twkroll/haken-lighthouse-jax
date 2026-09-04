# Lighthouse-JAX Research Governance

This repository uses a gated research workflow to prevent post-hoc retuning, cherry-picking, uncontrolled branching, and loss of frozen results.

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

## Commands

### `GO`
Execute only the currently authorized `Next instruction` of the current workstream. If none exists, or status is WAIT/BLOCKED/FROZEN/RETURN TO MASTER/STOP, do no new scientific work and return to MASTER.

### `Status?`
MASTER reconstructs global status, blockers, freezes, branching, rollback points, manuscript state, and selects exactly one next global step.

### `PDF`
MASTER produces or updates the versioned canonical project report.

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
