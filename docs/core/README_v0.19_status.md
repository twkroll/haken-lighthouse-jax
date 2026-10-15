# CORE status: v0.19

CORE v0.19 adds a hybrid trust-region / multi-chart optimizer for the v0.18 inverse problem.

The reference optimizer:

- uses fixed-shape event-token arrays so one JAX replay/Jacobian kernel is reused across physical charts;
- predicts distance to the nearest chart collision from the chart margin and its gradient;
- shortens a Gauss--Newton step before a nonpositive margin;
- crosses only through the physical event scheduler;
- rerecords the event chart after crossing;
- resumes differentiation with the new one-sided Jacobian;
- reproduces the true `(p,tau3)` from starts on either side of the firing-order boundary.

Reference assets:

- `docs/core/hybrid_multichart_optimizer_v0.19.md`
- `benchmarks/core_v019_reference.json`
- `reference/core_v019_multichart_optimizer.py`
- benchmark contract B289--B308

The project rule remains: topology and event-order choices are discrete. JAX differentiates continuous dynamics inside one valid event chart; it does not manufacture a global derivative through event `argmin` switches.
