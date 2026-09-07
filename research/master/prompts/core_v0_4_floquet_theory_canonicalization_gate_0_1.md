# CORE v0.4 Floquet Theory Canonicalization Gate 0.1

## Purpose

Independently audit, re-derive and narrowly canonicalize the C1/C2-eligible mathematical v0.4 spike-time Floquet and symmetry layer from the frozen legacy recovery snapshot, building only on currently frozen canonical CORE layers.

This gate is **mathematical / source / formulation verification only**. It does not execute B23–B40, search for Lighthouse multipliers, classify any actual Lighthouse branch as stable/unstable, or start v0.5+ science.

## Authoritative canonical inputs

Read first:

- `PROJECT_GOVERNANCE.md`
- `research/core/STATUS.md`
- `research/master/STATUS.md`
- `research/master/project_status.md`
- `research/master/decision_branch_log.md`
- `research/core/mathematical_freeze_0_1.md` — RB-004
- `research/core/v0_2_benchmark_result_freeze_0_1.md` — RB-006
- `research/core/v0_3_continuation_theory_freeze_0_1.md` — RB-007
- `research/core/v0_3_continuation_validation_contract_freeze_0_1.md` — RB-008
- `research/core/v0_3_continuation_validation_result_freeze_0_1.md` — RB-009
- `research/core/recovery_canonicalization_gate_0_1.md`

Frozen legacy recovery input is read-only at exact commit:

`287eae8a86560b78ed94f30a2786243714c33ac0`

Candidate legacy v0.4 inputs:

- `docs/core/spike_time_floquet_v0.4.md`
- `docs/core/symmetry_reductions_v0.4.md`
- `docs/core/floquet_contract_v0.4.md` only as candidate test/claim inventory, not as an accepted benchmark contract.

Do not merge, rebase, squash, delete or rewrite the legacy branch.

## Authorized work

### A. Claim/provenance audit

For every retained v0.4 mathematical statement, classify it as applicable:

- SOURCE-DERIVED
- DERIVATION HERE
- PROJECT DEFINITION / METHOD
- ASSUMPTION
- INTERPRETATION
- OPEN QUESTION

and assign the project epistemic labels THEOREM / PROVED, PROPOSITION, LEMMA, ASSUMPTION, CONJECTURE, INTERPRETATION or OPEN QUESTION only where justified.

Any attribution to Haken, Coombes 2025/2026, Coombes–Thul–Ruschel–Nicks 2026 or another source must be checked precisely enough for canonical use. Do not perform novelty positioning.

### B. Independently re-derive the core spike-time Floquet layer

Subject to the frozen RB-004/RB-007 event and regularity assumptions, independently derive or reject/repair:

1. phase-locked spike times `T_i^m=(m+chi_i)T` and local cycle representation;
2. spike-section/event velocity `nu_i` and its transversality role;
3. first-order spike-time perturbation of delayed kernel arrivals;
4. the one-cycle phase-gain linearization including moving integration limits;
5. lag-coefficient recurrence of the form
   `nu_i(delta T_i^{m+1}-delta T_i^m)=sum_j w_ij sum_l K_ij,l delta T_j^{m-l}`;
6. the cycle-Floquet ansatz and nonlinear characteristic operator
   `M(mu)=(mu-1)D_nu-H(mu)`;
7. precise domain/convergence assumptions for the lag sums and nonlinear eigenproblem;
8. the exact neutral global time-translation multiplier `mu=1`, including a proof of `M(1)1=0` under the stated assumptions;
9. multiplier versus cycle/physical-time exponent conventions and branch-log qualification;
10. the distinction between existence-Jacobian criticality from RB-007 and dynamic multiplier criticality.

Do not assume determinant-based numerics or any actual root result.

### C. Weighted derivative-comb / alpha-kernel layer

Independently verify or repair:

1. definition of the Floquet-weighted derivative comb `Q_mu`;
2. equivalence between lag-sum and weighted-comb formulations where mathematically justified;
3. the closed-form alpha-kernel weighted derivative comb away from arrival boundaries;
4. the precise absolute-convergence domain of the series representation;
5. any meromorphic-continuation statement, clearly separating algebraic continuation from convergent-series identity;
6. one-sided/event-chart conventions at arrival boundaries;
7. relation to the frozen periodic alpha state-space formulation without adding new numerical evidence.

### D. Symmetry reductions

Independently verify or repair the mathematical reductions, at minimum:

1. exchange-symmetric two-cell symmetric/antisymmetric reduction;
2. circulant-ring condition on the **full delayed locked-state characteristic operator**, not weights alone;
3. exact DFT/Fourier diagonalization for a circulant operator;
4. distinction between base twist `q0` and perturbation Fourier sector `q`;
5. neutral global shift lying in the uniform perturbation sector;
6. N=2 ring equivalence with the dedicated two-cell decomposition;
7. equitable cluster quotient condition for the full characteristic coupling;
8. distinction between longitudinal quotient and transverse cluster modes;
9. general finite permutation-symmetry/isotypic decomposition only to the extent it follows rigorously from commutation of the full operator with the group action;
10. base-state isotropy qualification — do not use network symmetries broken by the delayed locked state.

The continuum/large-ring limit may be retained only as a conditional asymptotic statement or OPEN QUESTION unless independently justified at the required level. Do not numerically demonstrate it in this gate.

### E. Conditioning and bifurcation labels

Audit the mathematical status of:

- left/right nonlinear-eigenvector conditioning denominator `y^* M'(mu_*) xi` for a simple root;
- unit (`mu=+1`), period-doubling (`mu=-1`) and Neimark–Sacker (`|mu|=1`, away from ±1) labels.

These may be retained as mathematical definitions/propositions only with the necessary simplicity, conjugacy, regularity and nontrivial-neutral-mode qualifications. No actual Lighthouse critical point may be classified.

### F. Legacy B23–B40 disposition

Create an explicit claim/test disposition table for legacy B23–B40 with labels such as:

- eligible for later pre-execution validation contract;
- requires repair before later validation;
- deferred because it depends on un-frozen v0.4 numerical root infrastructure or an actual Lighthouse branch;
- deferred to v0.5+ or later scientific work.

Do **not** execute any B23–B40 benchmark and do not adopt their legacy recommended tolerances as canonical.

## Mandatory exclusions

This gate must not:

- execute any Floquet multiplier/root calculation for an actual Lighthouse branch;
- run B23–B40;
- select/search a stability boundary;
- perform a parameter sweep or continuation;
- claim an actual Lighthouse unit/PD/NS instability;
- use a v0.3 legacy fold/pitchfork location as evidence;
- perform saltation-spectrum cross-validation beyond already frozen mathematical identities;
- perform continuum convergence numerics;
- build production/JAX root solvers;
- start v0.5 normal-form execution;
- run v0.6+ legacy numerical science;
- do inference, observation design, active experiment design, applications, novelty positioning, manuscript claim freeze or v0.27.

No tuning or effect-based selection is permitted.

## Deliverable

Create exactly:

`research/core/v0_4_floquet_theory_canonicalization_gate_0_1.md`

It must include at minimum:

1. Git/provenance identity;
2. authoritative/frozen-input map;
3. source/provenance claim map;
4. independently re-derived spike-time recurrence;
5. nonlinear characteristic operator and its domain assumptions;
6. neutral-mode proof;
7. weighted derivative-comb derivation and alpha formula qualification;
8. two-cell and ring/Fourier reductions;
9. cluster/general symmetry qualifications;
10. multiplier/exponent and dynamic-bifurcation definitions;
11. conditioning statement with assumptions;
12. existence-vs-dynamic-vs-event/chart taxonomy alignment with RB-007;
13. C1/C2/C5-style recovery disposition by claim;
14. B23–B40 inclusion/defer/repair matrix for a later contract;
15. explicit exclusions;
16. PASS / FAIL / CONDITIONAL gate decision;
17. if PASS, proposed contents of `CORE v0.4 Floquet Theory Freeze 0.1` only — not the freeze itself;
18. open questions and proposed MASTER sequencing only;
19. STOP.

PASS means only that the v0.4 mathematical Floquet/symmetry layer is sufficiently verified for MASTER to decide a narrow theory freeze. PASS does **not** validate a multiplier, stability boundary, B23–B40 result, v0.5 normal form or any downstream legacy numerical claim.

## Status transition

After writing the deliverable, update `research/core/STATUS.md` to `RETURN TO MASTER` or `BLOCKED` as appropriate.

Do not start another gate.

## STOP

STOP — RETURN TO MASTER
