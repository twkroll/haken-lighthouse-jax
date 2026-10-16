# NUM-ENG RIFC-0.1 — finite pre-execution contract 0.4

Date: 2026-10-16
Status: FIXED BEFORE VALIDATION OUTPUT (engineering only).
Authority: RB-004, RB-019, RB-021, RB-023, RB-024 and MASTER NUM-ENG gate 0.4.
Branch: \`engineering/numerics-v0.1\`; physical simulator authority remains \`NUMENG_PULSE_AWARE_REFERENCE_V1\`.

## Backend and inclusion contract (IR-A1–IR-A3, IR-A5)

Backend: **GNU MPFR 4.2.2**, Linux \`libmpfr.so.6\` dynamically linked via Python 3.13.5 \`ctypes\`; version read from \`mpfr_get_version()\`. MPFR is the open-source correctly rounded multiple-precision binary arithmetic library based on the IEEE 754 floating-point arithmetic model. The upstream MPFR correctly-rounded elementary-function specification is the relied-upon independent EXP inclusion contract: \`mpfr_exp(x, MPFR_RNDD)\` is a lower enclosure, \`mpfr_exp(x, MPFR_RNDU)\` upper. The library calls for +, -, *, / use the same directed-rounding modes on finite operands. Input exact rational numbers are loaded by rounded directed numerator/denominator operations. Each endpoint is serialized as an *exact dyadic rational*, not a Python float. Hull, intersection, and min/max select verified endpoints using MPFR comparisons. Division requires divisor interval strictly away from zero; invalid inputs/overflow/NaN fail closed. Positive certificates must not involve standard float \`exp\` or nextafter approximations.

IR-A1: all primitive interval operations include exact real ranges on finite admissible operands when MPFR is correctly rounded.
IR-A2: directed rounding for every operand load and arithmetic primitive, rather than nearest-rounded scalar arithmetic.
IR-A3: exponential inclusion uses MPFR's correctly rounded directed \`mpfr_exp\`; no unproven libm-based error bound.
IR-A5: fail-closed on unsupported, zero-containing divisors, nonfinite endpoints, arithmetic exceptions or inability to serialize exact endpoint.
MPFR's documented correct-rounding contract supplies the finite-result inclusion justification; this gate does not independently formally verify MPFR's implementation. All positive certificates record library version and precision.

**IR-A4-R: NOT ESTABLISHED**. In particular, no independently derived uniform \`B_K N 2^-p\` whole-expression constant is claimed. Eventual certification and automatic full parameter-box NNE-A radius remain \`DEFERRED / NOT ESTABLISHED\`. A bounded PASS would therefore certify **finite certificate soundness only**.

Precision/refinement: \`p_n=128+8n\`, \`m_n=2^n\` equal dyadic cells, integers n from 0 through Nmax. Candidate domain for this finite validation: positive singleton alpha in {1,1000}, positive singleton r=1, h in {-1,1,1/10}, singleton segment L in {1,4,1/50}, singleton inputs psi0 in {0,1/4}, q0 in {0,1/2,4000000}, exact gap d in {0,1/4,1,1/200}. All are exact rationals, no parameter-family interval NNE-A. All computed exact intermediates are finite on these compact segments; arithmetic proof failures are rejected.

## Fixed fixtures, comparison rules and expected outcomes

Use equal dyadic time partitions for every segment; compute alpha-state \`q(s)=exp(-alpha*s)q0\`, \`psi(s)=exp(-alpha*s)(psi0+s*q0)\`, then \`S=0\` for x<=h and \`S=exp(-r/(x-h)^2)\` for x>h, including the threshold-crossing monotone splice. Darboux cell gain is \`Delta*R(cell)\`; outward prefix sums are recorded.

- **S01 / TH-FH-02**: alpha=1, r=1,h=1,psi0=0,q0=0,L=1,d=1/4; \`CERTIFIED_NO_HIT\`; Nmax=5.
- **S01T**: same, with threshold box x=[1,1], and x=[3/4,5/4]; endpoint response bounds include zero; no division at x=h; no hit S01T at d=1/4.
- **S02**: alpha=1,r=1,h=-1,psi0=0,q0=0,L=4,d=1; \`CERTIFIED_REGULAR_HIT\`; Nmax=7; exact mathematical hit t=e is expected only as independent validation comparator, never as certificate input.
- **S03 / TH-FH-01**: alpha=1000,r=1,h=1/10,psi0=0,q0=4000000,L=1/50,d=1/200; \`CERTIFIED_REGULAR_HIT\`; Nmax=10. Independently check first-hit inclusion against RB-019 narrow first-hit offset \`t-1/2=0.005000505363421\`, numerical-comparator-only.
- **S04**: same as S01 but d=0; \`STRICT_MARGIN_ABSENT\` (initial phase gap zero; no false strict positive certificate).
- **S05**: same as S03 but Nmax=0; expected \`RESOURCE_EXHAUSTED\`, never a false NO-HIT.
- **S06**: same as S01 but alpha=-1; \`ASSUMPTION_VIOLATED\`.
- **S07**: same as S02 but declared backend unavailable; \`UNCERTIFIED_ARITHMETIC\`.
- **S08**: interval-valued alpha=[1,2] on an unsupported parameter-family full-chart request; \`UNSUPPORTED_CASE\`, not an accepted global chart.
- **S09**: request event order spike interval [2/5,3/5] vs arrival [1/2,7/10]; \`ENCLOSURE_INCONCLUSIVE\`.
- **S10 / TH-FH-04**: exact spike and structural arrival both t=1/2; \`ORDINARY_CHART_INVALID\`. Spike before-arrival and arrival-before-spike controls use disjoint rational brackets [1/4,1/3] and [1/2,2/3] and their reversal; expect \`CERTIFIED_EVENT_ORDER\`.
- **S11 / TH-FH-07**: point event at t=1/2 and horizon=1/2, or t=0 initial boundary; \`ORDINARY_CHART_INVALID\`.
- **S12 / TH-FH-08**: two simultaneous commuting structural arrivals at t=1/2 to distinct targets; both jumps included in physical interval state, but ordinary order \`ORDINARY_CHART_INVALID\`.
- **S13 / TH-FH-06**: fixed structural edge labelled e0 arrival t=1/2 with weight in [-1/16,0,1/16] while alpha=1; retain e0 and jump interval \`weight*alpha^2\`; at zero jump exactly zero; omitted-edge comparison has different labelled event tape; negative control deletes arrival from base tape and must be rejected.
- **S14 / TH-FH-03**: constant positive crossing S02 and analytically near-threshold point x=h+1/4 with r=1, where transversality is \`exp(-16)\`; if transversality lower bound demanded >=1/1000, do not promote to regular hit (\`STRICT_MARGIN_ABSENT\`), not a theorem contradiction.
- **S15 / TH-FH-05**: alpha=1,A=4,L=1, finite omitted pulse weights [1/2,1/4] and ages [4,5]; compute \`M_eta(A)=e^-A(1+A)\`; verify integral omitted-tail bound and \`L_S=2(3/2)^(3/2)e^-3/2\` using MPFR enclosures, with independent high-precision quadrature comparator; no finite-tail theorem certificate claimed for history lacking absolute summability.
- **S16**: interval gain for alpha=1, psi0=1/4,q0=1/2,L=1,r=1,h=-1 at levels n=0,2,4,8; include analytic alpha formula samples s=0,1/8,1/2,1 and 200-digit mpmath gain comparator. Nmax=8.
- **S17**: exact alpha propagation at alpha=1000,psi0=0,q0=4000000, s=1/1000,1/200,1/50; independently compare 200-digit mpmath value enclosure.
- **S18**: arithmetic primitives on exact rational operands a=-7/8,b=3/5,c=11/10; check +, -, *, /, exp for point/interval cases plus hull/intersection/min/max against exact Fraction or mpmath 200-digit point references.
- **S19**: replay a serialized \`CERTIFIED_NO_HIT\` and \`CERTIFIED_REGULAR_HIT\` proof with separate checker redoing exact endpoint inequality and all cell/prefix bounds from the serialized input; deliberately corrupt a stored prefix, precision identifier, event signature, strict margin or bracket and require rejection.

RI-01 through RI-12 each map to S01–S19, as stated in MASTER prompt. RI-13 is \`DEFERRED\` because IR-A4-R is not established; finite deterministic n-level refinement output may be logged without a termination theorem claim. RI-14 uses S05.

All positive proofs record exact input rationals, fixed topology signature, backend identity, p, level, each cell psi and S enclosure, each prefix, phase-gap, bracket endpoint inequalities, transversality lower bound, event/arrival/horizon comparisons if applicable, and input/output SHA256. Checker runs without physical simulator, recomputes MPFR enclosures and checks all interval/prefix inclusions and strict inequalities. Mutations must fail.

Comparison: exact rational containment for polynomial primitives; independent mpmath \`dps=200\` point/integral values must be contained in serialized dyadic intervals with no ad-hoc tolerance. RB-019 physical hit merely verifies membership in rigorous bracket (not used for bracket construction). Mathematical equality ties are explicitly invalid; overlap without exact proof is UNCERTIFIED.

Compatibility (without changing any RB-019/RB-021 source): \`tests/test_reference.py\` (6), \`tests/test_rri_repair_v01.py\` (14), \`tests/test_gate02_batch_guard.py\` (8) if available in the baseline overlay; any missing suite is reported unavailable, never invented. New test suite shall have a clean process exit. All evidence is DEVELOPMENT / ENGINEERING VALIDATION only. Manifest: SHA-256 of each new file plus exact MPFR runtime and CPU/backend metadata; JSON certificates with canonical sorted keys; raw tests/logs/fixture results in versioned subtree. No new stochastic trials, protected seed streams, TR-27C or APP-3. Do not change fixtures/tolerances/classifications after output.
