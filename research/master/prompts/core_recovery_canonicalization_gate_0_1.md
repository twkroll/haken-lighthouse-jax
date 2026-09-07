# CORE Recovery & Canonicalization Gate 0.1

## Purpose

Recover, audit, and classify the legacy CORE working state contained in `core/theory-v0.1` without silently canonizing it, discarding it, or continuing its scientific program.

The exact recovery input is frozen by `research/master/core_legacy_recovery_snapshot_0_1.md` at commit:

`287eae8a86560b78ed94f30a2786243714c33ac0`

Do not substitute a later moving branch head.

## Background

The canonical `main` branch still records `CORE Mathematical Scope Gate 0.1` as READY and unexecuted. The legacy branch nevertheless contains 133 branch-specific commits beyond merge base `948dedbc5294fbe864b940060ee6b2053020347f`, including mathematical, numerical, implementation, benchmark, inference, and active-experiment-design artifacts through CORE v0.26.

At the recovery snapshot, the legacy branch's own `research/core/STATUS.md` was never advanced beyond Scope Gate 0.1 / READY. Therefore the branch is scientific working evidence, not a canonical result lineage.

## Authorized scope

### A. Lineage reconstruction

1. Reconstruct the commit lineage from merge base `948dedbc5294fbe864b940060ee6b2053020347f` to recovery head `287eae8a86560b78ed94f30a2786243714c33ac0`.
2. Build a version/artifact manifest for the complete recovered CORE sequence, including intermediate versions and unversioned foundational files.
3. Identify the relationship among documentation, reference scripts, benchmark JSON files, and status summaries.

### B. Scope-Gate recovery

4. Determine whether `CORE Mathematical Scope Gate 0.1` was satisfied **in substance** somewhere in the legacy artifacts, especially foundational files such as `docs/core/mathematical_core.md`, `docs/core/derivations_v0.2.md`, and related source/notation material.
5. Map recovered baseline content against every required item of the original Scope Gate 0.1 prompt:
   - Scope
   - Source map
   - Canonical equations and notation
   - Event / spike definition
   - Synaptic and delay definitions
   - Baseline assumptions
   - Variant registry
   - Analytical validation targets
   - Explicit exclusions
   - Gate decision material
   - Proposed freeze contents
   - Open questions
6. Do not retroactively declare Scope Gate 0.1 PASS. Report whether the recovered material is sufficient, insufficient, or requires repair; MASTER decides canonical acceptance.

### C. Scientific and governance classification

7. For each recovered CORE version/artifact, classify its content into one or more of:
   - SOURCE-DERIVED
   - DERIVATION HERE
   - MATHEMATICAL CLAIM
   - NUMERICAL RESULT
   - IMPLEMENTATION ARTIFACT
   - BENCHMARK / REFERENCE OUTPUT
   - EXPERIMENT-DESIGN RESULT
   - INFERENCE RESULT
   - INTERPRETATION
   - OPEN QUESTION
8. Record the epistemic status where appropriate:
   - THEOREM / PROVED
   - PROPOSITION
   - LEMMA
   - ASSUMPTION
   - CONJECTURE
   - INTERPRETATION
   - OPEN QUESTION
9. Record governance provenance for each major version: what the canonical `main` authorization allowed at that time, whether the artifact remained within that scope, and whether required status/STOP transitions were performed.
10. Treat the legacy branch as `NON-CANONICAL LEGACY CORE WORKING STATE` throughout this gate.

### D. Reproducibility audit

11. Exact replay of already committed reference calculations and benchmarks is authorized solely for recovery verification.
12. Exact replay means:
   - use the committed recovery-snapshot code/configuration without parameter modification;
   - no tuning;
   - no new parameter scan;
   - no new pulse/design search;
   - no objective replacement;
   - no horizon/resolution change selected after inspecting effects;
   - no continuation to a new scientific question.
13. Record whether each replayed result reproduces its committed benchmark within the artifact's own stated tolerance, if such a tolerance exists.
14. If a script is incomplete, empty, non-runnable, environment-dependent, or lacks enough information for exact replay, classify that limitation explicitly. Do not repair the science during this gate.

### E. Anti-cherry-picking / design provenance audit

15. For versions involving continuation, bifurcation search, active pulses, observation design, inverse inference, or experimental optimization, determine from the committed lineage whether model choices, objectives, geometry, pulse families, constraints, horizons, and success criteria were fixed before effect inspection or were adapted afterward.
16. Do not infer misconduct from missing records. Classify provenance as:
   - PRE-SPECIFIED / TRACEABLE
   - PARTIALLY TRACEABLE
   - NOT TRACEABLE FROM RECOVERY SNAPSHOT
   - CLEARLY POST-HOC / EXPLORATORY
17. Results lacking sufficient pre-specification may remain scientifically interesting working evidence but cannot be promoted directly to a frozen confirmatory result.

### F. Canonicalization recommendation

18. Assign each major recovered artifact/result one recommendation class:
   - `C1 — DIRECTLY RECOVERABLE`: mathematically/source-wise auditable and suitable for proposed canonical adoption without new scientific execution;
   - `C2 — REPLAY-VERIFIABLE`: suitable only after exact committed replay succeeds;
   - `C3 — REQUIRES PREREGISTERED RERUN`: scientifically valuable but design/provenance does not support direct canonical result freeze;
   - `C4 — LEGACY EXPLORATORY`: retain as historical working evidence, do not use as frozen evidence;
   - `C5 — UNRESOLVED`: insufficient information to classify.
19. Distinguish canonicalization of **definitions/derivations** from canonicalization of **numerical effect claims**. A sound mathematical derivation may be recoverable even when a downstream numerical experiment requires a fresh preregistered rerun.
20. Propose a minimal ordered canonicalization path that preserves as much valid work as possible while restoring governance.

## Required late-version anchors

Audit explicitly at least:

- CORE v0.24: `docs/core/README_v0.24_status.md`, `docs/core/active_pulse_design_v0.24.md`, related benchmark/reference assets.
- CORE v0.25: `docs/core/README_v0.25_status.md`, `docs/core/full_q1_two_probe_v0.25.md`, related benchmark/reference assets.
- CORE v0.26: `docs/core/trial_nuisance_calibration_v0.26.md`, related benchmark/reference assets, and the stated next hierarchical repeated-trial direction.

The former next-step language in these artifacts is historical evidence only. **Do not execute v0.27 or any hierarchical experiment in this gate.**

## Explicitly forbidden

- No merge/rebase/squash/delete/rewrite of `core/theory-v0.1`.
- No continuation beyond recovery head `287eae8a86560b78ed94f30a2786243714c33ac0`.
- No new theoretical branch.
- No new pulse design or active experiment design.
- No new parameter fitting or optimization.
- No new parameter scans.
- No new JAX implementation except what is strictly necessary to execute an exact committed replay; do not improve or refactor scientific code.
- No application execution.
- No novelty claim.
- No manuscript claim freeze.
- No promotion of a legacy result to canonical/frozen status without MASTER review.

## Deliverable

Create:

`research/core/recovery_canonicalization_gate_0_1.md`

It must contain at minimum:

1. Recovery input identity and hashes
2. Commit/version lineage
3. Artifact manifest
4. Original Scope Gate 0.1 substantive-coverage matrix
5. Mathematical/source-derived claim inventory
6. Numerical/implementation/benchmark inventory
7. Governance provenance audit
8. Exact-replay audit and limitations
9. Anti-cherry-picking/design-provenance audit
10. Detailed treatment of v0.24, v0.25, v0.26
11. Canonicalization recommendation classes C1–C5
12. Proposed minimal canonicalization sequence
13. Items that must be freshly preregistered/rerun
14. Items that can be retained only as legacy exploratory evidence
15. Open questions
16. Gate decision: PASS / FAIL / CONDITIONAL
17. Proposed next MASTER decision(s), without executing them
18. STOP

Then update `research/core/STATUS.md` to `RETURN TO MASTER` (or `BLOCKED` if recovery cannot be completed) and return to MASTER.

## Gate success criterion

PASS means the legacy working state has been sufficiently reconstructed and classified for MASTER to make an informed canonicalization decision. PASS does **not** mean that v0.2–v0.26 scientific claims are accepted or frozen.

## STOP boundary

STOP after the recovery deliverable and CORE STATUS update.

Do not resume the legacy next step, do not execute v0.27, and do not merge the branch.

STOP — RETURN TO MASTER
