# CORE v0.3 Continuation Theory Canonicalization Gate 0.1

## Authority

Authorized by MASTER after establishment of:

- RB-004 `CORE Mathematical Freeze 0.1`;
- RB-005 `CORE Benchmark Contract Freeze 0.1`;
- RB-006 `CORE v0.2 Benchmark Result Freeze 0.1`.

The legacy branch `core/theory-v0.1` remains read-only recovery evidence. Its frozen recovery head is:

`287eae8a86560b78ed94f30a2786243714c33ac0`

## Objective

Canonicalize only the mathematically recoverable v0.3 continuation-theory layer before any v0.3 numerical continuation/bifurcation execution.

The gate must independently audit and, where justified, re-derive the mathematical claims recovered primarily from:

- `docs/core/continuation_bifurcations_v0.3.md` at the frozen recovery head;
- `docs/core/continuation_contract_v0.3.md` only as a registry of later validation ideas, not as already accepted science.

## Required mathematical scope

At minimum:

1. reconstruct the normalized phase-locked coordinate system and its relation to the frozen v0.2 dimensional-offset formulation;
2. verify the global phase/time-translation gauge treatment and the use of unwrapped internal phase coordinates;
3. derive the normalized phase-locked branch equations `F(z,p)=0` from the RB-004/RB-006 baseline;
4. independently verify the exact branch-Jacobian formulas with respect to normalized phase coordinates;
5. independently verify the period derivative, including all explicit and implicit `T` dependence and conditions under which delay terms are held fixed physically;
6. state the smooth-chart assumptions required for these derivatives and identify arrival, threshold, event-grazing and wrapped-chart boundaries where the formulas do not apply directly;
7. formally separate:
   - existence singularities of the branch equations,
   - dynamical stability changes of the event/spike-time dynamics,
   - hybrid/event-chart singularities;
8. identify which legacy v0.3 claims are C1 directly recoverable mathematics, C2 replay-verifiable computational claims, C3 preregistered-rerun claims, C4 exploratory only, or C5 unresolved;
9. inspect legacy benchmark ideas B11 onward only to determine which future validation contracts would be needed. Do not execute them;
10. define explicit exclusions and a proposed narrow freeze package if the mathematical audit passes.

## Epistemic labels

Use only the project labels:

- THEOREM / PROVED
- PROPOSITION
- LEMMA
- ASSUMPTION
- CONJECTURE
- INTERPRETATION
- OPEN QUESTION

Also distinguish:

- SOURCE-DERIVED
- DERIVATION HERE
- PROJECT ASSUMPTION
- PROJECT INTERPRETATION
- OPEN

No legacy label such as COMPLETE, VERIFIED or CERTIFIED is evidentiary by itself.

## Forbidden execution

This gate must not:

- run numerical continuation;
- search for Lighthouse folds, pitchforks or bifurcation points;
- execute B11 or later benchmark cases;
- import stored v0.3 numerical locations as scientific evidence;
- run parameter scans;
- inspect/select effects for strength;
- execute Floquet spectra beyond purely algebraic definitions needed for separation of concepts;
- execute normal-form fitting;
- execute v0.4+ legacy work;
- continue JAX/production implementation;
- execute inference, observation design or active experiment design;
- execute v0.27;
- open application, novelty or manuscript work.

## Anti-cherry-picking boundary

Any future numerical v0.3 validation must receive its own MASTER-authorized pre-execution contract. This gate may design a registry of candidate checks but may not select test points or success thresholds after observing new numerical effects.

## Required deliverable

Create:

`research/core/v0_3_continuation_theory_canonicalization_gate_0_1.md`

It must contain at minimum:

1. provenance/input identity;
2. legacy v0.3 claim inventory;
3. canonical notation and coordinate map;
4. independent derivation of branch equations;
5. independent branch-Jacobian derivation;
6. period-derivative audit;
7. gauge/invariance audit;
8. smooth-chart and hybrid-boundary conditions;
9. existence-vs-stability-vs-hybrid singularity taxonomy;
10. C1–C5 classification table for v0.3 material;
11. deferred numerical/benchmark registry;
12. explicit exclusions;
13. gate decision PASS / FAIL / CONDITIONAL;
14. proposed contents of a narrow `CORE v0.3 Continuation Theory Freeze 0.1` if PASS;
15. open questions;
16. STOP.

Then update `research/core/STATUS.md` to RETURN TO MASTER or BLOCKED and stop.

## STOP boundary

After the deliverable and CORE STATUS update:

`STOP — RETURN TO MASTER`

No numerical continuation, no benchmark execution, no v0.4+ science and no second gate.
