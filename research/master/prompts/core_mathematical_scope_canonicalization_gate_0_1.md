# CORE Mathematical Scope Canonicalization Gate 0.1

## Purpose

Reconstruct and formally complete the originally missing `CORE Mathematical Scope Gate 0.1` deliverable using only C1-eligible foundational material recovered from the frozen legacy CORE snapshot, with precise primary-source provenance and independent mathematical verification.

This gate follows `CORE Recovery & Canonicalization Gate 0.1` PASS. It does **not** promote, replay, rerun, or continue the downstream legacy program.

## Authoritative inputs

Canonical governance / recovery inputs:

- `PROJECT_GOVERNANCE.md`
- `research/master/core_legacy_recovery_snapshot_0_1.md`
- `research/core/recovery_canonicalization_gate_0_1.md`
- original prompt: `research/master/prompts/core_mathematical_scope_gate_0_1.md`

Frozen legacy recovery input:

- exact commit: `287eae8a86560b78ed94f30a2786243714c33ac0`
- branch name for navigation only: `core/theory-v0.1`

Primary recovered foundational candidates:

- `docs/core/mathematical_core.md`
- `docs/core/derivations_v0.2.md`
- `docs/core/research_program.md` only where needed to identify historical scope/variants/open questions

Do not substitute a later moving legacy branch head.

## Authorized scope

### A. Primary-source provenance repair

1. Build a precise source map for every baseline statement proposed for canonical adoption.
2. Prefer primary Haken sources and authoritative later mathematical reformulations.
3. For each source-derived equation/definition, record enough location information to distinguish:
   - Haken original formulation;
   - later reformulation / reconstruction;
   - project canonicalization or extension.
4. Do not infer equivalence merely from similar notation. State whether equivalence is proved, source-stated, or only project interpretation.
5. No novelty positioning is authorized.

### B. Canonical baseline reconstruction

6. Produce exactly one proposed canonical baseline containing:
   - graph/network objects;
   - neuron phase/state variables;
   - phase evolution / response function;
   - spike/event definition;
   - spike counter / reset or section-crossing convention;
   - synaptic activation / kernel definition;
   - coupling convention;
   - fixed delay convention;
   - admissibility/transversality assumptions needed for regular events;
   - units/scaling/normalization conventions where required.
7. Separate baseline from variants. Do not choose a variant based on downstream effect strength from v0.3–v0.26.
8. Produce a formal variant registry covering at minimum alternative reset conventions, response families, exponential vs alpha kernels, fixed vs later adaptive-delay semantics, and external drive/project extensions where supported.
9. Produce a single explicit assumptions table.
10. Produce a single explicit exclusions list that restores the missing pre-execution boundary of the original Scope Gate.

### C. Independent mathematical verification of C1 candidates

11. Re-derive line by line, independently of branch-local COMPLETE labels, the C1-eligible elementary v0.2 results proposed for inclusion, including where applicable:
   - alpha-kernel state-space equivalence and jump normalization;
   - periodic alpha-kernel comb identity;
   - isolated-clock / autapse period relations;
   - basic phase-locked self-consistency identities;
   - first-hitting/admissibility conditions;
   - elementary event-time perturbation formula under transversality if needed as a validation target.
12. For each retained result assign one of:
   - THEOREM / PROVED
   - PROPOSITION
   - LEMMA
   - ASSUMPTION
   - CONJECTURE
   - INTERPRETATION
   - OPEN QUESTION
13. Also tag provenance:
   - SOURCE-DERIVED
   - DERIVATION HERE
   - PROJECT ASSUMPTION
   - PROJECT INTERPRETATION
   - OPEN
14. If a recovered derivation depends on an unverified downstream numerical fact or on v0.3+ theory, omit it from the proposed baseline freeze and record it as deferred.

### D. Original Scope Gate completion

15. Map the reconstructed deliverable explicitly against every requirement of `core_mathematical_scope_gate_0_1.md`:
   - Scope
   - Source map
   - Canonical equations and notation
   - Event / spike definition
   - Synaptic and delay definitions
   - Baseline assumptions
   - Variant registry
   - Analytical validation targets
   - Explicit exclusions
   - Gate decision
   - Proposed CORE Mathematical Freeze 0.1 contents if PASS
   - Open questions
   - STOP
16. Analytical validation targets may cite recovered downstream topics only as future targets; do not accept their legacy numerical results as validation evidence.

## Explicitly forbidden

- No merge/rebase/squash/delete/rewrite of `core/theory-v0.1`.
- No scientific execution from legacy v0.3–v0.26.
- No exact benchmark replay in this gate.
- No numerical continuation, bifurcation search, parameter scan, optimizer run, pulse design, observation design, inference benchmark, noise audit, or effect-size re-evaluation.
- No JAX implementation work.
- No v0.27 or hierarchical many-trial work.
- No application execution.
- No literature novelty positioning.
- No manuscript claim freeze.
- No direct promotion of branch-local COMPLETE / VERIFIED / CERTIFIED labels.

## Deliverable

Create:

`research/core/mathematical_scope_canonicalization_gate_0_1.md`

It must contain at minimum:

1. Scope and recovery provenance
2. Precise primary-source map
3. Original-vs-reformulation-vs-project distinction
4. Canonical baseline equations and notation
5. Event / spike / reset convention
6. Synaptic kernel and fixed-delay definitions
7. Baseline assumptions table
8. Formal variant registry
9. Independently verified C1 derivations with epistemic labels
10. Analytical validation targets
11. Explicit exclusions
12. Original Scope Gate coverage matrix
13. Deferred legacy material
14. Gate decision: PASS / FAIL / CONDITIONAL
15. Proposed `CORE Mathematical Freeze 0.1` contents if PASS
16. Open questions
17. Proposed next MASTER decision(s), without executing them
18. STOP

Then update `research/core/STATUS.md` to `RETURN TO MASTER` (or `BLOCKED` if the gate cannot be completed) and return to MASTER.

## Gate success criterion

PASS means the original Scope Gate has now been reconstructed in a governance-compliant, source-audited, mathematically checked form sufficient for MASTER to decide whether to authorize `CORE Mathematical Freeze 0.1`.

PASS does **not** freeze the model automatically and does not validate any v0.3–v0.26 numerical or implementation result.

## STOP boundary

STOP after the deliverable and CORE STATUS update.

Do not begin replay, implementation, active experiment design, or further theory.

STOP — RETURN TO MASTER
