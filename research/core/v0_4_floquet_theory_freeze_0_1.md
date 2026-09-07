# CORE v0.4 Floquet Theory Freeze 0.1

Date: 2026-09-07
Status: FROZEN / STABLE SCIENTIFIC THEORY
Rollback point: RB-010

## Authority

MASTER accepts `research/core/v0_4_floquet_theory_canonicalization_gate_0_1.md` as PASS.

Frozen source artifact:

- file: `research/core/v0_4_floquet_theory_canonicalization_gate_0_1.md`
- blob SHA: `00caa0dc75186967673062047af3fe3c251d3cd3`
- creation commit: `40d8a98dc237f1656ce91c1f33cda3eb51f43ff8`
- RETURN-TO-MASTER commit: `2bb88dfd1991594868314f180920c6625879ed1b`

Underlying authorities remain RB-004, RB-006, RB-007, RB-008 and RB-009. The read-only legacy recovery input remains fixed at `287eae8a86560b78ed94f30a2786243714c33ac0`.

## Frozen theory

RB-010 freezes only the narrow mathematical/source/formulation layer independently established in the gate, including:

1. the regular phase-locked timing representation `T_i^m=(m+chi_i)T` and local-cycle input representation;
2. the spike-section velocity `nu_i` and regular-event assumptions;
3. the spike-time linear recurrence

   `nu_i(delta T_i^{m+1}-delta T_i^m)=sum_j w_ij sum_ell K_ij,ell delta T_j^{m-ell}`

   under the stated itinerary, differentiability and convergence assumptions;
4. the exact cancellation of the source-aligned diagonal row-sum term under periodicity;
5. the nonlinear cycle-multiplier operator

   `M(mu)=(mu-1)D_nu-H(mu)`

   and characteristic problem `M(mu) xi=0` on its convergence domain;
6. the alpha lag-series convergence domain `|mu|>exp(-alpha T)` and the distinction between the convergent lag series and meromorphic algebraic continuation;
7. the exact neutral global time-translation mode `M(1) 1 = 0`;
8. the weighted derivative-comb representation and alpha closed form with arrival-boundary qualification;
9. multiplier/exponent conventions and multiplier-space stability labels as project conventions, without asserting completeness of the spike-time spectrum for the full hybrid state;
10. simple nonlinear-eigenvalue sensitivity for normalized left/right nullvectors;
11. the strict logical separation of existence criticality, dynamic criticality, event singularity, arrival/event-chart boundary and representation boundary;
12. event-index relabelling covariance and spectrum invariance under the corresponding similarity transformation;
13. exchange-symmetric two-cell reduction and the distinction between the v0.3 existence coefficient `B` and a dynamic `E_-(1)=0` condition;
14. exact DFT/Fourier reduction conditional on the full delayed locked-state characteristic operator being circulant in a consistent event-index gauge, including the distinction between base twist `q0` and perturbation sector `q`;
15. equitable cluster quotient conditions, transverse-sector qualification and general symmetry-sector decomposition where the full operator commutes with the relevant symmetry action.

## Canonical repairs / qualifications retained

- The source-aligned row-sum term is not omitted by convention; its cancellation is proved under periodicity and the stated interchange assumptions.
- A meromorphic alpha derivative-comb expression outside the absolute-convergence domain is not called a convergent lag-sum identity.
- `|y^* M'(mu_*) xi|` is used only with an explicit left/right-vector normalization and is not frozen as a universal scale-invariant condition number.
- Circulant weights alone do not justify Fourier reduction; the full locked-state characteristic operator must respect the symmetry in a consistent event-index gauge.
- The guaranteed neutral mode is identified by its physical uniform spike-time vector, not by deleting whichever numerical root lies nearest `1`.
- No equivalence between the spike-time characteristic spectrum and every auxiliary full hybrid-state Floquet mode is frozen here.

## Freeze boundary

RB-010 does **not** freeze, validate, compute or authorize:

- legacy B23–B40 outputs or tolerances;
- any actual Lighthouse Floquet multiplier/root set;
- any Lighthouse stability boundary, period-doubling, Neimark–Sacker, unit-multiplier or mode-selection result;
- any continuation/Floquet critical-point coincidence claim;
- v0.5 normal-form coefficients or scaling results;
- v0.6+ numerical bifurcation/invariant-object results;
- production/JAX Floquet implementation or performance;
- inference, observation design, active experiment design, applications, novelty, manuscript claims or v0.27.

Legacy `core/theory-v0.1` remains read-only recovery evidence and is not merged.

## Change control

Any alteration of this theory requires a new MASTER-authorized gate and a new versioned freeze.

## STOP

`CORE v0.4 Floquet Theory Freeze 0.1` is established.

STOP — FROZEN
