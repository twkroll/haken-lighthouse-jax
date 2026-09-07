# CORE v0.27 Hierarchical Repeated-Trial Execution Gate 0.1

Date: 2026-09-07
Status: SCIENTIFIC FAIL — C2 PASS; CONSERVATIVE SHARED INFORMATION PASS; FROZEN LAPLACE INFERENCE HAS NO FINITE INITIAL OUTER START ON ANY OF 32 DATASETS

## 1. Authority, Git identity, and frozen inputs

This is the governed effect-bearing execution of the MASTER-authorized `CORE v0.27 Hierarchical Repeated-Trial Execution Gate 0.1`.

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- governed execution start / pre-write HEAD: `ff901e0a0b554891dc5fba4f12c6bcd781de3a7d`
- CORE STATUS blob at execution: `624ede037f55421a97c68b35e09bf685744cb4bd`
- execution prompt blob: `dec6e08e2708fb6647764cb9a486529b532034c6`
- governance blob: `1db949ed6fe0a6c4a82b8b6f97086ece9d2672f0`
- MASTER STATUS blob: `e0b5cdb9092cac8871adfadd59eacf52def33e56`
- MASTER project-status blob: `c8cefa82c75efd20081246d2564e055ec88e0799`
- MASTER decision-log blob: `6defb37c8a28fc6aae25c11992d5ead928aa91cc`
- RB-004 mathematical freeze blob: `d84a2f8c23b0bb0d6be4867a42a6fea235232f20`
- RB-012 consolidated C1 freeze blob: `e371e0cc8b645eb23cbb683d2ed8997ccb9dc62f`
- RB-013 v0.27 scope freeze blob: `287b8942a17bb363e888bee7fe367b2066e3051e`
- RB-014 v0.27 execution-contract freeze blob: `dec52d17974ee49c792e6553c68aed72d5ae5813`
- frozen source contract blob: `05e55e7683ca7013ee6517c3da322c75732fe725`

All frozen scientific design quantities, seeds, solvers, starts, tolerances, budgets, metrics, thresholds, and failure rules were kept unchanged. No legacy C3 effect was used as a target or acceptance criterion.

## 2. Execution environment

| item | value |
|---|---|
| Python | `3.13.5` |
| NumPy | `2.3.5` |
| SciPy | `1.17.0` |
| JAX | `0.9.0.1` |
| jaxlib | `0.9.0.1` |
| JAX backend | `cpu` |
| JAX float64 | `True` |
| CPU | `Intel(R) Xeon(R) Platinum 8272CL CPU @ 2.60GHz` |
| OS/kernel | `Linux 6.18.35 x86_64, glibc 2.41` |
| deterministic environment hash | `4fe5ee7681bf3a768043668a39b35dfe7d4b9745b83fba8265f991971950b787` |
| explicit XLA/JAX/OMP/MKL thread flags | none set in the execution environment |

Physical rerecording used the frozen adaptive Gauss–Kronrod / Brent first-hit rules. Fixed-chart JAX differentiation used a shape-static float64 replay with deterministic Gauss–Legendre phase quadrature; C2-27-03 independently validates that derivative path against physically rerecorded five-point finite differences.

## 3. Phase A — mandatory C2 implementation validation

No scientific RNG object was created before the full C2 suite below passed.

| check | measured result | frozen tolerance / required control | result |
|---|---|---|---|
| C2-27-01 | max time error `3.552713678800501e-15`; section residual `0`; labels correct | both `<=1e-10`; swapped-label comparator must fail | PASS |
| C2-27-02 | arrival-time error `0`; max state error `0`; no premature contribution | arrival `<=1e-12`; state `<=1e-12`; premature-jump control must fail | PASS |
| C2-27-03 | relative Frobenius AD/FD error `1.41455260765337e-09`; all charts valid; sign-flip control error `0.4054464913078937` | positive `<=1e-6`; sign-flip comparator must fail | PASS |
| C2-27-04 | `delta>0` first label `0`; `delta<0` first label `1`; zero case `EVENT_COLLISION / DERIVATIVE_INVALID` | opposite labels; zero collision invalid; stale token rejected | PASS |
| C2-27-05 | max value/gradient error `2.664535259100376e-15` | `<=1e-12`; omitted-logdet control must fail | PASS |
| C2-27-06 | mode error `2.775557561562891e-17`; Hessian rel. error `0`; logdet error `0` | `<=1e-9`, `<=1e-10`, `<=1e-12`; non-PD control must fail | PASS |
| C2-27-07 | selected rows `(0, 2, 3, 6, 8, 10, 11)` | exact equality; constructed sparse dataset must be `INSUFFICIENT_MASK` | PASS |
| C2-27-08 | Laplace-vs-exact marginal objective-change error `8.881784197001252e-16`; wrong-mask control difference `0.07481101683178881` | positive `<=1e-10`; wrong-mask control `>1e-6` | PASS |

**Phase-A decision:** `C2 PASS — 8/8 positive checks and all required negative controls passed.`

## 4. Phase B — immutable stochastic datasets

After C2 PASS, and only then, the 32 scientific datasets were generated with the frozen NumPy `PCG64DXSM` seed map. No seed was replaced and no dataset/trial was regenerated.

- `INSUFFICIENT_MASK`: `0/32`
- truth physical/chart invalid: `0/32`
- minimum mask-rich trials in any dataset: `15/16`
- maximum fixed-chart replay vs physical truth time discrepancy observed in the truth-information audit: `5.542233338928781e-13`

Each dataset hash is SHA-256 over, in order, the generated `Z`, latent spike-time matrix, timing-noise matrix, uint8 mask matrix, and noisy timestamp matrix.

## 5. Conservative shared-parameter information

At the frozen truth, the RB-012 nuisance-profile construction was applied trial-by-trial with the observed masks:

`R_r=(I-P_{N_r})J_{s,r}`,

followed by the frozen shared-column scaling and `I_free = sigma_t^-2 sum_r R_r^T R_r`.

- rank/regularity PASS: `32/32 = 1.000` (threshold `>=0.90`)
- condition-number range: `348731` to `712596`, all below `1e8`

Thus the conservative free-nuisance two-parameter information audit is **positive** under the preregistered design. This does not rescue the inference failure below.

## 6. Frozen Laplace inference outcome

For every dataset and every one of the three frozen outer starts, the complete initial Laplace objective was evaluated by running the frozen per-trial BFGS mode solver from `z=0` in trial order. A complete outer point is finite only if every one of its 16 trial modes and Hessians is valid.

Result:

- total frozen starts attempted: `32 x 3 = 96`;
- finite complete start objectives: `0/96`;
- all `96/96` failures are `INNER_MODE_FAIL` caused by exhaustion/failure of the frozen maximum-20-trial strong-Wolfe line search at at least one trial mode;
- no fourth start, warm start, line-search relaxation, trust region, ridge, alternative optimizer, EM/VI/MCMC route, or data replacement was introduced.

Because each frozen outer start has `L_Lap=+infinity` at initialization, none is a successful bounded-Powell start. Under the frozen rule `if no start succeeds -> OUTER_OPT_FAIL`, every dataset is therefore classified `OUTER_OPT_FAIL`. The bounded Powell directional iterations are not entered from a non-finite complete start; doing so would require an implementation-specific rescue rule not present in RB-014.

This is a failure of the preregistered inference route, not a failure of C2 correctness and not evidence that the underlying shared parameters are structurally unidentifiable.

## 7. Complete 32-replicate ledger

`S0/S1/S2` entries are `failed-trial / BFGS-iteration / objective-gradient-evaluations / failure-detail`. Trial indices are zero-based. No replicate is omitted.

| d | seeds z/noise/mask | dataset SHA-256 | mask-rich | obs per neuron | I_free eig min | I_free eig max | kappa | S0 | S1 | S2 | fit |
|---:|---|---|---:|---|---:|---:|---:|---|---|---|---|
| 0 | `2701000/2701001/2701002` | `b095255cd7de22fd49020c4e245059fcd41ff756b70b67bff929b365203f4103` | 16 | `47/52/51` | 0.012064839 | 4862.5286 | 403033.02 | r1/it1/ev17/W20 | r0/it13/ev44/W20 | r0/it3/ev27/W20 | `OUTER_OPT_FAIL` |
| 1 | `2701003/2701004/2701005` | `4165998bd2bd2dc0a80b83a58d5436618dc2df7910378d6bf769f5856b3f09dd` | 16 | `55/51/51` | 0.011875507 | 4141.3622 | 348731.39 | r0/it13/ev58/W20 | r0/it12/ev41/W20 | r0/it14/ev41/W20 | `OUTER_OPT_FAIL` |
| 2 | `2701006/2701007/2701008` | `58d59cd7371730d10c2488b8bf8d6e57d39334443ce33245018be19a5f4c0d0c` | 16 | `49/49/51` | 0.010222306 | 4866.5336 | 476071.18 | r0/it12/ev44/W20 | r0/it1/ev16/W20 | r0/it14/ev42/W20 | `OUTER_OPT_FAIL` |
| 3 | `2701009/2701010/2701011` | `f1a90ffbd3703ba73a8aa47616d3c79a0afd9b8bb9bda136360223565634484a` | 16 | `52/51/54` | 0.01466278 | 6016.3785 | 410316.28 | r0/it1/ev16/W20 | r0/it13/ev50/W20 | r0/it17/ev55/W20 | `OUTER_OPT_FAIL` |
| 4 | `2701012/2701013/2701014` | `45f6b15c4ce9ae08e985001d0fb7fb6f5c743e85e38f8deeb8955c1869f167da` | 16 | `50/57/51` | 0.0156403 | 6266.6304 | 400670.57 | r0/it11/ev44/W20 | r0/it13/ev43/W20 | r0/it11/ev37/W20 | `OUTER_OPT_FAIL` |
| 5 | `2701015/2701016/2701017` | `59e0e35b94a82411dd96ade4cceae43d518498511424ea0c5711bd229436c154` | 16 | `46/55/58` | 0.009355672 | 6145.3287 | 656856.64 | r0/it13/ev44/W20 | r0/it15/ev51/W20 | r0/it19/ev56/W20 | `OUTER_OPT_FAIL` |
| 6 | `2701018/2701019/2701020` | `b17bb5de1e63f7ef4c37a3595f54106ac09d913db07594fdac5e5d1fbb573b10` | 16 | `53/43/53` | 0.0097806453 | 3712.8203 | 379608.94 | r2/it10/ev43/W20 | r0/it20/ev44/W20 | r0/it16/ev41/W20 | `OUTER_OPT_FAIL` |
| 7 | `2701021/2701022/2701023` | `659b5d964a7d13d15003d1dfb662847c69ba6c14ad3c90a9fe90140b2f889323` | 16 | `50/50/49` | 0.0093887287 | 4866.3134 | 518313.36 | r0/it12/ev47/W20 | r0/it11/ev36/W20 | r2/it14/ev37/W20 | `OUTER_OPT_FAIL` |
| 8 | `2701024/2701025/2701026` | `aa832ccdca807b749cde6c959a495a65f18d989b1e19f41b8b98880cd8bdd83e` | 16 | `48/51/52` | 0.012368853 | 6655.2259 | 538060.7 | r0/it13/ev44/W20 | r1/it14/ev53/W20 | r0/it16/ev43/W20 | `OUTER_OPT_FAIL` |
| 9 | `2701027/2701028/2701029` | `f3433fee04806b4b4bd593401110489419301e48a4d4b065f5b7e46080664470` | 16 | `48/51/53` | 0.010079003 | 5378.9116 | 533676.99 | r0/it13/ev49/W20 | r0/it10/ev41/W20 | r0/it8/ev41/W20 | `OUTER_OPT_FAIL` |
| 10 | `2701030/2701031/2701032` | `e7e00b299162a1cd3882434266f48024c53297acef1c5f322f50ae2dfdf80837` | 16 | `50/55/50` | 0.010008661 | 5764.4295 | 575944.13 | r1/it12/ev44/W20 | r0/it11/ev39/W20 | r0/it18/ev52/W20 | `OUTER_OPT_FAIL` |
| 11 | `2701033/2701034/2701035` | `5bfae64f263ade32149cd89a52d77bddbeb081889aed9135695211656bc88ecf` | 16 | `50/54/50` | 0.013548755 | 5119.2184 | 377836.81 | r1/it11/ev39/W20 | r0/it13/ev48/W20 | r0/it13/ev39/W20 | `OUTER_OPT_FAIL` |
| 12 | `2701036/2701037/2701038` | `db5f2d1b38e8b235f9a503bfc56ff0473db45f83cd4ed490a5d0548bad3bf3cb` | 16 | `49/52/52` | 0.0081899532 | 5836.1166 | 712595.7 | r0/it12/ev42/W20 | r0/it14/ev49/W20 | r0/it11/ev43/W20 | `OUTER_OPT_FAIL` |
| 13 | `2701039/2701040/2701041` | `8045095203fb2cfa2457860831386189f05ec86fbf88f97c4e0db9e58001f1b6` | 16 | `46/54/51` | 0.01146968 | 5502.5748 | 479748.99 | r0/it11/ev38/W20 | r1/it12/ev38/W20 | r0/it16/ev47/W20 | `OUTER_OPT_FAIL` |
| 14 | `2701042/2701043/2701044` | `5c9ebc8451f38ac74ec4bf82e6270cd4f1712697664c5fe153ccf0ca17d76a2e` | 16 | `49/52/56` | 0.0079877714 | 5249.5941 | 657203.12 | r2/it16/ev50/W20 | r0/it14/ev47/W20 | r0/it13/ev46/W20 | `OUTER_OPT_FAIL` |
| 15 | `2701045/2701046/2701047` | `169642dad298f8969c6ba9bdbf5dd7746c75f3270f5ca693e2187c25cf70920d` | 16 | `50/50/53` | 0.010283838 | 5122.712 | 498132.25 | r0/it13/ev46/W20 | r0/it15/ev49/W20 | r0/it10/ev38/W20 | `OUTER_OPT_FAIL` |
| 16 | `2701048/2701049/2701050` | `cc8058f4bcf990b82f8e44bd941540fa73c9c0db334535618697906382916f64` | 15 | `51/49/48` | 0.011919604 | 6272.1716 | 526206.69 | r0/it10/ev37/W20 | r0/it13/ev44/W20 | r0/it14/ev43/W20 | `OUTER_OPT_FAIL` |
| 17 | `2701051/2701052/2701053` | `b3e0aec6243bf6f44309a0a713f076af0fca40f2425fc363400e34703914271f` | 16 | `45/48/54` | 0.011680106 | 4226.1483 | 361824.47 | r0/it14/ev48/W20 | r0/it16/ev48/W20 | r0/it16/ev43/W20 | `OUTER_OPT_FAIL` |
| 18 | `2701054/2701055/2701056` | `f9b254293ce03413ce980319a03d709e0ac8209074576c63d2878bac7069ae0d` | 16 | `48/52/55` | 0.011534266 | 5246.9449 | 454899.75 | r0/it14/ev50/W20 | r0/it8/ev35/W20 | r0/it15/ev43/W20 | `OUTER_OPT_FAIL` |
| 19 | `2701057/2701058/2701059` | `f4d1f9935c1a7a596f55da8ba7188521a8c84bb84b4454f0d1e2066859944676` | 16 | `52/51/51` | 0.012804537 | 5123.4159 | 400124.99 | r0/it13/ev44/W20 | r0/it11/ev36/W20 | r0/it12/ev39/W20 | `OUTER_OPT_FAIL` |
| 20 | `2701060/2701061/2701062` | `2c8847ab56c961f5431e8a9e3e8e6748315f489282630e932e8897de22d4c51a` | 16 | `51/50/51` | 0.011964721 | 4738.3626 | 396027.87 | r1/it11/ev40/W20 | r1/it12/ev40/W20 | r0/it18/ev53/W20 | `OUTER_OPT_FAIL` |
| 21 | `2701063/2701064/2701065` | `747075ebe7ac0328b0ad536105170b218b6830b3c7d38d70a311f8e78ec6cc32` | 16 | `46/50/49` | 0.0084603978 | 4738.6979 | 560103.68 | r0/it13/ev50/W20 | r0/it13/ev46/W20 | r1/it11/ev41/W20 | `OUTER_OPT_FAIL` |
| 22 | `2701066/2701067/2701068` | `7eefb7dd77e8096b8b06cf92f52c576ad80b247e37e1cb2804f33ba04e2d80c8` | 16 | `51/52/49` | 0.009414942 | 4349.5158 | 461980.7 | r0/it14/ev48/W20 | r0/it15/ev49/W20 | r0/it13/ev40/W20 | `OUTER_OPT_FAIL` |
| 23 | `2701069/2701070/2701071` | `2c55d232cb0ff5f86f04b4ce83f8b043ea403969aef0fb6ddfef0b3cbd2d69a4` | 16 | `51/53/50` | 0.010820247 | 5250.4709 | 485245.13 | r0/it13/ev49/W20 | r0/it14/ev46/W20 | r0/it17/ev51/W20 | `OUTER_OPT_FAIL` |
| 24 | `2701072/2701073/2701074` | `be3d2292d66f7230a8527c4b023c90179d62989d6276231fdf2dc2f25e05c7a7` | 16 | `53/49/53` | 0.0081574368 | 5634.7899 | 690754.35 | r1/it11/ev38/W20 | r0/it12/ev40/W20 | r0/it14/ev44/W20 | `OUTER_OPT_FAIL` |
| 25 | `2701075/2701076/2701077` | `3c9c3d0fa970ee1460864104fdb5c33b3bef0662220e08132521d48212837649` | 16 | `53/47/46` | 0.01230624 | 4482.3195 | 364231.56 | r0/it13/ev45/W20 | r0/it10/ev40/W20 | r0/it11/ev38/W20 | `OUTER_OPT_FAIL` |
| 26 | `2701078/2701079/2701080` | `407c86bab2cbc145c1b95a05312f3ca80e73ae6c87ac1839830d2758ed1cf9d4` | 16 | `53/50/53` | 0.0083146653 | 5378.3111 | 646846.55 | r0/it14/ev47/W20 | r0/it14/ev45/W20 | r0/it15/ev46/W20 | `OUTER_OPT_FAIL` |
| 27 | `2701081/2701082/2701083` | `6547f7bc06866edd8bf6f1e94ffb785570231c9176ba12ca93b119e62c08b5f0` | 16 | `45/51/50` | 0.0087618174 | 4349.9318 | 496463.42 | r1/it11/ev40/W20 | r0/it12/ev41/W20 | r0/it12/ev44/W20 | `OUTER_OPT_FAIL` |
| 28 | `2701084/2701085/2701086` | `646ec09ca102594e49f0f3780ff857cc0be5e4b24a7ce0ada87712f36d0f63db` | 16 | `52/50/53` | 0.016360674 | 5759.595 | 352038.98 | r1/it11/ev41/W20 | r1/it14/ev47/W20 | r0/it16/ev48/W20 | `OUTER_OPT_FAIL` |
| 29 | `2701087/2701088/2701089` | `fee6ab15dac1d17ee03604f87bd4620c2bf41ef66a7833431c192a1a24d21144` | 16 | `52/44/53` | 0.0097297589 | 4224.8138 | 434214.65 | r1/it10/ev38/W20 | r0/it12/ev41/W20 | r0/it10/ev36/W20 | `OUTER_OPT_FAIL` |
| 30 | `2701090/2701091/2701092` | `30e89f15110869c6ac745108d57e40f29dd9ff129226d4d78c24db24d4182e26` | 16 | `49/50/47` | 0.010763096 | 5729.5491 | 532331.41 | r0/it14/ev48/W20 | r0/it8/ev37/W20 | r0/it14/ev44/W20 | `OUTER_OPT_FAIL` |
| 31 | `2701093/2701094/2701095` | `fc71847a41e4c84f62a58bbb8a7456f847c7739e80215600ade237974759bfc9` | 16 | `54/50/50` | 0.0090270503 | 5634.3675 | 624164.83 | r0/it13/ev50/W20 | r0/it11/ev37/W20 | r0/it12/ev43/W20 | `OUTER_OPT_FAIL` |

Here `W20` means `STRONG_WOLFE_20_FAIL` under the frozen maximum-20 line-search rule.

## 8. Frozen metrics and thresholds

| metric | observed | threshold | decision |
|---|---:|---:|---|
| `INSUFFICIENT_MASK` fraction | `0/32 = 0.000` | `<=0.10` | PASS |
| truth physical/chart-invalid fraction | `0/32 = 0.000` | `<=0.10` | PASS |
| conservative `I_free` rank-two/regular fraction | `32/32 = 1.000` | `>=0.90` | PASS |
| `INNER_MODE_FAIL` / `INNER_HESSIAN_FAIL` dataset fraction | `32/32 = 1.000` | `<=0.10` | **FAIL** |
| `OUTER_OPT_FAIL` fraction | `32/32 = 1.000` | `<=0.10` | **FAIL** |
| complete usable-fit fraction | `0/32 = 0.000` | `>=0.80` | **FAIL** |
| valid five-parameter uncertainty intervals | `0/32` | `>=26/32` | **FAIL** |
| hierarchical five-Hessian regular fraction | N/A: no successful fits | `>=0.90` among successful fits | not evaluable |
| shared Schur/profile regular fraction | N/A: no five-Hessian-valid fits | `>=0.90` among five-Hessian-valid fits | not evaluable |
| recovery bias / median absolute error / Q90 for all five coordinates | N/A: no estimates | frozen Sec. 9.1 thresholds | not evaluable |
| per-coordinate Wald coverage | N/A: no valid intervals | `>=0.80` | not evaluable; valid-interval minimum already fails |

The hard failure criteria in Section 9.4 fail before recovery/coverage can be meaningfully assessed. Therefore the frozen hierarchy selects `SCIENTIFIC FAIL`, not `SCIENTIFIC CONDITIONAL`.

## 9. Software-plumbing audit trail

Before the final governed rerun, an uncommitted preflight attempt applied SciPy 1.17.0 bounded Powell directly to a start with non-finite complete objective. SciPy's internal extrapolation path called `_line_for_search` with a zero direction and raised `ValueError: zero-size array to reduction operation maximum which has no identity` after evaluating only non-finite outer points.

That preflight output is **invalidated and is not evidence**. No scientific constant, seed, solver tolerance, start, criterion, or dataset was changed in response.

A zero-direction-safe wrapper was tested only to confirm the SciPy plumbing defect. The final governed execution was restarted from the complete fresh Git/freeze read and from C2. In that governed rerun, the relevant scientific fact occurs earlier: all three frozen complete start objectives are non-finite because a trial-mode solve fails. Consequently no Powell direction iteration is required to assign those starts as unsuccessful under the frozen `no successful start -> OUTER_OPT_FAIL` rule.

No post-output rescue, retuning, seed replacement, parameter change, horizon change, objective replacement, or additional start was performed.

## 10. Scientific interpretation

### PROPOSITION / GOVERNED NUMERICAL RESULT

Under exactly RB-014, the passive repeated-trial design has regular conservative local information for `(p,tau_3)` in all 32 frozen datasets, but the preregistered nested Laplace inference procedure fails operationally at its frozen trial-mode/outer-start layer for every dataset.

This result supports only the narrow statement above. It does **not** prove global non-identifiability, does not show that hierarchical repeated-trial inference is impossible, and does not authorize changing the optimizer or adding active probes in this branch.

## 11. Final gate decision

# SCIENTIFIC FAIL

Decision hierarchy application:

1. Phase A C2 passes, so this is not `IMPLEMENTATION FAIL / BLOCKED`.
2. Phase B hard failure fractions fail: `INNER_MODE_FAIL=1.00`, `OUTER_OPT_FAIL=1.00`, usable-fit fraction `0.00`.
3. Therefore the gate is `SCIENTIFIC FAIL` irrespective of the positive `I_free` audit.

This failed/null operational outcome is preserved exactly as required by governance.

## 12. Proposed MASTER result-freeze package

CORE proposes that MASTER, if it accepts the execution semantics above, establish `CORE v0.27 Hierarchical Repeated-Trial Result Freeze 0.1` containing only:

1. the environment identity and C2 PASS table;
2. immutable 32-dataset seed/hash ledger;
3. `0/32` mask failures and `0/32` truth chart failures;
4. `32/32` conservative `I_free` regularity PASS;
5. `0/96` finite frozen outer-start objectives due `STRONG_WOLFE_20_FAIL` in at least one trial mode;
6. `32/32 OUTER_OPT_FAIL`, `0/32` usable fits, and no valid uncertainty intervals;
7. final `SCIENTIFIC FAIL`;
8. the plumbing-audit note and explicit non-promotion of any legacy C3 effect.

The proposed freeze must not imply that a redesigned solver, additional starts, active sensing, or another hierarchical model would fail. Those are separate future branches requiring MASTER authorization.

## 13. Boundary

- no legacy C3 result was promoted;
- no v0.28 work was opened;
- no active pulse/probe extension was attempted;
- no application, novelty-positioning, or manuscript-claim work was performed.

STOP — RETURN TO MASTER