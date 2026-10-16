# Lighthouse-JAX — Canonical Project Status

Version: 2.16
Date: 2026-10-16

## Governance state

Canonical rule:

`Reconstruct state, not frozen science.`

The frozen chain now extends through RB-027.

Preserved boundaries:

- RB-015 remains immutable `SCIENTIFIC FAIL`;
- RB-019/RB-021 remain the finite Numerical Engineering baselines;
- RB-020 remains a frozen but unexecuted v0.27c pre-execution contract;
- RB-022 remains frozen first-hit/event-chart theory;
- RB-023 remains frozen finite theory-consistency engineering validation;
- RB-024 remains frozen rigorous outward-interval first-hit certification theory;
- RB-025 remains the immutable finite-soundness RIFC implementation freeze;
- RB-026 remains the historical Gate-0.5 old-source IR-A4-R negative qualification result;
- RB-027 freezes the separate exact-dyadic Gate-0.6 repair baseline;
- APP-3 remains PARKED / PROTECTED / WAIT.

## Gate 0.6 returned result

`NUM-ENG MPFR Exact-Dyadic Serialization Repair & IR-A4-R Requalification Gate 0.6` returned:

`SERIALIZATION REPAIR VALIDATED / FINITE SOUNDNESS PRESERVED / IR-A4-R NOT ESTABLISHED`.

MASTER verifies the complete Gate-0.6 contract was committed before source modification or validation outputs at:

`779c8f05256406c5684d4dec35ae123a418027fb`.

The contract prospectively fixed:

- RB-025 source identity and immutability;
- new Gate-0.6 source path;
- MPFR/GMP backend identities;
- exact `mpfr_get_z_2exp`-style dyadic serialization design;
- finite resource guards;
- compact requalification domain;
- candidate arithmetic-rate proof strategy;
- regression matrix;
- rule that eventual-certification validation cannot execute unless the analytical whole-expression qualification first passes.

## RB-027 — exact-dyadic repair baseline

MASTER establishes:

`NUM-ENG RIFC Exact-Dyadic Serialization Repair Freeze 0.6` / RB-027.

Status:

`FROZEN / STABLE ENGINEERING REPAIR BASELINE — FINITE SOUNDNESS PRESERVED / IR-A4-R NOT ESTABLISHED`.

### RB-025 remains immutable

The original RB-025 source remains byte-identical:

- blob `6df6740e86344628a2b9583f0a3f719f9d5817f8`;
- SHA-256 `0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539`.

RB-026 remains historically valid for that old source.

No RB-025 history is rewritten.

### Repaired Gate-0.6 source

New versioned source:

`software/numerical_engineering/rifc_interval_gate_0_6/source/rifc_mpfr_v0_2.py`.

SHA-256:

`a447f9a4d9d2be80243a21f4a47cb04d0c5ca2e9dd360b78de4b99cb68067202`.

The repaired serializer uses exact MPFR/GMP dyadic export of an already directed-rounded endpoint:

\[
y_p=z\,2^e.
\]

This adds no new arithmetic approximation after MPFR rounding.

The Gate-0.5 artificial \(2^{-2048}\) floor is absent in the repaired source.

### Gate-0.6 finite QA

Frozen finite Gate-0.6 evidence:

- 19/19 new exact-serialization/resource tests PASS;
- 26/26 original Gate-0.4 tests PASS on repaired source;
- 26/26 original Gate-0.4 tests PASS on unchanged RB-025 source;
- combined RIFC regression: 71/71 PASS, clean exit;
- physical/reference/JAX compatibility subset: 28/28 PASS;
- six original RB-025 certificate replays PASS;
- repaired positive proof artifacts, including the tiny-response no-hit certificate, replay PASS.

Finite resource excess fails closed.

### Remaining analytical limitation

The serializer repair removes the known fixed-rate obstruction.

However Gate 0.6 does not establish a complete finite constant \(B_K\) satisfying

\[
E_{\rm arith}(n)\le B_KN_n2^{-p_n}
\]

for the full positive-certificate expression graph.

The implementation also remains resource bounded:

\[
p\le8192,
\]

and `certify` remains finite with `nmax<=16`.

Therefore:

- finite certificate soundness is preserved;
- IR-A4-R is NOT ESTABLISHED;
- production finite execution is not identified with an unbounded eventual-certification process;
- Q6/Q7 rate/eventual-certification trials were correctly not executed.

## NUM-ENG Gate 0.7

MASTER opens:

`NUM-ENG RIFC Source-Graph Arithmetic Propagation & Idealized IR-A4-R Qualification Gate 0.7`.

Status:

`READY`.

Prompt:

`research/master/prompts/numerical_engineering_rifc_source_graph_ir_a4r_qualification_gate_0_7.md`.

This gate performs no source modification.

Its purpose is to separate and analyze:

1. the finite Gate-0.6 executable source; and
2. an idealized unbounded-precision arithmetic family with the same positive-certificate expression graph, exact-dyadic serialization semantics and certificate logic.

Before new analytical results it must commit:

`research/numerical_engineering/rifc_source_graph_ir_a4r_proof_contract_0_7.md`.

### Gate-0.7 target

The gate must prospectively freeze a compact domain and then attempt to prove or refute:

\[
E_{\rm arith}(n)\le B_KN_n2^{-p_n},
\]

with finite \(B_K\), source-graph operation count

\[
N_n\le a2^n+b,
\]

and

\[
p_n=128+8n.
\]

If established for the idealized family:

\[
E_{\rm arith}(n)\to0.
\]

The gate must also prove finite-source correspondence: every finite Gate-0.6 execution inside its resource domain must correspond to the same finite idealized-family member.

### Eventual-certification interpretation

Even if the idealized IR-A4-R theorem is established:

- the mathematical unbounded family may satisfy RB-024 eventual certification under strict margins;
- a real finite resource-bounded invocation may still return `RESOURCE_EXHAUSTED / UNCERTIFIED`;
- no finite-machine run is relabelled as possessing unlimited resources.

This distinction is mandatory.

### Non-goals

Gate 0.7 does not:

- modify Gate-0.6 source;
- lift finite production resource caps;
- implement full sequential multi-event RIFC;
- implement NNE-A;
- compute a full parameter-box chart radius;
- perform scaling/performance experiments;
- execute TR-27C;
- execute APP-3.

## CORE

CORE remains:

`FROZEN / WAIT`.

RB-024 and every prior scientific freeze remain unchanged.

## CORE v0.27c

RB-020 remains frozen and unexecuted.

- TR-27C-01…07: UNEVALUATED.
- `2711xxx`: UNGENERATED / UNEVALUATED.

## APP-3

APP-3 remains:

`PROTECTED / WAIT`.

AI work remains parked under the Numerics + Theory priority.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | NUM-ENG Gate 0.7 oversight |
| 10 CORE | FROZEN / WAIT | RB-024 rigorous interval theory |
| 20 NUM-ENG | READY | source-graph / idealized IR-A4-R qualification |
| 50 APP-1 | PROTECTED / WAIT | unchanged |
| 60 APP-2 | PROTECTED / WAIT | later electronics/neuromorphics |
| 70 APP-3 | PROTECTED / WAIT | AI parked |
| 80 LIT | WAIT | — |
| 90 MANUSCRIPT | WAIT | — |

## Current rollback points

RB-001 through RB-026 remain unchanged.

27. RB-027 NUM-ENG RIFC Exact-Dyadic Serialization Repair Freeze 0.6 — FROZEN / STABLE ENGINEERING REPAIR BASELINE — FINITE SOUNDNESS PRESERVED / IR-A4-R NOT ESTABLISHED

## Exact next step

### NUM-ENG

In the existing NUM-ENG chat:

`GO`

In a new/replacement NUM-ENG chat:

`RESUME`

Execute only:

`research/master/prompts/numerical_engineering_rifc_source_graph_ir_a4r_qualification_gate_0_7.md`.

The Gate-0.7 proof contract must be committed before analytical outputs.

### CORE

No CORE action is currently authorized.

### APP-3

No APP-3 action is currently authorized.

When Gate 0.7 returns, issue:

`Status?`

in MASTER.

## Global STOP boundaries

Until explicit later authorization:

- no source modification in Gate 0.7;
- no full multi-event/NNE-A work;
- no TR-27C execution;
- no `2711xxx` RNG creation;
- no v0.27c confirmatory execution;
- no APP-3 execution;
- no RB-015 relabelling;
- no v0.28 effect-bearing science;
- no APP-1/APP-2 execution;
- no novelty positioning;
- no manuscript claim freeze.
