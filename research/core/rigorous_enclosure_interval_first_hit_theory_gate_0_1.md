# CORE Rigorous Enclosure & Interval First-Hit Certification Theory Gate 0.1

Date: 2026-10-16
Status: PASS — CONSTRUCTIVE OUTWARD-VALID INTERVAL CERTIFICATION THEORY ESTABLISHED; NO NUMERICAL EXECUTION

## 1. Authority, identity, and scope

This gate executes the MASTER-authorized prompt

`research/master/prompts/core_rigorous_enclosure_interval_first_hit_theory_gate_0_1.md`.

Canonical identity at gate start:

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- `main` HEAD at gate start: `df504c802f9aeebaed70eea4cac4eb3a230e3f90`
- CORE STATUS blob: `b8ddbaf838eebb4d75b037afc8dfad9b84c62de5`
- MASTER prompt blob: `43b54f971335d4026a81abe5b2fbea13bb9eca31`
- MASTER STATUS blob: `6f0071832fab63c767edb92120a9d1b695d67c3f`
- MASTER project-status blob: `8a8042b6bf0374ee2f391edd7da86c05eedd1e57`
- MASTER decision-log blob: `18ff9fa8f25a57bf2dfad7055bec2cd0a9b574c9`
- PROJECT_GOVERNANCE blob: `1c9680db72f6e562b3efbeda2cdeca45c9d5f38a`
- command protocol blob: `f362f8d3628b29cf9482bc40a448098877f5dd0c`
- RB-004 blob: `d84a2f8c23b0bb0d6be4867a42a6fea235232f20`
- RB-012 blob: `e371e0cc8b645eb23cbb683d2ed8997ccb9dc62f`
- RB-019 blob: `68c674e50772620960b5e52092b9f6cd606d8f42`
- RB-020 blob: `b2015acc18da13755f078187895f274418751460`
- RB-021 blob: `88cac66ae5dbeb4f5ca9d006fcca2d2c4c792b0b`
- RB-022 blob: `89ab77edb932025c75277e98c0543d09f987ab92`
- RB-023 blob: `3e67d98a47703e1b05890c085de3df71b53ecd24`.

RB-015 remains immutable `SCIENTIFIC FAIL`.

This is a THEORY gate only. No interval library was executed or benchmarked. No floating-point fixture, TR-27C check, `2711xxx` RNG object, APP-3 task, v0.28 effect-bearing experiment, novelty analysis, or manuscript claim was executed.

### Claim discipline

Every new statement is labelled with one of:

- THEOREM / PROVED
- PROPOSITION
- LEMMA
- ASSUMPTION
- INTERPRETATION
- OPEN QUESTION.

RB-023 finite float64 agreement is not used as proof of interval inclusion.

---

# Part I — I1: finite outward-valid interval arithmetic

## 2. Interval representation

### IR-A1 — finite endpoint representation

**Label:** ASSUMPTION.

At working precision \(p\), a finite real interval is represented by

\[
X=[\underline x,\overline x],
\qquad
\underline x,\overline x\in\mathbb F_p,
\qquad
\underline x\le\overline x,
\]

with the semantic invariant

\[
x_{\rm true}\in X.
\]

The implementation may additionally use \(\pm\infty\) as fail-closed overflow endpoints. A positive finite certificate may not rely on an infinite endpoint.

### IR-A2 — directed arithmetic

**Label:** ASSUMPTION / IMPLEMENTATION PROOF OBLIGATION.

For each primitive real operation \(\circ\in\{+,-,\times,\div\}\), the interval backend provides endpoint operations rounded toward \(-\infty\) and \(+\infty\).

For example,

\[
X+Y
=
[
\operatorname{rdn}(\underline x+\underline y),
\operatorname{rup}(\overline x+\overline y)
].
\]

Multiplication uses outward-rounded enclosures of all four endpoint products.

Division is allowed only when \(0\notin Y\); otherwise the result is unbounded/inconclusive.

Every square, absolute value, minimum/maximum hull, and affine combination used below is built from inclusion-preserving primitives.

### IR-A3 — rigorous exponential

**Label:** ASSUMPTION / CRITICAL PROOF OBLIGATION.

The backend provides a rigorous exponential interval primitive

\[
\operatorname{Exp}_p([a,b])
\supseteq
\{e^x:x\in[a,b]\},
\]

with outward endpoints.

A usual libm `exp` followed only by `nextafter` is **not** accepted as a proof of inclusion unless a separate proved libm error bound makes the enclosure valid.

A correctly rounded or otherwise formally bounded arbitrary-precision exponential is sufficient.

### IR-A4 — refinement precision

**Label:** ASSUMPTION.

There is a sequence of valid arithmetic backends with increasing precision \(p\to\infty\) such that, on every fixed compact finite input domain, primitive interval overestimation from rounding tends to zero.

The constructive algorithm below uses

\[
p_n=p_0+8n,
\qquad
p_0=128\ {\rm bits},
\tag{2.1}
\]

at dyadic refinement level \(n\).

The particular values \(128\) and \(8\) are algorithm-definition choices, not theorem constants and not empirical tolerances.

### IR-A5 — bounded-domain no-silent-overflow rule

**Label:** ASSUMPTION.

If a primitive overflows, underflows in a way not covered by the backend's rigorous subnormal semantics, returns NaN, or loses its inclusion guarantee, the computation returns `UNCERTIFIED_ARITHMETIC`.

It may not replace the invalid primitive by an ordinary rounded scalar value.

---

## 3. Basic inclusion lemma

**Label:** LEMMA / PROVED.  
**Provenance:** DERIVATION HERE.

Any finite expression constructed from real inputs using only:

- constants enclosed by point/outward intervals;
- the IR-A2 arithmetic primitives;
- the IR-A3 exponential primitive;
- interval hull/intersection operations used only in inclusion-preserving directions,

produces an interval containing the exact real expression for every exact input represented by the input intervals.

### Proof

Induction on the expression tree. Each primitive encloses the image of its operand intervals. Composition preserves inclusion. QED.

---

# Part II — I2: rigorous interval alpha propagation

## 4. Arrival-free interval state

Let

\[
A=[\underline\alpha,\overline\alpha],
\qquad
0<\underline\alpha\le\overline\alpha,
\]

be an interval enclosure for \(\alpha\).

Let

\[
Q_0=[\underline q_0,\overline q_0],
\qquad
P_0=[\underline\psi_0,\overline\psi_0]
\]

enclose the exact arrival-free initial alpha state.

For a time cell

\[
I=[a,b]\subseteq[0,L],
\qquad
0\le a\le b,
\]

define

\[
E(I)
=
\operatorname{Exp}_p(-A I),
\tag{4.1}
\]

\[
Q(I)
=
E(I)Q_0,
\tag{4.2}
\]

\[
P(I)
=
E(I)\left(P_0+I Q_0\right).
\tag{4.3}
\]

## 5. Alpha-propagation inclusion theorem

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

For every exact

\[
\alpha\in A,\quad
q_0\in Q_0,\quad
\psi_0\in P_0,\quad
s\in I,
\]

the exact frozen arrival-free state

\[
q(s)=e^{-\alpha s}q_0,
\]

\[
\psi(s)=e^{-\alpha s}(\psi_0+s q_0)
\]

satisfies

\[
q(s)\in Q(I),
\qquad
\psi(s)\in P(I).
\]

### Proof

The exact formulas are compositions of multiplication, addition and exponential. Apply the basic inclusion lemma. QED.

## 6. Subdivision validity

**Label:** PROPOSITION / PROVED.

If \(I\) is subdivided into finitely many cells \(I_k\), then each \(P(I_k)\) remains a valid inclusion on that child cell.

Taking the hull of child enclosures is a valid enclosure of the parent range.

No assumption that a child enclosure must be nested inside the parent floating-point enclosure is required for validity.

## 7. Optional monotonicity sharpening

The exact derivative is

\[
\psi'(s)
=
e^{-\alpha s}
\left(
q_0-\alpha\psi_0-\alpha s q_0
\right).
\tag{7.1}
\]

Define the interval derivative enclosure

\[
D(I)
=
E(I)
\left[
Q_0-A P_0-A I Q_0
\right].
\tag{7.2}
\]

### Monotonicity proposition

**Label:** PROPOSITION / PROVED.

If

\[
\inf D(I)\ge0,
\]

then every represented trajectory is nondecreasing in \(s\) on \(I\), and a sharper valid state enclosure is

\[
P_{\rm mono}(I)
=
\operatorname{hull}\left(P([a,a]),P([b,b])\right).
\]

If

\[
\sup D(I)\le0,
\]

the same endpoint hull is valid for the nonincreasing case.

If \(0\in D(I)\), the primary algorithm falls back to (4.3).

### Singleton analytic-extremum specialization

**Label:** PROPOSITION / PROVED FROM RB-022.

When \(A,Q_0,P_0\) are singleton intervals, the exact interior stationary candidate

\[
s_c=
\frac{q_0-\alpha\psi_0}{\alpha q_0}
\]

for \(q_0\ne0\) may be included in the finite extrema set.

This is an optional sharpening only. The rigorous primary algorithm does not require division by an interval \(Q_0\) containing zero.

## 8. Structural arrival map under intervals

Let \(W_e\) be the interval for a fixed structural weight \(w_e\).

At the labelled arrival of structural edge \(e\),

\[
Q_i^+
=
Q_i^-+W_e A^2.
\tag{8.1}
\]

### Structural-zero proposition

**Label:** PROPOSITION / PROVED.

If \(0\in W_e\), topology is unchanged and the labelled arrival is retained.

If

\[
W_e=[0,0],
\]

then (8.1) encloses the identity jump exactly.

A weight interval crossing zero does not trigger edge deletion/insertion.

This carries RB-022 structural-zero semantics into interval propagation.

---

# Part III — I3: rigorous response enclosure

## 9. Fixed response parameters

The primary certification algorithm treats \(r>0\) and \(h\) as frozen exact model parameters represented by outward point intervals.

Interval uncertainty in \(r\) or \(h\) is not required for the present constructive certificate and is explicitly unsupported in Version 0.1.

Let

\[
X=[\underline x,\overline x]
\]

enclose the exact input \(\psi\).

## 10. Monotone response extension

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE + RB-022 monotonicity.

Because the frozen response is nondecreasing,

\[
S(X)
=
\left[
\underline S(X),
\overline S(X)
\right]
\]

may be defined as follows.

### Case 1 — fully below threshold

If

\[
\overline x\le h,
\]

then

\[
S(X)=[0,0].
\tag{10.1}
\]

### Case 2 — threshold straddling

If

\[
\underline x\le h<\overline x,
\]

then

\[
S(X)
=
\left[
0,\,
\operatorname{rup}S(\overline x)
\right],
\tag{10.2}
\]

where the scalar endpoint response is itself evaluated through rigorous interval primitives.

### Case 3 — fully above threshold

If

\[
h<\underline x,
\]

then

\[
S(X)
=
\left[
\operatorname{rdn}S(\underline x),
\operatorname{rup}S(\overline x)
\right].
\tag{10.3}
\]

These endpoint bounds are range-sharp in exact real arithmetic because \(S\) is monotone.

Finite floating-point endpoint intervals may be wider only because of outward rounding.

## 11. Derivative enclosures

### First derivative

**Label:** PROPOSITION / PROVED.

The global bound frozen in RB-022 is

\[
0\le S'(x)\le L_1,
\]

\[
L_1
=
\frac{2}{\sqrt r}
\left(\frac32\right)^{3/2}e^{-3/2}.
\tag{11.1}
\]

Therefore:

- if \(\overline x\le h\), \(S'(X)=[0,0]\);
- if \(X\) straddles \(h\), \(S'(X)\subseteq[0,\operatorname{rup}L_1]\);
- if \(X\) lies above \(h\), the natural interval extension of
  \[
  S'(x)=2r(x-h)^{-3}e^{-r/(x-h)^2}
  \]
  is valid; it may be sharpened by including the known critical point
  \[
  x-h=\sqrt{2r/3}
  \]
  if it lies in \(X\).

### Higher derivatives

**Label:** PROPOSITION / PROVED.

For threshold-straddling or otherwise difficult cells, a valid coarse enclosure is

\[
S^{(k)}(X)
\subseteq
[-C_k r^{-k/2},\,C_k r^{-k/2}],
\]

using the RB-022 global constants/scaling.

No singular derivative behavior occurs merely because \(X\) contains \(h\).

---

# Part IV — I4: rigorous accumulated phase-gain enclosure

## 12. Primary route: interval Darboux sums

The primary and only frozen integration route in this gate is:

\[
\boxed{\text{dyadic interval Darboux/Riemann enclosure}}
\]

using rigorous alpha-state and response interval ranges.

No alternative quadrature family is frozen here.

Let

\[
0=s_0<s_1<\cdots<s_m=L
\]

be a partition.

For cell

\[
I_k=[s_k,s_{k+1}],
\]

compute:

1. a rigorous input enclosure \(P_k\supseteq\psi(I_k)\);
2. the response enclosure
   \[
   R_k=S(P_k)
   =
   [\underline r_k,\overline r_k];
   \]
3. an outward cell-width enclosure
   \[
   \Delta_k\supseteq s_{k+1}-s_k.
   \]

Since \(S\ge0\), define

\[
\mathcal G_k
=
\Delta_k R_k.
\tag{12.1}
\]

The cumulative gain enclosure is the outward sum

\[
\mathcal G_{0:m}
=
\sum_{k=0}^{m-1}\mathcal G_k.
\tag{12.2}
\]

For prefix \(j\),

\[
\mathcal G_{0:j}
=
[\underline G_j,\overline G_j].
\tag{12.3}
\]

All sums use a deterministic fixed binary-tree reduction for the total and deterministic left-to-right prefix accumulation for bracket logic.

## 13. Phase-gain inclusion theorem

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

For every exact represented trajectory,

\[
G(L)
=
\int_0^L S(\psi(s))\,ds
\in
\mathcal G_{0:m}.
\]

Likewise,

\[
G(s_j)\in
[\underline G_j,\overline G_j]
\]

for every partition node.

### Proof

For every \(s\in I_k\),

\[
S(\psi(s))
\in
[\underline r_k,\overline r_k].
\]

Hence

\[
(s_{k+1}-s_k)\underline r_k
\le
\int_{I_k}S(\psi(s))ds
\le
(s_{k+1}-s_k)\overline r_k.
\]

Outward interval multiplication and summation preserve these inequalities. QED.

---

# Part V — I5: finite strict-margin certification

## 14. Phase-gap interval

Let

\[
D=[\underline d,\overline d],
\qquad
0<\underline d\le\overline d,
\]

enclose the remaining phase gap at the segment start.

If \(\underline d\le0\), the ordinary post-event segment precondition is not certified and the primary algorithm returns a boundary/precondition label rather than silently continuing.

## 15. Certified no-hit condition

**Label:** THEOREM / PROVED.

If

\[
\overline G_m<\underline d,
\tag{15.1}
\]

then no represented trajectory reaches the next phase section on \([0,L]\).

Output:

`CERTIFIED_NO_HIT`.

The certificate data must include at least:

- \(\mathcal G_{0:m}\);
- \(D\);
- strict margin
  \[
  \gamma_{\rm nohit}
  =
  \underline d-\overline G_m>0.
  \]

## 16. Certified regular first-hit bracket

Consider partition nodes \(s_j<s_k\).

Suppose

\[
\overline G_j<\underline d,
\tag{16.1}
\]

\[
\underline G_k>\overline d,
\tag{16.2}
\]

and for every cell \(I_\ell\subseteq[s_j,s_k]\),

\[
\underline r_\ell
\ge
\nu_{\rm cert}>0.
\tag{16.3}
\]

### First-hit bracket theorem

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

Under (16.1)–(16.3), every represented trajectory has a unique first hit in

\[
T\in(s_j,s_k),
\]

and its event velocity satisfies

\[
S(\psi(T^-))
\ge
\nu_{\rm cert}>0.
\tag{16.4}
\]

Output:

`CERTIFIED_REGULAR_HIT`

with bracket

\[
[s_j,s_k]
\]

and certified transversality lower bound \(\nu_{\rm cert}\).

### Proof

(16.1) excludes a hit by \(s_j\) for every represented trajectory.

(16.2) implies every represented trajectory has accumulated more than its maximum possible phase gap by \(s_k\).

Continuity gives a crossing.

(16.3) makes the accumulated phase strictly increasing throughout the bracket, so the crossing there is unique and transversal. QED.

## 17. Deterministic refinement sequence

At refinement level \(n\):

- use \(2^n\) equal dyadic cells;
- use working precision
  \[
  p_n=128+8n;
  \]
- recompute the complete level from the original segment data;
- test no-hit first;
- otherwise test regular-hit brackets using deterministic ordering described in Section 34.

No result from a coarser noncertifying level is treated as evidence except to continue refinement.

## 18. Enclosure-convergence lemma for singleton data

**Label:** LEMMA / PROVED UNDER IR-A1–IR-A5.

Assume:

1. \(A,Q_0,P_0,D\) are singleton exact real data represented by shrinking outward endpoint intervals as \(p_n\to\infty\);
2. the segment lies in a finite compact domain;
3. no primitive arithmetic failure occurs.

Then the width of the interval Darboux phase-gain enclosure tends to zero as \(n\to\infty\).

### Proof sketch

The exact \(\psi\) is continuous and \(S\circ\psi\) is uniformly continuous on the compact segment.

The exact upper-minus-lower Darboux gap therefore tends to zero as the dyadic mesh tends to zero.

The interval state overestimation from repeated appearance of the time variable also tends to zero with cell width.

At level \(n\), the arithmetic work is \(O(2^n)\). On a bounded domain, primitive outward rounding widths are \(O(2^{-p_n})\), so accumulated rounding contribution is bounded by

\[
C2^n2^{-p_n}
=
C2^{-128}2^{-7n}
\to0.
\]

The certified exponential primitive has the same shrinking-precision property by IR-A4.

Thus total enclosure width tends to zero. QED.

## 19. Finite termination theorem under strict deterministic margins

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

Under the singleton-data assumptions of Section 18:

### No-hit case

If the exact trajectory satisfies

\[
G(L)\le d-\gamma
\]

for some \(\gamma>0\), then there exists a finite level \(n_*\) for which (15.1) holds.

### Regular-hit case

If the exact first hit \(T\) satisfies:

- \(0<T<L\);
- positive event velocity
  \[
  S(\psi(T^-))\ge\nu_*>0;
  \]
- strict interior first-hit margin, so there are \(a<T<b\) with
  \[
  G(a)<d<G(b)
  \]
  and
  \[
  S(\psi(s))\ge\nu_*/2
  \quad
  \forall s\in[a,b],
  \]

then there exists a finite refinement level for which the algorithm returns `CERTIFIED_REGULAR_HIT`.

### Proof

By Section 18, prefix gain enclosures converge to exact prefix gains, while response enclosures converge uniformly on sufficiently small cells around the regular hit. Strict inequalities therefore survive at finite refinement. QED.

## 20. Interval-family qualification

**Label:** PROPOSITION / QUALIFIED.

For genuinely non-singleton input boxes, interval widths from physical uncertainty need not vanish under time refinement.

The same algorithm remains inclusion-valid.

Finite certification is guaranteed only under a **uniform robust margin** strong enough to separate:

- the interval upper gain from the minimum phase gap in the no-hit case; or
- an interval prefix upper/lower pair plus a uniform positive response lower bound in the hit case.

Failure to certify a wide uncertain family is not evidence that an exact member lacks a regular first hit.

---

# Part VI — I6: rigorous transversality

## 21. Bracket-based transversality certificate

**Label:** THEOREM / PROVED.

Let \(B=[a,b]\) be a certified first-hit bracket.

Compute a rigorous input enclosure

\[
P(B)\supseteq\{\psi(s):s\in B\}
\]

and response enclosure

\[
S(P(B))
=
[\underline\nu_B,\overline\nu_B].
\]

If

\[
\boxed{
\underline\nu_B>0,
}
\tag{21.1}
\]

then the exact event velocity obeys

\[
S(\psi(T^-))\ge\underline\nu_B>0.
\]

Thus (21.1) is a rigorous transversality certificate without knowing \(T\) exactly.

### Threshold-straddling consequence

If \(P(B)\) straddles \(h\), the monotone rigorous response enclosure has lower endpoint zero.

Then the present certificate cannot prove transversality.

Refine the bracket and/or state enclosure.

If the exact event is regular with \(\psi(T)>h\), continuity plus convergent refinement eventually produces a bracket lying strictly above threshold.

If the exact event is tangent/zero-velocity, no positive transversality certificate is expected.

---

# Part VII — I7: event ordering, separation, and boundaries

## 22. Generic interval event ordering

Let

\[
E_a=[\underline t_a,\overline t_a],
\qquad
E_b=[\underline t_b,\overline t_b]
\]

be rigorous enclosures for two labelled event times.

### Ordering lemma

**Label:** LEMMA / PROVED.

If

\[
\overline t_a<\underline t_b,
\]

then

\[
t_a<t_b
\]

for every represented trajectory, with certified separation

\[
\delta_{ab}
\ge
\underline t_b-\overline t_a>0.
\tag{22.1}
\]

If the intervals overlap, no order is certified by interval overlap alone.

Overlap means `UNCERTIFIED_EVENT_ORDER`, not `COLLISION`.

## 23. Spike-before-arrival certificate

Let

\[
T_{\rm spike}
\subseteq
[\underline T,\overline T]
\]

be a certified regular-hit bracket and let a labelled structural arrival satisfy

\[
A_e\in
[\underline A_e,\overline A_e].
\]

If

\[
\overline T<\underline A_e,
\]

then the spike is rigorously before the arrival with separation at least

\[
\underline A_e-\overline T.
\]

This applies unchanged to structural-zero arrivals.

## 24. Arrival-before-spike certificate without exact spike time

Let the pre-arrival alpha/phase flow be hypothetically extended to the latest possible arrival time \(\overline A_e\), without applying the arrival jump.

If the rigorous pre-arrival phase gain satisfies

\[
\overline G_{\rm pre}(\overline A_e)
<
\underline d,
\tag{24.1}
\]

then no spike can occur before the actual arrival \(A_e\).

Define the remaining phase-gap lower bound

\[
\gamma_e
=
\underline d
-
\overline G_{\rm pre}(\overline A_e)
>0.
\tag{24.2}
\]

Since \(0\le\dot\theta<1\), after the arrival the next spike cannot occur less than \(\gamma_e\) time units later.

Therefore the arrival/spike separation is at least

\[
\delta_{e,\rm spike}
\ge
\gamma_e.
\tag{24.3}
\]

### Qualification

Equation (24.3) uses only the global phase-rate upper bound 1.

It remains valid whether the arrival jump is nonzero or the structural-zero identity map.

## 25. Arrival-arrival ordering

**Label:** PROPOSITION / PROVED.

For any two structural arrivals with rigorous time intervals, (22.1) certifies their labelled order and separation.

A zero-weight arrival participates identically.

If exact structural formulas prove equal times, the ordinary sequential chart is collision-invalid even if the state jumps commute.

If intervals merely overlap, the outcome is inconclusive, not a certified collision.

## 26. Horizon boundary

Let the analysis horizon be represented by \(H=[\underline H,\overline H]\), usually a singleton.

### Interior event

If

\[
\overline T<\underline H,
\]

the event is certified inside the horizon with boundary margin at least

\[
\underline H-\overline T.
\]

### Outside event

If a rigorous event lower bound satisfies

\[
\underline T>\overline H,
\]

it is certified after the horizon.

### Boundary uncertainty

If the event enclosure overlaps \(H\), the ordinary finite-horizon classification is `UNCERTIFIED_HORIZON_ORDER` unless exact symbolic structure proves equality.

Exact equality is a boundary case, not a regular interior chart event.

## 27. Initial boundary

The same interval-order logic applies to \(t_0\).

A labelled event is ordinary-interior only when its lower time bound lies strictly after an upper enclosure of the initial time.

---

# Part VIII — I8: local chart-radius lower bounds

## 28. Conditional computable-radius theorem

Let \(\lambda\) lie in a normed parameter space.

Suppose a reference ordinary chart at \(\lambda_0\) has rigorous base lower margins:

- spike transversality:
  \[
  \nu_m(\lambda_0)\ge\underline\nu_m>0;
  \]
- event separation:
  \[
  |T_m(\lambda_0)-T_n(\lambda_0)|
  \ge
  \underline\delta_{mn}>0;
  \]
- boundary distance:
  \[
  b_m(\lambda_0)\ge\underline b_m>0.
  \]

Assume that on a **prevalidated parameter ball**

\[
B_R(\lambda_0)
\]

there are rigorous derivative bounds

\[
\|\nabla_\lambda T_m\|_*
\le
K_{T_m},
\tag{28.1}
\]

\[
\|\nabla_\lambda\nu_m\|_*
\le
K_{\nu_m}.
\tag{28.2}
\]

Here \(\|\cdot\|_*\) is the dual norm.

Define

\[
\rho_{\rm tr}
=
\min_m
\frac{\underline\nu_m}{2K_{\nu_m}},
\tag{28.3}
\]

\[
\rho_{\rm sep}
=
\min_{m<n}
\frac{\underline\delta_{mn}}
{2(K_{T_m}+K_{T_n})},
\tag{28.4}
\]

\[
\rho_{\rm bdry}
=
\min_m
\frac{\underline b_m}{2K_{T_m}},
\tag{28.5}
\]

omitting terms whose denominator is zero.

Then set

\[
\boxed{
\rho_{\rm cert}
=
\min
\left\{
R,\rho_{\rm tr},\rho_{\rm sep},\rho_{\rm bdry}
\right\}.
}
\tag{28.6}
\]

### Theorem

**Label:** THEOREM / PROVED UNDER THE STATED NEIGHBORHOOD-WIDE SENSITIVITY BOUNDS.

Every

\[
\|\lambda-\lambda_0\|
<
\rho_{\rm cert}
\]

retains at least half of every certified transversality, event-separation, and boundary margin.

Therefore the same ordinary labelled event chart is preserved.

### Proof

Mean-value bounds give

\[
|\nu_m(\lambda)-\nu_m(\lambda_0)|
\le
K_{\nu_m}\|\lambda-\lambda_0\|,
\]

and

\[
|T_m(\lambda)-T_m(\lambda_0)|
\le
K_{T_m}\|\lambda-\lambda_0\|.
\]

Substitute (28.6). Separation changes by at most the sum of event-time variations. Boundary distance changes by at most the event-time variation. QED.

## 29. Structural-zero contribution to chart radius

**Label:** PROPOSITION / PROVED.

A labelled structural-zero arrival is included in the event-time list used in (28.4)–(28.5).

Its state jump may be the identity, but its arrival-time sensitivity contributes to event-order and boundary-radius restrictions.

Crossing \(w_e=0\) does not alter topology and therefore does not by itself force chart radius zero.

## 30. No unconditional computable chart-radius result

**Label:** OPEN QUESTION / EXPLICIT NON-RESULT.

Equations (28.3)–(28.6) are useful only if the sensitivity bounds \(K_T,K_\nu\) are themselves rigorously valid throughout a prevalidated ball \(B_R\).

Producing such bounds without circularly assuming the same chart remains valid generally requires a validated variational/implicit continuation argument over the whole ball.

This gate does not construct that full parameter-ball sensitivity engine.

Therefore:

\[
\boxed{
\text{no universal nontrivial numerical chart-radius lower bound is frozen here.}
}
\]

The sharp/global chart-radius problem remains OPEN.

---

# Part IX — I9: structural-zero interval semantics

## 31. Fixed topology under weight intervals

**Label:** THEOREM / PROVED AS SEMANTIC CONSISTENCY.

Let a structural edge weight satisfy

\[
W_e=[\underline w_e,\overline w_e]
\]

with possibly

\[
0\in W_e.
\]

Then:

1. the edge remains in the fixed structural graph for the entire interval;
2. every source spike retains its labelled delayed arrival;
3. the jump enclosure is
   \[
   Q_i^+
   =
   Q_i^-+W_e A^2;
   \]
4. if \(0\in W_e\), the jump enclosure includes the identity state;
5. no parameter subcase removes the arrival from event-order or boundary certification.

An interval crossing zero is therefore an ordinary parameter interval, not a topology branch.

## 32. Structural-zero event-time certification

**Label:** PROPOSITION / PROVED.

Arrival-time enclosure is determined by

\[
A_e=T_{\rm launch}+\Tau_e
\]

independently of whether \(W_e\) contains zero.

The arrival interval participates in Sections 22–27.

A zero jump does not justify ignoring an overlap with another event-time interval.

---

# Part X — I10: fail-closed certification taxonomy

## 33. Positive certificate labels

### CERTIFIED_NO_HIT

All proof obligations of Section 15 hold.

### CERTIFIED_REGULAR_HIT

All proof obligations of Section 16 and Section 21 hold.

### CERTIFIED_EVENT_ORDER

Relevant time intervals are strictly separated by Section 22, or an arrival-before-spike phase-margin proof from Section 24 is available.

### CERTIFIED_ORDINARY_CHART

Every event on the finite tape has:

- a positive first-hit/transversality certificate where applicable;
- strict labelled-event ordering/separation;
- strict initial/horizon boundary separation;
- fixed topology including structural-zero arrivals.

## 34. Fail-closed nonpositive outcomes

### ASSUMPTION_VIOLATED

Use when a theorem precondition is actually false or not supplied, for example:

- \(\underline\alpha\le0\);
- response family differs from the frozen one without a new proof;
- infinite-history tail assumption required by a requested tail certificate is absent;
- parameter-dependent topology changes are requested.

This is not a statement that the physical trajectory itself is invalid.

### STRICT_MARGIN_ABSENT

Use when exact/symbolic information proves a zero margin:

- exact tangency/nontransverse event;
- exact simultaneous labelled events;
- exact horizon/initial-boundary event.

For an ordinary chart, such a case may additionally be `ORDINARY_CHART_INVALID`.

### ENCLOSURE_INCONCLUSIVE

Use when current outward intervals overlap a decision boundary but no exact zero margin is proved.

Examples:

- \(\overline G_m\ge\underline d\) and no hit bracket is certified;
- event-time intervals overlap;
- transversality lower bound is zero because the input enclosure straddles \(h\).

Interval overlap alone never proves collision.

### RESOURCE_EXHAUSTED

Use when a finite requested refinement limit \(N_{\max}\), memory budget, or allowed precision budget is reached before a positive or exact-negative classification.

### UNCERTIFIED_ARITHMETIC

Use when interval primitives lose their proof obligation, overflow without rigorous enclosure semantics, or a transcendental inclusion guarantee is unavailable.

### ORDINARY_CHART_INVALID

Use only when ordinary-chart invalidity is itself certified, for example:

- exact simultaneous labelled events;
- a certified event with zero transversality under the ordinary simple-root requirement;
- exact initial/horizon boundary event.

A physically meaningful grouped event may still exist.

### UNSUPPORTED_CASE

Use for cases outside Version 0.1, such as:

- interval uncertainty in response parameters \(r,h\);
- parameter-dependent graph topology;
- grouped-collision chart certification;
- nonsmooth response variants.

### MATHEMATICAL_CONTRADICTION

Use if two valid outward certificates imply logically incompatible exact statements or a deterministic theorem identity is rigorously violated under all stated assumptions.

This is a scientific/theory blocker and must return to MASTER.

---

# Part XI — one constructive finite certification algorithm

## 35. Algorithm RIFC-0.1

Name:

\[
\boxed{
\text{RIFC-0.1 — Rigorous Interval First-Hit Certifier}
}
\]

This is the single constructive algorithm specified by this gate.

It is not executed here.

## 36. Inputs

Required inputs:

1. fixed structural graph \(E\);
2. one certified current ordinary-chart origin time \(t_0\);
3. phase-gap intervals \(D_i\) for candidate neurons;
4. alpha-state intervals \(P_{0,i},Q_{0,i}\);
5. \(A=[\underline\alpha,\overline\alpha]\subset(0,\infty)\);
6. fixed exact frozen response parameters \(r,h\);
7. weight intervals \(W_e\), including intervals crossing zero;
8. delay/arrival-time intervals for all labelled structural arrivals;
9. finite horizon interval \(H\);
10. rigorous interval backend satisfying IR-A1–IR-A5;
11. finite maximum dyadic level \(N_{\max}\).

Unsupported inputs are rejected before certification.

## 37. Deterministic refinement order

For

\[
n=0,1,\ldots,N_{\max},
\]

set

\[
p_n=128+8n.
\]

For each neuron, evaluate the hypothetical no-arrival flow on the relevant candidate interval using exactly \(2^n\) equal dyadic cells.

At each level:

1. process neurons in increasing structural index;
2. process time cells left-to-right;
3. use monotonicity sharpening only when Section 7's sign condition is certified;
4. form response intervals by Section 10;
5. form prefix phase-gain intervals by Sections 12–13;
6. test no-hit condition (15.1);
7. if not no-hit, search for a regular-hit bracket.

### Deterministic bracket search

For each neuron:

1. find the smallest prefix index \(k\) satisfying
   \[
   \underline G_k>\overline d;
   \]
2. among \(j=k-1,k-2,\ldots,0\), choose the largest \(j\) for which
   \[
   \overline G_j<\underline d
   \]
   and every cell from \(j\) through \(k-1\) has strictly positive response lower bound;
3. if such \(j\) exists, output that neuron's candidate regular-hit interval.

This rule is deterministic.

## 38. Event-order module

At each level, combine:

- certified spike brackets;
- certified spike lower bounds from phase-rate \(\le1\);
- all labelled structural arrival intervals;
- horizon interval.

Attempt certificates in this order:

1. a spike bracket whose upper endpoint lies below every competing event lower endpoint;
2. a structural arrival certified before every competing labelled arrival and for which every candidate neuron satisfies the pre-arrival no-hit proof (24.1);
3. horizon/no-event classification if all spikes are no-hit through the horizon and all labelled arrivals are after the horizon;
4. otherwise refine.

Structural-zero arrivals are never removed.

## 39. Stopping rules

### Positive stop A — CERTIFIED NO-HIT on a requested segment

Stop when Section 15 holds.

### Positive stop B — CERTIFIED REGULAR HIT

Stop when Section 16 plus Section 21 hold and event ordering against arrivals/horizon is certified.

Return:

- neuron/event label;
- rigorous time bracket;
- phase prefix enclosures at bracket endpoints;
- transversality lower bound;
- separation lower bounds to all certified competitors;
- boundary lower bound;
- working precision/refinement level;
- exact structural topology signature.

### Positive stop C — CERTIFIED STRUCTURAL ARRIVAL

Stop when a labelled arrival is rigorously the next event under Section 38.

Return:

- edge/event label;
- arrival-time interval;
- weight interval;
- jump interval \(W_eA^2\);
- separation/boundary margins;
- whether \(0\in W_e\).

### Negative/uncertified stop

If \(n=N_{\max}\) and no positive/exact-invalid classification exists, return

`RESOURCE_EXHAUSTED / UNCERTIFIED`.

Exact theorem-assumption or chart-boundary failures use Section 34 labels immediately.

## 40. Proof obligations for every positive certificate

A later implementation may emit a positive certificate only if it can retain/reconstruct:

1. exact input interval endpoints and topology signature;
2. arithmetic precision and directed-rounding backend identity;
3. rigorous exponential primitive identity/proof contract;
4. every cell input interval \(P_k\);
5. every response interval \(R_k\);
6. outward prefix gain intervals;
7. phase-gap interval;
8. first-hit bracket inequalities;
9. transversality lower enclosure;
10. competing event-time intervals;
11. event-separation and boundary inequalities;
12. structural-zero arrivals and jump enclosures;
13. no occurrence of an arithmetic proof failure.

A scalar root estimate alone is not a certificate.

## 41. Unsupported cases

RIFC-0.1 does not certify:

- simultaneous/grouped ordinary events;
- parameter-dependent topology;
- response-parameter uncertainty in \(r,h\);
- nonsmooth response variants;
- adaptive/state-dependent propagation delays;
- infinite-history tails without the required summability/density assumptions;
- global parameter-box chart radii without independent neighborhood-wide sensitivity bounds.

These return `UNSUPPORTED_CASE` or a more specific fail-closed label.

---

# Part XII — correctness and termination of RIFC-0.1

## 42. Soundness theorem

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

Assume IR-A1–IR-A5 and all model preconditions of RIFC-0.1.

Then every emitted:

- `CERTIFIED_NO_HIT`,
- `CERTIFIED_REGULAR_HIT`,
- `CERTIFIED_EVENT_ORDER`,
- `CERTIFIED_STRUCTURAL_ARRIVAL`

statement is true for every exact trajectory represented by the input intervals.

### Proof

Alpha-state inclusion follows from Section 5.

Response inclusion follows from Section 10.

Phase-gain inclusion follows from Section 13.

No-hit and hit statements follow from Sections 15–16.

Transversality follows from Section 21.

Event-order statements follow from Sections 22–27.

Structural-zero semantics follow from Sections 31–32.

All positive decisions use strict inequalities on outward enclosures. QED.

## 43. Eventual-certification theorem for regular deterministic cases

**Label:** THEOREM / PROVED.

For singleton deterministic model/state inputs satisfying the strict-margin regularity assumptions of Section 19 and strict labelled-event/horizon separation, the unbounded refinement sequence

\[
N_{\max}\to\infty
\]

eventually emits the correct positive certificate.

For any finite \(N_{\max}\), failure to reach that level returns `RESOURCE_EXHAUSTED / UNCERTIFIED` without changing the mathematical classification.

### Qualification

This theorem is an eventual-termination theorem for strict regular cases.

It is not a guarantee that a particular fixed resource budget will suffice.

It gives no positive termination guarantee for zero-margin cases.

---

# Part XIII — relation to RB-019 / RB-021 / RB-023

## 44. What is mathematically promoted

**Label:** INTERPRETATION.

The following concepts now have explicit rigorous mathematical support:

- outward interval state propagation;
- threshold-safe response range enclosure;
- rigorous interval Darboux phase accumulation;
- strict no-hit and regular-hit certificate logic;
- transversality lower certificates;
- interval event-order and horizon certificates;
- topology-fixed structural-zero interval semantics;
- fail-closed distinction between overlap/inconclusive and actual collision.

## 45. What remains engineering evidence

**Label:** INTERPRETATION.

RB-019/RB-021/RB-023 finite tolerances, test counts, float64 residuals, timings and particular implementation details remain engineering evidence.

RB-023's finite gain enclosures are not retroactively reclassified as outward-rounded interval proofs.

A later NUM-ENG gate must implement RIFC-0.1 with a backend satisfying IR-A1–IR-A5 and validate that the implementation actually preserves these proof obligations.

## 46. No library endorsement

**Label:** NON-RESULT.

This theory does not endorse MPFR, IEEE binary64, a particular interval package, or any particular exponential implementation.

Any backend is admissible only if its directed arithmetic and transcendental inclusion contract is independently established.

---

# Part XIV — explicit open problems

## 47. Sharp computable chart radius

**Label:** OPEN QUESTION.

A nontrivial chart-radius lower bound is conditionally available through Section 28.

A general automatic neighborhood-wide sensitivity certifier sufficient to make that bound unconditional is not developed here.

## 48. Grouped simultaneous-event charts

**Label:** OPEN QUESTION.

Commuting simultaneous arrivals can be physically well-defined while violating the ordinary labelled total-order chart.

Validated grouped-event charts remain open.

## 49. Higher-efficiency rigorous integration

**Label:** OPEN QUESTION.

Taylor models, interval Gauss-Kronrod, validated ODE solvers, or interval Newton methods may be much more efficient than dyadic Darboux refinement.

They are not frozen because the present gate intentionally selects one proof-simple primary route.

## 50. Interval uncertainty in response parameters

**Label:** OPEN QUESTION / DEFERRED.

The present algorithm fixes \(r,h\).

Extending the sharp monotone response enclosure to interval \(r,h\), especially with threshold uncertainty, is deferred.

## 51. Infinite-history global certification

**Label:** OPEN QUESTION.

RB-022 alpha-tail bounds remain available under explicit summability/density hypotheses.

A universal certificate from local finiteness alone does not exist in this theory.

## 52. Formal machine verification

**Label:** OPEN QUESTION.

The mathematical algorithm is specified at proof level, but no proof assistant or formally verified interval implementation is produced here.

---

# Part XV — gate decision

## 53. Decision

# PASS — CONSTRUCTIVE OUTWARD-VALID INTERVAL CERTIFICATION THEORY ESTABLISHED

The main RB-023 rigor gap is closed at the mathematical specification level.

This gate establishes:

1. explicit finite interval semantics;
2. directed-rounding and certified-transcendental obligations;
3. rigorous interval alpha propagation with interval initial data and interval \(\alpha\);
4. threshold-safe rigorous response enclosures;
5. one primary interval Darboux phase-gain method;
6. sound no-hit and regular-hit certificates;
7. finite eventual certification under strict deterministic margins;
8. rigorous bracket-based transversality;
9. interval event-order, arrival/spike and horizon-boundary logic;
10. topology-fixed structural-zero interval semantics;
11. a conditional chart-radius lower-bound theorem and explicit unconditional non-result;
12. a fail-closed certification taxonomy;
13. one deterministic implementable algorithm, RIFC-0.1.

No numerical execution occurred.

## 54. Proposed theory freeze

If MASTER accepts this gate, establish:

`CORE Rigorous Enclosure & Interval First-Hit Certification Theory Freeze 0.1`

freezing:

- IR-A1–IR-A5;
- Sections 4–32 mathematical inclusion/certification results;
- the fail-closed taxonomy;
- RIFC-0.1 and its proof obligations;
- the conditional chart-radius theorem and the explicit non-result;
- the unsupported/open-problem boundaries.

The freeze must not:

- promote RB-023 float64 tests into formal certification;
- authorize a specific interval library without a later implementation gate;
- authorize TR-27C, `2711xxx`, APP-3, or v0.28 effect-bearing work.

## STOP

STOP — RETURN TO MASTER
