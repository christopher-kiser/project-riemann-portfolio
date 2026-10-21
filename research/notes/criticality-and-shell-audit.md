> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `92ad3b05a5a248d2c3d95e930a28f8a0528626a2c54317474834ab0146598da5`.

# Project Riemann — Prime-index criticality staircase and discarded-shell test

**Date:** 2026-10-20.  **Verdict:** `CLASSICAL_MULTISCALE_CRITICALITY / SHELL_TRANSFER_NO_GO / NO_NEW_RH_FRONTIER_ADVANCE`.

## Scope and provenance

This bounded follow-up tests the interaction of the previous prime-index isometry `U`, energy `D e_n = (log n)e_n`, nested survivor sets and Euler products. It is **not** a new zero-free theorem. The comparison with physical phase transitions is mathematical analogy, not a claim about measurement causing primes to change. The original uploaded Project Riemann handoff and all previous artifact files are read-only; this directory is additive.

Literature used: fixed-depth prime-indexed counting asymptotics (already studied), PNT `p_n ~ n log n` (DLMF), and standard regularized Fredholm determinants (Britz–Carey–Gesztesy–Nichols–Sukochev–Zanin). Links at end. Novelty of the derived staircase as a named result **has not been established**.

## Exact objects

For `p_n` the nth ordinary prime, set `S_0(n)=n`, `S_1(n)=p_n`, and `S_{k+1}(n)=p_{S_k(n)}` for fixed integers `k>=1`.  Let `P_k={S_k(n):n>=1}`; `P_{k+1} ⊂ P_k`. For `Re(s)>1`, define

`Z_k(s) = Product_{n>=1} (1-S_k(n)^(-s))^(-1)`.

In particular `Z_1(s)=zeta(s)` **only in this initial product domain**; for `k>=2` the products define different arithmetic functions and have no supplied zeta functional equation.

## Theorem A — fixed-depth criticality staircase (proved with PNT)

For every fixed `k>=1`,

`S_k(n) ~ n (log n)^k` as `n→∞`.

Indeed induction with `p_n ~ n log n` shows `p_{S_k(n)} ~ S_k(n) log S_k(n) ~ n (log n)^(k+1)`. The asymptotic is **not uniform** for jointly increasing k and n.

For `k>=2`, `F_k(s)=log Z_k(s)` has finite one-sided derivatives at real `s=1` of all orders `0<=j<=k-2`. In contrast, with `δ>0`,

`(-1)^(k-1) F_k^(k-1)(1+δ) ~ log(1/δ)` as `δ↓0`.

For `k=1` the same formula means `log zeta(1+δ) ~ log(1/δ)`.

**Proof:** On real `s>1`, expand absolutely

`F_k(s) = Sum_{n>=1} Sum_{r>=1} S_k(n)^(-r s)/r`.

For fixed j, the r=1 portion of the jth derivative at `s=1` is

`(-1)^j Sum_n (log S_k(n))^j / S_k(n)`.

By the nth-survivor asymptotic its terms are asymptotic to `1/[n(log n)^(k-j)]`. The integral test gives convergence precisely when `j<k-1`. All r>=2 contributions and their fixed-order derivatives are absolutely and locally uniformly summable at `s>=1` because `P_k⊂{2,3,...}` and `Sum_{n>=2}(log n)^j/n^2<∞`.

For j=k-1 and δ>0, the r=1 contribution is

`Sum_n [((log S_k(n))^(k-1))/S_k(n)] S_k(n)^(-δ)`.

The bracket is asymptotic to `1/(n log n)`. For any fixed ε>0, eventually `n<=S_k(n)<=n^(1+ε)`. Hence, up to factors `1±ε` and finitely many initial terms, the sum lies between `Sum n^(-1-(1+ε)δ)/log n` and `Sum n^(-1-δ)/log n`. Both are asymptotic to `log(1/δ)` as δ↓0 by the substitution u=log x (or the exponential integral). Squeeze and then ε→0; the r>=2 contribution remains bounded. QED.

**Interpretation:** Each additional indexing depth makes one more *low-order* derivative finite, but leaves a logarithmic divergence at the next derivative. This is analogous to changing the order of a thermodynamic singularity. It is not proof of an actual quantum phase transition.

**Adversarial control:** Every eventually strictly increasing sequence `a_k(n)~n(log n)^k` produces the same theorem for its corresponding Euler-type product, even if many `a_k(n)` are composite (e.g. the eventual sequence `floor((n+2)(log(n+2))^k)`). This is a **growth/density** theorem, not a prime-unique zero constraint.

## Theorem B — exact Euler-product shell decomposition (proved)

Define `D_k=P_k\P_{k+1}` and `W_k(s)=Product_{p∈D_k}(1-p^(-s))^(-1)` for Re(s)>1.

Every ordinary prime belongs to exactly one D_k: repeatedly take the prime index, which is strictly smaller, until hitting 1 or a composite. Equivalently, the prime-index isometry is a pure shift, as already established in the previous audit. Thus for Re(s)>1,

`zeta(s)=Product_{k>=1} W_k(s)`, and `Z_k(s)=W_k(s) Z_{k+1}(s)`.

The products are absolutely convergent; at each fixed s in that half-plane `Z_k(s)→1` as k→∞, by dominated convergence on nested subsets of primes.

A sharper endpoint conclusion follows:

* `Sum_{p∈P_1}1/p=∞` (classical Euler divergence).
* `Sum_{p∈P_2}1/p<∞`, from `S_2(n)~n(log n)^2`.
* Therefore `Sum_{p∈D_1}1/p=∞`; all later `D_k⊂P_2` for k>=2 have convergent reciprocal sums.
* Consequently `Z_2(1)` is finite and positive, `W_k(1)` is finite and positive for k>=2, but the **first discarded shell** carries zeta's entire leading pole: `W_1(1+δ) ~ 1/[δ Z_2(1)]` as δ↓0.

All statements at `s=1` refer to one-sided limits of positive real products, **not** holomorphic continuation across `s=1`.

**Meaning:** Deeper prime selection does not preserve the original zeta singularity. Any reconstruction of the genuine Xi from the shells has to retain the arithmetic in the discarded layers. Knowing the deep survivor hierarchy alone does not yield a new zero-exclusion theorem.

## Theorem C — Hilbert/Schatten criticality of nested prime energy (proved)

On `l²(N>=1)` let `D e_n=(log n)e_n` and `U e_n=e_{p_n}` as in the previous audit. For `Re(s)=σ>0` define the bounded diagonal operator

`T_{s,k}=U*^k exp(-sD) U^k = diag(S_k(n)^(-s))`.

For any finite real `q>=1` (Schatten exponent),

`||T_{s,k}||_{S_q}^q = Sum_{n>=1} S_k(n)^(-qσ)`.

Therefore it is in `S_q` if and only if `qσ>1`, or if `qσ=1` **and** `k>=2`. For `qσ<1` it is never in `S_q` for fixed depth k. In particular:

* All k>=1 are Hilbert–Schmidt for σ>1/2.
* Only k>=2 are Hilbert–Schmidt on σ=1/2 (including all imaginary heights there).
* Only k>=2 are trace-class at σ=1; k=1 fails due to Euler divergence.

This again follows by comparison to `Sum 1/[n^(qσ)(log n)^(k qσ)]`.

Since `||T_{s,k}||=S_k(1)^(-σ)<1` for σ>0, every Schatten-regularized Fredholm determinant `det_r(I-T_{s,k})` (where defined, r an integer >=1) is **nonzero**. For k>=2 the determinant `det_2(I-T_{s,k})` is defined and nonzero even on the critical line `Re(s)=1/2`; at the boundary this gives a pointwise, continuous-in-height value rather than asserted analytic continuation into the left half-plane.

The k=1 formula is explicit on σ>1/2:

`det_2(I-T_{s,1}) = Product_p (1-p^(-s)) exp(p^(-s))`

`= exp(-Sum_{r>=2} (1/r) Sum_p p^(-rs))`.

It is nowhere zero for σ>1/2 and has a uniform modulus lower bound on each vertical line σ>1/2,

`|det_2(I-T_{s,1})| >= exp(-(zeta(2σ)-1)/(2(1-2^(-σ)))) > 0`.

Derivation: use `|log(1-z)+z| <= |z|²/[2(1-|z|)]` for |z|<1 and bound `Sum_p p^(-2σ) <= zeta(2σ)-1`. Consequently for σ>1,

`zeta(s)=exp(P(s)) / det_2(I-T_{s,1})`, `P(s)=Sum_p p^(-s)`.

The determinant extends canonically into σ>1/2, while **the first-order prime trace** P(s) does not admit an automatic holomorphic continuation there: such a continuation at a hypothetical zeta zero would require removing exactly its logarithmic zero singularity. Locally, any off-critical-line zeta zero is carried by the complementary factor `zeta(s) det_2(I-T_{s,1})`, not by the nonvanishing det_2. This is the specific no-go for extracting RH from automatic Hilbert–Schmidt positivity.

**Control:** The Schatten convergence classification depends only on fixed-depth growth `n(log n)^k`, not the primality of terms. The determinant nonvanishing follows from `||T||<1` and is likewise automatic for comparison sequences with analogous growth.

## Falsification and go/no-go decision

The analogies to physics produce mathematically real phenomena: a hierarchy of critical derivative orders, divergent versus convergent cumulative reciprocal weights, and a shift from divergent ordinary traces to finite Hilbert–Schmidt regularized determinants.

**They do not exclude any off-critical-line zero.** The functional equation, the actual signed explicit formula, and the needed arithmetic prime-phase constraints are absent from `Z_k` at k>=2. The deepest shells lose the main pole rather than imposing a protective geometric law. The regularized determinants exist because low-order divergent cumulants have been removed; their zero-freeness is automatic and does not transfer to ζ.

**Stop:** Do not launch Codex for higher k/another regularized determinant unless an independently derivable signed cross-shell correlation, not forced by monotone growth or square summability, is supplied. This work is a rigorous classification/no-go, not a proof-critical RH advance.

Historical statuses: RH open; Haglund k=2/k=3 complete verification UNVERIFIED; marked inverse-moment BLOCKED_NEW_MOMENT_ESTIMATE; historical provenance BLOCKED_UNWAIVED.

## Finite cross-checks and evidence

The companion script `verify_staircase.py` consumes the *previously preserved* `FROZEN_INPUT_NESTED_GAPS_1000.csv` **read-only**. It verifies 104 direct prime-index iterations against SymPy, exact survivor nesting across a shared cutoff (7919), three exact-rational finite Euler-product shell identities, two complex finite-determinant expansions, and finite partial-sum diagnostics. These do not prove any infinite statement; the arguments above do.

Numerical sampled shell counts ≤7919: P1=1000, P2=168, P3=39, P4=12; discarded D1=832, D2=129, D3=27. They are cutoff-specific, not global density claims.

### References

- DLMF, `p_n∼n log n`: https://dlmf.nist.gov/27.12 .
- New bounds and computations on prime-indexed primes (2013), source for prior level-counting asymptotics: https://www.researchgate.net/publication/255711160_New_bounds_and_computations_on_prime-indexed_primes .
- Britz, Carey, Gesztesy, Nichols, Sukochev, Zanin (2020/21), **The product formula for regularized Fredholm determinants**, https://arxiv.org/abs/2007.12834 .
- Wolfram MathWorld, prime zeta and standard `log ζ=∑_r P(rs)/r`: https://mathworld.wolfram.com/PrimeZetaFunction.html .
- Connes–Consani–Marcolli (2009/10), geometric positivity as separate RH-equivalent approach: https://authors.library.caltech.edu/records/xf64a-qg632 .
