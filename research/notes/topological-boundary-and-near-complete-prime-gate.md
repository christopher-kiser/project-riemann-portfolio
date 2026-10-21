> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `6cb4cb5c8927d38cc9f9586e21e4c611e5039994e0ef67439e2f979db8cc9409`.

# Project Riemann — Topological boundary and near-complete prime-law gate

Date: October 20, 2026. Classification: **EXACT CLASSICAL TOPOLOGICAL/ARITHMETIC NO-GO; NO_NEW_RH_FRONTIER_ADVANCE**.

This audit follows `FINITE_PRIME_MULTISCALE_GATE.md`. It is independent of the older blocked marked-moment problem. RH remains open. Haglund k=2/k=3 remains unverified; provenance remains BLOCKED_UNWAIVED. No historical artifacts or Git references were altered. No Codex campaign was launched. Lean 4 is not installed in this execution environment; the algebraic arguments below are written classical proofs, not Lean certifications.

## 1. Originality/literature gate

The simplicial/topological representation of the Mertens function is **established literature**, in particular Anders Björner, *A cell complex in number theory* (2011), https://arxiv.org/html/1101.5704v1 (Theorem 3.1 and equation 1.1). The finite supertrace formula is the standard finite-dimensional McKean–Singer identity, e.g. O. Knill, *The McKean-Singer Formula in Graph Theory*, https://arxiv.org/abs/1301.1408. A prime-sieve perspective on incomplete constraints is classical in Buchstab-type decompositions: https://encyclopediaofmath.org/index.php?title=Buchstab_identity. Quantitative PNT: https://encyclopediaofmath.org/wiki/De_la_Vall%C3%A9e-Poussin_theorem. No literature priority claim is made for the elementary synthesis here.

## 2. Exact topology and parity cancellation

Let Δ_N have one vertex for each prime p≤N and faces given by sets F of distinct primes with ∏_{p∈F}p≤N, including the empty face. Its **augmented** real chain groups are C_r(N), with basis indexed by faces of cardinality r, and ∂ removing one prime with the alternating orientation convention. Note C_0 includes the empty face. Then ∂²=0 and

    str(I)= sum_{r≥0} (-1)^r dim C_r(N)
           = sum_{n≤N} μ(n) = M(N).

The ordinary reduced topological Euler characteristic of Δ_N is χ̃(Δ_N)=−M(N) with this indexing; the shifted augmented parity convention above gives +M(N). Confusing these signs would be an error.

For every N≥2, pairing every odd squarefree n≤N/2 with its even partner 2n gives μ(n)+μ(2n)=0. Every even squarefree n≤N has exactly one such odd partner; hence

    M(N) = sum_{N/2<n≤N, n odd} μ(n).              (T1)

The odd squarefree integers in (N/2,N] form an antichain for strict divisibility: if a|b with a<b, then b≥2a>N. No further cancellation by adding a prime factor can occur **within that residual shell**. This does not preclude a non-divisibility pairing using additional arithmetic data.

Björner's shifted-complex theorem gives, for r≥1,

    β_r^aug(N) = #{odd squarefree n∈(N/2,N] : ω(n)=r},

and β_0^aug(N)=0 for N≥2. Thus the even- and odd-degree ground-state populations are ≍N/π² **each**, while their difference is exactly M(N). The asymptotic uses the ordinary prime number theorem, not RH.

## 3. Exact supersymmetric heat identity — and why it is not an RH proof

On ⊕_r C_r(N), define Q=∂+∂*, H=Q²≥0, and Γ|_{C_r}=(-1)^r. Q is self-adjoint, ΓQ=−QΓ, and Q commutes with H. On a positive eigenspace of H, Q/√λ interchanges Γ=+1 and Γ=−1. Thus all positive-energy contributions to the graded trace cancel, leaving

    Tr(Γ e^{-tH})=sum_r (-1)^r β_r^aug(N)=M(N)   for all t≥0.      (T2)

This is a **finite artificial arithmetic quantum-style system**, not a physical measurement model and not a Hilbert–Pólya realization of Xi. Time evolution does not control the number of unpaired zero modes. The RH-strength estimate |M(N)|=O_ε(N^{1/2+ε}) is equivalent to bounding the imbalance of the ground-state populations; merely rewriting it as (T2) is not an independent result.

At N=30, exact rational boundary-matrix ranks give augmented Betti numbers β_1=4, β_2=1, others zero. The numerical supertrace at t=0, 0.01, 0.1, 1 and 10 equals −3 to floating-point precision; the theorem, not the computation, establishes the identity for all t.

## 4. Sharper no-go: prime laws in an increasing fraction approaching 100%

Fix N≥10 and a real y with N/2≤y<N. Consider any b:{1,...,N}→{−1,0,1} obeying:

 (i) b(1)=1;
 (ii) b(n)²=μ(n)² for all n≤N;
 (iii) b(pn)=−b(n) whenever p≤y is prime, p∤n, pn≤N (and b(pn)=0 if p|n).

**Exact classification.** For every composite squarefree n≤N, all its prime factors are ≤N/2≤y; repeatedly removing factors forces b(n)=μ(n). The same is true at each prime ≤y. Nonsquarefree values are zero by (ii). The *only free signs* are b(p) for prime p∈(y,N]. Conversely, assigning any ±1 values to those primes gives a sequence satisfying all conditions. Therefore the constraint space has exactly

    L_N(y) := π(N)−π(y)

independent binary degrees of freedom.

Let A_N denote the fixed signed sum over all nonfree positions. Then the extremal identity is exact:

    max_{admissible b} |sum_{n≤N} b(n)| = |A_N| + L_N(y) ≥ L_N(y).    (T3)

Indeed sum b=A_N+Σ_{free p}b(p); choose all free signs to agree with sign(A_N). This needs no estimate of M(N), no RH premise, and no statistical model. In particular any uniform RH-strength conclusion from (i)–(iii) alone is impossible whenever L_N(y) is much greater than sqrt(N).

**Near-complete regime.** Take y_N=floor(N−N/log N). The classical de la Vallée-Poussin PNT error gives

    L_N(y_N)=π(N)−π(y_N) ~ N/(log N)².          (T4)

Since π(y_N)/π(N)→1, the enforced prime directions comprise a fraction tending to **100%** of all primes up to N, but (T3) permits a summatory imbalance at least N/(log N)², far greater than N^{1/2+ε} for any fixed 0<ε<1/2.

**All bounded-order additive observations can also miss the change.** For r fixed, extend b and μ by zero outside [1,N]. For any integers h_1,...,h_r (even if they depend on N), define normalized correlations

    C_b(h_1,...,h_r) = (1/N) Σ_{n=1}^N ∏_{j=1}^r b(n+h_j).

Because b differs from μ at at most L_N(y) positions and all factors have absolute value ≤1, the telescoping-product inequality yields

    |C_b(h_1,...,h_r)−C_μ(h_1,...,h_r)| ≤ 2 r L_N(y)/N.    (T5)

For y=y_N this is O_r(1/(log N)²) uniformly in all shifts. In particular a fixed finite number of unnormalized observations can look increasingly similar while the possible global signed discrepancy is much larger than square-root scale.

**CRUCIAL QUANTIFIER WARNING:** b=b_N depends on the cutoff N. This does NOT construct a single alternative arithmetic function satisfying every prime dilation identity at all n. If b(1)=1 and the prime laws hold for *all primes at all scales*, then b=μ on the squarefree integers by unique factorization. Uniqueness does not provide the required cancellation bound. It is invalid to pass from per-cutoff, non-uniform estimates to a uniform infinite-prime theorem.

## 5. Verification and adversarial tests

- `verify_topology.py` regenerated μ up to 1,000,000, verified (T1) at six cutoffs, and checked exact augmented boundary-map ranks and ∂²=0 at N=30. A float matrix exponential diagnostic checked (T2) at five times. The proof of (T2) is exact and independent of those floats.
- `verify_boundary.py` regenerated μ independently; checked (T3) and shell sizes for N=100,1000,10000,100000,1000000; checked **all 24,179 admissible** small-prime dilation edges for N=10000; and tested a three-point shift correlation against (T5).
- For N=1,000,000, y=927617, there are exactly L=5200 untested prime signs. Actual M(N)=212. Choosing b(p)=+1 on those free primes yields sum b=10,612. This is a *countermodel to incomplete inference*, not a candidate counterexample to RH.
- At N=1,000,000, the actual augmented homology has 101,429 even-parity zero modes, 101,217 odd-parity modes, and index +212. Both classes are large; heat invariance gives no upper bound on their difference.

## 6. Decision and possible positive theorem candidate

**VERDICT: `TOPOLOGICAL_SUPERTRACE_EXACT / NEAR_COMPLETE_PRIME_LAW_NO_GO / NO_NEW_RH_FRONTIER_ADVANCE`.**

We now know that ordinary topological homology and quantum heat-time invariance merely re-express the Mertens index, while even near-complete prime-direction constraints at each cutoff permit RH-incompatible signed imbalances. The missing condition must be **quantitatively uniform in the prime-coordinate horizon and the observation cutoff**. Neither ordinary positive spectra nor average fixed-order correlations supplies that bound.

A future genuinely proof-critical candidate would be an *explicit arithmetic pairing of opposite-parity zero modes across incomparable boundary faces*, accompanied by an independently proved bound for unmatched modes. But merely assuming that only O_ε(N^{1/2+ε}) remain unmatched is RH-equivalent. No such independent pairing estimate was obtained here; no Codex run is warranted.

Historical RH, Haglund and provenance classifications remain unchanged.
