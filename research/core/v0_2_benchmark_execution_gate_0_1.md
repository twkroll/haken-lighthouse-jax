# CORE v0.2 Benchmark Execution Gate 0.1

Date: 2026-09-07
Status: PASS — BC01–BC10 EXECUTED UNDER RB-005; NO CONTRACT CHANGE

## 1. Git / reproducibility identity

- Repository: `twkroll/haken-lighthouse-jax`
- Canonical branch: `main`
- `main` HEAD at execution start: `d7d7303645e248e082363cec2b7ddd24bd0dd50d`
- Execution prompt blob SHA: `9e3eca9f603e4d2fcbfb8af0a8f598252f33d236`
- Governance blob SHA: `7ba28f4c959344930f7b22d10f6f0d5b5163eea9`
- CORE STATUS start blob SHA: `dff56d14b34e4e323f7b31f197ba8b4d0d88e505`
- MASTER STATUS start blob SHA: `f338d4e6e74bb17a10a492f2337dd2b73b06cef9`
- Project status v1.3 blob SHA: `851199d5b029266817a3b994304d17fa119e153b`
- Decision / branch log blob SHA: `281c5e48179eb9608e3002e887b10e974297a2d4`
- `CORE Mathematical Freeze 0.1` / RB-004 blob SHA: `d84a2f8c23b0bb0d6be4867a42a6fea235232f20`
- Frozen mathematical source blob SHA: `d34ba1129dfca892e76342f3c2d66b6b493535dd`
- `CORE Benchmark Contract Freeze 0.1` / RB-005 blob SHA: `ddf8d56099f392fbadfff30d7c4246831fb5cec7`
- Frozen benchmark-contract source blob SHA: `bfe0f23ac8c80d47aaf8c1c18ffd765689a64a33`

RB-005 was not modified. No v0.3+ legacy result or value was used as an execution reference.

## 2. Execution environment

- Python: `3.13.5`
- Linux: `6.18.35-x86_64`, glibc `2.41`
- NumPy: `2.3.5`
- SciPy: `1.17.0`
- SymPy: `1.14.0`
- Numeric precision: IEEE-754 binary64 / float64
- Deterministic quadrature: `scipy.integrate.quad`, with frozen `epsabs=1e-13`, `epsrel=1e-13` where specified
- Deterministic first-hit roots: `scipy.optimize.brentq`
- Alpha flow: binary64 matrix exponential of the frozen 2×2 `(a,q)` state-space flow using `scipy.linalg.expm`
- Symbolic / algebraic checks: SymPy plus exact algebra against RB-004 identities

## 3. Method notes and harness audit trail

All fixed parameter sets, grids, histories, horizons, observables, references and acceptance rules were taken from RB-005 unchanged.

For delayed periodic first-hit calculations, the cumulative alpha comb was evaluated with the exact primitive of the frozen periodic comb. With `rho=exp(-alpha*T)`,

\[
C_\alpha(u)=\frac{1-e^{-\alpha u}(1+\alpha u)}{1-\rho}
+\frac{\alpha T\rho(1-e^{-\alpha u})}{(1-\rho)^2},
\]

extended periodically by `H(x+T)=H(x)+1`. This is algebraically the integral of the frozen D3 comb. Contract-specified quadrature remained in use for residuals / integrals.

### Harness correction

An initial harness attempt placed adaptive-quadrature evaluations directly inside an endpoint-bracketed root solver. For a reference event exactly at the right endpoint, a quadrature residual that is scientifically within the frozen tolerance can have the same floating-point sign as the left endpoint, causing the root library to reject the bracket before a scientific PASS/FAIL classification.

Classification: **software-plumbing defect**, not a scientific-specification defect.

Correction: use the exact closed-form primitive of the already frozen periodic alpha comb inside first-hit root functions. Benchmark membership, parameters, histories, horizons, method classes, observables, references, tolerances, pass/fail rules and negative controls were unchanged. No output from the aborted harness attempt was used as scientific evidence. The complete suite below was then executed from the beginning.

## 4. BC01 — alpha-kernel normalization

Prescribed domain: symbolic `alpha>0`.

Observed symbolic result:

\[
\int_0^\infty \alpha^2 t e^{-\alpha t}\,dt=1.
\]

Reference: `1`. Error: exact zero. Rule: E0 exact equality. Admissibility: `alpha>0`.

**BC01: PASS.**

## 5. BC02 — impulse / state-space equivalence

Prescribed input: `alpha=2`, one spike at `t=0`, `a(0-)=q(0-)=0`, post-jump `(a,q)=(0,4)`. Evaluated at all 257 frozen points on `[0,2]`.

Reference:

\[
a(t)=4te^{-2t},\qquad q(t)=4e^{-2t}.
\]

Observed maximum absolute errors:

- `a`: `4.515832152662824e-14`
- `q`: `2.0761170560490427e-14`
- `a(0+)`: observed `0`, error `0`
- `q` jump: observed `4`, error `0`

Rule: N1 at every point and on continuity / jump. Exactly one spike and no extra input were used.

**BC02: PASS.**

## 6. BC03 — periodic alpha comb and unit mass

Prescribed input: `alpha=2`, `T=pi`, exact infinite periodic history. Evaluated at all 513 frozen points on `[0,pi)`.

Observed maximum pointwise comb error: `4.421463195569686e-14`.

One-period mass:

- observed: `0.9999999999999875`
- reference: `1`
- absolute error: `1.2545520178264269e-14`
- quadrature-reported absolute error estimate: `1.1102230246251427e-14`

Rule: N1 pointwise, N2 mass, internal quadrature `1e-13/1e-13`.

**BC03: PASS.**

## 7. BC04 — periodic hybrid alpha state / closure

Prescribed `alpha=2`, `T=pi`, exact post-spike periodic state. Evaluated at all 257 frozen points on `[0,T)` plus explicit `T-` and `T+`.

Observed:

- maximum pointwise state error: `4.399258735077183e-14`
- `a` continuity error: `0`
- `q` jump: `4`, error `0`
- post-cycle closure vector: `[0.0, 0.0]`
- Euclidean closure norm: `0`

Rule: N1 pointwise / continuity / jump, N2 state closure.

**BC04: PASS.**

## 8. BC05 — isolated-clock identity

### BC05-A — baseline response

- observed first hit: `17.079468445347132`
- reference `2*pi*e`: `17.079468445347132`
- absolute error: `0`
- N1 allowed error: `1.7089468445347133e-09`
- no earlier crossing: yes, by strict positive constant phase velocity

**BC05-A: PASS.**

### BC05-B — linear analytical variant

- observed first hit: `6.283185307179586`
- reference `2*pi`: `6.283185307179586`
- absolute error: `0`
- N1 allowed error: `6.293185307179587e-10`
- no earlier crossing: yes

**BC05-B: PASS.**

**BC05 overall: PASS.**

## 9. BC06 — delayed-autapse period identity

Fixed parameters: `w=1`, `gamma=pi`, `Theta=-1`, `T_ref=pi`. All nine frozen Cartesian-product cases were retained.

| alpha | tau | F residual | quadrature error estimate | first hit | period abs. error | result |
|---:|---:|---:|---:|---:|---:|---|
| 0.2 | 0 | 0 | `6.975736996017264e-14` | `3.141592653589793` | 0 | PASS |
| 0.2 | `1.0471975511965976` | `8.881784197001252e-16` | `6.208367153703875e-13` | `3.141592653589793` | 0 | PASS |
| 0.2 | `4.71238898038469` | `8.881784197001252e-16` | `6.975670041597937e-14` | `3.141592653589793` | 0 | PASS |
| 2 | 0 | 0 | `6.975736996017264e-14` | `3.141592653589793` | 0 | PASS |
| 2 | `1.0471975511965976` | `8.881784197001252e-16` | `6.975736996017264e-15` | `3.141592653589793` | 0 | PASS |
| 2 | `4.71238898038469` | 0 | `6.972200594645983e-14` | `3.141592653589793` | 0 | PASS |
| 20 | 0 | 0 | `6.937675118787336e-14` | `3.141592653589793` | 0 | PASS |
| 20 | `1.0471975511965976` | 0 | `1.305622276959184e-13` | `3.141592653589793` | 0 | PASS |
| 20 | `4.71238898038469` | `1.7763568394002505e-15` | `6.976021224104846e-14` | `3.141592653589793` | 0 | PASS |

All cases are transversal because `S_L(x)=pi*x+1>=1` for the nonnegative comb.

Rule: N2 on `F`, N1 on first-hit time; all nine cases required.

**BC06: PASS.**

## 10. BC07 — phase-locked self-consistency and global gauge

The frozen two-neuron matrix, offsets, delays, `alpha=2`, `T=pi` and gauge shift `c=0.37*pi` were used unchanged.

Observed:

- unshifted residual vector: `[0.0, 0.0]`
- shifted residual vector: `[0.0, 0.0]`
- componentwise gauge absolute difference: `[0.0, 0.0]`
- quadrature error estimates before shift: `[6.975736996017264e-14, 6.975736996017264e-14]`
- after shift: `[6.975736996017264e-14, 6.975736996017264e-14]`

Rule: N2 residuals before and after gauge shift; gauge difference `<=1e-11` componentwise. Positive weights give `S_L=pi*psi+1>0`, hence transversality.

**BC07: PASS.**

## 11. BC08 — linear row-sum identity

BC08-A uses `Gamma=1`, `T=pi`; BC08-B uses `Gamma=0`, `T=2*pi`. The three frozen dimensionless `(alpha*T,tau/T)` pairs were executed in both subcases.

| subcase | alpha*T | tau/T | alpha | tau | phase residual | first hit | period abs. error | cancellation residual | result |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| A | 0.5 | 0 | `0.15915494309189535` | 0 | 0 | `3.141592653589793` | 0 | — | PASS |
| A | `6.283185307179586` | 0.5 | 2 | `1.5707963267948966` | 0 | `3.141592653589793` | 0 | — | PASS |
| A | 20 | 1.5 | `6.366197723675814` | `4.71238898038469` | 0 | `3.141592653589793` | 0 | — | PASS |
| B | 0.5 | 0 | `0.07957747154594767` | 0 | 0 | `6.283185307179586` | 0 | 0 | PASS |
| B | `6.283185307179586` | 0.5 | 1 | `3.141592653589793` | 0 | `6.283185307179586` | 0 | 0 | PASS |
| B | 20 | 1.5 | `3.183098861837907` | `9.42477796076938` | 0 | `6.283185307179586` | 0 | 0 | PASS |

Rule: N1 on period, N2 on phase increment and balanced cancellation; all six cases required. All cases are transversal.

**BC08: PASS.**

## 12. BC09 — first hitting / admissibility

Positive reference:

- `T=2*pi*e = 17.079468445347132`
- observed accumulated phase at `T`: `6.283185307179586`
- absolute equality error to `2*pi`: `0`
- no crossing on `(0,T)`: yes, by strict monotonicity
- true candidate: ACCEPTED

Negative control:

- `T_bad=2*pi*e+1 = 18.079468445347132`
- result: REJECTED
- rejection reason: first hitting already occurred at `2*pi*e`

This is the contract-required L0 rejection, not an INVALID reclassification.

**BC09: PASS.**

## 13. BC10 — elementary event-time perturbation

Reference velocity: `v=e^-1>0`. Fixed perturbations `+1e-4` and `-1e-4`.

| epsilon | observed event time | reference event time | event abs. error | observed delta T | reference delta T | delta abs. error | result |
|---:|---:|---:|---:|---:|---:|---:|---|
| `+1e-4` | `17.07919661716429` | `17.07919661716429` | 0 | `-0.00027182818284288146` | `-0.00027182818284590454` | `3.023080917541332e-15` | PASS |
| `-1e-4` | `17.07974027352998` | `17.07974027352998` | 0 | `0.0002718281828464342` | `0.00027182818284590454` | `5.296327612591689e-16` | PASS |

Both perturbations preserve the same regular event section and satisfy N1.

Transversality negative control: `h=0`, `r=1`, `psi=0` gives `S(0)=0`. Observed status: `NON-TRANSVERSAL / NO-EVENT`; no finite next event, no division by zero, and no derivative returned.

**BC10 negative control: PASS.**

**BC10 overall: PASS.**

## 14. E0 symbolic / algebraic audit

All E0 components were checked independently of numerical tolerances:

1. BC01: normalized alpha-kernel integral equals one for `alpha>0`.
2. BC02: `q=alpha^2 exp(-alpha t)`, `a=alpha^2 t exp(-alpha t)` satisfies the frozen flow and jump exactly.
3. BC03: the geometric-series comb formula and one-period unit-mass identity reduce algebraically to D1–D3.
4. BC04: the prescribed post-spike periodic state satisfies the exact one-cycle fixed-point equations before and after `q+=alpha^2`.
5. BC05: constant velocity gives `T=2*pi/S(0)` exactly.
6. BC06: the shifted periodic comb has unit mass over a full period, hence the prescribed linear autapse gives `T=pi` exactly.
7. BC07: only offset differences occur and both row sums are one, so the common gauge shift cancels exactly and both residuals vanish.
8. BC08: D14 gives `T=pi` for `Gamma=1`; D15 gives `T=2*pi` for `Gamma=0`; the balanced synchronous input cancels exactly.
9. BC09: strict positive constant velocity makes `2*pi*e` the unique first hit, so `T_bad` necessarily contains an earlier crossing.
10. BC10: `T(epsilon)=(2*pi-epsilon)/v`, `delta T=-epsilon/v` exactly; at `S(0)=0`, D18 is undefined.

## 15. Complete suite summary

| Benchmark | Required cases / controls | Result |
|---|---:|---|
| BC01 | symbolic domain | PASS |
| BC02 | 257 points + jump / continuity | PASS |
| BC03 | 513 points + mass integral | PASS |
| BC04 | 257 points + `T-` / `T+` closure | PASS |
| BC05 | 2 subcases | PASS |
| BC06 | 9 fixed alpha / delay cases | PASS |
| BC07 | unshifted + gauge-shifted residuals | PASS |
| BC08 | 6 fixed synchronous cases | PASS |
| BC09 | positive + negative control | PASS |
| BC10 | 2 perturbations + transversality negative control | PASS |

No required fixed case, subcase or negative control was omitted.

\[
\boxed{\text{BC01--BC10: ALL PASS}}
\]

## 16. Failures / tuning statement

No scientifically valid benchmark failure occurred.

No parameter, finite test set, history, horizon, grid / resolution, method class, quadrature tolerance, acceptance tolerance, observable, reference, pass/fail rule or negative control was relaxed, replaced, added or removed after output inspection.

The single harness correction is recorded in Section 3 and did not change RB-005. No result was tuned away.

## 17. Overall gate decision

\[
\boxed{\text{PASS}}
\]

Every required BC01–BC10 benchmark, fixed subcase and required negative control passes under RB-005.

This PASS validates only the governed first analytical benchmark layer against RB-004. It does not promote or validate v0.3–v0.26 legacy numerical, implementation, inference or active-design results.

## 18. Proposed result-freeze contents

CORE proposes that MASTER may establish a narrow `CORE v0.2 Benchmark Result Freeze 0.1` containing:

1. the immutable RB-004 and RB-005 identities used here;
2. the complete BC01–BC10 execution record in this file;
3. the execution environment and method notes;
4. PASS of every required BC01–BC10 subcase and negative control;
5. the harness audit trail;
6. the explicit boundary that no v0.3+ claim is promoted.

CORE does not authorize that result freeze itself.

## 19. STOP

Do not execute a second gate, v0.3+ recovery, production implementation, active experiment design, v0.27, application work or novelty work.

STOP — RETURN TO MASTER
