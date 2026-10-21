> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `c049bb0b10e7ee0a46ea26b674fe10ec053ff775d997e4df0f42ca0667b9cd31`.

# Project Riemann — signed prime discrepancy: operator-norm obstruction and Sobolev escape hatch

**19 October 2026. Scope:** independently derived written argument under classical PNT, Kronecker approximation, elementary Fourier/functional analysis. NOT a proof of RH, not a new zero-free half-plane, not externally refereed or Lean-checked, novelty unverified. Project k=2/k=3 remains `UNVERIFIED`; historical provenance remains `BLOCKED_UNWAIVED`.

## 1. Exact setup and accepted input

Let `L>0` and let `f∈C_c^∞((-L,L))` be **real even**, `g=f*tilde f`, `tilde f(t)=f(-t)`. Thus `g(u)=∫f(t)f(t-u)dt` is real even and supported in `[-2L,2L]`. Write `ψ(x)=Σ_{n≤x}Λ(n)` and `E(x)=ψ(x)-x`, `x≥1`. In the compact-support normalization of the Weil explicit formula, the residual prime discrepancy is

`D_L(f)=∫_{(1,∞)} x^(-1/2)g(log x) dE(x)`
`       = Σ_{n≥2}Λ(n)/sqrt(n)*g(log n) − ∫_1^∞ x^(-1/2) g(log x)dx.`

Both expressions are exact finite/compactly supported expressions. This identity is independent of RH. The signed discrepancy is only one piece of the Weil form, not the full Weil form.

## 2. Main unconditional theorem: the signed discrepancy has full exponential norm

Define `M(L) = sup_{f real even smooth supported (-L,L), f!=0} |D_L(f)|/||f||_2^2`.

**THEOREM (written proof with classical inputs):** There exist constants `0<c<C<∞` such that for all sufficiently large `L`,

`c exp(L) ≤ M(L) ≤ C exp(L)`.

In particular, **for no fixed η>0** can one have a bound `|D_L(f)| ≪ exp((1−η)L)||f||²` uniformly over all such test functions.

### Upper bound

Cauchy–Schwarz gives `|g(u)|≤||f||²`. PNT and partial summation imply

`Σ_{n≤exp(2L)} Λ(n)/sqrt(n) = (2+o(1))exp(L)`.

The smooth main term has absolute value ≤`2(exp(L)−1)||f||²`. Therefore

`M(L) ≤ (4+o(1))exp(L)`.

### Lower bound: rephase all finitely many genuine prime powers

Fix a nonzero, smooth, real even nonnegative bump `φ` supported in `(-σ,σ)`, with `0<σ<c0` fixed. For `L` large put `a=L−c0` and `b_L(t)=φ(t−a)+φ(t+a)`. The support is inside `(-L,L)`, and `||b_L||²=2||φ||²`. Write `g_φ=φ*tilde φ`. Then

`g_{b_L}(u)=2g_φ(u)+g_φ(u−2a)+g_φ(u+2a)`.

By the ordinary PNT applied with a fixed smooth weight on a multiplicative interval,

`Σ_{n≥2} Λ(n)/sqrt(n) g_{b_L}(log n)
   = exp(a) ∫_R exp(v/2)g_φ(v)dv + o(exp(a))
   = exp(L−c0) [∫_R φ(t)exp(t/2)dt]^2 + o(exp(L))`.

The coefficient is strictly positive; the self-overlap near `u=0` contributes only `O(1)`.

For each fixed `L`, there are finitely many primes `p<exp(2L)`. Their logarithms are linearly independent over Q by unique factorization. Continuous Kronecker approximation supplies a sequence `T_j→∞` with `exp(i T_j log p)→1` for every such prime. Thus `exp(iT_j log n)→1` for every prime power `n<exp(2L)`.

Set `f_j(t)=sqrt(2)b_L(t)cos(T_j t)`. These are real even admissible tests. The identity `2cos A cos B=cos(A−B)+cos(A+B)` gives

`g_{f_j}(u)=cos(T_j u)g_{b_L}(u) + ∫b_L(t)b_L(t−u)cos(2T_j t−T_j u)dt`.

For each fixed `u`, the second integral tends to zero by Riemann–Lebesgue, and `||f_j||²→||b_L||²`. On the finitely many prime-power shifts, Kronecker approximation forces `g_{f_j}(log n)→g_{b_L}(log n)`. Meanwhile

`∫_0^(2L) exp(u/2)g_{f_j}(u)du→0`,

by Riemann–Lebesgue and dominated convergence on a fixed compact interval. Consequently,

`D_L(f_j)→Σ_{n≥2}Λ(n)/sqrt(n)g_{b_L}(log n)`.

As `L→∞`, the displayed asymptotic and the norm give

`liminf_(L→∞) exp(−L) M(L)
  ≥ exp(−c0) [∫φ(t)exp(t/2)dt]^2 / (2||φ||²) > 0`.

This proves the theorem. No zero-counting premise or RH is used.

## 3. Conditional Sobolev estimate: why this does not defeat every arithmetic approach

Put `E_0(x)=ψ(x)−x+1`, so `E_0(1)=0` and `dE_0=dE`. Integration by parts gives the **exact** identity

`D_L(f) = −∫_0^(2L) E_0(exp(u))exp(−u/2)[g'(u)−g(u)/2]du`.

If one has a classical prime-error bound `|E_0(x)|≤C_θ x^θ` with a **fixed** `θ>1/2`, then `|g|≤||f||²` and `|g'|≤||f||*||f'||` imply

`|D_L(f)| ≤ C_θ (exp((2θ−1)L)−1)/(θ−1/2)
  * (||f||*||f'|| + ||f||²/2)`.

This is not an unconditional claim for an arbitrarily chosen θ; it is conditional on an independently established prime-counting bound at that exponent (which must be sourced and accepted at its actual scope). For bounded `||f'||/||f||`, it provides an exponential improvement over the unrestricted `exp(L)` bound. It does not extend to all tests: the Kronecker-rephased functions have arbitrarily large derivative norms. A universal power-saving bound would be **false**.

## 4. Scientific interpretation and stop gate

The issue is not simply that the cumulative prime-counting error `ψ(x)−x` is insufficiently small. An arbitrary test can oscillate at frequencies that almost simultaneously align the phases of every prime below `exp(2L)`. This recovers the full prime sum while the smooth PNT term averages to zero. The archimedean component of the **full** Weil form grows with the frequency and may counteract this effect; the theorem does not give a negative Weil test or a counterexample to RH.

The only viable further spectral route must couple arithmetic cancellation to the test's **frequency distribution** and the archimedean term, rather than seek a uniform error-operator power saving. No such joint estimate was produced. The checked result is a NO-GO for a specific strategy; do not restart generic Weil positivity and numerical-window amplification.

## 5. Sources and status

- Primary Weil-form normalization and window barrier: arXiv:2608.24827v2, https://arxiv.org/html/2608.24827v2. The v2 HTML and abstract search indexing have inconsistent author metadata; this report cites the version and mathematical statement rather than relying on attribution.
- PNT equivalent to `ψ(x)=x+o(x)`: NIST DLMF §25.16, https://dlmf.nist.gov/25.16.
- Continuous Kronecker theorem: Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Kronecker_theorem.
- Input checkpoint: `Project_Riemann_Spectral_Aliasing_Prime_Cancellation_Checkpoint_20261019.md` (the prior exact rearrangement and norm bounds, not independently re-audited in full here).

**Verification classes:** Elementary identities and norm estimates: reconstructed in writing, plus exact trig symbolic check. PNT, Kronecker, Riemann–Lebesgue: classical-input premises. Lean: not available in this runtime; no declarations compiled. Numerical evidence: none needed. Historical inputs/evidence/refs/services remain untouched. `NO_NEW_RH_FRONTIER_ADVANCE`.
