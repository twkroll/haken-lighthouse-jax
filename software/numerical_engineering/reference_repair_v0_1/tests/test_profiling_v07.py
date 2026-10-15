"""Fixed deterministic v0.7 engineering sanity tests (not scientific gates)."""
import numpy as np
from numpy.testing import assert_allclose
import jax
import jax.numpy as jnp
from lighthouse_dev.sparse import SparseParameters, physical_rerecord_sparse
from lighthouse_dev.reference import Parameters, physical_rerecord
from lighthouse_dev.sparse_replay import prepare_replay, replay_sparse_fixed_chart
from lighthouse_dev.rechart import rechart_batch
from lighthouse_dev.profiling import count_rerecord_work


def make_ring(n):
    mask=np.eye(n,dtype=bool)
    w=np.zeros((n,n));d=np.zeros((n,n))
    for j in range(n):
        neighbor=(j+1)%n
        mask[neighbor,j]=True
        w[j,j]=1.2+.007*j
        d[j,j]=.25+.002*j
        w[neighbor,j]=.4
        d[neighbor,j]=.57+.003*j
    dense=Parameters(w,d,adjacency=mask)
    return dense,SparseParameters.from_dense(dense),tuple((float(-3.-.009*j),) for j in range(n)),np.linspace(.23,5.81,n)


def sort_events(rec):
    return [(e.kind,e.neuron,e.source,e.ordinal) for e in rec.events]


def test_accounting_preserves_physical_record():
    _,p,h,t=make_ring(5)
    kw=dict(horizon=18.,history=h,initial_theta=t)
    expected=physical_rerecord_sparse(p,**kw)
    recorded,work=count_rerecord_work(p,**kw)
    assert expected.chart_valid and recorded.chart_valid
    assert recorded.token==expected.token
    assert_allclose(recorded.spike_times(),expected.spike_times(),atol=1e-11)
    assert work.phase_integral_requests>0
    assert work.adaptive_quad_calls>0
    assert work.spike_brent_roots>0
    assert work.event_count==len(expected.events)


def test_no_edges_do_not_trigger_adaptive_quadrature():
    p=SparseParameters(2,[],[],[],[])
    record,work=count_rerecord_work(p,horizon=18.5,initial_theta=np.array([0.,.2]))
    assert record.chart_valid
    assert work.adaptive_quad_calls==0
    assert work.phase_integral_requests>0


def test_counter_is_not_global_and_repeat_is_deterministic():
    _,p,h,t=make_ring(5)
    a,c1=count_rerecord_work(p,horizon=18.,history=h,initial_theta=t)
    b,c2=count_rerecord_work(p,horizon=18.,history=h,initial_theta=t)
    assert a.token==b.token and c1==c2


def test_sparse_dense_event_sequences_5():
    d,p,h,t=make_ring(5)
    kw=dict(horizon=18.,history=h,initial_theta=t)
    x=physical_rerecord(d,**kw);y=physical_rerecord_sparse(p,**kw)
    assert x.chart_valid and y.chart_valid
    assert sort_events(x)==sort_events(y)
    assert_allclose([e.t for e in x.events],[e.t for e in y.events],atol=1e-9,rtol=0)


def test_sparse_dense_event_sequences_12():
    d,p,h,t=make_ring(12)
    kw=dict(horizon=18.,history=h,initial_theta=t)
    x=physical_rerecord(d,**kw);y=physical_rerecord_sparse(p,**kw)
    assert x.chart_valid and y.chart_valid
    assert sort_events(x)==sort_events(y)
    assert_allclose([e.t for e in x.events],[e.t for e in y.events],atol=1e-9,rtol=0)


def test_state_sizes_scale_with_edges():
    for n in [5,12,24]:
        d,p,h,t=make_ring(n)
        assert p.e==2*n
        assert p.e*16 < n*n*16
        r=physical_rerecord_sparse(p,horizon=6.,history=h,initial_theta=t)
        assert r.initial_a.shape==(p.e,) and r.initial_q.shape==(p.e,)


def test_jit_replay_is_synced_and_matches_physical():
    _,p,h,t=make_ring(5)
    r=physical_rerecord_sparse(p,horizon=12.,history=h,initial_theta=t)
    assert r.chart_valid
    tape=prepare_replay(r,p)
    def f(weights,delays,theta):
        return replay_sparse_fixed_chart(weights,delays,theta,r,p,prepared=tape)
    fun=jax.jit(f)
    result=np.asarray(fun(jnp.asarray(p.weight),jnp.asarray(p.delay),jnp.asarray(t)))
    assert_allclose(result,r.spike_times(),atol=1e-7,rtol=0)


def test_jit_weight_jacobian_shape_and_finiteness():
    _,p,h,t=make_ring(5)
    r=physical_rerecord_sparse(p,horizon=12.,history=h,initial_theta=t)
    tape=prepare_replay(r,p)
    def f(weights):
        return replay_sparse_fixed_chart(weights,p.delay,t,r,p,prepared=tape)
    grads=np.asarray(jax.jit(jax.jacrev(f))(p.weight))
    assert grads.shape==(len(r.spikes),p.e)
    assert np.isfinite(grads).all()


def test_vmap_work_accounting_and_tape_bucket():
    _,p,h,t=make_ring(5)
    r=physical_rerecord_sparse(p,horizon=18.,history=h,initial_theta=t)
    weights=np.tile(p.weight,(4,1));weights[:,0]+=np.array([-1.5,-.5,.5,1.5])*1e-5
    result=rechart_batch(p,r,weights,replay=True)
    assert result.counts=={'SAME_CHART':4}
    assert len(result.buckets)==1 and result.vmap_calls==1
    assert result.physical_evaluations==5
    assert max(x.max_replay_error for x in result.entries)<1e-7


def test_batch_invalidity_is_explicit_not_dropped():
    _,p,h,t=make_ring(5)
    r=physical_rerecord_sparse(p,horizon=18.,history=h,initial_theta=t)
    weights=np.tile(p.weight,(3,1));weights[1,0]=float('nan')
    result=rechart_batch(p,r,weights,replay=False)
    assert [x.status for x in result.entries]==['SAME_CHART','INVALID_PARAMETER','SAME_CHART']
    assert result.physical_evaluations==3
