# CORE v0.2 Benchmark Result Freeze 0.1

Date: 2026-09-07
Status: FROZEN / STABLE RESULT
Rollback point: RB-006

## Authority

MASTER authorizes this result freeze after review of `research/core/v0_2_benchmark_execution_gate_0_1.md`.

Frozen execution artifact:

- file: `research/core/v0_2_benchmark_execution_gate_0_1.md`
- blob SHA: `00c353b84692e108648bb19257ff06ea04978f16`
- creation commit: `4a11b6c0144e522b3515dd8160a3bb06c3ffb2f1`

Underlying authorities remain:

- RB-004 `CORE Mathematical Freeze 0.1`
- RB-005 `CORE Benchmark Contract Freeze 0.1`

## Frozen result

The governed BC01–BC10 benchmark suite was executed under RB-005 without scientific contract modification.

Every required benchmark, fixed subcase and required negative control passed:

- BC01 PASS — alpha-kernel normalization;
- BC02 PASS — impulse/state-space equivalence;
- BC03 PASS — periodic alpha comb and unit mass;
- BC04 PASS — periodic hybrid alpha state and closure;
- BC05 PASS — isolated-clock identity, both subcases;
- BC06 PASS — all nine delayed-autapse alpha/delay cases;
- BC07 PASS — phase-locked self-consistency and global gauge;
- BC08 PASS — all six row-sum cases;
- BC09 PASS — first-hitting positive case and negative control;
- BC10 PASS — both event-time perturbations and the non-transversal negative control.

Overall governed execution result:

`PASS — BC01–BC10 ALL PASS UNDER RB-005`

## Harness audit trail

The execution record documents one software-plumbing correction: adaptive quadrature was initially placed directly inside an endpoint-bracketed root solver. This could reject an endpoint root because of a floating-point residual sign even when the residual satisfied the frozen scientific tolerance.

The correction replaced the root-function evaluation by the exact closed-form primitive of the already frozen periodic alpha comb. The correction did not alter benchmark membership, model, parameters, finite cases, histories, horizons, grids, method classes, observables, references, quadrature tolerances, acceptance tolerances, pass/fail rules or negative controls. The aborted harness output was not used as scientific evidence.

MASTER accepts this as a documented software-plumbing correction permitted by RB-005, not as tuning or scientific repair.

## Result interpretation

RB-006 validates the first governed analytical benchmark layer against the frozen mathematical baseline RB-004 under the pre-execution contract RB-005.

It supports that the frozen baseline equations, elementary identities, event semantics and selected analytical variants used in BC01–BC10 are mutually consistent with the governed deterministic validation checks specified before execution.

## Freeze boundary

RB-006 does **not** validate, promote or freeze:

- any legacy v0.3–v0.26 numerical result;
- continuation or bifurcation locations;
- Floquet spectra or stability changes;
- normal-form coefficients or invariant objects;
- generic saltation or slow-synapse stability claims;
- JAX/production implementation performance;
- inference or optimizer performance;
- observation design;
- active pulse / hybrid experiment design;
- v0.25 two-probe effects;
- v0.26 nuisance/calibration numerical claims;
- v0.27 or hierarchical repeated-trial work;
- application or novelty claims.

The legacy branch `core/theory-v0.1` remains read-only recovery evidence and is not merged.

## Change control

Any attempt to reinterpret a failed/omitted case, alter RB-005 retrospectively, or expand this result freeze requires a new MASTER-authorized gate. Later work may build on RB-006 but may not silently broaden its evidentiary scope.

## STOP

`CORE v0.2 Benchmark Result Freeze 0.1` is established.

STOP — FROZEN
