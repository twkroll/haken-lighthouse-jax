# CORE v0.24 — chart-safe active experiment design with spike times only

## 1. Scope

CORE v0.23 removed the severe v0.22 phase/synapse ambiguity with one idealized subthreshold readout. v0.24 removes that extra sensor again. The unknown vector remains

\[
\vartheta=(p,\tau_3,\eta_1,\eta_2,\xi_\psi,\xi_q),
\]

and all observations after the intervention are labelled spike times only.

The intervention is a known deterministic pulse in the same zero-mean \(q=1\) contrast

\[
v=(2,-1,-1)/\sqrt6.
\]

At a fixed pre-event time \(t_p\),

\[
\psi^+=\psi^-+A\cos\gamma\,v,
\qquad
q^+=q^-+A\sin\gamma\,v.
\]

The pulse is not inferred. It is an experimental-design variable.

## 2. Hybrid-safety-constrained design problem

The design criterion is the smallest singular value of the twelve-spike sensitivity matrix after the pulse,

\[
\max_{t_p,\gamma,A}\ \sigma_{\min}(J_{\rm pulse}),
\]

subject to

\[
0\le A\le0.1,
\qquad
m_{\rm chart}\ge0.05,
\]

and, for the v0.24 reference branch, preservation of the nominal event signature. The chart constraint is essential: active design is not allowed to buy information by approaching an event-order collision.

A coarse global search followed by local refinement gave the certified reference pulse

\[
\boxed{t_p=0.0577345297347342},
\]

\[
\boxed{A=0.1},
\]

\[
\boxed{\gamma=0.12924575498190716}.
\]

Thus

\[
\Delta\psi=0.0991659387569161\,v,
\qquad
\Delta q=0.0128886225198646\,v.
\]

The optimum is almost a pure projected-\(\psi\) kick with a small projected-\(q\) component.

## 3. Hybrid safety

The first post-pulse spike occurs at

\[
7.936807414604705,
\]

well after \(t_p\). The full event order through four observed cycles is unchanged relative to the unpulsed truth chart.

The minimum event margin is

\[
\boxed{m_{\min}=0.0500000033143},
\]

which saturates the imposed safety floor but remains strictly positive.

The design therefore uses the available hybrid-safety budget without crossing or touching an event-order surface.

## 4. Information gain from spike times alone

Without the pulse, v0.22 gave

\[
\sigma_{\min}(J_0)=9.137484\times10^{-4}.
\]

For the active pulse,

\[
\sigma(J_{\rm pulse})\approx
(10.47382,7.72507,2.71095,0.46039,0.24633,0.07269497).
\]

Hence

\[
\boxed{\sigma_{\min}(J_{\rm pulse})=0.0726949714},
\]

and

\[
\boxed{\sigma_{\min}(J_{\rm pulse})/\sigma_{\min}(J_0)=79.56}.
\]

The condition number falls from roughly \(1.19\times10^4\) to about \(144\).

This gain is obtained with spike times only; unlike v0.23, no direct synaptic-state readout is present in the data vector.

## 5. Six-spike active design

Exhaustive E-optimal selection among the twelve post-pulse spike times gives

\[
\boxed{S_6=(0,1,2,3,10,11)}.
\]

Its singular values are approximately

\[
(8.01087,5.03972,1.64250,0.39176,0.16964,0.06834601),
\]

so

\[
\boxed{\sigma_{\min}(J_{S_6})=0.0683460105}.
\]

Thus six carefully selected spike times retain nearly all the weakest-direction information of the twelve-spike active experiment.

At spike-time noise \(\sigma_t=10^{-4}\), the corresponding local Fisher standard deviations are approximately

\[
(1.933,2.472,7.813,3.934,12.326,4.181)\times10^{-4}.
\]

Compared with unpulsed v0.22, the latent-state uncertainties are reduced by tens to hundreds of times.

## 6. Weak-direction and nonlinear-alias rejection

The finite v0.22 weak-direction displacement of amplitude \(0.01\) remains on the same pulsed chart, with minimum margin about \(0.05017\). But the pulsed spike-time residual now satisfies

\[
\boxed{\|\Delta Y\|/\sigma_t\approx18.01}
\]

for \(\sigma_t=10^{-4}\), versus only about \(0.588\) without intervention.

Likewise, the exact same-chart nonlinear alias found in v0.22 remains on the same active chart but is separated from the pulsed truth by

\[
\boxed{\|\Delta Y_{\rm alias}\|/\sigma_t\approx13.99}.
\]

Therefore the pulse changes the observation map itself in a direction transverse to the old ambiguity.

## 7. Nonlinear recovery and noise audit

Using the six-spike design \(S_6\), a deterministic twelve-start noiseless audit returns the true six-dimensional vector in all cases:

\[
\boxed{12/12}.
\]

A thirty-realization nonlinear audit at \(\sigma_t=10^{-4}\) gives empirical/Fisher marginal-standard-deviation ratios approximately

\[
(1.108,1.077,1.154,1.144,1.104,1.129),
\]

so the active experiment restores a practically useful local statistical regime using spike times alone.

## 8. Interpretation

v0.23 established that the v0.22 failure was an observation-operator deficiency. v0.24 shows that a known intervention can rotate that deficient observation operator into an informative one:

\[
\boxed{\text{latent state}\ \xrightarrow{\text{known pulse}}\ \text{informative spike-time transient}.}
\]

The pulse does not directly measure \(\psi\) or \(q\). It makes their decomposition dynamically visible in future event times.

The important hybrid rule is

> Active experiment design must optimize information subject to an explicit event-chart margin. Information gained only by approaching a hybrid collision is not accepted as robust information.

## 9. Benchmark contract B400–B423

- **B400** six-dimensional v0.22 unknown block is unchanged.
- **B401** pulse acts in the unit zero-mean \(q=1\) contrast.
- **B402** pulse law is \((\Delta\psi,\Delta q)=A(\cos\gamma,\sin\gamma)v\).
- **B403** reference amplitude obeys \(A=0.1\).
- **B404** reference pulse time equals \(0.0577345297\) within tolerance.
- **B405** reference direction angle equals \(0.129245755\) within tolerance.
- **B406** no direct synaptic-state observation is used after the pulse.
- **B407** pulse precedes the first physical event.
- **B408** pulsed event signature equals nominal truth signature.
- **B409** minimum chart margin is at least \(0.05\) within numerical tolerance.
- **B410** fixed-chart JAX replay matches physical truth times.
- **B411** JAX six-parameter Jacobian matches centered finite differences.
- **B412** full pulsed \(\sigma_{\min}>0.0726\).
- **B413** information gain over spike-only v0.22 exceeds \(79\times\).
- **B414** pulsed condition number is below 150.
- **B415** E-optimal six-spike set is \((0,1,2,3,10,11)\).
- **B416** six-spike \(\sigma_{\min}>0.0682\).
- **B417** finite old weak direction is separated by more than \(17\sigma_t\).
- **B418** old nonlinear alias is separated by more than \(13\sigma_t\).
- **B419** both weak-direction and alias states remain on the same pulsed chart.
- **B420** twelve-start noiseless six-spike audit returns truth 12/12.
- **B421** thirty-realization \(\sigma_t=10^{-4}\) audit is Fisher-consistent within the stored tolerance band.
- **B422** active-design score is never certified without an explicit chart-margin check.
- **B423** event-order selection itself is not differentiated through; one-sided fixed-chart derivatives remain the inference primitive.

## 10. Next step

The immediate next CORE question is robustness of the active design to intervention uncertainty. A real pulse has timing, amplitude and spatial-direction calibration error. CORE v0.25 should therefore promote small pulse-calibration errors to nuisance parameters and ask whether the same experiment remains identifiable. Only after that should the full \(q=1\) synaptic latent subspace or missing spike labels be introduced.
