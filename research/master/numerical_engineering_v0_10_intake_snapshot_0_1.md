# Numerical Engineering v0.10 Intake Snapshot 0.1

Date: 2026-10-15
Status: STABLE ADMINISTRATIVE / DEVELOPMENT EVIDENCE INPUT
Rollback point: RB-017

## Purpose

Freeze the exact locally supplied Numerik v0.10 package as controlled input for a governed engineering audit. This snapshot does **not** validate or promote its software, numerical, learning, benchmark, or performance claims.

## Frozen intake identity

Uploaded package:

`Lighthouse_Numerik_Starter_v0_10(1).zip`

SHA-256:

`e21202362fc9ead75a3e5d92736d38002eb75d4e4ec5b4dd1cfb3c0a7c88db53`

Archive inventory at MASTER intake:

- 137 regular archived files;
- 47 Python files;
- 11 pytest test modules;
- ZIP CRC/integrity check: PASS.

The package self-identifies as local/noncanonical engineering development and records canonical Git HEAD `5c02ccd18911490abbaffcc9663af2ce531f097a`.

## Development claims retained as unpromoted input

The package reports:

- Python/JAX reference and replay simulators;
- differentiable spike-time paths on regular event charts;
- structural/chart guards and physical rerecording;
- sparse edge-state machinery;
- accelerated first-hitting variants;
- local scaling/profiling work;
- 180 tests reported PASS when modules are run separately;
- one deterministic one-weight learning/optimizer smoke test.

Every such claim remains **DEVELOPMENT EVIDENCE** pending NUM-ENG audit. The learning smoke test is not APP-3 performance evidence.

## MASTER intake checks

Environment available during this MASTER audit matches the package's recorded versions:

- Python 3.13.5
- NumPy 2.3.5
- SciPy 1.17.0
- JAX/JAXLIB 0.9.0.1
- pytest 9.0.2
- Matplotlib 3.10.8

Protected-seed text scan found no use of `2701xxx` or `2711xxx` in the supplied source/tests.

Independent split-module reproduction completed in this MASTER audit for:

- `tests/test_reference.py`: 6 PASS, exit 0;
- `tests/test_z_history_multineuron.py`: 9 PASS, exit 0;
- `tests/test_structural_graph_v03.py`: 8 PASS, exit 0;
- `tests/test_sparse_v04.py`: 14 PASS, exit 0.

Thus 37 cases were independently reproduced with clean process exit here. The remaining modules were **not** certified by this MASTER audit because the current runner/transport path timed out before a trustworthy module-exit record could be obtained. This is not classified as a test failure; complete clean-suite reproduction remains a mandatory NUM-ENG gate task.

## Packaging/provenance defect

The archive's current `FILE_SHA256_MANIFEST.txt` contains 33 entries. During intake verification:

- 31 entries matched;
- 2 entries did not match the archived bytes:
  - `README.md`
  - `lighthouse_dev/sparse_replay.py`.

The archive itself passes ZIP integrity checking. The manifest mismatch/incompleteness is therefore classified as a **packaging/provenance repair requirement**, not a scientific failure.

NUM-ENG must create a complete immutable manifest for the exact audited intake before any software integration claim can PASS.

## Scientific boundaries

This snapshot does not:

- change RB-004 through RB-016;
- rescue or relabel RB-015;
- authorize `2711xxx` RNG creation;
- validate a scientific speedup, gradient, scalability, learning, or AI-performance claim;
- authorize APP-3 execution.

## STOP

RB-017 freezes only the intake identity and MASTER audit observations above.

STOP — STABLE ADMINISTRATIVE / DEVELOPMENT INPUT
