# CORE v0.3 Continuation Validation Contract Freeze 0.1

Date: 2026-09-07
Status: FROZEN / STABLE PRE-EXECUTION CONTRACT
Rollback point: RB-008

## Authority

MASTER authorizes this freeze after PASS of `research/core/v0_3_continuation_validation_contract_canonicalization_gate_0_1.md`.

Frozen source artifact:

- file: `research/core/v0_3_continuation_validation_contract_canonicalization_gate_0_1.md`
- blob SHA: `b521aeb48b813fca5197b12e53e751354d60528c`
- creation commit: `d611d5e058bfabc34347610a272bf24c9278cf0c`

Underlying authorities remain RB-004 through RB-007.

## Frozen contents

The following are frozen before any v0.3 validation execution:

1. Sections 4–5 execution conventions and common reference state R0;
2. V3C01–V3C09, including every fixed subcase and negative control;
3. every model/variant choice, graph, parameter, history, derivative convention, finite-difference step, chart margin and synthetic problem;
4. tolerance classes E0, V3-N1, V3-N2, V3-D1, V3-A1 and L0;
5. arrival-aware integration and fixed-physical-delay conventions;
6. PASS / FAIL / INVALID semantics and software-plumbing audit rule;
7. the complete-suite rule requiring V3C01–V3C09 all PASS for overall PASS;
8. DFR-V3-01 through DFR-V3-12 deferred boundary.

At establishment of RB-008, all V3C01–V3C09 are **UNEVALUATED**.

## Freeze semantics

This is a pre-execution contract freeze only. It states what will be tested and how the result will be judged; it does not claim that any v0.3 validation has passed.

No parameter, finite case, derivative step, chart margin, solver step, tolerance, reference, acceptance rule, benchmark membership or negative control may be changed after output inspection without a new MASTER-authorized contract revision.

A scientifically valid failed case is a valid result and must be preserved.

Clerical/software-plumbing corrections are permitted only under the frozen audit rule: they may not change the scientific contract, must be documented, and all affected validation families must be rerun from the beginning.

## Exclusions

RB-008 does not authorize or freeze:

- any Lighthouse continuation search or critical-point selection;
- any Lighthouse fold/pitchfork location or scaling result;
- any v0.4 Floquet/multiplier/stability object;
- saltation claims beyond the frozen elementary event-time layer;
- hard-threshold tests for the smooth baseline;
- adaptive-delay/commensurability work;
- production/JAX continuation performance;
- normal-form fitting or effect-bearing coefficients;
- v0.4+ legacy recovery execution;
- inference, observation design, active experiment design, applications, novelty, manuscript claims or v0.27.

## Change control

Any modification requires a new MASTER-authorized gate and a new versioned contract freeze. The first execution must use RB-008 unchanged.

## STOP

`CORE v0.3 Continuation Validation Contract Freeze 0.1` is established.

STOP — FROZEN
