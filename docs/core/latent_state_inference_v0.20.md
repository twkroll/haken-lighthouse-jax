# CORE v0.20 — latent initial-state inference and sequential chart crossings

## Scope

CORE v0.20 extends the v0.18/v0.19 inverse problem from two physical parameters to a four-dimensional continuous unknown block

\[
\vartheta=(p,\tau_3,\eta_1,\eta_2).
\]

The graph topology, initial synaptic state \((\psi_0,q_0)\), and packet occupancy are known. The two new variables describe a gauge-fixed latent initial phase perturbation

\[
\delta\phi_0=(\eta_1,\eta_2,-\eta_1-\eta_2),
\]

so the common phase component is not duplicated. Truth is

\[
(p_*,\tau_{3,*},\eta_{1,*},\eta_{2,*})=(-3.267985407948901,8,0,0).
\]

The six labelled spike times are the same two-cycle observations introduced in v0.18.

## Local identifiability

At truth the six-by-four sensitivity matrix is

\[
J=\frac{\partial Y}{\partial(p,\tau_3,\eta_1,\eta_2)}\approx
\begin{pmatrix}
0&0&-2.26983787&0\\
0&0&2.32222406&2.32222406\\
0&0&8.04195\!\times10^{-9}&-2.36892700\\
-0.37611719&0.32080597&-2.57178765&-1.12487260\\
-0.24223002&0.32800639&1.62862546&2.90965799\\
-0.48857785&0.25857154&0.90529124&-1.74959201
\end{pmatrix}.
\]

Its singular values are

\[
\boxed{(5.81134164,\;3.26704426,\;0.82982598,\;0.10170598)},
\]

hence rank four and

\[
\boxed{\kappa_2(J)=57.13864464}.
\]

The JAX Jacobian agrees with centered finite differences to relative error

\[
\boxed{1.24\times10^{-9}}.
\]

The first three spikes contain no information about \((p,\tau_3)\): their first two Jacobian columns vanish. They do, however, have rank two in the latent-phase columns. Prefix ranks for 3, 4, 5 and 6 spike observations are

\[
\boxed{(2,3,4,4)}.
\]

Thus five labelled spikes are the minimum for local rank-four recovery in this chart; the sixth improves the weakest singular value from approximately

\[
0.0499612\to0.101706.
\]

The weakest right singular vector is

\[
(-0.62490,-0.78018,-0.01243,0.02566),
\]

so the remaining weak direction is predominantly a \((p,\tau_3)\) tradeoff rather than a latent-phase ambiguity.

For spike-time noise \(\sigma_t=10^{-4}\), joint Fisher standard deviations are

\[
\boxed{(6.216\!\times10^{-4},\;7.708\!\times10^{-4},\;2.846\!\times10^{-5},\;3.482\!\times10^{-5})}.
\]

Relative to v0.18, marginal uncertainty in \(p\) and \(\tau_3\) grows only by factors

\[
\boxed{1.4529\quad\text{and}\quad1.4323}.
\]

The \(p\)-\(\tau_3\) correlation is approximately \(0.969\). A deterministic 20-realisation noise audit gives empirical standard deviations

\[
(5.646\!\times10^{-4},\;6.483\!\times10^{-4},\;2.133\!\times10^{-5},\;3.036\!\times10^{-5}),
\]

consistent with the local scale prediction.

## Event-margin vector

For a recorded chart \(C\), v0.19 used the scalar guard

\[
m(\vartheta;C)=\min_j m_j(\vartheta;C),
\]

where \(m_j\) is the selected-event time minus its nearest competitor at event index \(j\), with positive sign inside the chart. With latent initial state, different event margins can become active along one optimization step. The gradient of the scalar minimum can therefore point away from the *next* boundary.

v0.20 therefore records the full event-margin family

\[
\mathbf m=(m_0,\ldots,m_{11})
\]

for boundary prediction. For a proposed step \(s\), each approaching surface has the linear estimate

\[
\alpha_j^{\rm lin}=-\frac{m_j}{\nabla m_j\cdot s},\qquad
\nabla m_j\cdot s<0,
\]

and the smallest positive candidate predicts the next active boundary. The exact physical crossing used by the optimizer is still located by the scalar physical guard and bracketing before the chart is rerecorded; no linear predictor is treated as the crossing itself.

This distinction is essential: at the second sequential crossing below, the scalar minimum margin is \(1.21\times10^{-4}\) but its directional derivative is positive, giving the meaningless scalar prediction \(\alpha\approx-2.90\times10^{-4}\). The event-vector predictor correctly selects event 9 and predicts the upcoming boundary.

## Sequential two-boundary benchmark

Use the latent start

\[
\boxed{\vartheta_0=(-3.2,7.7,-0.07,-0.12)}.
\]

The multi-chart solver converges in five iterations to truth with two boundary hits and two physical chart rerecordings.

### First crossing — first-cycle firing order

The trust-limited step from the start crosses the boundary at

\[
\alpha_*^{(1)}=0.30185850641.
\]

The event-margin-vector prediction is

\[
\alpha_{\rm lin}^{(1)}=0.30256790936,
\]

only \(0.235\%\) high. The collision exchanges event indices 0 and 1:

\[
(F_2,F_0,F_1)\longrightarrow(F_0,F_2,F_1)
\]

for the first firing triplet. Objective values satisfy

\[
0.33179263\to0.16149891\to0.16135951
\]

from old point to safe point to physical cross point. The pre/post one-sided JAX Jacobian checks have relative errors \(1.71\times10^{-9}\) and \(1.26\times10^{-9}\).

### Second crossing — second-cycle firing order

Later in the same optimization, event margin 9 becomes the relevant approaching surface. The exact crossing is

\[
\alpha_*^{(2)}=0.85498339245,
\]

while the vector prediction gives

\[
\alpha_{\rm lin}^{(2)}=0.86679098173,
\]

a relative error of \(1.381\%\). This exchanges event indices 9 and 10, i.e. the first two firings of the second observed cycle. The objective decreases

\[
0.16135951\to0.00322857\to0.00321480.
\]

The pre/post JAX-vs-FD errors are \(1.50\times10^{-9}\) and \(8.65\times10^{-10}\).

Thus the two switching surfaces are distinct in event index and encountered sequentially, not a simultaneous multi-surface collision.

## Optimization-path dependence from latent state

A regular start \((-3.5,8.2,0.05,-0.04)\) converges in four iterations without chart changes. A one-boundary start \((-3.0,7.7,-0.08,0.06)\) converges in five iterations with one switch. The two-boundary start above converges in five iterations with two switches.

A particularly useful comparison is

\[
(-4,8,0,0):\quad 1\text{ boundary hit},
\]

versus

\[
(-4,8,0.03,-0.02):\quad 0\text{ boundary hits}.
\]

Allowing latent initial state can therefore route the trust-region path around a parameter-only event boundary even when the physical target is unchanged.

## Interpretation

For this benchmark, latent relative phase is not a source of structural non-identifiability. It modestly degrades parameter precision while remaining strongly observed by the first-cycle spike times. Its more important effect is geometric: it increases the dimension of parameter space in which event-order surfaces must be negotiated and can create multiple sequential chart crossings.

CORE v0.20 therefore augments the exact scalar physical chart guard with an event-indexed margin family for reliable boundary prediction. Scientific derivatives remain one-sided fixed-chart derivatives; exact crossing and chart rerecording remain physical event-scheduler operations.

## Benchmark contract B309–B328

B309 gauge-fixed two-dimensional latent phase block; B310 truth replay; B311 JAX/FD Jacobian agreement; B312 full rank four; B313 condition number below 60; B314 first-cycle parameter columns zero; B315 first-cycle latent rank two; B316 four-observation rank three; B317 five-observation rank four; B318 six-observation smallest singular value above 0.1; B319 weakest singular direction parameter-dominated; B320 parameter uncertainty inflation between 1.35 and 1.55; B321 deterministic noise audit; B322 regular no-switch recovery; B323 one-switch recovery; B324 two-switch recovery; B325 first switch exchanges events 0/1; B326 second switch exchanges events 9/10; B327 vector-margin boundary predictions within 2%; B328 objective descent and one-sided JAX/FD validation across both crossings.

## Not claimed

v0.20 does not infer latent \(\psi\) or \(q\), unknown topology, unlabelled spikes, missing spikes, or simultaneous codimension-two event collisions. The two certified boundaries are well-separated sequential chart changes.
