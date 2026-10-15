"""Non-threadsafe sequential counters for the *alternative* v0.8 scheduler."""
from dataclasses import dataclass
from unittest.mock import patch
from . import fast_first_hit, sparse, physical_first_hit_repair as physical_quad

@dataclass(frozen=True)
class FastWorkCount:
    phase_integral_requests: int
    adaptive_quad_calls: int
    spike_brent_roots: int
    event_count: int
    spike_count: int
    n: int
    structural_edges: int


def count_cached_work(p, **kwargs):
    counts=dict(phase_integral_requests=0,adaptive_quad_calls=0,spike_brent_roots=0)
    original_integrated=fast_first_hit._integrated
    original_quad=physical_quad.quad
    original_brentq=fast_first_hit.brentq
    def integrate(*args,**kw):
        counts['phase_integral_requests']+=1
        return original_integrated(*args,**kw)
    def quad(*args,**kw):
        counts['adaptive_quad_calls']+=1
        return original_quad(*args,**kw)
    def root(*args,**kw):
        counts['spike_brent_roots']+=1
        return original_brentq(*args,**kw)
    with patch.object(fast_first_hit,'_integrated',integrate),patch.object(physical_quad,'quad',quad),patch.object(fast_first_hit,'brentq',root):
        rec=fast_first_hit.physical_rerecord_cached(p,**kwargs)
    return rec,FastWorkCount(**counts,event_count=len(rec.events),spike_count=len(rec.spikes),n=p.n,structural_edges=p.e)
