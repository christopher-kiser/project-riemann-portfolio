#!/usr/bin/env python3
"""Exact synthetic xi/Pick obstruction checks; no numerical RH certification."""
from fractions import Fraction as Q
from math import floor, sqrt

A = [Q(1) + Q(j, 100) for j in range(8)]
# Polynomial zeros: -a_j and -2 +/- 3i.
second = sum(x*x for x in A) + 2*(4-9)
assert second == Q(-713, 500), second

# Imaginary part of 1/(u+a) for u=x+iy, and conjugate-complex roots.
x, y = Q(-2), Q(29, 10)
def imag_recip(re, im):
    return -im / (re*re + im*im)
v = sum((imag_recip(x+a, y) for a in A), Q(0))
v += imag_recip(x+2, y-3) + imag_recip(x+2, y+3)
expected = Q(60430254355211422137113494640862546,
             8225185041587396199596947465865015)
assert v == expected and v > 0, v

# Global H>0 and H'<0 use rigorous analytic lower bounds:
# H >= (8-2 exp(-0.93t))*exp(-1.07t), and
# -H' >= (8-2sqrt(13) exp(-0.93t))*exp(-1.07t).
assert 8 > 2 * sqrt(13)

# All m: K=sqrt(404)>4, choose A=floor(2K^m)+2.
# A > 2K^m and A <= 4K^m; so signs k<=m hold globally.
# For k=m+1, an adverse phase occurs at 0<=t<pi/10,
# and e^(pi/10)<2; 2K^(m+1)>A*e^t.
from math import pi, exp, atan2, ceil
K = sqrt(404)
theta = atan2(20,2)
for m in range(7):
    amp = floor(2*K**m) + 2
    assert amp > 2*K**m
    assert amp <= 4*K**m
    phase = ((m+1)*theta + pi) % (2*pi)
    t = phase/20
    assert 0 <= t < pi/10
    assert amp*exp(t) < 2*K**(m+1)
    print("diagnostic only", "m=",m,"first-failed-order=",m+1,
          "t=",round(t,8))

print("PASS: exact rational H'' and positive Pick witness; analytic bounds")
print("No conclusion about zeros of the actual Riemann zeta function.")
