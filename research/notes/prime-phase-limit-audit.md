> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `4267f3d1fceda9d3c2eba25e1e7b78ffc73a71990b6beebea8cc1b79022b7e1f`.

# Project Riemann — Infinite-prime phase and regularization gate

**Date:** 2026-10-20  
**Scope:** Bounded falsification-first continuation of `MULTISCALE_WALSH_AND_POLE_GATE.md` and the prior prime-coherence studies.  
**Verdict:** `EXACT_CLASSICAL_FIRST_HARMONIC_GATE / RANDOM_PHASE_CONTROL / NO_NEW_RH_FRONTIER_ADVANCE`.

## 1. Question and separation of facts

Does uniform arithmetic compatibility across arbitrarily many prime directions yield an independent, zero-free constraint in `Re(s)>1/2`, or does a more basic obstruction to passing from finite to infinite phase configurations remain? The claim proved below is a precise *no-go for a proposed mode of inference*, not a proof or refutation of RH, not a new numerical zero-free bound, and not a claim of research priority.

We use only classical results (uniform convergence of holomorphic series, Euler's divergence of the reciprocal prime sum, standard independence/martingale convergence, and the Euler product in `Re(s)>1`). The numerical experiment is a diagnostic, not a proof.

## 2. Exact all-prime first-harmonic decomposition

For `Re(s)>1` define the partial sums

    P_Y(s)= Σ_{p≤Y} p^{-s},
    H_Y(s)= Σ_{p≤Y} Σ_{m≥2} p^{-ms}/m,
    E_Y(s)= Π_{p≤Y} (1-p^{-s})^{-1}.

For every finite `Y`, the principal logarithm is unambiguous factorwise because `|p^{-s}|<1` for `Re(s)>0`. The elementary logarithm expansion gives

    log E_Y(s) = P_Y(s)+H_Y(s),   Re(s)>0.       (A)

For every compact `K⊂{Re(s)>1/2}` with `Re(s)≥σ0>1/2`,

    Σ_p Σ_{m≥2}|p^{-ms}|/m
       ≤ [2(1-2^{-σ0})]^{-1} Σ_p p^{-2σ0}<∞.

Consequently `H_Y→H` locally uniformly on the *whole* half-plane `Re(s)>1/2`, where `H` is holomorphic. Hence

    R_Y(s):=Π_{p≤Y}(1-p^{-s}) e^{p^{-s}}
           =exp(-H_Y(s)) → R(s):=exp(-H(s)) ≠ 0         (B)

locally uniformly in `Re(s)>1/2`. There is no required RH hypothesis.

Only in `Re(s)>1`, where `P_Y→P=Σ_p p^{-s}` absolutely, is it valid to take the unregularized Euler product limit and assert

    log ζ(s)=P(s)+H(s).                              (C)

The Euler product itself has *not* thereby been analytically continued to `1/2<Re(s)≤1`.

### Precise hypothetical-zero diagnostic

For any disk `D` in `1/2<Re(s)<1` not meeting `s=1`, the meromorphic one-form

    (ζ'(s)/ζ(s) - H'(s)) ds                       (D)

is the analytic continuation of `P'(s)ds` from the Euler-product domain along allowed paths. If a hypothetical zero `ρ∈D` has multiplicity `m`, this one-form has a simple pole at `ρ` of residue `m`. Since `H'` is holomorphic, the residue of the first-harmonic form is exactly the multiplicity.

Locally around the hypothetical zero, a branch of `P` has the form `m log(s-ρ)+ holomorphic`. This is a **conditional consequence of the assumed zero**, not an independent way to exclude it. Proving that the one-form has no residue in the unresolved half-strip would amount to excluding zeros there, i.e. would be RH-strength if done for all such disks.

## 3. Random-phase control: true for almost every infinite prime phase configuration, but not the genuine one

Give each prime an independent sign `ε_p∈{−1,+1}` with probability `1/2` each. Define

    Z_ε(s)=Π_p (1-ε_p p^{-s})^{-1}.

**Classical theorem (random Euler products; verified here from standard martingale inputs).** With probability one, this product converges locally uniformly to a holomorphic, *nowhere-zero* function on the entire half-plane `Re(s)>1/2`.

*Proof with explicit dependencies.* Let `K` be a closed disk lying inside that half-plane; choose a slightly larger disk `D` also inside it. In the Hilbert space of square-integrable holomorphic functions on `D`, independent centered random summands `ε_p p^{-s}` have square-summable Hilbert norms, since

    Σ_p E||ε_p p^{-s}||²_{L²(D)} = Σ_p∫_D p^{-2 Re(s)}dA(s)<∞.

The Hilbert-valued martingale convergence theorem implies almost sure convergence in that Hilbert norm. The mean-value inequality for holomorphic functions implies uniform convergence on compact subsets of `D`. A countable exhaustion by disks provides local uniform convergence throughout `Re(s)>1/2`. Finally, for each sign choice,

    -log(1-ε_p p^{-s}) = ε_p p^{-s} + O_K(p^{-2 Re(s)}),

and the remainder series converges locally uniformly by section 2. Thus the log-Euler product is holomorphic and its exponential is nowhere zero. QED with standard classical inputs.

**All finite genuine prime prefixes can coexist with this different behavior.** Fix any `Y` and force `ε_p=+1` for `p≤Y`, leaving the tail independent symmetric signs. With probability one, the resulting Euler product still converges to a holomorphic nonzero function for `Re(s)>1/2`, because replacing a finite number of local factors cannot affect convergence/nonvanishing.

Now couple all these finite-prefix models using a single random tail sequence `ε_p`, and let the forced prefix `Y→∞`. At any *real* `1/2<σ≤1`,

    log Z_Y(σ)=Σ_{p≤Y}[-log(1-p^{-σ})]
                +Σ_{p>Y}[-log(1-ε_p p^{-σ})].        (E)

The second series tends to zero almost surely as `Y→∞`, by convergence of the random log series; the first tends to `+∞` because `Σ_p p^{-σ}` diverges for every `σ≤1`. Hence

    Z_Y(σ)→+∞,      for every real 1/2<σ≤1, a.s.  (F)

while `Z_Y(σ)→ζ(σ)` for real `σ>1`. These facts are consistent because analytic families `Z_Y` **lack local boundedness** on the critical strip. Almost-sure/nonzero behavior of the random-phase model is not inherited by the all-positive actual Euler-product phase configuration, which has product probability zero.

This random model differs from genuine zeta and need not satisfy its functional equation. It is a control demonstrating a logical gap, not a surrogate proof of RH.

## 4. Finite-phase variance versus coherent amplification

At real `σ>1/2`, for the random first-harmonic sum

    P_Y^ε(σ)=Σ_{p≤Y} ε_p p^{-σ},

independence gives exactly

    E[P_Y^ε(σ)]=0,
    E|P_Y^ε(σ)|²=Σ_{p≤Y}p^{-2σ}≤ζ(2σ)-1<∞.

The coherent sum at the same `σ≤1` is

    P_Y^+(σ)=Σ_{p≤Y}p^{-σ}→+∞.

Thus arbitrarily good **statistical** second-moment control in all the prime dimensions cannot give uniform pointwise control at the unique coherent configuration corresponding to the genuine zeta Euler product. In Hilbert-space language, the cost of evaluating at that configuration grows without bound.

### Exact finite identity and numerical diagnostic

`verify_phase_limit.py` sieves every prime up to one million (78,498 primes), checks the finite complex log identity and reports, at `σ=0.75`:

| Last prime included | First-harmonic sum `P_Y` | Higher-order `H_Y` | Random-log sample |
|---:|---:|---:|---:|
| 97 | 3.008966044 | 0.604767753 | 0.715887000 |
| 997 | 4.662479887 | 0.617209160 | 0.772570595 |
| 9,973 | 6.800532491 | 0.619963243 | 0.720614152 |
| 99,991 | 9.774513192 | 0.620636574 | 0.754803967 |
| 999,983 | 14.113979941 | 0.620810457 | 0.730551989 |

A single random sample is *not* evidence of a probabilistic theorem; the almost-sure result has the separate classical proof above. With `σ=.75`, the deterministic remainder tail can be bounded by a convergent `Σ_{n>Y}n^{-3/2}`. The finite complex check at `s=0.72+14.134725i` across the first 200 primes had floating residual `1.12×10^-15`.

## 5. Adversarial verdict and exact stop condition

- **Passed:** full-prime quadratic correction is globally holomorphic and zero-free in `Re(s)>1/2` after exponentiation; exact finite log identity; random-phase nonvanishing in the half-plane with standard classical probabilistic inputs; a finite prefix of genuine prime laws is insufficient for passing the zero-free conclusion to all primes.
- **Not passed:** any arithmetic lower bound for the *actual* phase-sensitive prime wave; any new zero exclusion; an independent holomorphic continuation of `P(s)` through an arbitrary hypothetical off-line zero.
- **Literature gate:** first-order prime zeta and random Euler models are well-established, including Fröberg's prime-zeta identities, Wintner's random multiplicative models, and subsequent refinements. This note makes no novelty claim.
- **No-go:** the statement that the first-harmonic continuation has no logarithmic monodromy for `Re(s)>1/2` is itself equivalent to the unresolved zeta-zero exclusion (once `s=1` is handled). Assuming it would be circular.

A *future* proof-critical campaign requires an explicit new, noncircular arithmetic estimate on the actual first-order phase sum, uniform on a prescribed off-line disk or contour, with a calculable consequence excluding a zero; mere random-phase comparison or a new renormalization is not enough.

### Scope and provenance

No historical Haglund, RH, original moment, or Git evidence was modified. No Codex run. Lean 4 and `lake` were not installed in this environment; no Lean compilation is claimed. This is a classical-input analytic result plus finite diagnostics.

**Project status unchanged:** RH open; complete Haglund k=2/k=3 `UNVERIFIED`; marked-inverse moment `BLOCKED_NEW_MOMENT_ESTIMATE`; provenance `BLOCKED_UNWAIVED`.

### External literature checked

- Prime zeta function and the logarithmic decomposition: MathWorld (Fröberg references): https://mathworld.wolfram.com/PrimeZetaFunction.html ; Brent, *Primes, the Riemann zeta-function...* https://maths-people.anu.edu.au/brent/pd/Brent-CARMA21.pdf .
- Adam Harper, *Almost Sure Large Fluctuations of Random Multiplicative Functions*, *International Mathematics Research Notices*, https://academic.oup.com/imrn/article/2023/3/2095/6448070 ; cites Wintner (1944), including random Euler product behavior.
- 2026 review of probabilistic models and Euler products: https://epubs.siam.org/doi/10.1137/25M1806132 .
- Quasi-RH 7/8 Lean scope and external rebuild: https://github.com/openai/math/blob/main/lean/docs/003.md ; https://github.com/tomoto0/quasi-riemann-hypothesis-7-8-verification . Not directly employed in the current proof.
