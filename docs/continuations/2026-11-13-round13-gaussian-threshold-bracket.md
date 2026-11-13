# Round 13 — an exact Gaussian threshold bracket in a synthetic Xi-shaped spectrum

**Research date:** 2026-11-13. **Status:** EXACT_SYNTHETIC_OBSTRUCTION / NO_NEW_RH_FRONTIER_ADVANCE. Research directed by Christopher Kiser with substantial AI derivation and verification. Neither proof priority nor any claim about actual zeta zeros is asserted.

## 1. Audit of Round 12 and coordinate conventions

The preceding [Round 12 continuation](2026-11-12-round12-gaussian-window-no-go.md) and its Python checker were rerun successfully on November 13. In particular, the all-derivative finite-time interval statement, the n=100 negative witness, and Gaussian complete monotonicity at width 1/4 retain their earlier scope.

A suspected sign error was checked and **not found**. With the conventional Xi notation \(\Xi(z)=\xi(1/2+iz)\) and \(h(u)=\xi(1/2+\sqrt u)\), the identity is \(\Xi(z)=h(-z^2)\). Thus a synthetic polynomial \(P(u)\) yields \(\Xi_{\rm syn}(z)=P(-z^2)\). The complex roots \(-63/16\pm i\) give \(z=\pm(2\pm i/4)\), and the corresponding synthetic \(s=1/2+iz\) have real parts 1/4 or 3/4 and imaginary parts ±2. Wolfram reconfirmed \((2+i/4)^2=63/16+i\) and \(1/2+i(2+i/4)=1/4+2i\). The previous note does not require a change.

The starting result and smoothing transform come from Suvrit Sra, *Some positivity properties of Riemann Xi under smoothing* (v1, released 2026-11-11), https://suvrit.github.io/papers/riem-xi-smoothing/, particularly Propositions 2.2 and 3.1–3.2. The author already proves for actual Xi that RH is equivalent to the relevant minimum Gaussian smoothing widths being zero. **That equivalence is not a Project Riemann discovery.**

## 2. Exact synthetic profile and quantitative obstruction

Let \(a=63/16\) and

\[
P(u)=\frac{(u+1)^{10}(u+6)^{16}[(u+a)^2+1]}{6^{16}(a^2+1)},\qquad
H(t)=10e^{-t}+16e^{-6t}+2e^{-at}\cos t.
\]

The polynomial has negative real roots -1 and -6 and one conjugate pair \(-a\pm i\). Take \(G_\sigma(w)=c_\sigma e^{-w^2/(4\sigma)}\), where \(c_\sigma=(4\pi\sigma)^{-1/2}\). The symmetrized smoothed zero profile (counting multiplicities) is

\[
\begin{aligned}
p_\sigma(x)/c_\sigma={}&
5\big(e^{-(x-1)^2/(4\sigma)}+e^{-(x+1)^2/(4\sigma)}\big)\\
&+8\big(e^{-(x-\sqrt6)^2/(4\sigma)}+e^{-(x+\sqrt6)^2/(4\sigma)}\big)\\
&+e^{[(1/4)^2-(x-2)^2]/(4\sigma)}
 \cos\!\big((x-2)/(8\sigma)\big)\\
&+e^{[(1/4)^2-(x+2)^2]/(4\sigma)}
 \cos\!\big((x+2)/(8\sigma)\big).
\end{aligned}
\]

**Proposition (exact rational sign certificate).** At \(\sigma=1/50\), \(x=33/20\), one has

\[
\boxed{\quad p_{1/50}(33/20)< -\frac{37}{1500}c_{1/50}<0.\quad}
\]

**Proof.** The two cosine phases and exponents at this point give:

- Near complex term: \(e^{-3/4}\cos(35/16)<-\tfrac12e^{-3/4}<-\tfrac16\). The cosine bound follows from \(2\pi/3<35/16<4\pi/3\), using \(3<\pi<22/7\). The last inequality uses \(e<3\).
- Far complex term: absolute magnitude at most \(e^{-663/4}<e^{-5}<1/100\).
- The ten real \(z=1\) contributions total at most \(10e^{-169/32}<10e^{-5}<1/10\).
- Since \(\sqrt6>12/5\), the sixteen real \(z=\sqrt6\) contributions total at most \(16e^{-225/32}<16e^{-7}<16/500\).

All the exponential comparisons are exact inequalities: \(e^5>100\) is certified by the finite positive Taylor sum \(\sum_{k=0}^6 5^k/k!=16289/144>100\); \(e^2>1+2+2=5\) gives \(e^7>500\); and \(e<3\) is elementary. Summing yields

\[
p_{1/50}(33/20)/c_{1/50}
<\frac1{10}+\frac{16}{500}+\frac1{100}-\frac16
=-\frac{37}{1500}.
\]

Wolfram independently evaluated the normalized profile as approximately -0.24505125143686939924; a separate standard-library Python checker reproduced the exact rational enclosure. The numerical value is a diagnostic, not the certificate.

By Bernstein's Laplace-transform uniqueness (and Sra's Proposition 2.2), a negative smoothed zero profile means \(H_\sigma\) is **not** completely monotone at \(\sigma=1/50\).

## 3. An exact synthetic threshold bracket

Round 12 established that \((-1)^n H^{(n)}(t)>0\) for **every** integer \(n\ge0\) on \(0\le t\le1\). The Gaussian time change

\[
H_\sigma(t)=(1+4\sigma t)^{-1/2}H\big(t/(1+4\sigma t)\big)
\]

has completely monotone composition factors for \(\sigma\ge1/4\), since the inner time map lands in (0,1), is a Bernstein function, and the outer prefactor is completely monotone. Therefore \(H_\sigma\) is completely monotone for every \(\sigma\ge1/4\).

Gaussian convolution preserves profile positivity when smoothing is increased, and the completely-monotone set is closed at positive endpoints by local derivative convergence. Thus negativity at \(\sigma=1/50\) and positivity at \(\sigma=1/4\) give the exact bracket

\[
\boxed{\quad 1/50<\sigma_H^{\rm syn}\le1/4.\quad}
\]

The threshold is for this **synthetic polynomial only**. It says nothing about \(\sigma_H\) for actual Riemann Xi, whose value remains unknown. The source's smaller bound \(\sigma_\ell<0.00218\) concerns the **different** quantity \(H_\sigma/t\) for actual Xi and must never be substituted into this synthetic \(H_\sigma\) bracket.

## 4. Prime cutoff growth from the band-limited approach

Sra's Theorem 2.5 uses a density \(\kappa_A\) with half-variance \(w=\pi^2/(8A^2)\) and Fourier support \([-2A,2A]\). In the associated explicit formula, prime powers occur below \(e^{2A}\). Eliminating \(A\) gives the scale

\[
\boxed{\quad N(w)=\exp\!\left(\frac{\pi}{\sqrt{2w}}\right).\quad}
\]

For width \(w=\pi^2/288\) and \(A=6\), the prime cutoff is \(e^{12}\sim1.63\times 10^5\), matching the published certificate. For target \(w=10^{-3}\), the corresponding cutoff within this **same method** would be about \(3.2\times10^{30}\); for \(w=10^{-4}\), about \(3.0\times10^{96}\).

This is a **scaling deduction**, not an assertion that the published positivity theorem extends to arbitrary \(A\), and not a lower bound on the computational difficulty of all possible RH proofs. It means that brute-force extension of the existing finite-prime certificate cannot reach zero smoothing. A genuinely **uniform, sign-sensitive arithmetic estimate** would be needed to take \(A\to\infty\) by this route. That has not been proved.

## 5. Verification and research decision

- Reran the existing November 12 standard-library checker, PASS.
- Wolfram directly checked the complex root mapping, full profile decomposition, high-precision point evaluation and independent numerical margin.
- New Python standard-library rational replay checked exponents, phase, Taylor lower bound, the strict rational profile enclosure and an independent numerical diagnostic. PASS.
- No Lean build, Arb validation, referee review, new zero exclusion or theorem about actual zeta was performed. No change to historical finite certificates or unresolved Haglund and marked-inverse obligations.
- **Verdict: NO_NEW_RH_FRONTIER_ADVANCE.** Retain the exact synthetic bracket as a counterexample benchmark; do not pursue arbitrary smoothing-width scans. The productive next mathematics, if any, must use xi-specific theta/prime structure to control the unsmoothed sign uniformly, not finite synthetic positivity.


## 6. November 13 focused stop test: no bandwidth-independent linear positivity margin

**Purpose:** Test one proposed next step—extend a single positive lower-bound margin from the published \(A=6\) certificate uniformly as \(A\to\infty\). This was **rejected** on elementary grounds, not promoted to an RH claim.

Sra's kernel (Section 2.3) is
\[
\kappa_A(x)=\frac{8A}{\pi^3}
\left(\frac{\cos(Ax)}{1-(2Ax/\pi)^2}\right)^2.
\]
Assume RH *only for this conditional no-go test*. Then the positive ordinates \(\gamma>0\) are real, the zero profile at \(x=0\) satisfies
\[
P_{\kappa_A}'(0)=2p_{\kappa_A}(0)
=2\sum_{\gamma>0}\kappa_A(\gamma).
\]
For all sufficiently large \(A\) (indeed \(A\ge1\) since the least ordinate exceeds 14), we have \(4A^2\gamma^2/\pi^2\ge2\). Thus
\[
0\le\kappa_A(\gamma)
\le\frac{2\pi}{A^3\gamma^4},
\quad
0\le P_{\kappa_A}'(0)
\le\frac{4\pi}{A^3}\sum_{\gamma>0}\gamma^{-4}.
\]
The sum is finite by the classical Riemann–von Mangoldt zero-counting formula \(N(T)=O(T\log T)\). Therefore
\[
\boxed{\,P_{\kappa_A}'(0)=O(A^{-3})\to0\quad\text{if RH holds}.\,}
\]
The published \(A=6\) estimate is \(P_{\kappa_6}(x)\ge10^{-8}\min(x,1)\). If a *fixed* \(c>0\) gave \(P_{\kappa_A}(x)\ge c\min(x,1)\) for every large \(A\), letting \(x\downarrow0\) would force \(P_{\kappa_A}'(0)\ge c\), contradicting the conditional upper bound above. The algebraic kernel rewrite was independently checked with Wolfram; the inequality uses the elementary estimate \((q-1)^2\ge q^2/4\) when \(q\ge2\). The cited primary sources are Sra's 2026-11-11 preprint, Theorem 2.5 and its kernel in Section 2.3, and the classical Riemann–von Mangoldt zero-counting formula.

**Decision / anti-accumulation stop:** Close the proposed **bandwidth-independent fixed-margin** route. It is incompatible even with the *hypothetical RH-true world*, so it cannot serve as a general proof of RH. This does **not** exclude bandwidth-dependent positivity bounds, an \(A\)-dependent shrinking margin, or an entirely different kernel. Reopen only if a new arithmetic estimate is proved independently, with its error explicitly smaller than a justified \(A\)-dependent lower margin. Do not produce extra synthetic examples, increase bandwidth numerically, or claim first-in-literature novelty on this basis.

**Status:** CONDITIONAL_STRUCTURAL_NO_GO / NO_NEW_RH_FRONTIER_ADVANCE. No new zero-free region, actual-zeta positivity theorem, marked-inverse estimate, or Haglund gap closure.
