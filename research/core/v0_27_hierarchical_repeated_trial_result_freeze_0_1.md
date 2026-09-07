# CORE v0.27 Hierarchical Repeated-Trial Result Freeze 0.1

Date: 2026-09-07
Status: FROZEN / STABLE SCIENTIFIC RESULT — FAIL
Rollback point: RB-015

## Authority

MASTER accepts `research/core/v0_27_hierarchical_repeated_trial_execution_gate_0_1.md` as the governed result of the first effect-bearing v0.27 hierarchical repeated-trial execution.

Frozen source artifact:

- file: `research/core/v0_27_hierarchical_repeated_trial_execution_gate_0_1.md`
- result commit: `07a813e42107d3eea69fec1e858e586adad367bb`
- RETURN-TO-MASTER commit: `e17489514be283b5daa3e254504e97edd7ee5fa6`
- execution-contract authority: RB-014
- scope authority: RB-013
- upstream scientific/audit authorities: RB-004 through RB-012 as applicable.

## Frozen overall result

`SCIENTIFIC FAIL — C2 PASS; CONSERVATIVE SHARED INFORMATION PASS; FROZEN LAPLACE INFERENCE HAS NO FINITE INITIAL OUTER START ON ANY OF 32 DATASETS`

This is a valid negative result under the frozen RB-014 decision hierarchy. It is not reclassified as CONDITIONAL and is not erased by later method development.

## Frozen implementation result

C2-27-01 through C2-27-08 all PASS, including required negative controls.

Therefore the scientific failure is not classified as an implementation-validation failure.

## Frozen stochastic-data result

All 32 immutable stochastic datasets were generated only after C2 PASS, using the frozen PCG64DXSM seed map.

Frozen data-quality/admissibility findings:

- `INSUFFICIENT_MASK = 0/32`;
- truth physical/chart invalid = `0/32`;
- minimum mask-rich trials in any dataset = `15/16`;
- no seed or dataset was replaced or regenerated.

The complete per-dataset hash ledger in the execution artifact is part of this freeze.

## Frozen structural-information result

The conservative nuisance-profiled shared-parameter information audit is positive:

- rank-two/regular fraction = `32/32 = 1.000`;
- condition-number range = `348731` to `712596`, below the frozen `1e8` threshold.

Thus the execution does not support the conclusion that the two shared scientific directions `(p,tau_3)` are structurally unidentifiable under the conservative local audit.

## Frozen inference failure

For every dataset and each of the three frozen outer starts:

- total starts attempted = `96`;
- finite complete initial Laplace objectives = `0/96`;
- each failed start contains at least one trial-mode `INNER_MODE_FAIL` from the frozen maximum-20-trial strong-Wolfe line search;
- every dataset is `OUTER_OPT_FAIL` under the frozen rule;
- complete usable-fit fraction = `0/32`;
- valid five-parameter uncertainty intervals = `0/32`.

Therefore hard failure criteria fail and the final branch result is `SCIENTIFIC FAIL`.

No fourth start, warm start, line-search relaxation, trust region, ridge, alternative optimizer, EM/VI/MCMC route, seed replacement or data replacement was introduced.

## Interpretation boundary

RB-015 freezes only the result of the preregistered RB-014 inference route.

It does **not** prove that:

- the hierarchical scientific model is globally non-identifiable;
- Laplace marginalization is impossible in principle;
- a different preregistered trial-mode solver would fail;
- additional starts or alternative parameterizations would fail;
- active sensing is required;
- any legacy C3 optimized design is validated.

The positive `I_free` audit and the universal frozen solver-start failure must be retained together.

## Follow-up data-use boundary

The 32 RB-015 datasets and optimization traces are now observed data. They may be used in a separately authorized failure-mechanism/method-development gate, but any redesigned inference method selected using them is post hoc with respect to this dataset set.

A later confirmatory test of a redesigned method must therefore use a new MASTER-frozen execution contract with a disjoint, previously ungenerated confirmatory seed set. The original RB-015 result remains unchanged.

## Audit note

The preflight SciPy bounded-Powell crash on non-finite starts is invalidated as evidence exactly as recorded in the execution artifact. It changed no frozen scientific quantity and does not alter the SCIENTIFIC FAIL classification.

## STOP

`CORE v0.27 Hierarchical Repeated-Trial Result Freeze 0.1` is established.

STOP — FROZEN
