import numpy as np
from numpy.testing import assert_allclose
from lighthouse_dev import Parameters,physical_rerecord
from lighthouse_dev.replay import derivative_record

def test_isolated_jax_phase_derivative():
    p=Parameters(np.zeros((1,1)),np.zeros((1,1)))
    rec=physical_rerecord(p,horizon=25,initial_theta=[0.2])
    d=derivative_record(p,rec)
    assert_allclose(d.spike_times,rec.spike_times(),atol=2e-8)
    assert_allclose(d.d_times_d_initial_theta[:,0],[-np.e],atol=1e-8)

def test_delay_recurrent_jax_weight_derivative_vs_physical_fd():
    w=4.;eps=1.e-4
    p=Parameters(np.array([[w]]),np.array([[0.7]]))
    rec=physical_rerecord(p,horizon=42)
    assert rec.chart_valid
    d=derivative_record(p,rec)
    plus=physical_rerecord(Parameters(np.array([[w+eps]]),p.delays),horizon=42)
    minus=physical_rerecord(Parameters(np.array([[w-eps]]),p.delays),horizon=42)
    assert plus.chart_valid and minus.chart_valid
    assert plus.token==rec.token==minus.token
    fd=(plus.spike_times()-minus.spike_times())/(2*eps)
    assert_allclose(d.d_times_d_weights[:,0,0],fd,atol=1e-5,rtol=1e-4)


def test_delay_gradient_vs_physical_fd():
    w=4.;delay=0.7;eps=1e-4
    p=Parameters(np.array([[w]]),np.array([[delay]]))
    rec=physical_rerecord(p,horizon=42)
    d=derivative_record(p,rec)
    plus=physical_rerecord(Parameters(p.W,np.array([[delay+eps]])),horizon=42)
    minus=physical_rerecord(Parameters(p.W,np.array([[delay-eps]])),horizon=42)
    assert plus.chart_valid and minus.chart_valid
    assert plus.token==minus.token==rec.token
    fd=(plus.spike_times()-minus.spike_times())/(2*eps)
    assert_allclose(d.d_times_d_delays[:,0,0],fd,atol=1e-5,rtol=1e-4)

def test_stale_chart_token_rejected():
    from pytest import raises
    p=Parameters(np.array([[4.]]),np.array([[0.7]]))
    rec=physical_rerecord(p,horizon=42.)
    changed=Parameters(p.W,np.array([[20.]]))
    with raises(ValueError,match='Stale/invalid chart'):
        derivative_record(changed,rec)
