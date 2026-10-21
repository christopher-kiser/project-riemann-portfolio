> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `38e8310cec9e7e3e2074b406c15edae3846fbbf5f2287feed497cb0bcb5e2cc3`.

# Project Riemann — Dimensional Möbius tomography and the precision barrier

**Date:** 2026-10-20  
**Classification:** `EXACT_CLASSICAL_DIMENSIONAL_RECOVERY / UNIVERSAL_POSITIVITY_CONTROL / NO_NEW_RH_FRONTIER_ADVANCE`  
**Scientific scope:** This is a bounded, falsification-first examination of whether changing the number of spatial lattice dimensions reveals an independent arithmetic law about primes or Riemann zeros. It is a consequence of classical Möbius inversion and separation of distinct exponential growth rates. Literature novelty is **not** established. No candidate proof of RH is asserted.

## 1. The object and its normalization

For each integer dimension `d >= 1`, and `t>0`, let

`theta(x) = sum_{m in Z} exp(-pi*x*m^2)` and `a_k = theta(k^2*t)`.

`1 < a_{k+1} < a_k`, with `a_k -> 1` rapidly as `k -> infinity`.

Let the **primitive Gaussian heat trace** be

`P_d(t) = sum_{v in Z^d \ {0}, gcd(|v_1|,...,|v_d|)=1} exp(-pi*t*||v||^2)`.

The additive origin `(0,...,0)` is removed. The multiplicative identity `1` appears through the gcd requirement.

**Exact classical identity:**

`P_d(t) = sum_{k>=1} mu(k) [a_k^d-1]`.

Proof: uniquely write every nonzero integer vector `v = k*w`, where `k=gcd(v)` and `w` is primitive. Equivalently, for every nonzero `v`, apply the divisor identity `sum_{k|gcd(v)} mu(k) = 1` if `gcd(v)=1` and `0` otherwise. Interchanging sums is justified absolutely because `sum_k (a_k^d-1) < infinity` for each fixed `d,t` (Gaussian decay in `k^2`).

## 2. Exact all-dimensional recovery theorem

**Theorem (conditional on no unproved premise).** Fix any `t>0` and any integer `r>=1`. Then

`mu(r) = lim_{d->infinity} [P_d(t)-sum_{1<=k<r} mu(k)(a_k^d-1)]/(a_r^d-1)`.

The theorem also holds if `mu(k)` is replaced throughout by **any** bounded complex coefficient sequence `c(k)`; in that case the limit equals `c(r)`.

**Quantitative inequality (for |c(k)|<=1):**

`| [F_d(t)-sum_{k<r}c(k)(a_k^d-1)]/(a_r^d-1)-c(r) |`

`<= [d/(a_r-1)] * (a_{r+1}/a_r)^(d-1) * sum_{k>r}(a_k-1)`,

where `F_d(t)=sum_{k>=1}c(k)(a_k^d-1)`.

**Proof.** Remove the first `r-1` terms and divide by the `r`-th term. Every remaining term satisfies, for `k>r`,

`0 < a_k^d-1 = (a_k-1)*sum_{j=0}^{d-1}a_k^j <= d(a_k-1)*a_{r+1}^{d-1}`,

whereas `a_r^d-1 >= (a_r-1)*a_r^{d-1}`. Sum absolute values, using `|c(k)|<=1`. The right-hand side tends to zero exponentially in `d` (up to the factor `d`), since `a_{r+1}/a_r<1`.

The theorem recovers individually the exact values `mu(2)=-1`, `mu(4)=0`, `mu(6)=+1`, and every higher coefficient from a hierarchy of Gaussian lattice counts. Its construction requires all previous coefficients `mu(1),...,mu(r-1)` in the subtraction. It does not magically provide their signed correlations.

## 3. Independent finite numerical check

High-precision mpmath calculations, 185 decimal digits, `t=1/40`, with `k<=50`, returned:

| dimension d | recovered mu(4), true 0 | recovered mu(6), true +1 |
|---:|---:|---:|
| 20 | -0.0139011024 | +0.8455922816 |
| 40 | -0.0002161814 | +0.9505942200 |
| 80 | -0.0000000471 | +0.9964722337 |
| 120 | approximately -1.02e-11 | +0.9997798161 |

The 80-dimensional entries were independently reproduced in Wolfram (`mu(4)=0`, recovered `-4.711887325...e-8`; `mu(6)=1`, recovered `0.996472233687...`). See `verify_tomography.py` and `verify.log` for all `r=2..7` and the generic-sequence control.

**Finite truncation bound.** For `k>=51`, `theta(k^2*t)-1 <= 3*exp(-pi*t*k^2)` at `t=1/40`. Hence

`sum_{k>50}(a_k-1) <= 3 exp(-pi*t*50^2)/(2*pi*t*50)`.

For all tested dimensions `d<=120`, the total error caused by truncating the unnormalized P sum to k<=50 is below `2.45e-84`. The finite checks use high-precision floating point, **not formally verified interval arithmetic**. The theorem itself rests on elementary exact inequalities, not on the numeric check.

## 4. Why increasingly large dimensions make the inner pattern hard to observe

The raw primitive trace has leading growth `P_d(t) ~ a_1^d`. The signal of the r-th coefficient, after all previous layers are removed, scales as `a_r^d`. Thus an absolute measurement with fixed **relative** error in `P_d` can have its uncertainty magnified by roughly `(a_1/a_r)^d` in the extracted coefficient.

At `t=1/40`, dimension `d=120`, resolving the `r=6` layer directly from the raw value would require roughly **90 decimal digits** of relative accuracy. The dimensional effect is an *ill-conditioned microscope*: the information is present, but separating deeper layers demands exponentially increasing precision.

This quantitatively models the user's observation that higher-order patterns may be invisible until a change of scale/viewpoint—and an enormous precision budget—reveals them.

## 5. Strong adversarial countermodel

The recovery theorem is **not special to primes**: choose `c(k)=+1` for all k and define

`F_d(t)=sum_{k>=1}[theta(k^2*t)^d-1]`.

This is itself a legitimate **positive geometric counting function**:

`F_d(t)=sum_{v in Z^d \ {0}} tau(gcd(v)) exp(-pi*t*||v||^2) > 0`,

where `tau(n)` is the number of positive divisors of n. Indeed, each pair `(k,w)` with `v=k*w` contributes once for each positive divisor k of gcd(v).

It has exactly the same dimensional recovery theorem, with recovered coefficients `c(k)=+1`. Nevertheless its summatory coefficients are `sum_{k<=x}c(k)=floor(x)`, exhibiting **no square-root cancellation whatsoever**.

Therefore these properties, even **jointly**,
- positive lattice counts in every dimension,
- multiplicative/divisor structure,
- Fourier/Gaussian geometry,
- and exact all-dimensional coefficient recovery,

do **not** imply the signed cancellation needed for RH.

A new result must use additional arithmetic facts distinguishing the actual Möbius coefficients from other multiplicative/divisor-weighted counting systems.

## 6. Explicit RH barrier

For `Re(s)>1`, `sum_{n>=1} mu(n)n^{-s}=1/zeta(s)`. The classical square-root-type summatory estimate `M(x)=sum_{n<=x}mu(n)=O_eps(x^(1/2+eps))` for every positive eps is equivalent to RH (under the standard convention that all eps are admitted).

The dimensional recovery theorem is **pointwise in r**. It supplies no estimate that is uniform as the number of recovered coefficients `r` grows. One cannot exchange the limits `d->infinity` and `r->infinity` without an independent uniform inequality. The positive divisor-weighted countermodel demonstrates exactly why.

Thus the candidate route encounters the already recognized *signed-arithmetic-correlation* gap, rather than overcoming it.

## 7. One tempting geometric continuation explicitly closed

We also checked a fixed-area rectangular Epstein family `Q_y(m,n)=y*m^2+n^2/y`. Its classical Chowla–Selberg expansion shows that for **each fixed hypothetical nontrivial zero** `rho`, the completed Epstein numerator at `s=rho/2` is nonzero for all sufficiently large `y`, because its cusp leading coefficient involves `Gamma((rho-1)/2)*zeta(rho-1)`, both nonzero. Thus such a zero would be visible as a pole in the primitive Epstein quotient for suitably elongated shapes.

This is the **same Eisenstein-scattering resonance mechanism** already studied in the Project Riemann modular-scattering branch, not a new zero-exclusion argument. Source: John Roderick Smart (1971), *On the values of the Epstein zeta function*, formula (2.1), https://doi.org/10.1017/S001708950000166X; and Selberg–Chowla's original Epstein analysis. The geometry permits such meromorphic poles, so exposure of a hypothetical zero is not a contradiction. **CLOSED_DUPLICATION**; do not reopen that campaign.

## 8. Exact verdict and operational constraints

- **Established from classical inputs:** Primitive-theta Möbius identity; exponential all-dimensional coefficient recovery with explicit error; complete positive divisor-weighted countermodel.
- **Independent numerical checks:** High-precision calculations and Wolfram agreement for d=80, r=4,6; finite truncation controlled as stated.
- **Not established:** Any new signed bound for `sum mu(n)`, any exclusion of a single hypothetical off-real Xi zero, literature priority for the recovery presentation, or RH.
- **Lean:** No Lean compiler in this container; not claimed formally compiled.
- **Codex:** Not launched. Historical Project Riemann archive, certificates and Git provenance not modified.

**Verdict: `CLASSICAL_DIMENSIONAL_TOMOGRAPHY / NO_NEW_RH_FRONTIER_ADVANCE`.** Stop expanding the hierarchy until one can state an independently checkable, all-scale *signed* inequality that fails the divisor-weighted control and actually yields a forbidden off-critical zero. Do not accept another RH-equivalent reformulation as the missing proof.

### References (classical tools, not proof of novelty)

- NIST DLMF, §27.5, *Inversion Formulas*: https://dlmf.nist.gov/27.5
- Chowla–Selberg, *On Epstein's Zeta Function (I)*, PNAS 1949: https://pmc.ncbi.nlm.nih.gov/articles/PMC1063041/
- John Roderick Smart, *On the values of the Epstein zeta function*, 1971: https://doi.org/10.1017/S001708950000166X
- Werner G. Nowak, *Primitive lattice points inside an ellipse* (2003/2005): https://arxiv.org/abs/math/0307279
