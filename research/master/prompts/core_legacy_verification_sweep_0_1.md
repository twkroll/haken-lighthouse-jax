# MASTER Prompt — CORE Legacy Verification Sweep 0.1

Date: 2026-09-07
Workstream: `10 – CORE – Haupttheorie / mathematischer Kern`
Command: `VERIFY-LEGACY` or `RESUME` when CORE STATUS points here

## Purpose

Perform one consolidated verification-first audit of the existing legacy CORE material from v0.4 through v0.26 against the current canonical freeze chain, without returning to MASTER between individual legacy versions.

This sweep exists because the scientific material already exists in the frozen legacy recovery snapshot and should not be serially re-derived through micro-gates unless a concrete unresolved claim actually requires it.

## Authoritative inputs

Fresh-read at execution start:

- `PROJECT_GOVERNANCE.md`
- `research/master/command_protocol_v0_2.md`
- `research/core/STATUS.md`
- `research/master/STATUS.md`
- `research/master/project_status.md`
- `research/master/decision_branch_log.md`
- all current RB-004 through RB-010 freeze files
- frozen legacy recovery SHA `287eae8a86560b78ed94f30a2786243714c33ac0`
- `research/core/recovery_canonicalization_gate_0_1.md`

## Reuse rule

All FROZEN/STABLE canonical scientific layers are premises. Do not re-derive them merely to rebuild context.

Only independently check an already frozen statement if:

1. a legacy claim materially conflicts with it;
2. the current claim depends on a qualification not covered by the freeze; or
3. a concrete provenance/implementation inconsistency requires resolution.

## Sweep scope

Audit legacy v0.4–v0.26, including at minimum:

- v0.4 Floquet/symmetry documents and B23–B40 contract;
- v0.5 order-parameter/normal-form theory and contract;
- v0.6–v0.15 numerical bifurcation, codimension-two, invariant-circle, adaptive-delay and global-object layers;
- v0.16–v0.17 JAX packet-queue and graph/batch implementation/scaling;
- v0.18–v0.20 inverse problem, multichart optimizer and latent-state inference;
- v0.21–v0.23 observation/identifiability/transverse-sensor layers;
- v0.24–v0.25 active pulse / two-probe design;
- v0.26 nuisance/calibration mathematics and numerical results.

## Required per-claim / per-artifact classification

For each material unit record:

- legacy version and exact artifact path/blob when available;
- claim/result type: source claim / theorem-lemma-proposition candidate / algorithm / implementation / benchmark / numerical effect / interpretation / open question;
- relation to current canonical freezes;
- verification route;
- result class from:
  - `ALREADY CANONICAL`
  - `MATHEMATICALLY VERIFIED IN SWEEP`
  - `STATICALLY CONSISTENT`
  - `EXACT REPLAY PASS`
  - `EXACT REPLAY FAIL`
  - `REPLAY PENDING — ENVIRONMENT/ARTIFACT GAP`
  - `PREREGISTERED RERUN REQUIRED`
  - `SOURCE/PROVENANCE REPAIR REQUIRED`
  - `SUPERSEDED / REJECT`
  - `DEFER / OPEN QUESTION`
- recovery class C1/C2/C3/C4/C5 where applicable;
- whether it is eligible for a later freeze without new scientific design;
- whether it requires a new preregistered validation contract.

## Exact replay permission

Exact replay of committed deterministic legacy scripts/benchmarks is allowed only when:

- the exact artifact identity is known;
- required dependencies can be reconstructed without scientific refactoring;
- no parameter, objective, tolerance, horizon, geometry or success rule is changed;
- any failure is preserved.

If faithful replay cannot be established, do not manually reconstruct an approximate substitute and call it replay. Mark `REPLAY PENDING — ENVIRONMENT/ARTIFACT GAP`.

## C3 / exploratory rule

Legacy numerical effects with exploratory or post-hoc design provenance remain hypothesis-generating even if their stored arithmetic is internally consistent.

For v0.6–v0.15 scientific numerical effects and v0.21–v0.26 optimized/effect-selected results, the sweep may verify mathematics, implementation mechanics, artifact integrity and stored arithmetic, but it must classify confirmatory scientific promotion as `PREREGISTERED RERUN REQUIRED` unless a prior frozen pre-specification genuinely covers the effect.

No optimized pulse/sensor/subset discovered from legacy effects may be silently treated as preregistered.

## Special v0.4 rule

RB-010 already freezes the narrow v0.4 mathematical Floquet/symmetry layer. Do not rederive it. Audit B23–B40 only as a candidate validation inventory and determine which tests are still useful, duplicative, ill-posed, or require fresh contract specification.

No actual Lighthouse multiplier/root/stability search is authorized by this sweep unless it is an exact replay of a previously committed deterministic artifact under the exact replay rule; even then it remains recovery verification, not automatically a canonical scientific result.

## Special v0.24–v0.26 rule

Treat the existing active-design and nuisance/calibration material as high-value hypothesis/design generators. Verify formulas and artifact consistency aggressively, but do not promote the optimized numerical effect sizes as confirmatory evidence.

For v0.26, separately audit:

- nuisance projection algebra `R_r=(I-P_{N_r})J_{s,r}`;
- the structural self-calibration argument and its assumptions;
- the absence of matching benchmark JSON/status closure at the recovery snapshot.

## Deliverable

Create:

`research/core/legacy_verification_sweep_0_1.md`

It must contain:

1. Git/provenance identity;
2. freeze-chain reuse statement;
3. full legacy artifact inventory v0.4–v0.26;
4. consolidated claim/result verification matrix;
5. exact replay attempts and environment limitations;
6. contradictions/repairs against canonical freezes;
7. C1–C5 disposition;
8. explicit list of items now effectively closed by existing canonical work;
9. explicit list of genuinely unresolved mathematical claims;
10. explicit list of exact-replay-needed implementation claims;
11. explicit list of C3 preregistered-rerun-needed scientific effects;
12. rejected/superseded/deferred items;
13. minimal recommended next-work queue ordered by scientific leverage and dependency;
14. overall decision `PASS`, `CONDITIONAL`, or `FAIL` for completion of the verification sweep itself;
15. proposed freeze candidates, but no automatic promotion beyond what MASTER can review without new execution;
16. STOP.

## Gate success criterion

`PASS` means the existing legacy corpus has been comprehensively classified against the current canonical freeze chain so MASTER can stop serially rediscovering what is already known and can authorize only the genuinely unresolved work.

PASS does **not** mean all legacy science is true or canonical.

## Forbidden

- no tuning after effect inspection;
- no new optimization/search designed to rescue legacy results;
- no new v0.27 science;
- no application execution;
- no novelty claim;
- no manuscript claim freeze;
- no return to MASTER between individual legacy versions.

## STOP boundary

After writing `research/core/legacy_verification_sweep_0_1.md`, update CORE STATUS to `RETURN TO MASTER` and stop.

STOP — RETURN TO MASTER ONLY AFTER THE FULL V0.4–V0.26 SWEEP IS COMPLETE
