"""Prospectively frozen extra Gate-0.2 stale-batch guard QA addendum.
Separate from original predeclared stress matrix; software repair only.
"""
from dataclasses import replace
import numpy as np
import pytest
from lighthouse_dev.reference import Parameters
from lighthouse_dev.sparse import SparseParameters,physical_rerecord_sparse
from lighthouse_dev.sparse_replay import guarded_batch_replay,derivative_record_sparse


def fixture():
    w=np.array([[2.2,0.],[0.,2.5]])
    d=np.array([[.31,0.],[.83,.43]])
    adj=np.array([[1,0],[1,1]],bool)
    p=SparseParameters.from_dense(Parameters(w,d,adjacency=adj))
    rec=physical_rerecord_sparse(p,horizon=40.,initial_theta=[.3,1.1],history=((-3.,-.5),(-2.2,)))
    assert rec.chart_valid and rec.physical_certification=='NUMENG_PULSE_AWARE_REFERENCE_V1'
    return p,rec

@pytest.mark.parametrize('kind',['shifted_times','truncated','unverified','spike_list','initial_a','initial_q','final_phase'])
def test_negative_stale_batch_tape_rejected(kind):
    p,rec=fixture()
    if kind=='shifted_times':stale=replace(rec,events=tuple(replace(e,t=e.t+.02) for e in rec.events))
    elif kind=='truncated':stale=replace(rec,events=rec.events[:-1],spikes=tuple(e for e in rec.spikes if e in rec.events[:-1]))
    elif kind=='unverified':stale=replace(rec,physical_certification='UNVERIFIED')
    elif kind=='spike_list':stale=replace(rec,spikes=rec.spikes[:-1])
    elif kind=='initial_a':stale=replace(rec,initial_a=rec.initial_a+.01)
    elif kind=='initial_q':stale=replace(rec,initial_q=rec.initial_q+.01)
    elif kind=='final_phase':stale=replace(rec,final_theta=rec.final_theta+.01)
    else:raise AssertionError(kind)
    with pytest.raises(ValueError,match='Stale/invalid'):
        guarded_batch_replay(p,stale,np.stack([p.weight]))
    with pytest.raises(ValueError,match='Stale/invalid'):
        derivative_record_sparse(p,stale)


def test_positive_batch_base_and_same_chart_small_weight_perturbation():
    p,rec=fixture();w2=p.weight.copy();w2[int(np.where(p.weight==0)[0][0])]+=1e-5
    got=guarded_batch_replay(p,rec,np.stack([p.weight,w2]))
    assert got.shape==(2,len(rec.spikes))
    assert np.isfinite(got).all()
    ref2=physical_rerecord_sparse(p.with_weights(w2),horizon=rec.horizon,initial_theta=rec.initial_theta,history=rec.history)
    assert ref2.chart_valid and ref2.token==rec.token
    np.testing.assert_allclose(got[0],rec.spike_times(),atol=1e-7,rtol=0)
    np.testing.assert_allclose(got[1],ref2.spike_times(),atol=1e-7,rtol=0)
