"""Noncanonical deterministic work accounting for physical sparse rerecords.

Counts operations without asserting a performance model or modifying physical
semantics. Patches module-local functions temporarily: use sequentially only.
"""
from dataclasses import dataclass
from unittest.mock import patch
from . import sparse, physical_first_hit_repair as physical_quad


@dataclass(frozen=True)
class WorkCount:
    phase_integral_requests: int
    adaptive_quad_calls: int
    spike_brent_roots: int
    event_count: int
    spike_count: int
    n: int
    structural_edges: int


def count_rerecord_work(p: sparse.SparseParameters, **kwargs):
    """Return `(fresh_record, counters)` without any stochastic evaluation.

    This is a development-only single-process instrumenter. It must not be used
    concurrently because patching temporary module globals is not thread-safe.
    """
    counts=dict(phase_integral_requests=0,adaptive_quad_calls=0,spike_brent_roots=0)
    original_integrated=sparse._integrated
    original_quad=physical_quad.quad
    original_brentq=sparse.brentq

    def integrate(*a,**k):
        counts['phase_integral_requests']+=1
        return original_integrated(*a,**k)
    def quad(*a,**k):
        counts['adaptive_quad_calls']+=1
        return original_quad(*a,**k)
    def brentq(*a,**k):
        counts['spike_brent_roots']+=1
        return original_brentq(*a,**k)

    with patch.object(sparse,'_integrated',integrate),patch.object(physical_quad,'quad',quad),patch.object(sparse,'brentq',brentq):
        rec=sparse.physical_rerecord_sparse(p,**kwargs)
    return rec,WorkCount(**counts,event_count=len(rec.events),
                         spike_count=len(rec.spikes),n=p.n,structural_edges=p.e)
