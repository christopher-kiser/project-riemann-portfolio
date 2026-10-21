> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `711c99a9e869aef4200e11d20fad333177fa3e61d9db4151fa19c7192c2c1c62`.

# Project Riemann — Prime-index / multiplication spectral gate

**Date:** 2026-10-20. **Verdict:** `PROVED_EXACT_OPERATOR_LEMMAS / FALSIFIED_SPECTRAL_SHORTCUT / NO_NEW_RH_FRONTIER_ADVANCE`.

## Research question

The prime-index tower is a repeated rank/select counting system. Does representing its hierarchy quantum mechanically and combining it with multiplication produce a genuinely new, unconditional positivity constraint on the *actual* Riemann zeta function? The goal was to find a candidate strong enough to exclude one hypothetical off-critical-line zero, rather than another RH-equivalent condition or analogical correspondence.

## 1. Pure prime-index dynamics has no uniquely prime spectrum

Let `H = l²(N_{>=1})`, with orthonormal basis `e_n`. Write `p_n` for the nth usual prime and set `U e_n=e_{p_n}`. The operator U is an isometry (injectivity of n -> p_n), with `U U*` the projection onto the prime-indexed basis coordinates. Its defect subspace `H \ominus U H` is spanned by `e_r` for `r=1` or composite.

**Theorem.** The map `(r,k) -> p^{\circ k}(r)` is a bijection from `{1 and all composite positive integers} x N_0` to `N_{>=1}`. Therefore

`H = direct-sum_{r=1 or composite} closure span{ e_{p^{\circ k}(r)} : k>=0 }`

and U is the unilateral shift on each summand. **Proof:** Starting at any integer `n`, when n is prime replace it with its unique prime index `pi(n)<n`; the strictly decreasing process terminates at 1 or a composite root. Reversing the process gives a unique chain, and distinct chains cannot intersect by injectivity of n -> p_n. QED.

The even-index operator `V_2 e_n=e_{2n}` has the same infinite-multiplicity pure-shift decomposition (roots are odd integers). Consequently **U and V_2 are unitarily equivalent**, despite having completely different underlying arithmetic. Both have spectrum the *closed unit disk*, and self-adjoint symmetrizations `U+U*` and `V_2+V_2*` have the same spectrum `[-2,2]`. The latter statements are immediate from the classical unilateral-shift spectral theorem / Wold decomposition.

**Meaning:** No spectrum of U alone, or any operator obtained from it by unitary-invariant functional calculus, can be a prime-specific RH constraint. This is a no-go for a pure prime-index quantum Hamiltonian.

## 2. The exact survival/dead-end filtration

Set `P_k=U^k(U*)^k` for k>=0. Then `P_k` is the orthogonal projection onto the kth prime-index survivor set. `P_{k+1} <= P_k`, all ranks are infinite, and `P_k -> 0` **strongly**, not in operator norm. The differences `P_k-P_{k+1}` project onto survivors at depth k that fail the next filter. **Proof:** Every integer has finite backward prime-index ancestry, hence each finite-support vector is killed by P_k for sufficiently large k; conclude strong convergence by density and `||P_k||<=1`. There are infinitely many survivors at every fixed k because prime-index iteration is injective.

The same phenomenon occurs for repeatedly doubling. It explains the order-of-limits 'every individual eventually dies, but every level has infinitely many survivors'; it is not uniquely prime arithmetic.

## 3. Coupling rank/select to multiplication: an exact noncommutativity law

For m>=2 let `V_m e_n=e_{mn}`, another isometry. For all integers m>=2, k>=1, and all x,y in H:

`<U^k V_m x, V_m U^k y> = 0`

because all outputs of the left operator are supported on primes while all outputs of the right operator are supported on composites. Each operator is an isometry, so

`[U^k,V_m]*[U^k,V_m]=2 I`, with `[U^k,V_m]=U^k V_m - V_m U^k`.

Thus `||[U^k,V_m]||=sqrt(2)` at **every** depth, and the two operational orders generate orthogonal output states. This is an elementary all-depth exact identity using actual prime atomicity. It is **not** evidence of physical wavefunction collapse.

**Adversarial control (decisive).** Let `a_n` be the nth *semiprime* (integers with Ω(n)=2, prime factors counted with multiplicity), and define `W e_n=e_{a_n}`. Multiplication by m>=2 increases Ω and therefore makes `m a_n` non-semiprime. Consequently the identical identity `[W^k,V_m]*[W^k,V_m]=2I` holds for every m>=2,k>=1. More generally any fixed-almost-prime class Ω(n)=r has this property. Thus this mathematically exact law is shared by counting systems with completely different zeta-like Dirichlet series. It cannot independently force RH.

## 4. Adding logarithmic energy: arithmetic reappears, but only in the convergence region

Define the self-adjoint unbounded diagonal operator `D e_n=(log n) e_n` on its natural dense domain. On finitely supported vectors:

`U* D U - D = diag(log(p_n/n)) > 0`,

whereas `V_m* D V_m - D=(log m) I`.

Using `p_n ~ n log n` (prime number theorem) gives

`log(p_n/n) ~ log log n`.

Thus the prime-index energy defect is unbounded, unlike doubling's constant energy increment. This is an unconditional prime-specific asymptotic, but arises from the known prime number theorem.

For `Re(s)>1`, `e^{-sD}` is trace-class and

`Tr(e^{-sD}) = zeta(s)`, `Tr(U* e^{-sD} U) = sum_p p^{-s} = P(s)`.

The Euler product gives `log zeta(s) = sum_{r>=1} P(rs)/r` in this half-plane. All these identities are exact with their convergence hypotheses. They recover the familiar arithmetic quantum trace / prime-zeta relations; they are not a novel analytic continuation or a zero-free-region theorem. Positive Hilbert traces for real s>1 cannot simply be transported into `0<Re(s)<1`, where the defining trace diverges and continuation is a different operation.

For a fixed m>=2, the prime number theorem also gives `p_{mn}/(m p_n) -> 1`, even though `e_{p_{mn}}` and `e_{m p_n}` are orthogonal for every n. This is a precise version of 'nearly identical energies but completely different basis states', not a claim that physical observation modifies arithmetic.

## 4.5. The attempted Hasse-style geometric form is tautological here

An obvious attempt to imitate the elliptic-curve degree argument is to build, for a unit vector `x` and integers `a,b`, the form

`Q_x(a,b)=||a x - b U x||² = a² - 2ab Re<x,Ux> + b² >= 0`.

Its discriminant bound merely yields `|Re<x,Ux>| <= 1`, which is true of **every** isometry by Cauchy–Schwarz, including simple doubling and the semiprime countermodel. There is no identified coefficient in Q equal to any Xi zero parameter. Thus the most immediate 'positive degree' analogue is falsified as a route to an arithmetic zero constraint: it is automatic Hilbert-space positivity, not the independent algebro-geometric degree positivity of the finite-field Hasse proof.

## 5. What the comparison proves — and does not prove

- `PROVED`: Prime-index operator is a pure isometry of countably infinite shift multiplicity, unitarily equivalent to simple even-index doubling. Projectors strongly tend to zero but are all infinite rank.
- `PROVED`: Exact all-scale multiplicative orthogonality and energy-shift formulas; trace identities in Re(s)>1.
- `FALSIFIED`: Prime-index spectral data alone distinguishes primes; positive commutator/orthogonality alone singles out the ordinary primes or confines zeta zeros.
- `NOT PROVED`: Any new independent positive quadratic form or trace inequality whose validity forces exclusion of even one hypothetical Xi zero.
- `NO RH ADVANCE`: All zero-location information still requires an independent analytic bridge across the line of Euler-product convergence. One should not merely assume the needed positivity or translate a known RH equivalent.

**Stop condition:** This particular cross-scale Hilbert-space approach does not warrant a Codex campaign until a concrete mixed trace/correlation inequality (in U, the V_m, and D) is independently justified in a domain where genuine Xi zeros matter, and until the inequality distinguishes the semiprime control system rather than holding by mere divisibility.

## Sources / literature distinction

- Classical Wold decomposition for isometries: https://link.springer.com/article/10.1007/s40590-023-00558-4
- NIST DLMF prime number theorem and nth-prime asymptotic: https://dlmf.nist.gov/27.2
- Bost & Connes (1995), genuine arithmetic quantum statistical mechanics / zeta partition function: https://doi.org/10.1007/BF01589495
- Prime-zeta identity: https://mathworld.wolfram.com/PrimeZetaFunction.html
- Finite-field positive geometric-degree proof blueprint (for the contrast with positivity simply asserted): https://cbirkbeck.github.io/AINTLIB-blueprints/hasseweil/

None of the established Wold, prime zeta, or Bost–Connes mathematics is claimed to originate with this audit; literature priority for the particular elementary combined-operator identities has not been established.

## Verification and preservation

`verify_index_multiplication.py` uses exact integer arithmetic and `sympy` to test 17,389 prime chains, 960 two-path disjointness cases, 20 semiprime control cases, and survivor counts through 100,000, along with non-proving floating-point energy-drift diagnostics. The stated all-scale results have written proofs independent of these finite tests. Original handoff files and evidence were untouched. Lean 4 unavailable on PATH; no Lean theorem was compiled. Codex was not launched.

**Project statuses:** RH unproved; full Haglund k=2/k=3 `UNVERIFIED`; marked inverse moment `BLOCKED_NEW_MOMENT_ESTIMATE`; historical provenance `BLOCKED_UNWAIVED`.
