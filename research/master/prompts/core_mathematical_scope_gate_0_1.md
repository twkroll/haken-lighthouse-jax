# CORE Mathematical Scope Gate 0.1

## Purpose
Establish the canonical mathematical baseline for the Haken Lighthouse model before implementation or application work begins.

## Authorized scope

1. Identify the primary Haken formulation(s) relevant to the Lighthouse model and distinguish original definitions from later reformulations.
2. Define a canonical baseline notation for neuron state, phase evolution, spike events, synaptic activation, coupling, thresholds, and delays.
3. State the minimum baseline model that future numerical work must reproduce.
4. Enumerate mathematically meaningful model variants that may later be compared, but do not select a variant based on observed effect strength.
5. Separate:
   - PROVED / established source-derived statements,
   - assumptions introduced for the project,
   - conjectures,
   - open questions.
6. Record known analytical structures relevant to later validation: synchronization, phase locking, delay effects, waves, bumps, stability, or continuum limits, only where supported by sources.
7. Define explicit exclusions for the baseline freeze.

## Required source discipline

Prefer primary sources and authoritative mathematical literature. Clearly distinguish original Haken sources from later analyses such as modern reformulations. Do not infer novelty from absence of a search hit.

## Explicitly forbidden in this task

- No JAX implementation.
- No parameter fitting or optimization.
- No scanning parameter ranges to find strong effects.
- No ML benchmarks.
- No application-domain claims beyond identifying later possibilities.
- No STDP or adaptive-delay execution unless needed only to classify them as later variants.
- No manuscript novelty claims.

## Deliverable

Create:

`research/core/mathematical_scope_gate_0_1.md`

It must contain:

- Scope
- Source map
- Canonical equations and notation
- Event / spike definition
- Synaptic and delay definitions
- Baseline assumptions
- Variant registry
- Analytical validation targets
- Explicit exclusions
- Gate decision: PASS / FAIL / CONDITIONAL
- Proposed `CORE Mathematical Freeze 0.1` contents if PASS
- Open questions
- STOP

Then update `research/core/STATUS.md` and return to MASTER.

## STOP boundary

STOP after the gate deliverable and status update. Do not begin implementation or a second theory task.

STOP — RETURN TO MASTER
