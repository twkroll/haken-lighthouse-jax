# CORE Event-Chart Regularity & Certified First-Hit Theory Freeze 0.1

Date: 2026-10-16
Status: FROZEN / STABLE SCIENTIFIC THEORY
Rollback point: RB-022

## Authority

MASTER reviews and accepts, jointly:

1. \`research/core/event_chart_first_hit_theory_gate_0_1.md\`
   - candidate blob SHA: \`a889d19d0679f61f75750db1cf8c51669857ade4\`
2. \`research/core/event_chart_first_hit_theory_semantic_repair_gate_0_1.md\`
   - repair blob SHA: \`53640bfd94b1bf24601710a81734c95fc24ff48b\`

The semantic-repair artifact is mandatory and supersedes the original candidate wherever the two conflict.

The original conflicting structural-zero statements remain audit history only.

## Frozen theory

RB-022 freezes the following theorem layer under the explicit assumptions stated in the two authority artifacts.

### 1. First-hit existence and exclusion

On an arrival-free segment with remaining phase gap \(d\) and accumulated phase

\[
G(s)=\int_0^s S(\psi(u))\,du,
\]

the frozen theory includes:

- no-hit sufficiency from strict upper bounds with \(G(L)<d\);
- existence from \(G(L)>d\);
- unique transversal first-hit brackets under strict phase and positive-response margins;
- endpoint/equality cases as chart/boundary cases rather than ordinary strict-interior certificates.

### 2. Exact arrival-free alpha-state structure

For

\[
\psi(s)=e^{-\alpha s}(\psi_0+s q_0),
\]

the derivative has at most one interior zero, giving a finite exact candidate set for extrema.

This supports finite upper/lower phase-gain bounds on subintervals.

### 3. Finite certification under strict margins

If outward-valid enclosures for accumulated phase converge under refinement, then:

- strict no-hit margins are finitely certifiable;
- strict first-hit brackets with positive transversality margins are finitely certifiable.

No theorem is frozen for zero-margin cases, exact tangencies, exact collisions, exact horizon events, or nonconvergent/nonrigorous error estimators.

### 4. Response regularity

The frozen response

\[
S_{r,h}(x)=
\begin{cases}
0,&x\le h,\\
\exp[-r/(x-h)^2],&x>h,
\end{cases}
\]

is globally \(C^\infty\).

RB-022 includes the explicit global first-derivative bound

\[
\|S'\|_\infty
=
\frac{2}{\sqrt r}
\left(\frac32\right)^{3/2}e^{-3/2},
\]

and the explicit second-derivative scaling

\[
\|S''\|_\infty=\frac{c_2}{r},
\]

with the constant identified in the authority artifact, plus the general scaling form

\[
\|S^{(k)}\|_\infty\le c_k r^{-k/2}.
\]

Threshold contact at \(\psi=h\) is therefore not itself a loss of smoothness in the frozen baseline response.

### 5. Alpha-tail and phase-error bounds

RB-022 freezes:

\[
M_\eta(A)=e^{-\alpha A}(1+\alpha A)
\]

for the remaining mass of the normalized alpha kernel, together with finite omitted-history input-tail and accumulated phase-error bounds under the stated absolute-tail / firing-density assumptions.

Local finiteness of infinite history alone is not promoted to a sufficient summability hypothesis.

### 6. Ordinary finite-event chart regularity

Under smooth segment dynamics, positive spike-transversality margin, positive labelled-event separation, arrival regularity, positive boundary margin and a finite event list, there exists a local parameter neighborhood in which:

- the same finite labelled event types occur in the same ordinary order;
- spikes remain transversal;
- spike and scheduled-arrival times are smooth functions of parameters;
- event-indexed states are smooth;
- the fixed event tape is a valid local chart.

This is a local ordinary-chart theorem, not a global hybrid differentiability theorem.

### 7. Structural-zero semantics — mandatory repaired convention

The fixed structural topology is independent of coupling value.

For every structural edge \(e=(j\to i)\), including \(w_e=0\),

\[
A_e=T_{\rm launch}+\tau_e
\]

remains a labelled delayed arrival.

The alpha-state event map is

\[
q_i^+=q_i^-+w_e\alpha^2.
\]

At \(w_e=0\), the state jump is the identity but the labelled structural arrival remains present in the topology-fixed event tape.

Therefore:

- graph-with-edge-omitted and graph-with-edge-present-at-zero can have identical physical state/spike trajectories at the exact zero value while having different labelled event tapes;
- topology must not be created/deleted when a structural weight crosses zero;
- ordinary chart separation/collision conditions include structural-zero arrivals;
- identity arrival maps do not invalidate the finite-event chart theorem.

This repaired convention supersedes the conflicting original candidate text.

### 8. Local derivatives at structural zero

The jump-map derivative satisfies

\[
\partial_{w_e}(q_i+w_e\alpha^2)=\alpha^2.
\]

For a structural pulse contribution

\[
\psi_e(t;w)=w\,\eta_\alpha(t-A_e(w)),
\]

the derivative at \(w=0\) is

\[
\left.\partial_w\psi_e(t;w)\right|_{w=0}
=
\eta_\alpha(t-A_e(0)).
\]

Hence downstream sensitivity with respect to a structural weight at zero need not vanish.

No blanket nonzero claim is made for every observable.

The labelled arrival-time derivative with respect to its delay coordinate remains

\[
D_{\tau_e}A_e=D_{\tau_e}T_{\rm launch}+1.
\]

At zero coupling, physical spike times may be locally insensitive to that delay while the labelled arrival moves and chart margins change.

### 9. Local event-time differentiability

Within a regular fixed topology/event chart, spike times inherit the standard implicit-function sensitivity

\[
D_\lambda T
=
-\frac{D_\lambda \theta(T)|_{t\ {\rm fixed}}}
{S(\psi(T^-))}
\]

under positive transversality.

Arrival times inherit the corresponding delayed-launch derivative.

The freeze distinguishes:

- mathematical derivative existence;
- validity of the fixed chart;
- representation by JAX/fixed-chart replay;
- numerical ability to certify chart validity.

JAX is not itself a physical certificate.

### 10. Positive chart neighborhood

RB-022 freezes existence of a positive local chart-validity neighborhood under strict margins and smoothness assumptions.

It does not freeze a globally sharp or universally computable chart radius.

## Theory-derived future validation fixtures

RB-022 freezes TH-FH-01 through TH-FH-08 as theory-derived future validation fixtures, NOT as executed evidence.

TH-FH-06 is the repaired topology-fixed structural-zero fixture from the semantic-repair artifact and supersedes the original candidate TH-FH-06.

The fixture family includes:

- narrow alpha first-hit;
- near-threshold no-hit;
- near-tangent/transversality stress;
- near/simultaneous labelled events;
- omitted-history/tail-error stress;
- topology-fixed structural-zero edge;
- horizon-boundary event;
- simultaneous commuting arrivals / grouped-event distinction.

## Engineering interpretation boundary

RB-022 does not promote RB-019/RB-021 numerical constants such as collision tolerances, quadrature tolerances, event-time tolerances or runtime budgets into theorem constants.

It does not prove:

- global floating-point first-hit correctness;
- formal interval-arithmetic certification;
- universal chart-radius computability;
- grouped-collision chart theory;
- unconditional infinite-history tail control from local finiteness alone;
- global equivalence of AD and physical hybrid derivatives;
- universal speedup/scaling properties.

## Preserved governance boundaries

RB-022 does not:

- change RB-015 SCIENTIFIC FAIL;
- execute RB-020/TR-27C;
- create any \`2711xxx\` RNG object;
- authorize APP-3;
- authorize v0.28 effect-bearing science;
- create novelty/manuscript claims.

## STOP

RB-022 is a scientific-theory freeze only.

STOP — FROZEN / STABLE SCIENTIFIC THEORY
