> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `bf452835700f150233d1539e7fd996a94c088f48ae89eb26df2c81f81399b850`.

# Project Riemann — first-power-core conditioning (bounded continuation)

**Date:** 19 October 2026. **Scientific classification:** New written *restricted-family* row-count deduction subject to the primary source's character/reciprocity normalization and the cited ordinary Hecke-character large sieve. Its **rational exponent certificate is exact**. It is not a proved improvement of the zeta zero-free region, not a full independent analytic audit, and not a Lean theorem. No novelty established. RH OPEN; Haglund k=2/k=3 UNVERIFIED; historical provenance BLOCKED_UNWAIVED.

## Source and original obligation

We use Xu–Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*, arXiv:2610.15291v2 (15 Oct 2026), particularly §§2, 4–6, for the physical sixth-power-free Eisenstein rows, normalized prime polynomials, amplitude bins, published row exponent `R_kappa`, the numerator-average input, and its conditional 0.8748867 result. We use the **ordinary primitive ray-character large sieve** as stated in `lem:ordinary-sieve` of the OpenAI *An unconditional first moment for cubic Gauss sums* source, which has a `(Z+Q^2)` right side and explicitly accommodates fixed local/ray data. This classical input has been read, not formally rebuilt in Lean. The original quasi-RH analytic inputs and their licensing hypotheses are inherited, not newly proved.

## New fixed-core conditioning deduction (written, source-dependent)

For one physical sixth-power-free row `u` prime to the fixed bad set, uniquely write `u=v*w` as coprime ideals, where `v` is squarefree and contains exactly primes appearing with exponent one, and every prime valuation in `w` is 2,3,4, or 5. Work in a dyadic family `Nu~U`, `Nv~V=U^theta`. Then `Nw~U/V` and, crucially, `Nrad(w)^2<=Nw`; the primitive character induced by the `w`-part has conductor norm `O((U/V)^(1/2))`, with fixed local factors. At each good prime its local character remains nontrivial, so its conductor support is the radical of `w`. The physical `chi_p(u)` factors as `chi_p(v)chi_p(w)`. For **fixed v**, its first factor can be absorbed in the polynomial coefficients, while the second is represented (after sextic reciprocity and a fixed finite ray-class split) by the variable primitive character induced by `w`. Zeros on nonunits are retained. The physical multiplicity over one inducing character is `O_epsilon(U^epsilon)`, using the finite valuation patterns.

For one amplitude class, the source supplies slot polynomials `Q_i(u;z)`, lengths `P_i=Z^{ell_i}`, `sum ell_i=ell`, amplitudes `0<=g_i<=delta/2`, and `q=sum ell_i*g_i/ell=delta*x`. Fix integer multiplicities `m_i<=5` by choosing the highest amplitude copies among five of each slot, to total prime-product length `M<=U/V`. The weighted-mean selection gives, after an arbitrarily fine fixed slot mesh,

    sum_i m_i ell_i*g_i >= (d(1-theta))*q - arbitrary small mesh loss,
    A_u:=product_i (1+|Q_i(u;z)|^2)^m_i >= U^{2*delta*x*(1-theta)-epsilon}.

The expression `A_u` is a finite positive combination of squared character polynomials supported on products of selected prime ideals with length `M<=U/V`. Each coefficient-vector squared norm is `O_epsilon(U^epsilon)`: disjoint prime windows, bounded powers `m_i<=5`, the `P_i^{-1/2}` normalizations and standard finite divisor bounds. For each fixed `v`, ordinary Hecke large sieve gives `O_epsilon((U/V+M)*U^epsilon)` for the sum over squarefull `w`. Summing the `O(V)` possibilities for `v` in a dyad yields `O_epsilon((U+V*M)*U^epsilon)=O_epsilon(U^{1+epsilon})`. Since the bin's `A_u` has the displayed lower bound, this gives the **candidate** uniform dyadic count

    #B_(theta) << U^{1-2*delta*x*(1-theta)+epsilon} (1+T1)^A.

This is a written source-dependent proof: a completely independent referee audit must check the exact reciprocity phases, ray/projective choices, zero extensions, fixed character multiplicity, smooth profiles and uniformity with all source moment uses. This text **does not** assert those issues have been formally checked. The bound is otherwise a standard large-sieve application; no tenth-moment conjecture is used.

## Exact rational exponent gate

Fix `b=1/100`, `ell=21/125`, `kappa=29991/40000`, `h=(1+b+3ell)/2=757/1000`, `ly=(1+b-ell)/2=421/1000`. Put `c=1/(3kappa)` and use exactly Xu–Sang's `R_kappa(delta,x)` from their equation (21) and their high-side endpoint expression (28). For the row restriction `Nv<=U^(1/40)`, set

    Rcond(delta,x) = 1 - (39/40)*2*delta*x,
    Rusable = min(R_kappa, Rcond).

The attached exact-rational Bernstein checker `check_core_conditioned_1_40_gate.py` establishes

    E(Rusable; delta,x) < -1/3000
    for every 1/8<=delta<=5/6 and 0<=x<=1/2.

Its run returns 147 nodes, 74 certified leaves, depth 17, using two bivariate polynomials and exact fractions. A separate Wolfram quantifier elimination returned `False` for the existence of a violating pair. The existing scalar geometry checks from `check_first_power_conductor_gate.py` hold for this same parameter tuple (`zeta=1/1000000`, `g=1/3000`, `g_star=1/4000`), and `g-2*zeta>g_star`. Fixed mesh, height and analytic epsilon losses must fit the remaining strict reserve. The certificate validates only rational algebra, not the analytic rows or the original quasi-RH bridge.

## Why this does NOT complete the proof

The family `Nv<=U^(1/40)` is sparse and excludes the **squarefree physical rows**, where `v=u` and `theta=1`. Those are still bounded only by the published `R_kappa` argument. In fact, at the algebraically admissible test parameters `delta=27/50`, `x=1/2`, the published endpoint is

    E_old = 13241129843269 / 6369554560200000 > 0.

This exact rational value is **not an assertion that an actual physical row realizes the corresponding extreme amplitude bin**; it shows that the existing upper-bound system permits a positive exponent there. The conductor-conditioning argument becomes powerless as `theta ->1`, so it does not remove that witness. The observed Xu–Sang squarefree-squarefree sextic large-sieve lower-bound result in the stated unbalanced regime does not prove that the *particular structured prime-slot coefficients* saturate it.

## Research decision

**Retain the restricted-family deduction for independent verification, but STOP enlarging the small-core exponent through parameter tweaking.** It does not control the first-power-rich/squarefree rows which cause the unresolved exponent obstruction. The only proof-critical next question in this route is an independent, signed or structured-coefficient cancellation estimate for those rows that improves the published `R_kappa` bound, with a fixed power margin. No such estimate is proved here, hence no Codex campaign is justified solely by this note. Nothing historical is modified or waived.
