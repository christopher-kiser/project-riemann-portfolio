> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `9991ad95ecc6aca86ee91d7a53aa8a4cc096c0a056397ce1e53218c8de801902`.

# Project Riemann — first-power-core conductor reduction

**19 October 2026. Status: new written arithmetic deduction under a published ordinary Hecke-character large-sieve input; exact endpoint algebra certified. No RH frontier advance. Not independently refereed or Lean-compiled.**

## 1. Objective and accepted sources

Continue the squarefull-row reduction without reopening a tenth-moment conjecture. Main source: Xu–Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*, [arXiv:2610.15291v2](https://arxiv.org/html/2610.15291v2), Sections 2, 4–6, Appendix B. The required ordinary primitive-character large sieve is stated and proved as `lem:ordinary-sieve` in the [background-type1.tex source of *An unconditional first moment for cubic Gauss sums*](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/background-type1.tex). Its proof uses primitive Gauss sums, ray character orthogonality, and Huxley's planar additive large sieve. De Faveri's [arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045) gives the fixed-order character structure and the sixth-power-free row setting. The reported Xu–Sang zero-free result is itself conditional on prior analytic inputs; the present reduction inherits those limits.

For the physical sixth-power-free Eisenstein row `u`, define `v(u)` to be its squarefree product of primes appearing with valuation **exactly one**. Write `Nu ≍ U=Z^d`. Fix a nonnegative `tau`, and restrict to `Nv(u) <= U^tau`. For any good prime dividing `u`, its local order is `6/gcd(6,j)>1`, `1<=j<=5`; hence its primitive character is ramified at precisely the radical of `u` outside fixed primes. Consequently, including fixed ray factors,

    N f_u <<_S N rad(u) <= (Nu * Nv(u))^(1/2) <<_S U^((1+tau)/2).

For each inducing character, the possible valuation patterns number at most `5^omega(rad(u)) <<_eps U^eps`, apart from a fixed number of unit/ray choices. This **must not** be confused with applying a fixed-order sieve at physical row cutoff `sqrt(U)`; we instead apply the all-primitive-character conductor-aspect sieve at actual conductor cutoff `Q << U^((1+tau)/2)`.

## 2. Source-consistent prime-amplitude polynomial

In Xu–Sang's notation, the physical prime slots are

    Q_i(u;z) = P_i^(-1/2) sum_(p in slot i) overline(chi_p(u)) W_i(Np/P_i)(Np/P_i)^(z-1),

with `P_i=Z^ell_i`, `sum ell_i=ell`. The source's amplitude class records `g_i in [0,delta/2]`, `g_i>0 => |Q_i|>=P_i^g_i`, and `q=sum ell_i*g_i/ell=delta*x`.

Assume `d` is in the paper's retained intermediate-row range `d_min<=d<=h+zeta`, with `5 ell>h+zeta`, and fix the prime-slot mesh before taking limits. Form a multiset with five copies of every slot, sort by decreasing `g_i`, and select an initial segment of total log-Z length <=`d` with all but at most one copy included. This gives integers `0<=m_i<=5` such that

    sum m_i ell_i <= d,
    sum m_i ell_i g_i >= d*q - (delta/2)*max_i ell_i.

(The weighted mean over all five copies is still `q`.) With `A_u=prod_i(1+|Q_i(u;z)|^2)^m_i`, the amplitude bin implies

    A_u >= U^(2*q - delta*max_i(ell_i)/d).

This use of `1+|Q_i|^2` is essential: slots with `g_i=0` have no promised lower bound for `|Q_i|`.

Expand the nonnegative product by the binomial theorem:

    A_u = sum_(j_i<=m_i) [prod_i binom(m_i,j_i)] |prod_i Q_i(u;z)^j_i|^2.

Each inner product is one common Hecke character polynomial in the prime/ideal variable. Its product support has norm length at most `Z^(sum m_i ell_i) <= U`. Because there is a fixed number of disjoint prime windows and `j_i<=5`, elementary finite factorization bounds its squared coefficient norm by `U^eps`, uniformly along the fixed `Re z=17/50` contour. The bounded ratio `Np/P_i` prevents growth from imaginary heights. Fixed ray characters and primary-generator conventions are included in common coefficients; changing the row changes the inducing primitive character, not the coefficients. The primitive zero extension at every good ramified prime equals the original row character's zero extension.

Apply the standard ordinary primitive Hecke-character large sieve:

    sum_(primitive chi, Nf_chi<=Q) |sum_(Nn≲M) a_n chi(n)|^2
        << (Q^2+M)*(QM)^eps * sum |a_n|^2.

Here `Q^2<<U^(1+tau)` and `M<=U`, and each primitive character has only `U^eps` physical preimages. Therefore

    sum_(Nu≍U, Nv(u)<=U^tau) A_u << U^(1+tau+eps).

The amplitude lower bound yields the **small-first-power-core row count**

    #B_core << U^(1+tau-2*delta*x+eps) (1+T1)^A,

after a fixed mesh refinement. The height factor is written compatibly with the source; the ordinary sieve bound itself has uniform coefficient modulus along this contour. Combine this with Xu–Sang's independently supplied row-count bound, using

    R_core(delta,x) = min(R_kappa(delta,x), 1+tau-2*delta*x).

This improves only the restricted first-power-core rows. The large complementary family `Nv(u)>U^tau` is not controlled by this argument.

## 3. Exact endpoint parameter gate

Take `b=1/100`, `ell=21/125`, `kappa=29991/40000`, `h=757/1000`, `l_y=421/1000` and `tau=1/1000`. The previously preserved exact Bernstein certificate
`check_squarefull_mixed_degree_gate.py` proves

    min(E_old,E_squarefull) < -1/1000

over `delta in [1/8,5/6]`, `x in [0,1/2]`, with
`R_squarefull=1-2*delta*x`. The new row exponent adds exactly `tau` to that restricted exponent, raising its high-side endpoint by `(3h/4)*tau=2271/4000000`. Hence

    min(E_old,E_core) < -1729/4000000 < -1/3000

throughout the same rectangle. Both source conditions needed to apply its existing numerator average are preserved, because the new row exponent is combined with (and is never larger than) the published `R_kappa`.

All scalar parameter geometry and the small-row/floor inequalities of Xu–Sang Section 6.2 pass exact rational checking for `zeta=1/1000000`, `g=1/3000`, `g_star=1/4000` (the source requires `0<g_star<1/1000`, `2*zeta<1/1000`, and `g-2*zeta>g_star`). The fixed mesh and analytic eps/height losses must still be chosen within the positive reserve. See `check_first_power_conductor_gate.py`.

## 4. Scope, challenges, and stop

- **Arithmetic count:** justified by the source-backed ordinary conductor-aspect sieve and the explicit binomial-polynomial reduction, with ray/multiplicity caveats stated. It has not been independently checked in Lean or by an external number theorist.
- **Exact algebra:** the older 149-node Bernstein certificate was rerun and the extension's margin, geometry, and lower-row inequalities independently checked with exact fractions.
- **Not proved:** the required high-side cancellation for rows whose exponent-one product exceeds `U^(1/1000)`. Such rows may dominate. No new zero-free half-plane for zeta follows.
- **Scientific novelty:** not established. This is a conditional refinement of the proof bookkeeping for one sparse arithmetic subfamily, not a new RH theorem.
- **Next action:** prioritize the remaining first-power-rich rows; do not develop more squarefull variants or run a speculative large Codex campaign. A bounded audit is only justified if a proof-critical estimate for that complementary family is found.
- **Preservation:** no historical k=2/k=3 files, Git refs, WSL services, certificates, or prior sealed claims changed. RH remains unproved, complete k=2/k=3 `UNVERIFIED`, historical provenance `BLOCKED_UNWAIVED`.
