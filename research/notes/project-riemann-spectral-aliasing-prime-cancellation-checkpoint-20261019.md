> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `40ca1557db645d360a95721b293b2e40d372804651e013995a6c1ac190eb8603`.

# Project Riemann — bounded spectral-aliasing and prime-cancellation audit

**19 October 2026.** Mathematical status: elementary proofs and classical inputs, not independently refereed, not formalized in Lean. **NO_NEW_RH_FRONTIER_ADVANCE.** Complete k=2/k=3 `UNVERIFIED`, historical provenance `BLOCKED_UNWAIVED`. This checkpoint is independent of, and does not change, all earlier Codex or manuscript records.

## 1. Decision and research aim

Test a fundamentally different route from the blocked Hecke-character marked inverse-moment inequality: whether a spectral/Weil trace inequality can detect an individual nonreal zero with a bounded amount of information. Seek an actual **noncircular** arithmetic identity; attempt to falsify a finite-window shortcut. Do not count a restatement of Weil positivity as an RH proof.

Public literature checked: M. Chuk, *Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law*, arXiv:2608.24827 (2026), particularly the Weil formula and unconditional claimed L=0.8 certificate; Connes–Consani, arXiv:2006.13771; Bondarenko–Radchenko–Seip, *Fourier Interpolation with Zeros of Zeta and L-Functions*, Constr. Approx. 57 (2023); and the 2026-10-08 unreviewed Nic Johns magic-function preprint. These are distinct evidence categories; none establishes RH.

## 2. Elementary theorem: exact finite-window spectral aliasing

Fix `a>0`, `0<eps<pi/(4a)`, and `delta>0`. Define

    A(z)=cos(a(z-eps))*cos(a(z+eps))
        = (cos(2az)+cos(2a eps))/2,
    B(z)=cos(a(z-i delta))*cos(a(z+i delta))
        = (cos(2az)+cosh(2a delta))/2.

Both are even real entire functions of exponential type 2a and order one, strictly positive on the imaginary axis, and Fourier transforms of finite **positive measures**: an atom of mass cos(2a eps)/2 or cosh(2a delta)/2 at zero, and atoms of mass 1/4 at ±2a. A has only simple real zeros `x_n±eps`; B has only simple nonreal zeros `x_n±i delta`, where `x_n=(n+1/2)pi/a`, `n in Z`. These models are **not** zeta or Haglund approximants, and have no Euler product or full modular theta identity.

Let `f in C_c^infty(R)` be arbitrary (complex allowed), supported in `[-L,L]`, and put `f_tilde(t)=conj(f(-t))`, `g=f*f_tilde`, `h(z)=hat(g)(z)=hat(f)(z)hat(f_tilde)(z)` with the Fourier convention `hat(f)(z)=int f(t)e^(izt)dt`. Then `g` is supported on `[-2L,2L]`, `g(0)=||f||_2^2`, and `h(x)=|hat(f)(x)|^2` for real x. All zero sums of h below are absolutely convergent.

Poisson summation in distributions, or in the Schwartz class after testing against g, gives for every complex shift s:

    sum_(n in Z) h(x_n+s)
      = 2a sum_(j in Z) (-1)^j e^(2iaj s) g(2aj).

If `L<=a`, then for `j!=0` one has `g(2aj)=0`, and therefore

    sum_(zeros of A) h(rho) = sum_(zeros of B) h(rho)
       = 4a ||f||_2^2.

This holds for **every** test function of that support, not just a selected basis or a numerical sample. Thus an all-real spectrum and an all-offreal spectrum pass precisely the same **strictly positive zero-side tests** on every fixed window L<=a.

The threshold is sharp for these models. For any L>a, choose a real even nonnegative smooth bump `phi` supported in `(-sigma,sigma)` with `0<sigma<min(a/4,L-a)`, set `f(t)=phi(t-a)+phi(t+a)`, and write `C=||phi||_2^2`. Its autocorrelation satisfies `g(0)=2C`, `g(±2a)=C`, and `g(2aj)=0` for `|j|>=2`. Poisson summation yields

    sum_(zeros of B) h(rho) = 8a C [1-cosh(2a delta)] < 0,
    sum_(zeros of A) h(rho) = 8a C [1-cos(2a eps)] > 0.

**Interpretation:** Bounded support spectral positivity, on its own, cannot determine whether the zeros are real. The model is synthetic; the actual zeta prime distribution can rule out such models. The argument makes no claim of new RH restrictions or literature novelty. It warns against extending a finite-window positivity result to all supports by mere precision increase or by continuity of the restricted test space.

## 3. A sharp single-shift bound for the actual prime-transfer operator

For arbitrary `f in L^2([-L,L])`, let `g(h)=int f(t)conj(f(t-h))dt`. For every `h>0` put `N=ceil(2L/h)` (if `h>=2L`, N=1). The **sharp** bound is

    |g(h)| <= cos(pi/(N+1)) ||f||_2^2.

Proof: disintegrate `[-L,L]` along fibers modulo h. Each fiber is a chain with at most N nodes, the shift couples neighboring nodes, and the largest eigenvalue of the symmetric N-node path adjacency divided by 2 is `cos(pi/(N+1))`. A fiber with N nodes occupies positive residual measure when h<2L. Choosing its sine-eigenvector weights attains the bound, up to harmless smooth approximation. At h=2L the autocorrelation vanishes.

For the **actual** prime part of the Weil quadratic form,

    P_L(f)=2 sum_(n>=2, log n<2L) Lambda(n)/sqrt(n) * Re g(log n),

this gives an unconditional asymptotic operator-norm bound, by the prime number theorem and partial summation,

    |P_L(f)| <= (2+o(1)) e^L ||f||_2^2,

rather than the crude coefficient-mass bound `(4+o(1))e^L ||f||_2^2`. Indeed `log n in (L,2L)` entails N=2 and the exact factor 1/2; smaller n contribute `O(e^(L/2))` in this crude upper bound. This is a **quadratic-form** bound, not a false pointwise improvement of the prime-cosine symbol.

The exponential scale cannot be lowered by a uniform prime-part norm estimate alone. Choose an even nonnegative smooth phi supported on a fixed tiny interval `(-sigma,sigma)` and `c>sigma`, and set `f_L(t)=phi(t-(L-c))+phi(t+(L-c))`. Its positive autocorrelation has a cross term at separation `d=2(L-c)`; PNT in the fixed-relative window around x=e^d gives

    P_L(f_L) = 2 e^(d/2) (int phi(t)e^(t/2)dt)^2 + o(e^(d/2))

(the self-overlap at small fixed lags contributes only O(1)). Since `||f_L||_2^2=2||phi||_2^2`, there is a fixed `c_phi>0` with `P_L(f_L)>=c_phi e^L ||f_L||_2^2` for all sufficiently large L. Thus the norm scale is `Theta(e^L)` unconditionally. No power saving in this prime operator by itself is possible.

**Caveat:** The shift numerical-radius inequality is classical finite-path spectral algebra, not claimed as a new mathematical discovery. The combined asymptotic is a new computation in this project, not independently compared exhaustively against prior literature.

## 4. Exact cancellation: the pole and the PNT main term

For a smooth **real even** f supported in `[-L,L]`, with Fourier transform F and real even autocorrelation g, take the Weil normalization used by Chuk:

    Q_zeta(f)=2F(i/2)^2
       +(1/(2pi)) int_R |F(t)|^2 [Re digamma(1/4+it/2)-log pi]dt
       -2 sum_(n>=2) Lambda(n)/sqrt(n) g(log n).

Introduce `psi(x)=sum_(n<=x)Lambda(n)` and its signed deviation `E(x)=psi(x)-x` for x>1; use Stieltjes measures `dE=dpsi-dx`. Then

    sum_(n>=2) Lambda(n)/sqrt(n) g(log n)
       =int_1^infty x^(-1/2) g(log x)dx
        +int_1^infty x^(-1/2) g(log x)dE(x).

Because f is real even, the pole and the **smooth PNT main term cancel exactly**:

    2F(i/2)^2 -2 int_1^infty x^(-1/2)g(log x)dx
      = int_R int_R f(t)f(s)e^(-|t-s|/2) dt ds
      =(1/(2pi))int_R |F(t)|^2/(t^2+1/4) dt >=0.

This uses only a change of variables, symmetry, and Plancherel; no RH and no prime error bound. Consequently the **actual** Weil form has the exact alternative expression

    Q_zeta(f)= (1/(2pi)) int_R |F(t)|^2 B(t)dt
             -2 int_1^infty x^(-1/2) g(log x)dE(x),
    B(t)=Re digamma(1/4+it/2)-log pi +1/(t^2+1/4).

The residual Stieltjes term has compact support in x up to e^(2L). The kernel `e^(-|t-s|/2)` is strictly positive definite. However **B(t) is NOT everywhere positive**:

    B(0)=4-EulerGamma-pi/2-3log 2-log pi
        =-1.372183419225... <0.

In fact, for any fixed nonzero even smooth phi, the wide test `f_L(t)=L^(-1/2)phi(t/L)` makes the first integral tend to `B(0)||phi||_2^2<0`. The signed prime error is therefore indispensable, not a term that can be thrown away by absolute values. Establishing the necessary positivity from an independent uniform estimate on that error is the unresolved analytic obligation; assuming an RH-strength Chebyshev error would be circular.

## 5. Decision

**Accepted at written classical-input scope:** exact synthetic bandlimit aliasing; sharp shift correlation inequality; prime part `Theta(e^L)` norm scale via unconditional PNT; exact zeta pole/PNT-main cancellation and residual signed-error formula. They have explicit proofs or standard input, but no local Lean 4 compilation and no independent human refereeing. Numerical checks are diagnostics only.

**Not accepted or established:** any uniform RH-strength sign control of the signed Chebyshev-error bilinear form, an all-L Weil positivity theorem, an improved zero-free half-plane, an RH disproof, or an equivalence that somehow discharges itself.

**Research verdict:** the finite-window spectral route by itself is insufficient, and the actual arithmetic form only becomes tractable if it preserves cancellation between poles, archimedean terms and the exact signed prime discrepancy. This is a coherent mechanism to keep in mind, but **no independent estimate supplying the missing cancellation has been found**. Close this bounded branch here; do not commission a new speculative Codex search or extend finite windows numerically for its own sake.

Preservation: only this new report was created. Nothing in WSL, Git, k=2/k=3 archives, seals, or stopped services was modified. `BLOCKED_UNWAIVED` remains.

## References

- Marcus Chuk (2026), *Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law*: https://arxiv.org/abs/2608.24827 . Preprint, not an accepted RH proof.
- Connes–Consani, *Weil positivity and Trace formula, the archimedean place*: https://arxiv.org/abs/2006.13771 .
- H. Davenport / Montgomery–Vaughan, Weil formula treatment: https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/16.0_pp_397_418_Explicit_formulae.pdf .
- Bondarenko–Radchenko–Seip, *Fourier Interpolation with Zeros of Zeta and L-Functions*, Constructive Approximation 57 (2023): https://link.springer.com/article/10.1007/s00365-022-09599-w .
