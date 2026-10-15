# CORE hybrid trust-region / multi-chart optimizer v0.19

## Purpose

CORE v0.19 turns the chart guard of v0.18 into an optimizer that can cross a hybrid event-order boundary without assigning a fictitious gradient to the switching surface.

The benchmark keeps the same controlled inverse problem:

\[
\theta=(p,\tau_3),
\qquad
\theta_*=(-3.267985407948901,8),
\]

with known topology, known initial hybrid state, and six labelled spike-time observations.

The new question is not local identifiability; v0.18 already certified that. The new question is:

> can a gradient method start in a different physical event chart, approach the event-order collision, cross it deliberately, rerecord the physical chart, and continue with the new one-sided derivative?

The answer for the benchmark is yes.

---

## 1. Tokenized event charts

A recorded chart is represented by fixed-shape token arrays

\[
C=(k_j,i_j,g_j,s_{j,1},s_{j,2})_{j=1}^{12},
\]

where `k` is arrival/firing type, `i` is the selected neuron or packet slot, `g` is a root initializer, and the two slot labels specify deterministic packet insertion after a firing event.

The continuous replay is

\[
Y(\theta;C)\in\mathbb R^6.
\]

All chart tokens are runtime arrays of one fixed shape. The same compiled JAX replay and Jacobian kernels therefore operate before and after a chart switch; changing the event itinerary changes data, not Python control flow or array shapes.

The discrete chart remains non-differentiable. Only

\[
D_\theta Y(\theta;C)
\]

inside a fixed physical chart is used.

---

## 2. Chart margin and collision prediction

For selected event `sigma_j`, define

\[
m_j(\theta;C)
=\min_{r\neq\sigma_j}\{t_r-t_{\sigma_j}\},
\qquad
m(\theta;C)=\min_j m_j.
\]

A chart is regular when

\[
m>0.
\]

Given a local step `s`, the first-order predicted distance to the nearest collision is

\[
\boxed{
\alpha_{\rm lin}
=-\frac{m}{\nabla m\cdot s}
}
\]

when `nabla m dot s < 0`.

If the proposed endpoint still has positive margin, ordinary trust-region/backtracking is used. If the endpoint has nonpositive margin, the solver brackets the first zero of

\[
\alpha\mapsto m(\theta+\alpha s;C)
\]

on the step segment.

It then:

1. moves to a safe point just before the zero;
2. evaluates a tiny physical crossing point just beyond the zero using the packet/event scheduler rather than the old fixed chart;
3. accepts the crossing only when the physical objective decreases;
4. records the new physical chart tokens;
5. resumes JAX differentiation with the new one-sided chart Jacobian.

No derivative of the discrete chart selection or event `argmin` is used.

---

## 3. Deliberate crossing benchmark

Start at

\[
\theta_0=(-4,8).
\]

This point is on the opposite firing-order side from the truth. The initial chart ends with

\[
F_2\to F_0\to F_1,
\]

whereas the truth chart ends with

\[
F_0\to F_2\to F_1.
\]

The initial objective is

\[
\Phi(\theta_0)=0.03500849360234459
\]

and the initial margin is

\[
m_0=0.03133095974702904.
\]

The trust-limited Gauss--Newton step is

\[
s=(0.55,-0.22766929).
\]

At the naive endpoint the old-chart margin would be

\[
\boxed{m(\theta_0+s)=-0.04552791793330435,}
\]

so blindly accepting the fixed-chart derivative would be invalid.

The margin gradient at the start is approximately

\[
\nabla m=(-0.14806738,-0.02037183).
\]

Hence

\[
\alpha_{\rm lin}=0.4079604094567599.
\]

Direct bracketing of the physical old-chart margin gives

\[
\boxed{\alpha_*=0.4067616722632621,}
\]

only

\[
\boxed{0.2947\%}
\]

relative error from the linear prediction.

The corresponding boundary point is

\[
\theta_B\approx(-3.77628108,7.90739286).
\]

The safe point has margin

\[
7.70965\times10^{-6}>0,
\]

while a small crossing step lands at

\[
\theta_C\approx(-3.77617108,7.90734732)
\]

and the physical event order changes from

\[
(F_2,F_0,F_1)
\quad\hbox{to}\quad
(F_0,F_2,F_1).
\]

The objective decreases monotonically across the guarded transition:

\[
0.03500849
\;\to\;
0.01667445
\;\to\;
0.01666124.
\]

---

## 4. Convergence after chart rerecording

After exactly one boundary hit and one physical chart rerecording, the solver converges in five iterations to

\[
\boxed{
(p,\tau_3)=(-3.2679854079489,8.0)
}
\]

with objective approximately

\[
2.1\times10^{-29}.
\]

Two additional cross-chart starts were tested:

- `(-4.1,7.8)`: one boundary hit, one chart switch, six iterations;
- `(-3.95,8.25)`: one boundary hit, one chart switch, five iterations.

A regular same-side start `(-3.5,8.2)` converges in four iterations with zero boundary hits and zero chart switches.

Thus the guard is not spuriously activated when no hybrid crossing is required.

---

## 5. One-sided gradient certification

The tokenized JAX Jacobian is checked against centered finite differences on both sides of the switching surface.

Before the crossing, at `(-4,8)`,

\[
\boxed{
\frac{\|J_{\rm JAX}-J_{\rm FD}\|_F}{\|J_{\rm FD}\|_F}
\approx9.16\times10^{-9}.
}
\]

Immediately after chart rerecording,

\[
\boxed{
\frac{\|J_{\rm JAX}-J_{\rm FD}\|_F}{\|J_{\rm FD}\|_F}
\approx4.84\times10^{-9}.
}
\]

This is the intended mathematical object: two accurate one-sided chart derivatives separated by a discrete chart transition.

---

## 6. Interpretation

CORE v0.19 establishes a practical rule for hybrid gradient-based inference:

\[
\boxed{
\text{differentiate within charts; detect, locate, and rerecord across chart boundaries.}
}
\]

The optimizer does **not** smooth the event-order `argmin` and does not pretend that the derivative is globally continuous.

This closes the first end-to-end chain from exact hybrid simulation to chart-aware gradient inference across an actual switching surface.

---

## 7. Scope

Certified here:

- known topology;
- known initial hybrid state;
- two continuous unknowns `(p,tau3)`;
- labelled spike-time data;
- one firing-order chart boundary;
- trust-limited Gauss--Newton steps;
- first-order boundary-distance prediction;
- safe step shortening;
- physical chart rerecording;
- reuse of fixed-shape JAX kernels across charts;
- one-sided Jacobian validation before and after the switch.

Not yet certified:

- simultaneous multi-surface saltation derivatives;
- latent initial-state inference;
- unknown topology;
- multiple closely spaced chart collisions;
- non-labelled spike matching;
- stochastic observation models beyond the v0.18 small-noise audit;
- large-N inverse problems.

The next CORE target should add latent-state/parameter blocks and multiple chart crossings while retaining this exact chart-boundary protocol.
