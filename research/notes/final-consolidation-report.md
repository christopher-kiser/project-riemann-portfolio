> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `675ef063e5ce6b5727745164c5b68993f78f0873a6dbef52316286c7dba9e081`.

# Project Riemann — single-pass consolidation, 18 October 2026

**Verdict: NO_NEW_RH_FRONTIER_ADVANCE. RH is unproved. Complete historical k=2/k=3 verification remains UNVERIFIED. Historical provenance remains BLOCKED_UNWAIVED.**

Workspace: `LOCAL_ARCHIVE/project-riemann-consolidation-20261018T221141Z`.

The useful outcome is a corrected dependency chain, not a new zero-exclusion theorem. The late claims yield valid coefficient identities, correctly normalized moment transfers and finite Fourier identities. None proves the long, zeta-weighted mollified moment estimate needed to reach a new zero-free half-plane. In particular, comparison with the actual theta approximants does not remove that missing estimate. No new RH research campaign was started.

## 1. Evidence and scope

The supplied ZIP's README and single-pass prompt were adopted as the task instructions; its research delta was treated as an unverified claim queue. The six original audited handoff files, eight subsequent WSL audit reports, their dependency ledgers, actual Lean sources and accepted compilation receipts are the primary local evidence. Exact paths, quotations and hashes are in `UPDATED_HANDOFF/06_SOURCES_AND_PATHS.md`, `SOURCE_READ_MANIFEST.json` and `sources/LOCAL_SUPPORT_QUOTES.md`.

Prior analytic results are **reused at their written, classical-input scope**. This consolidation inspected their statements, domains, dependencies and relevant derivations; it did not independently repeat all eight full analytic audits or historical numerical integrations. The new late-claim arguments are reconstructed below. Modern primary-source statements were checked in bounded introductions/abstracts, not their entire proofs or external formal builds. Retrieval scope and versions are recorded in `sources/RETRIEVAL.json`. A reported theorem and a locally compiled theorem are distinct evidence classes.

## 2. Historical results retained, with their exact limitations

Use the actual normalization

\[
 a_n=\pi n^2,\quad h_n(u)=a_ne^{5u/2-a_ne^{2u}}(2a_ne^{2u}-3),\quad
 \Phi_n(z)=4\int_0^\infty h_n(u)\cos(zu)\,du,
\]
\[
 \Xi(z)=\xi(1/2+iz),\quad \Xi_k=\sum_{n\le k}\Phi_n,\quad
 F_{j,v}=\Xi_j+v\Phi_{j+1},\quad 0\le v\le1.
\]

The audited common bound is
\[
 |\Xi-F_{j,v}|\le V_N=64N^2e^{-\pi N^2}
 \quad(N\ge2,\ j\ge N-1,\ |\Im z|\le1/2).                 \tag{T}
\]
It follows by positive kernel majorants, not by ordering complex tails. The quasi-RH report's §2 rederives the geometric sum including both deformation endpoints. This is a written analytic input, not a newly formalized integral theorem.

The original corrected checkpoint also retains theta-tail accretivity for N≥2 and the qualitative fact that the largest positive real zero L_k exists, strictly increases and tends to infinity. Positivity of the spatial kernel does not imply positivity of every cosine transform: Phi_1 is eventually negative on the real axis. The qualitative L_k conclusion gives no quadratic rate. Old stronger finite/exterior certificates and the reported k=27 ordering counterexample remain unreplayed at their recorded scope; the latter is not a refutation of the deformation-motion conjecture. Historical Gaussian/Epstein/other model limitations are not upgraded by newer models with different preserved properties.

* **Fixed-head obstruction:** the first-order absolute Euler–Maclaurin lower budget fails at Re s=1 for all cutoffs M≥q once t≥q²2^(2q+1), for each fixed q. It says nothing universal about growing heads or retained phase.
* **Cofinal transfer:** for every sufficiently large k, N=k+1, some regular R lies in `(4N²−B log N,4N²−B log N+1)` and the symmetric-rectangle total count for Xi_k equals N_zeta(R), with multiplicity. This is an existential selection, not a count of real zeros and not a statement about every ordinate.
* **Upper cap:** some absolute c*>0 works for each fixed C<8/π, all sufficiently large N, every j≥N−1 and v∈[0,1], throughout `0≤x≤4N²+C log N`, `1/2−c*/log³(3+x)≤|y|≤1/2`. The relative error is O_C(N^(−2+πC/4) log N). Thresholds remain existential.
* **Density/corridor:** for fixed 0<a<b<4, in the moving window [aN²,bN²], the upper band above h_N=12 log log N/log N has total multiplicity O(N²/log^10 N), against a total `(b−a)N² log N/π+O(N²)`. The exceptional proportion is O(log^(−11)N); there is a common closed zero-free corridor of length Ω(log^11 N), uniformly over later deformations. **The upper bound grows; it does not prove that the actual exceptional count grows, or even that an exception exists.** It cannot eliminate a fixed exception or cover the anchored inner region.
* **Exponential shadowing:** for each fixed 0<b<4, every later-deformation zero in `0≤x≤bN²`, `|y|≤1/2` lies strictly within exp(−c_bN²/log N) of some genuine Xi zero. The shadow need not be unique, real, in that rectangle, or index/multiplicity matched.
* **Artificial countermodels:** positive kernels, order one, actual increments and one persistently descending nonreal branch are compatible in the audited artificial families. In the arithmetic-rigidity model only the *limit* f=Xi·g preserves Xi's real zeros/signs; the G approximants do not inherit that claim. These models neither refute RH nor Haglund's actual conjecture. This generic countermodel line stays closed.
* **7/8 bridge:** the prior report inspected an externally formalized statement and independent build records but did not rebuild its closure. Conditional on that external premise, Xi zeros satisfy |y|≤3/8. Each fixed band `3/8+ε≤|y|≤1/2` is eventually excluded up to `4N²−B_ε log N+1`, uniformly over later deformations. The inner band remains unresolved.

## 3. L02–L03: mollified moments and the corrected transfer

For integer L≥2 use exactly the linear taper
\[
 M_L(s)=\sum_{d\le L}\mu(d)(1-\log d/\log L)d^{-s},\quad
 I_L(U,V)=\int_U^V|\zeta(1/2+iu)M_L(1/2+iu)|^2du.
\]
[Bettin–Gonek, arXiv:1604.02740v1, Theorems 1–2](https://arxiv.org/html/1604.02740v1), later Mathematika 63 (2017), requires, for fixed θ>0, every ε>0 and **uniformly all integers 2≤L≤T^θ and all sufficiently large T**, a bound O_ε(T^(1+ε)). For [0,T] it implies nonvanishing on Re s>1/2+1/(2θ); for [T,2T] the stated implication is Re s>1/2+2/θ. Fixed θ may enter constants, L,T may not. Arbitrarily large θ gives RH. No required moment bound is established here; dyadic information cannot simply be inserted into the stronger theorem.

Let `A(s)=s(s−1)π^(−s/2)Γ(s/2)/2` and `Q(u)=F_(j,v)(u)/A(1/2+iu)`. Gamma has no zeros; A is nonzero on this line, including u=0. Fixed-sector Stirling gives
\[
 |A(1/2+iu)|\asymp (1+u)^{7/4}e^{-\pi u/4}\quad(u\ge0).     \tag{1}
\]
The power is 2 from s(s−1) and −1/4 from Γ(1/4+iu/2). A positive minimum on a fixed compact interval supplies the low-height extension. These are the same classical gamma inputs as the existing contour/shadow audits; [DLMF 5.11.1–3](https://dlmf.nist.gov/5.11) and the completion [25.4.4](https://dlmf.nist.gov/25.4#E4) were also checked directly. No zero-free assumption on zeta is involved.

Since |M_L|≤Σ_(d≤L)d^(−1/2)≤2√L, (T) and (1) imply, uniformly in all j≥N−1 and v∈[0,1],
\[
 E^2:=\int_0^T|(Q-\zeta)M_L|^2du
 \le C L N^4(1+T)^{-7/2}e^{-2\pi N^2+\pi T/2},\quad T\ge1. \tag{2}
\]
For the integral estimate, split at T/2: on the second half bound `(1+u)^(−7/2)` by a constant times `(1+T)^(−7/2)` and integrate the exponential; on the first half exponential decay relative to the endpoint absorbs the remaining power. Enlarge the absolute constant on bounded T. This verifies the endpoint factor rather than bounding the entire interval by T times its supremum.

Write J=∫_0^T|QM_L|². The reverse L² triangle inequality and elementary algebra give
\[
 |\sqrt J-\sqrt I|\le E,\qquad |J-I|\le E(2\sqrt I+E),
 \quad J\le2I+2E^2,\quad I\le2J+2E^2.                    \tag{3}
\]
Consequences, all **transfers**:

1. Fixed b<4, T≤bN², L≤T^θ with fixed θ: the error is exponentially small as N grows, up to polynomial factors.
2. Fixed B≥0, T=4N²−B log N, N large: T≍N² and
   `E²/T ≪ L T^(−5/2) N^(−πB/2) ≪ T^(θ−5/2−πB/4)`.
   Thus B>max(0,4(θ−5/2)/π) suffices for normalized L² error tending to zero with a power margin. **The T exponent contains πB/4.**
3. At T=4N², `E²/T≪T^(θ−5/2)`; θ<5/2 gives vanishing normalized L² error. At θ=5/2 it only gives O(1), still enough to transfer an O_ε(T^(1+ε)) bound, if such a bound were proved for one side.
4. For [T,2T], apply (2) at **2T**. The quadratic height condition must cover 2T; replacing it by T loses the exponential budget.

**Correction:** E=o(√T) alone does not imply J−I=o(T). Indeed take √I=T, √J=T+1 and E=1: E²/T→0, but (J−I)/T=2+1/T. An adequate bound on I is also required. With a strict power margin in (2), an all-ε moment bound suffices; with I=O(T), E=o(√T) suffices directly. The relevant algebra and the counterexample identity compiled in Lean.

Applying Bettin–Gonek requires all large real heights, not just T=4N² on an integer grid. One can choose N(T)=ceil(sqrt(T/b)) for fixed b<4 to obtain the uniform *comparison*. A hypothetical approximant moment bound would still need the same uniform L,T quantifiers. No discrete-to-continuous moment bound or long-mollifier estimate is silently assumed.

## 4. L04: coefficient identity, endpoints and analytic domain

Absolute convergence on Re s>1 justifies multiplying the finite mollifier by the zeta series. Its coefficient is
\[
 c_L(n)=\sum_{d\mid n,\ d\le L}\mu(d)(1-\log d/\log L)
 =\mathbf1_{n=1}+\frac{\Lambda(n)}{\log L}
  +\sum_{d\mid n,\ d>L}\mu(d)\left(\frac{\log d}{\log L}-1\right). \tag{4}
\]
Proof: the full divisor sums are Σμ(d)=1_(n=1) and Σμ(d)log d=−Λ(n). The latter follows by expanding the squarefree subsets of the distinct prime divisors: a logarithm of one prime survives only when there is one distinct prime. Subtract the omitted divisors. The sign before the final sum in (4) is **plus**. At n=1 the coefficient is 1; for 2≤n≤L it is Λ(n)/log L; for prime p>L the d=p correction leaves 1. At d=L the taper is zero, so inclusion of that endpoint is harmless. The Lean lemma checks the cutoff algebra given the two explicit divisor identities; it does not formalize μ, Λ or the analytic product.

This identity gives **no convergent critical-line Dirichlet series**. The interpretation of c_L(p)=1 as a literal term of a truncated direct Riemann–Siegel product is false when p>max(L,X): a factorization nd=p has n=1 or d=1 and violates one cutoff. That finite obstruction is Lean-verified with the precise prime factorization property explicit.

## 5. L05: covariance, overlap, Gram matrix and what they cannot prove

For a finite polynomial P(u)=Σ a_n exp(−iu log n), finite sums justify all interchanges. Gaussian integration gives
\[
 \frac1{T\sqrt\pi}\int_{\mathbb R}e^{-(u/T)^2}|P(u)|^2du
 =\sum_{m,n}a_m\overline{a_n}e^{-T^2\log^2(m/n)/4}.          \tag{5}
\]
An unnormalized integral has the factor T√π. A Gaussian centered at u0 additionally has the phase exp(iu0 log(n/m)). Define `S_Δ(v)=Σ a_n 1_`log n,log n+Δ` (historical artifact)`. Intersecting these finite intervals gives exactly
\[
 \frac1\Delta\int|S_\Delta(v)|^2dv
 =\sum_{m,n}a_m\overline{a_n}(1-|\log(m/n)|/\Delta)_+.       \tag{6}
\]
Interval endpoints have zero measure. In the transform convention exp(−iuv),
`hat S_Δ(u)=Δ exp(−iuΔ/2) sinc(uΔ/2)P(u)`.
Plancherel therefore gives `∫|S_Δ|²=(Δ²/(2π))∫sinc²(uΔ/2)|P|²`.
Taking Δ=1/T and using sinc(x)≥1/2 for |x|≤1/2 proves the sufficient, nonoptimal sharp-interval **inequality**
\[
 \int_{-T}^{T}|P(u)|^2du\le8\pi T^2\int|S_{1/T}(v)|^2dv.  \tag{7}
\]
This is not an equality of sharp and triangular kernels. Fourier integration and Plancherel are classical analytic inputs, not Lean formalizations in this pass.

For the candidate's matrix `G_de=(1/T)∫_0^T |ζ|² exp(iu log(e/d))du`, the matrix is Hermitian positive semidefinite. For the real coefficients `α_d=μ(d)(1−log d/log L)/√d`, `I_L/T=α*Gα`. For general complex negative-frequency coefficients a, the vector in this convention is conjugate(a); that conjugation cannot be dropped. Direct expansion proves both statements. Positivity gives a lower bound of zero, not a useful upper bound: positive matrices c·Id have arbitrarily large quadratic forms. Unweighted Möbius variance is a different integral and does not control this zeta-weighted form without an additional correlation estimate.

## 6. L01 and L06: literature applicability, not imported analytic closure

The bounded primary-source check resolves the important distinctions:

| Source/version | Statement actually available | Applicability boundary |
|---|---|---|
| [Matomäki–Pandey–Pliego–Teräväinen–Wang, 2610.09567v1, 7 Oct 2026](https://arxiv.org/html/2610.09567v1), Thm 1.4 | All intervals, untwisted μ; H≥X^(19/35+ε), H≤X; saving `(log X)^(−1/3+ε)` | Not arbitrary logarithmic saving or an unrestricted twisted estimate at 19/35. Its Thm 1.2/Cor 1.3 give arbitrary logarithmic savings with fixed complexity/degree for X^(3/5+ε)≤H≤X^(1−ε). |
| [Matomäki–Radziwiłł–Shao–Tao–Teräväinen, 2411.05770v2, 23 Jan 2026](https://arxiv.org/html/2411.05770v2), Thm 1.1(i), Cor 1.2(i) | H between X^(1/3+ε) and X^(1−ε); arbitrary log saving, fixed-degree polynomial twists, for almost all starting points, with exceptional measure O(X log^(−A)X) and parameter-dependent constants | The phase can depend on the starting point; exceptional points cannot be erased or presumed harmless under ζ weights. At the shorter X^ε scale, the separate result gives ηH-type cancellation, not the same arbitrary log-saving conclusion. The preprint originated in 2024; this is a January revision. |
| [Pliego–Wang, 2610.11487v1, 8 Oct 2026](https://arxiv.org/html/2610.11487v1), Thms 1.1–1.2 | All intervals H≥X^(0.58+ε), uniformly all real linear frequencies; μ sum ≪H(log X)^(−1/3+ε) | Arbitrary log savings in Thm 1.2 have a rational-frequency exception. Do not give its stronger saving to every frequency. |
| [Guth–Maynard, 2405.20552](https://arxiv.org/abs/2405.20552), published Annals 203 (2026) | Prime short-interval consequence with exponent 17/30 (with positive slack), from large-value/zero-density work | A prime statement is not an all-interval Möbius-twist theorem or a zero-free half-plane. |

At X=T^θ the coherence length H=X/T is X^(1−1/θ). Therefore a theorem requiring H≥X^(α+ε) can apply with some positive slack only for θ>1/(1−α). The exact translations are 19/35→35/16, 3/5→5/2, 1/3→3/2, 17/30→30/13, and 0.58=29/50→50/21. Lean checks these implications with θ>0. These are **range conversions, not moment bounds or RH thresholds**; other hypotheses still apply.

An untwisted bound is not useless for all moving twists. On a single coherence interval and |τ|≲T, the total variation of n^(−iτ) is O(1). Abel summation bounds the twisted sum by a constant times the largest untwisted prefix sum. Prefixes shorter than the source's minimum length H0 use the trivial H0 bound; longer prefixes use its cancellation bound. With positive power slack H0/H→0 this yields a local logarithmic saving. Likewise a fixed-degree polynomial theorem can approximate a logarithmic phase locally (linear Taylor error O(1/T) at this scale). Neither deduction establishes the global, zeta-weighted estimate; the almost-all exception and all weights must still be controlled. No prime-coherence-block asymptotic is accepted here.

For modern quasi-RH refinements, [Liu 2610.12234v2, revised 12 Oct 2026](https://arxiv.org/abs/2610.12234v2) reports boundary 0.874957019420098946… with ξ the root in (0.38858,0.38859) of `1188ξ³−2160ξ²+171ξ+190=0` and boundary `(18ξ+7)/(18ξ+9)`. Its optimality claim is confined to its specified exponent-comparison system. It differs from the v1 number 0.874957069799…. [Xu–Sang 2610.15291v2, 15 Oct 2026](https://arxiv.org/html/2610.15291v2), Thm 1.1, explicitly assumes the original analytic inputs and 7/8 conclusion, and reports 0.8748867. These are **external reported results, not locally rebuilt proof inputs**. No new boundary is imported into Project Riemann's accepted bridge. A method-specific limitation is not a universal obstruction. The alleged Guo source and the delta's exact geometry-parameter formula were not identified/checked sufficiently: **NEEDS_EXTERNAL_SOURCE / UNVERIFIED**, not accepted from chat attribution.

## 7. L07–L08: stationary phase and rejected anti-correlation

Here let Q_mol=ζM_L, distinct from the normalized approximant Q in §3, and fix the inner-product convention ∫conj(B)Q_mol. A prime term of B contributes p^(−1/2+iu); the dual zeta term contributes χ(1/2+iu)m^(−1/2+iu); the mollifier contributes μ(d)w_d d^(−1/2−iu). The standard large-positive-u phase of χ is `u−u log(u/(2π))+π/4`. Thus the combined phase is
`φ(u)=u−u log(u/(2π))+u log(pm/d)+π/4`.
It has saddle u0=2πpm/d and φ''(u0)=−1/u0. The −π/4 stationary-phase factor cancels +π/4, leaving exp(2πi pm/d). For a saddle well inside the support, the formal leading amplitude is `sqrt(2πu0)/sqrt(pmd)=2π/d`, times μ(d)w_d and any smooth weight. Its squared algebra is Lean-checked. These ordinary rational phases do not contain modular inverses.

This local calculation is **not a verified global direct/dual/transition decomposition**. Endpoint saddles, sharp cutoffs, all index sums and a uniform remainder still require proof. With the ordinary balanced two-sum zeta error O(u^(−1/4)), explicitly given in [DLMF 25.9.3](https://dlmf.nist.gov/25.9#E3), the absolute mollifier estimate alone gives
`∫_T^(2T)|error·M_L|²du ≪ L T^(1/2)`.
After division by T this is L T^(−1/2); it does not vanish for a long L=T^θ, θ≥1/2. This is a limitation of the available bound, not a lower bound on the true error. One cannot drop that term to prove a long-mollifier claim. The functional equation/Stirling phase is independently reconstructed; no uniform stationary-phase expansion of the complete sum is claimed.

Finally, for any square-integrable Q_mol and B, R=Q_mol−B always implies `〈B,R〉=〈B,Q_mol〉−||B||²`, and Cauchy–Schwarz gives `|〈B,R〉+||B||²|≤||B||||Q_mol||`. This holds for every selected block B. It is not evidence of a special prime anti-correlation. Lean verifies its complex-pair algebra. Both rejected prime-block interpretations remain rejected.

## 8. Verification and preservation

**Eleven new Lean declarations** compile with the existing Lean 4.35.0 toolchain and Std only. Exact source, printed declarations, `#print axioms`, receipt and statement-faithfulness table are in `lean/Consolidation.lean`, `verification/build_20261018T221736284341Z/` and `LEAN_VERIFICATION_REPORT.md`. Only propext, Classical.choice and Quot.sound appear; the prime-factor argument uses only propext and Quot.sound. No custom axioms, unsafe definitions or placeholders occur in the accepted source/closure. The failed first development run is retained and excluded from acceptance. No Real/Complex integration, μ/Λ definition, zeta theorem, stationary-phase theorem or asymptotic limit was formalized.

The eight existing accepted Lean runs cover 119 declarations. Their pinned sources, complete accepted logs, actual declaration signatures and transitive axiom listings were inspected; `verification/PRIOR_LEAN_CHECK.json` records consistent source hashes and no unexpected axioms. They were **not recompiled**. This does not promote their analytic premises to formal theorems. No full numerical certificate, old 420-member archive check or external quasi-RH build was run.

Only this new workspace was written. All 59 original source pins and all 12 extracted packet members match; HEAD, branch, tracked state and service fields are unchanged. The full-ref comparison **does not match**: one new `historical-capture-reference` reference appeared, pointing to `e97c8bddb073f70332b872c54a0c05451c1c7784`. No pre-existing ref changed or disappeared. The namespace is consistent with app capture bookkeeping; its creator was not independently identified. This discrepancy is not waived or removed. `PRESERVATION_REPORT.md` and `verification/PRESERVATION.json` preserve the exact comparisons. No service was restarted; no Git mutation command, installation, publication, email or paid action was performed. SHA256SUMS is a byte-integrity seal, not a proof or cryptographic signature.

## 9. Single unresolved proof-critical obligation and stop

For the **actual** Xi_k, prove independently of RH that for some fixed b∈(0,4), every sufficiently large k has no zero in
\[
 0\le\Re z\le b(k+1)^2,\qquad 1/k\le|\Im z|\le1/2.
\]
The quadratic-shadow audit proves the equivalence for each fixed b, including multiple possible Xi zeros. The criterion's proof does not establish the criterion. A sufficient signed-moment route still lacks its zeta-weighted estimate with the necessary uniform quantifiers and remainders. Selected total counts, density one, shadowing, positive kernels, descent of an artificial branch and algebraic transfers do not close this gap.

This consolidation is complete and stops here. No controller or follow-on mathematical campaign is running. A future authorized session should start with updated handoff 01, 02 and 05 and require a genuinely new premise before reopening a closed route.
