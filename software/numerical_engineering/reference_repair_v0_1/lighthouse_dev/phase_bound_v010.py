"""Conservative local phase-rate bound for the frozen RB-004 baseline.

LOCAL ENGINEERING ONLY. Between physical events, each incoming alpha state evolves as
psi_i(s) = exp(-alpha*s) * (A_i + s*Q_i), for 0<=s<=dt,
where A_i=sum_e w_e*a_e and Q_i=sum_e w_e*q_e.
Taking the maximum at the interval endpoints and (if interior) the unique
critical point gives the exact real maximum of psi. Since S is monotone,
max theta_dot <= S(max psi) <= 1. Slight floating safety margins are applied.
"""
from __future__ import annotations
import numpy as np
from .reference import response
from .sparse import SparseParameters


def psi_upper_interval(i:int,dt:float,a:np.ndarray,q:np.ndarray,p:SparseParameters)->float:
    if not np.isfinite(dt) or dt<0:
        raise ValueError('interval length must be finite and nonnegative')
    es=p.incoming[i]
    if len(es)==0:
        return 0.0
    A=float(np.dot(p.weight[es],a[es]))
    Q=float(np.dot(p.weight[es],q[es]))
    values=[A, float(np.exp(-p.alpha*dt)*(A+dt*Q))]
    if Q!=0.0:
        critical=(Q-p.alpha*A)/(p.alpha*Q)
        if 0.0<critical<dt:
            values.append(float(np.exp(-p.alpha*critical)*(A+critical*Q)))
    # Overshoot upwards to avoid spuriously rejecting true first hits due to rounding.
    return float(np.nextafter(max(values),np.inf))


def phase_rate_upper(i:int,dt:float,a:np.ndarray,q:np.ndarray,p:SparseParameters)->float:
    psimax=psi_upper_interval(i,dt,a,q,p)
    # The response saturates at 1; margin makes pruning conservative in floating arithmetic.
    return min(1.0,float(response(psimax,p.r,p.h))+2e-14)
