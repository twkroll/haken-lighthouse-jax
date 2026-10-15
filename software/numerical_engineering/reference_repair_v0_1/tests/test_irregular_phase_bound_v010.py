"""Noncanonical engineering validation of a stronger first-hit exclusion bound."""
import numpy as np
import pytest
from lighthouse_dev.sparse import SparseParameters
from lighthouse_dev.irregular_fixtures_v010 import irregular_fixture
from lighthouse_dev.phase_bound_v010 import phase_rate_upper,psi_upper_interval
from lighthouse_dev.fast_first_hit_gauss_v09 import physical_rerecord_gauss
from lighthouse_dev.fast_first_hit_bound_v010 import physical_rerecord_phase_bound
from lighthouse_dev.fast_first_hit import physical_rerecord_cached


def same(ref, other, tol=1e-8):
    assert [x.signature() for x in ref.events] == [x.signature() for x in other.events]
    assert ref.token == other.token
    assert ref.chart_valid == other.chart_valid
    assert ref.warnings == other.warnings
    assert len(ref.events) == len(other.events)
    assert max([abs(x.t-y.t) for x,y in zip(ref.events,other.events)] or [0]) < tol
    assert np.allclose(ref.final_theta,other.final_theta,atol=tol,rtol=0)


@pytest.mark.parametrize('A,Q,alpha,dt',[
    (2.,4.,1.,3.),(-1.,8.,1.,5.),(1.,-3.,2.,3.),
    (-5.,-3.,1.,4.),(0.,0.,1.,5.),(1.,0.,1.,6.),
    (-2.,0.,1.,6.),(-2.,3.,0.5,10.),(4.,-20.,3.,1.)
])
def test_upper_envelope_against_dense_analytic_grid(A,Q,alpha,dt):
    p=SparseParameters(1,np.array([0]),np.array([0]),np.array([1.]),np.array([.1]),alpha=alpha)
    bound=psi_upper_interval(0,dt,np.array([A]),np.array([Q]),p)
    grid=np.linspace(0,dt,10001)
    arr=np.exp(-alpha*grid)*(A+grid*Q)
    assert bound >= np.max(arr)-1e-13
    v=phase_rate_upper(0,dt,np.array([A]),np.array([Q]),p)
    assert 0<=v<=1


@pytest.mark.parametrize('n,degree',[(5,2),(7,3),(12,2),(12,4),(24,3)])
def test_irregular_record_equivalence(n,degree):
    p,h,th=irregular_fixture(n,degree)
    kw=dict(horizon=18.,history=h,initial_theta=th)
    ref=physical_rerecord_gauss(p,**kw)
    new=physical_rerecord_phase_bound(p,**kw)
    assert ref.chart_valid,ref.warnings
    same(ref,new)


@pytest.mark.parametrize('n,degree',[(5,3),(12,3)])
def test_reference_scipy_v010_equivalence(n,degree):
    p,h,th=irregular_fixture(n,degree)
    kw=dict(horizon=14.,history=h,initial_theta=th)
    ref=physical_rerecord_cached(p,**kw)
    got=physical_rerecord_phase_bound(p,**kw)
    assert ref.chart_valid, ref.warnings
    same(ref,got)


@pytest.mark.parametrize('weight',[-1.,0.,1.,5.])
def test_frozen_structure_at_zero_and_negative_weights(weight):
    p,h,th=irregular_fixture(5,3)
    p=p.with_weights(np.full(p.e,weight))
    kw=dict(horizon=13.,history=h,initial_theta=th)
    same(physical_rerecord_gauss(p,**kw),physical_rerecord_phase_bound(p,**kw))


@pytest.mark.parametrize('alpha',[.2,1.,5.,100.])
def test_alpha_stress(alpha):
    p,h,th=irregular_fixture(5,2,alpha=alpha)
    kw=dict(horizon=14.,history=h,initial_theta=th)
    same(physical_rerecord_gauss(p,**kw),physical_rerecord_phase_bound(p,**kw))


def test_empty_network_no_spike():
    p=SparseParameters(2,np.array([],int),np.array([],int),np.array([]),np.array([]),h=0.)
    kw=dict(horizon=15.,initial_theta=[0.,0.],history=[[],[]])
    same(physical_rerecord_gauss(p,**kw),physical_rerecord_phase_bound(p,**kw))


def test_collision_preserved():
    p=SparseParameters(1,np.array([0]),np.array([0]),np.array([1.]),np.array([.5]))
    kw=dict(horizon=10.,initial_theta=[6.0],history=[[-.5]])
    same(physical_rerecord_gauss(p,**kw),physical_rerecord_phase_bound(p,**kw))


def test_jax_replay_compatible_with_bound_record_and_ad_fd():
    import jax
    import jax.numpy as jnp
    from lighthouse_dev.sparse_replay import prepare_replay,replay_sparse_fixed_chart
    p,h,th=irregular_fixture(5,2)
    kw=dict(horizon=18.,history=h,initial_theta=th)
    rec=physical_rerecord_phase_bound(p,**kw)
    assert rec.chart_valid
    tape=prepare_replay(rec,p)
    f=lambda w: replay_sparse_fixed_chart(w,jnp.asarray(p.delay),jnp.asarray(th),rec,p,prepared=tape)
    times=np.asarray(f(jnp.asarray(p.weight)))
    assert np.max(np.abs(times-rec.spike_times()))<1e-8
    # Compare an actual local derivative against a new physical rerecord in BOTH directions.
    eid=int(np.flatnonzero((p.target==0)&(p.source==0))[0])
    tangent=np.zeros(p.e);tangent[eid]=1.
    _,ad=jax.jvp(f,(jnp.asarray(p.weight),),(jnp.asarray(tangent),))
    eps=1e-4
    wp=p.weight.copy();wm=p.weight.copy();wp[eid]+=eps;wm[eid]-=eps
    rp=physical_rerecord_phase_bound(p.with_weights(wp),**kw)
    rm=physical_rerecord_phase_bound(p.with_weights(wm),**kw)
    assert rp.chart_valid and rm.chart_valid and rp.token==rm.token==rec.token
    fd=(rp.spike_times()-rm.spike_times())/(2*eps)
    assert np.allclose(np.asarray(ad),fd,atol=5e-5,rtol=3e-4)


@pytest.mark.parametrize('n,degree,scale,threshold',[
    (5,2,0.1,0.05),(5,3,0.3,0.2),(5,3,1.,0.1),
    (12,3,0.1,0.4),(12,3,0.3,0.1),(12,3,1.,0.2),
    (24,3,0.1,0.3),(24,3,0.5,0.4),
])
def test_exact_silent_variant(n,degree,scale,threshold):
    from lighthouse_dev.fast_first_hit_quiet_v010 import physical_rerecord_quiet
    p,h,th=irregular_fixture(n,degree)
    p=SparseParameters(n,p.target,p.source,p.weight*scale,p.delay,p.alpha,p.r,threshold)
    kw=dict(horizon=18.,history=h,initial_theta=th)
    base=physical_rerecord_gauss(p,**kw)
    alt=physical_rerecord_quiet(p,**kw)
    same(base,alt)


def test_quiet_bounds_negative_weights_and_zero():
    from lighthouse_dev.fast_first_hit_quiet_v010 import physical_rerecord_quiet
    p,h,th=irregular_fixture(5,3)
    p=SparseParameters(p.n,p.target,p.source,-abs(p.weight),p.delay,p.alpha,p.r,0.2)
    kw=dict(horizon=18.,history=h,initial_theta=th)
    same(physical_rerecord_gauss(p,**kw),physical_rerecord_quiet(p,**kw))
