# Lighthouse-JAX Command Protocol v0.2

Date: 2026-09-07
Status: STABLE / MASTER-AUTHORIZED

## Purpose

This protocol removes unnecessary MASTER↔CORE ping-pong and prevents new chats from re-deriving already frozen mathematics merely to rebuild context.

It supplements `PROJECT_GOVERNANCE.md`. Scientific freeze, anti-cherry-picking and STOP rules remain in force.

## Frozen-work reuse principle

`FROZEN / STABLE` scientific artifacts are reusable canonical premises.

A workstream reconstructing context MUST:

1. fresh-read Git identity and current STATUS files;
2. verify required freeze files/rollback points exist and dependencies are consistent;
3. treat their frozen contents as established canonical premises;
4. NOT re-derive or re-execute frozen material merely to regain context;
5. begin at the first unresolved claim or currently authorized gate.

Independent re-derivation of frozen material is performed only when a current MASTER prompt explicitly requires it, or when a concrete contradiction/provenance defect is detected.

## `GO`

Execute only the current workstream's `Next instruction` after a fresh Git/STATUS check.

Use all FROZEN/STABLE dependencies as premises. Do not redundantly reconstruct them unless the active prompt explicitly requires an independent check.

If current status is WAIT/BLOCKED/FROZEN/RETURN TO MASTER/STOP, do no new science.

## `RESUME`

`RESUME` is the preferred command for a new/replacement chat.

On `RESUME` the chat MUST:

1. reconstruct current state directly from Git;
2. read `PROJECT_GOVERNANCE.md`, this protocol, current workstream STATUS, MASTER STATUS, project status, decision log tail, current freeze chain and current prompt;
3. reuse all FROZEN/STABLE science as canonical premises without full re-derivation;
4. if the workstream is READY and has a `Next instruction`, execute that instruction in the same turn/session;
5. if the workstream is not executable, report the exact blocking state and return to MASTER.

Thus `RESUME` replaces the old pattern `reconstruct everything -> restate prior derivations -> GO`.

## `VERIFY-LEGACY`

`VERIFY-LEGACY` is a CORE-only batch verification command and is executable only when CORE STATUS explicitly authorizes a Legacy Verification Sweep.

It MUST fresh-read Git and then execute the entire authorized sweep without returning to MASTER between legacy versions.

The sweep may:

- inventory legacy v0.4–v0.26 claims/artifacts at the frozen recovery SHA;
- compare them against current FROZEN/STABLE canonical theory/results;
- perform claim-by-claim mathematical consistency checks without re-proving already frozen premises;
- perform static code/benchmark provenance checks;
- exact-replay committed deterministic artifacts only where the execution environment and artifact closure permit faithful replay without scientific repair;
- classify unresolved items as replay-needed, preregistered-rerun-needed, source-repair-needed, reject/superseded, or defer.

It MUST NOT:

- promote an exploratory C3 effect merely because a legacy result exists;
- tune parameters, tolerances, objectives, horizons, geometries or success criteria after effect inspection;
- invent missing replay artifacts;
- turn a failed/weak/null legacy check into a success by redesign;
- start new v0.27 science.

The sweep returns one consolidated verification matrix and one proposed minimal queue of genuinely unresolved work.

## `Status?`

MASTER performs a fresh global Git reconstruction. If a returned result can be integrated, MASTER may freeze it and authorize exactly one next global action.

MASTER should prefer consolidated verification/validation gates over serial micro-gates when the underlying scientific material already exists and the consolidation does not weaken pre-specification or provenance controls.

## `PDF`

Unchanged: MASTER updates the canonical versioned project report.

## New-chat rule

A new chat must never infer that lack of conversational memory requires scientific re-derivation. Git freezes are the context handoff.

The canonical rule is:

> Reconstruct state, not frozen science.

