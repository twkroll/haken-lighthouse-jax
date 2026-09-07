# CORE v0.27 Hierarchical Repeated-Trial Execution Contract Freeze 0.1

Date: 2026-09-07
Status: FROZEN / STABLE PRE-EXECUTION CONTRACT
Rollback point: RB-014

## Authority

MASTER accepts `research/core/v0_27_hierarchical_repeated_trial_execution_contract_canonicalization_gate_0_1.md` as the complete governed pre-execution contract for the first v0.27 hierarchical repeated-trial experiment.

Frozen source artifact:

- file: `research/core/v0_27_hierarchical_repeated_trial_execution_contract_canonicalization_gate_0_1.md`
- blob SHA: `05e55e7683ca7013ee6517c3da322c75732fe725`
- contract commit: `d1dc2d63070dd21d713e16a3d1c92b28b2b90c7b`
- RETURN-TO-MASTER commit: `c0856c41e6c7dc52c504bc987fb233dd3141f15b`
- scope authority: RB-013
- upstream scientific/audit authorities: RB-004 through RB-012 as applicable.

## Frozen contract result

`PASS — COMPLETE PRE-EXECUTION CONTRACT FIXED; NO V0.27 SCIENTIFIC DATASET OR INFERENCE EXECUTED`

At freeze time:

- C2-27-01 through C2-27-08 are UNEVALUATED;
- all 32 scientific stochastic datasets are UNGENERATED / UNEVALUATED;
- no v0.27 recovery, rank, conditioning, uncertainty, coverage or effect result exists.

## Frozen scientific design

The complete contract freezes, without post-output modification:

- the N=3 directed-cycle graph, complete `W^(0)`, `B`, `Tau^(0)` and `C` matrices;
- `alpha=1`, `r=1`, `h=-1`, nominal preparation and gauge;
- truth `p*=0.05`, `tau_3*=0.90`, `Theta=[-0.20,0.20] x [0.60,1.60]`;
- hierarchical truth `sigma_phi*=sigma_psi*=sigma_q*=0.05` and `Lambda=[log(0.01),log(0.20)]^3`;
- `R=16` repeated trials and `H=4` firing ordinals per neuron, hence 12 candidate labelled times per trial;
- timing noise `sigma_t=0.02` and MCAR missingness `pi_miss=0.20`;
- exactly 32 stochastic datasets and the immutable PCG64DXSM seed map specified in the contract;
- minimal-data, physical-timeout and event-budget rules;
- the Laplace-marginal objective, inner BFGS trial-mode solve, Hessian/logdet validity rules, outer scaled bounded Powell optimization and fixed-start policy;
- physical rerecording and fixed-chart derivative rules;
- local information, Schur/profile, Hessian and uncertainty definitions;
- normalized error, identifiability, coverage, failure and usable-fit criteria;
- the overall decision hierarchy IMPLEMENTATION FAIL/BLOCKED, SCIENTIFIC FAIL, SCIENTIFIC CONDITIONAL, SCIENTIFIC PASS;
- C2-27-01 through C2-27-08 and all their tolerances/negative controls;
- the rule that every C2 check must pass before any scientific RNG object is created;
- all exclusions and deferred branches.

## Change control

No truth, graph, parameter box, preparation scale, trial count, horizon, noise level, missingness rate, seed, optimizer, start, derivative rule, chart rule, tolerance, budget, metric, threshold, validation case or decision criterion may be altered after any C2 or scientific output is inspected.

A failed, weak, null or conditional result is a valid final result for this preregistered branch. Any redesigned follow-up requires a new MASTER-authorized branch and must preserve the original result and provenance.

Software/package versions and CPU metadata are execution-environment metadata. If the execution environment changes after C2 validation, the full C2 suite must rerun from the beginning before science; frozen scientific design quantities remain unchanged.

## Explicit exclusions

RB-014 does not itself validate any implementation or scientific result. It does not promote any legacy C3 effect, optimized pulse/sensor/subset, active intervention, application result, novelty claim or manuscript claim.

## STOP

`CORE v0.27 Hierarchical Repeated-Trial Execution Contract Freeze 0.1` is established.

STOP — FROZEN
