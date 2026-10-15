# CORE v0.25 — full real q=1 synaptic state from two chart-safe pulse experiments

## Scope

CORE v0.24 showed that one known pre-event pulse can recover practical spike-time observability for one real q=1 direction in each initial synaptic state. v0.25 enlarges the latent state to the full real two-dimensional q=1 subspace.

Let

\[
v_1=\frac1{\sqrt6}(2,-1,-1),\qquad
v_2=\frac1{\sqrt2}(0,1,-1).
\]

The unknown vector is now

\[
\boxed{
\Theta=(p,\tau_3,\eta_1,\eta_2,
\xi_{\psi,1},\xi_{\psi,2},
\xi_{q,1},\xi_{q,2})
}
\]

with

\[
\psi_0=\psi_{0,*}+\xi_{\psi,1}v_1+\xi_{\psi,2}v_2,
\]

\[
q_0=q_{0,*}+\xi_{q,1}v_1+\xi_{q,2}v_2.
\]

The two controlled experiments are assumed to start from the same reproducibly prepared but unknown initial state \(\Theta\). If every trial has an independent latent initial state, the present stacked-identifiability result does not apply.

No direct synaptic-state observation is used. Each experiment records labelled spike times only.

## Pulse family and safety

The pulse family is inherited unchanged from v0.24:

\[
d(\gamma)=\cos\gamma\,v_1+\sin\gamma\,v_2,
\]

\[
\psi^+=\psi^-+A\cos\beta\,d(\gamma),
\qquad
q^+=q^-+A\sin\beta\,d(\gamma).
\]

Both experiments obey

\[
A\le0.1,\qquad t_p\ge0.05,
\qquad m_{\rm chart}\ge0.06.
\]

Experiment 1 is exactly the v0.24 reference pulse:

\[
\boxed{P_1=(t_p,A,\beta,\gamma)=(0.05,0.1,0.55,-0.1).}
\]

Its physical truth-chart margin is

\[
\boxed{m_1\approx0.06285674669.}
\]

## Why one experiment is not enough in practice

For the eight-dimensional unknown block, the single-P1 spike-time Jacobian is formally rank eight. Its singular values are approximately

\[
(13.75538,10.29232,2.71230,0.538068,0.277929,0.137705,0.0757493,1.86287\times10^{-4}).
\]

Thus

\[
\boxed{\sigma_{\min}(J_1)\approx1.86287\times10^{-4}},
\]

with condition number about

\[
\boxed{7.38\times10^4}.
\]

The unforced eight-parameter experiment is even worse,

\[
\sigma_{\min}(J_0)\approx3.24415\times10^{-5},
\qquad
\kappa_2(J_0)\approx3.97\times10^5.
\]

Repeating the *same* P1 experiment twice only multiplies all singular values by \(\sqrt2\):

\[
\boxed{\sigma_{\min}(J_1\oplus J_1)\approx2.63450\times10^{-4}.}
\]

Therefore more trials are not enough if they reproduce the same sensitivity geometry.

## Second active experiment

A constrained search keeps P1 fixed and designs a second chart-safe pulse. A refined boundary solution near

\[
(t_p,A,\beta,\gamma)
=(0.05,0.1,0.20,3.03310684454)
\]

reaches

\[
\sigma_{\min}(J_1\oplus J_2)\approx0.14696444
\]

at the hard second-experiment margin \(m_2=0.06\).

For reproducibility v0.25 stores the rounded interior pulse

\[
\boxed{P_2=(0.05,0.1,0.20,3.02).}
\]

Its spatial direction is

\[
d_2\approx(-0.8104681554,0.4910013608,0.3194667945),
\]

with state kick

\[
\Delta\psi_2\approx(-0.07943127515,0.04812140234,0.03130987281),
\]

\[
\Delta q_2\approx(-0.01610151661,0.00975469118,0.00634682543).
\]

The physical margin is

\[
\boxed{m_2\approx0.06334074092>0.06.}
\]

The rounded design loses only about

\[
\boxed{7.30\times10^{-4}}
\]

relatively in the stacked E-optimal objective versus the refined boundary point.

The combined reset vectors of P1 and P2 form an angle of approximately

\[
\boxed{159.91^\circ}.
\]

Thus the useful pair is not an orthogonal spatial probe pair. It is closer to a two-sided nonlinear operating-point probe: two nearly opposing state-space deformations produce different spike-time sensitivity geometries.

## Two-experiment identifiability

Stack the two twelve-spike Jacobians:

\[
J_{12}=\begin{pmatrix}J_1\\J_2\end{pmatrix}\in\mathbb R^{24\times8}.
\]

For the rounded reference pair,

\[
\boxed{
\sigma(J_{12})\approx
(18.40506,15.35792,3.847894,0.726733,0.416403,0.243863,0.197115,0.146857).
}
\]

Hence

\[
\boxed{\sigma_{\min}(J_{12})=0.14685712345},
\]

\[
\boxed{\kappa_2(J_{12})\approx125.3263.}
\]

Relative to one P1 experiment,

\[
\boxed{
\frac{\sigma_{\min}(J_{12})}{\sigma_{\min}(J_1)}\approx788.34.
}
\]

Relative to simply repeating P1 twice, the gain is still

\[
\boxed{\approx557.44.}
\]

An unforced trial plus P1 gives only

\[
\sigma_{\min}(J_0\oplus J_1)\approx0.0874104,
\]

so two actively differentiated operating points are substantially more informative.

This establishes the v0.25 rule:

> Replicate trials to reduce noise; diversify trials to change identifiability geometry.

## Derivative audit

For each experiment, the physical hybrid scheduler is rerun at central finite-difference parameter perturbations. The fixed-chart JAX Jacobians agree with these physically rerecorded finite differences at relative errors

\[
\boxed{2.55\times10^{-9}\quad(P_1)},
\]

\[
\boxed{2.23\times10^{-9}\quad(P_2)}.
\]

Both truth charts remain above the v0.24 hard margin threshold.

## Minimal eight-spike design

Because there are eight unknowns, eight scalar spike times are the smallest possible square local design. Exhaustive search over all \(\binom{24}{8}\) subsets gives the E-optimal set

\[
\boxed{(1,5,6,7,12,16,21,23)}
\]

in global stacked indexing. Equivalently:

- P1 indices \((1,5,6,7)\),
- P2 indices \((0,4,9,11)\).

Its singular values are approximately

\[
(10.78787,8.63566,2.23217,0.259952,0.187223,0.133469,0.0994662,0.0936843),
\]

so

\[
\boxed{\sigma_{\min}=0.09368428829.}
\]

The exact global eight-row optimum is therefore balanced four-plus-four across the two experimental conditions.

At spike-time noise \(\sigma_t=10^{-4}\), the full 24-spike Fisher marginal standard deviations are approximately

\[
(1.270,1.792,2.260,3.895,4.509,6.152,2.133,2.971)\times10^{-4},
\]

and the minimal eight-spike design gives approximately

\[
(2.889,4.373,4.848,8.485,7.029,8.924,4.014,6.825)\times10^{-4}.
\]

## Nonlinear uniqueness

A deterministic twelve-start audit uses common unknown initial-state coefficients across the two trials and solves the complete nonlinear fixed-chart inverse problem.

Both

- all 24 spike times, and
- the exact E-optimal eight-spike design

return the true eight-dimensional state/parameter vector in 12/12 starts. Maximum final distances from truth are below \(10^{-12}\).

A direct 50-realisation audit at \(\sigma_t=10^{-4}\) remains on the Fisher scale. For all 24 spikes, empirical/Fisher marginal-standard-deviation ratios lie approximately in \([0.95,1.11]\); for the eight-spike design they lie approximately in \([0.93,1.20]\).

Thus the improved local conditioning translates into stable nonlinear recovery at the reference noise level.

## Interpretation

The full real q=1 latent synaptic subspace is not practically observable from one operating-point experiment even though the corresponding Jacobian is formally full rank. A second known pulse changes the nonlinear operating point enough to rotate the very weak sensitivity direction and remove the near-null intersection.

The important distinction is

\[
\boxed{
\text{rank} \neq \text{practical identifiability},
\qquad
\text{replication} \neq \text{experimental diversity}.
}
\]

Two chart-safe experiments provide the diversity needed here without direct synaptic-state sensing.

## Benchmark contract B426--B451

B426. The latent initial synaptic state spans both real zero-mean q=1 basis vectors in \(\psi_0\) and \(q_0\).

B427. The two experiments share one reproducibly prepared unknown eight-dimensional initial state.

B428. Both probes use the v0.24 pulse family with \(A\le0.1\), \(t_p\ge0.05\), and hard chart margin \(\ge0.06\).

B429. P1 equals the v0.24 reference pulse.

B430. Rounded P2 equals `(0.05,0.1,0.20,3.02)`.

B431. Each physical truth chart contains 30 events through four firing cycles.

B432. P1 and P2 truth margins exceed 0.06.

B433. Each JAX Jacobian agrees with physically rerecorded central finite differences below relative error \(10^{-8}\).

B434. One P1 experiment is rank eight but has \(\sigma_{\min}<2\times10^{-4}\).

B435. The unforced eight-parameter experiment has \(\sigma_{\min}<4\times10^{-5}\).

B436. Repeating P1 twice leaves \(\sigma_{\min}<3\times10^{-4}\).

B437. The rounded P1+P2 stack has \(\sigma_{\min}>0.146\).

B438. The rounded P1+P2 stack has condition number below 126.

B439. P1+P2 improves \(\sigma_{\min}\) by more than 780x relative to P1 alone.

B440. P1+P2 improves \(\sigma_{\min}\) by more than 550x relative to duplicate P1 trials.

B441. Refined P2 at the 0.06 safety boundary reaches \(\sigma_{\min}\approx0.14696444\); rounded P2 loses less than 0.1% objective.

B442. The two normalized state-space pulse vectors have stored inner product/angle consistent with about 159.91 degrees.

B443. Exhaustive global eight-row E-optimal design is `(1,5,6,7,12,16,21,23)`.

B444. Its \(\sigma_{\min}\) exceeds 0.0936.

B445. Stored full24 and E-opt8 Fisher marginal standard deviations reproduce from the stacked Jacobians.

B446. Twelve-start full24 nonlinear recovery returns truth 12/12.

B447. Twelve-start E-opt8 nonlinear recovery returns truth 12/12.

B448. Fifty-realisation full24 noise audit remains within the stored Fisher-ratio interval.

B449. Fifty-realisation E-opt8 noise audit remains within the stored Fisher-ratio interval.

B450. Unforced+P1 stacked information is lower than P1+P2 stacked information.

B451. No direct \(\psi/q\) observation is used in either trial.

## Scope and next step

v0.25 assumes the same latent initial state can be reproducibly prepared across trials, pulse parameters are known exactly, spike identities are labelled, and topology is known. It does not yet allow trial-to-trial latent-state jitter or actuator uncertainty.

The next scientifically necessary step is therefore not unknown topology. CORE v0.26 should add **trial-to-trial preparation variability and pulse calibration uncertainty** and ask which combinations of shared network parameters and trial-specific latent state remain identifiable. Only after that robustness test should missing labels or topology recovery enter the CORE program.
