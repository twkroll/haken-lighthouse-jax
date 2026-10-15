# CORE v0.27c Whitened Trust-Region Laplace Execution Contract Freeze 0.1

Date: 2026-10-15
Status: FROZEN / STABLE PRE-EXECUTION CONTRACT
Rollback point: RB-020

## Authority

MASTER reviews and accepts:

`research/core/v0_27c_whitened_trust_region_laplace_execution_contract_canonicalization_gate_0_1.md`

Gate blob SHA:

`96cb9c14bc89f4d93a737401043fab9a99715295`.

The returned gate decision is:

`PASS — COMPLETE PRE-EXECUTION V0.27C CONTRACT FIXED; NO CONFIRMATORY OUTPUT GENERATED`.

## Frozen scope

RB-020 freezes the complete v0.27c numerical pre-execution contract for the single follow-up route already selected in RB-016:

`Whitened Trust-Region Laplace Route`.

The frozen inner solver is deterministic whitened dogleg trust-region Gauss-Newton with:

- exact augmented residual and whitened coordinates;
- fixed trust-region radii, acceptance/update rules and invalid-proposal contraction;
- fixed stationarity criterion and finite operation budgets;
- no ridge, LM, pseudoinverse, warm start, alternate solver or post-output rescue;
- physical rerecording and derivative-chart certification at every new state/parameter point;
- exact original-coordinate final Hessian/logdet authority for Laplace;
- inherited bounded-Powell outer route and starts;
- explicit non-finite-start semantics.

## Validation boundary

The deterministic suite `TR-27C-01` through `TR-27C-07` is frozen exactly as specified, including all positive tolerances and all negative controls.

At RB-020 freeze time:

- TR-27C-01 through TR-27C-07 are UNEVALUATED;
- no implementation PASS is asserted;
- no confirmatory stochastic dataset has been generated.

Any TR-27C failure must return:

`IMPLEMENTATION FAIL / BLOCKED`

and prevents all confirmatory RNG creation.

## Confirmatory seed boundary

The disjoint confirmatory namespace is frozen as:

`seed_z^c(d)=2711000+3d`
`seed_noise^c(d)=2711001+3d`
`seed_mask^c(d)=2711002+3d`

for `d=0,...,31`.

At freeze time every `2711xxx` stream remains:

`UNGENERATED / UNEVALUATED`.

The old `2701xxx` data remain DEVELOPMENT ONLY and cannot contribute to the v0.27c confirmatory decision.

## Scientific decision hierarchy

If a later MASTER-authorized v0.27c execution occurs, it must use exactly:

1. IMPLEMENTATION FAIL / BLOCKED;
2. SCIENTIFIC FAIL;
3. SCIENTIFIC CONDITIONAL;
4. SCIENTIFIC PASS.

RB-014 recovery, identifiability, uncertainty, failure-rate and usable-fit thresholds remain inherited except for the prospectively added finite-initial-start criterion fixed by this contract.

Weak/null/fail/conditional results are valid outcomes and cannot be rescued by changing solver constants, seeds, design, thresholds or metrics.

## Relationship to RB-019

RB-019 is acknowledged as the stable Numerical Engineering baseline.

RB-020 does not silently replace the governed CORE implementation path with the NUM-ENG branch code. Any later execution that wishes to import RB-019 executable components into CORE must state that provenance explicitly in its own MASTER-authorized execution gate.

## Preserved results and exclusions

- RB-015 remains immutable SCIENTIFIC FAIL.
- RB-016 remains the follow-up-scope authority.
- no `2711xxx` RNG object has been created;
- no v0.27c confirmatory result exists;
- no APP-3 AI-performance result exists;
- no v0.28, active pulse/probe, novelty or manuscript claim is authorized.

## MASTER sequencing

RB-020 freezes the v0.27c contract but does not self-authorize its execution.

MASTER may separately authorize a future v0.27c execution gate.

For current sequencing, MASTER opens APP-3 scope/benchmark preregistration as the single next scientific/application action because its engineering dependency RB-019 and its CORE-contract dependency RB-020 are both now satisfied. That APP-3 gate is preregistration only and cannot execute training or held-out benchmarking.

## STOP

STOP — FROZEN / STABLE PRE-EXECUTION CONTRACT
