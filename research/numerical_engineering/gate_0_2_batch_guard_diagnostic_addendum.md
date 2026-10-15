# Gate 0.2 — exploratory batch guard defect and prospective software repair QA addendum

Date: 2026-10-15
Classification: ADDITIONAL DEVELOPMENT DIAGNOSTIC, NOT A POST-HOC CHANGE TO THE FROZEN F01–F18 / G01 / S01–S04 STRESS MATRIX.
Scope: Authorized "harden sparse/JAX kernels" work under NUM-ENG Gate 0.2; no scientific experiment.

## Observed defect (recorded before the following software repair)

Input: predeclared G01 deterministic ordinary 2-neuron fixture; physically certified and regular event tape with 13 events and 5 spikes. Mutate *only* each `SparseEvent.t` of its base record by +0.02 using `dataclasses.replace`. The `token` remains unchanged because it captures event signatures, not times. Call `guarded_batch_replay(p,stale_record,np.stack([p.weight]))`.

Observed before repair: silently returns finite five spike times instead of raising an invalid/stale-chart error. The high-level single-parameter `derivative_record_sparse` already checks baseline tape times correctly, but batch replay does not.

## Frozen before executing the repair-validation cases

1. Introduce a shared high-level physical authority check for `SparseRecord` on input `p`; require baseline `physical_rerecord_sparse` with record history/horizon/initial theta.
2. Require both baseline and supplied tape chart-valid, `physical_certification == NUMENG_PULSE_AWARE_REFERENCE_V1`, topology and signatures/token match, event counts match, maximum absolute event time difference <=1e-8, spike/event consistency, and finite consistent initial alpha states.
3. High-level derivative and batch routes must BOTH use the shared authority check before any JAX replay; direct `replay_sparse_fixed_chart` remains explicitly unguarded.
4. Negative controls: shifted base times +0.02; truncated events; falsely labelled certification; modified spike list inconsistent with events; modified initial alpha state.
5. Positive controls: unmodified certified G01 baseline; same-chart batch with one unmodified and one tiny weight perturbation (+1e-5 in structural zero coordinate), each freshly rerecorded. JAX/physical agreement must satisfy inherited 1e-7 absolute spike-time tolerance.
6. Re-run frozen Gate 0.2 48-test suite twice, original 194-case baseline suite and new negative/positive controls. Do not adjust numerical tolerances based on measured outcomes.
7. If any high-level path still accepts stale tapes, classify REPAIR-REQUIRED and return BLOCKED.

This is an additional defect-driven ENGINEERING repair regression, not preregistered scientific evidence, and it does not redefine, rescue, or replace the originally frozen stress matrix.

## STOP

All outputs DEVELOPMENT EVIDENCE. No scientific promotion, protected RNG, TR-27C, APP-3 or main merge.
