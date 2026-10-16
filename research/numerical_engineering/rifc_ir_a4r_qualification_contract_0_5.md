# NUM-ENG Gate 0.5 — IR-A4-R qualification pre-execution contract

Date: 2026-10-16
State: FROZEN BEFORE ALL NEW GATE-0.5 VALIDATION OUTPUTS
Purpose: Qualify or rigorously reject the IR-A4-R rate for the unmodified RB-025 code. All outputs ENGINEERING VALIDATION / DEVELOPMENT EVIDENCE; no scientific effect claim.

## Exact authority and source identity

RB-024 rigorous interval theory with mandatory proof-closure repair; RB-025 finite certificate implementation. Branch engineering/numerics-v0.1.
Source path: \`software/numerical_engineering/rifc_interval_gate_0_4/source/rifc_mpfr_v0_1.py\`.
Git blob SHA1: \`6df6740e86344628a2b9583f0a3f719f9d5817f8\`.
Source byte SHA256: \`0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539\`.
Backend: GNU MPFR 4.2.2 (\`mpfr_get_version\`), dynamically linked \`libmpfr.so.6\`; OS package libmpfr6 4.2.2-1; ELF \`/lib/x86_64-linux-gnu/libmpfr.so.6.2.2\` SHA256 \`4e3ccf5b442fc91054b0153140fe62939009f98ca1367f45de62376d5b18d28c\`. Python 3.13.5, Linux x86_64.
No library upgrade, code repair or domain shrinking is allowed within the Gate 0.5 analysis. The physical simulator authority \`NUMENG_PULSE_AWARE_REFERENCE_V1\` remains untouched.

## Domain K (fixed without reviewing Gate-0.5 output)

Primary exact singleton arrival-free segment:
\`alpha=1, r=1, h=0, psi0=1/100, q0=0, L=1\`.
Exact phase gap for strict-margin near-zero no-hit case: \`d=2^-2049\` (exact dyadic fraction). For threshold-safe graph branch controls, include exact below-threshold x=-1/2, above-threshold x=1/100, and threshold-straddling interval [-1/100,1/100], with \`h=0,r=1\`.

Choose compact scalar domain \`K=[-100000,100000]\` for every *exact real scalar* appearing in the named expression graphs, including exp inputs. On the primary segment, x(s)=exp(-s)/100 in [exp(-1)/100,1/100] and thus remains strictly above zero. A proved convenient lower bound is \`x(s)>1/400\` for 0<=s<=1, since e<4; hence denominator \`(x-h)^2>1/160000\`. The above-threshold reciprocal is therefore explicitly away from zero. The exact negative reciprocal lies in (-160000,0) using only that bound; the chosen finite K=-100000…100000 is instead supported by the sharper analytic bound e<3, giving x(s)>1/300 and negative reciprocal >-90000. All other exact graph intermediates fit K. For the separate threshold-straddling case, NO reciprocal is evaluated at/below threshold, consistent with RB-024.

The exact scalar exp argument \`-10000\` arises from \`S(1/100)\` with r=1,h=0. This is the **prospectively frozen candidate arithmetic-rate negative control**, not a fitted case. The compact domain includes small positive outputs but forbids no positive value on magnitude grounds. Division in the above-threshold branch is admissible on the stated singleton trajectory.

## Expression-graph and primitive inventory (actual RB-025 source)

\`_fraction_round\`: rational-to-MPFR via correctly rounded integer parsing and division;
\`_binary\`: add/sub/mul/div using RNDD/RNDU;
\`M.val\`: MPFR binary to exact dyadic \`Fraction\` serialization, with branch: for binary exponent \`e.value < -2048\`, output 0 for one directed bound and \`+/- 2^-2048\` for the other, independent of requested precision; for \`e.value > 2048\` fail.
\`I.point,I.bounds,I._op,I.exp,I.sqrt,I.hull,I.intersect,I.min_with,I.max_with\`: interval operations and correctly directed primitive rounding.
\`psi_interval,q_interval\`: exp(-alpha*s), linear alpha-state products/sums.
\`response\`: x.hi<=h => 0; straddling => [0, upper above threshold]; x.lo>h => above-threshold reciprocal-square and exp.
\`darbouxs\`: each of m=2^n cells uses 2 endpoint loads, 1 psi interval, 1 response, 1 width*response gain and 1 prefix addition; arithmetic dependency via interval ranges must be distinguished from *arithmetic excess*.
\`certify\`: p_n=128+8n, n=0..nmax; nmax hard capped at 16; strict no-hit/hit checks; event order/collision logic separate and does not change arithmetic graph.
\`structural_arrival,event_order,artifact_json\`: interval alpha^2 jump and exact rational ordering/serialization; no omitted primitive/branch for a positive certificate.
MPFR exponent range assumption: actual MPFR exponents remain in the backend supported range. The source's additional -2048 serialization cutoff is a separate algorithm-level branch, not an MPFR exponent-underflow guarantee. No formal overflow/subnormal behavior is being inferred from Python float.

## Definitions and analytical obligation

At exact singleton operands, \`excwid\` of an outward output interval is its width minus the width of the exact real image (0 for a singleton). For general interval operands subtract the exact range width. IR-A4-R requires a finite K-uniform constant C_K **independent of precision p**, and a B_K **independent of n and p**, such that primitive arithmetic excess <=C_K 2^-p and the fixed graph output excess <=B_K N_n 2^-p.

Q1: derive MPFR correctly-rounded primitive ulp bounds conditional on normal finite exponent range and exact endpoint loading; include factors 2^ceil(log2|y|) and divisor distance. Explicitly account for serialization branches beyond pure MPFR.
Q2: examine derivative/lipschitz propagation in all three threshold branches and with x-h>=1/400 on primary singleton trajectory.
Q3: bound q(s),psi(s) arithmetic propagation using fixed alpha, s, psi0, q0.
Q4: derive a conservative operation count \`N_n <= a 2^n+b\` from source graph and finite repeated cells, with explicit a,b or provable overcount, and the hoped-for B_K requirement.
Q5/Q6: inspect \`M.val\` and \`I.exp\` for a precision-independent excess-width floor on S(1/100). Determine whether this produces a rigorous NO-GO for the actual implemented graph under the fixed K. Distinguish an MPFR primitive bound from the full Python serializer's bound.
Q7: numerical rate-validation is permitted **only after** a successful analytical Q5 PASS with a fixed B_K. If Q5 NO-GO, do NOT run Q7 to fit a rate.
Q8: eventual-certification trial family is permitted **only after** Q5 PASS. If Q5 NO-GO, do NOT claim eventual certification or run an empirical substitute; retain finite positive certificate soundness (RB-025).
Q9: no multi-event/NNE-A, optimizer, scaling, TR-27C, APP-3 or protected seed operations.

## Prospective finite diagnostics for the NO-GO route

If the source-level branch shows a rigorous contradiction, validate its *mechanism only*, at fixed precisions p={128,256,512,2048,4096}: evaluate \`I.point(-10000,p).exp()\` and \`response(I.point(1/100,p),1,0)\` without modifying source. The expected classification is \`IR-A4-R NOT ESTABLISHED / SOURCE RATE COUNTEREXAMPLE\` if output width remains 2^-2048 or otherwise fails the fixed O(2^-p) requirement. Do not fit C_K or B_K from measurements. For exact mathematical containment, bound 0<exp(-10000)<2^-10000<2^-2048 using e>2; this uses no floating-point assertion. The independent exact arithmetic implication is that any nonvanishing width floor cannot be <=C_K 2^-p for *all* p with finite C_K.

Check \`certify\`'s hard nmax<=16 gate separately: a finite Nmax run is a finite-budget procedure, not an unbounded eventual-certification guarantee. No change of Nmax is authorized.

## Deterministic technical validation and output format

Create \`research/numerical_engineering/rifc_ir_a4r_qualification_gate_0_5.md\` with Q1–Q9 disposition, source SHA and backend identity, explicit mathematical argument, and result classification. Preserve raw JSON (fixed precision + exact rational endpoints) and a reproducible pure-Python diagnostic script, with environment, SHA256 manifest. All source files remain unchanged. If the Q5 NO-GO is mathematically demonstrated, gate outcome is \`IR-A4-R NOT ESTABLISHED — CONDITIONAL/BLOCKED FOR EVENTUAL CERTIFICATION\`; finite-soundness RB-025 remains in force. Update NUM-ENG STATUS to \`BLOCKED\` or \`RETURN TO MASTER\` with the exact recommendation.

Negative controls: no implicit rounding-to-nearest \`math.exp\`; no posthoc source modification; no shrinking K; no treating nmax exhaustion as physical non-hit; no scientific promotion. Test harness MUST assert source byte hash / MPFR version before diagnosis. Gate result is not a scientific PASS/FAIL.

STOP — RETURN TO MASTER.
