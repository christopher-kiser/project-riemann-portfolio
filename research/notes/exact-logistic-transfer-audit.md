> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `a7b796e466706083330b9390455c48e5732ce9f582c9c46c091a7d128af39409`.

# Project Riemann — Exact-logistic Guinand–Weil transfer audit

**Date:** 2026-10-19 (independent continuation).  **Verdict:**
`ANALYTIC_IDENTITY_EXTENDED_WITH_CLASSICAL_INPUTS / ZERO_PAIRING_TRANSFER_WITH_STATED_INDUCTION / FULL_ZFR_206_UNVERIFIED / NO_NEW_RH_FRONTIER_ADVANCE`.

This is a **bounded audit**, not a claimed new zero-free region, RH proof, or Haglund proof. It supersedes the *specific* open derivative-at-zero issue in the prior `ANALYTIC_GATE_AUDIT.md`, **not** its outstanding scalar or literature limitations. Original historical archive, hashes, Git refs, service state, and Codex runs were not changed.

## 1. Primary source, hypotheses, and exact logical scope

Bellotti, Trudgian, Yang, *Zero-free regions inspired by work of Heath-Brown*, arXiv:2603.21490v1 (March 23/24, 2026), https://arxiv.org/pdf/2603.21490 . The relevant **classical input** is their Lemma 7, attributed to Kadiri, Proposition 2.1 (PDF page 13). It requires a real compactly supported `C^2` function `g`, with

- `g'(0)=0`;
- at the right endpoint `D`, `g(D)=g'(D)=g''(D)=0`;
- Laplace transform `G(z)` and the usual zeta nontrivial zero count with multiplicities.

For the logistic proposal (the *full*, not a truncated theta/Heath-Brown kernel)

\[
f(u)=\frac{\eta w(\eta u)}{1+e^{-du}},\qquad d=2\sigma-1,
\qquad f(0)=\frac{\eta w(0)}2,
\quad f'(0)=\frac{\eta w(0)d}{4}>0,
\]

`w` is precisely the kernel in BTY Definition 1, with support `[0,U]`, `U=2 theta cot(theta)` and `theta=5669/5000`. Thus the source Lemma 7 **does not apply directly to f**.

Our analytic extension below is for fixed `s` with `Re(s)>1/2`, and `f` real `C²` supported in `[0,D]` with the usual three zero endpoint conditions. Uniform numeric error estimates are separate; this local extension alone is insufficient to establish the proposed R=4.85437.

## 2. Derivative-zero approximants leave EVERY prime sum unchanged

Fix a smooth cutoff `chi:[0,infinity)->[0,1]`, identically 1 in a neighborhood of 0 and 0 on `[1,infinity)`. Choose `0<eps<min(log 2,D)` and define

\[
 h_\varepsilon(u)=f'(0)u\chi(u/\varepsilon),
 \qquad g_\varepsilon(u)=f(u)-h_\varepsilon(u).
\]

Then `g_eps'(0)=0`, `g_eps(0)=f(0)`, and all endpoint conditions are unchanged; Kadiri's Lemma 7 applies verbatim. Since every nonzero term in the von Mangoldt sum comes from `n>=2` and `log n>=log 2>eps`, one has the **exact**, not asymptotic, equality

\[
  \sum_{n\ge1}\Lambda(n)n^{-s}g_\varepsilon(\log n)
 =\sum_{n\ge1}\Lambda(n)n^{-s}f(\log n).
\]

There is no change to the arithmetic detector, the positivity of its prime sum, or the trigonometric polynomial.

To pass the remaining terms to the limit: `h_eps=O(eps)` on support length `eps`, so its Laplace transform tends to zero at every fixed argument, uniformly in vertical strips of bounded real part. Moreover

\[
  h_\varepsilon''(u)=f'(0)\left[\frac2\varepsilon\chi'(u/\varepsilon)
        +\frac{u}{\varepsilon^2}\chi''(u/\varepsilon)\right],
\]

and its `L¹` norm is bounded independently of `eps`. Two integrations by parts give a constant `C_s` such that, for all sufficiently large `|Im(s-rho)|`,

\[
  |\Re(G_\varepsilon(s-\rho)-F(s-\rho))|
     \le \frac{C_s}{1+|\Im(s-\rho)|^2}
\]

uniformly in eps: the zero-at-0 condition on `h_eps` cancels the leading `1/z` term and its `L¹` second-derivative bound controls the remainder. Standard Riemann–von Mangoldt zero counting makes the majorant summable for fixed `s`, so dominated convergence passes the nontrivial-zero sum with multiplicities. All finite pole terms converge directly. **Important summation convention:** the displayed zeta-zero term means the absolutely convergent *sum of real parts* `sum_rho Re F(s-rho)`; the complex-valued series need not be absolutely convergent, and should not be rearranged without a prescribed height ordering.

This is a **fixed-s analytic result**; it is not by itself a numerical uniform estimate for every height.

## 3. The archimedean correction and its exact sign

Write

\[
 A(s)=-\tfrac12\log\pi+\tfrac12\psi(1+s/2),
 \quad H_g(z)=G(z)-g(0)/z.
\]

For a derivative-zero input `g`, integrating its Laplace transform twice by parts yields `G_2(z)/z²=H_g(z)` for `Re(z)>0`. In BTY/Kadiri Lemma 7, substitute this identity in the gamma remainder. Its digamma-contour term is

\[
 \frac1{2\pi}\int_{\mathbb R} H_g(s-1/2-iy)
       \Re\psi(1/4+iy/2)\,dy.
\]

For `Re(s)>1/2`, the integral is absolutely convergent: `H_g` is `O((1+|y|)^{-2})`, while the digamma factor is `O(log(2+|y|))`. The real digamma representation

\[
 \Re\psi(1/4+iy/2)=\psi(1/4)
  +\int_0^\infty\frac{e^{-r/4}[1-\cos(yr/2)]}{1-e^{-r}}\,dr
\]

is valid pointwise. For rigorous exchange with the Fourier integral, truncate `r` at positive endpoints and use the `1-cos` cancellation for small `r`; the relevant Fourier inverse is `-e^{-u/2}/(1-e^{-2u})` for `u>0`. The constants supported at `u=0` vanish because `g(u)-g(0)` is zero there. The extra `H_g(s)` term from Kadiri's displayed formula then makes the combined gamma remainder exactly

\[
 E_g(s)=-\int_0^\infty [g(u)-g(0)]
              \frac{e^{-(s+2)u}}{1-e^{-2u}}du.
\]

Under the `g_eps -> f` limit, the difference `h_eps` contributes `O(eps)` to this integral because `h_eps(u)=O(u)` near 0 while `(1-e^{-2u})^{-1}=O(1/u)`. Hence the generalized explicit formula becomes

\[
 \boxed{\Re\sum_{n\ge1}\frac{\Lambda(n)}{n^s}f(\log n)
   =\Re\left[f(0)A(s)+F(s-1)-\sum_\rho F(s-\rho)
     -\int_0^\infty(f(u)-f(0))\frac{e^{-(s+2)u}}{1-e^{-2u}}du\right].}
\]

Use the absolutely convergent trigamma identity

\[
 A'(s)=\int_0^\infty\frac{u e^{-(s+2)u}}{1-e^{-2u}}du
 \qquad(\Re s>-2)
\]

to split off the linear Taylor term. This gives the **corrected form**

\[
 \boxed{\Re S_f(s)=\Re\Bigl[f(0)A(s)-f'(0)A'(s)
       +F(s-1)-\sum_{\rho}F(s-\rho)+E_f(s)\Bigr],}
\]

\[
 \boxed{E_f(s)=-\int_0^\infty
    [f(u)-f(0)-u f'(0)]\frac{e^{-(s+2)u}}{1-e^{-2u}}du.}
\]

**Adversarial sign/shift check:** For the simple model weight `f(u)=exp(-h u)` (used solely as an analytic digamma consistency test), the correction reads `A(s+h)=A(s)+h A'(s) - int (exp(-hu)-1+hu)K_s(u) du`. Direct high-precision evaluation has residual <2×10⁻⁴⁷. This agrees with the sign `-f'(0)A'(s)` because `f'(0)=-h`. This is a consistency check, not the proof; the smooth-approximant argument provides the classical-input proof for compact weights.

## 4. Explicit uniform error bound, with separated finite certification

The previous exact-rational kernel bounds `w(0)<5.7`, `|w(v)-w(0)|<=117 v²`, and the logistic Taylor estimate give, uniformly on support and beyond,

\[
 |f(u)-f(0)-u f'(0)|\le
 \frac{5.7\eta}{48}u^3+117\eta^3u^2(\tfrac12+\tfrac u4).
\]

For `Re(s)=sigma>=0.993`, `a=Re(s)+2>=2.993`, define

\[
 I_n(a)=\int_0^\infty \frac{u^n e^{-au}}{1-e^{-2u}}du
 \le n!\left(a^{-n-1}+\frac{a^{-n}}{2n}\right)\quad (n=2,3)
\]

using `1/(1-e^{-2u}) <= 1+1/(2u)`. Consequently when `eta<=0.007171`,

\[
  \frac{|E_f(s)|}{\eta}
   \le \frac{5.7}{48}I_3(2.993)
        +117\eta^2\bigl(\tfrac12 I_2(2.993)+\tfrac14 I_3(2.993)\bigr)
   = \frac{4451707598741271653}{320986567545604000000}
   <0.014.
\]

The supplied `verify_transfer_constants.py` rechecks this rational inequality *without floating-point pass/fail decisions*, the tail coefficient comparison, a parameter-interval instance, and the high-precision digamma consistency test. Original `check_exact_logistic.py` and `check_scalar_rational.py` were run again unchanged; see `VERIFICATION_LOG.txt`. The real hypothesis `eta >= 1-sigma` remains a **separately required induction condition**; a checked sample does not prove that condition universally.

## 5. Reflected zero-pairing: exact applicability interval

For a nontrivial zero `rho=beta+i gamma`, pair it with `rho*=1-conjugate(rho)=1-beta+i gamma`, **not** with a zero of the opposite ordinate. Put `s_k=sigma+ik t` and `d=2sigma-1`. Then the relevant paired contribution is

\[
 B(a,y)=\Re F(a+iy)+\Re F(d-a+iy),\quad
 a=\sigma-\beta,\quad y=kt-\gamma,
\]

since the sign of the second imaginary part does not affect its real part. Previous bounded lemma, reproduced by exact-rational checker, says

- `B(a,y)>=0` for `0<=a<=d`, all real y;
- `B(a,y)>=-38 eta/y²` for `-eta<=a<=d+eta`, nonzero y.

When the induction gives `beta<=sigma` for the finite-height zeros, its reflected partner also obeys `a<=d`, giving nonnegative pairs. For *all* nontrivial zeros (`0<beta<1`), the real parameter satisfies `sigma-1<a<sigma`, which is inside `[-eta,d+eta]` exactly when `eta>=1-sigma`. Under the same initial height cutoff, induction, and zero-counting hypotheses as BTY Lemma 6, the very-high-zero tail therefore inherits their estimate with our `38` replacing their `44`; the source's `-10^{-8}` allowance is retained.

This is a **transfer relative to the named zero-count and induction inputs**, not an independent proof of the entire source Lemma 6 or of the full iterative zero-free theorem. Multiplicities are retained in the zero sum; the potentially exceptional pair from a chosen zero contributes at least once even if it has multiplicity >1.

## 6. What remains actually unresolved

1. **Full scalar/comparison result** at `A=0.206`: the saved negative rational margin about `-0.00266458` is conditional on BTY's bulk lower bound `C1(mu)` and several other analytic estimates.
2. **High-k archimedean and pole bounds**, with the corrected `-f'(0)A'(s)` term included for all `k=0,...,16`; no independent complete uniform constants have been certified in this audit.
3. **Bulk moment envelope** `a1 W(1-mu)-W(-mu)>=C1(mu)` across the required continuous parameter interval. Previous samples are not a rigorous interval certificate.
4. **All-height finalization**: low-height zero verification, tiny-step induction, and explicit Littlewood-range stitching have not been completely rerun.
5. **Literature relevance**: the 2026 OpenAI quasi-RH uniform zero-free halfplane `Re(s)>7/8` and follow-up small improvements **were already recorded in the October 19 master handoff**. If accepted with the announced Lean formalization, they subsume any classical `1-0.206/log t` boundary in terms of *excluded zeros*. An independent classical inequality might still be of technical interest, but it does not move the active RH zero-exclusion frontier.

The new exact-logistic transfer closes an isolated classical-formula hypothesis issue and supports the local analytic lemmas. **It does not exclude a single new hypothetical off-critical-line zeta zero.** Therefore no additional Codex run or larger constant-optimization campaign is justified. The next true RH frontier is the interior of the strip and would require a fresh, independent phase-sensitive arithmetic theorem, not another smoothing parameter fit.

## 7. Verification and preservation

- Source: https://arxiv.org/pdf/2603.21490, Definition 1, Lemmas 6–9, equations 27–29, 45–48.
- This directory is **additive**. It contains this report, deterministic verification script, verification log, and SHA256 manifest.
- Existing original files were read, not edited. No Git refs/services altered; no Codex launched.
- Lean 4 and Lake are not installed in this runtime. Nothing is called Lean-checked.
- `RH=OPEN`, `HAGLUND_K2_K3=UNVERIFIED`, `MARKED_MOMENT=BLOCKED_NEW_MOMENT_ESTIMATE`, `PROVENANCE=BLOCKED_UNWAIVED`.
