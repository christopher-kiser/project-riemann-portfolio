> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `ed3db3c64bd85cc1924ada559fdc51e894c4683e3ee0dc1d91c19d5492839448`.

# Project Riemann — Arithmetic coherence, cutoff flux, and rare revivals

**Date:** 2026-10-19, US Eastern.  
**Classification:** `EXACT_CLASSICAL_INTERMITTENCY_THEOREM / NO_NEW_RH_FRONTIER_ADVANCE`.  
**Novelty:** This combination of standard classical facts was derived for this investigation; no claim of first discovery or new published number-theoretic theorem. The proof is a written classical proof, **not Lean-certified**.  
**Evidence:** Independent exact symbolic checks up to 120; coefficient-by-coefficient integer checks up to 1000; finite floating-point diagnostics only. The originals and historical project records are unchanged.

## 1. Physical question

Double-slit interference and rare coherent revivals suggest asking what goes wrong when one replaces a *signed, pointwise* cancellation statement by a *long-time averaged* energy statement. We test this on **actual Möbius and von Mangoldt coefficients**, not synthetic random coefficients or arbitrary alternative zeta functions.

The relevant physical analogy is **dephasing/intermittency**; no physical observer changes primes. Temporal averages discard relative phases, but arithmetic phase synchronization may still occur at rare times. The exercise cannot assume that a positive intensity is a zero-free criterion.

## 2. Definitions (finite actual arithmetic)

For `K >= 2` and `1/2 < sigma < 1` define

\[
M_K(s)=\sum_{n\le K}\frac{\mu(n)}{n^s},\qquad
Q_K(s)=\sum_{n\le K}\frac{\Lambda(n)}{n^s},\qquad
D_K(s)=\sum_{n\le K}\frac{\mu(n)\log n}{n^s},\quad s=\sigma+it.
\]

All expressions are entire Dirichlet polynomials. Note the sign: on `Re(s)>1`, `(1/zeta)'(s)=(1/zeta(s))`-zeta'/zeta` (historical artifact)` and consequently the **untruncated** arithmetic identity is

\[
\boxed{\mu*\Lambda=-\mu\log.}\tag{1}
\]

Set the *boundary-flux residual*

\[
\boxed{H_K(s)=M_K(s)Q_K(s)+D_K(s).}\tag{2}
\]

This is a mathematically specific candidate for a signed-cancellation observable. It is **not** the original sixfold-ray-character marked polynomial, and no analytic estimate about that family is inferred from it.

## 3. Theorem: mean-square vanishing and unbounded rare coherent revivals coexist

**Theorem (unconditional, classical input).** For fixed `1/2 < sigma < 1`, and every `epsilon > 0`,

\[
\boxed{
\lim_{T\to\infty}\frac1{2T}\int_{-T}^T
|H_K(\sigma+it)|^2\,dt
\ll_{\sigma,\epsilon} K^{1-2\sigma+\epsilon}.}
\tag{3}
\]

In particular, the time-averaged mean-square tends to **zero** when `epsilon<2 sigma-1`.

On the other hand, if
\[
C_\sigma=\frac{6}{\pi^2(1-\sigma)^2}>0,
\]
then
\[
\boxed{\limsup_{t\to+\infty}|H_K(\sigma+it)|
\ge (C_\sigma+o(1))K^{2(1-\sigma)},\qquad K\to\infty.}
\tag{4}
\]

Consequently there are *arbitrarily late times* displaying coherent excursions that **diverge** with `K`, even though their long-time mean-square **vanishes** with `K`.

Moreover, for any fixed `c>0`, the upper asymptotic time-density of the set
`{t: |H_K(sigma+it)| >= c K^(2(1-sigma))}` obeys
\[
\boxed{\overline{\mathrm{dens}}\ll_{\sigma,c,\epsilon} K^{2\sigma-3+\epsilon}.}\tag{5}
\]
This is a rigorous version of *rare giant bursts amid a vanishing average*; it is not probabilistic evidence about individual zeta zeros.

### Proof of (3): perfect cancellation in the bulk

By (1), the coefficient of `n^(-s)` in `M_K Q_K` is exactly `-mu(n)log n` for **every n<=K**. Therefore all coefficients of `H_K` below and including `K` vanish identically.

For `K<n<=K^2`, the coefficient is
\[
c_K(n)=\sum_{ab=n,\ a\le K,\ b\le K}\mu(a)\Lambda(b).
\]
It satisfies `|c_K(n)| <= d(n)log n` because `|mu(a)|<=1` and `Lambda(b)<=log n`. There are no coefficients above `K^2`. Orthogonality of distinct frequencies `log n` in infinite-time averaging gives exactly
\[
\lim_{T\to\infty}\frac1{2T}\int_{-T}^T |H_K(\sigma+it)|^2dt
=\sum_{K<n\le K^2}|c_K(n)|^2 n^{-2\sigma}
\le \sum_{n>K}d(n)^2(\log n)^2n^{-2\sigma}.
\]
The standard bound `d(n) <<_delta n^delta` proves the estimate for any `epsilon>0` (choosing sufficiently small intermediate delta and absorbing log factors), establishing (3).

### Proof of (4): a coherent anti-phase alignment of every prime

Assign to every prime `p<=K` the phase `e^(-it log p)=-1`. This is a *target point of the finite prime-phase torus*, not necessarily an exactly attained finite real `t`. Unique factorization makes the logarithms of distinct primes rationally independent, so Kronecker's theorem supplies **arbitrarily large real times** at which all these phases are simultaneously arbitrarily close to this target. For fixed `K`, every value of `M_K`, `Q_K`, `D_K`, and `H_K` consequently comes arbitrarily close to its torus-target value.

For squarefree `n`, `mu(n)=(-1)^omega(n)` and the induced phase is `(-1)^Omega(n)=(-1)^omega(n)`, hence `mu(n)*(-1)^Omega(n)=mu(n)^2`. Thus at the torus target:

\[
M_K^- = \sum_{n\le K}\frac{\mu(n)^2}{n^\sigma}
\sim \frac{6}{\pi^2(1-\sigma)}K^{1-\sigma};
\]

\[
Q_K^-=\sum_{p^j\le K}(\log p)(-1)^j p^{-j\sigma}
= -\sum_{p\le K}(\log p)p^{-\sigma}+O_\sigma(1)
\sim-\frac{K^{1-\sigma}}{1-\sigma};
\]

\[
D_K^- = \sum_{n\le K}\frac{\mu(n)^2\log n}{n^\sigma}
=O_\sigma(K^{1-\sigma}\log K).
\]

The first uses the elementary squarefree density `sum_{n<=x}mu(n)^2=(6/pi^2)x+O(sqrt x)` and partial summation. The second uses PNT `sum_{p<=x}log p ~ x`; its `j>=2` prime-power remainder is absolutely bounded for `sigma>1/2`. Their product dominates `D_K^-` because `K^(1-sigma)/log K -> infinity`. Hence
\[
H_K^- = M_K^-Q_K^-+D_K^-\sim
-\frac{6}{\pi^2(1-\sigma)^2}K^{2(1-\sigma)}.
\]
Kronecker's theorem then proves (4). In the actual continuous-time model, the phases recur arbitrarily late for **each fixed K**, and no single time is asserted to align infinitely many primes.

### Proof of (5): large-value rarity

For each `K`, the averaged energy `E_K` exists and satisfies (3). Chebyshev/Markov's inequality for normalized Lebesgue measure on `[-T,T]` gives the upper asymptotic density at height `c K^(2(1-sigma))` at most `E_K / (c^2 K^(4(1-sigma)))`, which yields exponent `(1-2sigma+epsilon)-4(1-sigma)=2sigma-3+epsilon`.

## 4. Optional finite-window statement

Montgomery–Vaughan's mean-value theorem for Dirichlet polynomials of length at most `K^2` gives, uniformly in center `t0`,
\[
\frac1{2T}\int_{t_0-T}^{t_0+T}|H_K(\sigma+it)|^2\,dt
\ll_{\sigma,\epsilon}
\left(1+\frac{K^2}{T}\right)K^{1-2\sigma+\epsilon}.
\]
This *particular averaging method* becomes effective for `T` comparable to or greater than `K^2`. It provides **no pointwise control at an individual suspect ordinate**. The theorem is not an impossibility result for all conceivable localized wavelet or arithmetic methods.

## 5. Diagnostics and independent checking

`check_interference.py` is a standalone finite checker. It verifies the identity (1) coefficient-by-coefficient using **integer coefficients of log primes** up to `n=1000` (no numeric logs needed for that test). A distinct SymPy exact symbolic expansion verified the convolution up to 120. The finite norm and target values use ordinary floating point **only as diagnostics**, not as a proof of (3) or (4).

Sample results (sigma=0.875):

| K | Long-time mean-square of residual | Torus-target residual `H_K^-` |
|---:|---:|---:|
| 100 | 0.3541278 | -11.024437 |
| 300 | 0.2627594 | -22.152745 |
| 1000 | 0.1663832 | -41.643530 |

The target residual is a value approached arbitrarily closely at arbitrarily large times, **not** a claimed observed zero of the actual zeta function.

## 6. Consequences and strict limitations

1. **Physical insight:** a conservation-like arithmetic cancellation can be *perfect for low frequencies* and asymptotically perfect in *averaged energy*, while coherent exceptions grow without bound. This is analogous to rare phase-locked interference in physical wave systems, not a measurement-induced change in prime numbers.
2. **No RH deduction:** None of (1)–(5) excludes an individual off-critical-line Xi zero, or bounds the genuine analytic continuation of `-zeta'/zeta` on `1/2<Re(s)<1`. The product of truncated Dirichlet sums is not the product of the analytically continued infinite functions there.
3. **No Codex marked-moment shortcut:** The original marked inverse estimate applies to a ray-character family, smooth annular masks, fixed independent prime-slot coefficients and delicate height-uniform restrictions. The present vertical-time ensemble and canonical von Mangoldt slots **are different objects**. Never substitute (3) for the unproved `r+z<m` moment bound; original `BLOCKED_NEW_MOMENT_ESTIMATE` stands.
4. **New mathematical target, only if independently justified:** The right kind of progress would be a **local, phase-sensitive cancellation law** on the exact arithmetic family at an individual candidate height/row, not merely a time-averaged `L²` bound. The theorem shows why generic claims that finite modes 'decohere' are inadequate. No valid stronger law has been proved here.
5. This is a new *investigation result* proved from established classical tools, **not a claim of literature novelty or an RH theorem**. No need to initiate a broad Codex campaign on these identities.

## 7. Classical reference anchors (not premises from RH)

- NIST DLMF §27.5, Möbius and Mangoldt inversion: https://dlmf.nist.gov/27.5 .
- Squarefree counting density, standard elementary sieve: https://mathworld.wolfram.com/Squarefree.html .
- Montgomery–Vaughan mean value theorem (survey notes by S. Gonek, §7): https://people.math.rochester.edu/faculty/gonek/papers/26-Applics%20MVTs.pdf .
- Bohr theory/Dirichlet-series convergence and almost periodicity: https://doi.org/10.1002/mana.201800542 .
- L. Guth & J. Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics 203 (2026): https://doi.org/10.4007/annals.2026.203.2.6 . Their work treats density/large values; it is not claimed to imply a pointwise RH theorem.

## 8. Decision

`EXACT_CLASSICAL_INTERMITTENCY_THEOREM / NO_NEW_RH_FRONTIER_ADVANCE`. The exact arithmetic provides a concrete **bulk-cancellation versus rare-coherence** principle worth retaining as an explanatory and falsification result. However, the needed new pointwise signed-arithmetic exclusion law remains absent. RH OPEN; Haglund k=2/k=3 UNVERIFIED; marked moment BLOCKED_NEW_MOMENT_ESTIMATE; provenance BLOCKED_UNWAIVED. Lean 4 unavailable in this environment; no Lean proof is claimed. No original evidence, service, Git ref, certificate, or manuscript changed.
