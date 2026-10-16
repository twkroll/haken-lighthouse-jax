# NUM-ENG RIFC Restricted Idealized IR-A4-R Qualification Freeze 0.7

Date: 2026-10-16
Status: FROZEN / STABLE ENGINEERING ANALYTICAL QUALIFICATION — RESTRICTED K01–K06
Rollback point: RB-028

## Authority

MASTER reviews and accepts the returned:

`NUM-ENG RIFC Source-Graph Arithmetic Propagation & Idealized IR-A4-R Qualification Gate 0.7`

from branch:

`engineering/numerics-v0.1`.

Frozen provenance:

- prospective proof contract commit:
  `d6b76886663a911a85e4b684825b3047e517b754`;
- proof-contract blob:
  `87949856e315f6e5f2cb2f040225734c6d70200d`;
- returned gate blob:
  `2c2defcd164b96d0bb254cf33ab0598c542bfde1`;
- repaired Gate-0.6 source blob:
  `1b94cf36447f428a9968c90ac3c0e74c18494d1c`;
- repaired Gate-0.6 source SHA-256:
  `a447f9a4d9d2be80243a21f4a47cb04d0c5ca2e9dd360b78de4b99cb68067202`;
- RB-025 source blob:
  `6df6740e86344628a2b9583f0a3f719f9d5817f8`; RB-025 remains byte-identical and authoritative for its finite-soundness baseline;
- derivation artifact:
  `research/numerical_engineering/rifc_source_graph_ir_a4r_derivation_0_7.md`;
- finite-correspondence artifact:
  `research/numerical_engineering/rifc_source_graph_finite_correspondence_0_7.md`.

The repaired Gate-0.6 executable source was not modified in Gate 0.7.

RB-025, RB-026 and RB-027 remain unchanged.

## Gate result

`PASS — RESTRICTED IDEALIZED IR-A4-R SOURCE-GRAPH QUALIFICATION K01–K06 / FINITE SOURCE CORRESPONDENCE`.

This is an analytical numerical-engineering qualification result.

It is not a global RIFC theorem and not a finite-machine unlimited-resource guarantee.

## Frozen idealized family

RB-028 accepts one idealized arithmetic family, \(\mathrm{RIFC}_\infty\), defined by:

- the same positive-certificate arithmetic/comparison graph as the Gate-0.6 repaired source;
- the same directed-rounding semantics;
- exact dyadic endpoint export;
- the same threshold-safe response branching;
- the same dyadic Darboux/prefix construction;
- the same strict certificate inequalities;
- arbitrary precision/exponent/integer resources for each finite mathematical level;
- removal only of finite production resource caps.

No certificate logic or model equation is changed.

## Frozen compact qualification domain

The qualification applies only to the prospectively frozen finite union K01–K06 from the Gate-0.7 contract.

It includes:

- tiny positive response / \(\exp(-10000)\) behavior;
- strict no-hit examples;
- one strict regular-hit case;
- fully subthreshold behavior;
- threshold contact / straddling / above-threshold response controls;
- one topology-fixed structural-zero arrival/order control.

It does not cover arbitrary Lighthouse parameter boxes.

## Primitive/source-graph arithmetic result

For \(p\ge128\), define

\[
u=2^{1-p}.
\]

Within the ideal unbounded-exponent correctly-directed arithmetic model, the frozen derivation establishes bounded relative rational-load error and zero additional exact-dyadic export error.

On K01–K06, the source-specific stability analysis establishes:

- semantic scalar endpoint hull:
  \[
  |x|\le H=2^{18};
  \]
- active above-threshold gap lower bound after directed enclosure:
  \[
  x-h>1/400;
  \]
- squared divisor lower bound:
  \[
  (x-h)^2>1/160000;
  \]
- nonpositive exponential arguments on the active reciprocal/exponential response graph;
- response/gain/prefix bounds sufficient to keep the actual computed graph in the frozen compact hull independently of the later coarse error bound.

This noncircular compact-hull step is part of the accepted qualification.

## Operation count

RB-028 freezes the source-graph count overbound:

\[
N_n\le1024\,2^n+1024,
\]

with

\[
N_n\ge2^n.
\]

This is an analytical graph-count bound, not a runtime-complexity benchmark.

## Whole-expression arithmetic excess result

The accepted proof uses a deliberately conservative local Lipschitz majorant and finite cell-DAG depth to obtain a per-cell arithmetic excess bound.

For the complete frozen positive-certificate graph on K01–K06, RB-028 accepts:

\[
E_{\rm arith}(n)
\le
B_K N_n2^{-p_n},
\]

with the prospectively frozen constant

\[
B_K=2^{65536},
\]

and

\[
p_n=128+8n.
\]

Therefore, for the idealized family,

\[
E_{\rm arith}(n)\to0.
\]

The enormous \(B_K\) is a proof constant only.

It is not a usable numerical tolerance or performance estimate.

## Arithmetic excess versus interval range width

RB-028 freezes the distinction:

\[
\text{total enclosure width}
=
\text{natural interval / Darboux range width}
+
\text{arithmetic excess contribution}
\]

at the conceptual level.

The IR-A4-R result controls the second term.

It does not by itself prove physical/Darboux convergence for arbitrary domains; RB-024 continuity/strict-margin assumptions remain separately required.

## Finite executable correspondence

Within all Gate-0.6 finite resource caps, the repaired executable source and the corresponding finite member of \(\mathrm{RIFC}_\infty\) use the same:

- directed endpoint arithmetic;
- exact dyadic serialization;
- branch logic;
- prefix construction;
- strict certificate comparisons.

Thus finite supported calls correspond to finite ideal-family members.

Resource-cap failure remains a fail-closed finite software outcome and is not interpreted as a physical conclusion.

## Eventual-certification interpretation

For K01–K06-type cases satisfying all RB-024 strict-margin/continuity/outward-inclusion hypotheses, RB-024's eventual-certification theorem may be combined with the RB-028 idealized arithmetic-rate qualification.

This statement applies to the mathematical idealized family.

It does NOT imply that the finite production implementation, with caps such as \(p\le8192\) and `nmax<=16`, must terminate with a positive certificate.

Finite production calls may still return:

`RESOURCE_EXHAUSTED / UNCERTIFIED`.

## Post-proof validation

Only after the analytical G-PASS was recorded, the prospectively fixed finite QA was executed.

Frozen result:

- 26/26 fixed isolated validation runs PASS with clean exit;
- one mutated-prefix negative certificate was rejected while the original certificate was accepted;
- the initial monolithic process timeout is retained as NOT PASS and not used as aggregate evidence.

No source modification or post-output fixture retuning occurred.

## Explicit limitations

RB-028 does not establish IR-A4-R for:

- arbitrary Lighthouse parameter families;
- arbitrarily near-threshold positive reciprocal branches;
- unbounded alpha/delay/state domains;
- zero-margin collision/horizon geometries;
- full sequential event tapes;
- parameter-box NNE-A;
- full chart radii.

It does not establish:

- an unconditional finite-machine eventual-certification guarantee;
- global first-hit completeness;
- global simulator correctness;
- scientific performance/scaling claims.

## Classification

### IDEALIZED SOURCE-GRAPH CORRESPONDENCE ESTABLISHED

For the frozen positive-certificate graph and K01–K06.

### IR-A4-R IDEALIZED FAMILY ESTABLISHED

For the prospectively frozen K01–K06 domain only.

### FINITE EXECUTION CORRESPONDENCE ESTABLISHED

For Gate-0.6 calls that remain inside all finite source resource caps.

### DEFERRED

- symbolic/general compact-domain IR-A4-R theorem;
- broader parameter-domain qualification;
- full sequential multi-event certification;
- NNE-A / chart-radius implementation;
- practical unlimited refinement.

## Governance boundaries

RB-028 does not modify or replace:

- RB-025;
- RB-026;
- RB-027;
- RB-024 or any prior scientific freeze;
- RB-015 SCIENTIFIC FAIL;
- RB-020.

It does not authorize:

- TR-27C execution;
- protected RNG creation;
- APP-3;
- v0.28 effect-bearing science;
- executable-source merge to main;
- novelty/manuscript claims.

## STOP

RB-028 freezes only the restricted idealized K01–K06 arithmetic qualification.

STOP — FROZEN / STABLE ENGINEERING ANALYTICAL QUALIFICATION — RESTRICTED K01–K06
