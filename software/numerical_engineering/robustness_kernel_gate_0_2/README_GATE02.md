# NUM-ENG Gate 0.2 — versioned engineering overlay

Classification: DEVELOPMENT EVIDENCE / LOCAL ENGINEERING METRICS ONLY.
Authority: RB-019 `NUMENG_PULSE_AWARE_REFERENCE_V1` (physical authority unchanged).
Governance: frozen Gate-0.2 matrix `research/numerical_engineering/gate_0_2_frozen_stress_matrix.md`. Subsequent discovered batch-guard defect is in a *separate* `gate_0_2_batch_guard_diagnostic_addendum.md`; it is not retroactively added to the preregistered stress matrix.

## Reconstruct without changing RB-019

1. Copy the frozen baseline from `software/numerical_engineering/reference_repair_v0_1/` into a disposable working directory `WORK`.
2. Overlay **only** `overrides/lighthouse_dev/sparse_replay.py` onto `WORK/lighthouse_dev/sparse_replay.py`.
3. From `WORK` set `PYTHONPATH=WORK:<path-to-this-dir>/harness`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`, `JAX_PLATFORMS=cpu`, `JAX_ENABLE_X64=1`, `XLA_PYTHON_CLIENT_PREALLOCATE=false`.
4. Run baseline + new QA: `python -m pytest -q tests/ <path-to-this-dir>/tests/test_gate02.py <path-to-this-dir>/tests/test_gate02_batch_guard.py`.
5. Run deterministic metrics: `python <path-to-this-dir>/harness/stress_gate02.py` and `python <path-to-this-dir>/harness/grad_gate02.py`. The original captured run writes full JSON to `/mnt/data/numeng_gate02`; that location is an engineering output path, not a universal runtime requirement. Reconfigure it explicitly when running elsewhere, preserving baseline fixtures and tolerances.

The local captured environment is Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, JAX/JAXLIB 0.9.0.1, pytest 9.0.2, CPU x64, virtualized AMD EPYC 9V74, with thread controls above.

## Exact verified Git blob identities

- frozen RB-019 `lighthouse_dev/sparse_replay.py` blob: `f41c5529e924c15ac35d61a839ed1dd05e4a62a1`.
- Gate-0.2 overlay `sparse_replay.py` blob: `5606c09aed4dc18202af199f3323062562606d8d`.
- fixed predeclared 48-case test module blob: `338c2dda1a1d1f0fb6b7fe20db2d9d8e50d2ff3b`.
- diagnostic-addendum 8-case batch test module blob: `6413deb0221196626dff32176010dacfbfa113e2`.
- stress harness blob: `6fd9bd679e6a0a42f3d9ce06adf7d641390e3e6f`.
- gradient/JAX harness blob: `c2fcd11244035a2f416f8da8c26f2d621a12d53b`.

## Raw local reproduction package (attached in the NUM-ENG chat)

Archive: `NUMENG_Gate_0_2_Engineering_Bundle.zip`
SHA-256: `762b4467dc30dbaba5ebf24dd662d66f8c87e8d12c4bb086d73d710891292fc6`.
CRC/integrity PASS, 20 archived members. Its complete SHA256 manifest has SHA-256 `9062c26caa93853de43001de6d5e51c4bb1a6ba0f48a2ed0ede79755664a9e15`.
Contains exact harness sources, CPU/environment snapshot, independently generated JSON metrics, targeted and aggregate raw pytest logs. Full raw results are not scientific observations.

## Boundaries

The optional historical accelerated first-hit schedulers still emit `UNVERIFIED` records; no accelerator receives physical certification merely by matching a finite suite. The high-level JAX guard is fail-closed only within finite RB-019 QA; `replay_sparse_fixed_chart` is an unguarded mathematical primitive by design. No formal interval arithmetic, universal scaling law, protected confirmatory RNG, TR-27C science, APP-3 training, main executable-source merge, novelty or manuscript claim is made.
