> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `0fd82eff7a9c760429e655bdce612b48fbed0f0edf7e28d1f7ea77fe1243a608`.

# Project Riemann — Finite-prime Walsh–Möbius gate and analytic pole persistence

Date: 2026-10-20. Verdict: **EXACT CLASSICAL FINITE-PRIME GATE / NO_NEW_RH_FRONTIER_ADVANCE**.

This is a deliberately bounded follow-up to the prime-boundary/topology audit. It asks whether expanding to more prime-index directions produces a new cancellation theorem about the *actual* Möbius function. It does **not** claim RH, a new zero-free region, or mathematical priority. All historical artifacts remain untouched; no Codex run was launched. Lean 4 was absent from this environment. Exact finite checks were executed with integer arithmetic.

## 1. The exact multiscale identity

Fix a nonempty finite set of distinct primes `P={p_1,...,p_r}` and write `Q=∏_{p∈P}p`. For real `x>=0` put

    A_Q(x) = Σ_{n≤x, gcd(n,Q)=1} μ(n).

Each squarefree `n` has a unique factorization `n=d m`, with `d=gcd(n,Q)|Q`, `gcd(m,Q)=1`, and `μ(n)=μ(d)μ(m)`. Nonsquarefree terms vanish. Therefore, for every `x>=0`,

    M(x) = Σ_{d|Q} μ(d) A_Q(x/d).                           (1)

The `r=1, p=2` case is exactly the established odd upper-shell pairing `M(x)=A_2(x)-A_2(x/2)`.

For `e∈{0,1}^r` let `d_e=∏_i p_i^{e_i}` and `g_x(e)=A_Q(x/d_e)`. The normalized Boolean Walsh transform is

    ghat_x(S) = 2^{-r} Σ_{e∈{0,1}^r} (-1)^{Σ_{i∈S}e_i}g_x(e).

The full parity frequency, `S={1,...,r}`, satisfies

    M(x) = 2^r ghat_x({1,...,r}).                          (2)

This is an **identity**, not a bound on the high-order coefficient. General Walsh analysis is established literature.

## 2. Exact worst-case amplification

On bounded functions `f:(0,∞)→ℂ` define

    (D_Q f)(x)=Σ_{d|Q}μ(d)f(x/d).

The triangle inequality gives `||D_Q||_{∞→∞}≤2^r`. Equality follows by fixing an arbitrary `x>0` and assigning `f(x/d)=μ(d)` at the `2^r` distinct points `x/d` (and `f=0` elsewhere). Thus

    ||D_Q||_{∞→∞}=2^r.                                    (3)

The sharpness example is for **arbitrary** bounded functions, not necessarily an arithmetic rough-sum `A_Q`, so it is a methodological warning rather than a no-go theorem about every possible arithmetic proof.

Similarly, full parity cannot be bounded from every proper Walsh coefficient for a general nonnegative cube array: the two strictly positive arrays `g_0(e)=10` and `g_1(e)=10+(-1)^{Σ e_i}` have identical Walsh coefficients on every proper subset `S`, but their full Walsh coefficients differ by `1`, or equivalently the unnormalized parity sums differ by `2^r`. These artificial arrays do **not** satisfy all arithmetic compatibility identities as `x` varies. This demonstrates the incompleteness of generic lower-order observations only.

## 3. Analytic persistence of a hypothetical zero

In `Re s>1`, the Dirichlet series of the same actual rough Möbius sequence satisfies

    G_Q(s) = Σ_{(n,Q)=1} μ(n)/n^s
           = [1/ζ(s)] ∏_{p|Q}(1-p^{-s})^{-1}.             (4)

Its right side supplies a meromorphic continuation. Suppose the genuine Riemann zeta function has a zero `ρ` with `0<Re ρ<1`, of multiplicity `m`. Every `1-p^{-ρ}` is nonzero because `|p^{-ρ}|=p^{-Reρ}<1`. Consequently `G_Q` has a pole of **the same order m** at `ρ`.

For a simple zero,

    Res_{s=ρ} G_Q(s) = (1/ζ'(ρ)) ∏_{p|Q}(1-p^{-ρ})^{-1} ≠ 0.   (5)

This is unconditional **as an implication about a hypothetical zero**, and applies to every fixed finite set `P`. It does not say that `ρ` exists. It rules out the notion that finitely many ordinary prime-coordinate filters can *erase* an off-line pole. Such filters can change its amplitude, and may be useful within a richer argument, but cannot alone supply the missing zero-exclusion estimate.

## 4. Exact finite experiment

`verify_gate.py` independently sieves `μ` through `N=1,000,000`, checks (1) for the first 1 through 7 primes, computes the full Boolean parity coefficient, and verifies the strictly-positive lower-order-blindness counterexample in dimensions 2, 3, 5. The recorded output is `verification.log`.

| Prime directions r | Σ_{d|Q}|A_Q(N/d)| | Σ_{d|Q} μ(d)A_Q(N/d) |
|---:|---:|---:|
| 1 | 212 | 212 |
| 2 | 692 | 212 |
| 3 | 3,696 | 212 |
| 4 | 11,728 | 212 |
| 5 | 25,276 | 212 |
| 6 | 45,200 | 212 |
| 7 | 68,584 | 212 |

All arithmetic is exact integer arithmetic. The growth of the absolute component sum is **not claimed as monotone for every N or every prime set**; it is a reproducible finite observation. The signed sum equals 212 at all r by (1), independently of the calculation. Normalization of the Walsh coefficient by `2^{-r}` makes it appear small as `r` grows; that decrease by itself is also automatic and not evidence of a new cancellation mechanism.

## 5. Falsification result and next proof-critical requirement

The natural proposed inference, "more independent prime-dimension observations automatically imply stronger cancellation of `M(N)`", fails. The arithmetic transformation preserves its target exactly, generic reconstruction can amplify error by `2^r`, and the meromorphic pole associated with any hypothetical off-critical zero survives every **fixed finite** prime filter.

What remains is the all-prime, moving-scale analytic constraint that none of the previous finite-prime, topological, spectral, positive-kernel, or signed-average constructions has provided. It would have to give a noncircular *quantitative* bound on a signed full-prime interaction, and explicitly show how that bound excludes a zero or improves the existing zero-free exponent. Merely stipulating `|M(N)|≪N^α` in the full parity coefficient (2) is exactly an equivalent reformulation, not a new proof.

A promising path must therefore either (i) derive a **uniform-in-growing-Q** arithmetic estimate whose constants do not suffer the worst-case `2^r` amplification, or (ii) find a new prime-specific analytic/geometry principle that excludes a hypothetical pole in (4) without presupposing its absence. Neither is established here. This branch is closed to further *finite-prime dimension-count* optimization.

## Literature and comparison

- Steve Lester and Zeév Rudnick, *Introductory lectures on arithmetic functions* (Dirichlet series, Möbius convolution and `1/ζ`), https://www.math.tau.ac.il/~rudnick/courses/sieves2015/arithmetic%20functions.pdf.
- *Buchstab identity*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/index.php?title=Buchstab_identity — established prime-sieve decomposition.
- Anders Björner, *A cell complex in number theory* (2011), https://doi.org/10.1016/j.aam.2010.09.007 — existing topology of `M(N)` and large homology.
- Standard Walsh–Hadamard Fourier analysis of Boolean cube (not a new transform), see https://www.sciencedirect.com/topics/mathematics/walsh-transform.
- OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s>7/8* (2026; external formal-check reports), https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/README.md. Recent proposed refinements exist, so beating classical logarithmic zero-free regions alone would not establish new territory.

## Scope

`PROVED_EXACT_FINITE_PRIME_IDENTITIES / CONDITIONAL_POLE_PERSISTENCE / NO_NEW_RH_FRONTIER_ADVANCE`.
No Lean proof is claimed. No fresh mathematical priority is claimed. RH remains open; Haglund `k=2/k=3` complete verification remains `UNVERIFIED`; historical provenance `BLOCKED_UNWAIVED`; the prior marked-moment estimate `BLOCKED_NEW_MOMENT_ESTIMATE`.
