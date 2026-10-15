"""Noncanonical deterministic engineering; chart guards, not scientific inference."""
import numpy as np
import pytest
from lighthouse_dev.reference import Parameters
from lighthouse_dev.sparse import SparseParameters,physical_rerecord_sparse
from lighthouse_dev.chart_validation import chart_margins,perturbation_check,five_point_probe


def regular():
    mask=np.array([[True,False],[True,True]])
    w=np.array([[2.2,0.],[0.,2.5]])
    delays=np.array([[.31,0.],[.83,.43]])
    p=SparseParameters.from_dense(Parameters(w,delays,adjacency=mask))
    h=((-3.,-.5),(-2.2,))
    th=np.array([.3,1.1]);rec=physical_rerecord_sparse(p,horizon=40.,initial_theta=th,history=h)
    assert rec.chart_valid
    return p,rec


def boundary():
    p,rec=regular()
    d=p.delay.copy();d[1]=.5002 # historic spike at -0.5 arrives just AFTER t=0
    p=p.with_delays(d)
    rec=physical_rerecord_sparse(p,horizon=40.,initial_theta=rec.initial_theta,history=rec.history)
    assert rec.chart_valid,rec.warnings
    return p,rec


def test_positive_margins_and_consistent_event_counts():
    p,r=regular()
    m=chart_margins(p,r)
    assert m.chart_valid and m.event_count==len(r.events) and m.spike_count==len(r.spikes)
    assert m.min_event_separation>0 and m.min_endpoint_separation>0
    assert m.min_history_arrival_separation>0 and m.min_spike_velocity>0


def test_five_point_weights_at_exact_zero():
    p,r=regular(); probe=five_point_probe(p,r,'weight',1,step=1e-4)
    assert probe.status=='PASS',probe
    assert probe.max_absolute_error < 1e-6
    assert max(abs(x) for x in probe.ad_values) > .001
    assert all(c.status=='SAME_CHART' for c in probe.checks)


def test_five_point_delays_and_phases():
    p,r=regular()
    for kind,idx in [('delay',0),('phase',0)]:
        probe=five_point_probe(p,r,kind,idx,step=1e-4)
        assert probe.status=='PASS',(kind,probe)
        assert probe.max_absolute_error<1e-5


def test_initial_arrival_history_margin_is_measurable():
    p,r=boundary()
    m=chart_margins(p,r)
    assert np.isclose(m.min_history_arrival_separation,.0002,atol=1e-13)


def test_probe_does_not_differentiate_through_history_partition():
    p,r=boundary()
    probe=five_point_probe(p,r,'delay',1,step=0.00015)
    assert probe.status=='CHART_EXIT'
    assert probe.fd_values is None and probe.ad_values is None
    assert any(c.status!='SAME_CHART' for c in probe.checks)
    assert any(c.status=='SAME_CHART' for c in probe.checks)


def test_smaller_steps_remain_inside_chart():
    p,r=boundary()
    checks=[perturbation_check(p,r,'delay',1,offset) for offset in (-.00005,.00005)]
    assert all(c.status=='SAME_CHART' for c in checks),checks


def test_invalid_delay_and_phase_are_rejected():
    p,r=regular()
    invalid_delay=perturbation_check(p,r,'delay',1,-1.)
    assert invalid_delay.status=='INVALID_PARAMETER'
    invalid_phase=perturbation_check(p,r,'phase',0,-1.)
    assert invalid_phase.status=='INVALID_PARAMETER'


def test_chart_changed_by_horizon_loss():
    p,r=regular()
    # Every spike signature from the original horizon is part of the token.
    # Huge inhibitory weights may abolish downstream spikes, but not assumed;
    # deterministic change in initial phase by a full cycle is invalid.
    test=perturbation_check(p,r,'phase',0,2*np.pi)
    assert test.status=='INVALID_PARAMETER'


def test_collision_detected():
    p=SparseParameters(2,[],[],[],[])
    r=physical_rerecord_sparse(p,horizon=20.,initial_theta=np.array([0.,0.]))
    assert not r.chart_valid
    assert any('COLLISION' in warning for warning in r.warnings)
    assert chart_margins(p,r).min_event_separation==0
    assert five_point_probe(p,r,'phase',0).status=='INVALID_CENTER'


def test_no_spike_handling():
    p=SparseParameters(1,[],[],[],[],h=0.)
    r=physical_rerecord_sparse(p,horizon=30.)
    assert r.chart_valid and len(r.spikes)==0
    assert five_point_probe(p,r,'phase',0).status=='NO_SPIKES'


def test_unsupported_inputs_fail_explicitly():
    p,r=regular()
    with pytest.raises(IndexError):perturbation_check(p,r,'weight',999,.1)
    with pytest.raises(ValueError):five_point_probe(p,r,'delay',1,step=0.)
    with pytest.raises(ValueError):perturbation_check(p,r,'weight',0,float('nan'))
    with pytest.raises(ValueError):five_point_probe(p,r,'external_input',0)


def test_exact_history_arrival_is_invalid_chart():
    p,r=boundary()
    result=perturbation_check(p,r,'delay',1,-.0002)
    assert result.status=='INVALID_CHART',result
    assert 'INITIAL_ARRIVAL_CHART_BOUNDARY' in result.reason


def test_development_probe_preserves_base_chart():
    p,r=regular()
    before=r.token
    _=five_point_probe(p,r,'weight',1,step=1e-4)
    assert r.token==before
    assert p.weight[1]==0.
