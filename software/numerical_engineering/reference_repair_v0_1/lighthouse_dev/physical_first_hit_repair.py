"""NUM-ENG software-only pulse-aware physical first-hit quadrature.

Authority: PRE_REPAIR_CONTRACT_0_1; engineering quality controls are NOT
formal interval arithmetic certificates or scientific error bounds.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad
from .reference import response
from .gauss_integral_v09 import _effective_window, _response_breakpoints, _tail_integral_bound

class PhysicalFirstHitUncertified(RuntimeError):
    """The caller MUST invalidate the record, never accept a partial tape."""

MAX_SEGMENTS = 512
QUAD_ABS = 2e-13
QUAD_REL = 2e-12
TAIL_BOUND = 2e-13


def pulse_aware_integral(dt, wa, wq, alpha, r, h, *, max_segments=MAX_SEGMENTS):
    """Return absolute phase gain on a physical inter-event interval.

    Frozen alpha flow: psi(s)=exp(-alpha*s)*(wa+s*wq). Splits at all
    analytic extrema and threshold crossings and resolves the alpha scale.
    Analytical Lipschitz tail bound controls the omitted difference to S(0).
    """
    if not np.isfinite([dt,wa,wq,alpha,r,h]).all() or dt < 0 or alpha <= 0 or r <= 0:
        raise PhysicalFirstHitUncertified('NONFINITE_OR_INVALID_INPUT')
    if dt == 0:
        return 0.
    baseline=response(0.,r,h)
    if wa == 0 and wq == 0:
        return dt*baseline
    # The full pulse tail, including the baseline, is represented by an
    # analytic integral plus a rigorously bounded *difference* tail.
    window=_effective_window(dt,alpha,wa,wq,r,TAIL_BOUND*8)
    if window < dt and _tail_integral_bound(window,alpha,wa,wq,r)>TAIL_BOUND:
        raise PhysicalFirstHitUncertified('TAIL_BOUND_UNRESOLVED')
    points=_response_breakpoints(window,alpha,wa,wq,h).tolist()
    step=0.5/alpha
    refined=[points[0]]
    for left,right in zip(points[:-1],points[1:]):
        n=max(1,int(math.ceil((right-left)/step)))
        if n>max_segments or (len(refined)-1+n)>max_segments:
            raise PhysicalFirstHitUncertified('SEGMENT_BUDGET_EXCEEDED')
        for k in range(1,n+1):
            refined.append(left+(right-left)*(k/n))
    def integrand(s):
        psi=math.exp(-alpha*s)*(wa+s*wq)
        return response(psi,r,h)-baseline
    value=0.;error=0.
    for lo,hi in zip(refined[:-1],refined[1:]):
        if hi<=lo:
            continue
        out=quad(integrand,lo,hi,epsabs=QUAD_ABS,epsrel=QUAD_REL,limit=200,full_output=1)
        if len(out)!=3:
            raise PhysicalFirstHitUncertified('QUADPACK_CONVERGENCE_FAILED')
        contribution,err,_=out
        if not np.isfinite([contribution,err]).all() or err<0:
            raise PhysicalFirstHitUncertified('QUADRATURE_NONFINITE')
        value+=contribution
        error+=err
    if error>max(2e-11,2e-11*dt):
        raise PhysicalFirstHitUncertified('QUADRATURE_ERROR_BUDGET_EXCEEDED')
    result=dt*baseline+value
    if not np.isfinite(result) or result< -2e-11 or result>dt+2e-11:
        raise PhysicalFirstHitUncertified('PHYSICAL_RATE_BOUND_VIOLATION')
    return float(np.clip(result,0.,dt))
