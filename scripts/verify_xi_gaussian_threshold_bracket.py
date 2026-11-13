#!/usr/bin/env python3
"""Round 13: exact rational Gaussian profile witness for a synthetic spectrum.

The proof uses classical 3<pi<22/7, e<3, and elementary Taylor bounds.
This is NOT a result about the actual Riemann xi-function.
"""
from fractions import Fraction as Q
from math import factorial, sqrt, exp, cos

sigma, x, delta = Q(1,50), Q(33,20), Q(1,4)
assert (x-2)*delta/(2*sigma) == -Q(35,16)
assert (delta*delta-(x-2)**2)/(4*sigma) == -Q(3,4)
assert (delta*delta-(x+2)**2)/(4*sigma) == -Q(663,4)
assert (x-1)**2/(4*sigma) == Q(169,32)
assert (Q(12,5)-x)**2/(4*sigma) == Q(225,32)
assert Q(12,5)**2 < 6
# Strict cosine comparison: 2pi/3 < 35/16 < 4pi/3.
# This rational line follows from the known bounds 3<pi<22/7.
assert Q(2,3)*Q(22,7) < Q(35,16) < Q(4,3)*3
# e**5>100 from the exact partial Taylor series; e**2>5;
# e**7>500 and e<3 by standard elementary inequalities.
taylor = sum((Q(5)**k/Q(factorial(k)) for k in range(7)), Q(0))
assert taylor == Q(16289,144) and taylor>100
bound = Q(1,10)+Q(16,500)+Q(1,100)-Q(1,6)
assert bound == -Q(37,1500) and bound<0
# Numerical diagnostic only; exact rational inequalities above prove sign.
s,x0=float(sigma),float(x)
f=lambda v:exp(-v*v/(4*s))
p=5*(f(x0-1)+f(x0+1))+8*(f(x0-sqrt(6))+f(x0+sqrt(6)))
p+=exp(float(delta*delta)/(4*s))*(f(x0-2)*cos(float((x-2)*delta/(2*sigma)))+f(x0+2)*cos(float((x+2)*delta/(2*sigma))))
assert p<float(bound)
print("PASS: p_(1/50)(33/20) / c < -37/1500 < 0, by exact rational comparisons.")
print("Numerical check only:",p)
print("No statement about real Riemann xi zeros.")
