# CORE status pointer v0.17

Current versioned mathematical source of truth for graph scaling is:

- `docs/core/graph_batch_scaling_v0.17.md`
- `benchmarks/core_v017_reference.json`
- `reference/core_v017_graph_queue_kernel.py`
- `reference/core_v017_graph_batch_scaling.py`

CORE v0.17 generalizes the fixed-capacity JAX packet queue from the hard-coded N=3 ring to sparse directed graph tensors while preserving the v0.16 ring as an exact specialization. It adds state batching, equal-shape graph-parameter batching, edge-order invariance, continuous edge-weight differentiation inside a fixed event chart, and structural scaling checks through N=256.

Benchmark contract: B247--B268.

The historical `docs/core/mathematical_core.md` remains intentionally unchanged; versioned documents carry later CORE results.
