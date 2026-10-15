# CORE v0.22 — latent synaptic state and the spike-time information limit

## Scope

CORE v0.22 asks how much unknown continuous internal state can be carried by labelled Lighthouse spike times before the inverse problem becomes practically sloppy.

The v0.20/v0.21 unknown block

\[
(p,\tau_3,\eta_1,\eta_2)
\]

is enlarged by the **minimal non-trivial synaptic latent block**

\[
\boxed{\vartheta=(p,\tau_3,\eta_1,\eta_2,\xi_\psi,\xi_q)}.
\]

The phase perturbation remains gauge-fixed,

\[
\delta\phi_0=(\eta_1,\eta_2,-\eta_1-\eta_2).
\]

The new synaptic variables perturb the initial alpha-synapse state along one unit zero-mean spatial \(q=1\) contrast

\[
v=\frac{1}{\sqrt6}(2,-1,-1),
\]

so that

\[
\boxed{
\psi_0=\psi_{0,*}+\xi_\psi v,
\qquad
q_0=q_{0,*}+\xi_qv.
}
\]

Truth is

\[
\boxed{
(p_*,\tau_{3,*},\eta_{1,*},\eta_{2,*},\xi_{\psi,*},\xi_{q,*})
=(-3.267985407948901,8,0,0,0,0).
}
\]

This is intentionally not yet the full four-dimensional \(q=1\) synaptic subspace. Keeping two additional synaptic variables makes the total dimension six, so the old six-spike v0.20 baseline and the v0.21 six-spike designs can be compared nontrivially rather than failing by observation count alone.

Topology, packet occupancy, spike labels and the mean initial synaptic state remain known.

## Fixed-chart differential audit

The truth chart through four firing cycles contains 30 physical events and twelve candidate labelled spike times. The fixed-chart JAX replay reproduces the physical truth trajectory to machine precision, and the full \(12\times6\) Jacobian agrees with centered finite differences to relative error

\[
\boxed{4.07\times10^{-9}}.
\]

The full twelve-observation sensitivity matrix is formally rank six. Its singular values are

\[
\boxed{
(10.91371972,\;7.45684461,\;2.71638665,\;0.33185424,\;0.22877200,\;9.13748\times10^{-4}).
}
\]

Thus the problem is locally structurally identifiable on this chart, but extremely anisotropic:

\[
\boxed{\kappa_2\approx1.1944\times10^4}.
\]

The weakest right singular vector is approximately

\[
\boxed{
v_{\min}=(-4.14\!\times10^{-4},-7.07\!\times10^{-4},-0.54827,0.27421,0.78635,-0.07659).
}
\]

The weak direction is therefore almost entirely a combination of initial phase and initial synaptic state, especially \(\xi_\psi\); it contains essentially no \((p,\tau_3)\) component.

This is a different information bottleneck from v0.20. There the weakest direction was mainly a \(p/\tau_3\) tradeoff. Once initial synaptic state is admitted, the dominant ambiguity becomes an **initial-state decomposition ambiguity**.

## Nonlinear practical ambiguity

The near-null direction is not merely a linear-algebra artifact. Move a finite distance

\[
\vartheta=\vartheta_*+0.01v_{\min}.
\]

The physical packet scheduler records the **same event chart** and retains minimum chart margin

\[
\boxed{m_{\min}\approx0.0729046}.
\]

Nevertheless, across all twelve spike times the shift is only

\[
\operatorname{RMS}|\Delta t|\approx1.70\times10^{-5},
\]

with maximum

\[
\boxed{\max|\Delta t|\approx2.75\times10^{-5}}.
\]

For the v0.20/v0.21 noise scale \(\sigma_t=10^{-4}\), the full twelve-dimensional residual norm is only

\[
\boxed{\|\Delta Y\|/\sigma_t\approx0.588}.
\]

Hence a finite initial-state displacement of size \(10^{-2}\) along the weak direction is less than one total noise standard deviation away from truth even when all twelve spikes are used.

This ambiguity is **not caused by an event-order boundary**. It occurs deep inside the same regular hybrid chart.

## What happens to the old observation plans?

### v0.20 baseline: first six spikes

For indices

\[
S_{\rm base}=(0,1,2,3,4,5),
\]

the expanded six-unknown system remains formally rank six, but

\[
\boxed{\sigma_{\min}=8.83262\times10^{-4}},
\qquad
\kappa_2\approx8851.
\]

At \(\sigma_t=10^{-4}\), local Fisher standard deviations are approximately

\[
\boxed{
(6.46\!\times10^{-4},\;8.10\!\times10^{-4},\;0.0621,\;0.0310,\;0.0890,\;0.00870).
}
\]

Thus spike timing constrains \((p,\tau_3)\) moderately, but it hardly separates initial phase from synaptic contrast.

### The v0.21 E-optimal schedule is no longer optimal

The v0.21 four-unknown E-optimal schedule was

\[
S_{E,6}^{(v0.21)}=(1,2,3,4,9,11).
\]

Under the six-dimensional unknown block it gives

\[
\boxed{\sigma_{\min}=2.52371\times10^{-4}},
\qquad
\kappa_2\approx2.9253\times10^4.
\]

Although its \(p\) and \(\tau_3\) marginal errors remain better than the old baseline, its latent-state Fisher standard deviations become approximately

\[
(0.2188,\;0.1094,\;0.3104,\;0.0287),
\]

roughly factors \(3.3\)--\(3.5\) worse than the baseline latent uncertainties.

Therefore

\[
\boxed{\text{an observation design is only optimal relative to its assumed nuisance/latent space.}}
\]

A schedule optimized for the four-dimensional model can actively expose a new near-null direction when the model class is enlarged.

## Re-optimizing six spike times for the six-dimensional problem

Exhaustive enumeration of all six-subsets gives the E-optimal schedule

\[
\boxed{S_{E,6}^{(v0.22)}=(0,1,2,3,4,11)}
\]

with

\[
\boxed{\sigma_{\min}=8.95995\times10^{-4}}.
\]

This is only about 1.4% better than the v0.20 baseline in the weakest direction.

The D-optimal schedule is much more interpretable:

\[
\boxed{S_{D,6}^{(v0.22)}=(0,1,2,9,10,11)},
\]

i.e. **all three first-cycle spikes plus all three fourth-cycle spikes**.

Its weakest singular value remains

\[
8.90477\times10^{-4},
\]

but its Fisher standard deviations are

\[
\boxed{
(1.93\!\times10^{-4},\;2.95\!\times10^{-4},\;0.0616,\;0.0308,\;0.0883,\;0.00862).
}
\]

Relative to the v0.20 baseline this improves \(p\) by factor \(3.34\) and \(\tau_3\) by factor \(2.74\), while leaving all four initial-state uncertainties slightly better rather than sacrificing them.

Thus later cycles still help the physical parameters, but they do not resolve the phase/synaptic near-null direction.

## Longer spike-time observation does not cure the weak direction

For the best six-row E-optimal design constrained to the first two, three or four cycles,

\[
\sigma_{\min}^{E6}
\approx
8.8326\times10^{-4}
\to
8.9270\times10^{-4}
\to
8.9599\times10^{-4}.
\]

Using **all twelve** spike times gives only

\[
\boxed{\sigma_{\min}=9.1375\times10^{-4}},
\]

just 3.45% above the six-spike baseline.

This is the opposite of the v0.21 \(p/\tau_3\) result, where later cycles strongly improved the weak direction. The present synaptic perturbation is a decaying initial transient; after its early effect has been absorbed into phase, later spike timing contains little new information about how that initial transient was decomposed between \(\phi_0\), \(\psi_0\) and \(q_0\).

## Nonlinear aliases: square designs versus overdetermination

The six-row problem can have multiple exact nonlinear solutions even while the local Jacobian is nonsingular.

From the common start

\[
\vartheta_0=\vartheta_*+(0.01,-0.01,0.002,-0.002,0.003,-0.001),
\]

the old v0.21 E-optimal six-row schedule converges to the distinct state

\[
\boxed{
(-3.26799961,\;7.99996553,\;-0.00437740,\;0.00218983,\;0.00609092,\;-0.00050680).
}
\]

Its distance from truth is

\[
\boxed{7.83\times10^{-3}},
\]

and the displacement is aligned with the full-twelve weak singular vector at

\[
\boxed{0.999813}.
\]

The six selected spike times agree with truth to machine precision, while omitted spike times differ by as much as

\[
\boxed{4.12\times10^{-5}}.
\]

The alternate solution remains on exactly the same physical event chart with margin \(\approx0.07293\).

This demonstrates a genuine **nonlinear observation alias**, not a hybrid-chart artifact.

A deterministic 12-start audit separates this from linear conditioning:

- E-optimal 6 observations: 8/12 starts return truth; 4 reach an exact alternate root;
- E-optimal 7 observations: 7/12 return truth; remaining starts reach nearby nonzero-residual aliases;
- E-optimal 8 observations: 7/12 return truth; remaining starts reach nearby nonzero-residual aliases;
- E-optimal 9 observations: **12/12 return truth**;
- all 12 observations: **12/12 return truth**.

The E-optimal nine-row plan is

\[
\boxed{(0,1,2,3,4,5,7,9,11)}.
\]

Crucially, its smallest singular value is still only

\[
9.1269\times10^{-4}.
\]

Therefore overdetermination removes the observed nonlinear aliases without materially curing the local sloppy direction.

We must distinguish

\[
\boxed{\text{local conditioning} \neq \text{nonlinear uniqueness}.}
\]

## Small-noise Fisher audit

Because \(\sigma_t=10^{-4}\) would imply order-\(10^{-1}\) uncertainty along the weak linear direction, the local Gaussian approximation is already strongly nonlinear at that noise scale. The direct Fisher consistency audit is therefore performed at

\[
\sigma_t=10^{-6}.
\]

For 30 deterministic noise realizations, empirical standard deviations agree with local Fisher predictions within the benchmark tolerance for both the baseline and the v0.22 D-optimal plan. This verifies the JAX sensitivity calculation in its actual linear regime; it does **not** claim that a Gaussian Fisher approximation is reliable at \(10^{-4}\) for the synaptic latent state.

## Main conclusion

CORE v0.22 finds the first clear **continuous-state information limit** in the Lighthouse inference program:

\[
\boxed{
\text{labelled spike times alone can identify the expanded state formally,
while remaining practically almost blind to one phase/synapse combination.}
}
\]

The key lessons are:

1. enlarging the latent state can invalidate a previously optimal observation design;
2. later spike cycles still improve physical parameters but do not necessarily improve transient-state identifiability;
3. overdetermination can suppress nonlinear aliases even when the smallest singular value barely changes;
4. the new ambiguity is internal to a regular hybrid chart and must not be confused with event-order non-smoothness.

## Benchmark contract B351--B377

- **B351**: unknown block is \((p,\tau_3,\eta_1,\eta_2,\xi_\psi,\xi_q)\).
- **B352**: synaptic contrast mode is unit norm and zero mean, \((2,-1,-1)/\sqrt6\).
- **B353**: four-cycle physical chart has 30 events and twelve labelled spike candidates.
- **B354**: truth fixed-chart replay agrees with physical replay below \(2\times10^{-12}\).
- **B355**: six-parameter JAX Jacobian agrees with centered finite differences below \(10^{-8}\) relative error.
- **B356**: full twelve-row Jacobian has rank six.
- **B357**: full twelve-row \(\sigma_{\min}\approx9.13748\times10^{-4}\).
- **B358**: weak singular vector is dominated by latent initial-state coordinates and \(|v_{\xi_\psi}|>0.78\).
- **B359**: a \(0.01\) weak-direction displacement remains on the same physical chart.
- **B360**: that displacement changes no spike by more than \(0.30\sigma_t\) for \(\sigma_t=10^{-4}\).
- **B361**: v0.20 baseline six-row \(\sigma_{\min}\approx8.83262\times10^{-4}\).
- **B362**: v0.21 E-optimal six-row plan degrades to \(\sigma_{\min}\approx2.52371\times10^{-4}\).
- **B363**: v0.21 latent-state Fisher standard deviations worsen by more than factor 3.2 relative to baseline.
- **B364**: v0.22 E-optimal six-row plan is \((0,1,2,3,4,11)\).
- **B365**: v0.22 D-optimal six-row plan is \((0,1,2,9,10,11)\).
- **B366**: v0.22 D-optimal plan improves \(p\) Fisher std by more than factor 3.3.
- **B367**: v0.22 D-optimal plan improves \(\tau_3\) Fisher std by more than factor 2.7.
- **B368**: v0.22 D-optimal plan does not worsen any of the four latent-state Fisher std values versus baseline.
- **B369**: best six-row E-optimal \(\sigma_{\min}\) improves by less than 2% from cycle horizon 2 to 4.
- **B370**: all twelve rows improve baseline \(\sigma_{\min}\) by less than 4%.
- **B371**: the controlled v0.21 six-row solve has a distinct exact nonlinear alias on the same chart.
- **B372**: alias displacement aligns with the full-twelve weak vector by more than 0.999.
- **B373**: selected alias residual is below \(5\times10^{-13}\) while an omitted spike differs by more than \(3\times10^{-5}\).
- **B374**: direct 12-start audit finds alternate solutions for E-optimal 6- and 8-row schedules.
- **B375**: direct 12-start audit returns truth for all starts with E-optimal 9 rows and all 12 rows.
- **B376**: at \(\sigma_t=10^{-6}\), 30-realization baseline empirical std is within the stored Fisher-consistency tolerance.
- **B377**: the same small-noise Fisher-consistency test passes for the v0.22 D-optimal six-row plan.

## Scope boundary and next step

v0.22 does not infer the full two-dimensional \(q=1\) contrast independently in both \(\psi_0\) and \(q_0\), and it does not infer the spatial mean synaptic state. It also retains known topology and labelled spikes.

The next scientific target should not simply add more spike times. The weak direction has now been shown to saturate under spike-only observation. CORE v0.23 should test an **orthogonal observation or intervention** that directly exposes subthreshold synaptic state: for example one projected \(\psi\) or \(q\) measurement near the initial time, or a controlled input pulse whose transient response separates phase from synaptic state. Only after breaking this continuous-state ambiguity should the full \(q=1\) synaptic latent block or unknown spike labels be attempted.
