"""NUM-ENG Gate 0.2 engineering harness: uses precommitted frozen matrix, no RNG.
All results DEVELOPMENT EVIDENCE / LOCAL ENGINEERING METRICS only.
"""
from __future__ import annotations
import json, os, sys, time, platform, hashlib, traceback, statistics
from pathlib import Path
from math import pi
import numpy as np
import scipy, jax, pytest
from lighthouse_dev.sparse import SparseParameters, physical_rerecord_sparse
from lighthouse_dev.reference import physical_rerecord
from lighthouse_dev.fast_first_hit_gauss_v09 import physical_rerecord_gauss
from lighthouse_dev.fast_first_hit_quiet_v010 import physical_rerecord_quiet
from lighthouse_dev.fast_first_hit_bound_v010 import physical_rerecord_phase_bound
from lighthouse_dev.physical_first_hit_repair import pulse_aware_integral,PhysicalFirstHitUncertified
from lighthouse_dev.profiling import count_rerecord_work

OUT=Path('/mnt/data/numeng_gate02');OUT.mkdir(exist_ok=True)

def fixture(k):
    if k in ('F01','F02','F03','F04','F11','F12','F13'):
        alpha={'F01':1000.,'F02':1000.,'F03':30.,'F04':1.,'F11':1000.,'F12':1000.,'F13':1000.}[k]
        delay= .5 if k=='F11' else 1.5
        horizon=12. if k in ('F03','F04') else 2. if k=='F11' else .5 if k=='F12' else 20.
        phase=2*pi-(.5 if k=='F02' else .005)
        history=(-.5,) if k=='F11' else (-1.,)
        p=SparseParameters(1,[0],[0],[4.],[delay],alpha,1.,.1)
        kw=dict(horizon=horizon,initial_theta=[phase],history=[history])
        if k=='F13':kw['max_events']=0
        return p,kw
    if k in ('F05','F06','F07'):
        w,d,alpha,h,init,hist,horizon={'F05':(0.,.71,1.,-1.,5.8,-1.23,8.),'F06':(-2.,.18,1.,-1.,5.8,-1.23,8.),'F07':(6.,.11,30.,.1,2*pi-.05,-.07,6.)}[k]
        return SparseParameters(1,[0],[0],[w],[d],alpha,1.,h),dict(horizon=horizon,initial_theta=[init],history=[(hist,)])
    if k in ('F08','F09','F10'):
        h=.1 if k=='F10' else -1.
        initial={'F08':[6.,6.],'F09':[6.,5.9999999],'F10':[6.,6.1]}[k]
        return SparseParameters(2,[],[],[],[],1.,1.,h),dict(horizon=3.,initial_theta=initial)
    if k in ('F15','F16','F17','F18'):
        n={'F15':5,'F16':12,'F17':24,'F18':48}[k]
        edges=sorted({(i,i) for i in range(n)}|{(i,(i+1)%n) for i in range(n)})
        target=np.array([t for t,s in edges],int);source=np.array([s for t,s in edges],int)
        weight=np.array([2.25+.17*(s%3)-.11*(t%2) if t==s else (-.6 if t%3==0 else .9) for t,s in edges],float)
        delay=np.array([.12+.017*((5*t+3*s)%13) for t,s in edges],float)
        p=SparseParameters(n,target,source,weight,delay,1.,1.,-1.)
        return p,dict(horizon=4. if n==48 else 8.,history=tuple(((-1.1-.021*i),) for i in range(n)),initial_theta=np.array([5.2+.021*(i%7)+.002*i for i in range(n)]))
    raise KeyError(k)

def signatures(rec):return [e.signature() if hasattr(e,'signature') else (e.kind,e.neuron,e.source,e.ordinal) for e in rec.events]
def reduced_signatures(rec):return [(e.kind,e.neuron,e.source,e.ordinal) for e in rec.events]
def compare(a,b):
    if len(a.events)!=len(b.events):time_diff=None
    else:time_diff=max((abs(e.t-f.t) for e,f in zip(a.events,b.events)),default=0.)
    return dict(token_exact=a.token==b.token if getattr(a,'topology_id',None)==getattr(b,'topology_id',None) else reduced_signatures(a)==reduced_signatures(b),signature_exact=reduced_signatures(a)==reduced_signatures(b),time_error=time_diff,final_phase_error=float(np.max(np.abs(a.final_theta-b.final_theta))),validity_match=a.chart_valid==b.chart_valid)

def main():
    rows=[];acc=[];scale=[];start=time.time();klist=[f'F{i:02d}' for i in range(1,14)]+[f'F{i:02d}' for i in range(15,19)]
    for k in klist:
        p,kw=fixture(k)
        t=time.perf_counter(); rec=physical_rerecord_sparse(p,**kw);physical_elapsed=time.perf_counter()-t
        dense=physical_rerecord(p.to_dense(),**kw)
        c=compare(rec,dense)
        row=dict(fixture=k,n=p.n,e=p.e,alpha=p.alpha,h=p.h,weight_range=[float(np.min(p.weight)),float(np.max(p.weight))] if p.e else [],horizon=kw['horizon'],events=len(rec.events),spikes=len(rec.spikes),valid=rec.chart_valid,physical_certification=rec.physical_certification,warnings=list(rec.warnings),physical_seconds=physical_elapsed,dense_sparse=c)
        row['dense_sparse_pass']=c['signature_exact'] and c['validity_match'] and c['time_error'] is not None and c['time_error']<=2e-8 and c['final_phase_error']<=3e-8
        if k in ('F08','F11','F12','F13'):row['required_failclosed']=not rec.chart_valid
        if k=='F01':row['frozen_hit_error']=abs(rec.spikes[0].t-.505000505363421) if len(rec.spikes)==1 else None
        if k in [f'F{i:02d}' for i in list(range(1,8))+[10]+list(range(15,19))]:
            for nm,method in [('gauss',physical_rerecord_gauss),('quiet',physical_rerecord_quiet)]+([('phase_bound',physical_rerecord_phase_bound)] if k in ('F15','F16','F17','F18') else []):
                try:
                    x=method(p,**kw);d=compare(rec,x)
                    acc.append(dict(fixture=k,method=nm,comparison=d,candidate_certification=x.physical_certification,candidate_warnings=list(x.warnings),candidate_events=len(x.events),reference_events=len(rec.events),reference_valid=rec.chart_valid,comparison_pass=d['signature_exact'] and d['validity_match'] and d['time_error'] is not None and d['time_error']<=2e-8 and d['final_phase_error']<=3e-8))
                except Exception as e:acc.append(dict(fixture=k,method=nm,comparison_pass=False,exception=repr(e)))
        if k in ('F15','F16','F17','F18'):
            times=[]; work=None; rer=0
            for _ in range(3):
                t=time.perf_counter();r2,w2=count_rerecord_work(p,**kw);times.append(time.perf_counter()-t);rer+=1;work=w2
                assert compare(r2,rec)['signature_exact']
            scale.append(dict(fixture=k,n=p.n,e=p.e,events=len(rec.events),spikes=len(rec.spikes),rerecord_count=rer,reference_event_token=rec.token,clean_reference=rec.chart_valid,physical_state_bytes=16*p.e,dense_alpha_state_bytes=16*p.n*p.n,memory_ratio=(p.n*p.n/p.e if p.e else None),work=work.__dict__,wall_seconds=times,median_wall_seconds=float(statistics.median(times))))
        rows.append(row)
        print(json.dumps(dict(fixture=k,valid=rec.chart_valid,events=len(rec.events),dspass=row['dense_sparse_pass'],elapsed_sec=round(time.time()-start,2)),sort_keys=True),flush=True)
    try:
        pulse_aware_integral(10.,0.,4e6,1000.,1.,.1,max_segments=1)
        budget='UNEXPECTED_SUCCESS'
    except PhysicalFirstHitUncertified as e:budget=str(e)
    result=dict(kind='NUMENG_0_2_STRESS_DEVELOPMENT_ONLY',source_git='RB-019',rows=rows,accelerations=acc,scaling=scale,short_budget_negative_control=budget,elapsed_seconds=time.time()-start,environment=dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,jax=jax.__version__,jaxlib=jax.lib.__version__,pytest=pytest.__version__,platform=platform.platform(),jax_backend=jax.default_backend(),cpu_count=os.cpu_count(),thread_controls={k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','PYTEST_DISABLE_PLUGIN_AUTOLOAD','JAX_PLATFORMS','JAX_ENABLE_X64')}))
    (OUT/'STRESS_METRICS.json').write_text(json.dumps(result,indent=2,default=float))
    print('SUMMARY',json.dumps(dict(n=len(rows),physical_matches=sum(q['dense_sparse_pass'] for q in rows),accelerators=len(acc),accelerators_pass=sum(q['comparison_pass'] for q in acc),budget=budget,seconds=round(result['elapsed_seconds'],2))),flush=True)

if __name__=='__main__':main()
