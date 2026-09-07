# CORE v0.27 Hierarchical Repeated-Trial Execution Gate 0.1

## Purpose

Execute the first genuinely new v0.27 hierarchical repeated-trial experiment exactly under RB-013 and RB-014. This gate is effect-bearing. It may return IMPLEMENTATION FAIL/BLOCKED, SCIENTIFIC FAIL, SCIENTIFIC CONDITIONAL, or SCIENTIFIC PASS. No result may be rescued by post-output redesign.

## Mandatory fresh-read inputs

Before execution, read and verify current Git identity plus at minimum:

- `PROJECT_GOVERNANCE.md`
- `research/core/STATUS.md`
- `research/master/STATUS.md`
- `research/master/project_status.md`
- `research/master/decision_branch_log.md`
- `research/core/mathematical_freeze_0_1.md` (RB-004)
- `research/core/consolidated_c1_theory_freeze_0_1.md` (RB-012)
- `research/core/v0_27_hierarchical_repeated_trial_scope_freeze_0_1.md` (RB-013)
- `research/core/v0_27_hierarchical_repeated_trial_execution_contract_freeze_0_1.md` (RB-014)
- frozen source contract `research/core/v0_27_hierarchical_repeated_trial_execution_contract_canonicalization_gate_0_1.md`.

Reuse frozen premises. Do not re-derive them merely to reconstruct context.

## Frozen execution rule

Execute RB-014 exactly. Do not change after observing any C2 or scientific output:

- graph/model constants or truth;
- parameter/hyperparameter boxes;
- preparation scales;
- R, H, noise or missingness;
- stochastic dataset count or seeds;
- minimal-data, timeout or event-budget rules;
- optimizer, derivative, chart/rerecording, Hessian/logdet or uncertainty rules;
- starts, tolerances, iteration/evaluation budgets;
- C2 membership, tolerances or negative controls;
- scientific metrics, thresholds, failure limits or decision hierarchy.

No rescue cases, seed replacement, trial regeneration, tuning, extra starts, tolerance relaxation, alternative inference objective, active pulse, sensor design, or legacy C3 substitution is permitted.

## Phase A — mandatory C2 implementation validation

1. Capture exact environment metadata before validation: Python, NumPy, SciPy, JAX, jaxlib, CPU/backend and relevant deterministic configuration/hash.
2. Implement/use the fresh canonical execution path described by RB-014. Do not import legacy C2 code unless MASTER has separately authorized an implementation-provenance change; none is currently authorized.
3. Execute C2-27-01 through C2-27-08 in the frozen order and retain all numeric errors and negative-control outcomes.
4. Do not create any RNG object for the 32 scientific datasets before all eight C2 checks have passed.
5. If any C2 check fails scientifically/technically under the frozen contract, stop before science and classify the gate `IMPLEMENTATION FAIL / BLOCKED`. Preserve the failure. Do not repair by changing scientific or validation specification.
6. A genuine clerical/software-plumbing defect may be corrected only if the frozen scientific/C2 contract is unchanged. Document the defect, correction, invalidated prior output and unchanged-contract rerun. Any material contract change requires RETURN TO MASTER without science.

## Phase B — scientific execution, only if all C2 checks PASS

1. Create the 32 stochastic datasets exactly with the frozen PCG64DXSM seed mapping and generation order.
2. Never regenerate an awkward/failed dataset or replace a seed.
3. Apply the frozen mask rules, physical validity rules and failure labels exactly.
4. Run the frozen per-trial mode solver and five-parameter Laplace-marginal inference exactly for each eligible dataset.
5. Compute the conservative free-nuisance information diagnostics, hierarchical information/Hessian and shared Schur/profile block exactly as frozen.
6. Construct uncertainty intervals only by the frozen method; invalid intervals remain invalid.
7. Compute every Section 9 metric on its frozen denominator, retaining failed/invalid replicate IDs.
8. Apply the frozen decision hierarchy exactly:
   - IMPLEMENTATION FAIL / BLOCKED if Phase A fails;
   - SCIENTIFIC FAIL if any hard identifiability/failure/usable-fit criterion fails;
   - SCIENTIFIC CONDITIONAL if hard criteria pass but at least one recovery-error or coverage criterion fails;
   - SCIENTIFIC PASS only if every frozen criterion passes.

## Required result artifact

Write:

`research/core/v0_27_hierarchical_repeated_trial_execution_gate_0_1.md`

The artifact must include:

1. Git/freeze identity and exact SHAs;
2. execution environment metadata;
3. C2-27-01…08 table with every measured result, tolerance, negative control and PASS/FAIL;
4. explicit statement of whether scientific RNG was created and, if not, why;
5. if Phase B runs, immutable dataset/seed identity and failure/admissibility table for all 32 replicate IDs;
6. fit outcome and diagnostic summary for every replicate;
7. all frozen recovery, identifiability, conditioning, coverage, missingness and failure metrics with thresholds;
8. no hidden omission of failed/invalid replicates;
9. any clerical/plumbing correction audit trail;
10. final decision using only the four frozen labels;
11. a proposed result-freeze package for MASTER review; CORE may propose but not authorize it;
12. explicit statement that no legacy C3 result was promoted and no post-output tuning occurred.

## Forbidden extensions

No v0.28, no active pulse/probe design, no new observation modality, no unknown topology, no unlabelled-spike matching, no new hierarchical family, no parameter expansion, no application work, no literature novelty positioning and no manuscript claim work.

## STOP boundary

After writing the result artifact, update `research/core/STATUS.md` to `RETURN TO MASTER` (or `BLOCKED` if appropriate) and stop.

Do not open a second scientific gate.
