# NUM-ENG Theory-Derived First-Hit Certification Validation Gate 0.3 — RETURN

Date: 2026-10-16
Workstream: 20 – NUM-ENG – Numerical Engineering
Engineering decision: **PASS — THEORY-CONSISTENT ENGINEERING VALIDATION (finite, non-formal)**
Evidence: **ENGINEERING VALIDATION / DEVELOPMENT EVIDENCE ONLY**
Branch: `engineering/numerics-v0.1`

## Authorities and chronological controls

Frozen science/theory: RB-004 and RB-022, with the corrected structural-zero semantic repair controlling TH-FH-06. Engineering dependencies: RB-019 `NUMENG_PULSE_AWARE_REFERENCE_V1`, RB-021 high-level tape validator, and the current MASTER Gate-0.3 prompt. RB-020 is a parked CORE pre-execution contract, not executed here.

The complete finite contract was committed **before new Gate-0.3 tests** at `research/numerical_engineering/theory_derived_first_hit_validation_contract_0_3.md`, commit `7a488ed6777d206313c512f437216b05b8e5eb6e`. Source-contract SHA-256: `3732943fe4746a6c0d76304f8751ff98bac99ae0c41959d66118bce22ab81be5`. Fixtures, topology, histories, equalities, margins, refinement sequence n∈{64,128,256,512,1024,2048}, and TV-01..TV-11 tolerances were not altered after viewing results. No generated stochastic data or protected seeds.

The physical and high-level JAX guard source Git blob SHAs were verified against the frozen engineering branch. Numerical reference source remains unchanged. This gate adds a deterministic validation harness only; it does not replace the authoritative scheduler.

## TV-01..TV-11 result matrix

| Family | Finite result | Required classification |
|---|---|---|
| TV-01 | PASS — Exact alpha-state propagation (4 parameter cases, 24 samples) | THEORY-CONSISTENT ENGINEERING VALIDATION |
| TV-02 | PASS — Arrival-free analytic extrema (4 cases) | THEORY-CONSISTENT ENGINEERING VALIDATION |
| TV-03 | PASS — Strict upper no-hit; equality UNCERTIFIED; near-threshold no-hit | THEORY-CONSISTENT / UNCERTIFIED control |
| TV-04 | PASS — Constant and narrow-pulse unique first hit; endpoint bracket UNCERTIFIED | THEORY-CONSISTENT / UNCERTIFIED control |
| TV-05 | PASS — Sharp S-prime and S-double-prime bounds, r={0.25,1,4} | THEORY-CONSISTENT ENGINEERING VALIDATION |
| TV-06 | PASS — Alpha mass and finite omitted-history phase bound; missing-tail UNCERTIFIED | THEORY-CONSISTENT / UNCERTIFIED control |
| TV-07 | PASS — 12 physically rerecorded regular-chart perturbations, unchanged labels | THEORY-CONSISTENT ENGINEERING VALIDATION |
| TV-08 | PASS — 5 JAX/physical-FD coordinates, including structural zero delay and weight | THEORY-CONSISTENT ENGINEERING VALIDATION |
| TV-09 | PASS — Topology-fixed zero-weight triplet, omitted-edge contrast and guard rejection | THEORY-CONSISTENT ENGINEERING VALIDATION |
| TV-10 | PASS — TH-FH-01...TH-FH-08, all covered; collisions physically valid but chart invalid | THEORY-CONSISTENT / INVALID / UNCERTIFIED |
| TV-11 | PASS — Stale timestamps, dropped zero edge, missing certification, changed itinerary | THEORY-CONSISTENT negative controls |

Every above TV family completed twice with clean exit code 0, including one fresh single-process TV-01..TV-11 rerun. The raw `TV_RESULTS.json` contains outcomes, parameter values, margins and errors. Two full-phase outputs are in `TV_01_06.log` and `TV_07_11.log`; `TV_01_11_REPRO.log` is the independently repeated single-process log.

## Decisive numeric observations

- TH-FH-01 narrow pulse: physical t=0.5050005053634212; independent segmented quadrature first hit t=0.5050005053634210, absolute discrepancy 2.22e-16. Strict upper/lower enclosure bracket [.004,.007] relative to arrival .5 passed at n=64.
- TV-06 finite omitted-tail phase discrepancy = 0.023643397381274, theorem Lipschitz/mass upper bound = 0.0325178946640312. Equality margin and absent infinite-tail summability explicitly classified UNCERTIFIED.
- TV-07 tested 12 fixed signed perturbations; smallest observed margins: transversality=0.36790092; inter-event separation=0.0027747987; boundary=0.19437144. These are empirical margins, not a rigorously certified open-ball radius.
- TV-08 fixed-chart JAX/physically certified replay spike-time max residual = 9.59e-14. Differentiating a structural weight at exactly zero remains meaningful.

| Derivative | Max |AD - physical FD| |
|---|---:|
| nonzero_weight | 6.08907591015e-10 |
| zero_weight | 5.41919620289e-10 |
| active_delay | 3.02006197828e-10 |
| zero_delay | 3.5526026565e-11 |
| initial_theta | 1.89521287552e-10 |

- Zero-weight structural arrival derivative with respect to its own delay: 0.99999999999989 (theory +1 for the fixed historical launch).
- TV-09: kept-zero graph has 8 labelled arrivals, omitted-edge graph 5; spike and final-state trajectories agree to frozen finite tolerance; tokens differ.

## TH-FH-01..08 classification (TV-10 cross-references TV-03/04/06/09)

1. TH-FH-01 CERTIFIED REGULAR HIT, narrow pulse; coarse endpoint-only no-hit rejected.
2. TH-FH-02 CERTIFIED NO-HIT under strict threshold margin.
3. TH-FH-03 regular synthetic segment with delta=.2 and t*=1; delta=.01 is UNCERTIFIED in float64, not physically invalid.
4. TH-FH-04 opposite event order at ±.001; exact coincidence is PHYSICALLY VALID BUT ORDINARY-CHART INVALID.
5. TH-FH-05 finite-history strict tail margin valid; equality/summability-absent controls UNCERTIFIED.
6. TH-FH-06 topology-fixed edge at w=-1e-4,0,+1e-4; at zero physical equality with edge-omitted graph but distinct labelled tapes.
7. TH-FH-07 horizon t_H=1.5001/1.5/1.4999 is respectively regular interior hit / chart-boundary invalid / no-hit on shortened horizon.
8. TH-FH-08 simultaneous independent arrival jumps commute physically, but ordinary sequential chart invalid due labelled tie.

## Compatibility/process result

- Three targeted baseline modules (`test_reference.py`, `test_rri_repair_v01.py`, `test_gate02_batch_guard.py`): **28 tests PASS, process exit 0**, local CPU under captured isolated environment.
- An attempted aggregate legacy suite (RB-017+RRI+RB-021: expected 250 cases) exceeded the external execution time limit; process did not produce an exit code or a PASS summary. The raw log shows only progress dots. It is NOT counted as completed regression or treated as implementation failure. The already-frozen RB-021 250/250 evidence remains independently frozen, but is not falsely repeated here.
- No source changes were necessary. Gate 0.3 is an additive deterministic validation; no source alteration to RB-019/021, no executable merge to main.

## Important limitations and disposition

- The finite extremum-based gain bounds are calculated in float64, not with an outward-rounded interval library. Passing these tests **does not establish a rigorous floating-point certification theorem**, globally sharp chart radius or universal first-hit correctness. Classification is THEORY-CONSISTENT ENGINEERING VALIDATION, not universal certificate.
- `UNCERTIFIED` is not conflated with a physical singularity or a mathematically invalid event. Exact ties are physically meaningful but excluded from the ordinary sequential-chart claims.
- TH-FH-03 `delta=.01` has mathematically positive velocity but is under-resolved in floating point; the harness declines regular certification.
- Conceptual divergent infinite-history negative control is not instantiated in the finite software scheduler; no absolute-tail bound is asserted from local finiteness alone.
- Repetition/portability of the complete legacy 250-case aggregate remains a practical QA follow-up. No component was retuned to rescue a post-output failure.
- Source/rerecord and guard: ENGINEERING-APPROVED WITH DOMAIN (unchanged RB-019/021); theorem-derived finite validation harness: THEORY-CONSISTENT ENGINEERING VALIDATION; outward interval arithmetic/global certificate: DEFERRED; arbitrary unguarded JAX as independent physical authority: REJECTED.

## Engineering gate decision and STOP

**PASS — engineering theory-consistency validation on the fixed finite cases.** Recommend to MASTER a narrowly bounded `NUM-ENG Theory-Derived Certification Validation Freeze 0.3`, preserving the above limitations and the uncompleted aggregate regression as follow-up QA. No new scientific effect result exists.

RB-015 remains SCIENTIFIC FAIL. RB-020/TR-27C not executed; `2711xxx` ungenerated/unevaluated; APP-3 remains PROTECTED/WAIT. No stochastic benchmark, no model training, no novelty or manuscript claim, no executable source merge to `main`.

**STOP — RETURN TO MASTER.**
