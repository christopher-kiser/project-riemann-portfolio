# Case study: turning a nested-prime observation into exact statements

Christopher's recorded question was to repeatedly select primes at prime-numbered positions, then study skipped integers, prime-valued gaps, runs and their nested patterns. This produced precise combinatorial questions and controls that distinguish an identity from an arithmetic bound.

Let pₙ be the nth prime, S₀(n)=n, S₁(n)=pₙ and Sₖ₊₁(n)=Sₖ(pₙ). Define Δₖ(n)=Sₖ(n+1)−Sₖ(n) and qₖ(n)=Δₖ(n)−1.

## Two written elementary proofs

**Gap-block identity.** Telescoping gives

$$\Delta_{k+1}(n)=\sum_{j=p_n}^{p_{n+1}-1}\Delta_k(j).$$

There are pₙ₊₁−pₙ summands. Subtracting one from both sides therefore gives

$$q_{k+1}(n)=q_1(n)+\sum_{j=p_n}^{p_{n+1}-1}q_k(j).$$

The q₁ term is essential. Omitting it produces a false skipped-count identity.

**Interior survivor count.** For 0≤j<k, Sₖ=Sⱼ∘Sₖ₋ⱼ. Since Sⱼ is strictly increasing, its values strictly between Sₖ(n) and Sₖ(n+1) correspond exactly to integers strictly between Sₖ₋ⱼ(n) and Sₖ₋ⱼ(n+1). Their number is qₖ₋ⱼ(n). The proof uses order and composition, not an assumption about randomness of primes.

For example, consecutive level-five values 31 and 127 contain 95 integers, 19 level-one survivors, 5 level-two, 1 level-three and no level-four survivors strictly between them.

## Adversarial control and limitation

The telescoping identity also works for a general strictly increasing integer sequence when it is reindexed by the same prime positions. An affine control retains related gap patterns. Therefore the identity itself cannot be promoted into a prime-specific cancellation theorem or an RH argument. The original project also investigated modular constraints, signed prime-error flow and deeper geometric encodings; their separate hypotheses remain visible in the atlas.

The [small standard-library demonstration](../../scripts/nested_prime_demo.py) checks the stated finite examples and deliberately rejects the missing-q₁ formula. It does not rerun the historical 30-million-integer explorations, and finite examples do not prove the general statements above.

[Original research note](../../research/notes/nested-prime-pattern-audit.md) · [Multiscale count audit](../../research/notes/multiscale-dual-count-and-growth-audit.md) · [Contribution and novelty boundaries](../contributions.md)
