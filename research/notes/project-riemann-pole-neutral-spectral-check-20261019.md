> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `7810c2b5aa6b8b9d768a59a8c800a2a7d28716e058f84cf378c14d0c45c47ac1`.

# Project Riemann — pole-neutral signed-prime-error test

**Date:** 2026-10-19. **Status:** written elementary/classical-input proof; not a new RH proof, no claimed novelty, no Lean 4 compilation or independent mathematical refereeing. This is a bounded strengthening of the previous signed-prime-error *no-go*. No existing evidence has been altered.

## The precise claim

Let \(\widehat f(z)=\int_\mathbb R f(t)e^{izt}\,dt\), \(g=f*\widetilde f\), \(\widetilde f(t)=f(-t)\), and
\[
D_L(f)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(\log n)
       -\int_1^\infty x^{-1/2}g(\log x)\,dx,
\]
for real even \(f\in C_c^\infty((-L,L))\). All contributions have finite support. Define the **pole-neutral** subspace by
\(\widehat f(i/2)=\widehat f(-i/2)=0\).

**Theorem, with classical PNT and continuous Kronecker approximation as stated inputs.** There exists an absolute \(c>0\) such that for every sufficiently large \(L\), there are nonzero real even pole-neutral tests \(f_+,f_-\in C_c^\infty((-L,L))\) with
\[
\frac{D_L(f_+)}{\|f_+\|_2^2}>ce^L,
\qquad
\frac{D_L(f_-)}{\|f_-\|_2^2}<-ce^L.
\]
The crude PNT estimate \(|D_L(f)|\ll e^L\|f\|_2^2\) shows both exponential orders are sharp within constants. The obstruction survives exact removal of BOTH pole directions; it is not an RH counterexample.

## Proof sketch with all decisive steps

Choose a fixed real even nonnegative nonzero \(\phi\in C_c^\infty((-\sigma,\sigma))\) and fixed \(c_0>\sigma\). Put \(a=L-c_0\) and \(b_L(t)=\phi(t-a)+\phi(t+a)\). For all large \(L\), \(b_L\) is real even and supported strictly inside \((-L,L)\), with \(\|b_L\|_2^2=2\|\phi\|_2^2\). Its autocorrelation is
\[
g_{b_L}(u)=2g_\phi(u)+g_\phi(u-2a)+g_\phi(u+2a)\ge0.
\]
The smooth weighted prime number theorem, with a fixed multiplicative interval determined by \(\phi\), gives
\[
S_L:=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g_{b_L}(\log n)
=e^a\left(\int\phi(t)e^{t/2}dt\right)^2+o(e^a).
\]
The terms with \(n=p^{2j}\), \(j\ge1\), contribute at most \(O(L^2)\), since \(\sum_{p\le e^L}(\log p)/p=O(L^2)\) trivially and \(\sum_p\sum_{j\ge2}(\log p)/p^j<\infty\).

For each fixed \(L\), only finitely many prime powers \(n<e^{2L}\) occur. Distinct prime logarithms are rationally linearly independent. The **continuous** Kronecker theorem therefore supplies arbitrarily large real \(T\) for which \(e^{iT\log p}\) tends simultaneously to \(+1\), or simultaneously to \(-1\), for every prime in this finite set. Set \(h_T(t)=\sqrt2\,b_L(t)\cos(Tt)\). Then \(\|h_T\|_2^2\to\|b_L\|_2^2\), while elementary trigonometric expansion and the Riemann–Lebesgue lemma imply
\[
g_{h_T}(u)=\cos(Tu)g_{b_L}(u)+o(1)
\]
at every fixed \(u\), and the continuous smooth main term in \(D_L\) tends to zero. Along the plus and minus phase sequences, respectively,
\[
D_L(h_T)\to S_L,
\qquad D_L(h_T)\to -S_L+2S_{L,\mathrm{even}}.
\]
Here \(S_{L,\mathrm{even}}=O(L^2)=o(e^L)\); thus the two limits have opposite signs of full exponential size.

For exact pole neutrality choose a fixed real even \(q\in C_c^\infty((-\sigma,\sigma))\) with \(\ell(q)>0\), where \(\ell(f)=\int f(t)e^{t/2}dt\). Because \(h_T\) is real even, its two pole transforms are both \(\ell(h_T)\), and \(\ell(h_T)\to0\) (in fact superpolynomially for fixed \(L\)) by Riemann–Lebesgue/integration by parts. Let
\[
f_T=h_T-\frac{\ell(h_T)}{\ell(q)}q.
\]
Then \(\widehat f_T(\pm i/2)=0\) **exactly**, \(\|f_T-h_T\|_2\to0\), and \(D_L(f_T)-D_L(h_T)\to0\) for fixed \(L\) by the boundedness of its finite-sum/compact-integral quadratic form. Select sufficiently large phase-approximating \(T\) for each sign, then let \(L\to\infty\). This proves the two inequalities.

## Why this does not violate Weil positivity

The exact prime–pole rearrangement in the previous checkpoint expresses the full Weil form as
\[
Q_W(f)=\frac1{2\pi}\int_{\mathbb R}|\widehat f(t)|^2B(t)dt-2D_L(f),
\qquad B(t)=\Re\psi_\Gamma(1/4+it/2)-\log\pi+\frac1{t^2+1/4}.
\]
The classical digamma expansion gives \(B(t)=\log(|t|/(2\pi))+o(1)\) at large real \(|t|\). For the modulated bumps and their vanishing pole corrections, the first term is
\[
\bigl(\log(T/(2\pi))+o(1)\bigr)\|b_L\|_2^2
\]
as \(T\to\infty\) for each fixed \(L\), whereas \(D_L(f_T)\) tends to a finite number depending on \(L\). Hence these rephased tests eventually have **positive** full Weil form. They do not exhibit any nonreal zeta zero or disprove RH.

## Decision and provenance

The spectral proposal to make the signed prime error uniformly small, or one-sided, is closed **even on the exact pole-neutral subspace**. The only remaining possibility here is a genuinely joint frequency-sensitive prime-plus-archimedean inequality; absent an independently provable new estimate, do not restart the same Weil-positivity manipulations. The present argument does not prove any RH-level zero exclusion and should not be advertised as a novel theorem before a literature search and expert scrutiny.

Sources checked: NIST DLMF §25.16 (PNT and RH-strength prime errors), §5.11.2 (digamma asymptotics), Encyclopedia of Mathematics (continuous Kronecker theorem); Chuk, arXiv:2608.24827 (2026 compact-window and frequency barriers); two previous Project Riemann signed-prime and spectral-aliasing checkpoint files. No WSL/Git/Codex/Lean state or historical k=2/k=3 evidence was modified. RH remains unproved, full k=2/k=3 verification **UNVERIFIED**, historical provenance **BLOCKED_UNWAIVED**.
