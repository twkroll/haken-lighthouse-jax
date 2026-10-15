# Reference/Rerecord Repair 0.1 — development-only changelog

- Frozen PRE_REPAIR_CONTRACT_0_1 before repair outputs, SHA-256: a0a7742b53159a204e815f72d7d7e53aff293825e5901fcd684b6e98f01188d4
- Pulse-aware physical quadrature and named fail-closed errors, with analytic alpha-tail bound and interval splitting.
- Dense and sparse rerecording share the same physical reference; no modified RB-004 equations.
- Physical certification tag added to high-level reference records; JAX derivative guards reject incomplete, stale or uncertified tapes.
- JAX fast-alpha nodes cluster near impulse onset for alpha>=100; original nodes preserved for alpha<100. Both remain physically checked.
- Legacy Gauss API routed to corrected reference; instrumentation counts the new physical quadrature calls.
- 180/180 original split-module tests and aggregate 194/194 incl. 14 new RRI tests, clean exits.
- 139-file repaired working-tree manifest, preserved original 137-file intake and original defective 33-line manifest.

No AI benchmarks/confirmation, no protected RNGs, no canonical scientific freeze changed.
