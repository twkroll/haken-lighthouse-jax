# CORE Mathematical Freeze 0.1

Date: 2026-09-07
Status: FROZEN / STABLE
Rollback point: RB-004

## Authority

MASTER authorizes this freeze after PASS of `research/core/mathematical_scope_canonicalization_gate_0_1.md`.

Frozen source artifact:

- file: `research/core/mathematical_scope_canonicalization_gate_0_1.md`
- blob SHA: `d34ba1129dfca892e76342f3c2d66b6b493535dd`
- creation commit: `8d2fcb3f1cb020e4e6b3388ad05987f8c6bf3be2`

The source artifact remains the detailed mathematical specification. This freeze records exactly which portions are now canonical scientific baseline material.

## Frozen contents

The following contents of the source artifact are frozen:

1. source map S1–S6, with S6 registry-only;
2. canonical baseline equations (C1)–(C11);
3. lifted-phase first-hitting event convention with no reset below threshold;
4. normalized alpha kernel and the proved `(a,q)` state-space equivalence;
5. fixed edge-delay semantics;
6. assumptions A1–A13;
7. formal variant registry V-R0 through V-P1;
8. independently re-derived elementary identities (D1)–(D18), with the epistemic labels stated in the source artifact;
9. analytical validation targets in Section 10;
10. explicit exclusions in Section 11.

## Freeze boundary

This freeze is limited to baseline definitions, source/provenance distinctions, assumptions, variant registration, and elementary analytical C1 derivations.

It does **not** freeze or validate:

- any legacy v0.3–v0.26 numerical result;
- continuation, Floquet-spectrum, bifurcation, normal-form or invariant-object values;
- JAX or other implementation claims;
- benchmark outputs;
- inverse/inference performance;
- observation or active experiment design;
- v0.24 pulse effects;
- v0.25 two-probe effects;
- v0.26 nuisance/calibration numerical results;
- v0.27 or hierarchical repeated-trial work;
- application or novelty claims.

`core/theory-v0.1` remains read-only legacy recovery evidence and is not merged by this freeze.

## Change control

Any change to the frozen mathematical baseline requires a new MASTER-authorized gate and a new versioned freeze. Later work may extend this freeze but must not silently rewrite it.

## STOP

`CORE Mathematical Freeze 0.1` is established.

STOP — FROZEN