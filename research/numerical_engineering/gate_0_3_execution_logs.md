# NUM-ENG Gate 0.3 — process log and provenance

Date: 2026-10-16
Authority: contract commit `7a488ed6777d206313c512f437216b05b8e5eb6e`; RB-019/RB-021 unchanged source; RB-022 theory.

## Environment

Python 3.13.5; NumPy 2.3.5; SciPy 1.17.0; JAX/JAXLIB 0.9.0.1; pytest 9.0.2; CPU platform, float64.
Execution isolation: `JAX_ENABLE_X64=1 JAX_PLATFORMS=cpu PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 XLA_PYTHON_CLIENT_PREALLOCATE=false`.

Source Git blob identity validated:
- `lighthouse_dev/physical_first_hit_repair.py`: `0a6023b09e8b5b2b54cdcc5165e74804c03b301a`
- `lighthouse_dev/sparse.py`: `0bfc454bf9e9fa7087937f70fed7002fcc71def7`
- `lighthouse_dev/reference.py`: `155304ca5039df6798074adfdf928cfd39aea981`
- RB-021 `lighthouse_dev/sparse_replay.py`: `5606c09aed4dc18202af199f3323062562606d8d`

## First Gate-0.3 execution (split)

```text
TV-01 PASS 0.001
TV-02 PASS 0.002
TV-03 PASS 0.042
TV-04 PASS 0.243
TV-05 PASS 0.025
TV-06 PASS 0.001
EXIT_CODE=0

TV-07 PASS 2.767
TV-08 PASS 6.618
TV-09 PASS 3.412
TV-10 PASS 0.003
TV-11 PASS 0.956
EXIT_CODE=0
```

## Independent repeat in one process

```text
TV-01 PASS 0.001
TV-02 PASS 0.001
TV-03 PASS 0.039
TV-04 PASS 0.302
TV-05 PASS 0.026
TV-06 PASS 0.001
TV-07 PASS 2.94
TV-08 PASS 6.706
TV-09 PASS 3.325
TV-10 PASS 0.003
TV-11 PASS 0.941
EXIT_CODE=0
```

## Targeted prior-source compatibility

```text
$ python -m pytest -q tests/test_reference.py tests/test_rri_repair_v01.py tests/test_gate02_batch_guard.py
............................                                             [100%]
28 passed in 20.20s
EXIT_CODE=0
```

An optional wider 250-case test process timed out under the execution-environment limit. Its raw log contains only progress dots and **NO** authoritative completion summary or exit status. It is neither counted as a reproducibility PASS nor classified as a software test FAIL. Existing RB-021 250/250 frozen QA is not modified or misrepresented.

## Raw/reproduction archive

`NUMENG_Theory_First_Hit_Gate_0_3.zip`
SHA-256: `20e66a8a2b7ef30f0a94facfd94178acef2c4a0ee2b2d464251b188ae99df57f`
ZIP CRC: PASS. 50 entries (including source, executable Gate-0.3 harness, full TV_RESULTS.json, environment metadata, full raw logs, contract, report, old/new software tests and a complete SHA256 manifest).

Archive produced as a conversation artifact for MASTER review; it is not, merely by reference here, an executable source merge on main. The project/Git canonical audit trail consists of the prospectively frozen contract, final gate report, machine-readable result summary, and this log. Detailed reproducer is retained in the archive.

All findings remain ENGINEERING VALIDATION / DEVELOPMENT EVIDENCE; no scientific PASS or universal first-hit guarantee.

STOP — RETURN TO MASTER.
