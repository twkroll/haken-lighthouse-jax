# CORE v0.3 Continuation Validation Execution Gate 0.1

Date: 2026-09-07
Status: PASS — V3C01–V3C09 ALL PASS UNDER RB-008

## 1. Git / reproducibility identity

Canonical execution started from:

- repository: `twkroll/haken-lighthouse-jax`
- branch: `main`
- `main` HEAD at execution start and immediately before result write: `956ab9c9f709a006e9789b3151da1f65245d9100`
- governance blob SHA: `7ba28f4c959344930f7b22d10f6f0d5b5163eea9`
- CORE STATUS start blob SHA: `5d9acf4e531ceb63d71af9682b92376ef4c2bb55`
- MASTER STATUS start blob SHA: `17e033dccd17a0845c5cf5f16e28c7f977482135`
- project status v1.6 blob SHA: `1af43394873caec65f330fde9eb5ebbdc1d78ce2`
- execution prompt blob SHA: `9fc65e56c95573dda2b9eff41e285b3e48662909`

No repository state change occurred between the execution authorization check and the result write.

## 2. RB-008 identity

Execution authority:

`CORE v0.3 Continuation Validation Contract Freeze 0.1` / RB-008

- freeze blob SHA: `911acb4c589735e964f5cd25c7f438bacfa0e6e0`
- frozen contract file: `research/core/v0_3_continuation_validation_contract_canonicalization_gate_0_1.md`
- frozen contract blob SHA: `b521aeb48b813fca5197b12e53e751354d60528c`
- contract creation commit: `d611d5e058bfabc34347610a272bf24c9278cf0c`

Underlying authorities remain RB-004, RB-006 and RB-007.

All scientific specifications were kept unchanged.

## 3. Execution environment

Deterministic isolated numerical validation runtime:

- Python `3.13.5`
- NumPy `2.3.5`
- SciPy `1.17.0`
- platform `Linux-6.18.35-x86_64-with-glibc2.41`
- floating-point: IEEE-754 binary64 / `float64`
- quadrature: `scipy.integrate.quad`, `epsabs=1e-13`, `epsrel=1e-13`
- root control in V3C07: deterministic bracketed scalar root on the frozen interval
- randomness: none
- optimizer/search: none

The periodic alpha waveform was evaluated from the exact periodic `(a,q)` state / equivalent closed form; no finite warm-up was used. Integrals involving arrival kinks or `R_T'` were split at analytically known arrivals.

The independent derivative path used exactly the frozen five-point stencil and the fixed steps from RB-008. No step-size scan was performed.

## 4. Harness audit trail

No software-plumbing defect occurred.

No scientific or clerical correction was made after output inspection.

No preliminary failed output was discarded.

No parameter, reference state, derivative convention, finite-difference step, chart margin, solver step, tolerance, benchmark membership, negative control or PASS/FAIL rule was altered.

## 5. V3C01 — coordinate equivalence and global gauge

R0 branch-operator values:

- `F_phi = (-4.475313543276366, -4.486696439112598)`
- `F_chi = (-4.475313543276366, -4.486696439112598)`
- componentwise dimensional/normalized difference: `(0.000e+00, 0.000e+00)`

Gauge shift `c=0.37`:

- shifted `F = (-4.475313543276366, -4.486696439112598)`
- gauge difference: `(0.000e+00, 0.000e+00)`

Both subtests satisfy V3-N2.

**V3C01: PASS**

## 6. V3C02 — phase Jacobian and gauge null

Gauge-fixed `partial F / partial chi_2`:

| component | analytic | five-point reference | analytic-reference |
|---|---:|---:|---:|
| 1 | 0.1010966514704912 | 0.1010966514651083 | 5.383e-12 |
| 2 | 0.2115810625555109 | 0.2115810625961482 | -4.064e-11 |

Ungauged analytic phase-column sum:

`(2.776e-17, 0.000e+00)`

Independent numerical phase-column sum:

`(-7.401e-12, 7.401e-12)`

Minimum chart margin over every required phase-stencil point:

`0.0954929658551372 >= 0.05`

No null identity was imposed by explicit numerical zeroing.

**V3C02: PASS**

## 7. V3C03 — fixed-physical-delay period derivative and scalar coupling derivative

### V3C03-A period derivative

| component | analytic | five-point reference | analytic-reference |
|---|---:|---:|---:|
| 1 | 0.3960486918856531 | 0.3960486918848834 | 7.697e-13 |
| 2 | 0.396197589250181 | 0.3961975892496916 | 4.894e-13 |

Physical delays were held unchanged. As a direct negative-control audit, the dimensionless ratio for `tau_11=0.3` changed from

- `tau_11/(T-2h_T) = 0.0954990455131988`
- `tau_11/(T+2h_T) = 0.09548688697111243`

so the harness did not silently hold `tau/T` fixed.

Minimum period-stencil arrival-chart margin:

`0.09548688697111243 >= 0.05`

### V3C03-B scalar coupling `w_12(p)=0.35+p`

| component | analytic | five-point reference | analytic-reference |
|---|---:|---:|---:|
| 1 | 0.4749303477758477 | 0.4749303477602495 | 1.560e-11 |
| 2 | 0 | 7.401486830834376e-12 | -7.401e-12 |

Coupling stencils leave arrival geometry unchanged; margin is `0.0954929658551372`.

**V3C03: PASS**

## 8. V3C04 — synthetic pseudo-arclength fold

E0 fold matrix:

`[[0,-1],[-1,0]]`

with determinant `-1`, hence nonsingular.

Execution used exactly `Delta s=0.05`, exactly 20 predictor/corrector steps and no adaptive step resize.

| step | x | p | `|x^2-p|` | corrector `||G||_2` | Newton updates |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.3601832048061829 | 0.1297319410243607 | 0.000e+00 | 4.626e-17 | 2 |
| 2 | 0.3188013892657372 | 0.1016343257976583 | 1.388e-17 | 1.475e-17 | 2 |
| 3 | 0.2758182707161332 | 0.07607571834477276 | 0.000e+00 | 2.156e-17 | 2 |
| 4 | 0.2311476435371381 | 0.05342922897037299 | 6.939e-18 | 7.344e-18 | 2 |
| 5 | 0.1847171790745454 | 0.03412044597935734 | 0.000e+00 | 1.197e-17 | 2 |
| 6 | 0.1364763132158233 | 0.01862578409624549 | 0.000e+00 | 1.388e-17 | 2 |
| 7 | 0.08640775977357955 | 0.007466297002113074 | 8.674e-19 | 8.674e-19 | 2 |
| 8 | 0.03552783130739044 | 0.001262206792166684 | 0.000e+00 | 1.093e-17 | 2 |
| 9 | -0.01117128315285151 | 0.0001247975672811754 | 1.355e-20 | 1.388e-17 | 2 |
| 10 | -0.06109075971989375 | 0.003732081941374784 | 4.337e-19 | 1.389e-17 | 2 |
| 11 | -0.1105351383800707 | 0.01221799981636352 | 1.735e-18 | 1.735e-18 | 2 |
| 12 | -0.1588821032759843 | 0.02524351925685298 | 3.469e-18 | 4.221e-18 | 2 |
| 13 | -0.2056420691897014 | 0.0422886606100082 | 0.000e+00 | 3.851e-17 | 2 |
| 14 | -0.2504693726034202 | 0.06273482366344956 | 0.000e+00 | 3.687e-17 | 2 |
| 15 | -0.2931589597021926 | 0.08594217683034342 | 1.388e-17 | 1.627e-17 | 2 |
| 16 | -0.3336290375350137 | 0.1113083456439027 | 0.000e+00 | 5.287e-17 | 2 |
| 17 | -0.3718950793763569 | 0.1383059460740115 | 2.776e-17 | 2.896e-17 | 2 |
| 18 | -0.4080479705400089 | 0.1665031443300521 | 0.000e+00 | 3.362e-17 | 2 |
| 19 | -0.4422307916952752 | 0.1955670981586634 | 2.776e-17 | 2.776e-17 | 2 |
| 20 | -0.474608273131739 | 0.2252529991582197 | 2.776e-17 | 2.776e-17 | 2 |

Summary:

- maximum Newton updates: `2` <= 12
- maximum corrected branch residual: `2.776e-17`
- maximum corrector residual: `5.287e-17`
- first negative accepted point: step `9`, `(x,p)=(-0.01117128315285151, 0.0001247975672811754)`
- final point: `(x,p)=(-0.474608273131739, 0.2252529991582197)`
- discarded/resized steps: none

No Lighthouse branch was used.

**V3C04: PASS**

## 9. V3C05 — exchange-symmetric two-cell structure and corrected B

At `chi=+0.07`:

`(F_+,F_-)=(-4.508819514524995, 0.01111369047007127)`

At `chi=-0.07`:

`(F_+,F_-)=(-4.508819514524995, -0.01111369047007127)`

Parity residuals:

- `F_+(-chi)-F_+(chi) = 0.000e+00`
- `F_-(-chi)+F_-(chi) = 0.000e+00`

Synchrony/block controls:

- `F_-(T,0) = 0.000e+00`
- `partial_chi F_+(T,0)` five-point = `-1.480e-11`
- `partial_T F_-(T,0)` five-point = `0.000e+00`

Antisymmetric coefficient:

- `B_analytic = 0.1655741803759718`
- `B_FD = 0.165574180418145`
- difference = `-4.217e-11`

E0 chain-rule audit retained the frozen **negative prefactor** in

`B = -T^2 w_c integral S'(Psi_0) R_T'(...) d sigma`.

The numerical value of B is positive for this predetermined state because the integral itself has the corresponding sign; this does not alter the E0 prefactor audit.

No Lighthouse pitchfork claim is made.

**V3C05: PASS**

## 10. V3C06 — synthetic pitchfork algebra

E0 controls all hold: even/odd parity, synchronous branch, zero antisymmetric linear coefficient at `p=0`, `a=1`, `b=-1`, and exact `chi^2=p` nontrivial branches.

| p | chi | F_plus | F_minus | `chi^2-p` | result |
|---:|---:|---:|---:|---:|---|
| 1e-04 | -0.01 | 0.000e+00 | -0.000e+00 | 0.000e+00 | PASS |
| 1e-04 | 0.01 | 0.000e+00 | 0.000e+00 | 0.000e+00 | PASS |
| 1e-03 | -0.03162277660168379 | 0.000e+00 | -6.857e-21 | -2.168e-19 | PASS |
| 1e-03 | 0.03162277660168379 | 0.000e+00 | 6.857e-21 | -2.168e-19 | PASS |
| 1e-02 | -0.1 | 0.000e+00 | 1.735e-19 | 1.735e-18 | PASS |
| 1e-02 | 0.1 | 0.000e+00 | -1.735e-19 | 1.735e-18 | PASS |

No inference about a Lighthouse pitchfork is made.

**V3C06: PASS**

## 11. V3C07 — first hitting and transversality

Frozen isolated clock:

- `v=e^-1 = 0.3678794411714423`
- exact `T0=2*pi*e = 17.07946844534713`
- deterministic first hit = `17.07946844534713`
- first-hit error = `0.000e+00`
- accumulated phase at `sigma=1` = `6.283185307179586`
- endpoint phase residual = `0.000e+00`

Because the positive case has constant `v>0`, accumulated phase is strictly monotone and is strictly below `2*pi` for every `sigma<1`.

Premature-event negative control:

- `T_bad = 18.07946844534713`
- classification: rejected because first hitting occurred at `T0 < T_bad`

Nontransversal negative control:

- `h=0`, `psi=0`, `S(0)=0.0`
- exact classification: `NON-TRANSVERSAL / NO-EVENT`
- no finite event time or derivative was manufactured

**V3C07: PASS**

## 12. V3C08 — arrival-aware integration and chart qualification

Integrated periodic mass:

| unwrapped a | wrapped a | J(a) | J(a)-1 | quadrature error estimate | result |
|---:|---:|---:|---:|---:|---|
| -0.001 | 0.999 | 1 | 0.000e+00 | 1.110e-14 | PASS |
| +0 | 0 | 0.99999999999999989 | -1.110e-16 | 1.110e-14 | PASS |
| +0.001 | 0.001 | 1 | 0.000e+00 | 1.110e-14 | PASS |
| +0.4 | 0.4 | 1 | 0.000e+00 | 1.110e-14 | PASS |

Off-boundary fixed-stencil derivatives:

| a | five-point `dJ/da` | reference | rule | result |
|---:|---:|---:|---|---|
| -0.001 | 0.000e+00 | 0 | 5e-7 absolute | PASS |
| +0.001 | 1.850e-12 | 0 | 5e-7 absolute | PASS |
| +0.4 | 1.480e-11 | 0 | 5e-7 absolute | PASS |

At exactly `a=0`:

- pointwise classical arrival-kink derivative classification: `ARRIVAL_CHART_BOUNDARY / DERIVATIVE_INVALID`
- this is the one explicitly allowed case-level INVALID classification
- integrated `J(0)=0.99999999999999989` remains valid and passes V3-N2

No physical/existence singularity was inferred from the wrapped arrival chart change.

**V3C08: PASS**

## 13. V3C09 — exact regular autapse branch sensitivity

Reference branch:

`F(T,w)=pi*w+T-2*pi`

At `T=pi`, `w=1`, `tau=pi/3`:

- implementation `F = 0.000e+00`
- `F_T = 1.0000000000000004`
- `F_w = 3.141592653589793`
- `F_tau = -1.788e-15`

Weight sensitivity:

- implicit `-(F_T)^-1 F_w = -3.141592653589792`
- exact reference `-pi = -3.141592653589793`
- error = `1.332e-15`
- centered exact-branch slope with `h_w=1e-4`: `-3.141592653590486`
- centered slope error = `-6.928e-13`

Fixed-delay sensitivity:

- `F_tau = -1.788e-15`
- centered branch-period sensitivity = `0.000e+00`

Branch-pair residuals:

- weight minus: `8.882e-16`
- weight plus: `-8.882e-16`
- delay minus: `-1.776e-15`
- delay plus: `1.776e-15`

Strict positive phase velocity is preserved analytically because the periodic alpha comb is positive and `S_L=pi*psi+1>1>0`.

**V3C09: PASS**

## 14. Complete suite

| family | result |
|---|---|
| V3C01 | PASS |
| V3C02 | PASS |
| V3C03 | PASS |
| V3C04 | PASS |
| V3C05 | PASS |
| V3C06 | PASS |
| V3C07 | PASS |
| V3C08 | PASS |
| V3C09 | PASS |

Overall governed execution:

`PASS — V3C01–V3C09 ALL PASS UNDER RB-008`

## 15. Failures / INVALID / blockers

Scientifically valid failures: none.

Execution blockers: none.

Required INVALID classification:

- V3C08 at exactly `a=0`: `ARRIVAL_CHART_BOUNDARY / DERIVATIVE_INVALID` for the requested pointwise classical kink derivative.
- This does not invalidate the integrated `J(0)` check and is exactly the categorical behavior frozen by RB-008.

No other case was classified INVALID.

## 16. Tuning statement

No tuning occurred.

After output inspection there was:

- no parameter retuning;
- no point replacement;
- no derivative-step change;
- no tolerance change;
- no chart-margin change;
- no solver-step change;
- no benchmark omission;
- no negative-control removal;
- no objective or success-criterion change;
- no Lighthouse branch / fold / pitchfork search.

## 17. Overall gate decision

**PASS**

Reason: every required V3C01–V3C09 family, every fixed subcase and every frozen negative/categorical control satisfied RB-008 exactly as specified.

PASS validates only the governed deterministic C2 validation layer tied to RB-007. It does not broaden the frozen theory and does not promote downstream legacy effects.

## 18. Proposed MASTER result-freeze contents

If MASTER accepts this execution, CORE proposes a narrow:

`CORE v0.3 Continuation Validation Result Freeze 0.1`

containing only:

1. the exact execution artifact and reproducibility identity above;
2. `PASS — V3C01–V3C09 ALL PASS UNDER RB-008`;
3. the recorded derivative errors, chart margins, synthetic-fold residuals, parity/B comparison, event controls, V3C08 INVALID classification and exact autapse sensitivities;
4. the statement that no frozen scientific specification was changed after output inspection;
5. all RB-008 exclusions unchanged.

The proposed result freeze must not include any Lighthouse continuation branch, fold/pitchfork location, v0.4 stability object or downstream effect.

## 19. Explicit exclusions

This execution does not validate, compute, promote or authorize:

- any Lighthouse continuation search;
- any Lighthouse fold or pitchfork location/scaling;
- any v0.4 Floquet/multiplier/stability result;
- saltation claims beyond the frozen elementary event layer;
- hard-threshold tests for the smooth baseline;
- adaptive-delay or commensurability effects;
- production/JAX continuation performance;
- normal-form fitting or effect-bearing critical coefficients;
- v0.4+ legacy recovery execution;
- inference, observation design, active experiment design;
- applications, novelty, manuscript claims or v0.27.

## 20. STOP

The authorized V3C01–V3C09 execution is complete.

No second CORE gate was started.

STOP — RETURN TO MASTER
