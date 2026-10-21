> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `ba353772f99ae1f56e8961f8822c89e8255ef40302d309b04d8bbd87bb2d12bc`.

# Project Riemann — Exact quantum-Gibbs / Lee–Yang stability gate

**Checkpoint:** 2026-10-19. **Verdict:** `NO_NEW_RH_FRONTIER_ADVANCE`. Written classical-input proof plus exact independently recomputed finite Walsh coefficient; **not Lean checked**; **not claimed novel in the literature**.

## Scope and historical preservation

This is a separate follow-up to the original 2026-10-19 `Project_Riemann_Complete_Handoff_20261019(1).zip`, `Project_Riemann_Gibbs_PF_Audit_20261019.zip`, and `Project_Riemann_Exact_ID_Obstruction_20261019.zip`. None of the originals was modified. The recent exact non-infinite-divisibility result about the full Xi theta law is **not** assumed in this audit. RH remains unproved, complete Haglund k=2/k=3 `UNVERIFIED`, the marked inverse moment `BLOCKED_NEW_MOMENT_ESTIMATE`, historical provenance `BLOCKED_UNWAIVED`.

## Primary research source and candidate

S. Wei, Y. Zhai, Q. Lu et al., **The Riemann Hypothesis manifested in dynamical quantum phase transitions**, *Nature Communications* **17**, 8163 (published 1 July 2026), https://www.nature.com/articles/s41467-026-74935-8 . The article's exact finite model has an energy level `E_n=log(n)` for `1 <= n <= N=2^q`, with a binary/Walsh expansion (Eqs. 2, 7–8) and the finite normalized alternating observable (Eqs. 9–10):

`L_N(beta,t) = (sum_{n=1}^N (-1)^(n+1) n^(-beta-it))/(sum_{n=1}^N n^(-beta))`.

The paper's Eqs. 38–42 **already analyze** the pointwise finite-size exponents and link their discontinuities to eta/zeta zeros. This audit does not assert that those displayed calculations are absent or that the physics experiments are invalid. We test one stronger missing inference: *does ordinary quantum/ferromagnetic thermal positivity independently forbid any zero with 1/2 < beta < 1?*

## Theorem A: exact 3-spin obstruction in the paper's binary basis

For the paper's assignment of level `n` to the binary digits of `n-1`, let `z_j(n)=(-1)^(bit_j(n-1))`, j=1,2,3, and expand

`H_0 = sum_{I subseteq {1,2,3}} J_I product_{j in I} sigma_j^z`, with `J_I = (1/8) sum_{n=1}^8 log(n) product_{j in I} z_j(n)`.

The degree-three coefficient is **exactly**

`J_{123} = log[(1*4*6*7)/(2*3*5*8)]/8 = log(7/10)/8 < 0`.

Proof: the Walsh signs for n=1,...,8 are `(+, -, -, +, -, +, +, -)`; orthogonality of the eight Boolean characters makes this coefficient unique. Hence the exact **specified** 3-spin Hamiltonian cannot be expressed using only 0-, 1- and 2-body Ising couplings in that basis. The ordinary pairwise ferromagnetic Lee–Yang circle theorem has hypotheses that this encoding does not meet. This does not disprove more general Lee–Yang results, alternative nonbinary encodings, or an unrelated spectral method.

Independent exact cross-check: standard-library `fractions.Fraction` and Wolfram Language `FullSimplify` both returned 7/10, with `J_{123}=-(1/8) Log[10/7]`. No floating point is used for the proof.

Primary circle-theorem source: T. D. Lee and C. N. Yang, *Statistical Theory of Equations of State and Phase Transitions. II. Lattice Gas and Ising Model*, *Phys. Rev.* **87** (1952), 410, https://doi.org/10.1103/PhysRev.87.410 . The theorem has stated ferromagnetic interaction assumptions; it does not automatically apply to arbitrary many-body Hamiltonians or signed dynamical observables.

## Theorem B: escape of the actual thermal Gibbs law and its universal centered limit

For fixed `0 < beta < 1` and `N >= 1`, define the probability law on integers `1 <= n <= N` by

`P_beta,N(n) = n^(-beta) / H_N(beta)`, `H_N(beta) = sum_{n=1}^N n^(-beta)`.

1. Since `H_N(beta) ~ N^(1-beta)/(1-beta)`, the mass of every bounded interval of the original energy `E=log n` tends to zero as `N -> infinity`. There is no weak probability limit on the unshifted real energy axis: the Gibbs mass escapes to infinity.
2. Let `X_N = log(N/n)` when n is sampled from this law. For every fixed x>=0,

`P(X_N >= x) = H_floor(N exp(-x))(beta)/H_N(beta) -> exp(-(1-beta)x)`.

Therefore `X_N` converges in distribution to an exponential law with rate `1-beta`. Its characteristic function is `(1-beta)/(1-beta-it)` (for the convention E exp(it X)). It is zero-free for real t, contains no information about Riemann zeros, and is a universal leading thermodynamic profile, not a noncircular zero-exclusion theorem.

The paper's finite quantum state is legitimate at each N. We do **not** claim that the authors falsely asserted a normalizable uncentered infinite Gibbs probability law. Their relevant signal is finite-size scaling of a signed observable, not a pointwise normalized-amplitude limit with isolated zeros.

## Theorem C: arithmetic appears only in the signed subleading scaling

Let `s=beta+it`, `0<beta<1`, t fixed. Write `A_N(s)=sum_{n=1}^N (-1)^(n+1) n^(-s)` and `eta(s)=(1-2^(1-s))zeta(s)` (analytic Dirichlet eta function). Then as N->infinity,

`A_N(s) = eta(s) + (-1)^(N+1) N^(-s)/2 + O_s(N^(-beta-1))`.

Proof: the alternating tail equals `(-1)^N` times `sum_{k>=0} (-1)^k (N+1+k)^(-s)`. By the gamma integral or Euler's transformation this equals `(-1)^N[(N+1)^(-s)/2 + O_s(N^(-beta-1))]`. Moreover `H_N(beta) = N^(1-beta)/(1-beta) + O_beta(1)`.

Consequently, for every fixed `0<beta<1` and real t:

* `L_N(beta,t)->0` **for all** t, regardless of whether zeta(s)=0.
* If `zeta(s) != 0` (equivalently `eta(s) != 0` within the strip), then `L_N(beta,t) ~ (1-beta)eta(s) N^(beta-1)`.
* If `zeta(s) = 0`, then `L_N(beta,t) = (-1)^(N+1)(1-beta)N^(-1-it)/2 * (1+o(1))`.
* Hence the asymptotic finite-size exponent `-log|L_N|/log N` equals `1-beta` off the zeta zero set and equals `1` at a zero (for the natural-log convention). The published paper presents this same distinction using its chosen normalization by spin count.

A Lee–Yang theorem, self-adjointness, or Gibbs positivity would exclude an off-line zero **only if** it independently prohibited the exponent-1 anomaly when `beta!=1/2`. No such exclusion is supplied by these ingredients: the anomaly is **equivalent** to the fact being tested (`eta(s)=0`), while the leading thermal law loses the arithmetic phase. This is a precise dependency failure, not an objection to the finite-size asymptotic representation.

## Adversarial stop decision

The paper's spectral construction is an exact arithmetic encoding, but it is not a new mechanism proving RH. The standard pairwise Lee–Yang hypotheses fail already at 3 spins in its specified encoding; the uncentered positive Gibbs laws lack a limiting probability distribution for `0<beta<1`; the properly centered leading distribution is universal, whereas the zero-sensitive signal comes from the signed subleading eta term. No contradiction is obtained from a hypothetical zero with `1/2 < beta < 1`. We do not claim literature priority, discovery of an error in the paper's Methods, or any new zero-free region.

**Verdict:** `NO_NEW_RH_FRONTIER_ADVANCE`. **Codex gate:** NO GO: no independent theorem/inequality beyond the known RH-equivalent anomalous-scaling condition. Lean 4 is unavailable in this container; no Lean verification is asserted. Use of Wolfram and exact Python checks establishes only Theorem A's algebra; Theorems B–C use the explicit classical arguments above.

**Practical research direction if a genuinely new idea appears:** a positive/phase-sensitive *independent* constraint on the signed correction term that is not already the same as `eta(s)!=0`; otherwise do not repeat a thermal-model or operator-positivity campaign.
