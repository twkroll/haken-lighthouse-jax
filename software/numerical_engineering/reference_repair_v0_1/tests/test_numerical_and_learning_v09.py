"""Local v0.9 development checks, not a canonical scientific gate."""
from math import pi
import numpy as np
import pytest
from demo_performance_v07 import ring
from lighthouse_dev.sparse import SparseParameters, physical_rerecord_sparse
from lighthouse_dev.fast_first_hit import physical_rerecord_cached
from lighthouse_dev.fast_first_hit_gauss_v09 import physical_rerecord_gauss
from lighthouse_dev.gauss_integral_v09 import gl_integrated
from lighthouse_dev import sparse


def assert_same_record(ref,got, tol=1e-8):
    assert tuple(x.signature() for x in ref.events)==tuple(x.signature() for x in got.events)
    assert ref.token==got.token
    assert ref.chart_valid == got.chart_valid
    assert ref.warnings == got.warnings
    assert np.allclose(ref.final_theta,got.final_theta,atol=tol,rtol=0.)
    assert max([abs(x.t-y.t) for x,y in zip(ref.events,got.events)] or [0])<tol

@pytest.mark.parametrize('n',[1,5,12,24])
def test_same_events_ring(n):
    if n==1:
        p=SparseParameters(1,np.array([0]),np.array([0]),np.array([3.]),np.array([1.]))
        h=[[-3.]]; theta=[0.3]
    else:
        _,p,h,theta=ring(n)
    kw=dict(horizon=18.,history=h,initial_theta=theta)
    assert_same_record(physical_rerecord_cached(p,**kw),physical_rerecord_gauss(p,**kw))

@pytest.mark.parametrize('alpha',[0.2,0.5,1.,2.,5.])
def test_alpha_event_variants(alpha):
    _,p,h,theta=ring(5)
    p=SparseParameters(p.n,p.target,p.source,p.weight,p.delay,alpha=alpha,r=p.r,h=p.h)
    kw=dict(horizon=18.,history=h,initial_theta=theta)
    assert_same_record(physical_rerecord_cached(p,**kw),physical_rerecord_gauss(p,**kw))

@pytest.mark.parametrize('factor',[-1.,0.,0.1,1.,2.])
def test_weight_event_variants(factor):
    _,p,h,theta=ring(5)
    p=p.with_weights(p.weight*factor)
    kw=dict(horizon=18.,history=h,initial_theta=theta)
    assert_same_record(physical_rerecord_cached(p,**kw),physical_rerecord_gauss(p,**kw))


def test_quadrature_wide_grid():
    # Combinatorial deterministic stress fixture, not an external or scientific dataset.
    for k in range(210):
        alpha=(0.18,0.5,1.,3.,15.,80.)[k%6]
        r=(0.25,1.,2.)[(k//6)%3]
        h=(-1.,-0.1,0.,0.4)[(k//18)%4]
        w=(-5.,-1.,0.,1.,7.)[(k//72)%5]
        a=(0.,0.1,1.,5.)[(k*7)%4]
        q=(0.,0.2,5.,50.)[(k*13)%4]
        dt=(0.03,0.3,1.,7.,30.)[(k*17)%5]
        p=SparseParameters(1,np.array([0]),np.array([0]),np.array([w]),np.array([0.5]),
                           alpha=alpha,r=r,h=h)
        ref=sparse._integrated(0,dt,np.array([a]),np.array([q]),p)
        got=gl_integrated(0,dt,np.array([a]),np.array([q]),p)
        assert abs(got-ref)<5e-9*(1+abs(ref)),(k,ref,got)


def test_collision_warning_preserved():
    p=SparseParameters(1,np.array([0]),np.array([0]),np.array([1.]),np.array([0.5]))
    # historical packet reaches t=0 boundary
    kw=dict(horizon=10.,initial_theta=[2*pi-0.5],history=[[-0.5]])
    assert_same_record(physical_rerecord_cached(p,**kw),physical_rerecord_gauss(p,**kw))


def test_exact_no_events():
    p=SparseParameters(2,np.array([],int),np.array([],int),np.array([]),np.array([]),h=0.)
    kw=dict(horizon=15.,initial_theta=[0.,0.],history=[[],[]])
    assert_same_record(physical_rerecord_cached(p,**kw),physical_rerecord_gauss(p,**kw))

@pytest.mark.parametrize('alpha',[100.,300.,1000.])
@pytest.mark.parametrize('threshold',[0.,0.1,1.])
@pytest.mark.parametrize('weight',[0.1,1.,4.])
def test_fast_alpha_pulse_segmented_reference(alpha,threshold,weight):
    """Narrow pulse test: unsegmented SciPy quad can silently miss it."""
    from scipy.integrate import quad
    from lighthouse_dev.reference import response
    p=SparseParameters(1,np.array([0]),np.array([0]),np.array([weight]),
                       np.array([0.7]),alpha=alpha,r=1,h=threshold)
    a=np.array([0.]);q=np.array([alpha**2])
    f=lambda t:response(weight*alpha**2*t*np.exp(-alpha*t),1.,threshold)
    ref=quad(f,0,20,points=[1/alpha,5/alpha,20/alpha],
             epsabs=1e-12,epsrel=1e-12,limit=300)[0]
    assert abs(ref-gl_integrated(0,20,a,q,p))<1e-10


def test_synthetic_one_weight_optimizer_smoke():
    # Pure engineering; no benchmark against a second learner is claimed.
    from demo_trainability_v09 import run
    data=run()
    assert data['optimizer_success']
    assert abs(data['estimated_weight']-data['teacher_weight'])<1e-4
    assert data['holdout_abs_error']<1e-4
