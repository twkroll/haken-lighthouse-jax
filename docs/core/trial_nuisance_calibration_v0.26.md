# CORE v0.26 — trial-specific preparation and pulse-calibration nuisance

## Scope

CORE v0.25 showed that two complementary chart-safe pulse experiments identify the full real q=1 latent synaptic state when both trials start from the **same** unknown preparation.

v0.26 removes that reproducibility assumption. The shared network parameters are only

\[
\theta_s=(p,\tau_3),
\]

while trial \(r\in\{1,2\}\) has its own latent initial state

\[
z_r=(\eta_{1r},\eta_{2r},\xi_{\psi1,r},\xi_{\psi2,r},\xi_{q1,r},\xi_{q2,r}).
\]

The two pulse controls may also differ from their nominal calibration by

\[
\delta u_r=(\delta t_{p,r},\delta A_r,\delta\beta_r,\delta\gamma_r).
\]

The scientific target changes accordingly: v0.26 does **not** require every trial nuisance coordinate to be uniquely recoverable. It asks which **shared network parameters** remain identifiable after profiling out preparation and calibration nuisance.

---

## Reference non-identical preparations

The two deterministic preparation offsets are

\[
z_1=(0.0015,-0.0010,0.0030,-0.0020,0.0010,-0.0005),
\]

\[
z_2=(-0.0003,0.000325,-0.000625,0.00055,-0.0002,0.000175).
\]

The nominal v0.25 pulses are perturbed by

\[
\delta u_1=(0.001,-0.001,0.010,-0.008),
\]

\[
\delta u_2=(-0.0015,0.001,-0.012,0.006).
\]

Thus the actual controlled trials use

\[
P_1^{\rm true}=(0.051,0.099,0.56,-0.108),
\]

\[
P_2^{\rm true}=(0.0485,0.101,0.188,3.026).
\]

Both remain chart-safe:

\[
\boxed{m_1\approx0.07483243},\qquad
\boxed{m_2\approx0.06081747}>0.06.
\]

---

## Trial-specific state nuisance

Let one trial sensitivity be partitioned as

\[
J_r=[J_{s,r}\;N_r],
\]

where \(J_{s,r}\in\mathbb R^{12\times2}\) contains derivatives with respect to \((p,\tau_3)\), and \(N_r\in\mathbb R^{12\times6}\) contains derivatives with respect to the trial-specific initial state.

The full two-trial Jacobian has shape \(24\times14\):

\[
J_{14}=
\begin{pmatrix}
J_{s,1}&N_1&0\\
J_{s,2}&0&N_2
\end{pmatrix}.
\]

It is rank 14, but the full nuisance problem is still highly conditioned because each individual preparation contains weak phase/synapse directions.

For the shared parameters the correct object is the nuisance-profiled sensitivity

\[
R_r=(I-P_{N_r})J_{s,r},
\]

and

\[
R=\begin{pmatrix}R_1\\R_2\end{pmatrix}.
\]

Numerically,

\[
\boxed{\sigma(R)\approx(1.11043772,0.32439413)}.
\]

At spike-time noise \(\sigma_t=10^{-4}\),

\[
\boxed{\operatorname{sd}(p)\approx1.5449\times10^{-4}},
\]

\[
\boxed{\operatorname{sd}(\tau_3)\approx2.8155\times10^{-4}}.
\]

Relative to v0.25's identical-preparation two-trial experiment, this is only about \(1.22\times\) worse for \(p\) and \(1.57\times\) worse for \(\tau_3\).

This is the first explicit CORE example where the shared scientific parameters remain well identified even though the trial-specific hidden states are individually sloppy.

---

## Structural pulse-calibration ambiguity

Let

\[
K_r=\partial_{u_r}Y_r
\]

be the four calibration columns in the order

\[
(t_p,A,\beta,\gamma).
\]

After projection onto the complement of the trial-state nuisance space, the column norms are approximately

\[
\|(I-P_{N_1})K_1\|
\approx
(5.54\times10^{-7},1.50\times10^{-9},1.19\times10^{-10},1.46\times10^{-10}),
\]

\[
\|(I-P_{N_2})K_2\|
\approx
(3.59\times10^{-8},2.48\times10^{-10},6.75\times10^{-12},1.58\times10^{-11}).
\]

The \(A,\beta,\gamma\) calibration directions are therefore in the trial-state sensitivity span to numerical precision.

This has a direct dynamical explanation. Before the first event, the q=1 synaptic state evolves invertibly as

\[
q(t)=e^{-\alpha t}q_0,
\qquad
\psi(t)=e^{-\alpha t}(\psi_0+tq_0).
\]

At fixed pulse time, any small perturbation of the q=1 pulse reset can be cancelled by changing the unknown q=1 initial \((\psi_0,q_0)\). The two relative phase coordinates can simultaneously compensate the induced pre-pulse phase change. Post-pulse spike times therefore cannot separate pulse amplitude/direction calibration from the unknown preparation.

Hence

\[
\boxed{\text{pulse self-calibration from spike times alone is structurally impossible here}.}
\]

The pulse-time direction is slightly different: it leaves one very weak direction outside the preparation span. Treating both pulse times as completely free nuisance changes the profiled shared standard deviations to only

\[
\boxed{(2.636\times10^{-4},4.859\times10^{-4})}.
\]

The corresponding data-only calibration-time scales are enormous (about 183 and 1924 time units), so any finite external timing calibration dominates this residual ambiguity.

---

## External calibration information

v0.26 represents pulse calibration by independent reference uncertainties

\[
\sigma_{u}=(0.002,0.002,0.02,0.02)
\]

for \((t_p,A,\beta,\gamma)\) in each trial.

These calibration observations are added to the spike-time likelihood rather than pretending the pulse can calibrate itself.

With these reference uncertainties the full calibration-aware posterior Fisher problem has 22 unknowns but regains finite rank. The shared marginal uncertainties are

\[
\boxed{\operatorname{sd}(p)\approx1.5449\times10^{-4}},
\qquad
\boxed{\operatorname{sd}(\tau_3)\approx2.8155\times10^{-4}},
\]

indistinguishable from the trial-state-only profile at the displayed precision.

The calibration posterior standard deviations remain essentially equal to their input calibration uncertainties. Spike times therefore add almost no calibration information, exactly as predicted by the span calculation.

---

## Derivative audit

Each trial is physically rerecorded under centered perturbations of both its eight state/network coordinates and its four pulse coordinates. The fixed-chart JAX derivatives agree with physical finite differences at relative errors of order

\[
2\times10^{-9}\text{ to }6\times10^{-9}.
\]

All v0.26 truth and calibration perturbations remain on their respective regular event charts.

---

## Nonlinear recovery: shared parameters versus nuisance decomposition

A twelve-start noiseless audit of the 14-unknown state-jitter model shows two different notions of recovery:

- all 12/12 starts recover \((p,\tau_3)\) within \(10^{-5}\);
- only part of the starts recover the complete 14-dimensional nuisance vector;
- the largest observed full-state distance can be of order \(10^{-1}\) while the shared network errors remain microscopic.

With calibration coordinates and external calibration residuals the same phenomenon persists: all tested starts recover the shared parameters, even when some latent-state decompositions remain aliased.

This establishes the v0.26 interpretation:

> nuisance non-uniqueness does not imply scientific-parameter non-identifiability.

A 50-realisation spike-noise audit for the trial-specific-state model gives empirical shared standard deviations approximately

\[
(1.51\times10^{-4},2.75\times10^{-4}),
\]

within about 3% of the profiled Fisher prediction.

With noisy pulse-calibration readouts included, the shared empirical standard deviations remain on the same scale.

---

## CORE rule

v0.26 adds a new inference rule:

\[
\boxed{
\text{evaluate identifiability after profiling scientifically irrelevant nuisance directions.}
}
\]

The smallest singular value of the full augmented parameter vector is not the right diagnostic when some nuisance coordinates are structurally non-identifiable by construction.

For pulse-controlled trials, calibration and preparation must also be separated conceptually:

- trial preparation may be inferred as nuisance state;
- pulse calibration requires external information if its decomposition is scientifically needed;
- shared network parameters can remain identifiable even when both nuisance blocks are individually sloppy.

## Scope and next step

v0.26 still assumes labelled spikes, known topology, exactly two trials, independent Gaussian calibration readouts, and a known pulse-family form. It does not yet include missing spikes, unknown trial correspondence, or hierarchical population distributions for preparation variability.

The next CORE step should make the nuisance model explicitly hierarchical: infer a shared preparation distribution and shared network parameters from many trials with missing/noisy spike observations. That provides the correct bridge from the current controlled two-trial benchmark to realistic repeated-experiment data before unknown topology is attempted.
