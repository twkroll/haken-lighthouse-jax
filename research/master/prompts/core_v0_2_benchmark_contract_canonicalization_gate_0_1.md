# CORE v0.2 Benchmark Contract Canonicalization Gate 0.1

## Purpose

Construct a governed, pre-execution benchmark contract for the first deterministic analytical validation layer under `CORE Mathematical Freeze 0.1`.

This gate canonicalizes benchmark **definitions, inputs, observables, tolerances and pass/fail rules before execution**. It does not run benchmarks and does not validate any legacy numerical output.

## Authoritative inputs

- `PROJECT_GOVERNANCE.md`
- `research/core/mathematical_freeze_0_1.md`
- `research/core/mathematical_scope_canonicalization_gate_0_1.md`
- frozen legacy recovery input at `287eae8a86560b78ed94f30a2786243714c33ac0`

Legacy candidate documents may be inspected only as historical design input:

- `docs/core/derivations_v0.2.md`
- `docs/core/benchmark_contract_v0.2.md`

The legacy recovery snapshot contains no standalone v0.2 reference script or v0.2 benchmark JSON. Do not invent an exact-replay claim where no committed executable asset exists.

## Authorized scope

1. Audit every proposed v0.2 benchmark against `CORE Mathematical Freeze 0.1`.
2. Retain only benchmarks that test frozen baseline definitions or frozen elementary identities D1–D18.
3. For every retained benchmark, pre-specify before execution:
   - mathematical target;
   - model/variant used;
   - parameter values or symbolic parameter domain;
   - initial/history conditions;
   - observable/output;
   - independent reference value or identity;
   - numerical method class if numerical evaluation will later be needed;
   - horizon/domain and resolution where applicable;
   - absolute/relative tolerance and rationale;
   - pass/fail rule;
   - admissibility/transversality conditions;
   - expected failure mode if assumptions are violated.
4. Separate exact symbolic/algebraic checks from future numerical checks.
5. Identify any legacy benchmark whose choices or tolerances cannot be justified without looking at downstream effects; classify it as deferred rather than repairing it post hoc.
6. Produce one proposed canonical benchmark contract suitable for a later MASTER freeze.

## Minimum benchmark families to consider

Subject to the audit above:

- alpha-kernel normalization;
- impulse/state-space equivalence;
- periodic alpha comb and unit-mass identity;
- periodic hybrid alpha state;
- isolated-clock identity;
- delayed-autapse period identity under its stated assumptions;
- phase-locked self-consistency residual and global time-shift gauge;
- linear-response row-sum identity under its stated assumptions;
- first-hitting/admissibility condition;
- elementary event-time perturbation identity under transversality.

Do not add v0.3+ Floquet, continuation, bifurcation, implementation, inverse, observation-design or active-design tests.

## Explicitly forbidden

- No benchmark execution.
- No new simulation or JAX implementation.
- No parameter scan or optimization.
- No tolerance chosen after observing numerical errors.
- No change to `CORE Mathematical Freeze 0.1`.
- No use of v0.3–v0.26 numerical values as acceptance criteria.
- No active experiment design.
- No v0.27.
- No application or novelty work.

## Deliverable

Create:

`research/core/v0_2_benchmark_contract_canonicalization_gate_0_1.md`

It must contain:

1. input/provenance identity;
2. legacy v0.2 asset inventory;
3. benchmark inclusion/exclusion matrix;
4. fully pre-specified proposed benchmark contract;
5. tolerance rationale table;
6. symbolic-vs-numerical classification;
7. admissibility/transversality requirements;
8. deferred legacy items;
9. gate decision PASS / FAIL / CONDITIONAL;
10. proposed contents for `CORE Benchmark Contract Freeze 0.1` if PASS;
11. exact next execution gate that would be permissible after MASTER freeze, without executing it;
12. STOP.

Then update `research/core/STATUS.md` to RETURN TO MASTER or BLOCKED and stop.

## Gate success criterion

PASS means the benchmark contract is fully specified before any benchmark execution and is traceable to the frozen mathematical baseline. PASS does not mean any benchmark has passed.

## STOP boundary

STOP after deliverable and CORE STATUS update.

STOP — RETURN TO MASTER