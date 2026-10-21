> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `c6d4d8c59d45195c8320bdb89028af52f2321a219c5c55d102c043dcaeab5376`.

# Project Riemann — prime-classification and RH-falsification gate

**Date:** 2026-10-19. **Verdict:** NO_NEW_RH_FRONTIER_ADVANCE. This is a bounded audit and a practical correction to the research strategy, not an RH proof, disproof, or novelty claim. RH, complete Haglund k=2/k=3, and historical provenance retain their previous classifications: RH OPEN, complete k=2/k=3 UNVERIFIED, provenance BLOCKED_UNWAIVED.

## 1. Evidence separated by status

**Prior project, reused and NOT re-proved here.** The October-18 single-pass consolidation, corrected six-file audit ledger, theta tail bound, contour-transfer argument, exterior estimates, quadratic shadowing and density report. The basic uniform approximation under review is

`|Xi(z) - Xi_k(z)| <= V_N := 64 N^2 exp(-pi N^2)`, `N=k+1 >= 2`, `|Im z|<=1/2`.

This uniform analytic tail estimate is a documented project input, not newly Lean-checked here. The k=27 proposed violation of Haglund's *ordering* conjecture remains REPORTED_NOT_REPLAYED and is not a refutation of RH or Haglund's motion conjecture. The proposed pair-correlation transfer remains a separate unverified candidate; even if correct its asymptotic proportion does not eliminate fixed exceptions.

**External published/reported material.** Platt–Trudgian's interval-certified verification through height 3e12; OpenAI's reported and externally checked Lean 7/8 nonvanishing result (not locally rebuilt, so apply at its stated external scope only); Lamzouri's reported 2026 lower proportion 67.25%; and established Dirichlet-character orthogonality. Their proofs have NOT been locally reproduced for this audit.

## 2. Exact principal-mode obstruction for classifying primes by residue

Let `q>=2`, `g=phi(q)`, and `psi(x;q,a)=sum_{n<=x,n=a mod q} Lambda(n)` for each unit residue a mod q. Let `psi(x,chi)=sum_{n<=x}Lambda(n)chi(n)` and `chi_0` be the principal Dirichlet character modulo q. Character orthogonality gives, exactly for every x,

`psi(x;q,a) = (1/g) sum_{chi mod q} conj(chi(a)) psi(x,chi)`.

Writing `U_q(x)=psi(x,chi_0)=psi(x)-sum_{p|q}sum_{m>=1,p^m<=x}log(p)`, this becomes

`psi(x;q,a) = U_q(x)/g + (1/g) sum_{chi != chi_0}conj(chi(a))psi(x,chi)`.

The excluded prime powers contribute at most `omega(q)*log x` for fixed q. The vector of class counts decomposes into a common **principal** component `(U_q(x)/g) * (1,...,1)` and a sum-zero **nonprincipal** component. Thus ALL pairwise class differences annihilate the principal term identically. A theorem that controls only pairwise differences cannot by itself bound the principal error `psi(x)-x`, whose square-root error is RH-equivalent. A theorem that instead bounds the absolute errors of every class by `O(x^(1/2+epsilon))` would, upon summation, directly supply the missing RH-strength bound rather than avoid it.

**Explicit q=4 identity** (every x):

`psi(x;4,1) = [psi_odd(x)+psi_chi4(x)]/2`, 
`psi(x;4,3) = [psi_odd(x)-psi_chi4(x)]/2`, 
`psi(x;4,1)-psi(x;4,3)=psi_chi4(x)`, 
`psi(x;4,1)+psi(x;4,3)=psi(x)-floor(log_2(x))*log(2)`.

The last formula includes prime powers, not only primes. The q=4 indicator identities were independently checked with exact rational arithmetic for all integers 1 through 2000 (2000/2000 pass). This is a consistency check, not formalization of Dirichlet-character theory.

**Adversarial nonlinear check.** `chi(n)*conj(chi(n))=1` for units n; putting a character and its conjugate together simply recovers the principal weight. Positivity of the square does not give any additional cancellation in `U_q`. Nonlinear statistics might offer a different method ONLY when accompanied by an independently proved off-diagonal arithmetic cancellation inequality. Standard quadratic recombinations alone are not such an estimate.

**Disposition:** fixed-modulus linear classifications and their elementary quadratic lifts are CLOSED AS SHORTCUTS. This does not exclude adaptive or deeper prime classifications that genuinely prove a new cross-mode arithmetic inequality.

## 3. One finite certificate that would truly disprove RH

This is an independent elementary sufficient condition, not an RH-equivalent conjecture. Let `F=Xi_k`, `N=k+1`, and choose a center `c=x+iy` in the first quadrant with `0<y<1/2`. Choose `r>0` with the entire closed disk `D={|z-c|<=r}` contained in `Re z>0`, `0<Im z<1/2`. Let an RIGOROUS upper bound `M2 >= sup_{z in D}|F''(z)|` be available. If one verifies by interval/ball arithmetic that

`|F(c)| + (M2*r*r)/2 + V_N < r*|F'(c)|`,

then there is exactly one ZERO OF THE GENUINE Xi in D (counted with multiplicity), so RH is FALSE.

**Proof.** Taylor's theorem along the complex line from c to z bounds `|F(z)-F(c)-F'(c)(z-c)| <= M2*r^2/2` for |z-c|=r. The documented tail gives `|Xi(z)-F(z)|<=V_N`. Hence `|Xi(z)-F'(c)(z-c)| <= V_N+|F(c)|+M2*r^2/2 < r|F'(c)|` on the circle. Rouché compares Xi with the one-zero linear function `F'(c)(z-c)`. Since the disk is disjoint from the real axis, that Xi zero would refute RH. The inequality is STRICT, and every numeric operand must have a certified enclosure.

A possible positive integral for M2 uses the actual theta kernel:

`M2 <= 4 sum_{n<=k} integral_0^infty u^2 h_n(u) cosh(Y u) du`, where `Y=max_{z in D}|Im z|` and `h_n>=0` for n>=1. The bound is finite; its numerical computation is not performed here.

**Feasibility gate.** The rigorous Platt–Trudgian verification already excludes any such off-axis certificate below `T0=3,000,175,332,800`. If seeking beyond T0 while keeping an approximant center in the effective quadratic window `x<bN^2`, the necessary lower bound on N is enormous: for `b=4`, `N>=866051` (`k>=866050`); for `b=3.9`, `N>=877084`; for `b=3`, `N>=1000030`. These thresholds were verified with exact integer comparisons. Since the audited strong estimates require fixed `b<4`, the first is an optimistic absolute limit, not an admissible choice of b. This defeats broad inexpensive sweeps of small Haglund truncations as a route to a NEW RH counterexample. It does not disprove RH or preclude other analytic falsification methods, including rigorous direct zeta evaluation.

## 4. What remains a genuinely new research contribution?

A proof-critical advance must accomplish one of the following:

1. A new unconditional prime/Hecke cancellation inequality with a nonzero principal-mode projection that improves the proved zero-free half-plane of the genuine zeta function beyond the existing published/reported boundaries; or
2. A rigorously certified off-critical-line zero of Xi, for example by the finite disk certificate above, beyond the verified height; or
3. An independently proved, uniform inner zero-exclusion inequality for the actual Xi_k that discharges the prior quadratic-shadow frontier rather than restates RH.

Another counting equivalence, positivity of a transformed kernel, improvement to an asymptotic fraction, or a zero-free conclusion under an RH-equivalent hypothesis fails this acceptance test. A new prime classification must provide **an explicit cross-mode arithmetic estimate** with all uniform parameters; merely renaming residues, characters, or eigenmodes does not qualify. No such estimate was discovered in this bounded review. We do NOT start another Codex campaign on the present evidence.

## 5. Sources and provenance

- Project handoff supplied by the user: `FINAL_CONSOLIDATION_REPORT.md`; `03_MATHEMATICAL_CLAIM_LEDGER.md`; existing `Project_Riemann_Pair_Correlation_Transfer_20261018.md` (unverified candidate).
- James Haglund (2009): https://arxiv.org/abs/0910.5228.
- Platt and Trudgian, *The Riemann hypothesis is true up to 3 * 10^12*: https://arxiv.org/abs/2004.09765.
- OpenAI math quasi-RH comparator/solution documentation (reported 7/8): https://github.com/openai/math/blob/main/lean/docs/003.md.
- Dirichlet character orthogonality: https://encyclopediaofmath.org/wiki/Dirichlet_character.
- Prime-class Chebyshev character decomposition (journal treatment): https://academic.oup.com/qjmath/article/74/4/1505/7240642.
- Rodgers and Tao, de Bruijn–Newman perspective: https://terrytao.wordpress.com/2018/01/19/the-de-bruijn-newman-constant-is-non-negativ/.

**Lean:** unavailable in the current isolated runtime (`lean`, `lake`, `elan` not installed); no claim in this report is labeled Lean-checked. **Repository preservation:** no original local/WSL project files, services, evidence, Git refs, certificates, or manuscripts were accessed for modification. This report alone was created under `LOCAL_ARCHIVE/data`.
