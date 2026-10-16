# NUM-ENG Gate 0.6 — exact-dyadic MPFR RIFC repair

**Engineering-only repair, not a scientific result.** Gate chronology: prospectively frozen MASTER contract (commit `779c8f05256406c5684d4dec35ae123a418027fb`), then new source and deterministic tests. RB-025 stays byte-identical.

Source: `source/rifc_mpfr_v0_2.py` (GMP exact MPFR dyadic extraction, finite fail-closed resource limits). The RB-025 original `rifc_mpfr_v0_1.py` is not copied or modified by this versioned subtree; it remains under `../rifc_interval_gate_0_4/source/`.

On captured environment GNU MPFR 4.2.2, GNU GMP 6.3.0, Python 3.13.5, pytest 9.0.2, mpmath and standard Linux x86_64 C ABI:

```sh
PYTHONPATH=source PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 JAX_PLATFORMS=cpu python -m pytest -q tests/test_gate06_exact_dyadic.py tests/test_rifc_gate04_repaired.py
python scripts/produce_gate06_artifacts.py certificates
```

Baseline unchanged 26-case suite and 28 physical/JAX regression tests were additionally run in isolation; see logs. To reproduce baseline directly use the corresponding old subtree's tests under the same environment. No protected RNG.

Expected scope: serialization repair validated, finite positive certs remain sound. IR-A4-R/eventual-certification is **NOT ESTABLISHED**, Q6/Q7 were **NOT EXECUTED** because analytical Q4 was not established. See `EXACT_DYADIC_AND_IR_A4R_PROOF_0_6.md` and Gate-0.6 report for explicit reasons. The mathematically unbounded p_n schedule is NOT executable indefinitely with the current p<=8192 and nmax<=16 resource guards.

Finite self-check: compare test suite and SHA256_MANIFEST.json against source. Certificate JSONs are exact rational proof objects and must pass `audit_certificate` independently; no physical simulator is needed for their replay. The large `SER_tiny_nohit` example checks lossless long integer/decimal proof serialization rather than global physical simulator behavior.
