"""Independent Fraction-only reconstruction and fixed-grid Bernstein replay.
No SymPy, no imports or calls to the supplied certificate generator.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,time
W=Path(__file__).resolve().parents[1]
if not __debug__:
 raise RuntimeError('Run without -O: exact certificate assertions must be enabled.')
(W/'build').mkdir(exist_ok=True)
class P:
 def __init__(self,a=0):self.c={k:F(v) for k,v in a.items() if v} if isinstance(a,dict) else ({(0,0):F(a)} if a else {})
 def __add__(self,b):
  b=b if isinstance(b,P) else P(b);c=self.c.copy()
  for k,v in b.c.items():c[k]=c.get(k,F(0))+v
  return P(c)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.c.items()})
 def __sub__(self,b):return self+-b if isinstance(b,P) else self+P(-b)
 def __rsub__(self,b):return P(b)+-self
 def __mul__(self,b):
  b=b if isinstance(b,P) else P(b);c={}
  for (i,j),v in self.c.items():
   for (k,l),u in b.c.items():c[i+k,j+l]=c.get((i+k,j+l),F(0))+v*u
  return P(c)
 __rmul__=__mul__
 def __truediv__(self,b):return self*F(1,b)
 def at(self,d,x):return sum((v*d**i*x**j for (i,j),v in self.c.items()),F(0))
 def bernstein(self,a,b,c,d):
  n=max((i for i,j in self.c),default=0);m=max((j for i,j in self.c),default=0)
  # Coefficient of Bernstein_i^n after restricting the monomial d^k.
  def monomial(k,i,n,left,right):
   return sum((F(comb(k,h)*comb(i,h),comb(n,h))*left**(k-h)*(right-left)**h for h in range(min(k,i)+1)),F(0))
  dx={(k,i):monomial(k,i,n,a,b) for k in range(n+1) for i in range(n+1)}
  xx={(k,i):monomial(k,i,m,c,d) for k in range(m+1) for i in range(m+1)}
  return [sum((v*dx[k,i]*xx[l,j] for (k,l),v in self.c.items()),F(0)) for i in range(n+1) for j in range(m+1)]
d=P({(1,0):1});x=P({(0,1):1})
b=F(1,100);ell=F(21,125);kap=F(29991,40000);c=1/(3*kap);h=F(757,1000);ly=F(421,1000);nu=F(1,1000)
D=3-(1+2*c)*x; PP=(2-2*c*x)*(1-x);J=(F(5,6)-d)*D+d*PP
base=-F(1,4)+b/6+5*ell/4+d/2+d*x*(ell+c*(h/4-ly/2))
# All reconstructed critical expressions have the common positive denominator K.
K=2*J*D;tn=F(24,25)*2*J+d*PP
rn=(2-2*c*x)*tn+2*J*(c-1)*x-F(3,100)*K
mn=tn*D-rn;zi=(F(3,8)-nu)*K-rn/4;zp=(1/(6*kap)-nu)*K-mn/(3*kap)
ri=K-d*rn-2*d*x*zi;rp=K-2*d*mn-2*d*x*zp;rl=(1-d)*K+(F(5,6)-d)*(tn*D-K)
critical=(F(5,12),F(13,20),F(7,16),F(1,2))
checks={f'critical_{name}':((base+nu-F(3,4)*h)*K+F(3,4)*h*r,critical) for name,r in [('inverse',ri),('plain',rp),('long',rl)]}
oldnum=(base+nu-F(3,4)*h*d)*2*J+F(3,4)*h*(F(5,6)-d)*d*PP
for name,box in [('lower_d',(F(1,8),F(5,12),F(0),F(1,2))),('upper_d',(F(13,20),F(5,6),F(0),F(1,2))),('lower_x',(F(5,12),F(13,20),F(0),F(7,16)))]:checks['published_'+name]=(oldnum,box)
feas={'t_ge_1':K-tn*D,'t_le_3/2':tn*D-F(3,2)*K,'r_ge_t_minus_half':tn*D-K/2-rn,'r_le_1':rn-K,'m_positive':-mn,'m_below_half':mn-K/2,'zI_positive':-zi,'zI_below_supply':zi-ell/(h+F(1,1000000))*K,'zI_below_one_minus_r':zi+rn-K,'zP_positive':-zp,'zP_below_supply':zp-ell/(h+F(1,1000000))*K,'inverse_2r8z_strict':2*rn+8*zi-3*K+K/200,'plain_2m6kz_strict':2*mn+6*kap*zp-K+K/500}
checks.update({'feasible_'+name:(p,critical) for name,p in feas.items()})
# Explicit independent denominator bounds over the full domain, including d=5/6.
Dmin=3-(1+2*c)/2;Pmin=1-c/2
assert 0<c<1 and Dmin>0 and Pmin>0
# J=(5/6-d)D+dP >= d P >= Pmin/8; K>=2 Dmin Pmin/8.
records=[];start=time.monotonic()
for name,(p,(a,b0,c0,d0)) in checks.items():
 maxcoef=None
 for i in range(8):
  for j in range(8):
   coef=p.bernstein(a+(b0-a)*i/8,a+(b0-a)*(i+1)/8,c0+(d0-c0)*j/8,c0+(d0-c0)*(j+1)/8)
   top=max(coef);maxcoef=top if maxcoef is None else max(maxcoef,top)
   assert top<0,(name,i,j,str(top))
 records.append({'name':name,'boxes':64,'largest_Bernstein_coefficient':str(maxcoef),'strictly_negative':True})
# Every supplied fixed parameter condition is independently evaluated.
ze=F(1,1000000);g=F(1,3000);gs=F(1,4000);lx=(1-F(1,100)-ell)/2;z0=F(17,50);dmin=F(1,100)
Asm=F(1,2)+ell/2*(F(1,2)+2*ell/h)-h/2;C0=-F(1,4)+F(1,100)/6+5*ell/4
conditions=[F(1,6)<=ell<=F(1,5),F(29991,40000)<=kap<=F(3,4),F(11,12)-ell/4>F(87,100),lx>ell,ly-ell>F(11,6)*F(1,100),6*kap*ell>F(3,4),ell/h<1/(6*kap),ell/(h+ze)>F(21,100),h/2<ly<F(1,2),0<gs<F(1,1000),0<2*ze<F(1,1000),g-2*ze>gs,max(C0,C0+Asm/8)<-F(1,250),C0+(F(1,2)+3*ell/2)/50<-F(1,100),h*(z0-F(1,6))-ly/2+2*dmin<-F(1,20),F(8748867,10000000)<=(1+kap)/2]
assert all(conditions)
# Actual gate point, not a new optimized parameter choice.
pt=(F(1,2),F(1,2));den=K.at(*pt);r=rn.at(*pt)/den;z=zi.at(*pt)/den
witness={'delta':'1/2','x':'1/2','r0':str(r),'zI':str(z),'proposed_first_gap':str(1-r-z),'old_first_gap':str(1-r-2*z),'second_gap':str(3-2*r-8*z)}
assert 1-r-z>0 and 3-2*r-8*z>0 and 1-r-2*z<0
# Negative controls: reversing a proved negative polynomial cannot certify;
# the deliberately asserted old margin fails at the exact gate point.
assert max((-checks['critical_plain'][0]).bernstein(*critical))>0
result={'method':'Fraction-only formula reconstruction; independent fixed 8x8 box partitions and direct monomial-to-Bernstein conversion','denominator_lower_bounds':{'D':str(Dmin),'P':str(Pmin),'J':str(Pmin/8),'K':str(Dmin*Pmin/4)},'box_certificates':records,'fixed_conditions':len(conditions),'all_fixed_conditions':all(conditions),'gate_point_obstruction':witness,'negative_controls':{'sign_reversal_rejected':True,'old_margin_claim_rejected':True},'endpoint':str(F(11,12)-ell/4),'seconds':time.monotonic()-start,'scope':'finite rational algebra only; not the analytic moment'}
(W/'build/exact-gate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks':len(records),'boxes':sum(r['boxes'] for r in records),'fixed':len(conditions),'witness':witness,'seconds':result['seconds']}))
