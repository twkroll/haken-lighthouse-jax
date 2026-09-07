# CORE Benchmark Contract Freeze 0.1

Date: 2026-09-07
Status: FROZEN / STABLE
Rollback point: RB-005

## Authority

MASTER authorizes this freeze after PASS of `research/core/v0_2_benchmark_contract_canonicalization_gate_0_1.md`.

Frozen source artifact:

- file: `research/core/v0_2_benchmark_contract_canonicalization_gate_0_1.md`
- blob SHA: `bfe0f23ac8c80d47aaf8c1c18ffd765689a64a33`
- creation commit: `a645789c4cb087452a059ab935d86e56025c53e3`

`CORE Mathematical Freeze 0.1` / RB-004 remains the mathematical authority beneath this contract.

## Frozen contents

The following contents of the source artifact are frozen before any benchmark execution:

1. contract-wide execution conventions in Section 4;
2. benchmark definitions BC01–BC10 in Section 5;
3. tolerance classes E0, N1, N2 and L0 in Section 6;
4. symbolic-versus-numerical separation in Section 7;
5. admissibility and transversality requirements in Section 8;
6. deferred-item boundary DFR-01 through DFR-07 in Section 9.

This includes all fixed parameter values, finite test sets, histories, horizons, grids/resolutions, quadrature stopping tolerances, observables, independent references, acceptance tolerances and pass/fail rules stated there.

## Freeze semantics

This is a **pre-execution contract freeze**. It freezes what will be tested and how it will be judged.

It explicitly does **not** state that any benchmark has passed. At establishment of RB-005, BC01–BC10 are UNEVALUATED under the governed execution gate.

No parameter, history, grid, method class, tolerance, acceptance rule, benchmark membership or negative control may be changed after observing benchmark outputs without a new MASTER-authorized contract revision. A failed benchmark remains a valid result.

Clerical or software-plumbing defects in a future execution harness may be corrected only if the frozen scientific contract is unchanged; every such correction must be documented, and no failed scientific case may be dropped or replaced.

## Exclusions

RB-005 does not authorize or freeze:

- legacy v0.3–v0.26 numerical claims;
- continuation, Floquet, bifurcation, normal-form or invariant-object claims;
- generic saltation or slow-synapse stability claims;
- JAX/production implementation performance;
- inference or observation-design performance;
- active pulse / hybrid experiment design;
- v0.27 or repeated-trial work;
- application or novelty claims.

## Change control

Any modification of this contract requires a new MASTER-authorized gate and a new versioned contract freeze. The first execution must use RB-005 unchanged.

## STOP

`CORE Benchmark Contract Freeze 0.1` is established.

STOP — FROZEN
