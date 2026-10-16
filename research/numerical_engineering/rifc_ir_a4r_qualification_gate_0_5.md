# NUM-ENG Gate 0.5 — MPFR IR-A4-R Qualification and Eventual Certification

Date: 2026-10-16. Workstream: 20 – NUM-ENG – Numerical Engineering.
Decision: IR-A4-R NOT ESTABLISHED — SOURCE-LEVEL ANALYTICAL NO-GO.
Status: RETURN TO MASTER; not a PASS for eventual certification. DEVELOPMENT EVIDENCE only.

## Frozen authorities and source

Gate prompt: research/master/prompts/numerical_engineering_rifc_ir_a4r_qualification_gate_0_5.md.
Pre-execution contract committed before validation outputs: 20d9ae3c5973b5226387c5f679c9ae03c1e58973.
Authorities: RB-019, RB-021, RB-023, RB-024, RB-025. Physical authority remains NUMENG_PULSE_AWARE_REFERENCE_V1.
Source: software/numerical_engineering/rifc_interval_gate_0_4/source/rifc_mpfr_v0_1.py.
Git blob 6df6740e86344628a2b9583f0a3f719f9d5817f8; SHA256 0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539.
Runtime: GNU MPFR 4.2.2, libmpfr.so.6.2.2 SHA256 4e3ccf5b442fc91054b0153140fe62939009f98ca1367f45de62376d5b18d28c, Python 3.13.5 x86_64.
All numerical tests use the exact prospectively fixed compact domain K=[-100000,100000]. No fixture, tolerance, source or domain was changed after output inspection.

## Q1: Primitive MPFR rates

Conditional on correctly-rounded MPFR with supported exponents, finite compact output bounds |y|<=M give an absolute directed rounding error bounded conservatively by 2^(ceil(log2(M))+1-p) per scalar rounding. Division also requires a positive divisor distance delta, with sensitivities bounded by 1/delta and M/delta^2. MPFR exp on compact arguments has bounded derivative exp(M). Endpoint loads, min/max/hull and intersection remain interval-valid under this contract.
However, the implemented primitive includes the Python function M.val after MPFR. Its precision-independent small-value floor is not covered by the MPFR ulp theorem. This is the decisive obstruction.

## Q2: Response threshold branches

Below threshold response is exactly 0. Threshold-straddling output is the monotone interval [0,S(upper)] without singular division at the threshold. The above-threshold branch uses a reciprocal-square followed by exp. On the frozen segment alpha=1, r=1, h=0, psi0=1/100, q0=0, L=1, the exact input stays above 1/300 (e<3), so the squared reciprocal denominator is bounded away from 0; all exact scalar intermediates remain inside K. Smooth mathematical response propagation does not overcome M.val's fixed floor.

## Q3: Alpha-state graph

The exact segment expressions q(s)=exp(-alpha*s)q0 and psi(s)=exp(-alpha*s)(psi0+s*q0) have bounded derivatives on K; the chosen case has q(s)=0 and psi(s)=exp(-s)/100. Exact interval time-range width is conceptually distinct from arithmetic rounding excess. Conditional O(2^-p) primitive rates would propagate through this fixed expression graph, but the later response exponential violates that condition in the actual implementation.

## Q4: Darboux cell and prefix operations

Each dyadic cell contains a fixed bounded number of interval loads, exp/alpha flow, response operations, width multiplication and one prefix addition. Product/division consider at most four endpoint combinations. A deliberately conservative count based on these bounded loops is N_n <= 1024 * 2^n + 1024 per level; total through n is <= 2048 * 2^n + 2048. The linear operation count does not prove a whole-expression B_K while even one actual primitive has a precision-independent excess.

## Q5: Analytical NO-GO

At x=1/100, h=0, r=1, exact S(x)=exp(-10000). Using e>2 yields 0<exp(-10000)<2^-10000<2^-2048. The source M.val checks MPFR binary exponent e.value < -2048, replacing a tiny positive RNDD result with 0 and RNDU with exactly 2^-2048. Thus I.point(-10000,p).exp() and response(I.point(1/100,p),1,0) return [0,2^-2048] for every supported p>=128.
For this exact singleton, arithmetic excess width is 2^-2048, independent of p. An inequality excess<=C_K*2^-p for every p forces C_K>=2^(p-2048), unbounded as p increases. No finite C_K exists on the frozen domain for the implemented Python+MPFR expression graph. Hence IR-A4-R and the requisite whole-expression B_K cannot be established for this source. This DOES NOT contradict conditional RB-024 theory or MPFR itself.

## Q6: Correspondence and source-level failure

The failing branch exists verbatim in M.val within the immutable RB-025 source. The correctly rounded MPFR primitive is followed by a non-rate-preserving dyadic serialization fallback. Independently, the certify API restricts nmax<=16 and therefore implements a finite-budget method, not an unbounded eventual-certification procedure. No code was repaired under this gate.

## Fixed negative-control reproducibility

The precommitted precisions were 128, 256, 512, 2048, 4096 bits. Both direct exp and composed response returned [0,2^-2048] at every precision; source and library hashes were asserted in the diagnostic. Results: research/numerical_engineering/rifc_ir_a4r_negative_control_results_0_5.json. Proof: research/numerical_engineering/rifc_ir_a4r_no_go_proof_0_5.md. Portable script: software/numerical_engineering/rifc_ir_a4r_gate_0_5/diagnose_rate_v05.py.

## Q7 and Q8: NOT EXECUTED as required

Because the analytical Q5 prerequisite is false, no empirical rate fitting or eventual-certification fixture was performed. A finite nmax exhaustion must remain RESOURCE_EXHAUSTED / UNCERTIFIED, never evidence of physical no-hit. Full multi-event tapes and NNE-A remain outside scope.

## Preservation of RB-025

No RB-025 source changed. Its 26 targeted test cases independently passed with clean exit 0, and all six saved positive certificate artifacts passed independent replay without physical simulation. FINITE SOUNDNESS PRESERVED; EVENTUAL CERTIFICATION NOT ESTABLISHED.

## Classification and MASTER recommendation

FINITE SOUNDNESS PRESERVED: RB-025 positive finite certificates in their captured numerical envelope.
IR-A4-R NOT ESTABLISHED / REPAIR-REQUIRED: nonvanishing dyadic export floor blocks the frozen uniform p-rate.
DEFERRED: rate constant B_K, eventual termination claims, full event-tape certification, NNE-A, AI and scientific speedups.
REJECTED: claiming that correct MPFR rounding also proves the rate of modified Python serialization; empirical fitting of B_K; post-output domain reduction.

Recommend a separately authorized prospective gate to replace/fail-close the M.val fixed floor with a precision-scaled inclusion-preserving conversion or exact MPFR dyadic export, then repeat finite-soundness QA and independently prove the rate on a precommitted domain. Do not silently edit or replace RB-025.

No protected 2701xxx/2711xxx RNG/data, TR-27C, APP-3, main merge, scientific effect, novelty or manuscript work. RB-015 remains SCIENTIFIC FAIL, RB-020 is parked.

STOP — RETURN TO MASTER.
