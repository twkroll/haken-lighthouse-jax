import numpy as np
from numpy.testing import assert_allclose
from scipy.integrate import quad
from lighthouse_dev import Parameters,alpha_kernel,propagate_alpha,physical_rerecord,validate_same_chart

def test_alpha():
    for alpha in (0.5,1.,2.3):
        assert_allclose(quad(lambda t:alpha_kernel(alpha,t),0,100/alpha)[0],1.,atol=1e-12)
        for t in (0,0.1,1.,3.):
            a,q=propagate_alpha(np.array([0.]),np.array([alpha**2]),t,alpha)
            assert_allclose(a[0],alpha_kernel(alpha,t),atol=1e-13)
            assert_allclose(q[0],alpha**2*np.exp(-alpha*t),atol=1e-13)

def test_isolated_clock():
    p=Parameters(np.zeros((1,1)),np.zeros((1,1)))
    T=2*np.pi*np.e
    rec=physical_rerecord(p,horizon=2.2*T)
    assert rec.chart_valid
    assert_allclose(rec.spike_times(),[T,2*T],atol=1e-10)
    assert_allclose(rec.final_theta,[np.exp(-1)*2.2*T],atol=1e-10)

def test_sensitivity_and_negative_control():
    p=Parameters(np.zeros((1,1)),np.zeros((1,1)))
    a=physical_rerecord(p,horizon=25,initial_theta=[0.1]).spike_times()[0]
    b=physical_rerecord(p,horizon=25,initial_theta=[0.1001]).spike_times()[0]
    assert_allclose((b-a)/1e-4,-np.e,atol=2e-9)
    no=physical_rerecord(Parameters(np.zeros((1,1)),np.zeros((1,1)),h=0),horizon=100.)
    assert no.chart_valid and len(no.spikes)==0

def test_delay_and_chart():
    p=Parameters(np.array([[4.]]),np.array([[0.7]]))
    rec=physical_rerecord(p,horizon=55)
    assert rec.chart_valid,rec.warnings
    assert len(rec.spikes)>=2
    arrivals=[e for e in rec.events if e.kind=='arrival']
    assert_allclose(arrivals[0].t,rec.spikes[0].t+0.7,atol=1e-11)
    assert rec.spikes[1].t-rec.spikes[0].t<2*np.pi*np.e
    ok,again=validate_same_chart(p,rec)
    assert ok and again.token==rec.token

def test_collision_invalid():
    p=Parameters(np.zeros((2,2)),np.zeros((2,2)))
    rec=physical_rerecord(p,horizon=20)
    assert len(rec.spikes)==2 and not rec.chart_valid
    assert any('COLLISION' in s for s in rec.warnings)

def test_invalid_delays_rejected():
    import pytest
    with pytest.raises(ValueError, match='negative delay'):
        Parameters(np.array([[1.]]),np.array([[-0.1]]))
