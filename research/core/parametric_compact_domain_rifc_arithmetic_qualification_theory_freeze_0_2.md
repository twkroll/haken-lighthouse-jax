# CORE Parametric Compact-Domain RIFC Arithmetic Qualification Theory Freeze 0.2

Date: 2026-10-16
Status: FROZEN / STABLE SCIENTIFIC THEORY
Rollback point: RB-029

## Authority

MASTER accepts:

`research/core/parametric_compact_domain_rifc_arithmetic_qualification_theory_gate_0_2.md`

as the canonical source for this freeze.

Returned gate blob SHA:

`44309453f0ed4058ef6716262185aa1b898cd98e`.

No numerical execution occurred in the gate.

RB-028 remains unchanged and becomes a restricted corollary/instance of the general theorem frozen here.

## Frozen theorem class

RB-029 freezes a reusable sufficient-condition theorem for a compact RIFC input domain \(K\) and a finite positive-certificate endpoint-graph family.

The theorem is not universal over arbitrary interval programs or arbitrary Lighthouse parameter domains.

## A1 — directed inclusion

Every inexact primitive used by a qualified positive-certificate graph must be evaluated with a specified outward/directed inclusion contract.

The core primitive family contains:

- rational endpoint load;
- addition/subtraction;
- multiplication;
- division on a divisor set bounded away from zero;
- exponential;
- exact comparisons/min/max/hull/intersection where applicable;
- exact dyadic serialization of an already rounded endpoint.

Optional primitives require separate qualification.

## A2 — primitive arithmetic rate

On every qualified branch and compact semantic operand set, each primitive endpoint map must admit a finite bound

\[
|\operatorname{fl}^{\pm}_{p,v}(z)-F_v(z)|
\le r_{v,b}2^{-p}.
\]

Raw exact-rational numerator/denominator magnitudes need not themselves lie in the semantic hull; the rational-load composite may instead be qualified directly.

## A3 — finite branch cover

The positive-certificate source graph over \(K\) must admit a finite branch cover

\[
\mathcal B_K=\{b_1,\ldots,b_J\}.
\]

Threshold-subthreshold, threshold-straddling and fully above-threshold paths may be distinct qualified branches.

Uncovered dynamic expression-graph topology is outside the theorem.

## A4 — noncircular compact semantic hull

For every branch, exact model/range properties must establish before use of the final coarse arithmetic bound:

\[
|x_v|\le H_{K,b}<\infty.
\]

Set

\[
H_K=\max_b H_{K,b}.
\]

Compactness plus continuity of the finite exact endpoint graph is a sufficient route when singular denominators are excluded.

The final \(B_K\) may not be used to prove the hull needed to construct \(B_K\).

## A5 — divisor / active-threshold separation

Every active division node must satisfy a branchwise exact lower denominator margin

\[
|d|\ge\delta_{K,b}>0.
\]

For the current Lighthouse response source graph, every positive endpoint actually sent through

\[
1/(x-h)^2
\]

must satisfy

\[
x-h\ge\delta_{x,K}>0.
\]

Fully subthreshold branches need no reciprocal margin.

Threshold-straddling branches may return exact lower response zero, but any positive upper endpoint evaluated through the reciprocal graph still requires positive separation.

The smoothness of the composed physical response at \(x=h\) does not remove the singular intermediate in this particular source graph.

## A6 — bounded local graph

Each qualified cell branch has finite:

- primitive count \(c_K\);
- dependency depth \(D_K\);
- fan-in;
- fixed wrapper work \(b_K\).

For dyadic \(m_n=2^n\) cells,

\[
N_n\le a_K2^n+b_K.
\]

This is a primitive-operation graph bound, not a bit-complexity, memory or wall-time theorem.

## A7 — local endpoint stability

Every exact endpoint map must be Lipschitz on a compact perturbation tube that remains inside the independently established hull/divisor-safe branch domain:

\[
|F_v(z)-F_v(z')|
\le L_{v,b}\|z-z'\|_\infty.
\]

Set

\[
L_K=\max_{v,b}L_{v,b}.
\]

## Nodewise propagation

With

\[
r_K=\max_{v,b} r_{v,b}
\]

and

\[
\Phi(L,D)=\sum_{j=0}^{D}L^j,
\]

a valid coarse cell constant is

\[
C_{\rm cell}(K)
=
r_K\Phi(L_K,D_K).
\]

Then every qualified cell output satisfies

\[
e_{\rm cell}\le C_{\rm cell}(K)2^{-p}.
\]

A sharper nodewise recursive constant is permitted.

## A8 — additive prefix structure

For RIFC Darboux accumulation,

\[
P_k=P_{k-1}+G_k
\]

with no nonlinear reuse of the previous prefix.

If

\[
|\widehat G_k-G_k|
\le C_{\rm gain}(K)2^{-p},
\]

then

\[
|\widehat P_m-P_m|
\le
m\,[C_{\rm gain}(K)+r_{\rm pref,K}]2^{-p}.
\]

For \(m_n=2^n\),

\[
E_{\rm prefix}(n)
\le
C_{\rm prefix}(K)2^n2^{-p_n}.
\]

Non-additive recurrent validated integrators require their own stability theorem.

## Parametric IR-A4-R theorem

Let

\[
C_*(K)
=
\max\{C_{\rm cell}(K),C_{\rm prefix}(K),C_{\rm wrap}(K)\}.
\]

For a nonempty RIFC prefix computation with \(N_n\ge2^n\), an explicit sufficient whole-expression constant is

\[
B_K=2C_*(K).
\]

Under A1–A8,

\[
\boxed{
E_{\rm arith}(n)
\le
B_KN_n2^{-p_n}
}.
\]

Thus a finite \(B_K\) exists whenever all frozen assumptions/proof obligations are met.

## General precision-growth condition

If

\[
N_n\le a2^{\beta n}+b
\]

and

\[
p_n=p_0+\gamma n,
\]

then the frozen sufficient asymptotic condition is

\[
\boxed{\gamma>\beta}.
\]

For dyadic RIFC, \(\beta=1\), so

\[
\boxed{\gamma>1}
\]

is sufficient for

\[
E_{\rm arith}(n)\to0.
\]

Under only worst-case dyadic \(\Theta(2^n)\) operation growth, \(\gamma=1\) does not force this proof bound to vanish.

The RB-024 schedule

\[
p_n=128+8n
\]

therefore satisfies the arithmetic-rate condition.

## Natural interval width is separate

RB-029 controls arithmetic excess relative to the exact natural interval graph at a fixed partition.

It does not itself control interval dependency or finite-cell Darboux range width.

For scalar endpoints,

\[
\operatorname{wid}(\widehat{\mathcal I}_n)
\le
\operatorname{wid}(\mathcal I_n^{\rm natural})
+
2E_{\rm arith}(n).
\]

RB-024 continuity/strict-margin theory remains independently necessary for eventual first-hit/no-hit certification.

## Exact-dyadic serialization theorem

If an already directed-rounded binary endpoint has exact value

\[
y=m2^e
\]

and serialization/reconstruction preserves exactly that dyadic rational, then serialization contributes exactly zero arithmetic excess.

This says nothing about finite memory/time required to materialize large \(m,e\).

## A9 — finite-source correspondence

A finite executable source may be treated as a finite member/truncation of an idealized unbounded arithmetic family only when:

- exact inputs match;
- directed arithmetic results match;
- serialization is exact;
- branch comparisons and strict certificate semantics match;
- resource exits are fail-closed;
- no resource guard is hit for the compared finite call.

Under those conditions all finite intermediate endpoints, prefixes and classifications coincide.

Idealized eventual certification does not imply that finite production always certifies.

Finite source may still return:

`RESOURCE_EXHAUSTED / UNCERTIFIED`.

## RB-028 recovery

RB-028 K01–K06 satisfies the theorem assumptions with its frozen restricted constants, including:

\[
H_K=2^{18},
\qquad
x-h>1/400,
\qquad
(x-h)^2>1/160000,
\]

\[
r_K\le2^{24},
\qquad
L_K\le2^{80},
\qquad
D_K<512,
\]

and

\[
N_n\le1024\,2^n+1024.
\]

The generic cell construction recovers a coarse cell coefficient below the already frozen RB-028 proof scale, so the RB-028 choice

\[
B_K=2^{65536}
\]

is a valid admissible overbound.

RB-028 is therefore a corollary/instance of RB-029; its domain is not enlarged.

## Failure-domain taxonomy

RB-029 does not apply automatically when any required assumption fails, including:

- active positive threshold gap can approach zero;
- semantic hull cannot be proved finite;
- denominator approaches zero;
- source graph enters branches outside a finite qualified cover;
- a transcendental primitive lacks a rigorous \(O(2^{-p})\) endpoint-rate contract;
- prefix/recurrent accumulation is nonlinear without a separate stability theorem;
- branch switching lacks stable/common enclosure semantics;
- finite resource handling changes arithmetic/certificate semantics;
- topology changes outside a finite qualified graph family.

These are theorem-assumption failures, not automatically implementation failures.

## Q-RIFC-K qualification recipe

A later NUM-ENG compact-domain qualification must proceed prospectively:

1. define \(K\);
2. prove semantic hull;
3. prove active threshold/divisor margins;
4. enumerate branch graphs;
5. bound local depth/count;
6. instantiate primitive backend constants;
7. derive endpoint Lipschitz constants;
8. prove additive-prefix structure;
9. construct \(B_K\) symbolically;
10. verify finite-source correspondence;
11. only then run finite consistency checks.

Empirical errors may not define \(B_K\).

## Preserved limitations

RB-029 does not establish:

- that arbitrary Lighthouse parameter domains satisfy its assumptions;
- a practical/tight \(B_K\);
- global first-hit completeness by itself;
- full sequential event-tape certification;
- NNE-A;
- a full chart radius;
- finite-machine unlimited eventual certification;
- performance/scaling claims;
- AI performance.

## Governance boundaries

RB-029 does not modify or replace RB-024 through RB-028.

It does not:

- alter RB-015 SCIENTIFIC FAIL;
- execute RB-020/TR-27C;
- create protected RNG;
- authorize APP-3;
- authorize v0.28 effect-bearing science;
- authorize novelty/manuscript claims.

## STOP

RB-029 is a scientific-theory freeze only.

STOP — FROZEN / STABLE SCIENTIFIC THEORY
