# Round 12 — finite-window and Gaussian positivity no-go for an xi-shaped synthetic spectrum

**Date:** 2026-11-12. **Scientific status:** `NO_NEW_RH_FRONTIER_ADVANCE`. Direction: Christopher Kiser with substantial AI-assisted derivation and checks. This is an exact synthetic obstruction, **not a claim about actual zeta zeros**, a new zero-free region, or first-in-literature originality.

## 1. External advance and scope

Suvrit Sra, *Some positivity properties of Riemann Ξ under smoothing*, preprint v1 (released 2026-11-11), https://suvrit.github.io/papers/riem-xi-smoothing/riem-xi-smoothing-v1.pdf, Proposition 3.1, proves the Gaussian time-change identity
```
H_sigma(t) = (1+4 sigma t)^(-1/2) H(t/(1+4 sigma t)).
```
That preprint proves sufficient positive-smoothing widths from the critical strip, primes, and published zero verification; it also proves that the corresponding smoothed reciprocal laws lose even PF_2/log-concavity. No extension of a verified zero height or RH solution is claimed by that source. We use the exact transformation, with attribution, on a **finite synthetic spectrum**. See also Sra, *On some positivity properties of the Riemann Ξ function* (2026-11-02), https://arxiv.org/abs/2611.02944, and the earlier project note `2026-11-07-geometric-unfolding-positivity.md`.

## 2. The finite-window countermodel

Let
```
a=63/16, b=1, K=sqrt(a^2+b^2)=65/16, c=6,
theta=arctan(16/63).
```
For any finite T>0 choose an **integer** M>2 exp((33/16) T), and set
```
P_M(u) = [(u+1)^10 (u+6)^M ((u+a)^2+1)] / [6^M (a^2+1)]
H_M(t) = 10 exp(-t) + M exp(-6t) + 2 exp(-a t) cos(t).
```
The logarithmic derivative P'_M/P_M is the Laplace transform of H_M. The polynomial has ordinary negative real roots -1 and -6 with positive integer multiplicity, plus a nonreal conjugate pair -a±i. Under the squared coordinate and Ξ(z)=P_M(-z^2), these nonreal roots give **synthetic** zeros at z=±(2±i/4), corresponding to s=1/4 or 3/4 with imaginary part ±2: inside the critical strip and respecting reflection/conjugation symmetry. They are NOT zeta zeros and do not reproduce zeta's known zero-free low-height region.

**(a) Global positivity and first-order decrease.** Since a>1 and 10>2K,
```
H_M(t) >= 10 exp(-t) - 2 exp(-a t) > 0,
-H'_M(t) >= 10 exp(-t) - 2K exp(-a t) > 0  (t>=0).
```

**(b) All derivative orders are positive on the entire finite window.** For every integer n>=0 and every 0<=t<=T,
```
(-1)^n H_M^(n)(t)
 >= 10 exp(-t)+ M 6^n exp(-6t)-2 K^n exp(-a t)
 >= 10 exp(-t) + K^n exp(-a t)[M exp(-(6-a)T)-2] >0.
```
Here 6>K and 6-a=33/16. This is an *analytic all-n, all-t in [0,T]* result, not sampled derivatives.

**(c) Outside the window, one alternating derivative becomes negative.** For positive integers n, put `t_n=n theta+pi`, so `cos(t_n-n theta)=-1`. Dividing the nth alternating derivative by the positive number `2 K^n exp(-a t_n)` gives
```
R_n = -1
    +5 K^(-n) exp((a-1)t_n)
    +(M/2)(6/K)^n exp(-(6-a)t_n).
```
Both positive terms tend exponentially to zero. Indeed `6/25<theta<13/50` follows from `x-x^3/3<arctan(x)<x` for `x=16/63`; `log K>log 4>112/81` follows from the first two terms of the positive arctanh series for log 2; `log(6/K)<log(3/2)<5/12` follows from the alternating log series. Therefore
```
(a-1) theta - log K < (47/16)(13/50)-112/81 <0,
log(6/K)-(6-a) theta < 5/12-(33/16)(6/25)<0.
```
Hence `R_n -> -1`, and for all sufficiently large n, `t_n>T` and `(-1)^n H_M^(n)(t_n)<0`. So H_M is **not** completely monotone globally.

**(d) Nevertheless, the Gaussian-smoothed heat sum is globally CM.** Choose any `sigma>=1/(4T)`. Then `v(t)=t/(1+4 sigma t)` maps (0,infinity) into (0,T), and `v'(t)=(1+4 sigma t)^(-2)` is CM; v is a Bernstein function. The derivative-sign form of the composition rule (Faà di Bruno) transfers the all-order alternating signs of H_M on the image of v to H_M(v(t)). The factor `(1+4 sigma t)^(-1/2)` is also CM; products of CM functions are CM. Therefore
```
(-1)^n H_{M,sigma}^(n)(t) >= 0
for EVERY integer n>=0 and EVERY t>0.
```
The spectrum still has the nonreal pair. This shows why a globally CM **smoothed** heat sum, even for a strip-shaped symmetric polynomial with positive multiplicities, cannot by itself prove real-rootedness of the **unsmoothed** polynomial. It does not invalidate the actual xi-specific theorems in the cited preprint.

## 3. Concrete, reproducible instance and independent checks

Take `T=1, M=16, sigma=1/4`. The inequality `16 exp(-33/16)>2` is exact: `log 2=2 arctanh(1/3)>56/81>11/16`, implying `exp(33/16)<8`. All alternating derivatives of `H_16` are positive on [0,1], while `H_{16,1/4}(t)=H_16(t/(1+t))/sqrt(1+t)` is globally completely monotone. Yet for `n=100`, `t_*=100 arctan(16/63)+pi`, Wolfram gives
```
t_* ≈ 28.0125915629420802,
R_100 ≈ -0.9999999441410682.
```
This sign has an independent **exact rational envelope**. Elementary bounds give `27<t_*<30` and `8/3<e<3`; thus
```
R_100 < -1 + 5*3^89/4^100 + 8*(3/2)^100*(3/8)^55 < -1/2.
```
The two rational positive terms are ~9.05e-18 and ~1.21e-5, respectively; this is a rigorous (loose) witness, not a floating-point sign test. A standard-library Python verifier, `scripts/verify_xi_gaussian_window_no_go.py`, checks the exact rational comparisons and prints clearly separated numerical diagnostics. Wolfram independently checked the spectral squares, the all-order window margin, the n=100 phase, and the normalized derivative.

## 4. Scientific decision and outstanding obligations

**Accepted:** The finite-window all-order and globally smoothed CM countermodel is established by elementary analytic inequalities, a CM-composition argument, exact rational controls, and a separate Wolfram check. It strengthens the November 7 synthetic caution from *finitely many derivative orders* to *all derivative orders on any prescribed finite time window*, and explicitly respects critical-strip symmetry.

**Not established:** Any zero of actual zeta off the critical line, extension of any verified zero-free range, an actual xi-specific unsmoothed complete-monotonicity estimate, or independent peer review. The Nov 11 paper is a recent preprint and its author owns its results; our construction is an internal project-specific countermodel with unassessed literature novelty.

**Next frontier:** Any attempt to invert smoothing to prove RH must use structure beyond (a) finite time-window all-order positivity, (b) smoothed global complete monotonicity, and (c) symmetry/critical-strip geometry. Candidate inputs requiring separate research are prime-explicit-formula cancellations or truly global theta-specific estimates. Do not reopen coefficient-only finite-node scans already closed in Rounds 10–11 without genuinely new data.

The marked-inverse `r+2z<1 -> r+z<1` estimate remains `BLOCKED_NEW_MOMENT_ESTIMATE`; full Haglund k=2/k=3 remains `UNVERIFIED`; historical provenance is unchanged. **No new RH frontier advance.**

## 5. Verification accounting

- Independent exact script: `scripts/verify_xi_gaussian_window_no_go.py`, Python standard library, passed locally on 2026-11-12.
- Connected Wolfram evaluation: exact `(2±i/4)^2=63/16±i`, `K=65/16`, window margin `16 exp(-33/16)-2>0`, and n=100 diagnostic; passed.
- The global CM conclusion relies on a written Bernstein composition and product argument, not a numerical derivative grid.
- Not run: Lean, Arb validation of **actual xi**, hosted CI, referee review, new zero computations, or any proof of RH.
