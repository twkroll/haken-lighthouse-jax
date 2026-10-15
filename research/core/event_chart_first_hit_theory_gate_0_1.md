# CORE Event-Chart Regularity & Certified First-Hit Theory Gate 0.1

Date: 2026-10-15
Status: PASS — FIRST-HIT / EVENT-CHART THEORY ESTABLISHED WITH EXPLICIT MARGINS AND CERTIFICATION LIMITS

## 1. Authority, identity, and scope

This gate executes the MASTER-authorized prompt

\`research/master/prompts/core_event_chart_first_hit_theory_gate_0_1.md\`.

Canonical identity at gate start:

- repository: \`twkroll/haken-lighthouse-jax\`
- canonical branch: \`main\`
- \`main\` HEAD at gate start: \`d0c65c2d7347e43396067654a369a1c5bef0ba8f\`
- CORE STATUS blob: \`21c7e238afd02426453fbd6ebda75953d4434c74\`
- MASTER prompt blob: \`efa6cb96baab90bcd2ebdb18ddc2df57c78c64c8\`
- MASTER STATUS blob: \`fbdf9afa2889cd3ce9427f039e451b32a20982f5\`
- MASTER project-status blob: \`5eb16673efa89a3a2e7b3bff39f8955351ba1508\`
- MASTER decision-log blob: \`9947d10e4a1fd8158bc75abbcf668410c9bb7d45\`
- RB-004 Mathematical Freeze blob: \`d84a2f8c23b0bb0d6be4867a42a6fea235232f20\`
- RB-007 Continuation Theory Freeze blob: \`9ba55b855b3257d11e9fc741ea19a0e2deacc329\`
- RB-010 Floquet Theory Freeze blob: \`21c2d9a77ff1d2f17fe6068b43b2d004538cf257\`
- RB-012 Consolidated C1 Theory Freeze blob: \`e371e0cc8b645eb23cbb683d2ed8997ccb9dc62f\`
- RB-019 Numerical Engineering Freeze blob: \`68c674e50772620960b5e52092b9f6cd606d8f42\`
- RB-020 v0.27c Execution Contract Freeze blob: \`b2015acc18da13755f078187895f274418751460\`

RB-015 remains immutable \`SCIENTIFIC FAIL\`.

This is a THEORY gate. No TR-27C check, \`2711xxx\` RNG object, v0.27c confirmatory execution, APP-3 training, scaling benchmark, effect-bearing v0.28 experiment, novelty positioning, or manuscript claim is produced here.

### Claim/provenance convention

Every substantive new statement below is labelled with both:

- epistemic label: THEOREM / PROVED, PROPOSITION, LEMMA, ASSUMPTION, INTERPRETATION, OPEN QUESTION;
- provenance: DERIVATION HERE, FROZEN PREMISE, or ENGINEERING INTERPRETATION.

---

## 2. Frozen baseline used here

### F1 — baseline response

**Label:** FROZEN PREMISE.

\[
S_{r,h}(x)=
\begin{cases}
0,&x\le h,\\
\exp[-r/(x-h)^2],&x>h,
\end{cases}
\qquad r>0.
\]

The lifted phase satisfies

\[
\dot\theta_i=S_{r,h}(\psi_i).
\]

Hence \(0\le S<1\).

### F2 — normalized alpha kernel

**Label:** FROZEN PREMISE.

\[
\eta_\alpha(t)=\alpha^2 t e^{-\alpha t}H(t),
\qquad \alpha>0.
\]

On a target-local arrival-free segment of duration \(s\), the delayed alpha convolution has the exact aggregated state representation

\[
q(s)=e^{-\alpha s}q_0,
\qquad
\psi(s)=e^{-\alpha s}(\psi_0+s q_0).
\tag{2.1}
\]

At an arrival on edge \(j\to i\),

\[
q_i^+=q_i^-+w_{ij}\alpha^2,
\qquad
\psi_i^+=\psi_i^-.
\tag{2.2}
\]

This is the delayed target-local form of the RB-004 alpha convolution and is the mathematical object underlying the RB-019 pulse-aware segmentation.

### F3 — first hitting

**Label:** FROZEN PREMISE.

A spike is the first hitting of the next lifted section. For the current target phase \(\Theta_i^{\rm sec}\),

\[
T_i=\inf\{t>t_0:\theta_i(t)=\Theta_i^{\rm sec}\}.
\]

Regular-event theory uses

\[
\nu_i=S(\psi_i(T_i^-))>0.
\]

Simultaneous-event collisions are outside the ordinary regular event chart.

---

# Part I — T1: first-hit existence and mathematical completeness

## 3. One arrival-free segment

Fix one neuron and an interval

\[
I=[t_0,t_0+L],\qquad L>0,
\]

containing no interior arrival and no already accepted firing event.

Let

\[
d=\Theta^{\rm sec}-\theta(t_0)>0
\]

be the remaining phase gap, and define, in local time \(s=t-t_0\),

\[
\psi(s)=e^{-\alpha s}(\psi_0+s q_0),
\tag{3.1}
\]

\[
G(s)=\int_0^s S(\psi(u))\,du.
\tag{3.2}
\]

Because \(S\ge0\), \(G\) is continuous and nondecreasing. Because \(S<1\), it is 1-Lipschitz.

## 4. First-hit classification theorem

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

For the exact \(G\) of (3.2):

1. If
   \[
   G(L)<d,
   \]
   then no spike threshold is hit on \((t_0,t_0+L]\).

2. If
   \[
   G(L)>d,
   \]
   then a first hit exists at
   \[
   s_*=\inf\{s\in(0,L):G(s)=d\}.
   \]

3. If there are \(0\le a<b\le L\) and \(\nu_*>0\) such that
   \[
   G(a)<d<G(b)
   \tag{4.1}
   \]
   and
   \[
   S(\psi(s))\ge\nu_*
   \quad\forall s\in[a,b],
   \tag{4.2}
   \]
   then there is exactly one threshold root in \((a,b)\), it is the first root after \(a\), and it is transversal.

4. If \(G(L)=d\), then the next section is reached at or before the right endpoint. This is an endpoint/boundary case, not a regular strict-interior certificate.

### Proof

Continuity gives the intermediate-value statement. Nonnegativity of \(S\) gives monotonicity of \(G\). Under (4.2),

\[
G(b)-G(a)
=\int_a^bS(\psi(s))ds
\ge\nu_*(b-a)>0,
\]

and \(G\) is strictly increasing on the bracket, so the root there is unique. Its event velocity is \(S(\psi(s_*))\ge\nu_*>0\). QED.

### Qualification

A first hit can still exist with zero derivative, for example at the edge of a phase plateau. Such a hit is not covered by the regular simple-root theorem and is not certified as a differentiable event.

## 5. Exact alpha-state extrema and cheap phase-gain bounds

**Label:** LEMMA / PROVED.  
**Provenance:** DERIVATION HERE.

For (3.1),

\[
\psi'(s)=e^{-\alpha s}\left(q_0-\alpha\psi_0-\alpha s q_0\right).
\]

Hence \(\psi\) has at most one interior stationary point. If \(q_0\ne0\),

\[
s_c=\frac{q_0-\alpha\psi_0}{\alpha q_0}.
\tag{5.1}
\]

Therefore the exact extrema of \(\psi\) on \([a,b]\) occur in the finite candidate set

\[
\{a,b\}\cup
\{s_c:\ a<s_c<b\}.
\tag{5.2}
\]

Because \(S\) is nondecreasing,

\[
(b-a)S(\psi_{\min})
\le
\int_a^b S(\psi(s))ds
\le
(b-a)S(\psi_{\max}).
\tag{5.3}
\]

Consequently, for any partition
\(0=s_0<\cdots<s_m=L\),

\[
G(L)
\le
\sum_{k=0}^{m-1}\Delta s_k
S(\psi_{\max,k}),
\tag{5.4}
\]

\[
G(L)
\ge
\sum_{k=0}^{m-1}\Delta s_k
S(\psi_{\min,k}).
\tag{5.5}
\]

### Corollary — sufficient no-hit certificate

**Label:** PROPOSITION / PROVED.  
**Provenance:** DERIVATION HERE.

If the right-hand side of (5.4) is strictly smaller than \(d\), there is no hit on the segment.

The very crude special case

\[
L\,S(\max_{[0,L]}\psi)<d
\tag{5.6}
\]

already suffices.

Since \(S<1\), \(L<d\) is an even cruder universal no-hit condition.

### Corollary — sufficient hit certificate

**Label:** PROPOSITION / PROVED.  
**Provenance:** DERIVATION HERE.

If the lower sum (5.5) exceeds \(d\), a hit occurs before the segment endpoint. A regular unique bracket follows once two partition nodes enclose the phase gap and a positive response lower bound holds between them.

## 6. Finite numerical certification under strict margins

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

Suppose a numerical method produces outward-valid enclosures

\[
G(s_k)\in[\underline G_k,\overline G_k]
\]

and a lower response enclosure on each cell.

Then:

- **certified absence** holds if
  \[
  \overline G_m<d;
  \tag{6.1}
  \]

- **certified regular first-hit bracket** \((s_a,s_b)\) holds if
  \[
  \overline G_a<d<\underline G_b
  \tag{6.2}
  \]
  and the certified cellwise response lower bound on \([s_a,s_b]\) is \(>0\).

If the true problem has a strict no-hit margin, or a strict bracket plus transversality margin, and the enclosure widths converge to zero under refinement, then finite refinement eventually certifies the correct case.

### Limitation

**Label:** OPEN QUESTION / NON-RESULT.  
**Provenance:** DERIVATION HERE.

No finite-certification theorem is claimed for zero-margin cases:

- \(G(L)=d\);
- tangential hit with \(S(\psi(s_*))=0\);
- exact event collision;
- exact horizon/initial-boundary event;
- an enclosure algorithm whose error bounds do not converge rigorously.

Mathematical truth and finite numerical certifiability are distinct.

---

# Part II — T2: response, alpha-state, and tail bounds

## 7. Global smoothness and derivative bounds of the frozen response

Let \(y=x-h\).

### 7.1 Smoothness

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

The zero extension of

\[
e^{-r/y^2},\qquad y>0,
\]

is \(C^\infty\) at \(y=0\). Hence the frozen \(S_{r,h}\) is globally \(C^\infty(\mathbb R)\).

Every derivative at \(x=h\) equals zero.

### Proof sketch

Every right derivative is a finite sum of terms

\[
P(1/y)e^{-r/y^2},
\]

where \(P\) is a polynomial. Exponential decay in \(1/y^2\) dominates every power as \(y\downarrow0\), so all right derivatives tend to zero and match the zero left derivatives.

### 7.2 First derivative

For \(x>h\),

\[
S'(x)
=
\frac{2r}{(x-h)^3}
e^{-r/(x-h)^2}.
\tag{7.1}
\]

Set

\[
t=\frac{r}{(x-h)^2}.
\]

Then

\[
S'(x)=
\frac{2}{\sqrt r}t^{3/2}e^{-t}.
\]

The maximum occurs at \(t=3/2\), so

\[
\boxed{
\|S'\|_\infty
=
\frac{2}{\sqrt r}
\left(\frac32\right)^{3/2}e^{-3/2}
=
\frac{3}{\sqrt r}\sqrt{\frac32}\,e^{-3/2}.
}
\tag{7.2}
\]

Numerically,

\[
\|S'\|_\infty
\approx
\frac{0.8198325578837201}{\sqrt r}.
\]

Thus \(S\) is globally Lipschitz.

### 7.3 Second derivative

For \(x>h\),

\[
S''(x)
=
e^{-r/(x-h)^2}
\left[
\frac{4r^2}{(x-h)^6}
-
\frac{6r}{(x-h)^4}
\right].
\tag{7.3}
\]

Equivalently,

\[
S''(x)
=
\frac1r(4t^3-6t^2)e^{-t}.
\]

A global bound is

\[
\boxed{
\|S''\|_\infty
=
\frac{c_2}{r},
\qquad
c_2\approx2.9785942853413405.
}
\tag{7.4}
\]

The dominating stationary point is

\[
t_+=\frac{9+\sqrt{33}}4.
\]

### 7.4 Higher derivatives

**Label:** PROPOSITION / PROVED.  
**Provenance:** DERIVATION HERE.

For every integer \(k\ge0\), there is a finite universal constant \(c_k\) such that

\[
\boxed{
\|S^{(k)}\|_\infty
\le
c_k r^{-k/2}.
}
\tag{7.5}
\]

This follows by the rescaling

\[
u=\frac{x-h}{\sqrt r},
\qquad
S=e^{-1/u^2}
\]

on \(u>0\), with zero extension at \(u\le0\).

No loss of differentiability occurs merely because \(\psi=h\) in the frozen smooth-response model. This preserves the RB-007 repair.

## 8. Alpha-state decay

**Label:** LEMMA / PROVED.  
**Provenance:** DERIVATION HERE.

On an arrival-free interval,

\[
|q(s)|\le e^{-\alpha s}|q_0|,
\tag{8.1}
\]

\[
|\psi(s)|
\le
e^{-\alpha s}
\left(|\psi_0|+s|q_0|\right).
\tag{8.2}
\]

The kernel itself satisfies

\[
0\le\eta_\alpha(t)\le\frac{\alpha}{e},
\tag{8.3}
\]

with its maximum at \(t=1/\alpha\).

Its exact remaining mass after age \(A\ge0\) is

\[
\boxed{
M_\eta(A)
=
\int_A^\infty\eta_\alpha(t)\,dt
=
e^{-\alpha A}(1+\alpha A).
}
\tag{8.4}
\]

Also,

\[
|\eta_\alpha'(t)|\le\alpha^2
\qquad(t>0).
\tag{8.5}
\]

## 9. Weighted omitted-history tail bound

Let \(\mathcal O_i\) be any set of omitted historical edge pulses contributing to target \(i\). Let pulse \(e\) have absolute coupling magnitude \(c_e\) and age \(a_e\ge0\) at the segment start.

Assume

\[
\sum_{e\in\mathcal O_i}
c_e M_\eta(a_e)<\infty.
\tag{9.1}
\]

### 9.1 Input-tail bound

**Label:** PROPOSITION / PROVED.  
**Provenance:** DERIVATION HERE.

For \(s\ge0\),

\[
|\delta\psi_i(s)|
\le
\sum_{e\in\mathcal O_i}
c_e\,
\alpha^2(a_e+s)e^{-\alpha(a_e+s)}.
\tag{9.2}
\]

Moreover, over a finite interval \([0,L]\),

\[
\int_0^L|\delta\psi_i(s)|\,ds
\le
\sum_e c_e
\left[
M_\eta(a_e)-M_\eta(a_e+L)
\right].
\tag{9.3}
\]

Hence

\[
\int_0^L|\delta\psi_i(s)|ds
\le
\sum_e c_eM_\eta(a_e).
\tag{9.4}
\]

### 9.2 Phase-tail error

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

Using the global Lipschitz constant \(L_S=\|S'\|_\infty\),

\[
\boxed{
\left|
\int_0^L
S(\psi_i(s))\,ds
-
\int_0^L
S(\psi_i(s)-\delta\psi_i(s))\,ds
\right|
\le
L_S
\sum_e c_e
\left[M_\eta(a_e)-M_\eta(a_e+L)\right].
}
\tag{9.5}
\]

The infinite-horizon upper bound is

\[
\le
L_S\sum_e c_eM_\eta(a_e).
\tag{9.6}
\]

This gives a mathematically valid route from an absolute alpha-tail mass bound to a phase-accumulation error bound.

### 9.3 Minimum-interspike corollary

**Label:** PROPOSITION / PROVED.  
**Provenance:** DERIVATION HERE.

Suppose, on one source edge of absolute weight \(c\), omitted spike ages satisfy

\[
a_n\ge A+n\delta,
\qquad n=0,1,\ldots,
\]

for \(\delta>0\), and choose \(A\ge1/\alpha\). Set

\[
\rho=e^{-\alpha\delta}.
\]

Then the omitted pointwise alpha tail is bounded by

\[
c\alpha^2e^{-\alpha A}
\left[
\frac{A}{1-\rho}
+
\frac{\delta\rho}{(1-\rho)^2}
\right],
\tag{9.7}
\]

and the total future omitted mass is bounded by

\[
c e^{-\alpha A}
\left[
\frac{1+\alpha A}{1-\rho}
+
\frac{\alpha\delta\rho}{(1-\rho)^2}
\right].
\tag{9.8}
\]

Summing these bounds over incoming edges gives a finite network tail certificate.

### Qualification

RB-004 assumes locally finite prehistory. Local finiteness alone does not imply the infinite-past summability condition (9.1). A tail theorem for an infinite historical spike train therefore needs an additional absolute-tail or firing-density/minimum-separation assumption.

---

# Part III — T3: event-chart regularity

## 10. Ordinary event-chart assumptions

Let \(\lambda\in\mathbb R^d\) collect any admissible local parameters.

For a finite horizon \([0,T_H]\), consider a reference trajectory with a finite ordered event sequence

\[
E_1,\ldots,E_M.
\]

The following are sufficient assumptions for an ordinary sequential chart.

### EC-A1 — smooth segment dynamics

**Label:** ASSUMPTION.

Between events, the state flow depends \(C^k\)-smoothly on state, time and \(\lambda\), for some \(k\ge1\).

The frozen alpha flow plus smooth response satisfies this wherever parameter maps are \(C^k\).

### EC-A2 — spike transversality margin

**Label:** ASSUMPTION.

Every reference spike satisfies

\[
\nu_m
=
S(\psi_{i_m}(T_m^-))
\ge\nu_*>0.
\tag{10.1}
\]

### EC-A3 — event-separation margin

**Label:** ASSUMPTION.

At each reference event, the winning candidate event time differs from every competing spike/arrival candidate by at least

\[
\delta_{\rm sep}>0.
\tag{10.2}
\]

### EC-A4 — arrival regularity

**Label:** ASSUMPTION.

Every active delayed arrival has a well-defined launch event and a \(C^k\) delay map. For fixed physical delay,

\[
A_e=T_{\rm launch}+\tau_e.
\tag{10.3}
\]

Structural zero-weight edges are not treated as physical input events in the ordinary chart.

### EC-A5 — boundary margin

**Label:** ASSUMPTION.

No chart event occurs at the initial time or final horizon, and all accepted events have distance at least

\[
\delta_{\rm bdry}>0
\]

from those boundaries.

### EC-A6 — finite event list

**Label:** ASSUMPTION / FROZEN-COMPATIBLE.

The reference trajectory contains finitely many events on the finite horizon.

For the baseline spikes, \(S<1\) already supplies a same-neuron minimum \(2\pi\) phase-accumulation time. With finite graph, locally finite history and fixed finite-delay fan-out, finite-horizon spike Zeno accumulation is excluded in the baseline setting.

## 11. Event-chart regularity theorem

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

Under EC-A1 through EC-A6, there exists an open parameter neighborhood \(U\) of the reference \(\lambda_0\) such that:

1. the same finite event types occur in the same ordinary order;
2. all reference spike events remain transversal;
3. all spike and scheduled-arrival times are \(C^k\) functions of \(\lambda\) on \(U\);
4. the event-indexed pre/post-event state is \(C^k\) in \(\lambda\);
5. the complete fixed event tape is a valid local chart on \(U\).

### Proof

Proceed by induction over events.

For the first spike candidate, define the event function

\[
g(t,\lambda)
=
\theta_i(t,\lambda)-\Theta_i^{\rm sec}.
\]

At the reference root,

\[
\partial_tg
=
S(\psi_i)
\ge\nu_*>0.
\]

The implicit-function theorem gives a unique local \(C^k\) spike-time map.

A scheduled arrival time is the smooth composition

\[
T_{\rm launch}(\lambda)+\tau_e(\lambda).
\]

The positive event-separation margin and continuity preserve the winner and ordering on a sufficiently small neighborhood.

The flow to the event and the reset/arrival map are \(C^k\), so the post-event state is \(C^k\). Repeat finitely many times. Boundary margins preserve the finite horizon membership. QED.

## 12. Necessary versus sufficient conditions

### 12.1 Transversality

**Label:** INTERPRETATION.

\(\nu>0\) is sufficient for the standard simple-root differentiability theorem.

It is not logically necessary for event existence, continuity, or differentiability in every specially structured degenerate example. But when \(\nu=0\), the standard implicit-function argument fails and derivative blow-up/nonexistence can occur. Therefore a nontransverse event is correctly excluded from the ordinary certified chart.

### 12.2 Event separation

**Label:** INTERPRETATION.

Strict positive pairwise separation is sufficient for an ordinary total-order event tape.

It is not necessary for every possible generalized hybrid representation. Simultaneous commuting arrivals could be represented as a grouped event. Such grouped-event theory is not frozen here.

Exact spike/arrival or spike/spike collisions are not ordinary regular-chart points.

### 12.3 Arrival separation

**Label:** INTERPRETATION.

Positive separation of active arrival times is sufficient for sequential pulse-aware segmentation.

Two simultaneous jumps to distinct commuting state components may be mathematically well-defined, but their representation as two sequential labelled events is not unique. The current theory therefore treats them as a chart boundary unless a later grouped-event gate is authorized.

### 12.4 Boundary events

**Label:** INTERPRETATION.

A positive initial/horizon margin is sufficient for a fixed finite chart. An event exactly at the analysis horizon can be handled by another convention, but not by claiming that the present open chart extends through the boundary.

---

# Part IV — T4: local differentiability and chart radius

## 13. Spike-time derivative

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE + RB-004 D18.

Let a regular spike be given by

\[
g(T(\lambda),\lambda)
=
\theta_i(T(\lambda),\lambda)-\Theta_i^{\rm sec}
=0
\]

with

\[
\nu_i=\partial_tg=S(\psi_i(T^-))>0.
\]

Then

\[
\boxed{
D_\lambda T
=
-\frac{D_\lambda\theta_i(T,\lambda)|_{t\ {\rm fixed}}}
{S(\psi_i(T^-))}.
}
\tag{13.1}
\]

The numerator contains every upstream initial-state, weight, delay and prior-event-time dependence propagated through the fixed chart.

## 14. Arrival-time derivative

**Label:** LEMMA / PROVED.  
**Provenance:** DERIVATION HERE.

For an arrival generated by a source spike \(T_j^m(\lambda)\),

\[
A_{ij}^m(\lambda)
=
T_j^m(\lambda)+\tau_{ij}(\lambda).
\]

Therefore

\[
\boxed{
D_\lambda A_{ij}^m
=
D_\lambda T_j^m
+
D_\lambda\tau_{ij}.
}
\tag{14.1}
\]

For the delay coordinate itself, the direct contribution is \(+1\), in addition to any network feedback through the source spike time.

## 15. Fixed-segment state sensitivities

**Label:** LEMMA / PROVED.  
**Provenance:** DERIVATION HERE.

For fixed \(\alpha\) on an arrival-free segment,

\[
D_\lambda q(s)
=
e^{-\alpha s}D_\lambda q_0,
\tag{15.1}
\]

\[
D_\lambda\psi(s)
=
e^{-\alpha s}
\left(
D_\lambda\psi_0+sD_\lambda q_0
\right),
\tag{15.2}
\]

and

\[
D_\lambda\theta(s)
=
D_\lambda\theta_0
+
\int_0^s
S'(\psi(u))
D_\lambda\psi(u)\,du.
\tag{15.3}
\]

At an arrival \(j\to i\),

\[
q_i^+=q_i^-+w_{ij}\alpha^2.
\]

Hence, in event-indexed coordinates,

\[
D_\lambda q_i^+
=
D_\lambda q_i^-
+
\alpha^2D_\lambda w_{ij}
\tag{15.4}
\]

for fixed \(\alpha\), together with the ordinary chain-rule dependence through the moving arrival time.

If \(\alpha\), response parameters, or other smooth scalar model quantities are themselves varied, the same theorem applies after their explicit derivatives are included, provided they remain inside their admissible open domain, e.g. \(\alpha>0\), \(r>0\).

## 16. Parameter classes covered

**Label:** PROPOSITION / PROVED.  
**Provenance:** DERIVATION HERE.

Within an ordinary regular chart, local derivatives exist with respect to:

1. initial lifted phases;
2. initial alpha states \((\psi,q)\);
3. real coupling weights;
4. fixed physical delays;
5. any admissible scalar parameter entering the smooth segment flow, response, weights, delays, or smooth reset maps.

The derivatives follow by the event-chart theorem, segment variational equations, smooth reset composition, and (13.1)/(14.1).

## 17. Fixed-chart replay / JAX representation

**Label:** PROPOSITION / QUALIFIED.  
**Provenance:** DERIVATION HERE + ENGINEERING INTERPRETATION.

The mathematical derivative of Sections 13–16 can be represented by fixed-chart automatic differentiation **only if** the computational graph represents the same local chart map.

Required conditions include:

- physical rerecording identifies the current event sequence;
- every derivative is evaluated on that same certified sequence;
- event-time dependence is represented by differentiable root/implicit formulas or an equivalent correct custom derivative;
- no derivative is taken through a discrete \`argmin\`, stale event token, silently reordered collision, or a branch chosen from a different parameter point.

Ordinary AD of a scheduler containing discrete event-selection logic is **not** justified merely because a mathematical derivative exists.

Conversely, a fixed-chart JAX computation can be an exact representation of the local derivative while the physical scheduler remains the authority for selecting the chart.

## 18. Existence of a positive chart radius

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

Under the event-chart regularity theorem, there exists some radius

\[
\rho_*>0
\]

such that every \(\lambda\) with
\(\|\lambda-\lambda_0\|<\rho_*\)
remains in the same ordinary event chart.

This follows immediately because the finite set of transversality, separation and boundary margin functions is continuous and strictly positive at \(\lambda_0\).

## 19. Quantitative chart-radius bound

**Label:** PROPOSITION / PROVED UNDER STATED LIPSCHITZ BOUNDS.  
**Provenance:** DERIVATION HERE.

Let the finite regularity margins at \(\lambda_0\) be represented by positive scalar functions

\[
m_a(\lambda_0)>0,
\qquad a=1,\ldots,A,
\]

where each \(m_a\) is one of:

- a spike transversality;
- an event-time separation;
- an event-to-boundary distance.

If, on a candidate neighborhood,

\[
|m_a(\lambda)-m_a(\lambda_0)|
\le
K_a\|\lambda-\lambda_0\|,
\]

then every radius satisfying

\[
\boxed{
\rho
<
\min_a\frac{m_a(\lambda_0)}{2K_a}
}
\tag{19.1}
\]

for \(K_a>0\) preserves at least half of every margin.

Terms with \(K_a=0\) impose no radius restriction.

### Limitation

The theorem does not provide the \(K_a\) automatically. Rigorous numerical certification of a chart radius requires certified sensitivity/enclosure bounds for those margin functions.

A finite empirical perturbation test is evidence, not a proof of the full ball (19.1).

---

# Part V — T5: mathematical interpretation of RB-019

## 20. Pulse-aware segmentation

**Label:** PROPOSITION / MATHEMATICALLY JUSTIFIED.  
**Provenance:** DERIVATION HERE.

Arrival times are points where the target-local \(q\) state jumps and the analytic formula for subsequent \(\psi\) changes.

Therefore segmentation at every active arrival is a mathematically natural sufficient decomposition into intervals on which (2.1) is exact.

It is not merely an implementation heuristic.

### Qualification

Segmentation alone does not prove that every first hit has been found. Completeness additionally requires a correct no-hit or hit certificate on each segment.

## 21. Tail bounds

**Label:** PROPOSITION / MATHEMATICALLY JUSTIFIED UNDER EXPLICIT ASSUMPTIONS.  
**Provenance:** DERIVATION HERE.

RB-019-style alpha-tail control has a theorem-level basis through (8.4), (9.2)–(9.8), provided the omitted history satisfies an explicit absolute-tail summability or firing-density/minimum-separation assumption.

The particular RB-019 numerical error budget remains an engineering control. It is not promoted to a universal theorem.

## 22. Transversality threshold

**Label:** INTERPRETATION.

Mathematics requires

\[
\nu>0
\]

for the standard spike-time IFT.

The RB-019 threshold \`1e-10\` is a conservative engineering margin. The number \`1e-10\` is not mathematically distinguished and is not a theorem.

## 23. Collision tolerance

**Label:** INTERPRETATION.

Ordinary chart theory requires nonzero event separation.

RB-019's finite collision tolerance \`1e-8\` is an engineering decision for finite precision. It is not equivalent to the mathematical condition \(\delta_{\rm sep}>0\), and it is not retroactively promoted to a theorem.

## 24. Tape certification

**Label:** PROPOSITION / QUALIFIED.  
**Provenance:** DERIVATION HERE + ENGINEERING INTERPRETATION.

A tape satisfying finite-horizon first-hit completeness, transversality, event separation and boundary conditions is a valid local chart.

RB-019's \`NUMENG_PULSE_AWARE_REFERENCE_V1\` certification can therefore be interpreted as finite evidence that those requirements were checked inside its audited numerical envelope.

It is not proof of global first-hit correctness outside that envelope.

## 25. Fail-closed invalidity

**Label:** PROPOSITION / MATHEMATICALLY CONSERVATIVE.  
**Provenance:** DERIVATION HERE.

If the numerical method cannot certify first-hit completeness or regular chart conditions, refusing to assert a valid tape/derivative is logically sound.

Failure to certify does **not** imply that the physical trajectory is singular or incorrect.

Thus

\`UNCERTIFIED\`

and

\`MATHEMATICALLY INVALID\`

must remain distinct states.

## 26. Quadrature/root tolerances

**Label:** INTERPRETATION.

RB-019's QUADPACK/Brent tolerances, segment budgets, and finite search budgets are engineering controls.

A mathematical first-hit theorem requires either exact quantities or rigorous enclosures whose errors are shown small relative to the relevant first-hit/transversality/separation margins.

Ordinary floating-point tolerance values alone do not provide such a theorem.

---

# Part VI — T6: theory-derived stress fixtures for a later numerical gate

No fixture below is executed in CORE.

## 27. TH-FH-01 — narrow alpha pulse

**Label:** PROPOSED THEORY-DERIVED VALIDATION FIXTURE.

Use one target with a single known arrival at \(t=0\), \(\psi_0=0\), and

\[
q_0=A\alpha^2,
\]

so

\[
\psi(s)=A\alpha^2s e^{-\alpha s}.
\]

Choose a large predetermined \(\alpha\) and a phase gap whose exact first hit lies on the narrow pulse flank.

Required future checks:

- arrival segmentation must not skip the pulse;
- a certified phase-gain enclosure must bracket the first hit;
- coarse endpoint-only sampling is the negative control and must not be accepted as complete.

## 28. TH-FH-02 — near-threshold but noncrossing

**Label:** PROPOSED THEORY-DERIVED VALIDATION FIXTURE.

Choose \(h<0\), \(q_0=0\), \(\psi_0=h-\varepsilon\), and a horizon \(L\) satisfying

\[
e^{-\alpha L}(h-\varepsilon)\le h.
\]

Then

\[
\psi(s)\le h
\]

throughout the segment and

\[
G(L)=0.
\]

Required future check: certify no hit despite input lying arbitrarily close to the response threshold.

## 29. TH-FH-03 — nearly tangent regular first hit

**Label:** PROPOSED THEORY-DERIVED VALIDATION FIXTURE.

Choose \(q_0=0\), \(h<0\), a prescribed \(t_*>0\), and small \(\delta>0\). Set

\[
\psi_0=(h+\delta)e^{\alpha t_*},
\]

so

\[
\psi(t_*)=h+\delta.
\]

Define the phase gap prospectively as

\[
d=\int_0^{t_*}S(\psi(s))ds.
\]

Then \(t_*\) is a first-hit candidate with

\[
\nu_*=S(h+\delta)=e^{-r/\delta^2},
\]

which can be made arbitrarily small but positive.

Required future checks:

- event time remains finite and first-hitting;
- derivative magnitude scales like \(1/\nu_*\);
- decreasing \(\delta\) must eventually make a finite-precision certification fail closed rather than fabricate regularity.

## 30. TH-FH-04 — nearly simultaneous spike and arrival

**Label:** PROPOSED THEORY-DERIVED VALIDATION FIXTURE.

Construct an isolated regular spike candidate at exact time \(T_s\) and schedule an independent arrival at

\[
T_a=T_s+\varepsilon.
\]

Use predetermined cases

\[
\varepsilon>0,\qquad
\varepsilon<0,\qquad
\varepsilon=0.
\]

Required future checks:

- opposite signs give opposite valid event ordering;
- \(\varepsilon=0\) is an ordinary-chart collision;
- no neuron-index or queue-order tie break may manufacture differentiability.

## 31. TH-FH-05 — long-delay / old-tail dominated segment

**Label:** PROPOSED THEORY-DERIVED VALIDATION FIXTURE.

Place all omitted historical pulses at ages \(a_e\ge A\gg1/\alpha\), with an explicit convergent weight/age list.

Choose the remaining phase gap near, but prospectively separated from, the bound

\[
L_S\sum_e c_eM_\eta(a_e).
\]

Required future checks:

- computed omitted-tail enclosure satisfies (9.5);
- a no-hit/hit decision is accepted only when the residual phase margin exceeds the certified tail error;
- otherwise return \`UNCERTIFIED\`.

## 32. TH-FH-06 — structural zero-weight edge

**Label:** PROPOSED THEORY-DERIVED VALIDATION FIXTURE.

Add an edge with

\[
w_{ij}=0
\]

and arbitrary fixed delay.

Required future checks:

- physical state, first-hit time and derivatives with respect to unrelated parameters equal the graph with the zero edge removed;
- the zero edge must not create a spurious physical arrival competitor;
- an implementation that lets its delay reorder the chart is a negative control.

## 33. TH-FH-07 — horizon-boundary event

**Label:** PROPOSED THEORY-DERIVED VALIDATION FIXTURE.

Choose an analytically known regular spike at

\[
T_s=T_H-\varepsilon
\]

and cases \(\varepsilon>0\), \(\varepsilon=0\), \(\varepsilon<0\).

Required future check: only the strict interior case belongs to the current finite-horizon ordinary chart without a boundary convention change.

## 34. TH-FH-08 — simultaneous commuting arrivals

**Label:** PROPOSED THEORY-DERIVED VALIDATION FIXTURE.

Schedule two equal-time arrivals to distinct target components whose jumps commute.

Required future check:

- physical post-arrival state is independent of sequential processing order;
- ordinary labelled total-order chart certification must still reject zero separation;
- this demonstrates that physical well-posedness does not imply ordinary-chart regularity.

---

# Part VII — proposed finite validation requirements

## 35. Proposed later validation matrix

**Label:** PROJECT PROPOSAL / NOT EXECUTED.

A later MASTER-authorized numerical theory-validation gate should, at minimum, test:

1. exact alpha-state segment propagation against (2.1);
2. analytic segment extrema against (5.1)–(5.2);
3. no-hit upper certificates from (5.4);
4. unique-hit lower/bracket certificates from (6.2);
5. response derivative bounds (7.2) and selected higher-derivative checks;
6. tail mass identity (8.4) and phase-tail inequality (9.5);
7. event-order persistence under perturbations inside a predetermined regular-margin fixture;
8. spike-time derivative (13.1) against independently rerecorded finite differences;
9. arrival derivative (14.1) against independently rerecorded finite differences;
10. fail-closed behavior on TH-FH-01 through TH-FH-08;
11. explicit distinction between \`UNCERTIFIED\` and \`PHYSICALLY INVALID\`;
12. stale-tape rejection after an itinerary change.

No tolerance or fixture should be selected from later output.

---

# Part VIII — explicit non-results and open questions

## 36. No global first-hit theorem for arbitrary floating-point execution

**Label:** OPEN QUESTION / NON-RESULT.

This gate does not prove that an arbitrary finite-precision scheduler finds every first hit globally for all admissible states/parameters.

The theory supplies sufficient margin conditions and exact bounds that a future rigorous implementation may use.

## 37. No universal certified chart radius

**Label:** OPEN QUESTION / NON-RESULT.

Existence of a positive local chart radius is proved. A globally computable sharp radius over broad parameter boxes is not.

## 38. No theorem that RB-019 tolerances are optimal or universally sufficient

**Label:** NON-RESULT.

The numerical constants in RB-019 remain engineering controls.

## 39. No grouped-collision chart theory

**Label:** OPEN QUESTION.

Simultaneous commuting arrivals and other grouped events may admit a generalized smooth hybrid chart. This gate does not develop that theory.

## 40. No unconditional infinite-history tail theorem from local finiteness alone

**Label:** NON-RESULT.

Absolute tail summability or an equivalent spike-density/minimum-separation condition is required for the infinite-history bounds in Section 9.

## 41. No global equivalence between AD and physical hybrid derivatives

**Label:** NON-RESULT.

Fixed-chart AD is valid only after the chart map represented by the code is shown to match the mathematical local event map. Discrete scheduler branching is not differentiated by theorem.

## 42. No change to parked v0.27c execution

**Label:** GOVERNANCE NON-RESULT.

TR-27C-01 through TR-27C-07 remain UNEVALUATED. The \`2711xxx\` streams remain UNGENERATED / UNEVALUATED.

RB-015 remains SCIENTIFIC FAIL.

---

# Part IX — gate decision and proposed freeze

## 43. Gate decision

# PASS — FIRST-HIT / EVENT-CHART THEORY ESTABLISHED WITH EXPLICIT MARGINS AND CERTIFICATION LIMITS

The gate resolves T1–T5 at a narrow theorem level and supplies a finite theory-derived T6 stress suite.

The strongest proved additions are:

1. exact arrival-free alpha-state extrema and segment phase-gain bounds;
2. sufficient no-hit and unique-transversal first-hit certificates;
3. a finite-certification theorem under strict phase/transversality margins and convergent enclosures;
4. global \(C^\infty\) response regularity with explicit \(S'\) and \(S''\) bounds;
5. exact alpha remaining-mass and accumulated phase-tail error bounds;
6. a finite-event event-chart regularity theorem;
7. local differentiability of spike and arrival times with respect to initial state, weights, fixed delays and admissible smooth scalar parameters;
8. existence, but not automatic numerical certification, of a positive chart-validity neighborhood;
9. a precise theorem/engineering split for RB-019 segmentation, tail controls, thresholds, collision tolerances, tape certification and fail-closed semantics.

No global numerical first-hit correctness theorem is claimed.

## 44. Proposed theory freeze

If MASTER accepts this gate, establish

\`CORE Event-Chart Regularity & Certified First-Hit Theory Freeze 0.1\`

freezing only:

- Sections 3–19 mathematical statements under their explicit assumptions;
- Sections 20–26 theorem/engineering interpretation boundaries;
- the explicit open questions/non-results;
- TH-FH-01 through TH-FH-08 as theory-derived future validation fixtures, not as executed benchmarks.

The freeze must not convert RB-019 engineering tolerances into theorem constants and must not authorize v0.27c execution.

## STOP

STOP — RETURN TO MASTER; NO TR-27C EXECUTION; NO 2711XXX RNG; NO EFFECT-BEARING SCIENCE
