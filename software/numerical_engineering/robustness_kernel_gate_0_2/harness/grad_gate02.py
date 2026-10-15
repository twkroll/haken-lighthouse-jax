"""Gate-0.2 predetermined G01/J01 gradient and CPU JAX audit; NO stochastic methods."""
import time,json,os,sys,platform,statistics
from pathlib import Path
import numpy as np
import jax
import jax.numpy as jnp
from lighthouse_dev.sparse import SparseParameters,physical_rerecord_sparse
from lighthouse_dev.reference import Parameters
from lighthouse_dev.sparse_replay import derivative_record_sparse,prepare_replay,replay_sparse_fixed_chart

jax.config.update('jax_enable_x64',True)
output=Path('/mnt/data/numeng_gate02')
w=np.array([[2.2,0.],[0.,2.5]])
d=np.array([[.31,0.],[.83,.43]])
mask=np.array([[1,0],[1,1]],bool)
p=SparseParameters.from_dense(Parameters(w,d,adjacency=mask))
kw=dict(horizon=40.,history=((-3.,-.5),(-2.2,)),initial_theta=[.3,1.1])
rec=physical_rerecord_sparse(p,**kw)
base={'event_count':len(rec.events),'spike_count':len(rec.spikes),'chart_valid':rec.chart_valid,'certification':rec.physical_certification,'topology_id':rec.topology_id,'base_spike_times':rec.spike_times().tolist()}
assert rec.chart_valid and rec.physical_certification=='NUMENG_PULSE_AWARE_REFERENCE_V1'
t0=time.perf_counter();dr=derivative_record_sparse(p,rec);base['high_level_jax_derivative_seconds']=time.perf_counter()-t0
base['max_jax_physical_disagreement']=dr.max_reference_disagreement
index={'weight':int(np.where(p.weight==0.)[0][0]),'delay':int(np.where(p.weight!=0.)[0][-1]),'phase':0}
eps=1e-4
mats={'weight':dr.d_times_d_edge_weights,'delay':dr.d_times_d_edge_delays,'phase':dr.d_times_d_initial_theta}
for name,idx in index.items():
    arr_plus=(p.weight if name=='weight' else p.delay if name=='delay' else np.asarray(kw['initial_theta'])).copy()
    arr_minus=arr_plus.copy()
    arr_plus[idx]+=eps;arr_minus[idx]-=eps
    def physical(arr):
        if name=='weight':params=p.with_weights(arr); theta=kw['initial_theta']
        elif name=='delay':params=p.with_delays(arr);theta=kw['initial_theta']
        else:params=p;theta=arr
        return physical_rerecord_sparse(params,horizon=kw['horizon'],initial_theta=theta,history=kw['history'])
    plus,minus=physical(arr_plus),physical(arr_minus)
    matching=(plus.chart_valid and minus.chart_valid and rec.token==plus.token==minus.token and
             plus.physical_certification==minus.physical_certification=='NUMENG_PULSE_AWARE_REFERENCE_V1')
    if matching:
        fd=(plus.spike_times()-minus.spike_times())/(2*eps)
        error=float(np.max(np.abs(fd-mats[name][:,idx]))) if fd.size else 0.
        base[name]={'index':idx,'chart_exit':False,'absolute_max_err':error,'physical_fd':fd.tolist(),'jax_ad':mats[name][:,idx].tolist(),'pass':error<=3e-5}
    else:
        base[name]={'index':idx,'chart_exit':True,'plus_valid':plus.chart_valid,'minus_valid':minus.chart_valid,'plus_token':plus.token,'minus_token':minus.token,'base_token':rec.token}
    print(name,base[name],flush=True)

prepared=prepare_replay(rec,p)
weights=jnp.asarray(p.weight);delays=jnp.asarray(p.delay);theta=jnp.asarray(rec.initial_theta)
def f(w):return replay_sparse_fixed_chart(w,delays,theta,rec,p,prepared=prepared)
# JVP and VJP consistency + physically rerecorded finite difference from weight check
direction=np.zeros(p.e);direction[index['weight']]=1.
_,jvp=jax.jvp(f,(weights,),(jnp.asarray(direction),))
y,vjp_f=jax.vjp(f,weights)
adjoint=np.linspace(.3,1.1,len(rec.spikes))
vjp_grad=np.asarray(vjp_f(jnp.asarray(adjoint))[0]);vjp_check=float(abs(np.dot(np.asarray(jvp),adjoint)-np.dot(direction,vjp_grad)))
base['jax_jvp_vjp']={'direction':direction.tolist(),'jvp':np.asarray(jvp).tolist(),'adjoint':adjoint.tolist(),'adjoint_dot_error':vjp_check,'jvp_vs_jac_max':float(np.max(np.abs(np.asarray(jvp)-mats['weight']@direction))),'pass':vjp_check<1e-8}
# JIT compile/time split, no inference about holistic speed.
jitted=jax.jit(f)
t0=time.perf_counter();jit_val=jitted(weights);jit_val.block_until_ready();base['jit_forward_first_seconds']=time.perf_counter()-t0
times=[]
for i in range(3):
    t0=time.perf_counter();jitted(weights).block_until_ready();times.append(time.perf_counter()-t0)
base['jit_forward_warm_seconds']=times
jac=jax.jit(jax.jacrev(f))
t0=time.perf_counter();ja=jac(weights);ja.block_until_ready();base['jit_jac_first_seconds']=time.perf_counter()-t0
times=[]
for i in range(3):
    t0=time.perf_counter();jac(weights).block_until_ready();times.append(time.perf_counter()-t0)
base['jit_jac_warm_seconds']=times
base['jit_jac_max_diff_vs_high_level']=float(np.max(np.abs(np.asarray(ja)-mats['weight'])))
base['jit_forward_max_reference_diff']=float(np.max(np.abs(np.asarray(jit_val)-rec.spike_times())))
(output/'GRADIENT_JAX_METRICS.json').write_text(json.dumps(base,indent=2))
print('SUMMARY',json.dumps({k:base[k] for k in ('event_count','spike_count','max_jax_physical_disagreement','jit_forward_first_seconds','jit_jac_first_seconds','jit_forward_max_reference_diff','jit_jac_max_diff_vs_high_level')}),flush=True)
