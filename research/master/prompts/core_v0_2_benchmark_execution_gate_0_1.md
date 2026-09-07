# CORE v0.2 Benchmark Execution Gate 0.1

Date: 2026-09-07
Authorizing branch: MASTER
Execution branch: CORE

## Objective

Execute the frozen benchmark suite BC01–BC10 exactly as specified in `research/core/benchmark_contract_freeze_0_1.md` and its frozen source artifact `research/core/v0_2_benchmark_contract_canonicalization_gate_0_1.md`.

This gate is the first governed execution against `CORE Mathematical Freeze 0.1` (RB-004) under the pre-execution contract freeze RB-005.

## Mandatory inputs

Read and obey:

- `PROJECT_GOVERNANCE.md`
- `research/core/STATUS.md`
- `research/master/STATUS.md`
- `research/master/project_status.md`
- `research/master/decision_branch_log.md`
- `research/core/mathematical_freeze_0_1.md`
- `research/core/benchmark_contract_freeze_0_1.md`
- `research/core/v0_2_benchmark_contract_canonicalization_gate_0_1.md`

## Frozen execution rule

Execute BC01–BC10 exactly as frozen.

Do not change after observing results:

- benchmark membership;
- parameter values;
- finite test sets;
- histories or initial conditions;
- horizons;
- grids/resolutions;
- method classes;
- quadrature stopping tolerances;
- acceptance tolerances;
- observables;
- references;
- pass/fail rules;
- negative controls.

No failed case may be dropped, replaced, softened or rerun with a scientifically different specification inside this gate.

## Allowed execution work

You may:

1. perform exact symbolic/algebraic checks required by E0;
2. perform deterministic float64 calculations required by N1/N2;
3. use deterministic quadrature only where the frozen contract permits it;
4. use deterministic first-hit/root calculations only where permitted;
5. evaluate the frozen alpha state-space flow;
6. write a minimal validation harness solely to execute BC01–BC10;
7. correct a clerical or software-plumbing defect in that harness only when the frozen scientific contract is unchanged.

If a harness correction occurs, document:

- the defect;
- why it is implementation/plumbing rather than a scientific-specification change;
- the correction;
- whether any prior output was invalidated.

Do not erase the audit trail.

## Forbidden

- no parameter search or tuning;
- no tolerance relaxation;
- no additional rescue cases;
- no continuation or bifurcation analysis;
- no Floquet/stability extension;
- no generic saltation analysis beyond BC10/D18;
- no slow-synapse stability work;
- no JAX/production implementation continuation;
- no performance/scaling benchmark;
- no inference or optimization;
- no active experiment or pulse design;
- no v0.3+ legacy recovery beyond what BC01–BC10 explicitly require;
- no v0.27;
- no application or novelty claims.

## Required result record

Create:

`research/core/v0_2_benchmark_execution_gate_0_1.md`

It must contain at least:

1. Git/reproducibility identity and exact frozen input SHAs;
2. execution environment sufficient to reproduce calculations;
3. method implementation notes, without changing RB-005;
4. one section per BC01–BC10;
5. for every benchmark/subcase:
   - prescribed inputs;
   - observed result(s);
   - reference value(s);
   - error/residual;
   - applicable tolerance/rule;
   - admissibility/transversality status;
   - PASS / FAIL / INVALID classification;
6. explicit negative-control results for BC09 and BC10;
7. complete suite summary with no omitted fixed case;
8. any harness corrections and audit trail;
9. overall gate decision;
10. proposed result-freeze contents if the execution is complete;
11. explicit statement that failures are preserved and not tuned away;
12. STOP.

## Gate decision semantics

Use:

- `PASS` only if every required BC01–BC10 benchmark and required subcase/negative control passes exactly under RB-005;
- `FAIL` if any scientifically valid required benchmark/subcase fails its frozen rule;
- `CONDITIONAL` only for a genuine execution-completeness blocker that prevents a scientifically meaningful PASS/FAIL classification without changing the contract;
- `INVALID` only at individual-case level when the frozen contract itself says the case is outside its admissible domain; do not use INVALID to hide an ordinary failure.

A FAIL is a valid result and must return to MASTER unchanged.

## Result freeze boundary

CORE may propose, but may not itself authorize, a benchmark result freeze.

No result from v0.3–v0.26 is promoted by success of BC01–BC10.

## STOP boundary

After creating `research/core/v0_2_benchmark_execution_gate_0_1.md`, update `research/core/STATUS.md` to `RETURN TO MASTER` or `BLOCKED` and stop.

Do not execute a second gate.

STOP — RETURN TO MASTER
