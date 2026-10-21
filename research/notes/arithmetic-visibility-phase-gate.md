> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `93c6a360cd7f56c87ff45414497abc4475577577090fcfef7c22f0776ea69259`.

# Project Riemann — All-direction primitive visibility, spectral covariance, and the phase-information gate

**Date:** 2026-10-20  
**Classification:** `EXACT_CLASSICAL_VISIBILITY_CORRELATIONS / HOMOMETRIC_COUNTERMODEL / NO_NEW_RH_FRONTIER_ADVANCE`  
**Scope:** Continuation of `DIMENSIONAL_MOBIUS_TOMOGRAPHY_AUDIT.md`, with no changes to that report or to the Project Riemann October 19 master evidence. This report checks whether going from single-point dimensional counts to simultaneous multi-point correlations creates an independently proved signed restriction relevant to a hypothetical off-critical-line zero.

## 1. Definitions and all-order correlation theorem

For integer `d>=2`, define `V_d(x)=1` if `x` is a **primitive** nonzero integer vector (`gcd(|x_1|,...,|x_d|)=1`), and `0` otherwise. For **fixed** integer displacements `h_1,...,h_m ∈ Z^d`, define the joint density

`eta_d(h_1,...,h_m)=lim_{R->∞}(2R+1)^(-d) sum_{x∈[-R,R]^d} prod_{j=1}^m V_d(x+h_j)`.

**Classical theorem.** The density exists, and

`eta_d(h_1,...,h_m)=prod_{p prime} (1 - nu_p/p^d)`,

where `nu_p` is the number of distinct residue vectors `-h_j mod p` in `(Z/pZ)^d`. If a local factor is zero, the density is zero.

Proof: for each finite set of primes `p≤P`, the Chinese remainder theorem gives exact periodic density `prod_{p≤P}(1-nu_p/p^d)`. The error contributed by primes `p>P` for a fixed number of shifts is at most `O_{d,m,h}(sum_{p>P} p^{-d})` in density (apart from finitely many exceptional zero vectors with vanishing density). For `d>=2` this tends to zero as `P→∞`. The infinite Euler product converges absolutely. This is a special case of established visibility/lattice correlations, **not a priority claim**.

For two shifts `h_1=0,h_2=h`, put `g=gcd(|h_1|,...,|h_d|)`, with `g=0` when `h=0`. Then

`eta_d(h)=prod_{p|g}(1-p^{-d}) prod_{p∤g}(1-2p^{-d})`.

The single-point density is `delta_d=1/zeta(d)`. The independence reference for two points is `delta_d²`.

## 2. Exact positive spectral decomposition and signed local covariance

Put `A_d=prod_p(1-2p^{-d})>0`. For each squarefree positive integer `q` define

`a_d(q)=A_d / prod_{p|q}(p^d-2) >=0`, and put `a_d(q)=0` otherwise. Empty product is 1.

Since `(1-p^{-d})/(1-2p^{-d})=1+1/(p^d-2)`, expanding over squarefree divisors gives

`eta_d(h)=sum_{q squarefree, q|g} a_d(q)`.

A second Euler-factor computation gives `sum_q a_d(q)/q^d=delta_d²`. Thus the **centered** covariance is exactly

`eta_d(h)-delta_d² = sum_{q squarefree} a_d(q)[1_{h∈q Z^d}-q^{-d}]`.

The right-hand series converges absolutely. For each q the bracket is the nonzero-frequency Fourier sum

`1_{h∈qZ^d}-q^{-d}=q^{-d} sum_{r∈(Z/qZ)^d, r≠0} exp(2 pi i r·h/q)`.

Every Fourier weight is nonnegative. Consequently the *centered covariance is positive definite as a function of displacement*, despite taking strictly negative values for some displacements. This is the exact local-to-global diffraction mechanism; visible lattice point diffraction (including pure-point structure) was already proved by Baake, Moody and Pleasants.

For a **primitive displacement** (`g=1`) one has `eta_d(h)=A_d<delta_d²`, since `1-2u < (1-u)^2` for every `u=p^{-d}>0`. Thus the covariance is strictly negative.

For the displacement `h=2e_1` in `d=5`, one has `eta_d(2e_1)>delta_d²`; the inequality is quantitatively certified by the absolutely convergent Euler products (and remains true for sufficiently large d).

As `d→∞` for the displacements `e_1` and `2e_1`, the two covariances have distinct leading rates:

`eta_d(e_1)-delta_d² = -4^{-d}(1+o(1))`,

`eta_d(2e_1)-delta_d² = +2^{-d}(1+o(1))`.

Proof: let `u_p=p^{-d}`. In the nonnegative Euler-factor ratio `delta_d²/A_d=prod_p(1+u_p²/(1-2u_p))`, the term `p=2` dominates with order `4^{-d}`, while all `p>=3` give a total `O(9^{-d})`. Since `A_d→1`, this yields the first rate. The extra factor `1+1/(2^d-2)` for the even displacement yields the second.

This identifies two quantitatively different kinds of long-distance arithmetic organization: negative covariance is order `4^{-d}`, while a shared prime-divisor direction produces positive covariance order `2^{-d}`. **This is an exact dimension law, not an RH zero bound.**

## 3. Exact and numerical checks

`verify_visibility.py` performs exhaustive integer enumeration on the five-dimensional finite torus `(Z/6Z)^5` (7,776 vectors), whose prime factors are 2 and 3:

- Two points offset by `e_1`: `7230 / 7776` jointly allowed, agreeing exactly with `(1-2/2^5)(1-2/3^5)`.
- Two points offset by `2e_1`: `7471 / 7776` jointly allowed, agreeing exactly with `(1-1/2^5)(1-2/3^5)`.
- Three points offset by `{0,e_1,e_2}`: `6960 / 7776` jointly allowed, agreeing exactly with `(1-3/2^5)(1-3/3^5)`.

It independently checks the rational spectral decomposition for primes 2,3,5,7 and three integer displacements. The same exact counts and the homometric calculation were independently reproduced using Wolfram (`{True,1,0,7230,7471,6960}`).

Using high-precision Euler products (primes below 50,000) and `1/zeta(d)` the observed five-dimensional values are:

- Single density `delta_5 = 0.964387340429262459...`.
- Independence reference `delta_5² = 0.930042942380226162...`.
- Primitive-shift joint density `0.929059192959662815...` (negative covariance `-0.0009837494205633473...`).
- Shared-factor-two joint density `0.960027832724984909...` (positive covariance `+0.0299848903447587465...`).
- Three mutually distinct shifts `{0,e_1,e_2}` have joint density approximately `0.89401525205666`.

The decimal values are **numerical approximations**; an elementary tail bound from `sum_{n>=50000} n^{-5} <= 1/[4(49999)^4]` is much smaller than the displayed eight-digit accuracy in the five-dimensional products. Exact integer tests establish the finite models; the Euler-product formulas establish the infinite theorems.

## 4. Adversarial phase-loss test (homometric sets)

Take the finite sets

`A={0,1,4,10,12,17}`, `B={0,1,8,11,13,17}`.

These are distinct and not translates. Their **entire ordered difference multisets** are exactly identical, so they have exactly the same two-point correlation function and Fourier diffraction **intensity**. `verify_visibility.py` checks this by exhaustive integer enumeration. However the triple count

`T_S(h,k)=#{x∈S:x+h∈S and x+k∈S}`

satisfies `T_A(1,4)=1` and `T_B(1,4)=0`. Hence **third-order correlation distinguishes configurations that no collection of pairwise distances can distinguish**.

This is a finite, exact instance of the general phase-retrieval problem in optics: the magnitude-squared Fourier transform loses phase information. Higher-order correlation can retain additional phase combinations (bispectrum).

The tempting move would be to apply a corresponding *signed* Möbius bispectrum, `B_N(alpha,beta)=F_N(alpha) F_N(beta) conjugate(F_N(alpha+beta))` for `F_N(theta)=sum_{n<=N} mu(n)exp(i n theta)`. But `B_N(0,0) = [sum_{n<=N}mu(n)]³`, so demanding the necessary square-root-order bound at `(0,0)` is **RH in disguise** unless derived from a genuinely independent theorem. No such new theorem is established here.

## 5. Third-order visibility itself fails the RH gate

The genuine visible-lattice three-point correlations are already determined by the **local excluded residue counts** `nu_p`, as in §1. No nontrivial bound on the signed summatory Möbius function follows merely from their positivity or from the spectral decomposition in §2.

An explicit control is the `r`-power-free gcd indicator, which forbids simultaneous divisibility of all coordinates by `p^r` instead of `p`. It has the analogous joint-density formula with `p^d` replaced by `p^{rd}` and `p|h` replaced by `p^r|h`. Its one-point density is `1/zeta(rd)`. Thus the local correlation/diffraction principle is not unique to the original Möbius sieve.

This resolves the bounded question: simultaneous observations across many directions retain detailed modular **visibility**, but they do not supply the independently proved cancellation of `mu(n)` needed to exclude an individual hypothetical Xi zero. The gap is not a choice of dimension, frequency scale, or observation order. It is the missing **nonlocal signed arithmetic constraint**.

## 6. Literature and status

- M. Baake, R. V. Moody, P. A. B. Pleasants, *Diffraction from visible lattice points and kth power free integers*, Discrete Mathematics 221 (2000), 3–42. https://arxiv.org/abs/math/9906132 — established diffraction and correlation methods.
- M. Baake, C. Huck, *Ergodic properties of visible lattice points* (2015). https://arxiv.org/abs/1501.01198 — dynamical/spectral context and correlation methods.
- *Visible lattice points along curves*, The Ramanujan Journal (2020), https://link.springer.com/article/10.1007/s11139-020-00302-w — earlier joint-visibility results and attributions.
- T. Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, Forum of Mathematics, Pi (2016), https://arxiv.org/abs/1509.05422 — the difference between local visibility correlations and deep signed multiplicative correlations.

**Verification:** All finite claims checked by self-contained exact Python with no tolerance thresholds; all five-dimensional asymptotic signs follow from Euler products. Exact Wolfram cross-check on the finite torus and homometric pair. The high-precision decimals are diagnostics, not an Arb certificate.

**Lean 4:** Not installed in this environment; no Lean compilation is claimed.

**Codex:** Not launched. This is a negative proof-critical gate, not a reason to run a large campaign.

**Project verdict:** `EXACT_VISIBILITY_SPECTRUM_AND_PHASE_LOSS / NO_NEW_RH_FRONTIER_ADVANCE`. Mathematical originality not established; most of the underlying visibility theory is known. RH remains open. Haglund k=2/k=3 complete verification `UNVERIFIED`, stronger marked moment estimate `BLOCKED_NEW_MOMENT_ESTIMATE`, provenance `BLOCKED_UNWAIVED`. No historical evidence modified.
