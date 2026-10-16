# NUM-ENG RIFC-0.1 Interval Certification Freeze 0.4

Date: 2026-10-16
Status: FROZEN / STABLE ENGINEERING CERTIFICATION LAYER — FINITE SOUNDNESS ONLY
Rollback point: RB-025

## Authority

MASTER reviews and accepts the returned:

\`NUM-ENG RIFC-0.1 Outward-Interval Implementation & Validation Gate 0.4\`

from:

\`engineering/numerics-v0.1\`.

Frozen provenance:

- pre-execution contract commit: \`2aa95c77973fe63a82a7cf11472ee92273b5bb7c\`;
- contract blob SHA: \`99e8e4a96607fd4663c33c8fefcc937bc506cb13\`;
- returned gate blob SHA: \`b5512d38b9735012052984a7cc4ace7d8885c146\`;
- implementation integration commit: \`e5b1c488aa6e03e706171902942377c210979a8f\`;
- outcome-matrix commit: \`8b6d8455226d12489b08804d8915b28f2203df9b\`;
- source blob SHA: \`6df6740e86344628a2b9583f0a3f719f9d5817f8\`;
- source SHA-256: \`0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539\`;
- physical authority: RB-019 / \`NUMENG_PULSE_AWARE_REFERENCE_V1\`;
- engineering baseline: RB-021;
- theory-validation result: RB-023;
- theory authority: RB-024.

The Gate-0.4 finite contract was committed before new validation outputs.

No post-output change to the frozen fixture set, acceptance classes, backend choice or scientific target is accepted into RB-025.

## Gate result

\`PASS — ENGINEERING VALIDATION / FINITE CERTIFICATE SOUNDNESS ONLY\`

RB-025 is explicitly bounded.

It does not establish the RB-024 IR-A4-R whole-expression convergence-rate obligation and does not freeze an eventual-certification guarantee.

## Backend

The accepted finite-soundness backend is:

- GNU MPFR 4.2.2;
- directed RNDD / RNDU operations;
- rigorous exponential inclusion through MPFR's correctly-rounded directed \`mpfr_exp\` contract;
- exact-rational input loading by outward endpoint construction;
- exact dyadic-rational serialization of certificate endpoints;
- fail-closed behavior for unsupported/nonfinite/zero-denominator proof cases.

The accepted finite result is conditional on the documented MPFR correct-rounding semantics and captured runtime/library identity.

RB-025 does not formally verify the MPFR implementation itself.

## Frozen implementation scope

Within the tested finite deterministic domain, RB-025 accepts:

1. inclusion-valid interval primitives used by RIFC-0.1;
2. arrival-free interval alpha-state propagation;
3. threshold-safe monotone response enclosures;
4. dyadic Darboux gain enclosures;
5. outward prefix gain tapes;
6. strict-margin \`CERTIFIED_NO_HIT\`;
7. strict-bracket \`CERTIFIED_REGULAR_HIT\`;
8. rigorous finite transversality lower bounds on certified brackets;
9. exact-rational event-order/horizon/initial-boundary checks;
10. topology-fixed structural-zero labelled arrivals and zero-crossing weight intervals;
11. finite resource limits and fail-closed nonpositive outcomes;
12. serializable positive proof artifacts;
13. independent certificate replay without rerunning the physical simulator.

A positive regular-hit certificate applies to an individual arrival-free segment with known initial alpha state and phase gap.

RB-025 does not emit a general \`CERTIFIED_ORDINARY_CHART\` for arbitrary parameter families.

## Validation freeze

The preregistered Gate-0.4 validation records:

- RI-01: PASS;
- RI-02: PASS;
- RI-03 / IR-A4-R: DEFERRED / NOT ESTABLISHED;
- RI-04 through RI-12: PASS within frozen finite scope;
- RI-13 eventual-certification theorem validation: DEFERRED because IR-A4-R is not established;
- RI-14 finite-budget behavior: PASS with \`RESOURCE_EXHAUSTED / UNCERTIFIED\`.

New Gate-0.4 test suite:

- 26/26 PASS;
- repeated 26/26 PASS;
- both clean exit 0.

Compatibility subset:

- 28/28 PASS;
- clean exit 0.

Saved positive proof artifacts:

- 6/6 independently replay/audit PASS.

Interim software/test failures are retained in provenance and were corrected conservatively without changing the pre-execution fixture contract or interval backend.

## TH-FH relationship

Within the frozen finite Gate-0.4 domain:

- TH-FH-01 narrow-pulse: certified regular hit;
- TH-FH-02: certified no-hit;
- TH-FH-03: strict-margin negative control remains nonpositive rather than overpromoted;
- TH-FH-04: strict orders certified, exact tie ordinary-chart invalid;
- TH-FH-05: finite summable tail check consistent; unsupported infinite-history case deferred;
- TH-FH-06: structural-zero semantics preserved;
- TH-FH-07: boundary cases ordinary-chart invalid;
- TH-FH-08: simultaneous commuting arrivals remain ordinary-chart invalid under sequential ordinary-chart theory.

No RB-024 theorem contradiction was observed in these finite fixtures.

## Fail-closed classes

The implementation includes finite controls for:

- ASSUMPTION_VIOLATED;
- STRICT_MARGIN_ABSENT;
- ENCLOSURE_INCONCLUSIVE;
- RESOURCE_EXHAUSTED;
- UNCERTIFIED_ARITHMETIC;
- ORDINARY_CHART_INVALID;
- UNSUPPORTED_CASE.

No such control is promoted to a positive certificate.

## Certificate auditability

Positive artifacts retain the finite proof data required to reconstruct/check:

- exact rational inputs;
- topology identity;
- backend/version/precision;
- cell state intervals;
- response intervals;
- gain/prefix intervals;
- phase-gap intervals;
- hit/no-hit strict inequalities;
- transversality lower bounds;
- competing event/order data where applicable;
- output identity/hash data.

The saved-certificate auditor recomputes interval proof obligations without invoking the physical simulator.

## Explicit limitations

### IR-A4-R

Not established.

No uniform whole-expression bound

\[
E_{\rm arith}(N,p)\le B_KN2^{-p}
\]

has yet been independently derived for the implemented RIFC expression graph/backend/domain.

Therefore RB-025 does not claim:

- the RB-024 eventual-certification theorem is implemented;
- the fixed \(p_n=128+8n\) schedule is proven sufficient in software for all strict-margin cases in the supported domain.

Empirical successful refinement is not substituted for that proof obligation.

### Full multi-event certification

Deferred:

- automatic full sequential multi-event tape certification;
- general parameter-box NNE-A;
- general full-chart radius.

### Other deferred claims

RB-025 does not establish:

- global simulator correctness;
- global first-hit completeness;
- formal verification of MPFR itself;
- GPU portability;
- scientific speedup/scaling;
- AI performance.

## Component classification

### ENGINEERING-APPROVED FOR FINITE SOUNDNESS ONLY

- captured MPFR 4.2.2 directed interval backend;
- finite RIFC arrival-free segment certification;
- finite structural-zero/event-order logic;
- finite proof serialization/replay.

### ENGINEERING-APPROVED

- deterministic QA/provenance harness;
- exact source/input/manifests;
- saved-certificate audit workflow.

### DEFERRED

- IR-A4-R;
- eventual certification;
- sequential whole-tape RIFC;
- NNE-A / parameter-box full-chart radius;
- formal MPFR verification;
- global/portable performance claims.

### REJECTED

- \`math.exp\` + unproved nextafter as rigorous exponential proof;
- interval overlap interpreted as collision/order proof;
- token equality alone as physical/tape authority;
- global/eventual claims inferred from finite QA.

## Governance boundaries

RB-025 does not:

- alter RB-015 SCIENTIFIC FAIL;
- execute RB-020/TR-27C;
- create any \`2711xxx\` RNG object;
- authorize APP-3;
- authorize v0.28 effect-bearing science;
- merge executable source to \`main\`;
- create novelty/manuscript claims.

## STOP

RB-025 freezes a bounded finite-soundness engineering certification layer only.

STOP — FROZEN / STABLE ENGINEERING CERTIFICATION LAYER — FINITE SOUNDNESS ONLY
