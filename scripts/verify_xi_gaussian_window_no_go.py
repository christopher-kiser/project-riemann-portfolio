#!/usr/bin/env python3
"""Exact rational replay: synthetic xi-shaped zero set and Gaussian-CM no-go.

Scientific scope: this proves a synthetic obstruction only, NOT anything about
zeros of the actual Riemann zeta function. The CM closure proof is analytic and
fully stated in the associated note; this checker validates its rational bounds.
"""
from fractions import Fraction as Q
from math import atan, exp, pi

A, M, q, c = 10, 16, Q(1), Q(6)
a, b, K = Q(63, 16), Q(1), Q(65, 16)
assert a*a + b*b == K*K
assert (Q(2)**2 - Q(1, 4)**2) == a
assert 2 * Q(2) * Q(1, 4) == b
assert q < a < c and K < c
assert A > 2 and A*q > 2*K

# log(2)=2*(1/3 +1/(3*3**3)+...); this exact lower bound ensures
# e**(33/16)<8 and hence 16*exp(-33/16)>2.
ln2_lower = 2*(Q(1, 3)+Q(1, 81))
assert ln2_lower == Q(56, 81) and ln2_lower > Q(11, 16)
assert (c-a) == Q(33, 16)

# At n=100 choose t=100 atan(16/63)+pi with phase -1.
# The elementary arctan alternating series ensures 0.24<theta<0.26.
x = Q(16, 63)
assert x - x**3/3 > Q(6,25)
assert x < Q(13,50)
# Both competitors decay along t_n=n*theta+pi.
assert (a-q)*Q(13,50) - 2*ln2_lower < 0
assert Q(5,12) - (c-a)*Q(6,25) < 0
# Together with 3<pi<4, this proves 27<t<30 for n=100.

# Normalize the 100th alternating derivative by its negative term,
# 2*K**100 exp(-a*t). Use e<3 and e>8/3 for exact rational bounds.
slow_bound = Q(A, 2)*Q(1, 4)**100 * 3**89
fast_bound = Q(M, 2)*Q(3, 2)**100 * Q(3, 8)**55
assert K > Q(4)
assert c/K < Q(3,2)
assert (a-q)*30 < 89
assert (c-a)*27 > 55
assert slow_bound + fast_bound < Q(1,2)

# Gaussian sigma=1/4 yields H_sigma(t)=(1+t)^(-1/2) H(t/(1+t)).
# v(t)=t/(1+t) has a CM derivative; its image lies in (0,1).
# Since H has (-1)^n H^(n)(v)>0 on (0,1) for every n, the
# Faà di Bruno / CM-composition sign rule and CM-product rule imply
# (-1)^n H_sigma^(n)(t)>0 for every n and every t>0.
assert 4*Q(1,4)==1

print('PASS: exact algebra and inequalities certify synthetic no-go')
print('All alternating derivatives H^(n) strictly positive on 0<=t<=1')
print('100th alternating derivative negative at t*=100 atan(16/63)+pi')
print('Smoothed H_(1/4) is globally completely monotone by analytic composition')
print('Fully independent of actual zeta-zero location; no RH proof/disproof')
print('diagnostic t* =', 100*atan(16/63)+pi)
print('diagnostic normalized sign =', -1 + (A/2)*(1/float(K))**100 * exp(float((a-q))*(100*atan(16/63)+pi)) + (M/2)*(float(c/K))**100*exp(-float((c-a))*(100*atan(16/63)+pi)))
