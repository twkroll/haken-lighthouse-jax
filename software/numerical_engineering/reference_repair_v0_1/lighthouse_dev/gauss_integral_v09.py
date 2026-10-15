"""LOCAL ENGINEERING: adaptive vectorized Gauss-Legendre integration.

A conservative analytic tail bound prevents missing narrow alpha pulses when
alpha*dt is large. Quadrature agreement is still an *estimated* error, not a
rigorous quadrature certificate. Do not silently replace governed numerics.
"""
from functools import lru_cache
from scipy.optimize import brentq
import numpy as np
from .reference import response
from . import sparse

@lru_cache(None)
def nodes_weights(n):
    x,w=np.polynomial.legendre.leggauss(n)
    return 0.5*(x+1),0.5*w


def _tail_integral_bound(t, alpha, wa, wq, r):
    """Upper bound on integral_t^infinity |S(psi(s))-S(0)| ds.

    S' <= 2*(3/2)^(3/2)*exp(-3/2) / sqrt(r) uniformly, and
    |psi(s)| <= exp(-alpha*s)*(|wa|+s*|wq|).
    """
    lipschitz = 2*(1.5**1.5)*np.exp(-1.5)/np.sqrt(r)
    return lipschitz*np.exp(-alpha*t)*(abs(wa)/alpha +
                        abs(wq)*(t/alpha+1/alpha**2))


def _effective_window(dt, alpha, wa, wq, r, tol):
    end=min(dt,8./alpha)
    # Increase smoothly until the discarded tail's absolute integral is small.
    for _ in range(300):
        if end >= dt or _tail_integral_bound(end,alpha,wa,wq,r)<tol*0.125:
            return end
        end=min(dt,end+max(2./alpha,0.25*end))
    return dt



def _response_breakpoints(window,alpha,wa,wq,h):
    """Split at extrema and crossing of the smooth response's threshold.

    The unwrapped input exp(-alpha*t)*(wa+t*wq) has at most one
    stationary point. Thus on each monotone piece the threshold may be
    crossed at most once. This prevents underresolved narrow onset layers.
    """
    points=[0.,window]
    if wq!=0.:
        turn=1/alpha-wa/wq
        if 0<turn<window:
            points.append(float(turn))
    monotone=sorted(points)
    def gap(s):return float(np.exp(-alpha*s)*(wa+s*wq)-h)
    for l,r in zip(monotone[:-1],monotone[1:]):
        gl,gr=gap(l),gap(r)
        if gl*gr<0:
            points.append(float(brentq(gap,l,r,xtol=1e-14)))
    return np.asarray(sorted(set(points)),dtype=float)


def _composite_difference(window,alpha,wa,wq,r,h,baseline,n,breakpoints):
    x,w=nodes_weights(n)
    left=breakpoints[:-1,None]
    length=np.diff(breakpoints)[:,None]
    ss=left+length*x[None,:]
    psi=np.exp(-alpha*ss)*(wa+ss*wq)
    g=psi-h
    rates=np.zeros_like(g)
    active=g>0
    with np.errstate(divide='ignore',over='ignore',invalid='ignore'):
        rates[active]=np.exp(-r/np.square(g[active]))
    return float(np.sum(length[:,0]*((rates-baseline)@w)))

def gl_integrated(i, dt, a, q, p, *, tol=2e-12):
    """Compatibility API, routed to repaired pulse-aware physical quadrature.

    The original estimated-order GL rule is retained above for provenance but
    must not be treated as independent first-hit authority. Speed-up claims
    from that old approximate rule remain DEVELOPMENT ONLY / DEFERRED.
    """
    if dt<=0: return 0.
    edges=p.incoming[i]
    wa=float(np.dot(p.weight[edges],a[edges]))
    wq=float(np.dot(p.weight[edges],q[edges]))
    from .physical_first_hit_repair import pulse_aware_integral
    return pulse_aware_integral(dt,wa,wq,p.alpha,p.r,p.h)
