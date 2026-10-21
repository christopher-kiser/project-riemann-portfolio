> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `d9e9ce89d4c405ee490d2dee68c206185b410204e528b04bca47a68d86adf16f`.

# Project Riemann — Dual-count renormalization of nested prime gaps

**Date:** 2026-10-20. **Status:** `EXACT_MULTISCALE_DUALITY_AND_GROWTH_WITH_CLASSICAL_INPUTS / NO_NEW_RH_FRONTIER_ADVANCE`.

This is a **newly derived project note**, not a claim of priority in the literature. Original October 19–20 research archives and Git evidence are not edited. The aim is to test the user's suggestion that prime-valued patterns reappear when numerical gaps are viewed from other layers or resolutions, and that their scales compound too rapidly for small windows to reveal them. We specifically test whether this gives an **independent, signed constraint** on the actual prime counting error, rather than another rearrangement of prime indexing.

## Definitions

Write `p(n)` for the nth prime, let `S_0(n)=n` and, for `k>=1`, `S_k(n)=p(S_(k-1)(n))`. Define `D_k(n)=S_k(n+1)-S_k(n)` and `q_k(n)=D_k(n)-1`, including `D_0(n)=1`, `q_0(n)=0`. Every `S_k` is strictly increasing and `S_k=S_j∘S_(k-j)` for `0<=j<=k`. The sequences are the familiar higher-order prime-indexed primes; observed quasi-self-similar finite differences were described by Batchko (2014, arXiv:1405.2900).

## Theorem 1 — Exact change-of-viewpoint identity (unconditional, elementary)

**Statement.** For every `k>=1`, `n>=1`, and `0<=j<=k`, the number of level-`j` elements strictly between successive level-`k` survivors is

`# { m>=1 : S_k(n) < S_j(m) < S_k(n+1) } = q_(k-j)(n)`.

**Proof.** Since `S_k=S_j∘S_(k-j)` and `S_j` is strictly increasing, the inequality holds precisely for indices `m` in the integer interval `S_(k-j)(n) < m < S_(k-j)(n+1)`. The number of those indices is `S_(k-j)(n+1)-S_(k-j)(n)-1=q_(k-j)(n)`. This also covers `j=0` (ordinary integers) and `j=k` (no level-k elements between consecutive level-k elements). QED.

**Concrete first interval of level five.** The endpoints are 31 and 127; strictly between them are exactly 95 ordinary integers, 19 ordinary primes, 5 second-level primes, 1 third-level prime, and 0 fourth-level primes. Reading successive layers yields the same sequence `95,19,5,1,0` as the preceding levels' skipped counts `q_5(1),...,q_1(1)`. This was independently checked by a 30-million integer sieve and by Wolfram's `Prime`, `PrimePi`, and `Nest` commands.

The theorem is an exact **information reorganization**, not an independent zero-free restriction.

## Theorem 2 — Uniform dilution and factorial amplification (classical analytic input)

**Classical input (Montgomery–Vaughan's Brun–Titchmarsh short-interval estimate).** For real `x>=0` and real `H>1`, the uniform bound `π(x+H)-π(x) <= 2H/log H` holds. See Montgomery and Vaughan, *The large sieve*, Mathematika **20** (1973), 119–132, equation (1.12), DOI `10.1112/S0025579300004708`. A source pointer is https://mathoverflow.net/a/370956.

**Statement.** Put `D_k=D_k(n)`. For every `k>=2` and `n>=1`,

`D_(k-1) = π(S_k(n+1))-π(S_k(n)) <= 2 D_k / log(D_k)`,

and therefore

`D_k / D_(k-1) >= (1/2) log(D_k) >= ((k-1) log 2)/2`.

For all `k>=1` and `n>=1`,

`D_k(n) >= ((log 2)/2)^(k-1) (k-1)!`.

Consequently, *uniformly over starting position n*,

`sup_(n>=1) D_(k-1)(n)/D_k(n) = O(1/(k log k))` as `k→∞`.

Furthermore for each **fixed** `n>=1`,

`log D_k(n) ~ k log k` as `k→∞`.

**Proof.** The interval `(S_k(n),S_k(n+1)]` contains exactly `D_(k-1)(n)` primes, because its endpoints are the primes indexed by `S_(k-1)(n)` and `S_(k-1)(n+1)`. Apply the stated Brun–Titchmarsh bound with `H=D_k(n)`. For all `m>=2`, consecutive ordinary primes differ by at least two, hence `D_k(n)>=2 D_(k-1)(n)` for `k>=2`. Since `D_1(n)>=1`, we have `D_k(n)>=2^(k-1)`. Taking logarithms gives `log D_k(n)>=(k-1)log 2` and the second inequality. Iterating it from `2` through `k` gives the factorial lower bound.

Stirling's formula now gives `log D_k(n)>=k log k-O(k)` with an absolute error uniform in n. The same bound and the short-interval inequality imply

`D_(k-1)/D_k <= 2/log D_k=O(1/(k log k))`, uniformly in n.

For the upper bound at **fixed n**, note `D_k(n)<S_k(n+1)` and `log S_k(n+1)~k log k`: writing `a_m=S_m(n+1)` and `b_m=log a_m`, the prime number theorem `p_t~t log t` gives `b_(m+1)-b_m=log b_m+o(1)`. The positive increasing `b_m` first obeys `b_m=Ω(m)` and `b_m=O(m^2)` (using `log b<=sqrt b`), then these estimates improve the increment to `Θ(log m)`, so `b_m=Θ(m log m)`, and finally `b_(m+1)-b_m=log m+O(log log m)`. Summation yields `b_m=m log m+O(m log log m)`. Thus `log D_k(n)<=k log k(1+o(1))`, matching the lower bound. QED.

**Interpretation.** Gaps grow at approximately `exp(k log k)` on the logarithmic scale for any fixed starting position, rather than merely `2^k`. The fraction of ordinary primes among all integers in a deep level-k gap tends to zero at least at rate `O(1/(k log k))`, uniformly in n. For the literal interior fraction `q_(k-1)(n)/q_k(n)` the same upper bound holds because `D_k>=2`. This does not say that no new prime-valued skip patterns occur: their values and positions continue to vary.

## Proof-critical signed-error gate — an exact identity, but no inequality

At level k>=2, let `A=S_k(n)`, `B=S_k(n+1)` and

`e_k(n) = D_(k-1)(n) - ∫_A^B (dt/log t)`.

Then, **exactly**,

`e_k(n) = E(B)-E(A)`, where `E(x)=π(x)-li(x)`.

The positive short-interval bound from Theorem 2 says nothing about the sign or square-root-scale cancellation of these `e_k(n)`; it cannot by itself exclude a hypothetical zero off the critical line. A proposed simple law `e_k(n)>=0` or `<=0` is falsified at every numerically accessible level 2–8. For example, at level 2, intervals `(3,5]` and `(59,67]` give respectively `-0.470999715365...` and `+0.068629743261...`. These signs were separately verified at 60 decimal digits with mpmath.

In the first 200 matched positions the normalized signed-error correlations at adjacent levels were approximately `-0.006` (levels 2–3), `-0.048` (3–4), and `-0.028` (4–5). This is a finite descriptive diagnostic, *not proof* of asymptotic decorrelation. The large correlations in raw numerical gap lengths from earlier audits do **not** convert into a visibly robust same-position correlation of these signed arithmetic errors in this test.

A proof-critical route would need an **independent signed bound** on cumulative `e_k` that is strong enough to constrain `E(x)` at square-root scale and passes interpolation between sampled endpoints. Simply recasting RH as a bound on `E`, or assuming cancellation, is not an advance. The exact nesting and the unsigned Brun–Titchmarsh theorem do not supply that bound.

## Independent numerical audit

`verify_multiscale.py` independently rebuilt all primes to 30,000,000 (1,857,859 primes), regenerated the hierarchy (through level eight where possible), and passed **6,162 exact integer interval-count assertions**. It checked numerical inequalities and produced the full `results.json` and `VERIFICATION_LOG.txt`. The first numerical gap chain `D_k(1)` for levels 1 through 10 is

`1, 2, 6, 20, 96, 582, 4672, 47330, 595680, 9088942`.

Finite signed-error signs:

| Level | Intervals | Positive e_k | Negative e_k |
|---|---:|---:|---:|
| 2 | 500 | 262 | 238 |
| 3 | 500 | 254 | 246 |
| 4 | 500 | 246 | 254 |
| 5 | 241 | 110 | 131 |
| 6 | 52 | 16 | 36 |
| 7 | 15 | 2 | 13 |
| 8 | 5 | 1 | 4 |

The numerical tests are not needed for either theorem. The evidence only checks the formulas over available finite ranges and falsifies simplistic sign laws.

## Verdict and stopping decision

- `PROVED_WITH_STATED_CLASSICAL_INPUTS`: exact nested level-count identity, short-interval thinning/compounding inequalities, fixed-index logarithmic asymptotic. These are written mathematical proofs using PNT, Brun–Titchmarsh and Stirling; **not Lean-checked**, and novelty beyond existing literature is **not established**.
- `COMPUTATIONAL`: finite sieve checks and signed discrepancy diagnostics; all claims are limited to their ranges.
- `NO_NEW_RH_FRONTIER_ADVANCE`: no independent bound ruling out even one off-line zero. Full Haglund k=2/k=3 remains unverified, the marked-inverse moment estimate remains `BLOCKED_NEW_MOMENT_ESTIMATE`, and historic provenance remains `BLOCKED_UNWAIVED`.

**Decision:** Stop adding nested-gap statistics without a proof-critical reason. Keep the signed-error `e_k` as the single testable bridge: a future candidate must prove (not assume) cancellation strong enough to beat established error estimates, surviving the exact telescoping/selection controls. No Codex campaign, no installation, no historical artifact edits.

**Sources:**
1. Montgomery & Vaughan (1973), *The large sieve*, DOI `10.1112/S0025579300004708`, short-interval inequality; accessible statement at https://mathoverflow.net/a/370956.
2. NIST DLMF §27.12, https://dlmf.nist.gov/27.12, nth-prime asymptotic and RH-related prime counting error.
3. Batchko (2014), *A prime fractal and global quasi-self-similar structure in the distribution of prime-indexed primes*, https://arxiv.org/abs/1405.2900.
