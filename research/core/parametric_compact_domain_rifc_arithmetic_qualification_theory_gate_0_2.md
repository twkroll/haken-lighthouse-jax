# CORE Parametric Compact-Domain RIFC Arithmetic Qualification Theory Gate 0.2

Date: 2026-10-16
Status: PASS — PARAMETRIC COMPACT-DOMAIN IR-A4-R SUFFICIENT-CONDITION THEOREM ESTABLISHED; NO NUMERICAL EXECUTION

## 1. Authority, identity, and scope

This gate executes:

`research/master/prompts/core_parametric_compact_domain_rifc_arithmetic_qualification_theory_gate_0_2.md`.

Canonical identity at gate start:

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- `main` HEAD: `9db0f56b1efe7124e4c82cd41ec11f7cb9f59313`
- MASTER prompt blob: `1449a9d6d34126476645aa009d1d29e35ca2a364`
- RB-024 blob: `ef495dcc4cccdfd9ece7a074446b0c62dd393779`
- RB-025 blob: `06c1167c9d50cc93d08217870177f5214649d088`
- RB-027 blob: `62161ed19afe80dda0a22191f874c88fc4a9155b`
- RB-028 blob: `5e69cc66bf7e26b3bc3d3043f13b8f29c7cb12b9`
- RB-028 derivation blob on `engineering/numerics-v0.1`:
  `7a38c49cb2b6715dc6dbbc9e9f8d3cdf510e0e55`
- RB-028 finite-correspondence blob on `engineering/numerics-v0.1`:
  `c3227d11f5b661aed962b0df4cc96399ebf344f3`.

RB-015 remains immutable `SCIENTIFIC FAIL`.

This is a THEORY gate only.

No executable source was modified. No interval calculation, numerical experiment, benchmark, protected RNG, TR-27C run, APP-3 run, v0.28 effect-bearing experiment, novelty analysis, or manuscript claim was produced.

The goal is not a universal interval-arithmetic theorem for arbitrary programs. It is a reusable sufficient-condition theorem for the RIFC positive-certificate graph class described below.

---

# Part I — T1: abstract directed-rounding arithmetic model

## 2. Exact semantic graph and arithmetic graph

Let \(K\) be a compact set of exact RIFC inputs.

For one dyadic cell and one positive-certificate branch, let

\[
\mathcal G=(V,E)
\]

be a finite directed acyclic graph of exact real endpoint maps.

A node \(v\in V\) computes an exact semantic endpoint

\[
x_v=F_v(x_{u_1},\ldots,x_{u_d})
\]

from predecessor endpoints.

The implemented directed arithmetic graph computes an outward endpoint

\[
\widehat x_v.
\]

The **natural interval/range width** of the exact interval graph and the **arithmetic excess** caused by finite precision are distinct quantities.

For a scalar endpoint node define

\[
e_v
=
|\widehat x_v-x_v|.
\]

For an interval endpoint pair use the max endpoint displacement norm.

## 3. Primitive class

### Assumption A1 — directed inclusion

**Label:** ASSUMPTION.

Every inexact arithmetic primitive used by the positive-certificate graph is evaluated in a specified directed mode and encloses the corresponding exact real endpoint.

The supported abstract primitive family is:

1. rational endpoint load;
2. \(+\);
3. \(-\);
4. multiplication;
5. division on a divisor set bounded away from zero;
6. exponential;
7. exact comparisons;
8. min/max/hull/intersection;
9. exact dyadic serialization of an already rounded endpoint.

Optional square root is outside the core theorem unless an individual qualification supplies the same assumptions for it.

### Assumption A2 — primitive rate

**Label:** ASSUMPTION.

For every branch \(b\) of the qualified graph there is a compact semantic operand set \(C_{v,b}\) for every primitive node \(v\), and a finite constant \(r_{v,b}\) such that at precision \(p\),

\[
\boxed{
|\operatorname{fl}^{\pm}_{p,v}(z)-F_v(z)|
\le
r_{v,b}\,2^{-p}
}
\tag{3.1}
\]

for every exact operand tuple \(z\in C_{v,b}\).

This is an **absolute endpoint-error** bound.

It may be derived from a relative correct-rounding model together with a semantic magnitude bound.

### Rational endpoint load

Raw integer numerator/denominator magnitudes need not belong to one compact real interval.

It is sufficient that the semantic exact rational value belongs to a bounded compact set and that the load composite itself has a proved rate of the form (3.1).

Thus the theorem treats exact-rational loading as a semantic primitive, not as an assertion that arbitrarily large parse integers lie in the scalar semantic hull.

### Exact operations

Exact comparison, min/max/hull/intersection on already represented exact endpoints contribute

\[
r_{v,b}=0
\]

when their branch semantics are stable or when all possible finite branches are explicitly included in the branch partition.

Exact dyadic serialization likewise contributes zero; see Part VIII.

---

# Part II — T2/T3: compact semantic hull and divisor separation

## 4. Branch partition

### Assumption A3 — finite branch cover

**Label:** ASSUMPTION.

The positive-certificate source graph over \(K\) is covered by a finite branch family

\[
\mathcal B_K=\{b_1,\ldots,b_J\}.
\]

For every exact input in \(K\), every positive-certificate path belongs to at least one \(b\in\mathcal B_K\).

A branch may include threshold cases such as:

- fully subthreshold;
- threshold-straddling;
- fully above threshold.

Changing branch structure outside this finite cover is outside the theorem.

## 5. Noncircular semantic hull

### Assumption A4 — semantic hull

**Label:** ASSUMPTION / PROOF OBLIGATION.

For every branch \(b\), before using any whole-graph arithmetic excess estimate, prove from exact model/range properties and branch semantics that every exact semantic endpoint in the local positive-certificate graph obeys

\[
|x_v|\le H_{K,b}<\infty.
\tag{5.1}
\]

Set

\[
H_K=\max_{b\in\mathcal B_K}H_{K,b}.
\tag{5.2}
\]

The proof of (5.1) may use:

- compactness of \(K\);
- continuity of exact endpoint maps;
- exact physical/model bounds;
- monotonicity;
- exact Darboux range bounds;
- branch-specific inequalities.

It may **not** use the final coarse arithmetic bound whose existence is being proved.

### Proposition 1 — compact image criterion

**Label:** PROPOSITION / PROVED.

If \(K_b\subseteq K\) is compact and every exact endpoint map along branch \(b\) is continuous on its predecessor semantic image, with all singular denominators excluded, then the finite graph image is compact and therefore admits a finite \(H_{K,b}\).

### Proof

Finite composition of continuous maps sends compact sets to compact sets. A finite union of compact node images is compact and bounded. QED.

## 6. Active reciprocal separation

### Assumption A5 — divisor/threshold separation

**Label:** ASSUMPTION / PROOF OBLIGATION.

For every node that evaluates a reciprocal or division, its exact denominator \(d\) satisfies a branchwise lower bound

\[
|d|\ge\delta_{K,b}>0.
\tag{6.1}
\]

Set

\[
\delta_K
=
\min_{b\in\mathcal B_K}
\delta_{K,b}
>0.
\tag{6.2}
\]

### RIFC response specialization

For the frozen response top branch,

\[
S(x)
=
\exp\!\left[-r/(x-h)^2\right],
\qquad x>h,
\]

every endpoint actually passed to the reciprocal branch must satisfy

\[
x-h\ge\delta_{x,K}>0.
\tag{6.3}
\]

Then the squared reciprocal denominator obeys

\[
(x-h)^2
\ge
\delta_{x,K}^2.
\tag{6.4}
\]

### Fully subthreshold branch

If the branch returns the exact response \(0\), no reciprocal node is evaluated and no positive gap is required for that branch.

### Threshold-straddling branch

The monotone lower response endpoint is \(0\).

Any positive upper endpoint actually passed through the reciprocal/exponential top graph must still obey (6.3) for the present arithmetic-rate theorem.

### Why separation is necessary for this graph theorem

**Label:** PROPOSITION / PROVED.

There is no uniform finite semantic hull or Lipschitz majorant for the intermediate reciprocal graph

\[
x\mapsto 1/(x-h)^2
\]

over a family allowing

\[
x-h\downarrow0^+.
\]

Indeed the intermediate tends to \(+\infty\).

The smoothness of the composed physical response \(S(x)\) at \(x=h\) does not remove this source-graph intermediate singularity.

Therefore an arbitrarily near-threshold positive branch is outside this theorem unless the implementation uses a different qualified expression graph.

---

# Part III — T4: source-graph structure and operation count

## 7. Local DAG assumptions

### Assumption A6 — bounded local graph

**Label:** ASSUMPTION.

For every qualified branch and every dyadic cell:

- local primitive count is at most
  \[
  c_K<\infty;
  \]
- local dependency depth is at most
  \[
  D_K<\infty;
  \]
- predecessor fan-in is finite.

All fixed wrapper/final-comparison work outside the cell loop is bounded by

\[
b_K<\infty
\]

primitive operations.

## 8. Operation-count theorem

**Label:** THEOREM / PROVED.

Let the level-\(n\) dyadic partition contain

\[
m_n=2^n
\]

cells.

Then

\[
\boxed{
N_n
\le
a_K2^n+b_K
}
\tag{8.1}
\]

with

\[
a_K=c_K+c_{\rm prefix,K},
\tag{8.2}
\]

where \(c_{\rm prefix,K}\) is the fixed number of primitive operations used by one prefix update.

### Proof

Each cell evaluates at most \(c_K\) local primitives and one bounded prefix-update graph.

There are \(2^n\) cells.

Everything outside that loop contributes at most \(b_K\). QED.

### Qualification

This is a primitive-operation count.

It is not a bound on:

- bit complexity;
- memory;
- arbitrary-precision integer serialization cost;
- wall time.

---

# Part IV — T5: nodewise arithmetic propagation

## 9. Endpoint-map Lipschitz constants

### Assumption A7 — local endpoint stability

**Label:** ASSUMPTION / PROOF OBLIGATION.

For every node \(v\) in every qualified branch, the exact endpoint map \(F_v\) is Lipschitz on a compact neighborhood containing the semantic predecessor image and the permitted outward perturbation tube.

Using the predecessor max norm,

\[
|F_v(z)-F_v(z')|
\le
L_{v,b}\,
\|z-z'\|_\infty.
\tag{9.1}
\]

Set

\[
L_K
=
\max_{v,b}L_{v,b}
<\infty.
\tag{9.2}
\]

The perturbation tube must remain inside the already established semantic/divisor-safe branch domain.

This condition prevents use of the final global error bound to justify its own denominator assumptions.

## 10. Nodewise recurrence

### Lemma 1 — local error recursion

**Label:** LEMMA / PROVED.

Under A1–A7,

\[
e_v
\le
L_{v,b}
\max_{u\prec v}e_u
+
r_{v,b}2^{-p}.
\tag{10.1}
\]

### Proof

Insert and subtract the exact map evaluated at the rounded predecessor vector:

\[
|\widehat x_v-x_v|
\le
|\widehat x_v-F_v(\widehat z)|
+
|F_v(\widehat z)-F_v(z)|.
\]

The first term is bounded by the primitive directed-rounding rate.

The second is bounded by (9.1). QED.

## 11. Explicit cell constant

Let

\[
r_K=\max_{v,b}r_{v,b}.
\tag{11.1}
\]

Define

\[
\Phi(L,D)
=
\sum_{j=0}^{D}L^j.
\tag{11.2}
\]

Equivalently,

\[
\Phi(L,D)
=
\begin{cases}
D+1,&L=1,\\
\dfrac{L^{D+1}-1}{L-1},&L\ne1.
\end{cases}
\tag{11.3}
\]

### Theorem 2 — local cell arithmetic excess

**Label:** THEOREM / PROVED.

For every local cell output node,

\[
\boxed{
e_{\rm cell}
\le
C_{\rm cell}(K)\,2^{-p},
}
\tag{11.4}
\]

where the coarse explicit choice

\[
\boxed{
C_{\rm cell}(K)
=
r_K\,
\Phi(L_K,D_K)
}
\tag{11.5}
\]

is sufficient, after including endpoint-load nodes in \(D_K\).

### Proof

Apply (10.1) inductively along a topological layering of the finite DAG.

At each layer the worst predecessor error is multiplied by at most \(L_K\), then one new primitive error at most \(r_K2^{-p}\) is added.

Summing the finite geometric series gives (11.5). QED.

### Sharper recursive construction

**Label:** PROPOSITION.

A less conservative explicit constant is obtained nodewise from

\[
C_v
=
r_{v,b}
+
L_{v,b}\max_{u\prec v}C_u,
\tag{11.6}
\]

with input-load nodes initialized by their load constants.

Then

\[
C_{\rm cell}(K)
=
\max_{v\in V_{\rm cell},\,b}
C_v.
\tag{11.7}
\]

This is often much smaller than (11.5), but both are finite under the same assumptions.

---

# Part V — T6: additive prefix accumulation

## 12. Prefix structure

### Assumption A8 — additive prefix update

**Label:** ASSUMPTION.

The exact accumulated Darboux prefix has the form

\[
P_k=P_{k-1}+G_k,
\qquad
P_0=0,
\tag{12.1}
\]

where \(G_k\) is the exact natural interval cell-gain endpoint.

The finite-precision implementation uses one directed addition graph for the update and does not feed \(P_{k-1}\) through a nonlinear map before the next accumulation.

Let its one-update primitive arithmetic constant be

\[
r_{\rm pref,K}<\infty.
\]

## 13. Prefix theorem

**Label:** THEOREM / PROVED.

If every cell gain endpoint obeys

\[
|\widehat G_k-G_k|
\le
C_{\rm gain}(K)2^{-p},
\tag{13.1}
\]

then after \(m\) cells,

\[
\boxed{
|\widehat P_m-P_m|
\le
m
\left[
C_{\rm gain}(K)+r_{\rm pref,K}
\right]
2^{-p}.
}
\tag{13.2}
\]

### Proof

One step gives

\[
|\widehat P_k-P_k|
\le
|\widehat P_{k-1}-P_{k-1}|
+
|\widehat G_k-G_k|
+
r_{\rm pref,K}2^{-p}.
\]

Induction from \(P_0=0\) yields (13.2). QED.

### RIFC dyadic corollary

With

\[
m_n=2^n,
\]

\[
\boxed{
E_{\rm prefix}(n)
\le
C_{\rm prefix}(K)
2^n2^{-p_n},
}
\tag{13.3}
\]

where

\[
C_{\rm prefix}(K)
=
C_{\rm gain}(K)+r_{\rm pref,K}.
\tag{13.4}
\]

### Why additivity matters

**Label:** INTERPRETATION.

A nonlinear recurrence such as

\[
P_k=F(P_{k-1},G_k)
\]

with Lipschitz factor \(L>1\) in the old prefix could amplify old error geometrically in \(k\).

Such a graph is not covered by (13.2) unless a separate stability theorem bounds the recurrence.

---

# Part VI — T7: parametric IR-A4-R theorem

## 14. Whole-graph constant

Let

\[
C_{\rm wrap}(K)
\]

bound the arithmetic excess of fixed-depth positive-certificate wrapper outputs outside the prefix loop.

Define

\[
C_*(K)
=
\max
\left\{
C_{\rm cell}(K),
C_{\rm prefix}(K),
C_{\rm wrap}(K)
\right\}.
\tag{14.1}
\]

For a nonempty cell computation,

\[
N_n\ge 2^n.
\tag{14.2}
\]

Define the explicit whole-expression constant

\[
\boxed{
B_K
=
2C_*(K).
}
\tag{14.3}
\]

Any larger finite constant is also valid.

## 15. Parametric compact-domain IR-A4-R theorem

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

Let \(K\) and a finite positive-certificate branch family satisfy A1–A8.

Then there is a finite explicit constant \(B_K\), for example (14.3), such that at every dyadic refinement level \(n\),

\[
\boxed{
E_{\rm arith}(n)
\le
B_KN_n2^{-p_n}.
}
\tag{15.1}
\]

### Proof

Every local cell/wrapper endpoint has arithmetic excess at most

\[
C_*(K)2^{-p_n}.
\]

The prefix endpoint after at most \(2^n\) cells has excess at most

\[
C_*(K)2^n2^{-p_n}.
\]

Using \(N_n\ge2^n\) for the nonempty prefix graph and \(N_n\ge1\),

\[
E_{\rm arith}(n)
\le
2C_*(K)N_n2^{-p_n}.
\]

Thus (15.1) holds with (14.3). QED.

### Noncircularity

The finiteness of \(B_K\) follows from:

1. semantic compactness;
2. divisor separation;
3. primitive backend rates;
4. finite local graph depth/count;
5. additive prefix structure.

The final \(B_K\) is not used to prove the semantic hull or divisor margin.

## 16. Precision-growth theorem

Suppose more generally

\[
N_n
\le
a\,2^{\beta n}+b
\tag{16.1}
\]

and

\[
p_n=p_0+\gamma n.
\tag{16.2}
\]

Then

\[
E_{\rm arith}(n)
\le
B_K
\left(a2^{\beta n}+b\right)
2^{-p_0-\gamma n}.
\tag{16.3}
\]

### Corollary — sufficient growth condition

**Label:** COROLLARY / PROVED.

If

\[
\boxed{
\gamma>\beta,
}
\tag{16.4}
\]

then

\[
E_{\rm arith}(n)\to0.
\tag{16.5}
\]

### Dyadic RIFC specialization

For

\[
m_n=2^n,
\qquad
\beta=1,
\]

a sufficient condition is

\[
\boxed{
\gamma>1.
}
\tag{16.6}
\]

Therefore the RB-024 schedule

\[
p_n=128+8n
\]

satisfies the arithmetic convergence condition with substantial margin.

### Sharpness qualification

Under only the worst-case upper-bound information (16.1), \(\gamma=1\) does not force the right-hand side to vanish and \(\gamma<1\) cannot provide a general convergence guarantee.

Thus \(\gamma>1\) is the sharp threshold for this proof form when operation growth is genuinely of dyadic order \(\Theta(2^n)\).

This is a proof-rate statement, not an optimal computational-cost claim.

---

# Part VII — natural interval width versus arithmetic excess

## 17. Separation theorem

**Label:** PROPOSITION / PROVED.

The arithmetic theorem controls displacement between:

- the exact natural interval expression graph at the chosen finite partition; and
- its finite-precision directed evaluation.

It does not control the exact interval/Darboux range width caused by:

- nonzero input intervals;
- interval dependency;
- finite time-cell width.

Therefore

\[
\operatorname{wid}(\widehat{\mathcal I}_n)
\le
\operatorname{wid}(\mathcal I_n^{\rm natural})
+
2E_{\rm arith}(n)
\tag{17.1}
\]

for scalar endpoint intervals under the max endpoint metric.

RB-024's continuity/strict-margin theory is still required for natural interval/Darboux widths to shrink in deterministic regular cases.

IR-A4-R alone is not a first-hit completeness theorem.

---

# Part VIII — T8: exact-dyadic serialization

## 18. Exact serialization theorem

**Label:** THEOREM / PROVED.

Suppose an already directed-rounded finite binary endpoint has exact value

\[
y=m2^e
\]

with integer \(m,e\).

If serialization returns that same integer pair and reconstructs the exact rational

\[
m2^e
\]

without an additional approximate conversion, then serialization adds

\[
\boxed{
0
}
\]

arithmetic excess.

### Qualification

The bit length of \(m\) and magnitude of \(e\) may grow with precision.

Zero arithmetic error does not imply constant memory or time cost.

A finite production source may fail closed when exact materialization exceeds resource bounds.

This does not change the arithmetic theorem for the corresponding idealized exact-serialization family.

---

# Part IX — T9: finite-source correspondence

## 19. Idealized family

Let

\[
\mathcal S_\infty(p,n)
\]

be an idealized arithmetic family with:

- the same exact source expression graph;
- the same branch comparisons;
- the same directed rounding modes;
- the same exact serialization semantics;
- the same certificate inequalities;

but without finite limits on:

- working precision;
- exponent range;
- integer/significand storage;
- text/artifact size;
- refinement level.

## 20. Finite executable source

Let

\[
\mathcal S_{\rm fin}
\]

be an executable implementation that adds only explicit resource guards to the same graph.

### Assumption A9 — fail-closed resource policy

If a requested call exceeds a finite resource guard, the finite source exits with an uncertified/resource outcome.

It does not:

- substitute another arithmetic primitive;
- widen by an unqualified fallback;
- silently truncate;
- change branch/certificate semantics.

## 21. Finite-source correspondence theorem

**Label:** THEOREM / PROVED.

Assume:

1. \(\mathcal S_{\rm fin}\) and \(\mathcal S_\infty\) begin from identical exact inputs;
2. every executed finite primitive uses the same directed arithmetic result as the corresponding ideal primitive;
3. serialization is exact in both;
4. branch comparisons and strict certificate conditions are identical;
5. no finite resource guard is hit.

Then every intermediate endpoint, branch decision, prefix value, certificate classification and serialized proof datum is identical between the finite source and the corresponding finite member of the idealized family.

### Proof

Structural induction over the finite arithmetic DAG proves equality of corresponding local endpoints.

Induction over the finite prefix list proves equality of all accumulated prefixes.

Identical exact comparisons then select identical branches and classifications. QED.

## 22. Resource-bound non-implication

**Label:** COROLLARY / PROVED.

Even if the idealized family satisfies eventual certification as

\[
n\to\infty,
\]

it does not follow that a finite production implementation always certifies.

A finite implementation may reach a precision, refinement, exponent, integer-size, memory, or runtime guard first and return

\[
\boxed{
\texttt{RESOURCE\_EXHAUSTED / UNCERTIFIED}.
}
\]

This is fully compatible with the idealized theorem.

---

# Part X — T10: RB-028 as a corollary

## 23. RB-028 assumptions instantiated

RB-028 establishes prospectively, for K01–K06:

\[
H_K=2^{18},
\tag{23.1}
\]

an active positive response gap

\[
x-h>1/400,
\tag{23.2}
\]

and therefore squared reciprocal divisor

\[
(x-h)^2>1/160000.
\tag{23.3}
\]

It establishes a primitive local budget

\[
r_K\le2^{24},
\tag{23.4}
\]

a coarse endpoint Lipschitz majorant

\[
L_K\le2^{80},
\tag{23.5}
\]

local dependency depth

\[
D_K<512,
\tag{23.6}
\]

and per-cell operation count below

\[
c_K=1024.
\tag{23.7}
\]

The prefix update is additive.

Exact dyadic export contributes zero additional arithmetic error.

The operation count satisfies

\[
N_n
\le
1024\,2^n+1024,
\tag{23.8}
\]

and

\[
N_n\ge2^n.
\tag{23.9}
\]

## 24. Cell-constant recovery

Using the generic coarse formula,

\[
C_{\rm cell}
\le
2^{24}
\sum_{j=0}^{512}
(2^{80})^j.
\tag{24.1}
\]

A simple overbound is

\[
C_{\rm cell}
<
513\,
2^{24}\,
2^{80\cdot512}
<
2^{41000}.
\tag{24.2}
\]

Thus the RB-028 cell proof is recovered as a special instance of Theorem 2.

The additive-prefix theorem then yields a finite coefficient below a coarse constant of order

\[
2^{41002}.
\tag{24.3}
\]

RB-028's prospectively frozen

\[
\boxed{
B_K=2^{65536}
}
\tag{24.4}
\]

therefore safely dominates the generic sufficient construction.

## 25. RB-028 corollary

**Label:** COROLLARY / PROVED.

K01–K06 satisfy A1–A9 for the restricted positive-certificate graph qualified in RB-028.

Therefore the parametric theorem gives

\[
E_{\rm arith}(n)
\le
B_KN_n2^{-p_n}
\]

for a finite \(B_K\).

The already frozen RB-028 choice

\[
B_K=2^{65536}
\]

is one admissible coarse constant.

With

\[
p_n=128+8n,
\]

\[
E_{\rm arith}(n)\to0.
\]

Thus RB-028 is an instance of the parametric compact-domain theorem rather than a separate logical pattern.

### Preserved restriction

This corollary does not enlarge K01–K06.

RB-028 itself remains unchanged.

---

# Part XI — T11: theorem failure domains

## 26. Assumption-failure taxonomy

The following are **theorem-assumption failures**, not automatically implementation failures.

### F1 — arbitrarily vanishing active threshold gap

If an endpoint actually sent through the reciprocal response graph can satisfy

\[
x-h\downarrow0^+,
\]

no finite \(\delta_K\) exists for that graph.

The present theorem does not apply.

### F2 — unbounded semantic hull

If no finite \(H_K\) can be proved independently of the desired whole-graph error bound, the theorem does not apply.

### F3 — divisor approaching zero

For any division node with no positive divisor lower bound, uniform node Lipschitz and rate constants may diverge.

### F4 — uncovered branch topology

If the source can enter expression branches not represented in a finite qualified branch cover, no single finite theorem instance has been established.

### F5 — unsupported transcendental primitive rate

If an invoked transcendental primitive lacks a rigorous directed \(O(2^{-p})\)-type endpoint contract on the relevant compact set, A2 fails.

Finite outward inclusion may still be possible under another theorem, but this rate theorem does not follow.

### F6 — nonlinear recurrent accumulation

If the old prefix is repeatedly passed through a nonlinear map with amplification not uniformly stabilized, the additive-prefix theorem does not apply.

A separate recurrence-stability bound is required.

### F7 — branch instability without common semantics

If finite arithmetic perturbation can switch between branches whose endpoint maps do not agree on the guard boundary and no robust guard margin/common enclosure theorem is available, A3/A7 fail.

### F8 — non-fail-closed finite fallback

If a finite source changes arithmetic semantics after hitting a resource limit, finite-source correspondence fails.

### F9 — parameter-dependent topology outside finite cover

Structural graph creation/deletion or other topology changes not represented in the qualified finite graph family are outside the theorem.

---

# Part XII — T12: implementation-facing compact-domain qualification recipe

## 27. Qualification recipe Q-RIFC-K

**Label:** PROPOSITION / PROSPECTIVE METHODOLOGY — NOT EXECUTED.

A later NUM-ENG gate qualifying a new compact domain must perform these steps in this order.

### Step 1 — define K prospectively

Specify exact parameter/state/time/phase-gap/weight/delay ranges before qualification output.

### Step 2 — prove the semantic hull

Using exact model and branch semantics, establish branchwise \(H_{K,b}\).

Do not use the desired \(B_K\) to prove this hull.

### Step 3 — prove threshold/divisor separation

For every active reciprocal/division branch, establish \(\delta_{K,b}>0\).

Classify subthreshold/straddling branches separately.

### Step 4 — enumerate branch graphs

List the finite branch family and every primitive that can appear in a positive certificate.

### Step 5 — bound local structure

Establish:

\[
D_K,\qquad c_K,\qquad b_K.
\]

Derive

\[
N_n\le a_K2^n+b_K.
\]

### Step 6 — instantiate backend constants

For each primitive derive \(r_{v,b}\) from the backend correct-rounding/inclusion contract and semantic operand bounds.

For exact serialization use zero arithmetic excess.

### Step 7 — instantiate endpoint stability

Derive \(L_{v,b}\) on the independently proven compact/divisor-safe domain.

Compute \(C_{\rm cell}\) recursively or via the coarse geometric formula.

### Step 8 — prove prefix structure

Verify that Darboux prefix accumulation is additive and derive \(C_{\rm prefix}\).

### Step 9 — compute B_K symbolically

Construct a finite \(B_K\) before numerical validation output.

The constant may be deliberately conservative.

It may not be fitted to observed errors.

### Step 10 — verify finite-source correspondence

Audit exact graph, branch, rounding, serialization, strict-comparison and fail-closed resource semantics.

### Step 11 — only then run finite consistency checks

Numerical checks may test implementation consistency with the already fixed proof constant.

They may not define the proof.

---

# Part XIII — boundary between theorem, finite software, and Lighthouse science

## 28. What the theorem establishes

**Label:** INTERPRETATION.

For a compact domain satisfying A1–A8, the idealized directed arithmetic family has a finite whole-expression IR-A4-R constant.

If its cell count grows as \(2^n\) and precision grows faster than one bit per dyadic level, its arithmetic excess tends to zero.

Combined with RB-024's independent strict-margin/natural-enclosure convergence assumptions, this supports eventual certification in the mathematical idealized family.

## 29. What the theorem does not establish

**Label:** INTERPRETATION / NON-RESULT.

It does not establish:

- that every Lighthouse parameter domain satisfies the assumptions;
- that a finite machine reaches the required refinement;
- a practical or tight \(B_K\);
- full sequential event-tape certification;
- NNE-A;
- a full chart radius;
- simulator global correctness;
- scientific speedup;
- AI performance.

A huge valid proof constant is compatible with an impractical implementation.

## 30. No empirical promotion

RB-025/RB-028 finite QA remains engineering evidence.

The present theorem is analytical and does not rely on empirical error fitting.

---

# Part XIV — open questions

## 31. Near-threshold source graphs

**Label:** OPEN QUESTION.

Can one design a source graph for the smooth response that preserves a uniform compact arithmetic hull even when positive endpoint gaps approach \(h\) arbitrarily closely, without evaluating the singular reciprocal intermediate?

Such a graph could enlarge the domains covered by the theorem.

## 32. Non-additive validated integrators

**Label:** OPEN QUESTION.

Taylor-model or interval-ODE integrators may have better range behavior but require their own recurrent stability theorem.

## 33. Parameter-box full chart certification

**Label:** OPEN QUESTION.

The arithmetic theorem does not solve the RB-024 NNE-A/no-new-event problem for full parameter families.

## 34. Practical precision schedules

**Label:** OPEN QUESTION.

The sufficient condition \(\gamma>1\) concerns asymptotic arithmetic excess.

Practical optimal precision/refinement schedules under finite resource constraints remain an engineering problem.

---

# Part XV — gate decision

## 35. Decision

# PASS — PARAMETRIC COMPACT-DOMAIN RIFC ARITHMETIC QUALIFICATION THEOREM ESTABLISHED

The gate genuinely generalizes RB-028.

It does not require replaying each finite fixture.

The reusable sufficient assumptions are:

1. finite branch cover;
2. independently proved compact semantic hull;
3. positive divisor/active-threshold separation;
4. directed primitive endpoint rate \(O(2^{-p})\);
5. finite local DAG depth/count;
6. finite endpoint-map Lipschitz majorants;
7. additive prefix accumulation;
8. exact/finitely qualified serialization;
9. fail-closed finite-source correspondence.

Under these assumptions an explicit finite

\[
B_K
\]

exists and

\[
E_{\rm arith}(n)
\le
B_KN_n2^{-p_n}.
\]

For dyadic refinement, any linear precision schedule

\[
p_n=p_0+\gamma n
\]

with

\[
\gamma>1
\]

forces the arithmetic excess bound to vanish.

RB-028 is recovered as a corollary.

No numerical execution occurred.

## 36. Proposed freeze

If MASTER accepts this result, establish:

`CORE Parametric Compact-Domain RIFC Arithmetic Qualification Theory Freeze 0.2`.

The freeze should include:

- A1–A9;
- Theorems 1–2 and Parts V–IX;
- the explicit \(B_K\) construction;
- the \(\gamma>1\) dyadic schedule condition;
- exact-dyadic serialization theorem;
- finite-source correspondence theorem;
- RB-028 recovery corollary;
- failure-domain taxonomy;
- qualification recipe Q-RIFC-K;
- explicit exclusions/open questions.

It must not broaden RB-028's frozen domain or authorize numerical execution.

## STOP

STOP — RETURN TO MASTER
