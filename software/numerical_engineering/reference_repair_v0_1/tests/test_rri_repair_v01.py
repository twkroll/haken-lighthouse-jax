"""RRI-01..RRI-08 deterministic engineering QA; NOT scientific evidence.

Fixtures and numerical thresholds fixed by PRE_REPAIR_CONTRACT_0_1.md.
"""
from dataclasses import replace
from math import pi
import numpy as np
import pytest
from scipy.integrate import quad
from scipy.optimize import brentq

from lighthouse_dev.reference import Parameters, physical_rerecord, response
from lighthouse_dev.sparse import SparseParameters, physical_rerecord_sparse
from lighthouse_dev.physical_first_hit_repair import PhysicalFirstHitUncertified, pulse_aware_integral
from lighthouse_dev.sparse_replay import derivative_record_sparse, guarded_batch_replay
from lighthouse_dev.fast_first_hit_gauss_v09 import physical_rerecord_gauss
from lighthouse_dev.fast_first_hit_quiet_v010 import physical_rerecord_quiet


def narrow_fixture():
    p=SparseParameters(1,np.array([0]),np.array([0]),np.array([4.]),np.array([1.5]),1000.,1.,0.1)
    return p,dict(horizon=20.,initial_theta=[2*pi-.005],history=[[-1.]])


def ordinary_fixture():
    w=np.array([[2.2,0.],[0.,2.5]])
    d=np.array([[.31,0.],[.83,.43]])
    mask=np.array([[1,0],[1,1]],bool)
    p=Parameters(w,d,adjacency=mask)
    return p,dict(horizon=40.,history=((-3.,-.5),(-2.2,)),initial_theta=[.3,1.1])


def compare(p,args,*,tol=2e-8):
    dense=physical_rerecord(p,**args)
    sparse=physical_rerecord_sparse(SparseParameters.from_dense(p),**args)
    assert dense.chart_valid == sparse.chart_valid
    assert dense.physical_certification == sparse.physical_certification
    assert [(e.kind,e.neuron,e.source,e.ordinal) for e in dense.events] == [
        (e.kind,e.neuron,e.source,e.ordinal) for e in sparse.events]
    np.testing.assert_allclose([e.t for e in dense.events],[e.t for e in sparse.events],atol=tol,rtol=0)
    np.testing.assert_allclose(dense.final_theta,sparse.final_theta,atol=3e-8,rtol=0)
    return sparse


def test_rri01_frozen_narrow_pulse_and_independent_segments():
    p,args=narrow_fixture();s=physical_rerecord_sparse(p,**args)
    assert s.chart_valid and s.physical_certification=='NUMENG_PULSE_AWARE_REFERENCE_V1'
    assert [e.kind for e in s.events]==['arrival','spike','arrival']
    assert abs(s.events[0].t-.5)<1e-12
    assert abs(s.events[2].t-s.events[1].t-1.5)<1e-12
    # Independent physical quadrature on predetermined small time intervals.
    def f(u): return response(4.*1e6*u*np.exp(-1000*u),1.,.1)
    knots=[0.,.0002,.0005,.001,.002,.004,.006,.01,.02,.04]
    def accumulated(x):
        k=[z for z in knots if z<x]+[x]
        return sum(quad(f,l,r,epsabs=1e-13,epsrel=1e-13,limit=400)[0] for l,r in zip(k[:-1],k[1:]))
    direct=0.5+brentq(lambda x:accumulated(x)-.005,.0001,.03,xtol=1e-13)
    assert abs(s.spikes[0].t-direct)<2e-9
    compare(p.to_dense(),args)


@pytest.mark.parametrize('alpha', [1.,30.,1000.])
def test_rri04_reference_equivalence_alpha_pulses(alpha):
    p=SparseParameters(1,[0],[0],[4.],[1.5],alpha,1.,.1)
    rec=compare(p.to_dense(),dict(horizon=12.,initial_theta=[2*pi-.005],history=[[-1.]]))
    assert rec.physical_certification=='NUMENG_PULSE_AWARE_REFERENCE_V1' if rec.chart_valid else rec.warnings


def test_rri04_silent_multicell_and_structural_zero():
    p=Parameters(np.zeros((3,3)),np.zeros((3,3)),adjacency=np.zeros((3,3),dtype=bool))
    compare(p,dict(horizon=12,initial_theta=[.1,.5,.8]))
    p,args=ordinary_fixture()
    rec=compare(p,args)
    assert rec.chart_valid


def test_rri05_budget_failclosed_integrator_and_physical_record(monkeypatch):
    with pytest.raises(PhysicalFirstHitUncertified,match='SEGMENT_BUDGET'):
        pulse_aware_integral(10.,0.,4e6,1000.,1.,.1,max_segments=1)
    p,args=narrow_fixture()
    from lighthouse_dev import sparse
    def fail(*_args,**_kw): raise PhysicalFirstHitUncertified('DETERMINISTIC_UNRESOLVED_NEGATIVE_CONTROL')
    monkeypatch.setattr(sparse,'_integrated',fail)
    rec=sparse.physical_rerecord_sparse(p,**args)
    assert not rec.chart_valid and rec.physical_certification=='INVALID'
    assert any('PHYSICAL_FIRST_HIT_UNCERTIFIED' in warning for warning in rec.warnings)


def test_rri05_horizon_collision_and_event_budget():
    p,args=ordinary_fixture()
    s=SparseParameters.from_dense(p)
    insufficient=physical_rerecord_sparse(s,**args,max_events=0)
    assert not insufficient.chart_valid and 'EVENT_BUDGET_EXCEEDED' in insufficient.warnings
    boundary=physical_rerecord_sparse(s,horizon=.33,history=((-3.,-.5),(-2.2,)),initial_theta=[.3,1.1])
    assert not boundary.chart_valid


def test_rri06_jax_rejects_incomplete_stale_and_unverified():
    p,args=ordinary_fixture();s=SparseParameters.from_dense(p)
    rec=physical_rerecord_sparse(s,**args)
    assert rec.chart_valid
    good=derivative_record_sparse(s,rec)
    assert good.max_reference_disagreement<1e-7
    short=replace(rec,events=rec.events[:-1],spikes=tuple(e for e in rec.spikes if e in rec.events[:-1]))
    with pytest.raises(ValueError,match='Stale/invalid'):
        derivative_record_sparse(s,short)
    old=replace(rec,physical_certification='UNVERIFIED')
    with pytest.raises(ValueError,match='Stale/invalid'):
        derivative_record_sparse(s,old)
    perturbed=tuple(replace(e,t=e.t+.02) for e in rec.events)
    stale=replace(rec,events=perturbed)
    with pytest.raises(ValueError,match='Stale/invalid'):
        derivative_record_sparse(s,stale)
    with pytest.raises(ValueError,match='Stale/invalid'):
        guarded_batch_replay(s,old,np.stack([s.weight]))


def test_rri06_narrow_pulse_replay_numerical_agreement():
    p,args=narrow_fixture()
    rec=physical_rerecord_sparse(p,**args)
    d=derivative_record_sparse(p,rec)
    assert d.max_reference_disagreement <=1e-8
    assert np.isfinite(d.d_times_d_edge_weights).all()


def test_rri07_dense_sparse_equivalence_zero_weight():
    p,args=ordinary_fixture()
    compare(p,args)
    s=SparseParameters.from_dense(p)
    assert any(x==0 for x in s.weight)


@pytest.mark.parametrize('reference',[physical_rerecord_gauss,physical_rerecord_quiet])
def test_rri08_accelerated_existing_alternates(reference):
    p,args=ordinary_fixture();s=SparseParameters.from_dense(p)
    ground=physical_rerecord_sparse(s,**args)
    candidate=reference(s,**args)
    assert candidate.chart_valid == ground.chart_valid
    assert candidate.token==ground.token
    np.testing.assert_allclose([x.t for x in candidate.events],[x.t for x in ground.events],rtol=0,atol=2e-8)


def test_rri05_simultaneous_regular_spikes_invalid_chart():
    p=SparseParameters(2,[],[],[],[],1.,1.,-1.)
    rec=physical_rerecord_sparse(p,horizon=3.,initial_theta=[6.,6.])
    assert len(rec.spikes)==2
    assert not rec.chart_valid
    assert any('EVENT_CHART_COLLISION' in x for x in rec.warnings)


def test_rri06_regular_chart_finite_difference_against_jax():
    p,args=ordinary_fixture()
    sp=SparseParameters.from_dense(p)
    rec=physical_rerecord_sparse(sp,**args)
    deriv=derivative_record_sparse(sp,rec)
    idx=int(np.flatnonzero(sp.weight==0.)[0]);eps=1e-4
    wp=sp.weight.copy();wm=sp.weight.copy();wp[idx]+=eps;wm[idx]-=eps
    rplus=physical_rerecord_sparse(sp.with_weights(wp),**args)
    rminus=physical_rerecord_sparse(sp.with_weights(wm),**args)
    assert rplus.chart_valid and rminus.chart_valid and rplus.token==rec.token==rminus.token
    fd=(rplus.spike_times()-rminus.spike_times())/(2*eps)
    np.testing.assert_allclose(deriv.d_times_d_edge_weights[:,idx],fd,atol=3e-5,rtol=0)
