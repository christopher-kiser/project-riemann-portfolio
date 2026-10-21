> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `e4b9083b4984f276e28da0f254ec95d1741d34fbd8650166b1411598512c46a2`.

# Project Riemann — Mesoscopic signed-correlation inverse gate

**Date:** 2026-10-20  
**Scope:** Continuation of `SIGNED_PARITY_AND_AFFINE_GATE.md`.  
**Verdict:** `EXACT_UNIVERSAL_INVERSE_LEMMA / SQUAREFREE_SUPPORT_COUNTERMODEL / NO_NEW_RH_FRONTIER_ADVANCE`.  
**Historical statuses unchanged:** RH OPEN; Haglund k=2/k=3 full verification UNVERIFIED; marked-inverse moment estimate BLOCKED_NEW_MOMENT_ESTIMATE; historical provenance BLOCKED_UNWAIVED.

## 1. Exact finite Fejér identity

Let `N>=2`, `2<=H<=N`, and let `a_1,...,a_N` be real numbers of modulus at most one, extended by zero to all integers. Put

\[
M=\sum_{n=1}^Na_n,\qquad Q=\sum_{n=1}^Na_n^2,\qquad C_N(h)=\sum_{n=1}^{N-h}a_na_{n+h}.
\]

For every integer `x` define the moving window `W_H(x)=sum_{j=0}^{H-1}a_{x+j}`. Exactly `N+H-1` windows potentially intersect the support, and each `a_n` appears in exactly `H` of their sums. Therefore

\[
\sum_x W_H(x)=HM,\qquad
\sum_x W_H(x)^2=HQ+2\sum_{h=1}^{H-1}(H-h)C_N(h).
\tag{1}
\]

By finite Cauchy-Schwarz,

\[
\boxed{HQ+2\sum_{h=1}^{H-1}(H-h)C_N(h)
\ge\frac{H^2M^2}{N+H-1}.}
\tag{2}
\]

In particular,

\[
\boxed{\max_{1\le h<H} C_N(h)\ge
\frac{H M^2/(N+H-1)-Q}{H-1}.}
\tag{3}
\]

The bound is useful only when the numerator is positive. It is purely algebraic and applies equally to the actual Möbius function and to synthetic control sequences. It is a form of the classical van der Corput/Fejér correlation method, not a novel analytic-number-theoretic theorem.

## 2. Necessary correlation signature of one hypothetical off-line zero

Assume `rho=beta+i gamma` is a zero of the genuine Riemann zeta function, with `1/2<beta<1`. Since `1/zeta(s) = sum mu(n)n^{-s}` initially for `Re(s)>1`, if `M_mu(N)=O(N^{beta-delta})` held for any `delta>0`, partial summation would analytically continue this Dirichlet series to `Re(s)>beta-delta`, contradicting the pole of `1/zeta` at `rho`. Thus for every `delta>0` there are infinitely many integers `N` with

\[
|M_\mu(N)|\ge N^{\beta-\delta}.
\tag{4}
\]

**Precise mesoscopic consequence:** For any fixed `eps` with `0<eps<2 beta -1`, there are infinitely many `N` for which, setting `H=ceil(N^{2-2 beta+eps})`, there are at least

\[
\boxed{\frac5{32}N^{\varepsilon/2}}
\]

**distinct shifts** `1<=h<H` satisfying

\[
\boxed{C_N(h)>\frac1{16}N^{2\beta-1-\varepsilon/2}.}
\tag{5}
\]

**Proof:** Put `delta=eps/4` and take the infinitely many `N` from (4), with `M=M_mu(N)` and `Q<=N`. Since `eps<2beta-1`, for large `N` we have `H<=N`. Then

\[
\frac{H M^2}{N+H-1}\ge \frac{H M^2}{2N}\ge\tfrac12N^{1+\varepsilon/2}\ge4N\ge 4Q
\]

for sufficiently large `N`. Denote `S=sum_{h=1}^{H-1}(H-h) C_N(h)`. From (2),

\[
S\ge\frac38\frac{H^2M^2}{N+H-1}
\ge\frac3{16}\frac{H^2M^2}{N}.
\]

Set `tau=M^2/(16N)`. The total contribution of shifts with `C_N(h)<=tau` to `S` is at most `tau H(H-1)/2 <= H^2 M^2/(32N)`. Therefore the shifts with `C_N(h)>tau` contribute at least `5H^2M^2/(32N)`. Each such summand is at most `HN`, because `|C_N(h)|<=N`. There must be at least

\[
\frac{5 H M^2}{32 N^2}\ge\frac5{32}N^{\varepsilon/2}
\]

such shifts. Finally `tau>= N^{2beta-1-eps/2}/16`, proving (5). All inequalities are classical and unconditional *conditional on the existence of the hypothetical zero*. Multiplicities do not invalidate the analytic-continuation argument.

**Interpretation:** The necessary shift length has exponent approximately `2(1-beta)` and the necessary correlation magnitude has exponent `2beta-1`: their sum is `1`. This balancing relation comes from elementary finite Cauchy-Schwarz, not a zeta-specific conservation law. If `beta<=3/4`, the forced individual-correlation size is no larger than a square-root noise scale, so a pointwise bound close to random-sign estimates would not detect it. What matters would be a *joint weighted excess* of correlations on growing shift ranges.

## 3. Exact squarefree-support adversarial countermodel

For every fixed `1/2<beta<1` construct *independent* random signs `eps_n ∈ {-1,+1}` with mean `E eps_n = n^{beta-1}`. Define

\[
b(n)=\mu(n)^2\,\varepsilon_n.
\]

**Exact support:** `b(n)^2=mu(n)^2` for every `n`, deterministically. Thus `b` preserves every unsigned squarefree/divisibility observation, not merely finite samples. It is NOT multiplicative and is NOT the actual Möbius function.

**Biased first moment:** Using the classical `sum_{n<=N}mu(n)^2 = (6/pi^2)N + O(sqrt N)` and summation by parts,

\[
\mathbb E\sum_{n\le N}b(n)
=\sum_{n\le N}\mu(n)^2 n^{\beta-1}
=\frac{6}{\pi^2\beta}N^\beta+O_\beta(N^{\beta-1/2}+1).
\]

Hoeffding's inequality and Borel-Cantelli give almost surely

\[
\sum_{n\le N}b(n)
=\frac{6}{\pi^2\beta}N^\beta +O_\beta(\sqrt{N\log N}+N^{\beta-1/2}+1)
\sim\frac{6}{\pi^2\beta}N^\beta.
\tag{6}
\]

**All fixed shifted correlations have a power saving:** For each *fixed* integer `h>=1`, independence gives

\[
\mathbb E\sum_{n\le N-h}b(n)b(n+h)
=\sum_{n\le N-h}\mu(n)^2\mu(n+h)^2 n^{\beta-1}(n+h)^{\beta-1}
=O_\beta(N^{2\beta-1}).
\]

Changing one independent sign changes this correlation by at most `4`, because it influences at most two terms. McDiarmid's bounded-differences inequality and Borel-Cantelli give, almost surely for every fixed `h` (by a countable intersection),

\[
\boxed{\sum_{n\le N-h}b(n)b(n+h)
=O_{\beta,h}(N^{2\beta-1}+\sqrt{N\log N})=o(N).}
\tag{7}
\]

The exponent `max(2beta-1, 1/2)` is strictly below `1`, apart from the displayed square-root logarithm. Thus **there exists one deterministic realization** of a real three-valued sequence satisfying *simultaneously* the exact genuine squarefree support, power-saving fixed-shift autocorrelation for every fixed `h`, and an RH-violating exponent for its cumulative sum. This is a rigorous existence argument; the finite simulation below is not its proof.

**What the countermodel DOES NOT preserve:** Multiplicativity, the exact Dirichlet inverse `mu*1=delta`, the signs at actual primes, or the prime Euler product. Hence it does not disprove RH; it falsifies any argument that attempts to derive RH strength from unsigned counting and fixed-shift pair cancellation alone.

## 4. Exact numerical diagnostics

The script `verify_mesoscopic_gate.py` constructs the genuine Möbius function by a linear sieve at `N=120000`; independently checks selected FFT autocorrelations against exact integer dot products; verifies the full finite window identity by integer convolution at `H=32, 128, 512, 2048`; and checks the five-prime parity gauge from the prior audit.

For the genuine Möbius function, `M(120000)=104`, `Q=72948`. For the finite-prime gauge `M=5086`, while the squarefree support remains the same. At `H=2048` the gauge's correlation maximum is `43589`; the universal Cauchy lower bound for the maximum is `176.413`. The very wide gap shows that this is not a sharp bound without additional arithmetic input.

The independent script `verify_biased_sign_control.py` uses a published seed for a **finite diagnostic**, with `beta=3/4` and `N=120000`. A fully biased sign sequence has sum `8392`. Masking with exact genuine squarefree support gives a sum `5282` (predicted mean `5226.41`) and fixed-shift sample correlations between `-288` and `653` for shifts `h=1,2,3,5,10,100,300`. A finite experiment cannot verify the almost-sure infinite theorem; §3 supplies the proof.

## 5. Research decision

The main observation is a precise dual scaling obstruction:

- A hypothetical zero with `Re(rho)=beta>1/2` would force *some* mesoscopic sign coherence, at shifts approximately `N^{2(1-beta)}` and correlation size `N^{2beta-1}`, with tiny exponent allowances.
- Qualitative, or even power-saving, **fixed-shift** two-point cancellation does **not** independently imply RH. We have a squarefree-support synthetic countermodel proving this.
- The 2026 ordinary two-point Liouville preprint is stated for **fixed affine forms**, with a logarithmic saving; even if fully established, the claim is quantitatively far too weak for this inverse gate, and the preprint must not be silently identified with a uniform Möbius theorem over polynomially growing shifts.
- A plausible *separate, genuinely arithmetic premise* would control the **joint Fejér-weighted correlations** uniformly at polynomially growing shifts and approximate square-root variance. But this is not established and risks becoming another disguised RH-equivalent bound. No independent prime-specific inequality survived this audit. Do not launch Codex on the present formulation.

**Classification:** Classical universal inverse lemma proved, probabilistic squarefree-support countermodel proved, numerical diagnostics passed, NO_NEW_RH_FRONTIER_ADVANCE. Lean 4 was not available; no Lean-checked analytic proof is claimed. All work was saved to this new directory without modifying historical evidence.

### Relevant primary sources (scope checked)

- Nathan Ng, *The Möbius function in short intervals* (2008), `https://www.cs.uleth.ca/~nathanng/RESEARCH/mobiusshort.pdf` — studies short-interval moment conjectures; strong statements require additional Möbius correlation hypotheses.
- Matomäki, Radziwiłł, Shao, Tao, and Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Inventiones Mathematicae (2026), `https://doi.org/10.1007/s00222-026-01408-6` — unconditional higher uniformity for almost all intervals, different from the present conjectural square-root second-moment bound at all mesoscopic scales.
- OpenAI, *Ordinary two-point correlations of multiplicative functions* (2026), `https://github.com/openai/math/blob/main/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/README.md`, with formalization scope `https://github.com/openai/math/blob/main/lean/docs/007.md` — fixed nonproportional affine Liouville correlations with a claimed log-power saving; not a polynomial growing-shift estimate for Möbius.
- Classical van der Corput correlation inequality and Fejér's identity, from elementary Cauchy-Schwarz/Fourier analysis.
