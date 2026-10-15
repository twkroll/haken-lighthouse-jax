# NUM-ENG Gate 0.2 — frozen deterministic engineering stress matrix

Date: 2026-10-15
Status: FIXED BEFORE GATE-0.2 STRESS EXECUTION
Authority: MASTER NUM-ENG Robustness, Scaling & Differentiable Kernel Gate 0.2 / RB-019.
Environment: CPU float64 only. All outcomes are DEVELOPMENT EVIDENCE and local ENGINEERING METRICS. No random-number generation.

## Physical authority and invalidity

The independent engineering comparison standard is unchanged `NUMENG_PULSE_AWARE_REFERENCE_V1` from the RB-019 integrated subtree. Its valid/invalid status, labelled event signatures, spike times, and warnings are recorded without retrospective repair. The optional accelerated Gauss/quiet/phase-bound variants are comparators only until checked against physical authority and furnished with fail-closed fallback.

## Deterministic matrix (all fixed without observing Gate-0.2 results)

Use direct `SparseParameters`, `physical_rerecord_sparse` and its `to_dense()` equivalent with exact histories/initial phases.

F01: one self-edge (0,0), W=4, delay=1.5, alpha=1000, r=1, h=.1; history [[-1.]], theta0=2*pi-.005; horizon=20. RB-018 first-hit pulse.
F02: same F01 but theta0=2*pi-.5; horizon=20; threshold non-crossing guard.
F03: same F01 with alpha=30, theta0=2*pi-.005, horizon=12.
F04: same F01 with alpha=1, theta0=2*pi-.005, horizon=12.
F05: one self-edge W=0, delay=.71, alpha=1, r=1, h=-1; history [[-1.23]], theta0=5.8; horizon=8; structural zero edge.
F06: one self-edge W=-2, delay=.18, alpha=1, r=1, h=-1; history [[-1.23]], theta0=5.8; horizon=8; inhibitory weight.
F07: one self-edge W=6, delay=.11, alpha=30, r=1, h=.1; history [[-.07]], theta0=2*pi-.05; horizon=6; short-delay and brief pulse.
F08: N=2, E=0, alpha=1, r=1,h=-1; theta0=(6., 6.), horizon=3; intentional Spike–Spike collision, MUST fail-closed.
F09: same F08 with theta0=(6., 5.9999999); horizon=3; near-collision, classify per fixed collision_tol=1e-8.
F10: N=2, E=0, alpha=1,r=1,h=.1, theta0=(6.,6.1), horizon=3; silent due to zero input.
F11: one edge (0,0) W=4 delay=.5 alpha=1000 r=1 h=.1; historical emission=-.5, theta0=2*pi-.005 horizon=2; arrival at initial boundary MUST fail-closed.
F12: one edge (0,0) W=4 delay=1.5 alpha=1000 r=1 h=.1, historical emission=-1, theta0=2*pi-.005, horizon=.5; arrival exactly at horizon MUST fail-closed.
F13: one self-edge W=4 delay=1.5 alpha=1000 r=1 h=.1, historical emission=-1, theta0=2*pi-.005, horizon=20, max_events=0; budget failure MUST fail-closed.
F14: one self-edge W=4 delay=1.5 alpha=1000 r=1 h=.1; history [[-1.]], theta0=2*pi-.005, horizon=20; artificially force `max_segments=1` in direct pulse integral to test explicit uncertified failure.
F15–F18: deterministic directed sparse graphs N=5,12,24,48 and E target approximately 2*N. For each target i, include self-edge (i,i) and edge (i,(i+1)%N). Sort lexicographically (target,source); all weights are `2.25 + .17*(source%3) - .11*(target%2)` on self edges and `(-.6 if target%3==0 else .9)` on neighbor edges; delays `0.12 + .017*((5*target+3*source)%13)`; alpha=1,r=1,h=-1; one historical emission per source at `-1.1-.021*source`; initial phase_i=`5.2+.021*(i%7)+.002*i`; horizon 8 for N<=24 and 4 for N=48.

Predefined dense/sparse comparisons: F01–F13, F15–F18; expected event-token equivalence exact, both validity classifications equal, max |delta time|<=2e-8, final-phase difference <=3e-8. All invalid cases retained; no result screening.

Predefined acceleration comparisons: gauss and quiet for F01–F07, F10, F15–F18; upper phase-bound accelerator F15–F18 where available. Mismatch, exception, or invalid-status disagreement is logged and classified; candidate never overwrites authority.

AD/JVP/VJP finite-difference fixture G01: `tests/test_rri_repair_v01.py::ordinary_fixture`, sparse conversion; horizon=40, history=((-3,-.5),(-2.2,)), theta0=(.3,1.1). Weight coordinate the structural zero edge, delay coordinate the middle nonzero edge, initial phase coordinate neuron0. Central FD epsilon=1e-4 for weight/delay/phase; each plus/minus rerecorded independently; skip and label CHART_EXIT if any changed chart. AD max absolute mismatch tolerance 3e-5; replay-vs-physical spike-time tolerance 1e-7. Do not use negative/control fixtures for AD.

Compile/execution fixture J01: G01 baseline for JAX `jit` forward vs `jit` Jacobian; report first-call compilation cost and warmed median over 3 repeats separately. No general speedup claim; if JAX compile fails or memory budget exceeds local environment report separately.

Scaling matrix S01–S04: F15–F18; record N/E, events, work counters (integral requests, adaptive quadratures, root solves), rerecord calls, wall time for 3 warm runs (median and min-max), and expected physical alpha state memory = 16*E bytes vs dense 16*N*N bytes (two float64 alpha arrays only). Exclude Python/JAX heap from theoretical state bytes. A no-GPU CPU target is frozen; speedups are local development observations.

Process P01: run targeted new suite twice in isolated processes with plugin autoload disabled and CPU threads=1; run original 194 pytest tests once as aggregate if budget allows, and separately note any clean exit failure. Capture versions and CPU.

## Numerical decision rules

- Physical authority `chart_valid` and `physical_certification` must be preserved unchanged, including invalid cases.
- Event token exact. Relative tolerances are never substituted for above absolute tolerances.
- Positive stress cases without a spike are legitimate results; do not post-hoc tune to generate them.
- Accelerated schedulers must retain certified physical rerecord and fail-closed fallback before they could become authoritative. Otherwise DEVELOPMENT COMPARATOR, even if candidate matches.
- Fail-closed budget exhaustion and collision flags are requirements.
- PASS only if the engineering QA passes for accepted components. Any discovered physical-authority contradiction must block freeze recommendation and return to MASTER.

## STOP

No protected RNG namespaces, CORE TR validation/execution, APP-3, scientific claim, main merge or benchmark promotion.
