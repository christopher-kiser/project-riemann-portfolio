> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `fc2da427191376b108a0d086b00a8c5ed0cf0c54eda44fb40beae5798c0a9b42`.

# Project Riemann — Modular scattering, singular boundary, and zero-location transfer

**Research continuation:** October 19, 2026. **Verdict:** `GENUINE_MODULAR_SCATTERING_BOUNDARY_THEOREM_WITH_CLASSICAL_INPUTS / NO_NEW_RH_FRONTIER_ADVANCE`.

This is an independent derivation of consequences of the **actual** completed Riemann zeta function and the established modular Eisenstein constant term. It does **not** establish novelty/priority over existing mathematical literature. The small-boundary asymptotics are checked numerically, not interval-certified. All exact analytic statements below are classical-analysis proofs with explicit hypotheses, not Lean-checked. No Codex campaign or modification of historical evidence.

## Physical object and normalization

Set

    L(s) = pi^(-s/2) Gamma(s/2) zeta(s),
    xi(s)=s(s-1)L(s)/2,
    c(s)=L(2s-1)/L(2s).

Here `L` denotes the **meromorphic** completed zeta (usually called `Lambda`), with poles at 0 and 1 and zeros precisely at the nontrivial zeta zeros. Do not confuse it with the **entire** `xi` function. The completed zeroth Fourier coefficient of the modular Eisenstein series is

    F_Y(s) = Y^s L(2s) + Y^(1-s) L(2s-1), Y>0.

This is a genuine arithmetic/geometric object. For `Y>=1`, the established Lagarias–Suzuki/Ki/Müller theorems constrain **non-real** zeros of the constant term to `Re(s)=1/2`; when `Y>4*pi*exp(-EulerGamma)` there can additionally be two **real** off-line zeros. A cut-off Laplacian `Delta_Y` is self-adjoint; the explicit identification of its eigenvalues with zeros of `F_Y` uses `Y>=1`. Do not extend this spectral correspondence to `0<Y<1` merely because a cut-off operator can still be defined.

For `s=1/2+it`, the functional equation gives `|c(s)|=1` (except at removable singularities), so the two incoming/outgoing cusp waves balance in modulus. This unitary scattering relation does not constrain the poles of the meromorphically continued scattering matrix to be self-adjoint eigenvalues.

## Theorem 1: singular-boundary zero recovery; no RH assumption

Let `rho=beta+i gamma` be **any** nontrivial zeta zero, `0<beta<1` and `gamma!=0`, of multiplicity `m`. Put

    s_L = rho/2,       s_R = (rho+1)/2.

As `Y->0+`, the meromorphic family `F_Y(s)` has exactly `m` zeros (with multiplicities) in each sufficiently small fixed disk around `s_L` and around `s_R`, for every sufficiently small `Y`. The disks can be chosen disjoint, entirely in the left and right open half-strips, respectively, and avoid all poles. The clusters converge to `s_L` and `s_R`. For a fixed finite collection of such zeros, convergence is uniform in the sense of one common sufficiently-small `Y`.

**Proof.** On a compact set in `0<Re(s)<1/2`, normalize by the zero-free factor `Y^s`:

    F_Y(s)/Y^s = L(2s) + Y^(1-2s) L(2s-1).

The second term tends locally uniformly to zero since `Re(1-2s)>0`. Consequently the normalized function converges locally uniformly to `L(2s)`, with a multiplicity-`m` zero at `s_L`. On a sufficiently small circle around `s_L`, the limit has nonzero minimum modulus. Rouché then transfers the count `m` for all sufficiently small `Y`. In `Re(s)>1/2`, normalize instead by `Y^(1-s)`:

    F_Y(s)/Y^(1-s) = L(2s-1) + Y^(2s-1) L(2s),

which converges locally uniformly to `L(2s-1)` with multiplicity-`m` zero at `s_R`. Apply the same argument. Both neighborhoods lie away from the completed zeta poles at 0 and 1. QED.

The limiting locations themselves are never roots of `F_Y` at any finite `Y>0`:

    F_Y(rho/2) = Y^(1-rho/2) L(rho-1) != 0,
    F_Y((rho+1)/2) = Y^((rho+1)/2) L(rho+1) != 0.

The nonvanishing follows from the zero-free half-planes `Re(w)<0` and `Re(w)>1` of the completed zeta, not from RH. This is **migration toward** zeta zeros, not exact finite spectral identification.

## Theorem 2: explicit counter-rotating logarithmic spirals for simple zeros

If the zero `rho` is simple (`L'(rho)!=0`), the two zeros in the respective small disks are eventually unique and satisfy, as `Y->0+`:

    s_L(Y) = rho/2
       - [L(rho-1)/(2 L'(rho))] Y^(1-rho)
       + O_rho(Y^(2(1-beta)) (1+|log Y|)),

    s_R(Y) = (rho+1)/2
       - [L(rho+1)/(2 L'(rho))] Y^rho
       + O_rho(Y^(2 beta) (1+|log Y|)).

**Proof.** In the left normalization put `s=rho/2+h`, `q=Y^(1-rho)` and `ell=log Y`. Taylor-expand:

    L(rho+2h)=2 L'(rho)h+O(h^2),
    L(rho-1+2h)=L(rho-1)+O(h),
    Y^(1-2s)=q exp(-2h ell).

Since `|q log Y|->0`, Rouché on a circle `|h|=C|q|` gives one root with `h=O(q)`, then substitution gives `h= -q L(rho-1)/(2 L'(rho)) + O(|q|^2(1+|ell|))`. The same calculation on the right normalization, with `q=Y^rho`, gives the right formula. QED.

The **radial exponents** are `1-beta` and `beta`; the phases rotate in opposite directions because `Y^(1-rho)=Y^(1-beta)exp(-i gamma log Y)` and `Y^rho=Y^beta exp(+i gamma log Y)`. For the same `rho`, their radial exponents sum to one. Unequal rates encode `beta!=1/2`; equal rates encode `beta=1/2`. **This is an exact re-expression of RH, not an independent proof of it.**

For multiple zeros, Theorem 1 survives without any simplicity assumption. More precisely the local cluster lies at distance `O_rho(Y^((1-beta)/m))` on the left and `O_rho(Y^(beta/m))` on the right; a general simple-root spiral expansion must NOT be claimed for multiple zeros.

## Corollary 3: a growing number of off-line zeros in the same arithmetic family

For every positive integer `N`, there is `Y_N>0` such that, for every `0<Y<Y_N`, `F_Y` has **at least N nonreal zeros to the left** of `Re(s)=1/2` and **at least N to the right**, all inside `0<Re(s)<1`.

**Proof.** It is a classical theorem (Hardy) that zeta has infinitely many distinct nontrivial zeros on its critical line, with positive imaginary part. Choose `N` such zeros, apply Theorem 1 to disjoint small disks around their left locations `rho_j/2`, and select a common sufficiently small `Y_N`. The exact symmetries `F_Y(1-s)=F_Y(s)` and `F_Y(conj(s))=conj(F_Y(s))` (real `Y`) carry the left zeros to distinct right zeros at the same positive heights. QED.

This is a **zero-location change** in a genuine modular arithmetic family, without requiring RH to be true or false. For `Y>=1` the established theorem rules out those nonreal off-line zeros. For `Y<1` the theorem tying zeros of `F_Y` to eigenvalues of the self-adjoint cut-off Laplacian is *not* available. This is not a contradiction or an RH disproof.

## Physical interpretation and decisive caution

The Eisenstein scattering coefficient has a pole of multiplicity `m` at `s=rho/2`, because its numerator `L(rho-1)` does not vanish. The modular Laplacian energy is `E=s(1-s)`. At that scattering pole,

    Im E = gamma(1-beta)/2,

which is nonzero for any nontrivial positive-height zeta zero **even if RH is true**. This is a resonance on a continued scattering sheet, not an L² eigenvalue; self-adjointness does not require its complex resonance energy to be real.

The transition at `Y=1` is in the proven **zero-to-eigenvalue correspondence**, not a proof that the formal cut-off operator ceases to be self-adjoint at `Y<1`. The phase winding of the local branch describes a mathematical boundary response, not a literal quantum measurement acting on primes.

## Gate 4: physical time delay gives the wrong inequality direction

Let `S(s)=c(s)` and `s=1/2+it`, `t!=0`. Functional equation and conjugation imply

    d/dt arg S(1/2+it) = c'(1/2+it)/c(1/2+it)
       = -4 Re L'(1+2it)/L(1+2it)
       = -4 Re xi'(1+2it)/xi(1+2it)+4/(1+4t²).

The symmetric Hadamard partial fraction for entire `xi` gives for any `T`:

    Re xi'(1+iT)/xi(1+iT)
      = sum_{zeta zeros rho=beta+i gamma}
          (1-beta)/[(1-beta)^2+(T-gamma)^2] > 0,

with the usual symmetric zero grouping, and absolutely convergent real part for fixed `T`.

Hence a **single hypothetical zero** `rho=beta+i gamma` forces the necessary inequality

    -c'(1/2+i gamma/2)/c(1/2+i gamma/2)
         >= 4/(1-beta) - 4/(1+gamma²).

This is a genuine quantitative individual-zero signature, but it is a classical consequence of Hadamard, not a new zero-exclusion bound. An independently established **upper** bound on that time delay could constrain `beta`; none has been proved here beyond the existing zeta analysis.

At spectral quantization points (`1+c(s)Y^(1-2s)=0`) the Maass–Selberg positivity formula supplies

    ||truncated_E(s)||² = 2 log Y - c'(s)/c(s) > 0

for `s=1/2+it`, `t!=0`, since the oscillatory boundary term vanishes there. It bounds the phase derivative from **above**, and correspondingly the time delay from **below**. It therefore becomes *easier* to satisfy as the hypothetical resonance's delay grows. This is the **wrong direction** to exclude an individual off-line zero. Importing a sign-reversed bound would be a mathematical error.

## Verification

`verify_modular_scattering.py` uses 66-digit mpmath to reproduce the phase derivative identity and two complex branches near the first known zero `rho=1/2+14.134725141734693790457...i`; the predicted leading terms become increasingly accurate as `Y=e^-L` decreases. Both branches agree with exact reflection symmetry to numerical precision. The script is a diagnostic, not a proof or interval certificate. The imaginary-energy formula was checked independently with symbolic Wolfram algebra. The analytical Rouché proof above is the actual basis for the theorems.

## Primary literature, historical status, and stop/go decision

- Werner Müller, *A spectral interpretation of the zeros of the constant term of certain Eisenstein series*, arXiv:math/0703340: https://arxiv.org/abs/math/0703340 . The text gives the exact scattering coefficient, the cut-off Laplacian spectral correspondence and the Maass–Selberg norm formula. See §0 and §2 (equations (2.1)-(2.5)).
- Jeffrey C. Lagarias and Masatoshi Suzuki, *The Riemann hypothesis for certain integrals of Eisenstein series*, arXiv:math/0412039: https://arxiv.org/abs/math/0412039 . Real-zero theorem for the geometric spectral cutoff.
- Maciej Zworski, *Mathematical study of scattering resonances*, Bulletin of Mathematical Sciences, https://link.springer.com/article/10.1007/s13373-017-0099-4 . The physics distinction between resonances and eigenvalues, including modular surface resonances.

**Status:** RH OPEN; complete Haglund k=2/k=3 UNVERIFIED; marked-inverse `BLOCKED_NEW_MOMENT_ESTIMATE`; historical Git provenance `BLOCKED_UNWAIVED`. Nothing in this audit is a new zero exclusion for Xi. The sharp small-`Y` transfer is a useful standalone classical-input theorem and a **negative result for a passive/self-adjoint scattering shortcut**. No broad Codex run; Lean 4 is not installed here. This branch is closed pending an independently constructed new inequality controlling resonance widths from prime arithmetic (not merely a symmetric spectrum).
