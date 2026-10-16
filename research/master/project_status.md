# Lighthouse-JAX — Canonical Project Status

Version: 2.15
Date: 2026-10-16

## Governance state

Canonical rule:

`Reconstruct state, not frozen science.`

The frozen chain now extends through RB-026.

Preserved boundaries:

- RB-015 remains immutable `SCIENTIFIC FAIL`;
- RB-019/RB-021 remain the finite Numerical Engineering baselines;
- RB-020 remains a frozen but unexecuted v0.27c pre-execution contract;
- RB-022 remains frozen first-hit/event-chart theory;
- RB-023 remains frozen finite theory-consistency engineering validation;
- RB-024 remains frozen rigorous outward-interval first-hit certification theory;
- RB-025 remains the immutable finite-soundness RIFC implementation freeze;
- RB-026 freezes the negative Gate-0.5 IR-A4-R qualification result;
- APP-3 remains PARKED / PROTECTED / WAIT.

## RB-025 remains unchanged

`NUM-ENG RIFC-0.1 Interval Certification Freeze 0.4` / RB-025 remains:

`FROZEN / STABLE ENGINEERING CERTIFICATION LAYER — FINITE SOUNDNESS ONLY`.

Its source identity remains:

- blob: `6df6740e86344628a2b9583f0a3f719f9d5817f8`;
- SHA-256: `0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539`.

No RB-025 source/file is modified by the Gate-0.5 review or the new Gate 0.6 authorization.

## RB-026 — Gate-0.5 negative qualification result

`NUM-ENG MPFR IR-A4-R Qualification & Eventual-Certification Gate 0.5` returned:

`IR-A4-R NOT ESTABLISHED — SOURCE-LEVEL ANALYTICAL NO-GO`.

MASTER verifies that the full Gate-0.5 qualification contract was committed before diagnosis at:

`20d9ae3c5973b5226387c5f679c9ae03c1e58973`.

The prospectively frozen contract fixed:

- unchanged RB-025 source identity;
- GNU MPFR 4.2.2 backend identity;
- compact domain (K=[-100000,100000]);
- the exact source expression graph;
- the exact counterexample candidate (S(1/100)=exp(-10000));
- precision set ({128,256,512,2048,4096});
- Q7/Q8 as forbidden unless the analytical rate qualification first passed.

No source repair, domain shrinking, empirical (B_K) fitting or post-output fixture change occurred in Gate 0.5.

### Source-level blocker

The unchanged RB-025 `M.val` serializer contains a fixed small-value widening branch at MPFR exponent below (-2048).

For the frozen exact point:

[
x=rac1{100},quad r=1,quad h=0,
]

the exact response is

[
S(x)=exp(-10000).
]

The serializer returns

[
[0,2^{-2048}]
]

through the fixed tiny-value branch, independent of precision.

Therefore the arithmetic excess has a nonvanishing floor (2^{-2048}), so no finite compact-domain constant can satisfy

[
operatorname{excwid}le C_K2^{-p}
]

for all (p) in the implemented graph.

This is a source-level no-go for the unchanged Python+MPFR serialization layer.

It is not:

- a failure of MPFR correct rounding;
- a contradiction of RB-024;
- a revocation of RB-025 finite certificate soundness.

### Correct negative-gate behavior

Because analytical Q5 failed:

- Q7 empirical rate fitting was not executed;
- Q8 eventual-certification fixtures were not used as a substitute for proof.

RB-025 regression remains preserved:

- 26/26 targeted finite-soundness tests PASS;
- 6/6 stored certificate replays PASS.

MASTER therefore establishes:

`NUM-ENG IR-A4-R Qualification Result Freeze 0.5` / RB-026.

Status:

`FROZEN / STABLE ENGINEERING NEGATIVE QUALIFICATION RESULT`.

## NUM-ENG Gate 0.6

MASTER authorizes:

`NUM-ENG MPFR Exact-Dyadic Serialization Repair & IR-A4-R Requalification Gate 0.6`.

Status:

`READY`.

Prompt:

`research/master/prompts/numerical_engineering_mpfr_exact_dyadic_serialization_repair_ir_a4r_requalification_gate_0_6.md`.

### Exact repair boundary

Gate 0.6 must not edit RB-025.

It must create a new versioned implementation subtree.

The sole initial repair target is the MPFR-to-exact-dyadic serialization path responsible for the Gate-0.5 precision-independent floor.

The repaired path must exactly serialize an already rounded MPFR value as a dyadic rational:

[
y_p=z,2^e
]

with exact integer (z) and exponent (e), without a fixed underflow floor or ordinary floating-point conversion.

A route such as exact `mpfr_get_z_2exp` / GMP integer extraction is preferred, or another provably equivalent exact conversion.

### Gate-0.6 chronology

Before source repair or validation output, NUM-ENG must commit:

`research/numerical_engineering/rifc_exact_dyadic_repair_requalification_contract_0_6.md`.

That contract must freeze:

- old and proposed source identities;
- exact serialization mechanism;
- backend identities;
- resource guards;
- repaired source path;
- compact requalification domain;
- rate-proof strategy;
- operation-count strategy;
- regression fixtures;
- result classes and negative controls.

### Gate-0.6 required outcomes

The repair must first demonstrate:

1. RB-025 remains byte-identical;
2. new exact-dyadic serializer is inclusion-preserving and exact with respect to the directed MPFR endpoint;
3. the fixed (2^{-2048}) serialization floor is removed;
4. finite-soundness/fail-closed behavior remains intact;
5. Gate-0.4 compatibility/replay expectations remain satisfied.

Only then may the gate requalify IR-A4-R.

For a full PASS it must analytically establish on the frozen Gate-0.6 domain:

[
E_{m arith}(n)le B_KN_n2^{-p_n},
]

with finite (B_K), explicit

[
N_nle a2^n+b,
]

and

[
p_n=128+8n,
]

so that

[
E_{m arith}(n)	o0.
]

Only after the analytical qualification passes may eventual-certification fixtures be executed.

### Bounded repair-only outcome

A valid non-full result is:

`SERIALIZATION REPAIR VALIDATED / IR-A4-R NOT ESTABLISHED`.

Such an outcome preserves the repaired finite-soundness work but does not promote eventual certification.

### Non-goals

Gate 0.6 does not include:

- full sequential multi-event tape certification;
- parameter-box NNE-A;
- full-chart radius;
- performance/scaling work;
- TR-27C;
- APP-3;
- stochastic science.

## CORE

CORE remains:

`FROZEN / WAIT`.

RB-024 and all earlier scientific freezes remain unchanged.

## CORE v0.27c

RB-020 remains frozen and unexecuted.

- TR-27C-01…07: UNEVALUATED.
- `2711xxx`: UNGENERATED / UNEVALUATED.

## APP-3

APP-3 remains:

`PROTECTED / WAIT`.

Its AI scope prompt remains PARKED / NOT EXECUTABLE.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | NUM-ENG Gate 0.6 oversight |
| 10 CORE | FROZEN / WAIT | RB-024 rigorous interval theory |
| 20 NUM-ENG | READY | exact-dyadic serialization repair + IR-A4-R requalification |
| 50 APP-1 | PROTECTED / WAIT | unchanged |
| 60 APP-2 | PROTECTED / WAIT | later electronics/neuromorphics |
| 70 APP-3 | PROTECTED / WAIT | AI parked |
| 80 LIT | WAIT | — |
| 90 MANUSCRIPT | WAIT | — |

## Current rollback points

RB-001 through RB-025 remain unchanged.

26. RB-026 NUM-ENG IR-A4-R Qualification Result Freeze 0.5 — FROZEN / STABLE ENGINEERING NEGATIVE QUALIFICATION RESULT

## Exact next step

### NUM-ENG

In the existing NUM-ENG chat:

`GO`

In a new/replacement NUM-ENG chat:

`RESUME`

Execute only:

`research/master/prompts/numerical_engineering_mpfr_exact_dyadic_serialization_repair_ir_a4r_requalification_gate_0_6.md`.

The Gate-0.6 pre-repair/pre-execution contract must be committed before source modification or validation outputs.

### CORE

No CORE action is currently authorized.

### APP-3

No APP-3 action is currently authorized.

When NUM-ENG Gate 0.6 returns, issue:

`Status?`

in MASTER.

## Global STOP boundaries

Until explicit later authorization:

- do not modify RB-025;
- no full multi-event/NNE-A work inside Gate 0.6;
- no TR-27C execution;
- no `2711xxx` RNG creation;
- no v0.27c confirmatory execution;
- no APP-3 execution;
- no RB-015 relabelling;
- no v0.28 effect-bearing science;
- no APP-1/APP-2 execution;
- no novelty positioning;
- no manuscript claim freeze.
