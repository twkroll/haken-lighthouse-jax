# CORE status through v0.16

CORE v0.16 completes the first shape-static JAX implementation of the certified three-cell adaptive Lighthouse packet model.

## Certified layers

- v0.1--v0.11: exact model, continuation, Floquet theory, normal forms, Chenciner point, exact small invariant circles and local FIC.
- v0.12: adaptive slow-fast reduction and dynamic-bifurcation skip.
- v0.13: causal in-flight remaining-distance semantics.
- v0.14: full imperative adaptive packet-queue event engine and global bistability.
- v0.15: large quasiperiodic hybrid invariant circle and global hybrid circle fold.
- v0.16: fixed-capacity JAX queue, fixed-chart event tangents, dynamic-skip reproduction, and global-circle stability/fold reproduction.

## v0.16 assets

- `jax_packet_queue_v0.16.md`
- `../../benchmarks/core_v016_reference.json`
- `../../reference/core_v016_jax_queue_kernel.py`
- `../../reference/core_v016_jax_queue_tangent.py`
- `../../reference/core_v016_jax_packet_queue.py`

The N=3 reference queue has compile-time capacity `Qmax=12`; the certified benchmark region has observed at most six simultaneously active packets.

The value scheduler is shape-static and JIT-compatible. Scientific derivatives are certified only inside a fixed event chart. Event-order switching surfaces remain explicit hybrid singularities and are not assigned artificial `argmin` gradients.

The default v0.16 reference checks frozen recovery, the full `epsilon=1e-5` dynamic-skip passage, firing and arrival chart tangents, and the stored direct JAX global-circle fold data. `--stable-direct` reruns a bounded direct stable-circle normal-return regression. `--unstable-direct` validates the stored tight edge-circle audit and its saddle-node reciprocal consistency.

## Next

CORE v0.17 should generalize the static queue from the special three-cell ring to sparse directed graph tensors with batched packet slots, capacity laws, scalable event selection and vmap/pmap-ready simulation. The N=3 v0.16 kernel remains the oracle: graph generalization is accepted only if it reproduces v0.16 values and chart tangents when specialized back to the ring.
