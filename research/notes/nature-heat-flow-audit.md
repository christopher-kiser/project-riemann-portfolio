> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `66a8e1a8fee0907a09db089e858043123c1483f2df410cfd5be643c6e45ce502`.

# Project Riemann — bounded nature-mechanism audit

**Date:** 2026-10-19  
**Independent outcome:** `NO_NEW_RH_FRONTIER_ADVANCE`; finite-time contraction as a stand-alone RH route is **CLOSED**; the elementary absolute heat-transfer gate also fails at unbounded height.  
**Preserved statuses:** RH OPEN; complete Haglund Conjecture 4 for k=2 and k=3 UNVERIFIED; 2026-10-19 marked-inverse audit `BLOCKED_NEW_MOMENT_ESTIMATE`; historical provenance `BLOCKED_UNWAIVED`.  
**Scope:** New research only. No original archive, Git ref, service, Codex session, or old workspace changed.

## 1. Bounded source screening

- Hilbert–Pólya: Y. Shi, *Construction of Finite Hilbert–Pólya Matrices from Weil's Explicit Formula*, arXiv:2609.04908, explicitly uses known ordinates as inputs in its reconstruction and reports no RH proof. It does not provide an independent exact spectral determinant of the actual Xi function. https://arxiv.org/abs/2609.04908
- Lee–Yang: T. Konstantopoulos, P. Patie, R. Sarkar, *A new class of solutions to the van Dantzig problem, the Lee–Yang property, and the Riemann hypothesis*, Annales de l'Institut Fourier 74 (2024), 377–421. Relates the Xi real-zero property to the Laguerre–Pólya / Lee–Yang framework, but does not prove the missing membership. Y. Kozitsky, arXiv:2603.18675, proves Lee–Yang theorems for specified ferromagnetic models, not for a representation of Xi. https://www.numdam.org/articles/10.5802/aif.3600/ ; https://arxiv.org/html/2603.18675
- Heat flow: Rodgers–Tao, arXiv:1801.05914v5 (2021 revision), proved the lower bound Lambda>=0. D. H. J. Polymath, arXiv:1904.12438, proved Lambda<=0.22. M. Planat, arXiv:2609.37164v1, proposes collective contraction and an audit-relative numerical refinement. M. Planat, arXiv:2610.18214v1 (13 October 2026), reports Lambda<=0.148611789321711 conditional on explicit A1–A3 analytic interfaces; its own Theorem 1.1 says the end-to-end source-to-true-function assembly remains to be validated, so that number is NOT imported here as an unconditional bound. https://arxiv.org/abs/1801.05914 ; https://arxiv.org/abs/1904.12438 ; https://arxiv.org/html/2609.37164v1 ; https://arxiv.org/html/2610.18214

**Decision:** Heat flow was selected because the deformation acts on *exact Xi* with no arbitrary normalizer, whereas the available Hilbert–Pólya and Lee–Yang bridges do not establish the required exact realization.

## 2. Exact matching to Project Riemann's theta normalization

Let `a_n=pi*n^2` and `h_n(u)=a_n*exp(5u/2-a_n*exp(2u))*(2a_n*exp(2u)-3)` for `u>=0`, so `Xi(z)=4 sum_n integral_0^infty h_n(u) cos(zu) du`.

Define the **genuine** heat deformation (not an arbitrary model):

`X_t(z) = 4 sum_{n>=1} integral_0^infty h_n(u)*exp(t*u^2/4)*cos(z*u) du`.

Under `u=2v`, Polymath's kernel satisfies `h_n(2v)=(2*pi^2*n^4*exp(9v)-3*pi*n^2*exp(5v))*exp(-pi*n^2*exp(4v))`. Therefore `X_t(z)=8*H_t(2z)`, `X_0(z)=Xi(z)` and

`partial_t X_t(z)=-(1/4)*partial_z^2 X_t(z)`.

Zeros of `H_t` are real if and only if zeros of `X_t` are real. A hypothetical off-real Xi zero corresponds to an off-real zero of the standard `H_0` at twice the coordinate. All statements here use the genuine theta kernel for every `n`, not a truncated or modified analogue.

## 3. Exact proof-critical candidate and falsification

**Candidate HC-01 (tested, not proved):** A positive collective zero-interaction/contraction field for `X_t`, possibly combined with Jacobi theta self-duality, forces the entire zero set onto the real axis at `t=0` from estimates established at some `t>0`. This would imply Lambda<=0 and RH, but the implication needs a genuinely independent time-zero premise, not just a finite positive-time landing estimate.

### Quantitative local-persistence theorem (proved with classical entire-function inputs)

**Statement.** Suppose that genuine `Xi` has a zero `z_0` with `Im(z_0) != 0`, of *any* finite multiplicity. Choose `r>0` so that the closed disk `D={z: |z-z_0|<=r}` does not intersect the real axis and Xi has no zeros on the boundary. Put

`B=|Im z_0|+r`, `m_D=min_{|z-z_0|=r}|Xi(z)|>0` and

`M_B = sum_{n>=1} integral_0^infty u^2*h_n(u)*exp(u^2/4)*cosh(B*u) du`.

Then `0<M_B<infinity`, and for every `0<=t<=d=min(1,m_D/(2 M_B))` the *genuine* `X_t` has the same positive number of zeros in `D` as Xi, counted with multiplicity. In particular, `H_t` still has a nonreal zero for the entire interval `[0,d]`, and its de Bruijn–Newman constant obeys `Lambda>d>0`.

**Proof.** Because `u>=0`, `a_n>=pi` and `2 a_n exp(2u)-3>0`, every `h_n(u)>0`. The super-exponential theta decay makes `M_B` finite. For `z in D`, the inequality `|cos(zu)|<=cosh(Bu)` and `0<=t<=1` imply

`|partial_t X_t(z)| <= M_B`.

Thus `sup_{partial D}|X_t-X_0|<=t*M_B<=m_D/2<m_D`. Rouché's theorem gives an unchanged positive zero count in `D`, for every `t` in the stated interval. All such zeros are off-real because `D` was chosen disjoint from `R`. Since all zeros of `H_t` are real if and only if `t>=Lambda` (de Bruijn/Newman), `Lambda>d`. QED.

**Why this matters:** It is a direct, quantitatively explicit test on the authentic infinite theta series and handles multiple zeros. Finite-rate forward contraction is fully compatible with a hypothetical single off-real zero at time zero. Such a zero would simply survive for some (possibly very short) positive time; even an improved bound `Lambda<=0.1486` would not contradict this without a *lower* bound on its personal survival time exceeding the purported upper bound.

### Exact algebra check of the newer collective-contraction inequality

The factorization from Planat (arXiv:2609.37164v1, Theorem 2.1), for real `d`, `y>0`, `0<=v<=y`, is

`(y-v)/(d²+(y-v)²) + (y+v)/(d²+(y+v)²) - 2y/(d²+4y²)`

`= 2y*(y²-v²)*(3d²+v²+3y²)/((d²+4y²)*(d²+(y-v)²)*(d²+(y+v)²)) >=0`,

away from singular denominators. **Independently verified exactly with SymPy**: the fully simplified difference was zero. The sign follows from factors for `0<=v<=y`. This is **EXACT_SYMBOLIC_ALGEBRA_CHECKED**, not Lean-checked, not independent verification of the cited article's analytic or interval claims.

The mathematical direction is decisive: the strongest stated implication is `d(y²)/dt <= -2 - 4G_t*y²`, which supplies an **upper bound for landing time at positive t**. It does *not* supply the missing `y(0)=0`. Such a conclusion requires an additional bound applicable all the way to the heat-time-zero boundary and ruling out the local-persistence theorem's positive time interval. Positivity of `G_t` alone cannot do that.

### Alternative local check for a simple off-real zero

At a simple zero `z_0` of `Xi`, the implicit-function theorem gives an analytic zero branch `z(t)` of `X_t` with

`z'(0)=Xi''(z_0)/(4*Xi'(z_0))`.

This is finite; hence `Im z(t)` retains the nonzero sign of `Im z_0` for all sufficiently small `t>0`. This simple-zero check agrees with the multiplicity-safe Rouché result.

### Secondary falsification: transfer from the proven `Lambda <= 0.22` bound

There is a rigorous **sufficient local zero-exclusion criterion**, but it fails as a uniform infinite-height strategy. Since Polymath proved the genuine `X_0.22` has only real zeros, the bound `|X_0.22-X_0| <= 0.22*M_B` and Rouché give:

> **Conditional disk criterion (proved with stated classical/external inputs):** If `D` is any closed disk strictly off the real axis and with `m_D=min_{partial D}|Xi|>0`, and if `m_D > 0.22*M_B`, then `Xi` has **no zeros** in `D`. The proof uses Rouché to transfer zero count from `X_0.22`, which has none there.

This criterion is genuinely source-specific and excludes any hypothetical zero in a disk meeting its strict numerical gate; **no disk is shown to meet the gate** in this audit. Crucially, it does *not* provide the uniform exclusion required for RH. Fix `0<r<|y_0|` with `B=|y_0|+r<1/2`, and translate a disk `D_x={|z-(x+i y_0)|<=r}` to `x->+infinity`. Since `Xi(z)=xi(1/2+i z)`, the standard vertical-strip polynomial bounds for zeta and Stirling's formula imply

`sup_{z in partial D_x} |Xi(z)| <= C_(B,r) * (1+x)^A * exp(-pi*x/4)`

for some fixed constants `A,C_(B,r)>0`, for all sufficiently large x. In particular `m_(D_x)->0`, whereas `M_B>0` is **independent of x**. Therefore `m_(D_x)>0.22*M_B` fails for all sufficiently high translated disks. The absolute theta-integral heat-error loses the `exp(-pi*x/4)` oscillatory cancellation that the genuine Xi exhibits. The proof-critical missing estimate would have to be *phase-sensitive*, and survive the large-height limit; a uniform absolute kernel norm cannot supply it.

**Classification:** The local disk exclusion is a proved implication using Polymath's independently published real-zero theorem at t=0.22, but it verifies **no nontrivial new zero-free region** in this audit. Its large-height failure is mathematically proved and does not reject more delicate cancellation-aware heat-flow approaches.

## 4. Explicit missing premise and stop condition

To turn collective heat dynamics into a **time-zero** exclusion theorem for even one hypothetical off-real Xi zero, the method must supply an independent source-specific statement that contradicts the positivity of the local survival interval `d`. Examples would be an actual certified zero-free time interval `(0,epsilon)` *for all real heights*, or a phase-sensitive Xi-specific estimate forcing the off-real branch to be absent at time zero. Merely lowering a *positive* upper bound for Lambda, proving positive kernel properties, or deriving a finite lower bound on a collective interaction field does not meet this standard.

No such new arithmetic theorem was obtained in this bounded audit. The most recent 2026 numerical heat-flow reports are conditional/audit-relative as cited. The result is a **falsification of the proposed finite-rate inference, not a refutation of heat-flow research generally**.

## 5. Tool/evidence classification

- `PROVED_WITH_STATED_CLASSICAL_INPUTS`: genuine Xi/H_t normalization identity; multiplicity-safe local persistence theorem (entire theta convergence, Rouché, de Bruijn–Newman characterization); the local disk gate and its high-height failure (plus external unconditional Polymath Lambda<=0.22 and classical zeta vertical-strip bounds).
- `EXACT_SYMBOLIC_ALGEBRA_CHECKED`: Planat's projected-kernel factorization using local SymPy; does not extend to full zero-motion or numerical audit.
- `EXTERNALLY_PROVED`: Rodgers–Tao Lambda>=0; Polymath Lambda<=0.22 (cited original papers).
- `EXTERNALLY_REPORTED_CONDITIONAL`: Planat 2026 Lambda<=0.148611789321711 under A1–A3. Not re-executed or independently validated.
- `UNVERIFIED`: any physical transfer giving independent Lambda<=0, an exact Hilbert–Pólya Hamiltonian, or Lee–Yang ferromagnetic partition-function approximation of Xi.
- **Lean 4:** Not installed in this ChatGPT container (`lean`, `lake`, `elan` unavailable). No Lean compilation, declarations, axiom check, or Codex run claimed. Exact finite algebra was checked with SymPy instead. No installations or remote tool campaigns initiated.
- **ZIP integrity:** All 31 manifest member hashes matched the archived `SHA256SUMS` in the user-supplied handoff. Does not validate historical WSL evidence or mathematical conclusions.

**Disposition:** `NO_NEW_RH_FRONTIER_ADVANCE`. Close the **positive-time finite-rate heat contraction => time-zero RH** shortcut and the **uniform absolute kernel error => global zero-exclusion** shortcut. Preserve the other physical mechanisms as general research ideas only; no new proof-critical candidate survived the GO gate, so **no Codex campaign justified**.
