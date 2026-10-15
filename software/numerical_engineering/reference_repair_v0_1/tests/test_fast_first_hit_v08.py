"""Deterministic independent engineering tests; no governed science execution."""
import numpy as np
import pytest
from numpy.testing import assert_allclose
from lighthouse_dev.sparse import SparseParameters,physical_rerecord_sparse
from lighthouse_dev.fast_first_hit import physical_rerecord_cached
from lighthouse_dev.profiling import count_rerecord_work
from lighthouse_dev.fast_profiling import count_cached_work
from demo_performance_v07 import ring


def compare(p, **kwargs):
    a=physical_rerecord_sparse(p, **kwargs)
    b=physical_rerecord_cached(p, **kwargs)
    assert [x.signature() for x in a.events] == [x.signature() for x in b.events]
    assert a.chart_valid == b.chart_valid
    assert a.warnings == b.warnings
    assert a.token == b.token
    assert_allclose([x.t for x in a.events],[x.t for x in b.events],atol=1e-9,rtol=0)
    assert_allclose(a.final_theta,b.final_theta,atol=1e-9,rtol=0)
    assert_allclose(a.initial_a,b.initial_a,atol=0,rtol=0)
    assert_allclose(a.initial_q,b.initial_q,atol=0,rtol=0)
    return a,b


@pytest.mark.parametrize('n',[5,12,24])
def test_ring_complete_tape_and_state(n):
    _,p,h,theta=ring(n)
    a,b=compare(p,horizon=18.,history=h,initial_theta=theta)
    assert a.chart_valid and len(a.events)>0


def test_zero_edges_isolated_clock():
    p=SparseParameters(1,[],[],[],[])
    a,b=compare(p,horizon=20.,initial_theta=np.array([0.]))
    assert len(a.spikes)==1
    assert_allclose(b.spike_times(),[2*np.pi*np.e],atol=1e-10)


def test_no_event_quiescence():
    p=SparseParameters(1,[],[],[],[],h=0.)
    a,b=compare(p,horizon=20.)
    assert len(a.events)==0
    assert not np.any(b.final_theta)


def test_multiple_preexisting_packets_and_future_arrivals():
    p=SparseParameters(2,[0,1,1],[0,0,1],[2.2,0.,2.5],[.31,.83,.43])
    a,b=compare(p,horizon=40.,initial_theta=np.array([.3,1.1]),history=((-3.,-.5),(-2.2,)))
    assert a.chart_valid and len(b.spikes)>=3


def test_zero_weight_signs_keep_topology():
    p=SparseParameters(2,[0,1,1],[0,0,1],[2.2,0.,2.5],[.31,.83,.43])
    for weight in (-1e-4,0.,1e-4):
        w=p.weight.copy();w[1]=weight
        compare(p.with_weights(w),horizon=40.,initial_theta=np.array([.3,1.1]),history=((-3.,-.5),(-2.2,)))


@pytest.mark.parametrize('delta',[-1e-4,0.,1e-4])
def test_arrival_spike_collision_and_chart_boundary(delta):
    T=2*np.pi*np.e
    p=SparseParameters(1,[0],[0],[0.],[2.+T+delta])
    a,b=compare(p,horizon=T+1.,history=((-2.,),))
    assert a.chart_valid == (delta != 0)


def test_initial_history_arrival_at_zero():
    p=SparseParameters(1,[0],[0],[3.],[.5])
    a,b=compare(p,horizon=20.,history=((-0.5,),))
    assert not a.chart_valid and 'INITIAL_ARRIVAL_CHART_BOUNDARY' in b.warnings


def test_zero_delay_after_spike():
    p=SparseParameters(1,[0],[0],[0.],[0.])
    a,b=compare(p,horizon=20.)
    assert not a.chart_valid
    assert any('ZERO_DELAY' in x for x in b.warnings)


def test_spike_spike_exact_collision():
    p=SparseParameters(2,[],[],[],[])
    a,b=compare(p,horizon=19.,initial_theta=np.zeros(2))
    assert not b.chart_valid and any('COLLISION' in x for x in b.warnings)


def test_horizon_first_hit_boundary():
    p=SparseParameters(1,[],[],[],[])
    a,b=compare(p,horizon=2*np.pi*np.e)
    assert not b.chart_valid and any('HORIZON' in x for x in b.warnings)


def test_adaptive_solver_saves_integral_work_in_existing_fixture():
    _,p,h,theta=ring(5)
    kw=dict(horizon=18.,history=h,initial_theta=theta)
    a,original=count_rerecord_work(p,**kw)
    b,optimized=count_cached_work(p,**kw)
    assert a.token==b.token and a.chart_valid and b.chart_valid
    assert original.spike_brent_roots == optimized.spike_brent_roots
    assert optimized.phase_integral_requests < original.phase_integral_requests
    assert optimized.adaptive_quad_calls < original.adaptive_quad_calls


def test_no_quad_for_no_edge_case():
    p=SparseParameters(1,[],[],[],[])
    a,c=count_cached_work(p,horizon=20.)
    assert c.adaptive_quad_calls==0
    assert len(a.spikes)==1


def test_validation_errors_agree():
    p=SparseParameters(1,[],[],[],[])
    for kw in ({'horizon':0},{'horizon':-1},{'horizon':20,'initial_theta':[7]},{'horizon':20,'initial_theta':[np.nan]}):
        with pytest.raises(ValueError): physical_rerecord_sparse(p,**kw)
        with pytest.raises(ValueError): physical_rerecord_cached(p,**kw)


def test_multiple_regimes_independent_parameters():
    cases=[
      SparseParameters(1,[0],[0],[4.],[.7],alpha=.8,r=.5,h=-.3),
      SparseParameters(1,[0],[0],[-2.],[1.1],alpha=1.7,r=2.,h=-1.4),
      SparseParameters(2,[0,1],[0,1],[.7,1.2],[.6,.8],alpha=2.1,r=.7,h=-2.),
    ]
    for p in cases:
        compare(p,horizon=33.,history=tuple((float(-2.5-.11*i),) for i in range(p.n)),initial_theta=np.linspace(.1,1.2,p.n))


def test_zero_duration_initial_arrival_warning_matches():
    p=SparseParameters(1,[0],[0],[2.],[0.5])
    a,b=compare(p,horizon=20.,history=((-0.5,),))
    assert not a.chart_valid


def test_cached_record_can_be_used_for_guarded_fixed_chart_jax():
    # V0.8 scheduler must not create a new event ordering for a given chart.
    from lighthouse_dev.sparse_replay import prepare_replay, replay_sparse_fixed_chart
    from lighthouse_dev.rechart import rechart_batch
    _,p,h,theta=ring(5)
    rec=physical_rerecord_cached(p,horizon=12.,history=h,initial_theta=theta)
    assert rec.chart_valid
    tape=prepare_replay(rec,p)
    import jax.numpy as jnp
    prediction=np.asarray(replay_sparse_fixed_chart(
        jnp.asarray(p.weight),jnp.asarray(p.delay),jnp.asarray(theta),rec,p,prepared=tape))
    assert_allclose(prediction,rec.spike_times(),atol=1e-7,rtol=0)
    batch=rechart_batch(p,rec,np.tile(p.weight,(2,1)),replay=False)
    assert batch.counts=={'SAME_CHART':2}
