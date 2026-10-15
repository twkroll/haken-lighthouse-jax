# Lighthouse Numerical Engineering — repaired reference source v0.1

**Development evidence only**, not a governed scientific result.

This is a controlled, source-only engineering integration on `engineering/numerics-v0.1`.
Baseline mathematics are RB-004; exact source intake RB-017, SHA-256 e21202362fc9ead75a3e5d92736d38002eb75d4e4ec5b4dd1cfb3c0a7c88db53. RB-018 records the original narrow pulse defect. No originals or scientific freezings have been edited.

Local root: `software/numerical_engineering/reference_repair_v0_1/`.

From this root: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 JAX_PLATFORMS=cpu XLA_PYTHON_CLIENT_PREALLOCATE=false python -m pytest -q tests`.

Main physical authorities are `lighthouse_dev/reference.py`, `lighthouse_dev/sparse.py` and `lighthouse_dev/physical_first_hit_repair.py`. Only records with `physical_certification=NUMENG_PULSE_AWARE_REFERENCE_V1` and `chart_valid=True` are accepted by the high-level sparse/dense derivative wrappers. Direct fixed-chart replay remains a conditional mathematical primitive, **not** independently certified.

The legacy alternate first-hit schedulers and v0.9/v0.10 acceleration experiments remain **DEFERRED / DEVELOPMENT ONLY**, though retained for reproducing original fixtures. The legacy Gauss integration public function is an alias to the corrected common physical integrator: prior local speedup numbers cannot be transplanted to this branch.

This finite audit is not a global rigorous enclosure for quadrature or a proof of completeness at all parameter values. QUADPACK estimates are engineering error controls; physical indeterminacy must fail closed. Future scientific use needs separately frozen contracts. Do not merge to main without MASTER review.
