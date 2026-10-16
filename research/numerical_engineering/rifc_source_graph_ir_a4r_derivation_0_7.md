# Gate 0.7 — idealized IR-A4-R derivation for the prospectively frozen K_0.7

Date: 2026-10-16. Authority: frozen Gate-0.7 proof contract, commit \`d6b76886663a911a85e4b684825b3047e517b754\`.
Result: **ANALYTICAL G-PASS FOR THE EXPLICIT RESTRICTED IDEALIZED FAMILY K01–K06**, not an executable unlimited-resource promise; no theorem outside these families.

## 1. Exact finite arithmetic model

Let p>=128 and u=2^(1-p)<=2^-127. \`RIFC_infty\` uses the exact graph of Git blob \`1b94cf36447f428a9968c90ac3c0e74c18494d1c\` with only the finite caps on p, GMP materialization, MPFR exponent and nmax removed. MPFR in the idealized model is correctly directed-rounding binary p-bit arithmetic with **unbounded exponent**. A finite nonzero real y rounded in either directed mode obeys
\[
|\operatorname{fl}_p^\pm(y)-y|\le u|y|
\tag{1}
\]
because the adjacent p-bit binade gap is at most \(2^{1-p}|y|\). Zero is exact. This is a property of the correctly-rounded model, **not** a proof of a particular C library implementation.

The source's \`_fraction_round(a/b)\` rounds exact integer numerator/denominator in their required directed mode and then performs directed MPFR division. For any \(b>0\), the integer inputs may have arbitrarily many digits even if \(a/b\) is bounded. Let their relative rounding errors be \(\delta_a,\delta_b\), both of magnitude at most u. The unrounded ratio differs by
\[
\left|\frac{1+\delta_a}{1+\delta_b}-1\right|
\le\frac{2u}{1-u}.
\]
The final directed division multiplies the ratio by \(1+\delta_q\), |\delta_q|<=u. Thus the exact *rational-load composite* has relative error
\[
\left|\frac{\widehat{a/b}}{a/b}-1\right|
\le (1+u)\left(1+\frac{2u}{1-u}\right)-1
<8u \qquad (u\le 1/8).
\tag{2}
\]
Sign-dependent directed numerator/denominator choices preserve outward inclusion; (2) uses absolute errors and applies to signed ratios. This avoids the **invalid** inference that the huge raw GMP integer numerator/denominator parsing operands lie in one compact absolute interval. The semantic primitive \`I.point/I.bounds\` is the correctly enclosed **ratio**, not the underlying unbounded raw parse operands.

\`mpfr_get_z_2exp\` returns the *already rounded* finite MPFR value exactly as z*2^e; integer-to-Fraction and the custom chunked decimal parser/serializer preserve the exact rational endpoint. Its additional arithmetic error is **zero**. Min/max/hull/intersection compare exact Fraction endpoints and add no rounding. The idealized \`I.sqrt\` is not reached by K01–K06 positive first-hit/event/arrival certification; where used separately, it would require a positive sqrt-argument lower bound.

## 2. Prospective data and noncircular compact arithmetic hull

K01/K02: alpha=r=1, h=0, psi0=1/100,q0=0, L=1. K03: alpha=r=1,h=-1,psi0=q0=0,L=4. K04: alpha=r=1,h=1,psi0=q0=0,L=1. K05: direct response intervals below/contact/straddling/above with exact endpoints as frozen. K06: one structural arrival at t=1/2 with W in [-1/16,1/16], alpha=1. Every time-cell endpoint \(kL/2^n\) has a dyadic numerator of at most n+3 bits; \(p_n=128+8n\) represents these endpoints and cell widths \(\Delta=L/2^n\) **exactly**.

A noncircular stability proof is possible using the *actual short alpha/response chains*, before applying the very loose global Lipschitz bound below.

For K01/K02, \(x(s)=e^{-s}/100\), \(0\le s\le1\). Since \(e<3\),
\[
1/300<x(s)\le1/100.
\]
For the interval time cell \([a,b]\), the source computes \(\exp(-[a,b])\) and multiplies it by the point interval \([1/100,1/100]\), with the q0=0 paths exactly zero. The repeated integer loads, exp and multiplication in this *finite depth* expression give at most a \(1\pm 256u\) multiplicative enclosure widening at each nonzero endpoint: each of at most 20 serial relative-rounding stages contributes at most 8u; \((1+8u)^{20}<1+256u\) for \(u\le2^{-127}\). Therefore
\[
x_{\rm computed,lo}>\frac1{300}(1-256u)>\frac1{400}.
\tag{3}
\]
Re-loading an already rounded endpoint and subtracting h=0 may add at most another \(1\pm256u\) factor, still leaving a strict gap above \(1/400\) because the total relative widening is less than 1/4. Thus all above-threshold squaring and division branches have
\[
{\rm gap}_{lo}>1/400,\quad ({\rm gap}^2)_{lo}>1/160000.
\tag{4}
\]
The computed reciprocal magnitude is then bounded by 160000 (an exactly representable integer endpoint). Its negation lies in [-160000,0]. This is inside the fixed source hull \(H=2^{18}=262144\), for every n and \(p_n\ge128\), **without using** the later coarse whole-graph error bound. All exponentials in this branch have nonpositive input and output in [0,1].

K03 is exact input psi=0; h=-1 gives gap=1 and response \(e^{-1}\in(0,1)\). K04 stays exactly below h=1, so response=0. K05 below/contact branches return exact zero, straddling uses the positive upper endpoint \(1/100\) in the *same* away-from-zero top graph, and the strictly above interval has lower >=1/100. The K05 finite loads obey the same relative bound; all reciprocal branches satisfy (4). K06 uses point/interval addition and multiplication with weights magnitude <=1/16 and alpha=1, so endpoints remain in [-1,1]. Every active intermediate belongs to [-H,H]; positive certificate branch selection is stable: no above-positive endpoint crosses threshold due to rounding, the below/straddling labels remain correct, and contact x=0 remains exactly zero.

For each Darboux cell, \(0\le S_{lo}\le S_{hi}\le1\) by the correctly rounded MPFR exponential applied to nonpositive arguments and the exactly representable upper bound 1. The nonnegative cell width \(\Delta=L/2^n\) and \(k\Delta\) for \(k=0,\ldots,2^n\) are exactly representable at \(p_n\). By outward monotonicity of the MPFR operations, each stored gain belongs to [0,Delta], and induction on the source's prefix \`cumulative=cumulative+gain\` gives
\[
0\le {\rm prefix}_{k,lo}\le{\rm prefix}_{k,hi}\le k\Delta\le L\le4.
\tag{5}
\]
Therefore repeated prefix reloading never leaves the fixed scalar hull even for arbitrarily large n. No accumulated rounding-width upper bound was assumed in this stability argument.

## 3. Explicit primitive constants / interval endpoint norm

Use the max absolute displacement of the two interval endpoints relative to the exact **natural interval expression graph** (same input intervals and same stable source branches), not the physical integrand's intrinsic interval/range width. This is the arithmetic-excess metric; dyadic Darboux range dependence is separate.

Let H=2^18, delta=1/160000 and u=2^(1-p). Integer-load/ratio bound (2) gives <=8uH. A local directed arithmetic result of bounded magnitude H has absolute roundoff <=uH. Re-loading two endpoints and rounding one primitive is therefore covered by the prospective per-node additive budget
\[
r_p=2^{24}2^{-p}.
\tag{6}
\]
The real interval endpoint operations have the following l-infinity Lipschitz overbounds on the *proved* compact hull:
- add/sub: 2;
- multiplication: 2H <=2^19;
- nonzero division: delta^-1+H*delta^-2 <2^55;
- exponential: <=1 on nonpositive argument ranges actually reached;
- exact compare/hull/min/max: <=1, with K05 source branch stability as in Section 2;
- unary negation: 1.
The maximum \(\Lambda=2^{80}\) exceeds every required endpoint map constant. A separate sqrt bound is not needed on the frozen positive-certificate paths, which never invoke \`I.sqrt\`.

## 4. Depth, operation count and cell propagation

The code has no recursion in scalar interval operations. Each \`I._op\` evaluates at most 4 endpoint combinations in each of two directed modes (8 calls of \`one\`); one \`one\` performs at most two rational input loads (each <=3 MPFR primitive operations) and one final MPFR primitive, giving <=56 rounded scalar primitives per \`I._op\`. Each point/bounds load performs <=6 primitives, each exp endpoint pair <=8. \`psi_interval\` has at most 3 interval multiplications, 1 addition, 1 exp, and at most 3 point loads, totaling <240 primitives. \`response\` evaluates at most two \`top\` calls; one top contains 1 subtraction, 1 multiplication, 1 division, 1 exp and at most 3 point loads: <160 primitives per top, or <320 for both. Gain + prefix + time-cell bounds total <140. Fixed per-cell total <700, hence safely below the frozen 1024. The longest dependency path is shorter than 512 scalar primitives; in fact it is much shorter since separate endpoints are evaluated in parallel. Thus:
\[
N_n\le1024\,2^n+1024,\qquad N_n\ge2^n.
\tag{7}
\]
The constant overhead includes phase-gap input, final comparisons and a finite certificate wrapper; GMP exact serialization creates no *rounded* arithmetic operations (though its bit complexity is not claimed constant).

Let \(e_j\) denote max endpoint arithmetic perturbation at the jth point on one cell's sequential graph. From (6), \(\Lambda\) and source DAG dependence,
\[
e_{j+1}\le\Lambda e_j+r_p.
\]
For at most 512 nodes and an initial rational loading error <=r_p, the geometric sum gives
\[
E_{\rm cell}\le(513)\Lambda^{512}r_p
<2^{41000}2^{-p}.
\tag{8}
\]
This intentionally enormous bound is permitted *only because* (3)–(5) independently proved that all actual intermediate values stay in the compact source hull. It is not used to justify its own assumptions.

For a prefix of k cells, each next prefix computation adds the independently enclosed cell gain and one directed prefix-add operation, with no nonlinear multiplication of the already accumulated prefix:
\[
E_{\rm prefix}(k)
\le \sum_{i=1}^k(E_{{\rm gain},i}+r_p)
\le k(2^{41000}+2^{24})2^{-p}
<2^{41002}2^n2^{-p}.
\tag{9}
\]
This bound is on arithmetic endpoint excess relative to the exact natural interval prefix graph. The physical Darboux range width, which vanishes by continuity as the mesh shrinks, is not included in \(E_{\rm arith}\).

## 5. Whole-expression IR-A4-R theorem on frozen K

The prospectively frozen constant is \(B_K=2^{65536}\). By (7)–(9), and because every output endpoint of the positive-certificate graph either is a cell/prefix endpoint or belongs to a shorter fixed-depth arithmetic branch,
\[
\boxed{E_{\rm arith}(n)\le B_K\,N_n\,2^{-p_n}},
\quad p_n=128+8n,\quad N_n\le1024\,2^n+1024.
\tag{10}
\]
The inequality uses \(N_n\ge2^n\) for the implemented prefix graph; it is not incorrectly derived merely from an upper bound on N_n. Accordingly,
\[
E_{\rm arith}(n)
\le 2^{65536}(1024\,2^n+1024)2^{-128-8n}
=2^{65536-128}\left(1024\,2^{-7n}+1024\,2^{-8n}\right)\longrightarrow0.
\tag{11}
\]
This proves the **idealized source family's arithmetic-rate obligation on exactly K01–K06**, with the model's unbounded exponent/precision assumptions. The bound is not tight or a practical numerical tolerance. General RIFC families, arbitrarily close above-threshold inputs, unbounded-alpha/gap domains, unproved parameter-family NNE-A and multi-event charts are explicitly outside K.

RB-024's separate eventual strict-margin theorem can therefore be invoked for the *idealized source family* when its stated physical and outward-inclusion hypotheses hold. It does not say every finite request with a small nmax succeeds; resource exhaustion still returns UNCERTIFIED.

## 6. Source correspondence and status

The idealized family makes **no** arithmetic changes except lifting finite production caps for p (8192), exponent (131072), integer size, decimal serialization, and nmax (16). The repaired source uses MPFR directed RNDD/RNDU, exact GMP \`mpfr_get_z_2exp\`, exact Python Fraction operations, dyadic Darboux \`m_n=2^n\`, and identical source branches/strict inequalities. For any exact input whose finite v0.2 computation does not hit a resource cap, ideal and finite implementations produce the same endpoints, event/tape and positive/fail-closed classifications. A finite resource rejection does **not** imply a physical no-hit; it means that executable invocation is out of the finite correspondence domain.

**No executable source was modified.** This proof is an engineering/mathematical qualification of a restricted idealized arithmetic family, not a proof that finite machine memory can execute the n->infinity limit or a new Lighthouse science result.

## 7. Frozen downstream checks

Only after this analytical G-PASS may the prospectively frozen K01–K05 checks run at n={0,2,4,6,8}, requiring correct inclusion/failure classes, bounded endpoint arithmetic errors, full resource accounting, and fail-closed insufficient-budget results. Validations are evidence of correct implementation of the theorem, never its proof and never a way to fit B_K.
