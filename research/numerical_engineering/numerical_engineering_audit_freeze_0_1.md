# NUM-ENG Numerical Engineering Audit Freeze 0.1

Date: 2026-10-15
Status: FROZEN / STABLE ENGINEERING AUDIT — CONDITIONAL / BLOCKED
Rollback point: RB-018

## Authority

MASTER reviews the returned `NUM-ENG Numerical Engineering Gate 0.1` on development branch `engineering/numerics-v0.1`.

Frozen source artifact:

- branch: `engineering/numerics-v0.1`
- file: `research/numerical_engineering/numerical_engineering_gate_0_1.md`
- blob SHA: `2d1c9c5842eed69135114dc1810634cae80dc4f7`
- returned STATUS blob SHA: `e28c51be2d6a51bfd050279964d8e27c73ce8726`
- branch divergence at review: 2 commits ahead of `main`, 0 behind; only the gate report and NUM-ENG STATUS differ from the MASTER authorization base.

RB-017 remains the exact frozen intake identity.

## Frozen audit result

`CONDITIONAL / BLOCKED — NOT PASS`

This is an engineering audit classification, not a scientific result.

## Reproduction findings

The audit independently reproduced the full supplied deterministic suite:

- 11/11 pytest modules;
- 180/180 test cases;
- clean exit code 0 for every module;
- one aggregate single-process run: 180/180 PASS, clean exit.

The earlier aggregate teardown/hang was not reproduced under the captured CPU/plugin-isolated environment. No unconditional portability claim is frozen.

## Provenance findings

The original RB-017 archive is unchanged.

The obsolete 33-line manifest is preserved as defective provenance input. The audit generated a complete 137-file original-byte manifest:

`RB017_ORIGINAL_COMPLETE_SHA256.tsv`

with reported SHA-256:

`52b429d3c4784341b8615228896756295ad8a901317256d385d82b9e3c54268a`.

No scientific or performance claim is promoted by this manifest repair.

## Decisive reference defect

The audit found a deterministic first-hit counterexample in the original physical sparse/reference path.

Fixture:

- one cell;
- `alpha=1000`;
- `r=1`;
- `h=0.1`;
- weight `4`;
- delay `1.5`;
- historical emission at `-1` giving arrival `t=0.5`;
- initial phase `2*pi-0.005`;
- horizon `20`.

Returned behavior:

- `physical_rerecord_sparse`: arrival at 0.5, 0 spikes, `chart_valid=True`;
- pulse-aware `physical_rerecord_gauss` and `physical_rerecord_quiet`: exactly one first hit at approximately `0.5050005053634209`;
- independently segmented SciPy quadrature/root reference agrees to approximately `1.11e-16`;
- `derivative_record_sparse` accepts the incomplete event tape and returns an empty spike vector.

Frozen classification:

`REFERENCE / RERECORD FAIL-CLOSED DEFECT — REPAIR REQUIRED`.

This does not alter RB-004 mathematics. It shows that the current local numerical reference implementation is not yet a safe authority for all first-hit charts.

## Component classification

ENGINEERING-APPROVED, scoped only to audited functions:

- exact intake/source identity;
- complete regenerated original-byte manifest;
- reproduced test/fixture infrastructure;
- tested zero-weight structural-coordinate representation;
- deterministic environment/log protocol.

REPAIR-REQUIRED:

- stale/incomplete original manifest as checksum authority;
- unsegmented first-hit quadrature in affected physical reference/sparse paths;
- chart/JAX guards that trust an incomplete physical tape without an independent first-hit completeness guarantee.

DEFERRED:

- pulse-aware alternative integrators as production-authoritative default until repair QA closes;
- performance/scaling generalization;
- JAX fixed-chart claims outside validated regular charts;
- learning/optimizer smoke tests as scientific AI evidence.

REJECTED:

- treating the original 33-line manifest as complete/accurate;
- promoting local timing, speedup, learning, or optimization smoke outputs to confirmatory evidence.

## Integration boundary

No executable source is promoted to a canonical engineering baseline by RB-018.

No source is merged to `main`.

All software, runtime, scaling, gradient, and learning outputs remain DEVELOPMENT EVIDENCE.

## Scientific boundaries

- RB-015 remains immutable SCIENTIFIC FAIL.
- `2711xxx` confirmatory seeds remain forbidden to NUM-ENG.
- No v0.27c confirmatory execution is authorized.
- APP-3 remains non-executable.
- No novelty or manuscript claim is authorized.

## Required next engineering action

A separate MASTER-authorized repair gate must:

1. freeze a pulse-aware physical first-hit reference contract before repair validation;
2. repair affected physical reference/sparse rerecording paths;
3. make chart/JAX guards fail closed on incomplete tapes;
4. add the frozen narrow-pulse regression and relevant negative controls;
5. rerun all original 180 tests plus the new repair suite;
6. produce a complete repaired-source manifest;
7. integrate only reviewed ENGINEERING-APPROVED source on `engineering/numerics-v0.1`.

## STOP

RB-018 is an audit freeze only.

STOP — FROZEN / ENGINEERING REPAIR REQUIRED
