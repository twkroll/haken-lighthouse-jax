# CORE v0.3 Continuation Validation Execution Gate 0.1

Date: 2026-09-07
Status: PASS — V3C01–V3C09 ALL PASS UNDER RB-008

## 1. Git / reproducibility identity

Canonical execution started from:

- repository: `twkroll/haken-lighthouse-jax`
- branch: `main`
- `main` HEAD at execution start and immediately before the initial result write: `956ab9c9f709a006e9789b3151da1f65245d9100`
- preliminary result creation commit: `872199d6f885489898d64ac8bf957c629770d249`
- preliminary RETURN-TO-MASTER status commit: `02da2d7c68e0a631c9cb42941860e25450c5f127`
- governance blob SHA: `7ba28f4c959344930f7b22d10f6f0d5b5163eea9`
- CORE STATUS start blob SHA: `5d9acf4e531ceb63d71af9682b92376ef4c2bb55`
- MASTER STATUS start blob SHA: `17e033dccd17a0845c5cf5f16e28c7f977482135`
- project status v1.6 blob SHA: `1af43394873caec65f330fde9eb5ebbdc1d78ce2`
- execution prompt blob SHA: `9fc65e56c95573dda2b9eff41e285b3e48662909`

No repository state change occurred between the execution authorization check and the initial result write. A subsequent clerical result-transcription defect was then found during post-write audit and corrected under the frozen RB-008 software-plumbing rule as documented in Section 4.

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

One clerical/software-plumbing defect was detected **after the first result document had been committed**.

### Defect

The manually transcribed 20-row V3C04 pseudo-arclength table in preliminary result commit

`872199d6f885489898d64ac8bf957c629770d249`

did not match the actual deterministic V3C04 harness arrays. This was a result-serialization/transcription error only; the numerical V3C04 computation itself and all other validation families were unaffected.

### Affected path

Only the human-readable V3C04 result-table serialization was affected. No common scientific computation path, alpha waveform, quadrature, derivative evaluator, event control or other V3C family shared this transcription defect.

### Correction

The V3C04 family was rerun **from the beginning** under the unchanged frozen RB-008 contract:

- same synthetic equation `x^2-p=0`;
- same start `(0.4,0.16)`;
- same initial tangent;
- same fixed `Delta s=0.05`;
- exactly 20 predictor/corrector steps;
- same Newton target and iteration cap;
- no step resizing;
- no parameter/tolerance/reference change.

The rerun was bitwise identical to the original in-memory deterministic V3C04 harness output. The corrected table in Section 8 is generated directly from that rerun output.

### Invalidated preliminary output

Only the incorrect V3C04 table and summary numbers in preliminary commit `872199d6f885489898d64ac8bf957c629770d249` are invalidated as a scientific record. They are retained in Git history as the audit trail and are not used as evidence.

The corrected V3C04 rerun remains PASS under the original RB-008 criteria.

No scientific specification was changed after output inspection. There was:

- no parameter retuning;
- no reference-state change;
- no derivative-step change;
- no chart-margin change;
- no solver-step change;
- no tolerance change;
- no benchmark membership change;
- no negative-control change;
- no PASS/FAIL rule change.

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
| 1 | 0.3601832048061829 | 0.1297319410243607 | 9.198e-14 | 9.198e-14 | 2 |
| 2 | 0.3188013892657372 | 0.1016343257976583 | 1.058e-13 | 1.058e-13 | 2 |
| 3 | 0.2758039148150347 | 0.0760677994271893 | 1.096e-13 | 1.096e-13 | 2 |
| 4 | 0.2311807385603068 | 0.05344453388119191 | 9.701e-14 | 9.701e-14 | 2 |
| 5 | 0.1849840409065581 | 0.03421909539005116 | 6.800e-14 | 6.800e-14 | 2 |
| 6 | 0.1373521378557469 | 0.01886560977351062 | 3.348e-14 | 3.348e-14 | 2 |
| 7 | 0.08852936818383095 | 0.007837449031018875 | 9.425e-15 | 9.425e-15 | 2 |
| 8 | 0.0388718212019997 | 0.001511018483559254 | 9.795e-16 | 9.795e-16 | 2 |
| 9 | -0.01117128315285151 | 0.0001247975672811754 | 8.511e-18 | 8.531e-18 | 2 |
| 10 | -0.06110313160815999 | 0.003733592692324119 | 4.337e-19 | 2.498e-18 | 2 |
| 11 | -0.1104408048933147 | 0.01219717138548311 | 1.041e-16 | 1.041e-16 | 2 |
| 12 | -0.1587720218098005 | 0.02520855490956926 | 2.498e-15 | 2.498e-15 | 2 |
| 13 | -0.2057894098422015 | 0.04234928120318855 | 1.303e-14 | 1.303e-14 | 2 |
| 14 | -0.2512974415905195 | 0.06315040414990776 | 3.279e-14 | 3.279e-14 | 2 |
| 15 | -0.2951990041837309 | 0.0871424520710127 | 5.368e-14 | 5.368e-14 | 2 |
| 16 | -0.3374725995499198 | 0.1138877554469138 | 6.671e-14 | 6.671e-14 | 2 |
| 17 | -0.3781488607096066 | 0.1429965608559044 | 6.911e-14 | 6.911e-14 | 2 |
| 18 | -0.4172908799576025 | 0.1741316784957269 | 6.337e-14 | 6.337e-14 | 2 |
| 19 | -0.454979599668773 | 0.2070064361147034 | 5.357e-14 | 5.357e-14 | 2 |
| 20 | -0.4913038181530882 | 0.2413794417317599 | 4.285e-14 | 4.285e-14 | 2 |

Summary:

- maximum Newton updates: `2` <= 12
- maximum corrected branch residual: `1.096e-13`
- maximum corrector residual: `1.096e-13`
- first negative accepted point: step `9`, `(x,p)=(-0.01117128315285151, 0.0001247975672811754)`
- final point: `(x,p)=(-0.4913038181530882, 0.2413794417317599)`
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
