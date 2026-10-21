> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `a0209951b7f9f0702edf8ee5058d64fe0c7831414304407320167f422c8a7263`.

# Project Riemann — Aryan even/odd kernel checkpoint (18 October 2026)

**Verdict:** `NO_NEW_RH_FRONTIER_ADVANCE`. The proposed averaged detector has a valid elementary sign structure but does **not** yield a universal off-line zero-exclusion inequality. A precise periodic spectral counterconfiguration is given below. Nothing here proves RH or complete k=2/k=3, and historical provenance remains `BLOCKED_UNWAIVED`.

**Evidence scope:** Primary source F. Aryan, *On the Imaginary Part of ζ′/ζ*, arXiv:2610.12853v1 (9 October 2026), https://arxiv.org/html/2610.12853 . Read Theorem 2.1, Remark 1, Corollary 2.2, Lemmas 4.1–4.3, their written proofs and Proposition 5.1. The handoff `Project_Riemann_New_Chat_Handoff_20261018.zip` was located in the ChatGPT Library but direct raw-byte materialization was denied. The separately available `Project_Riemann_New_Chat_Prompt_20261018.md` and four supplied Markdown reports were read; therefore the ZIP's internal README and research delta have **not** been independently read in this container. Do not treat ZIP contents as audited here.

## 1. Exact normalizations and published analytic boundary

Let `L=log T`, `t ≍ T`, and

\[
 Z(s)=-\frac2L\sum_{n<T}\frac{\Lambda(n)}{n^s}\left(1-\frac{\log n}{L}\right),\qquad
 K(z)=\left(\frac{\sin(z/2)}{z/2}\right)^2=2\int_0^1(1-u)\cos(uz)\,du,
\]
\[
 A(z)=2\int_0^1(1-u)\sin(uz)\,du=\frac{2(z-\sin z)}{z^2}.
\]

**Important:** The Appendix A kernel `(sin z/z)^2` uses a different variable convention. The detector below uses `K(z)=sinc^2(z/2)`, paired with the paper's `A(z)`.

The paper reports, unconditionally for `t ≍ T`, with symmetric summation over zeros,
\[
 \operatorname{Re}Z(1/2+it)=-1+\operatorname{Re}\sum_\rho K(z_\rho(t))+O(L^{-1}),
 \quad\operatorname{Im}Z(1/2+it)=\operatorname{Re}\sum_\rho A(z_\rho(t))+O(L^{-1}),
\]
where `z_ρ(t)=−iL(ρ−1/2−it)`. The odd formula is its Theorem 2.1; the even formula follows from the previously established higher-Fejér identity. The source gives derivative control `E'_k(t)≪1/(TL)` for `1≤k≤2L` in Lemma 4.2. Its recursive identity and finite kernel summations were checked algebraically. The **entire uniform analytic contour bound has not been independently proved here**, and remains `REPORTED_NOT_REPLAYED`. A third-party T0 machine review also questions the completeness of the uniform derivative justification; this is only a caution, not independent proof of an error.

The candidate below avoids differentiating the `O(L^{-1})` **final** error: it uses finite differences at `t ±1/L`. This preserves an `O(L^{-1})` remainder, conditional on the two published explicit formulas with their stated uniformity.

## 2. Corrected shortened shifted-average normalization

Corollary 2.2 prints the full-length `β=1` answer while specifying `β=1−ε` for fixed `ε>0`. Its own Section 5 proof actually gives
\[
 M_\beta(\alpha)=\frac{2}{\beta}\int_0^\beta u(1-u/\beta)\sin(\alpha u)\,du
 =\frac{2\{2-2\cos(\alpha\beta)-\alpha\beta\sin(\alpha\beta)\}}{\beta^2\alpha^3},
\]
with the expression continuously extended at `α=0`, where the limit is zero. As `α→0`, `M_β(α)=β²α/6+O_β(α³)`, not `α/6+O(α³)` unless `β=1`. Thus the printed Corollary 2.2's `β=1` expression does not follow for **fixed** `0<ε<1`. This is an algebraic discrepancy in the stated corollary; it does not by itself invalidate Theorem 2.1. The finite integral was independently evaluated in a symbolic Wolfram calculation. The number-theoretic passage from Landau–Gonek to the average is the paper's stated input, not locally re-proved.

## 3. Our detector and exact prime-side identity

Define
\[
 B(z)=\tfrac13K(z)-A'(z),\quad
 H_*(z)=\tfrac12\int_{-1}^1B(z+v)\,dv.
\]
Then for `x∈ℝ`,
\[
 B(z)=\frac4{3z^3}\bigl[z(2+\cos z)-3\sin z\bigr],\quad B(0)=0,
\]
\[
 H_*(z)=\int_{-1}^1 q(u)e^{iuz}\,du,\quad
 q(u)=(1-|u|)(\tfrac13-|u|)\frac{\sin u}{u}\mathbf1_{[-1,1]}(u),\quad q(0)=\tfrac13.
\]

**Exact real sign:** `B(x)>0` for every real `x≠0`. For `0<x<π`, write `N(x)=x(2+cos x)−3 sin x`; `N(0)=0` and `N'(x)=2 sin(x/2)[2 sin(x/2)−x cos(x/2)]>0` since `tan v>v` on `(0,π/2)`. For `x≥π`, `N(x)≥x−3>0`. Evenness handles negative `x`. Therefore `H_*(x)>0` for all real `x`.

**Exact off-line local sign:** `H_*(ia)<0` for `a≥1`. Indeed, let `w(u)=(1-u)(1/3-u)` and `W(u)=∫_0^u w(v)dv=u(1-u)^2/3≥0`, with `W(0)=W(1)=0`. Then
\[
 H_*(ia)=-2\int_0^1W(u)\frac{d}{du}\left[\frac{\sin u}{u}\cosh(au)\right]du<0.
\]
For `0<u≤1, a≥1`, the logarithmic derivative is `a tanh(au)+cot u−1/u`. It is strictly positive because `a tanh(au)≥tanh u≥2u/3` and `1/u−cot u≤2u/5` (use `sin u−u cos u=∫_0^u v sin v dv≤u³/3` and `sin u≥5u/6`). The pointwise signs are therefore **PROVED_WITH_ELEMENTARY_CLASSICAL_INPUTS**.

For `v_n=(log n)/L`, the proposed zero sum, under the paper's two uniform explicit formulas and matched symmetric limits, obeys
\[
 \mathcal D_T(t):=\operatorname{Re}\sum_\rho H_*(z_\rho(t))
 =\frac13+\frac2L\sum_{n<T}\frac{\Lambda(n)}{\sqrt n}
 (1-v_n)(v_n-\tfrac13)\frac{\sin v_n}{v_n}\cos(t\log n)
 +O(L^{-1}).
\]
Derivation: average the `K` formula over `t−v/L` for `v∈[-1,1]`; replace the average of `A'` by the endpoint difference `(A(z+1)−A(z−1))/2`, i.e. the difference between odd identities at `t∓1/L`. Do **not** differentiate the terminal `O(L^{-1})` error.

## 4. Explicit global interference obstruction with 75% on-line zeros

Work in the microscopic coordinate `x=L(γ−t)`, with imaginary displacement `a=L|β−1/2|`. Begin with the on-line lattice at ordinates `2πj`, `j∈ℤ`. Its total detector sum equals the positive constant `1/3`, by Poisson periodization and the Fourier support of `q` in `[-1,1]`, with `q(±1)=0`.

In each interval of length `16π`, keep six simple on-line zeros at the residues
\[
 0,\quad2\pi,\quad4\pi,\quad6\pi,\quad8\pi,\quad10\pi,
\]
and replace the on-line zeros at `12π` and `14π` with **one reflected off-line pair** at ordinate `13π` and normalized horizontal displacements `±1`. Each period retains 8 zeros: **six on line (75%) and two off line (25%)**, with the correct local mean density `8/(16π)=1/(2π)`.

Exact Fourier series for the detector response from this synthetic spectrum:
\[
 \mathcal S(x)=\frac13+\frac12\sum_{m=1}^{7}q(m/8)
 \left(\cosh(m/8)-\cos(\pi m/8)\right)
 \cos\left(\frac{m(x-13\pi)}8\right).
\]
This follows by Fourier-series coefficients of the periodized `H_*` and the identity `2cosh u−2cos(πu)` for the replacement pair. It is an **exact** classical Fourier computation, not an actual zeta-zero identity.

There is a simple **exact rational certificate** that for every real `x`,
\[
 \mathcal S(x)>\frac1{75}>0.
\]
For `0≤u≤1`, bound `sin(u)/u≤1−u²/6+u⁴/120`; bound `cosh u` by `Σ_{j=0}^4 u^{2j}/(2j)!+1/3600000`; and for `0≤u≤7/8` use `π<63/20` and the degree-10 alternating Taylor polynomial `C_-(y)=Σ_{j=0}^5(-1)^j y^{2j}/(2j)!` to obtain `cos(πu)≥C_-((63/20)u)`. Define `q_+(u)=(1−u)|1/3−u|(1−u²/6+u⁴/120)`. Direct exact rational evaluation of the **seven** terms gives
\[
 U:=\frac12\sum_{m=1}^7q_+(m/8)\left[
 \sum_{j=0}^4\frac{(m/8)^{2j}}{(2j)!}+\frac1{3600000}
 -C_-(63m/160)\right]<\frac8{25}.
\]
Therefore `S(x)≥1/3−U>1/3−8/25=1/75`. Python `fractions.Fraction` and an independent Wolfram exact-rational evaluation both returned `U<8/25`; the decimal value is `U≈0.31744162928`. The inequalities needed to dominate the actual transcendental terms are stated above, so numerical rounding is not carrying the proof.

**Interpretation / NO-GO:** A reflected off-critical-line pair, correct mean density, and even a 75% simple critical-line fraction do **not** force the averaged scalar detector to turn negative. Its local negative response to a single pair can be cancelled by nearby zeros. Hence no RH-level exclusion follows from these scalar sign facts, symmetry, and mean density alone. The periodic spectrum is **artificial**, not a construction of actual zeta zeros; it does not satisfy or test the Euler product, exact theta modular identity, all arithmetic correlations, or the exact full counting formula. It does not rule out a genuinely stronger global *arithmetic* or matrix inequality. Do not extrapolate this model to all `a>0`: the explicit bound is proved here for `a=1`.

## 5. Decision and preservation

- **Accepted algebra/elementary analysis:** exact even/odd Fourier normalization; corrected `β` shifted-average formula conditional on the paper's Landau–Gonek asymptotic; strict signs of `B` and `H_*`; exact prime-side finite-difference transfer conditional on published explicit formulas; synthetic 75%-on-line no-go with exact rational bound.
- **Not independently proved in Lean:** the analytic contour bounds in Aryan's paper, Poisson periodization, or the Taylor majorant proof. The present sandbox has no installed `lean` or `lake`. No `LEAN_CHECKED_EXACT_STATEMENT` assertion is made. The rational certificate was independently checked by two algebra systems, which are **not** substitutes for Lean verification of its hypotheses.
- **No proof-critical forward step:** nothing establishes the required zero-free frontier for actual Xi_k. A new Codex campaign solely to accumulate further variations of this detector is **not warranted**. The next acceptable candidate must add a genuinely arithmetic, quantitative inequality surviving complete-zero interference and current literature checks.
- **Preservation:** no historical WSL/Git artifacts were accessed or changed; no service, external submission, publication, installation, or Codex campaign was started. RH is unproved, complete k=2/k=3 unverified, provenance `BLOCKED_UNWAIVED`.
