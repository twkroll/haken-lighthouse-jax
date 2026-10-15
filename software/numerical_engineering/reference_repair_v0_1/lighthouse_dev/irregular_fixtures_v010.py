"""Deterministic nonrandom irregular-graph engineering fixtures.

No scientific data, no reserved seeds. Uses reproducible modular arithmetic and
identical fixed-delay semantics. These fixtures are NOT registered benchmarks.
"""
from __future__ import annotations
from math import gcd, pi
import numpy as np
from .sparse import SparseParameters


def irregular_fixture(n:int, degree:int=3, *, inhibitory:bool=True, alpha:float=1.0):
    if n<5 or degree<1 or degree>=n:
        raise ValueError('require n>=5 and 1<=degree<n')
    # Mixing stride coprime to n; different neurons have different in-degrees.
    stride=next((x for x in range(n-2,n//2,-1) if gcd(x,n)==1),1)
    edges=set()
    for source in range(n):
        targets={source, (source+1)%n} # retain a cycle backbone and self-edge
        for j in range(1,degree+1):
            if (source+j)%3!=0 and j<=max(1, degree-(source%3)):
                targets.add((source+stride*j+source%2)%n)
        for target in targets:
            edges.add((target,source))
    ordered=sorted(edges)
    target=np.asarray([t for t,s in ordered],dtype=int)
    source=np.asarray([s for t,s in ordered],dtype=int)
    weight=[];delay=[]
    for k,(t,s) in enumerate(ordered):
        w=1.6 if t==s else (0.45+0.05*((3*t+s)%5))
        if inhibitory and t!=s and (7*t+3*s)%11==0:
            w=-0.6*w
        if (5*t+7*s)%29==0: w=0.0  # explicit structural zero
        weight.append(w)
        delay.append(0.13+0.019*((13*t+7*s)%31)+0.00037*((t+s)%7))
    p=SparseParameters(n,target,source,np.asarray(weight),np.asarray(delay),alpha=alpha,r=1.,h=-1.)
    history=tuple((float(-2.15-0.0071*j-0.000013*j*j),) for j in range(n))
    theta=np.asarray([0.23+5.4*((17*j+3)%n)/(n) + 0.000137*(j%5) for j in range(n)])
    assert np.all(theta < 2*pi)
    return p,history,theta
