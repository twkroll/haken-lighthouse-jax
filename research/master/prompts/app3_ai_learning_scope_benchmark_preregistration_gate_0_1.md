# MASTER Prompt — APP-3 AI Learning Scope & Benchmark Preregistration Gate 0.1

## Administrative state

PREPARED ONLY — NOT YET OPEN / NOT EXECUTABLE.

APP-3 remains `PROTECTED / WAIT` until MASTER explicitly changes its STATUS to READY after required dependencies return.

## Purpose

Define one controlled prospective research program testing whether a Lighthouse-network variant can function as a useful AI/temporal-learning method. This gate is scope and preregistration only. It must not train models or inspect new held-out performance.

## Required dependencies before activation

MASTER must first review:

1. the returned `NUM-ENG Numerical Engineering Gate 0.1` result and any authorized engineering baseline/freeze;
2. the returned `CORE v0.27c Whitened Trust-Region Laplace Execution Contract Canonicalization Gate 0.1` result.

RB-015 remains SCIENTIFIC FAIL and is not an AI baseline.

## Required architecture definition

Prospectively define:

- input representation/encoder;
- whether input is initial-state encoding, external drive, or another explicitly registered variant;
- exact readout;
- trainable parameters;
- whether weights, delays, initial states, readout parameters, or combinations are trained;
- constraints/parameterizations for delays and weights;
- event/chart invalidity behavior during optimization;
- physical rerecording vs fixed-chart differentiation responsibilities;
- inference-time state and event representation.

Any departure from the RB-004 autonomous/no-drive/fixed-parameter baseline must be explicitly registered as an application/model variant, not silently treated as baseline Lighthouse dynamics.

## Learning tasks

Choose a finite predetermined task suite before training. Candidate classes may include:

- temporal-order/memory tasks;
- event-time prediction;
- delayed classification;
- fixed public event/time-series data only if dataset and splits are fixed prospectively.

Do not choose tasks by trying many candidates and retaining favorable ones.

## Baselines

The preregistered comparison must include at minimum:

- a standard RNN or GRU;
- a reservoir / Echo-State Network;
- a spike-based baseline such as an LIF SNN or LIF reservoir;
- simple task-appropriate nonrecurrent/control baselines.

Define fair parameter/data/compute matching and document unavoidable mismatches.

## Train/validation/test and seed discipline

Before any scientific learning run, freeze:

- train/validation/test split;
- data preprocessing;
- all RNG namespaces;
- initialization seeds;
- hyperparameter-search seeds;
- independent final test seeds;
- replicate count.

All APP-3 seeds must be disjoint from `2701xxx`, reserved `2711xxx`, and other protected project namespaces.

No final-test split may be inspected during model/hyperparameter development.

## Training and compute budgets

Freeze prospectively:

- optimizer(s);
- learning-rate/search ranges;
- batch size;
- epochs/steps;
- early stopping;
- maximum hyperparameter trials;
- parameter-count budget;
- wall-clock/accelerator budget;
- numerical tolerances;
- invalid-chart retry/failure budget.

## Metrics and success hierarchy

Primary metrics must be task-appropriate and held-out. Also report:

- trainable parameter count;
- training/inference compute;
- chart-invalid/failure rate;
- gradient failure rate;
- event count or simulated physical work;
- robustness to predetermined jitter/missingness where relevant.

Energy may be claimed only if physically measured or clearly labelled as an engineering proxy.

Predefine an outcome hierarchy such as:

- FAIL / NULL;
- TECHNICALLY TRAINABLE;
- COMPETITIVE;
- DISTINCTIVE-LIGHTHOUSE EVIDENCE.

A distinctive claim requires preregistered ablations attributing performance to Lighthouse-specific structure such as delays, alpha-state memory, or first-hitting timing. Novelty still requires a separate literature gate.

## Negative controls and ablations

Freeze at least:

- no-delay ablation;
- no/weak-coupling or randomized-coupling control as appropriate;
- readout-only baseline;
- timing/jitter control where applicable;
- architecture-specific ablation capable of falsifying a Lighthouse-specific benefit claim.

## Existing local evidence boundary

Numerik v0.9/v0.10 learning and optimization smoke tests remain DEVELOPMENT EVIDENCE only.

They may inform software QA but may not:

- determine the final APP-3 test set;
- set success thresholds from favorable outcomes;
- count as confirmatory training replicates;
- be relabelled as held-out AI performance.

## Forbidden in this gate

- no model training;
- no benchmark execution;
- no held-out test inspection;
- no performance claim;
- no `2711xxx` use;
- no RB-015 relabelling;
- no active novelty positioning;
- no manuscript claim freeze.

## Required output when later activated

Create:

`research/app_diff_inference/ai_learning_scope_benchmark_preregistration_gate_0_1.md`

with:

- architecture and variant registry;
- task suite;
- baseline suite;
- data/split/seed plan;
- training/search/compute budgets;
- metrics and statistical aggregation;
- failure semantics;
- negative controls/ablations;
- anti-cherry-picking rules;
- proposed execution contract;
- PASS/CONDITIONAL/BLOCKED decision;
- STOP boundary.

After writing, APP-3 must return to MASTER. It must not self-authorize experiment execution.
