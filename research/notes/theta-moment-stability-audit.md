> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `63d74476acce1c0509ae316b3e0e373a2ac3dad293a3592d6cc613dda4f0893f`.

# Project Riemann — Theta moment/Jensen normalization and heat-flow falsification audit

Date: 2026-10-19 (research checkpoint). Branch: **nature-inspired zero-stability / arithmetic Xi**.

**Overall decision: `NO_NEW_RH_FRONTIER_ADVANCE`. No new Xi zero-exclusion inequality.** The raw-moment/Jensen identification tested below is false, and the newly advertised single-off-line-zero heat-flow inequality cannot contradict any possible off-line zero using established upper bounds, even if granted its as-yet-unverified proof.

**Scope:** All new analysis is in this document. The authoritative October 19 ZIP, earlier audit, Haglund k=2/k=3 artifacts, Git references, SHA evidence, and Codex processes were not modified. No Codex was started; no packages or Lean were installed. `lean` and `lake` were not installed in the current container. Symbolic algebra and numeric checks are ancillary; elementary analytic proofs are written, NOT Lean-certified. No new RH proof is claimed.

## 1. Inputs / provenance

1. Original handoff: `Project_Riemann_Complete_Handoff_20261019(1).zip`, read-only extracted for research under `/tmp/riemann_20261019_handoff_readonly`. The README, authority, research rules, historical log, post-consolidation ledger, no-go/error register, nature brief, literature register, bundled-artifact integrity guide, and claim register were consulted. Standing states: RH open, complete Haglund k=2/k=3 unverified, historical provenance `BLOCKED_UNWAIVED`, latest Codex `BLOCKED_NEW_MOMENT_ESTIMATE`.
2. Previous distinct investigation: `LOCAL_ARCHIVE/NATURE_HEAT_FLOW_AUDIT.md`: local heat-time persistence of any hypothetical nonreal Xi zero, and failure of a uniform absolute-error transfer at high ordinate.
3. Primary 2019 Griffin–Ono–Rolen–Zagier (GORZ), *Jensen polynomials for the Riemann zeta function and other sequences*, PNAS 116 (2019), 11103–11110, https://pmc.ncbi.nlm.nih.gov/articles/PMC6561287/ . Its Eq. (1) defines the Jensen sequence using **exponential coefficients** `gamma(n)/n!`; it proves degree <=8 for all shifts and eventual hyperbolicity for each fixed degree.
4. M. Planat, *Asymptotic Hyperbolicity of Jensen Polynomials and the Finite-Strip Obstruction for the Riemann Hypothesis*, posted preprint v2 2026-04-20, https://www.preprints.org/manuscript/202604.1239 (journal metadata indicates *Mathematics* 2026, 14(11), 1884). The v2 HTML was inspected directly; conclusions below target the **displayed definitions in v2**, not an unseen journal revision. Its Section 1.2 asserts a raw theta moment equals its Taylor coefficient and its Jensen coefficient, and its Remarks 2–3 simultaneously assert no quadratic real zeros at any shift and eventually hyperbolic quadratic Jensen polynomials. Its Section 1.1 displays only the n=1 theta term `Phi_1(u)` as an alleged full Xi kernel.
5. W. Michałowski, *An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann ξ-coefficients*, arXiv:2607.16795, https://arxiv.org/abs/2607.16795 . This independent 2026 manuscript specifies the **full theta sum** and the crucial normalization `a_n=M_n/Gamma(2n+1)`. Its asymptotic PF wedge is an externally reported, unverified new result and expressly does not establish RH.
6. W. Michałowski, *On the Pólya Frequency Order of the de Bruijn–Newman Kernel: Certified Failure at Order Five*, arXiv:2602.20313v2 (2026-07-20), https://arxiv.org/abs/2602.20313 . Abstract reports a certified negative 5-by-5 Toeplitz determinant for **continuous** theta kernel, and explicitly withdraws an erroneous stronger v1 conclusion. Source report NOT independently re-run; do not conflate kernel PF5 with coefficient PF hierarchy.
7. P. Caceres, *How long can an off-line zero survive the de Bruijn–Newman heat flow?*, Hexagon version 1, 2026-10-12, https://hexagonmath.org/2610.00207v1 ; source https://hexagonmath.org/api/v1/works/2610.00207v1/source?path=Caceres_DBN_OfflineZero.tex . Theorem advertises a lower bound on Λ from any hypothetical off-line zero. This is an unreviewed preprint and its uniform numerical premises have **not** been independently certified.
8. Tao/Polymath RH database on Λ, https://teorth.github.io/expdb/blueprint/debruijn-newman-chapter.html : the actual theta Fourier representation, heat normalization, Rodgers–Tao Λ >= 0, upper bound Λ <= 0.22 (Polymath 2019) and improved Λ <= 0.2 (Platt–Trudgian 2021).

## 2. Exact representation of actual Xi and coefficient normalization

Let `xi(s)` be the completed zeta function. Define `H_0(z) = xi(1/2 + iz/2)/8` and `Xi(z) = xi(1/2 + iz)`; then **Xi(z) = 8 H_0(2z)**. The legitimate classical Fourier representation is

    H_0(z) = integral_{0}^{infinity} Phi(u) cos(z u) du,
    Phi(u) = sum_{m>=1} [2*pi^2*m^4*exp(9u) - 3*pi*m^2*exp(5u)]*exp(-pi*m^2*exp(4u)).

Every summand is strictly positive for `u>=0` because `[2*pi*m^2*exp(4u)-3]>0`. Phi is strictly positive on every positive interval, and superexponentially decays as `u->infinity`. All moments `M_n = integral Phi(u) u^{2n} du` exist, are positive, and form a strict log-convex sequence `M_{n+1}^2 < M_n M_{n+2}` by the **strict** Cauchy–Schwarz inequality (non-point-support measure).

Write

    H_0(z) = sum_{n>=0} (-1)^n [M_n/(2n)!] z^{2n}.

For the ordinary generating entire function `G(x)=H_0(i sqrt(x))` (the square root notation is harmless because H_0 is even),

    G(x) = sum_{n>=0} [M_n/(2n)!] x^n
         = sum_{n>=0} [gamma_n/n!] x^n,     gamma_n = n! M_n/(2n)!.

The three quantities are **different**: raw moment `M_n`, ordinary Taylor coefficient `c_n=M_n/(2n)!`, and Jensen exponential coefficient `gamma_n=n!M_n/(2n)!`. Passing from H_0 to Xi introduces common factor `8` and geometric factor `4^n`, which preserve Jensen hyperbolicity after positive rescaling of the polynomial variable. It does not repair an absent factorial.

Independently, the Planat preprint's printed positive kernel `Phi_1(u)=2*pi*(2*pi*exp(4u)-3)*exp(5u-pi*exp(4u))` is **two times the first summand** of the actual H_0 theta kernel, not the full infinite theta series; terms `m>=2` are positive, nonvanishing on all `u>=0`. Even allowing overall constant and argument normalization, the displayed single-term identification is not the actual Fourier kernel. The raw Jensen error persists regardless of whether one uses full Phi or the first summand.

## 3. General theorem: raw positive-moment Jensen polynomials have at most one real zero

**Theorem (elementary, complete, no RH input).** Let `mu` be a nonzero finite positive Borel measure on `(0,infinity)` with moments `M_j=int t^j dmu(t)` finite and strictly positive for all `j>=0`. Suppose `mu` is not supported on a single point. For every integer `n>=0` and `d>=1`, define

    P_{d,n}(X) = sum_{j=0}^{d} binomial(d,j) M_{n+j} X^j
               = integral t^n (1+t X)^d dmu(t).

If d is even, `P_{d,n}(x)>0` for every real x, so P has **zero** real zeros. If d is odd, `P_{d,n}` has **exactly one simple real zero** (in fact, negative) and its remaining `d-1` zeros are nonreal when d>1.

**Proof.** Binomial expansion and moment finiteness give the integral formula. For even d, the integrand is everywhere nonnegative for real x, and vanishes only at the single point `t=-1/x` (if x<0). The measure is not supported at this point; hence the integral is strictly positive. For odd d,

    P'_{d,n}(x) = d * integral t^{n+1} (1+t x)^{d-1} dmu(t) > 0,

because d-1 is even and the support is not a singleton. The polynomial has odd degree d and positive leading coefficient `M_{n+d}`; hence tends to `-infinity` and `+infinity` as x tends to the respective infinities, has precisely one root by strict monotonicity, and has nonzero derivative there. Since P(x)>0 for x>=0, that root is negative. QED.

Specialize to the theta kernel by `t=u^2` and `dmu(t)=Phi(sqrt(t))dt/(2 sqrt(t))`: the hypotheses hold. This is an **all n, all degree** exact theorem; numerical root sweeps and a claimed parity-frozen range are not needed. For d=2, it is equivalent to the negative discriminant `4(M_{n+1}^2-M_n M_{n+2})<0`. For all even d>=2 the raw-moment P is NOT hyperbolic (unless d=0); for all odd d>=3 P is NOT hyperbolic. In contrast, true Jensen polynomials have the factorial-normalized `gamma_n` and are proven eventually hyperbolic by GORZ.

**Caveat:** For a single-atom measure `mu=delta_a`, `P=(a^n)(1+a X)^d` has all d real roots equal to `-1/a`. This is why the non-single-atom assumption is essential; both the full theta kernel and the first theta summand satisfy it.

**Adversarial relevance:** This theorem immediately contradicts the identification `gamma_n=M_n` together with any claim that these *same* raw-moment polynomials become hyperbolic at large n for d>=2. The preprint's admission of a negative d=2 discriminant cannot coexist with its invocation of GORZ eventual hyperbolicity for that misnormalized family. This is an issue with the specified paper, **not a disproof of RH or GORZ**. We have not verified whether the later published journal text has corrected it.

## 4. The corrected quadratic and Gaussian test

With `gamma_n=n! M_n/(2n)!`, an exact cancellation of factorial factors yields, for n>=0,

    gamma_{n+1}^2/(gamma_n gamma_{n+2})
      = ((2n+3)/(2n+1)) * [M_{n+1}^2/(M_n M_{n+2})].

Therefore the actual degree-two Jensen polynomial has nonnegative discriminant precisely when

    M_{n+1}^2/(M_n M_{n+2}) >= (2n+1)/(2n+3).

Cauchy–Schwarz supplies *only* the strict upper bound `M_{n+1}^2/(M_n M_{n+2})<1`; it provides no lower bound of the required strength. This is why raw positivity/log-convexity cannot be imported as RH proof. The actual Xi degree-two hyperbolicity is already contained in GORZ (degree<=8 for all n), so the displayed necessary-and-sufficient inequality provides **no new Xi claim**.

**Gaussian sharpness:** For `Phi_G(u)=exp(-a u^2)`, `a>0`,

    M_n^G = Gamma(n+1/2)/(2 a^{n+1/2}),
    (M_{n+1}^G)^2/(M_n^G M_{n+2}^G) = (2n+1)/(2n+3).

In fact, `G_G(x)=(sqrt(pi)/(2sqrt(a))) * exp(x/(4a))` and its Jensen polynomials are positive multiples of `(1+X/(4a))^d`: all zeros are the same real negative number. The Gaussian sits **exactly at the quadratic boundary**. A generic positive-mixture or Gaussian-analogy argument alone cannot generate the strict theta-specific margin; and establishing the degree-two margin still does not address higher-degree constraints or off-real Xi zeros.

**Symbolic regression:** SymPy exact-rational reduction confirmed

    ((n+1)/(n+2)) * ((2n+4)*(2n+3))/((2n+2)*(2n+1))
    == (2n+3)/(2n+1).

This is an exact algebra check, not Lean compilation.

## 5. Latest single-zero-sensitive heat-flow proposal: the bound is quantitatively vacuous

The 2026-10-12 Caceres Hexagon preprint states an unconditional theorem: if a nontrivial zeta zero occurs at `s=1/2+delta+i gamma` with `gamma>=3*10^12` and `0<delta<1/2`, then

    Lambda >= delta^2/[70 * log(gamma) * log(log(gamma))].

This has the virtue of targeting **one** hypothetical off-line zero and using the actual H_t heat flow. Nevertheless the proof has not been accepted as a certified unconditional theorem here: its Lemma C evaluation uses 18 sample heights and 721 angular grid points, explicitly calls itself *not an interval-arithmetic proof*, and its global constant uses further finite grids. To make it fully rigorous, it must supply proven coverage of all between-grid extrema and roundoff/truncation, or equivalent analytic monotonicity/derivative bounds. That gate has not been audited or cleared. The sharper linear-lifetime variant imposes local spacing/isolation assumptions; those must not be silently assumed for an arbitrary hypothetical zero.

**More decisive, grant its theorem fully and test the claimed consequence:** the rigorously established bound `0 <= Lambda <= 0.2` combines to give

    delta <= sqrt[70*(0.2)*log(gamma)*log(log(gamma))].

At the smallest height not covered by certified RH verification, `gamma=3*10^12`,

    log(gamma) = 28.729633404596658
    log log(gamma) = 3.357929112888788
    product = 96.47207241191735
    RHS delta bound = 36.7506328349165.

But any hypothetical **nontrivial** off-critical zeta zero is in `0<Re(s)<1`, so `delta<1/2`. Thus the obtained bound is **more than 73 times wider than the whole critical strip** and becomes weaker as gamma increases. For maximally unfavorable hypothetical `delta=1/2` at this height, the theorem would force only

    Lambda >= (1/4)/(70*96.47207241191735)
           = 0.0000370203363744406,

while present established upper bound is 0.2, a factor `5402.436...` larger. Even ruling out the maximally displaced hypothetical zero at the *lowest possible* height would require an independent strict upper bound `Lambda < 3.70204 * 10^-5`—and ruling out zeros arbitrarily close to the critical line or at arbitrarily large heights requires a far sharper result. A suggested 2026 *conditional* upper near 0.1486 would still be thousands of times too weak.

The no-go is therefore independent of whether the Caceres preprint's derivation can ultimately be certified: **it cannot presently exclude one hypothetical off-line Xi zero**. Do not launch Codex to optimize these constants by small factors.

## 6. PF∞ check: do not conflate different kernels

The published/claimed negative 5×5 Toeplitz determinant at specific nodes in arXiv:2602.20313v2 concerns total positivity of the **continuous function** `u -> Phi(|u|)`. Even if reproduced, it neither falsifies RH nor determines all finite Toeplitz minors of the separate factorial-normalized coefficient sequence of `G`. Thus Lee–Yang / PF∞ positivity of the *unmodified continuous theta kernel* is not a viable unconditional shortcut on current evidence. A positive Fourier theta kernel by itself was already refuted as a sufficient criterion by the older project countermodels.

## 7. Decision, proof obligations, stop condition

- `PROVED_WITH_STATED_CLASSICAL_INPUTS`: raw-moment polynomial root-count theorem for all shifts/degrees and any positive non-point-supported measure, exact normalization algebra, Gaussian threshold identity, and numerical vacuity of the advertised heat lifetime bound after combining it with **known** upper bounds.
- `LITERATURE_REPORTED_NOT_INDEPENDENTLY_REPRODUCED`: GORZ theorem, Platt–Trudgian upper bound, certified PF5 counterexample (v2); standard, well-defined sources but not newly formally checked here.
- `PREPRINT_UNVERIFIED`: Caceres claimed lower bound, its uniform continuum numerical verification, Planat journal paper consistency beyond the inspected online v2, Michałowski PF wedge technical proof.
- `NOT ESTABLISHED`: any new noncircular Xi-specific signed-correlation estimate, any proof that an off-real zero cannot exist, or any complete Haglund k2/k3 proof.
- `TOOLS`: Web source/primary text inspection, elementary exact proof, Python/SymPy symbolic identities, ordinary arithmetic. **Lean 4 unavailable; zero Lean declarations compiled in this investigation.** No Codex run, no broad computing sweep, no update to previous artifact, no publication.

**Research stop:** CLOSE raw-moment Jensen/Lee–Yang positivity and the current heat lifetime constant as routes to excluding even one hypothetical Xi zero. Their mathematical failure is structural, not a tunable parameter problem. A NEW campaign would require a truly independent, Xi-specific arithmetic constraint which either (i) controls the cancellation in Xi or (ii) yields a uniformly sufficiently strong bound connecting **one** off-real zero to a quantity already known to be smaller, without implicit RH or proof-equivalent premises. None identified in this investigation. Do not accumulate auxiliary inequalities absent that gate.

**Project-wide state unchanged:** RH OPEN; complete Haglund k=2/k=3 UNVERIFIED; latest Poisson/moment gate `BLOCKED_NEW_MOMENT_ESTIMATE`; historical references/provenance `BLOCKED_UNWAIVED`. All previous artifacts stay archived.
