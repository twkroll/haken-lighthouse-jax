# MASTER Prompt — NUM-ENG Theory-Derived First-Hit Certification Validation Gate 0.3

## Purpose

Validate the newly frozen RB-022 first-hit/event-chart theory against the frozen RB-021 numerical engineering baseline using only deterministic, prospectively fixed engineering fixtures.

This gate is a THEORY-VALIDATION / ENGINEERING gate.

It must not create effect-bearing science, protected stochastic data, AI-training evidence, novelty claims, or universal correctness claims.

## Mandatory authorities

Read and obey:

- `PROJECT_GOVERNANCE.md`
- `research/master/command_protocol_v0_2.md`
- `research/master/parallel_engineering_policy_v0_1.md`
- RB-004 Mathematical Freeze 0.1
- RB-019 Numerical Engineering Freeze 0.1
- RB-020 CORE v0.27c Execution Contract Freeze 0.1
- RB-021 Numerical Engineering Freeze 0.2
- RB-022 CORE Event-Chart Regularity & Certified First-Hit Theory Freeze 0.1
- current MASTER / CORE / NUM-ENG STATUS files.

Work only on:

`engineering/numerics-v0.1`.

The physical authority remains:

`NUMENG_PULSE_AWARE_REFERENCE_V1`.

The strengthened high-level tape/JAX validation from RB-021 may be used where applicable.

## Pre-execution rule

Before executing any new Gate-0.3 validation result, create and commit a finite validation contract containing:

- exact fixture definitions;
- exact parameter values;
- exact interval partitions/refinement schedule;
- exact tolerances;
- exact classification rules;
- exact negative controls;
- exact expected theorem relation for each fixture.

No fixture or tolerance may be changed after inspecting Gate-0.3 outputs.

If the finite validation contract is not fully fixed first, return BLOCKED.

## Validation families

### TV-01 — exact alpha-state segment propagation

On prospectively fixed arrival-free segments, validate

[
q(s)=e^{-alpha s}q_0,qquad
psi(s)=e^{-alpha s}(psi_0+s q_0)
]

against the frozen physical authority or an independently evaluated exact segment formula.

Include ordinary and narrow-pulse regimes.

### TV-02 — analytic extrema

For predetermined segment states, compare numerically found extrema of

[
psi(s)=e^{-alpha s}(psi_0+s q_0)
]

against the finite analytic candidate set:

[
{a,b}cup{s_cin(a,b)}.
]

Require classification agreement and fixed absolute tolerances.

### TV-03 — no-hit upper certificates

Use predetermined fixtures where the RB-022 upper phase-gain bound is strictly below the remaining phase gap.

The engineering layer must certify NO-HIT only when the frozen inequality margin is positive.

Include at least one near-zero-margin case that must return UNCERTIFIED rather than NO-HIT.

### TV-04 — unique regular first-hit certificates

Use predetermined fixtures where lower/upper accumulated-phase enclosures form a strict bracket and the response lower bound is positive.

Validate:

- existence of exactly one first hit in the bracket;
- physical first-hit time lies inside the certified bracket;
- transversality remains above the prospectively fixed margin;
- zero-margin/tangential controls are not promoted to regular certification.

### TV-05 — response derivative bounds

Numerically stress predetermined x-grids / analytic critical points for:

[
|S'|_infty
=
rac{2}{sqrt r}
left(rac32ight)^{3/2}e^{-3/2}
]

and selected (S'')/higher-derivative scaling checks.

The numerical result may confirm finite consistency but may not redefine the theorem constants.

### TV-06 — alpha-tail mass and phase-error bound

Validate:

[
M_eta(A)=e^{-alpha A}(1+alpha A)
]

against independent quadrature on fixed A/alpha cases.

Then construct deterministic omitted-history fixtures satisfying RB-022's explicit summability assumptions and verify the frozen phase-error inequality.

Include a case where local finiteness holds but the stronger tail assumption is deliberately absent; the implementation must not claim a theorem-backed finite tail certificate there.

### TV-07 — regular-chart perturbation persistence

Create a finite predetermined regular-margin fixture.

Apply a fixed set of small perturbations to:

- one structural weight;
- one fixed delay;
- one initial phase/state coordinate.

For each perturbation:

- physically rerecord;
- verify the same topology-fixed labelled event order where margins stay positive;
- record minimum transversality, event-separation and boundary margins;
- reject rather than differentiate any perturbation that changes the chart.

### TV-08 — local event-time derivatives

On predetermined regular charts compare:

- RB-022 spike-time derivative representation;
- arrival-time derivative;
- high-level JAX/fixed-chart derivative after physical certification;
- physically rerecorded centered finite differences.

Coordinates must include:

- a nonzero structural weight;
- a structural weight evaluated at exactly zero;
- an active fixed delay;
- a structural-zero edge delay;
- an initial-state/phase coordinate.

Do not finite-difference across itinerary changes.

### TV-09 — repaired structural-zero fixture TH-FH-06

Implement the topology-fixed three-point family:

[
w_e=-arepsilon,quad 0,quad +arepsilon
]

without changing topology.

Also create the separate graph-with-edge-omitted comparison.

Require:

1. physical state/spike equivalence at exact zero between zero-weight and omitted-edge systems when both are regular;
2. labelled event tapes are NOT identical;
3. zero-weight topology retains the arrival;
4. weight derivative at zero matches physically rerecorded centered finite differences on the predetermined regular fixture;
5. zero-edge delay moves the labelled arrival even when the physical state remains unchanged;
6. chart-margin/collision controls fail closed;
7. deleting the zero-edge arrival from a topology-fixed tape is rejected by the high-level tape guard.

### TV-10 — TH-FH fixture family

Execute all frozen theory-derived fixtures TH-FH-01 through TH-FH-08.

For each fixture predeclare whether the expected category is:

- CERTIFIED REGULAR HIT;
- CERTIFIED NO-HIT;
- PHYSICALLY VALID BUT ORDINARY-CHART INVALID;
- UNCERTIFIED;
- PHYSICALLY INVALID / RESOURCE FAILURE.

Do not merge UNCERTIFIED with PHYSICALLY INVALID.

### TV-11 — stale-tape / itinerary-change controls

Reuse RB-021 guard logic and add theory-derived controls showing that:

- same event token alone is insufficient if times/states are stale;
- topology deletion at structural weight zero is rejected;
- event-order change invalidates fixed-chart differentiation;
- physically certified rerecording is required before JAX derivative use.

## Outcome rules

A Gate-0.3 engineering PASS requires:

- every prospectively fixed positive theorem-validation case meets its finite tolerance/classification;
- all negative/fail-closed controls behave as preregistered;
- no fixture requires post-output retuning;
- no contradiction to RB-022 is observed;
- no physical-authority contradiction to RB-019/RB-021 is observed.

If a finite numerical fixture contradicts an RB-022 theorem under all of its stated assumptions, return:

`THEORY/IMPLEMENTATION CONTRADICTION — BLOCKED`

and preserve raw evidence.

If the problem is merely insufficient finite certification near a zero margin, classify:

`UNCERTIFIED`

rather than FAIL.

## Engineering result classes

Every material result must be classified as one of:

- THEORY-CONSISTENT ENGINEERING VALIDATION
- UNCERTIFIED
- ENGINEERING DEFECT
- THEORY/IMPLEMENTATION CONTRADICTION
- DEFERRED

No scientific effect PASS is possible in this gate.

## Forbidden

- no `2711xxx` RNG creation;
- no TR-27C execution;
- no v0.27c confirmatory run;
- no APP-3 execution;
- no new stochastic benchmark;
- no speedup/scaling scientific claim;
- no fixture search after outputs;
- no threshold/tolerance retuning after outputs;
- no executable source merge to `main`;
- no novelty/manuscript claims.

## Required outputs

On `engineering/numerics-v0.1` create:

1. `research/numerical_engineering/theory_derived_first_hit_validation_contract_0_3.md`
   - must be committed before Gate-0.3 execution;
2. `research/numerical_engineering/theory_derived_first_hit_certification_validation_gate_0_3.md`
3. raw machine-readable/log artifacts sufficient to reproduce every classification.

Update:

`research/numerical_engineering/STATUS.md`

to RETURN TO MASTER or BLOCKED.

## Recommendation

If PASS, recommend a bounded:

`NUM-ENG Theory-Derived Certification Validation Freeze 0.3`

without claiming global simulator correctness.

If any theorem contradiction appears, do not repair or reinterpret it inside this gate; return to MASTER.

## STOP

STOP — RETURN TO MASTER
