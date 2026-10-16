# Gate 0.6 — Exact MPFR/GMP dyadic export and IR-A4-R requalification

Date: 2026-10-16. Engineering proof/evidence only; frozen science RB-024 remains unchanged.

## 1. Provenance and immutability

The baseline, SHA256 `0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539` / git blob `6df6740e86344628a2b9583f0a3f719f9d5817f8`, is never edited. The replacement is versioned separately as `rifc_mpfr_v0_2.py`. The frozen prospective Gate-0.6 contract was committed at `779c8f05256406c5684d4dec35ae123a418027fb` before code changes or validation results. MPFR 4.2.2 and GMP 6.3.0 are fixed and exact library hashes are recorded by the contract.

## 2. Exact MPFR dyadic conversion — proof under the MPFR/GMP API contract

`mpfr_get_z_2exp(z, x)` extracts, without rounding, an integer `z` and an integral binary exponent `e` satisfying **x = z * 2^e** for the *already directed-rounded finite MPFR value x*. GMP's `__gmpz_get_str` writes `z` in base 10 exactly, which is reconstructed as a Python integer using integer-only parsing. The signed rational is constructed using `Fraction(z << e)` for e>=0 and `Fraction(z, 1 << (-e))` for e<0. Therefore it represents x exactly. Neither a Python float nor an ordinary floating-point transcendental function enters this conversion; numerical excess introduced by this conversion is exactly zero. Signed nonzero values retain their sign; `+0` and `-0` both become the real number zero.

The MPFR/ctypes and GMP/ctypes structures used are the installed x86_64 ABI layouts. The numerical correctness of MPFR/GMP itself is used as a source/library contract, not independently formally verified in Gate 0.6. Calling out with another ABI or backend version fails before use.

The exporter fails closed when p not in [2,8192], the extracted exponent magnitude exceeds 131072, the significand has more than p+2 bits, or the exact input/result numerator or denominator exceeds 262144 bits. A nonfinite input also fails closed. The rules are resource restrictions, not inward approximations, artificial underflow floors or theorem-level numerical tolerances. GMP decimal integers are bounded before buffer allocation. Python's normal 4300-digit decimal limit is *not disabled*: exact rational text is generated and parsed in bounded (1000-digit) integer chunks without changing the exact rational certificate values or schema.

## 3. Fixed Gate-0.5 counterexample — closed at the serialization layer

The exact value exp(-10000) satisfies 0 < exp(-10000) < 2^-10000 < 2^-2048. For each precommitted p in {128,256,512,2048,4096}, both the directed MPFR exp interval and the composed response interval from x=1/100 are strictly positive with upper endpoint below 2^-2048. There is no fixed [0,2^-2048] dyadic-export floor. Their rational end points grow in binary significand precision and retain exact dyadic identity. A 300-or-more-digit independent high-precision comparator was used only to check inclusion, not to construct positive certificates.

The prior negative Gate-0.5 result RB-026 remains historically true for the *old* source and is not relabelled or erased by the new source.

## 4. Primitive arithmetic rate: a conditional mathematical estimate

For an exact scalar real result v within |v|<=M, in supported normal MPFR exponent range, correct directed rounding to p bits has absolute error at most a conservative `2^(ceil(log2 M)+1-p)` (one full ulp bound). Under the fixed numerical domain in the contract, M<=2^18, allowing the deliberately conservative bound `2^20 * 2^-p` for one primitive result. Such a rate holds for finite MPFR operations and exp on the fixed compact arguments *conditional on the declared backend precision/exponent range*. The exact GMP dyadic export adds no rounding error; this eliminates the specific fixed source-level rate blocker.

Division has derivatives bounded when |denominator|>=delta>0. On the frozen rate-segment, psi(s)=exp(-s)/100>1/300 for 0<=s<=1 (since e<3), and `x-h` remains strictly positive. With the explicitly frozen safety hull, the above-threshold square divisor is at least 1/160000. Below-threshold response is identically zero; threshold-straddling response uses monotone [0,S(upper)] without a reciprocal at the threshold. These facts make an elementary bounded derivative propagation estimate *plausible* for the exact real graph, but do not by themselves prove the required global arithmetic excess B_K for the **entire implemented interval-expression graph**.

## 5. Alpha flow, Darboux dependency and prefix arithmetic

A cell evaluates exp(-alpha*t), psi(t)=exp(-alpha*t)*(psi0+t*q0), the threshold-safe response, an outward cell gain Delta*S and a prefix sum. There are 2^n cells at level n and a bounded number of directed arithmetic primitives per cell; a deliberately conservative static operation-count bound is `N_n <= 1024*2^n+1024`, without any runtime profiling or benchmark extrapolation.

This does not establish `E_arith(n)<=B_K*N_n*2^(-p_n)` with the frozen candidate `B_K=2^8192`: that inequality requires a complete nodewise error-propagation proof, including repeated directional reloading of interval endpoints, dependency/range width separation, the threshold-straddling branch, and all subsequent prefix sums, with a bounded constant independent of **unbounded** n and p. An empirical width plot or a bound extracted from a finite dataset cannot supply that proof. Gate 0.6 does not assert such a proof.

## 6. Hard asymptotic implementation limitation: Q4 NOT ESTABLISHED

The fixed refinement formula is `p_n = 128+8*n`, `m_n=2^n`. The repaired implementation enforces `p<=8192`; the core RIFC API additionally rejects `nmax>16`. Thus at n=1009 the formal schedule requires p=8200, outside the software's permitted domain, and already at requested nmax=17 the API fails closed. These are finite resource protections, not finite-rounding inclusion failures.

Consequently **the present code does not implement an unbounded refinement sequence**. No unbounded source-level error propagation constant B_K was proved either. The mathematical RB-024 eventual-certification theorem is conditional on IR-A4-R and a refinement sequence extendable as required. Finite successful results cannot establish the theorem's prerequisites for this implementation. Classification: `IR-A4-R NOT ESTABLISHED`; `EVENTUAL CERTIFICATION DEFERRED`. The hard caps do not refute the mathematical existence of some B_K for a hypothetical suitably extended backend, but prevent claiming a full current-source eventual-certification qualification.

A stronger theorem or subsequent work could (a) prove a detailed whole-expression B_K and (b) formally handle an unbounded precision/refinement abstraction and its resource constraints. Such extensions require a separate preregistered gate; do not silently relax this contract.

## 7. Consequences for permitted tests

R1-R4 exact export, resources, baseline regression and closure of the fixed floor may be executed and were validated. Q6 rate-fit/consistency and Q7 eventual-certification trials are **NOT EXECUTED**, as the frozen contract requires Q4 analytical PASS first. The low-budget finite negative control was exercised as finite-soundness/fail-closed QA, never as evidence about eventual termination.

## 8. Classification and boundary

- SERIALIZATION REPAIR VALIDATED: yes, within exact MPFR/GMP ABI and finite materialization budgets.
- FINITE SOUNDNESS PRESERVED: yes, finite regression and independent proof-data replay.
- IR-A4-R ESTABLISHED: **no**.
- EVENTUAL-CERTIFICATION IMPLEMENTATION VALIDATED: **no**.
- Source/proof qualification: incomplete; B_K and unlimited precision/refinement remain DEFERRED.

No physical simulator replacement, no sequential multi-event/NNE-A, no protected randomness, no CORE v0.27c, no APP-3, no model modification, no scientific speedup/scalability claim, no novelty/manuscript claim.
