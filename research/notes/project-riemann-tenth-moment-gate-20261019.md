> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `4d24112e0fcd1d43f74b6b6ed861738577991c74e8957fe92ec6c68dbdd40c6e`.

# Project Riemann — a bounded tenth-moment gate (19 October 2026)

**Status: CONDITIONAL ANALYTIC CANDIDATE, NOT PROVED. No RH frontier advance.** No Codex run, Lean build, external submission, project checkout modification, or historical evidence mutation is claimed. RH remains open, complete historical k=2/k=3 verification is UNVERIFIED, and historical provenance remains BLOCKED_UNWAIVED.

## 1. Primary verified source and exact setup

Xu–Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*, arXiv:2610.15291v2 (15 October 2026), §§2, 4–7, especially equations (20), (21), (25), (28)–(29): https://arxiv.org/html/2610.15291v2. Their result is conditional on the original 7/8 analytic inputs. de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1, Theorem 1.1: https://arxiv.org/html/2610.04045.

Take the fixed rational parameters

- b = 1/100, ell = 21/125, kappa = 29991/40000;
- h = (1+b+3 ell)/2 = 757/1000; l_y = (1+b-ell)/2 = 421/1000;
- c = 1/(3 kappa) = 40000/89973; C_0 = -1/4 + b/6 + 5 ell/4 = -23/600;
- zero-free boundary B(ell) = 11/12 - ell/4 = 328/375 = 0.8746666666... .

The first-stage 69991/80000 bound licenses kappa = 29991/40000; it is NOT to be assumed without the stated published external inputs.

For delta in [1/8,5/6] and x in [0,1/2], define the *published* functions

D(x) = 3-(1+2c)x,
P(x) = (2-2cx)(1-x),
J(delta,x) = (5/6-delta)D(x) + delta P(x),
R(delta,x) = 1-delta + ((5/6-delta)delta P(x))/(2J(delta,x)),
E_old(delta,x) = C_0 + delta/2 + delta*x*(ell+c*(h/4-l_y/2)) - (3h/4)*(1-R(delta,x)).

J>0 throughout this rectangle, according to the published theorem and directly from D,P>0. The physical amplitude variable x = q/delta where q = (sum ell_i g_i)/ell and the selected positive slots have product magnitude at least U^((ell/d)q-o(1)) at row scale U=Z^d. This selection is fixed within each amplitude bin; only the selected slots with g_i>0 are multiplied. Smooth weights, masks, finite ray twists, allowed height uniformity, and sixth-power-free rows are essential.

## 2. A precise new, UNPROVED moment hypothesis

Call H10 the uniform bound

    sum_{physical 6th-power-free nonunit rows N(u) ~ U}
      |prod_{i in I} Q_i(u;z)|^10
    <= C_epsilon * U^(1 + 1/25 + epsilon) * (1+H)^A

for every *fixed allowed slot system*, every fixed selected subset I of positive-amplitude physical slots of total length at most ell (measured in base Z), all admissible smooth masks/fixed twists/row heights, and the dyadic row scales d in [h-1/50, h+zeta] for some sufficiently small fixed positive zeta. Uniformity must be exactly strong enough for the source's finite bin subdivision, fixed slot mesh and subsequent contour integrations. We neither assert H10 nor assume it follows from the existing fourth-moment result. The rows may include lower-order characters induced by nonunit sixth-power-free moduli; any proof must handle them rather than silently restrict to primitive exact order six. **Nonunit exclusion is essential:** a principal unit row such as u=1 has no character cancellation and its prime products would violate this moment budget at the indicated scales. The source treats principal/unit rows separately.

Markov's inequality and the physical amplitude lower bound, if H10 holds, give

    #B <= U^(R10(d,delta,x)+epsilon) (1+H)^A,
    R10(d,delta,x) = 1 + 1/25 - 10*(ell/d)*delta*x.

Combine with the existing row-count bound by taking min(R, R10). Using only one of these estimates is not enough.

## 3. Exact algebraic gates already checked

At d=h, put

    E10(delta,x) = C_0 + delta/2 + delta*x*(ell+c*(h/4-l_y/2))
                   - (3h/4)*(1-(1+1/25-10*(ell/h)*delta*x)).

Wolfram exact real-closed-field quantifier elimination returned FALSE for

    EXISTS delta,x:
      1/8 <= delta <= 5/6 AND 0 <= x <= 1/2
      AND E_old(delta,x) >= -1/1000
      AND E10(delta,x) >= -1/1000.

Therefore **conditionally on correct transcription of source equations**, min(E_old,E10) < -1/1000 over the whole closed rectangle. An independent **exact rational Bernstein-polynomial subdivision** also certifies the same strict inequality: the polynomial sign test terminates after 27 tree nodes, producing 14 closed subboxes (11 certified by the old exponent, 3 by the new exponent), with maximum depth 7. The accompanying `check_tenth_moment_gate.py` is the self-contained certificate generator. Both checks concern rational endpoint algebra only, NOT the analytic H10 estimate or Lean formalization.

An eighth-moment hypothesis is insufficient. At delta=13/24,x=1/2, the source exponent remains exactly

    min(E_old,E8) = 338432663531 / 162721125936000 > 0,
    R8 = 1 - 8*(ell/h)*delta*x.

The obstruction is not just at the earlier delta=9/20 witness.

Additional exact scalar conditions of source equations (11), (29) were checked with Python fractions: b>0, 1/6<ell<1/5, B(ell)>87/100, l_x>ell, l_y-ell>11b/6, 6 kappa ell>3/4, ell/h<1/(6 kappa), ell/h>21/100, h/2<l_y<1/2, and all three small-row inequalities. These checks do not prove the new analytic moment bound.

For d <= h-1/50, the *original* estimate already suffices: exact quantifier elimination gave E_old(h;delta,x) <= 1/400, and E_old(h)>=0 implies R>=2/5. The source affine exponent has slope (3R+1)/4 + q/(12 kappa) - 17/50, hence >=21/100 when R>=2/5, so after reducing d by 1/50 the exponent is at most 1/400 - (21/100)(1/50) < 0. When E_old(h)<0, the positive slope also handles d<h. Thus the new H10 input is needed only in the narrow critical row-scale window. The moment-improved exponent in that window is affine increasing with d because d*R10(d)=d*(1+1/25)-10 ell q. A small enough zeta retains its negative endpoint margin at h+zeta.

Conditional consequence, pending detailed independent source-integration audit: H10 in the exact coefficient and uniformity class, together with the previously stated imported analytic inputs and the published high-side machinery, supplies the currently missing intermediate-row bound for the rational parameters above. The other published small-row and principal-row arguments then *should* yield a zero-free boundary B=328/375. This is not an unconditional theorem, and a full integration audit is still needed.

## 4. Why H10 is not already proved

The total physical prime length is at most Z^ell = U^(ell/d). Raising the product to its fifth power generates a character-polynomial column length up to U^(5 ell/d), which is U^(840/757) ~= U^1.1096 at d=h and as large as U^(840/737) ~= U^1.1398 at d=h-1/50. The general sextic large-sieve upper bound of de Faveri gives (for generic coefficients) terms U^(5/6)B^(1/3) and U^(1/3)B^(5/6), as large as about U^1.258 at d=h (or ~U^1.283 near the lower window edge), versus the desired special-coefficient U^1.04. H10 therefore requires a major coefficient-structured saving; the generic sieve does not establish it.

One suggestive algebraic feature: a fifth power of products of disjoint prime-slot sums has each source prime exponent <=5, so there is no *forced* nontrivial sixth-power ratio between two monomials from that fifth power unless their valuations coincide. This observation is elementary, does NOT prove an average bound, and may be disrupted by lower-order induced characters and Gauss-sum biases. It must not be portrayed as a theorem proving H10.

Direct multiplication of the inverse and plain witness polynomials is NOT a shortcut: they are annular sums, so the full Dirichlet convolution mu*1=delta_1 does not hold coefficientwise for their product. The selected long witness lengths r~0.738 and m~0.416 have product length U^1.154. The existing independent witness moment exponents meet exactly at R=74812109/122854370 at delta=9/20,x=1/2. Any stronger bound must use new joint arithmetic information.

## 5. Bounded falsification gate / research priority

Before allocating a full Codex proof campaign, test a single question: Is H10 even compatible with the physical sextic character family, including all sixth-power-free row types, exceptional Gauss-sum biases, the prime-slot masks, and fixed ray twists? Search for a *rigorous power-size lower bound* contradicting U^(1+1/25+epsilon), not just a generic operator-norm lower bound that may concern other coefficient vectors. Otherwise seek one honest analytic lemma for these highly structured fifth-power coefficient vectors that improves on de Faveri by the required exponent. If neither a counterexample nor a source-supported proof route exists, STOP the tenth-moment branch. Do not launch massive numerics or make a second speculative conjecture.

## 6. Evidence / preservation limits

No Lean was compiled here: the isolated runtime has no `lean`/`lake`. The exact rational endpoint checks and Wolfram quantifier-elimination outputs do NOT prove the analytic H10 premise. This note does not alter original manuscripts, historical numerical evidence, Git heads/refs or services. RH is unproved; Haglund full k=2/k=3 remains unverified; historical provenance remains BLOCKED_UNWAIVED.
