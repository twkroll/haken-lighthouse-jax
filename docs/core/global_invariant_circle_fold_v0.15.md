# CORE global hybrid invariant-circle fold v0.15

## Purpose

CORE v0.15 closes the global hysteresis mechanism discovered in v0.14.

At the fixed ring coupling

\[
p=-3.267985407948901
\]

the full three-cell packet-queue Lighthouse network has, near \(\tau_3=8\),

1. the stable synchronous orbit;
2. a large stable timing-modulated attractor;
3. an unstable basin-boundary object separating the two basins.

v0.15 classifies the two nontrivial objects and replaces the v0.14 empirical
upper persistence bracket by a quantitative hybrid fold condition.

The main conclusion is

\[
\boxed{\text{stable hybrid invariant circle}
+\text{ unstable hybrid invariant circle}
\longrightarrow
\text{ saddle-node/fold of invariant circles}.}
\]

The fold is near

\[
\boxed{\tau_F\simeq 8.00731.}
\]

This is a **global** fold. It is distinct from the small-amplitude FIC near the
v0.9 Chenciner point.

---

# 1. Why the v0.11 smooth circle map is not sufficient globally

The v0.11 exact circle solver assumes a fixed arrival itinerary. That
assumption is valid for the small circles near Chenciner but fails for the
large v0.14 timing attractor.

Let \(T_i^m\) be the target spike and let the short edge have delay 2. Along
the large circle at \(\tau_3=8\),

\[
\Delta_{\rm short}=T_{i-1}^m+2-T_i^m
\]

ranges approximately over

\[
\boxed{-0.31152993\lesssim\Delta_{\rm short}\lesssim4.70342075.}
\]

Hence the invariant object crosses the event-order surface

\[
\Delta_{\rm short}=0.
\]

A single smooth fixed-itinerary chart therefore cannot be continued through
the whole large object. v0.15 works directly with the full packet-queue
dynamics, which changes event order causally when the trajectory crosses that
surface.

This is the first CORE invariant-object benchmark that is intrinsically
piecewise-smooth at the event-chart level.

---

# 2. Classification of the large attractor

Define the physical complex \(q=1\) timing amplitude after cycle \(m\),

\[
Z_m=\frac{1}{3}\sum_{j=0}^2(T_j^m-\bar T^m)e^{-2\pi i j/3}.
\tag{GF1}
\]

At \(\tau_3=8\) the mean radius is approximately

\[
\langle |Z|\rangle=0.71814532.
\]

A linear regression of the unwrapped argument over 15000 cycles gives the
rotation number

\[
\boxed{\rho=0.03851429562}
\tag{GF2}
\]

turns per spike cycle.

The closest rational with denominator at most 50 is

\[
\frac1{26}=0.03846153846,
\]

but

\[
\boxed{\rho-\frac1{26}=5.2757160\times10^{-5}.}
\tag{GF3}
\]

The 26-cycle recurrence error is not stationary noise. Its RMS values grow
approximately as

\[
\|Z_{m+26}-Z_m\|_{\rm RMS}=6.29835\times10^{-3},
\]

\[
\|Z_{m+52}-Z_m\|_{\rm RMS}=1.25966\times10^{-2},
\]

\[
\|Z_{m+104}-Z_m\|_{\rm RMS}=2.51921\times10^{-2}.
\]

Thus the object is not a period-26 orbit.

A rigid-rotation Fourier representation

\[
Z_m\simeq\sum_{k=-M}^{M}c_k e^{ik(m\omega+\phi_0)}
\tag{GF4}
\]

with \(M=10\) gives

\[
\boxed{{\rm RMS}=2.37503\times10^{-4},\qquad |c_1|=0.71615791.}
\tag{GF5}
\]

With \(M=20\) the RMS falls to about \(3.0\times10^{-5}\).

CORE therefore classifies the v0.14 large attractor as a

\[
\boxed{\textbf{quasiperiodic hybrid invariant circle}.}
\]

The adjective *hybrid* records the arrival-order switching described above.

---

# 3. A transverse phase-return multiplier without a fixed itinerary

Because the event itinerary changes around the circle, v0.15 does not
differentiate the v0.11 fixed-itinerary formula.

Instead the full packet-queue trajectory itself defines a local circle chart.

From a long attracting trajectory construct the radial graph

\[
r_*(\vartheta)=|Z|\quad\text{at}\quad\vartheta=\arg Z
\tag{GF6}
\]

by periodic cubic interpolation.

For a nearby full packet state define the transverse observable

\[
d_m=|Z_m|-r_*(\arg Z_m).
\tag{GF7}
\]

Sample \(d_m\) whenever the unwrapped circle phase crosses one fixed ray.
Successive samples correspond to one full rotation around the invariant
circle. In the linear regime,

\[
d_{k+1}=\mu_{\perp,\rm rot}d_k+O(d_k^2).
\tag{GF8}
\]

This construction is invariant to the tangent phase drift to first order and
requires no assumption about which packet arrives first inside the rotation.

For the attracting large-circle branch:

| \(\tau_3\) | \(\mu_{\perp,\rm rot}\) |
|---:|---:|
| 8.00400 | 0.78431228 |
| 8.00600 | 0.86499368 |
| 8.00700 | 0.93581548 |
| 8.00720 | 0.96123381 |
| 8.00725 | 0.97179225 |

At \(\tau_3=8.0072\), changing the injected radial perturbation from
\(2\times10^{-6}\) to \(8\times10^{-6}\) gives

\[
0.96127812,\qquad0.96122752,
\]

with the \(4\times10^{-6}\) reference value

\[
0.96123381.
\]

Thus the measured factor is already in the finite-difference linear regime.

---

# 4. Multiplier approach to +1

For a generic saddle-node of invariant circles the stable normal return
multiplier obeys

\[
1-\mu_{\perp,s}=K\sqrt{\tau_F-\tau_3}+o(\sqrt{\tau_F-\tau_3}).
\tag{GF9}
\]

Fitting all five measured multipliers gives

\[
\boxed{K=3.74366,\qquad\tau_F^{(5)}=8.00730554,}
\tag{GF10}
\]

with multiplier RMS error

\[
6.37\times10^{-4}.
\]

Restricting the fit to the three closest points
\((8.007,8.0072,8.00725)\) gives

\[
\boxed{K=3.64831,\qquad\tau_F^{(3)}=8.00731073,}
\tag{GF11}
\]

with RMS

\[
2.63\times10^{-4}.
\]

The v0.14/v0.15 ghost-escape calculation independently gave

\[
\boxed{\tau_F^{\rm escape}\simeq8.00731041}
\tag{GF12}
\]

from

\[
N_{\rm escape}=N_0+\frac{C}{\sqrt{\tau_3-\tau_F}}.
\tag{GF13}
\]

The near-fold multiplier estimate and escape estimate differ by only about

\[
3.2\times10^{-7}.
\]

The benchmark reference is therefore recorded conservatively as

\[
\boxed{\tau_F=8.00731}
\]

rather than attaching unjustified additional digits to a piecewise-smooth
finite-trajectory computation.

---

# 5. Direct unstable-circle edge tracking

At \(\tau_3=8.0072\), radial perturbations of the same stable-circle phase
bracket the basin boundary extremely tightly.

A representative pair is

\[
\delta A_{\rm large}=-0.00809,\qquad
\delta A_{\rm sync}=-0.00809125.
\tag{GF14}
\]

The two trajectories remain close to the same intermediate circle for
thousands of cycles and then separate toward the large-circle and synchronous
attractors respectively.

During the shadowing interval the intermediate circle has mean timing
amplitude approximately

\[
\boxed{\langle A\rangle_u\simeq0.67738.}
\tag{GF15}
\]

The phase-conditioned growth of the separation of the two bracketing
trajectories gives

\[
\boxed{\mu_{\perp,u,\rm rot}\simeq1.04004.}
\tag{GF16}
\]

For the stable circle at the same parameter,

\[
\mu_{\perp,s,\rm rot}=0.96123381,
\]

so

\[
\frac{1}{\mu_{\perp,s,\rm rot}}=1.04032961.
\]

The direct unstable estimate differs from this leading saddle-node reciprocal
prediction by less than \(3\times10^{-4}\) in relative terms.

Thus both sides are observed directly:

\[
\boxed{\mu_{\perp,s}<1<\mu_{\perp,u},\qquad
\mu_{\perp,s},\mu_{\perp,u}\to1
\text{ as }\tau_3\to\tau_F^-.}
\tag{GF17}
\]

---

# 6. Independent square-root and ghost signatures

The multiplier test is not used in isolation.

Previous direct edge tracking gave a stable/unstable circle separation of
order

\[
\Delta A\propto\sqrt{\tau_F-\tau_3}.
\tag{GF18}
\]

Above the loss point, the long transient obeys the inverse square-root
saddle-node ghost law (GF13).

We therefore have three mutually independent signatures of the same object:

1. stable and unstable invariant circles coexist below the boundary;
2. their normal return multipliers approach \(+1\);
3. branch separation and post-fold escape time have the two complementary
   square-root scalings.

CORE v0.15 therefore classifies the upper v0.14 persistence boundary as a

\[
\boxed{\textbf{numerically nondegenerate hybrid fold / saddle-node of invariant circles}.}
\]

"Numerically nondegenerate" here means that the observed square-root
coefficients are finite and nonzero and that the two normal multipliers
approach one from opposite sides. It does **not** claim a globally smooth
single-itinerary Poincare map.

---

# 7. Consequence for the hysteresis mechanism

The global organization at fixed \(p\) is now:

\[
\text{synchronous orbit}\quad\text{(stable)}
\]

coexisting with

\[
\text{large stable hybrid invariant circle},
\]

with an

\[
\text{unstable hybrid invariant circle}
\]

as basin boundary.

At

\[
\tau_3=\tau_F\simeq8.00731
\]

the stable and unstable circles annihilate.

This closes the mechanism behind the history dependence first seen in v0.14:

\[
\boxed{\text{global hysteretic memory}
=\text{sync attractor}
+\text{stable large circle}
+\text{unstable basin-boundary circle}
+\text{global circle fold}.}
\tag{GF19}
\]

This is categorically different from the small local Chenciner wedge, which
correctly had no stable synchrony/stable-small-circle coexistence.

---

# 8. Benchmark contract B205--B224

**B205 — complex timing coordinate.** Use (GF1) for global circle diagnostics.

**B206 — large-circle rotation.** At \(\tau_3=8\),
\(\rho\approx0.03851430\).

**B207 — low-order nonlocking.** The nearest denominator-\(\le50\) rational is
\(1/26\), but the measured rotation differs by more than \(5\times10^{-5}\).

**B208 — period-26 rejection.** The 26-cycle RMS recurrence error exceeds
\(5\times10^{-3}\) and grows approximately linearly for 52 and 104 cycles.

**B209 — Fourier circle representation.** An \(M=10\) rigid-rotation fit has
RMS below \(4\times10^{-4}\).

**B210 — hybrid itinerary.** The short-arrival margin takes both signs on the
large circle.

**B211 — no fixed-itinerary extrapolation.** The large fold must not be
certified using the single smooth v0.11 arrival chart.

**B212 — transverse observable.** Use a phase-corrected distance to the
full-engine circle rather than raw amplitude decay.

**B213 — stable normal multiplier.** At \(\tau_3=8.0072\),
\(\mu_{\perp,s,\rm rot}\approx0.96123\).

**B214 — perturbation convergence.** Stable multiplier estimates from radial
impulses \(2\times10^{-6}\) and \(8\times10^{-6}\) differ by less than
\(10^{-3}\).

**B215 — stable fold scaling.** The multiplier table follows (GF9).

**B216 — all-point fold fit.** The five-point multiplier fit gives
\(\tau_F\) within \(10^{-5}\) of 8.00731.

**B217 — near-fold convergence.** The nearest-three-point multiplier fit gives
\(\tau_F\) within \(2\times10^{-6}\) of 8.00731.

**B218 — ghost agreement.** The near-fold multiplier and escape-time fold
estimates agree within \(10^{-6}\).

**B219 — edge circle.** Basin edge tracking at \(\tau_3=8.0072\) exhibits a
long-lived intermediate quasiperiodic circle.

**B220 — unstable normal multiplier.** Its full-rotation multiplier is about
1.04 and exceeds one.

**B221 — reciprocal saddle-node test.** The unstable multiplier agrees with
the reciprocal stable multiplier to better than \(10^{-3}\).

**B222 — opposite stability.** Stable and unstable circles lie on opposite
sides of normal multiplier one.

**B223 — global classification.** The upper persistence boundary is a hybrid
fold/saddle-node of invariant circles, not merely a finite-time crisis label.

**B224 — scope.** Exact saltation/AD through a fixed-capacity representation of
all packet-order charts remains a separate implementation target; the v0.15
classification is based on the direct full packet dynamics and its transverse
phase-return derivative.

---

# 9. Next CORE step

The mathematical core has now identified the global hysteresis object. The
next step should move from the imperative oracle to a differentiable
fixed-capacity packet representation.

CORE v0.16 should:

1. define a fixed-capacity JAX packet queue with mask-based active slots;
2. implement differentiable continuous propagation between events;
3. implement spike and arrival saltation maps;
4. treat event-order switching with explicit chart diagnostics rather than
   pretending the map is globally smooth;
5. reproduce v0.14 dynamic skip and the v0.15 large-circle fold;
6. compare exact packet-queue multipliers against JAX tangent propagation.

Only after those tests should the project scale the adaptive model to larger
graphs or use gradient-based inference on conduction dynamics.
