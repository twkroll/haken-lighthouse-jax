# CORE research program

## Mission

CORE is the mathematical source of truth for the Haken Lighthouse JAX project. It separates the original Lighthouse model, its mathematical reconstruction, modern generalizations, and implementable reference models.

## Current status through v0.22

The program has progressed from exact event/Floquet theory and normal forms through adaptive delays, full packet-queue dynamics, JAX/sparse-graph implementations, and chart-aware inverse problems.

The current inference sequence is:

1. v0.18: local chart-aware recovery of `(p,tau3)` from labelled spike times;
2. v0.19: trust-region / multi-chart optimization across a firing-order boundary;
3. v0.20: gauge-fixed latent relative initial phase and sequential chart crossings;
4. v0.21: exhaustive optimal observation design over four firing cycles plus a controlled clock-offset nuisance parameter;
5. v0.22: a minimal latent initial synaptic `(psi,q)` contrast and the first clear spike-time information limit.

The v0.22 result changes the next priority. Once a latent synaptic contrast is admitted, the full twelve-spike Jacobian remains rank six but develops a near-null phase/synapse direction with `sigma_min≈9.14e-4`. Later spike times and overdetermination can suppress observed nonlinear aliases, but they barely improve that differential weak direction. Therefore simply extending the spike-only window is no longer the right next experiment.

## Immediate next target: CORE v0.23

Introduce an observation or intervention that is genuinely transverse to the spike-time near-null direction. Candidate controlled benchmarks include:

- one projected subthreshold `psi` measurement near the initial time;
- one projected `q` measurement;
- a small known input pulse followed by transient spike-time readout;
- combinations chosen by Fisher/E-optimal design under explicit measurement-noise models.

The acceptance criterion should be that the augmented observation model raises the weakest singular value of the six-dimensional v0.22 inverse problem by orders of magnitude while preserving chart-aware differentiation and physical event scheduling.

Only after that ambiguity is broken should CORE enlarge to the full two-dimensional q=1 synaptic contrast in both `psi0` and `q0`, missing/unlabelled spikes, or unknown topology.
