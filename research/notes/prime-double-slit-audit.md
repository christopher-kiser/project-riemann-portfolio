> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `81aa75c119c73f983ba6432a606cb01c6c8c67d73e52860a6ffa3f9bcacb2018`.

# Project Riemann — Double-slit / phase preservation and prime diffraction

**Research date:** 2026-10-19 (local US Eastern).  
**Verdict:** `EXACT_CLASSICAL_PHASE_GATE / NO_NEW_RH_FRONTIER_ADVANCE`.  
**Evidence classification:** Sources cited below are published primary mathematics and physics; the elementary identities and limiting deductions are written classical proofs; numerical values are finite diagnostics only. Not Lean-formalized. No Codex run was launched and no historical data were modified.

## 1. The user's intuition and the source-grounded question

A double-slit detector can distinguish coherent amplitudes from incoherent path intensities; actual quantum which-path information causes loss of interference, *not observation by a conscious mind*. Does an analogous choice of arithmetic representation reveal primes' phase structure relevant to zeta's zeros? We compared published prime diffraction and made a falsification-first test on the **actual truncated von Mangoldt Dirichlet polynomial**, not an artificial spectrum.

**Published diffraction is normalization-sensitive.** Torquato, Zhang & de Courcy-Ireland reported sharp Bragg-like peaks for prime arrangements in certain finite windows. Their strong large-window pure-point description is conditional on Hardy–Littlewood prime-pair asymptotics; finite scattering pictures are not an RH proof. In 2025 Humeniuk, Ramsey & Strungaru proved, for specified classes of expanding intervals, that the **counting autocorrelation** of the primes is `delta_0` and the counting diffraction is Lebesgue measure. This is an *unconditional theorem about a different limiting normalization*, not a proof that finite primes have no arithmetic structure. These statements need not conflict.

Their theorem is specifically about the ordinary prime point set in arithmetic (integer) position. Below our Fourier coordinate is **log n** with weights **von Mangoldt**. Do not substitute one diffraction theorem for the other.

## 2. Two-prime exact interference example

Consider amplitudes `a_2(t)=exp(-it log 2)` and `a_3(t)=exp(-it log 3)`.

Coherent intensity:

\[
|a_2(t)+a_3(t)|^2=2+2\cos\big(t\log(3/2)\big).
\]

It equals four at `t=0` and zero at `t=pi/log(3/2)`. If the two channels are kept orthogonally labelled (a mathematical analogue of preserving which-path information), their summed intensity is always `|a_2|^2+|a_3|^2=2`. Nothing has happened to the primes. Only the observable has changed.

## 3. Exact phase-gate theorem for the ACTUAL arithmetic coefficients

Let `1/2 < sigma < 1` and `X >= 2`. Write `Lambda(n)` for the von Mangoldt function (log p at all prime powers `p^k`, otherwise zero). Define

\[
P_{X,\sigma}(t)=\sum_{2\le n\le X}\Lambda(n)n^{-\sigma-it},\quad
S_{X,\sigma}=\sum_{2\le n\le X}\Lambda(n)n^{-\sigma},\quad
D_{X,\sigma}=\sum_{2\le n\le X}\Lambda(n)^2n^{-2\sigma}.
\]

**Theorem (classical, no zero assumptions).** For every fixed `X` and `sigma`,

\[
\limsup_{t\to+\infty}|P_{X,\sigma}(t)|=S_{X,\sigma},
\qquad
\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^T|P_{X,\sigma}(t)|^2\,dt=D_{X,\sigma}.
\]

Furthermore, by the prime number theorem and `Lambda(n) <= log n`,

\[
S_{X,\sigma}\sim \frac{X^{1-\sigma}}{1-\sigma}\to\infty,
\qquad D_{X,\sigma}\to D_\sigma<\infty.
\]

Thus the contrast of arbitrarily late **coherent revivals** to time-averaged **dephased intensity** grows without bound as `X` increases:

\[
\frac{S_{X,\sigma}^2}{D_{X,\sigma}}\sim
\frac{X^{2(1-\sigma)}}{(1-\sigma)^2D_\sigma}\to+\infty.
\]

**Proof of the first claim.** The finite prime factors `p<=X` have rationally independent logarithms: `sum k_p log p = 0` for integer `k_p` implies `product p^{k_p}=1` and hence all `k_p=0`, by unique factorization. Kronecker's theorem for real continuous torus flows implies that there are arbitrarily large real `t` for which every `exp(-it log p)` is arbitrarily close to 1. Hence all the finitely many prime powers `exp(-it k log p)` are simultaneously close to 1. The triangle inequality supplies the reverse upper bound, proving the claimed limsup.

**Proof of the second claim.** For every finite `X`, expand the intensity and integrate exactly:

\[
\frac{1}{2T}\int_{-T}^{T}|P_{X,\sigma}(t)|^2\,dt=
D_{X,\sigma}+2\sum_{2\le n<m\le X}
\frac{\Lambda(n)\Lambda(m)}{(nm)^\sigma}
\frac{\sin(T\log(m/n))}{T\log(m/n)}.
\]

The number of off-diagonal terms is finite and all their sinc factors tend to zero as `T->infinity`, giving the diagonal. For the last estimates, partial summation of `psi(X)=sum_{n<=X}Lambda(n)~X` yields `S_{X,sigma}~X^{1-sigma}/(1-sigma)`. The squared-coefficient sum is dominated by `sum_{n>=2}(log n)^2n^{-2sigma}<infinity` because `2sigma>1`.

**Critical order-of-limits warning:** The recurrence times depend on `X` and may be enormous. This is **not** a uniform bound for the true analytically continued `-zeta'/zeta(s)` in `1/2<sigma<1`; the original Dirichlet series `sum Lambda(n)n^{-s}` converges only when `Re s>1`.

## 4. Finite diagnostics — NOT a proof

At `sigma=0.75` (using all prime powers up to each `X`):

| X | Asymptotic coherent-revival intensity `S_X^2` | Long-time dephased intensity `D_X` | Ratio |
|---:|---:|---:|---:|
| 100 | 62.2290 | 2.2753 | 27.35 |
| 1,000 | 318.8526 | 3.0302 | 105.23 |
| 10,000 | 1,252.2825 | 3.3677 | 371.85 |
| 100,000 | 4,424.0245 | 3.5060 | 1,261.84 |

The diagnostic script enumerates every prime power up to `X` and separately evaluates the exact sinc expression at finite averaging widths. The words "asymptotic coherent-revival intensity" refer to the **supremum/limsup over arbitrarily large times for that fixed X**, not a witnessed peak at a specified finite time.

## 5. Direct RH exclusion gate and adversarial failure

There is an exact, **known** link to real zeta zeros, valid initially for `Re s>1`:

\[
-\frac{\zeta'(s)}{\zeta(s)}=\frac{s}{s-1}+
 s\int_1^\infty\big(\psi(x)-x\big)x^{-s-1}\,dx.
\]

If one were to **independently** prove `|psi(x)-x|=O(x^a)` for a fixed `a<1`, the integral would analytically continue into `Re s>a`, apart from the pole at `s=1`, excluding zeros in that half-plane. This is a familiar prime-error/zero-free relation, **not new**. Assuming such a strong error bound without deriving it is the precise circular Mellin shortcut already rejected in the October 19 master handoff (`05_NO_GO_AND_ERROR_REGISTER.md`, A6).

The intensity calculations above do not bound `psi(x)-x` and do not establish cancellation uniformly in `X` and `t`. They demonstrate the opposite caution: large coherent revivals coexist with bounded dephased mean squares, even under the *exact* prime-power coefficients. Neither the coherent/diffuse distinction nor a finite diffraction pattern can exclude a single hypothetical off-critical-line zero.

**STOP:** A continuation would require a new, source-grounded quantitative estimate on the genuinely signed, off-diagonal prime correlations at uniform unbounded scales. No such estimate is established here; no Codex campaign or RH proof claim is authorized. This is an informative nature-to-arithmetic diagnostic, not a new zero-exclusion theorem.

## 6. Primary sources and scopes

1. Torquato, Zhang & de Courcy-Ireland, *Hidden Multiscale Order in the Primes* (2018), https://arxiv.org/abs/1804.06279 — conditional Hardy–Littlewood large-window pure-point result and finite-window structure.
2. Humeniuk, Ramsey & Strungaru, *Diffraction of the primes and other sets of zero density*, **J. Aust. Math. Soc. 119 (2025)**, https://doi.org/10.1017/S1446788725000096 — unconditional counting diffraction theorem, Theorem 5.13, with stated averaging-sequence hypotheses.
3. M. V. Berry, *Riemann zeros in radiation patterns*, **J. Phys. A 45 (2012) 302001**, https://doi.org/10.1088/1751-8113/45/30/302001 — optical Fourier implementation of actual Xi/zeta zero patterns. The author explicitly says it is not a proof strategy and discusses assuming zero ordinates real.
4. Schoolmann et al., *On Bohr's theorem for general Dirichlet series*, **Mathematische Nachrichten (2020)**, https://doi.org/10.1002/mana.201800542 — Kronecker phase-flow density for rationally independent frequencies, used here for log-primes.
5. Languasco, Perelli & Zaccagnini, *Explicit relations between pair correlation of zeros and primes in short intervals*, **J. Math. Anal. Appl. 394 (2012)**, https://doi.org/10.1016/j.jmaa.2012.04.058 — rigorous classical prime–zero pair-correlation relations; warns that stronger versions rely on RH or other hypotheses.
6. The user's master handoff `05_NO_GO_AND_ERROR_REGISTER.md`, sections A1, A6, A7 and F: earlier marked-moment, Mellin-continuation, and spectral-alignment stop conditions.

## 7. Preservation and verification scope

- `verify_prime_phase_gate.py`: direct finite arithmetic diagnostic with no external network or privileged actions.
- `VERIFICATION_LOG.txt`: captured numerical output.
- `SHA256SUMS`: hashes of these new files (the manifest is not self-hashed).
- The mathematics is checked by elementary finite Fourier integration, unique factorization, Kronecker's theorem, and the classical prime number theorem; **Lean 4 not installed here**, so no formal proof certification is claimed.
- `RH=OPEN`; `HAGLUND_K2_K3=UNVERIFIED`; `MARKED_MOMENT=BLOCKED_NEW_MOMENT_ESTIMATE`; `PROVENANCE=BLOCKED_UNWAIVED`.
