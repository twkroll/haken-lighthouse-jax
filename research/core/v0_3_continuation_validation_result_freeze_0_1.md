# CORE v0.3 Continuation Validation Result Freeze 0.1

Date: 2026-09-07
Status: FROZEN / STABLE RESULT
Rollback point: RB-009

## Authority

MASTER accepts the corrected governed execution record from `CORE v0.3 Continuation Validation Execution Gate 0.1`.

Frozen source artifact:

- file: `research/core/v0_3_continuation_validation_execution_gate_0_1.md`
- corrected blob SHA: `94437be2844304a512eacf67479397d6b7cda2a0`
- initial execution-result commit: `872199d6f885489898d64ac8bf957c629770d249`
- initial RETURN-TO-MASTER commit: `02da2d7c68e0a631c9cb42941860e25450c5f127`
- corrected-result commit: `f94049ef4037a0687384dafb01a042219592b53d`
- corrected RETURN-TO-MASTER commit: `7b0c1c3d13aac7cb6c8bad793327599493d00a4b`

Execution contract:

- RB-008 `CORE v0.3 Continuation Validation Contract Freeze 0.1`
- frozen contract blob SHA: `b521aeb48b813fca5197b12e53e751354d60528c`

Underlying scientific authorities remain RB-004, RB-006 and RB-007.

## Frozen result

`PASS — V3C01–V3C09 ALL PASS UNDER RB-008`

The frozen result includes the following governed findings only:

1. V3C01 dimensional/normalized branch-operator equivalence and global gauge invariance PASS.
2. V3C02 phase-Jacobian comparison, gauge-null identity and chart-margin controls PASS.
3. V3C03 fixed-physical-delay period derivative, scalar coupling derivative and negative-control convention PASS.
4. V3C04 synthetic pseudo-arclength fold machinery PASS after a full contract-preserving rerun; no Lighthouse branch was used.
5. V3C05 exchange-symmetric two-cell parity/block controls and the corrected negative-prefactor `B` formula PASS.
6. V3C06 synthetic pitchfork algebra PASS; no Lighthouse pitchfork inference is made.
7. V3C07 deterministic first-hitting/transversality and negative controls PASS.
8. V3C08 arrival-aware integrated-mass and off-boundary derivative checks PASS; exactly at the declared arrival chart boundary the pointwise classical kink derivative is `ARRIVAL_CHART_BOUNDARY / DERIVATIVE_INVALID`, as required by RB-008.
9. V3C09 exact regular autapse branch sensitivity PASS.

Scientifically valid failures: none.
Execution blockers: none.

## V3C04 transcription correction audit

After the preliminary result document was committed, CORE found that the manually transcribed V3C04 20-row result table did not match the deterministic in-memory harness arrays.

MASTER accepts the correction as a clerical/result-serialization defect under the RB-008 software-plumbing rule because:

- only the human-readable V3C04 table/summary serialization was affected;
- V3C04 was rerun from the beginning under the unchanged RB-008 contract;
- the rerun was bitwise identical to the original deterministic in-memory V3C04 harness output;
- no model, parameter, reference state, derivative step, chart margin, solver step, tolerance, benchmark membership, negative control or PASS/FAIL rule changed;
- the incorrect preliminary V3C04 table remains preserved in Git history and is explicitly invalidated as scientific evidence.

The corrected V3C04 run remains PASS under the original contract.

## Freeze boundary

RB-009 does **not** freeze, validate, compute or authorize:

- any Lighthouse continuation branch search;
- any Lighthouse fold or pitchfork location or scaling;
- any v0.4 Floquet multiplier, stability boundary or dynamic classification;
- B23–B40 execution or legacy v0.4 tolerances;
- saltation claims beyond already frozen elementary event-time identities;
- hard-threshold tests for the smooth baseline;
- adaptive-delay or commensurability effects;
- production/JAX continuation or Floquet performance;
- normal-form fitting or effect-bearing critical coefficients;
- v0.5+ legacy recovery execution;
- inference, observation design, active experiment design, applications, novelty, manuscript claims or v0.27.

Legacy `core/theory-v0.1` remains read-only recovery evidence and is not merged.

## Change control

Any alteration of this result requires a new MASTER-authorized gate and a new versioned freeze. The invalidated preliminary V3C04 table remains part of the audit trail and must not be used as evidence.

## STOP

`CORE v0.3 Continuation Validation Result Freeze 0.1` is established.

STOP — FROZEN
