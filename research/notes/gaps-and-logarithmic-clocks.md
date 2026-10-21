> **SUPPLEMENTARY — NOT ADOPTED.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `f66b48f5f7643e3a2f34ea287926852b22b92e059903026bdb32b749ccc4e904`.

# Project Riemann — Geometric Gap Clock versus Arithmetic Logarithmic Clock

**Date:** 2026-10-20.  **Classification:** `ANALYTIC_GEOMETRIC_CLOCK / EXACT_SIGNED_DEFECT_EQUIVALENCE / NO_NEW_RH_FRONTIER_ADVANCE`.

**Purpose:** Continue from the October 20, 2026 first-harmonic prime-phase audit without reopening finite-prime Walsh, random Euler-product, marked-inverse-moment, or kernel positivity investigations. Test whether treating gaps as a geometric clock creates an *independent* analytic constraint on zeros of the genuine Riemann zeta function.

**Research outcome:** A geometric Dirichlet series built from actual consecutive-prime gaps has unconditional meromorphic continuation *past the critical line* using a published mean-square prime-gap theorem (abscissa `1/4`) or, accepting the stated analytic result in Stadlmann's preprint, to `Re(s)>0.23`. The RH-sensitive part is isolated in the signed mismatch `log p - (p_next-p)`. But the cumulative mismatch is exactly `theta(p_m)-p_(m+1)+2` and its uniform RH-strength bound is **equivalent to RH**. No new independent zero exclusion.

## 1. Precise inputs and provenance

Let `p_n` be consecutive rational primes and `g_n=p_(n+1)-p_n`. Two classical external bounds:

- **Published classical input:** The Peck/Maynard exponent, for every `eps>0`,
  `sum_(p_n<=X) g_n^2 <<_eps X^(5/4+eps)` (Peck, *Proc. London Math. Soc.* **76** (1998), 33–69; Maynard, arXiv:1201.1787, explicitly credits Peck). This suffices for all the conclusions in `Re(s)>1/4`. The full mean-square theorem rather than just an extreme-gap bound matters.
- **Stronger stated preprint input:** Julia Stadlmann, *On the mean square gap between primes*, arXiv:2212.10867, Theorem 1 claims `sum_(p_n<=X)g_n^2 <<_eps X^(1.23+eps)`. Under that input the abscissa improves from `1/4` to `0.23`. This audit does **not** reproduce the 71-page sieve proof, or claim independent refereeing of the preprint.

The completed analytic argument uses only these inputs and standard uniform convergence of holomorphic series, Euler-product differentiation in `Re(s)>1`, and the meromorphic continuation of zeta. The proof below is direct, with the source scope kept explicit.

Sources checked (primary or accompanying source information):

1. Peck, *Differences Between Consecutive Primes*, DOI: https://doi.org/10.1112/S0024611598000021 ; Maynard https://arxiv.org/abs/1201.1787 .
2. Stadlmann, https://arxiv.org/abs/2212.10867 .
3. BHP for independent reference on endpoint gaps: https://doi.org/10.1112/plms/83.3.532 .
4. Johnston & Trudgian, *A round of Pintz to celebrate oscillations in sums*, 2026, https://doi.org/10.1007/s10476-026-00181-1 — nearby established converse zero/oscillation theory; this audit is **not** a claimed novelty relative to all literature.

## 2. Analytic geometric clock theorem

**THEOREM A (proved modulo stated classical mean-square input).** For `Re(s)>1` let

`G(s) = sum_(n>=1) g_n p_n^(-s)`.

Define, for any `s` with `Re(s)>0.25` (or `Re(s)>0.23` with the Stadlmann input),

`E(s) = sum_(n>=1) [g_n p_n^(-s) - integral_(p_n)^(p_(n+1)) x^(-s) dx]`.

Then the error series converges absolutely and locally uniformly on the stated half-plane. Therefore `E` is holomorphic there, and `G` has a meromorphic continuation

`G(s)=2^(1-s)/(s-1)+E(s)`

with the **single simple pole at s=1** in that region. In particular, the geometric gap-clock continuation has no pole at a hypothetical nontrivial zeta zero, on or off the critical line.

**Proof.** On a compact set with `Re(s)>=sigma_0>0` and `|s|<=T`, differentiation on the real interval gives

`|d(x^(-s))/dx|=|s|x^(-Re(s)-1) <= T p_n^(-sigma_0-1)` for `x>=p_n`.

Integrating once more,

`|g_n p_n^(-s) - int_(p_n)^(p_(n+1))x^(-s)dx| <= (T/2) g_n^2 p_n^(-sigma_0-1)`.

On the dyadic block `2^j<=p_n<2^(j+1)`, the published mean-square estimate yields the bound

`O_eps(T * 2^(-j(sigma_0-1/4-eps)))`

and, with Stadlmann, the exponent is `sigma_0-0.23-eps`. Choose `eps` positive and smaller than the corresponding margin; the dyadic series converges geometrically, uniformly on the compact set. For `Re(s)>1` the original `G` converges absolutely and the disjoint intervals `[p_n,p_(n+1))` partition `[2,infinity)`, hence

`sum_n integral_(p_n)^(p_(n+1)) x^(-s)dx=int_2^infty x^(-s)dx=2^(1-s)/(s-1)`.

Analytic continuation then proves the claim. The residue at `s=1` is 1, so the pole cannot be removable. QED.

**Important restriction:** Meromorphic continuation without poles at zeta zeros does *not* mean that `G` has no zeros there or anywhere else. The theorem is about singularities of this different function, not the zeros of `zeta`.

**Universal control:** The quadrature proof works for any strictly increasing positive real sequence starting at 2 for which the squared numerical gaps satisfy the same growth bound. It cannot by itself distinguish ordinary primes from an artificial counting system.

## 3. Arithmetic logarithmic clock and the exact singularity-transfer identity

Define, initially for `Re(s)>1`,

`D(s) = sum_p (log p - g_p)p^(-s)`, with `g_p=p_next-p`,

and the higher prime-power correction

`J(s) = sum_p sum_(k>=2) (log p)p^(-ks)`.

The latter is absolutely and locally uniformly convergent for `Re(s)>1/2`, since it is majorized on compact subsets by a constant times `sum_p log(p)p^(-2sigma_0)`.

Differentiating the genuine Euler product for `zeta` in `Re(s)>1` yields the exact identity

`-zeta'(s)/zeta(s) = [2^(1-s)/(s-1)] + E(s) + D(s) + J(s)`.       (1)

The right-hand side defines a meromorphic continuation of `D` to `Re(s)>1/2`; the geometric bulk, `E`, and `J` are holomorphic at any hypothetical nontrivial zero `rho` with `Re(rho)>1/2`. If `rho` has multiplicity `m`, then

`Res_(s=rho) D(s) = -m`.                                        (2)

The pole at `s=1` from `-zeta'/zeta` cancels the geometric bulk pole, so `D` is holomorphic there. Equation (2) is a **conditional diagnostic**, not a new exclusion of `rho`. Requiring `D` to be holomorphic at every point of the entire half-plane `Re(s)>1/2` is equivalent to the zero-free conclusion on that half-plane, and hence to RH using the functional equation.

This formula precisely identifies where the regularized geometric clock stops being sufficient: the remaining signed weight is `log p - actual gap`, the mismatch between a logarithmic arithmetic clock and a numerical gap clock.

## 4. Exact finite-level obstruction (no circular hypothesis hidden)

Let `theta(x)=sum_(p<=x) log p` and define the finite signed defect

`D_m = sum_(j=1)^m (log p_j - g_j)`.

Since prime gaps telescope,

`sum_(j=1)^m g_j = p_(m+1)-2`, hence

`D_m = theta(p_m)-p_(m+1)+2`,                              (3)

`D_m-D_(m-1)=log(p_m)-g_m`.                               (4)

**THEOREM B (unconditional elementary equivalence).** For every fixed `0<alpha<1`,

`D_m=O(p_m^alpha)` uniformly in `m` **if and only if** `theta(x)-x=O(x^alpha)` uniformly for all large `x`. The equivalence extends to the convention of exponents `alpha=1/2+eps` for every `eps>0` (and similarly harmless log factors). Therefore

`D_m=O_eps(p_m^(1/2+eps)) for every eps>0   <=>   RH`.

**Proof, forward.** Equation (4), using the bounds on `D_m,D_(m-1)` and `log p_m`, yields `g_m=O(p_m^alpha)`. Equation (3) then yields `theta(p_m)-p_m=O(p_m^alpha)`. For `p_m<=x<p_(m+1)`, the function theta is constant, so `|theta(x)-x|` differs from its value at `p_m` by at most `g_m`; this establishes the full `x` estimate.

**Proof, reverse.** Put `F(x)=theta(x)-x`. At consecutive primes, `F(p_(m+1))-F(p_m)=log(p_(m+1))-g_m`. The assumed bound on `F`, together with `p_(m+1)<2p_m` (Bertrand's postulate), yields `g_m=O(p_m^alpha)`. Equation (3) then gives `D_m=O(p_m^alpha)`. QED.

The final RH equivalence uses the standard prime-number-theoretic criterion `theta(x)-x=O_eps(x^(1/2+eps))` for all `eps>0`.

**Consequence:** The intuitive clock mismatch is mathematically exact, but asking for an RH-strength global bound on it would simply rename the missing theorem. No new arithmetic estimate has been obtained.

## 5. Computational checks and limitations

`verify_gap_clock.py` sieves 149,068 primes (last sieve prime 2,001,997), tests telescope and finite signed-defect identities for sample levels through 50,000, and evaluates the exact decomposition for sample `s=0.5`, `0.75`, `0.75+6i`, and `0.5+14i` up to the first 100,000 primes. Output is `verification.json` and `verification.log`.

For example, at `s=0.5` the partial geometric quadrature correction `E_m(s)` was:

| m | E_m(0.5) |
|---:|---:|
|100|1.1334609972|
|1,000|1.3018710100|
|10,000|1.3655640450|
|50,000|1.3838062631|
|100,000|1.3883746868|

At `s=0.75`, the corresponding values are `0.8500158622`, `0.8897044425`, `0.8975561961`, `0.8988185428`, `0.8990429067`. These are floating-point *diagnostics*, not a replacement for the analytic convergence proof.

`verify_exact_fraction.py` uses exact fractions at `s=2`, with first 10, 20, 100, and 250 primes, and returns **all identities exact** and positive quadrature corrections. The first 20-prime rational check was independently reproduced in Wolfram, which returned `{0,0,True}` for the quadrature difference, telescoping difference, and correction positivity.

No full external reproduction of Stadlmann's 71-page analytic theorem and no Lean 4 compilation were performed. All mathematical assertions here have explicit scopes. No numeric roots were used as zero evidence.

## 6. Stop/go decision

**PASS:** A distinct *geometric gap clock* constructed from actual primes possesses a holomorphic quadrature remainder in `Re(s)>1/4` with a published source, sharpened to `Re(s)>0.23` accepting Stadlmann's stated preprint theorem. This crosses the critical line with no RH assumption.

**PASS:** Exact decomposition (1) and pole-residue transfer (2) show that any hypothetical off-line zero survives entirely in the *signed* logarithm-minus-gap mismatch.

**NO-GO:** The summatory signed mismatch (3) is equivalent in strength to the standard theta error, by elementary identities (3)–(4). An RH-strength conjecture about it does not constitute an independent route. The decomposition has not excluded a hypothetical off-line zero or improved the established zero-free strip.

**Research action:** Close simple gap-clock regularization as a proof method. Reopen only for a **new, independently proved signed-correlation inequality** for the *actual* prime gaps that beats a known theta-error bound and survives control sequences. No Codex campaign without that precise inequality and a stop condition. Original Project Riemann historical evidence is untouched.

**Status:** RH open; complete Haglund `k=2/k=3` `UNVERIFIED`; prior marked-inverse moment `BLOCKED_NEW_MOMENT_ESTIMATE`; historical provenance `BLOCKED_UNWAIVED`.
