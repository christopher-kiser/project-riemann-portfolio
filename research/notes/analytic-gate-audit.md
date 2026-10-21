> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `501dc0808e8d03c63aae2dec08d5116ff34b04f6fcf9903ffb90c6027710efc3`.

# Project Riemann — Exact-logistic analytic gate, independent continuation (2026-10-19)

## Result
`DIGAMMA_CORRECTION_IDENTIFIED_AND_CHECKED / FULL_ZFR_206_UNVERIFIED`.
No assertion of a new zero-free region or of RH. No Codex, Lean, source project files or Git history changed.

## Proven finite/analytic identity (not a full explicit formula)
Define A(s)=-log(pi)/2+psi(1+s/2)/2. For Re(s)>-2 and a real nonnegative shift h, the absolutely convergent digamma identity is

A(s+h)-A(s)-h A'(s) = - integral_0^infinity (exp(-hu)-1+hu) exp(-(s+2)u)/(1-exp(-2u)) du.

Proof: The standard trigamma integral yields
A'(s)=integral_0^infinity u exp(-(s+2)u)/(1-exp(-2u)) du.
Integrate in s along [s,s+h] and subtract hA'(s), justified by absolute convergence near u=0 and exponential decay at infinity. This fixes BOTH the sign and the shift (s+2). For a test weight f with f(0) and f'(0) nonzero, the corresponding linear Taylor subtraction in the gamma-frequency transform is f(u)-f(0)-u f'(0). This check alone DOES NOT establish a Guinand–Weil formula for f or the required zero-sum rearrangement.

Independent numerical check at s=1.1+2i and h=0.2 with 35-digit mpmath: residual <3e-37. This is only a consistency test; not the proof.

## Source comparison
Primary source: Bellotti, Trudgian, Yang, arXiv:2603.21490v1, https://arxiv.org/pdf/2603.21490. Its displayed Kadiri Proposition 2.1 (Lemma 7, PDF p.13) assumes g'(0)=0. For exact logistic f(u)=eta w(eta u)/(1+exp(-d u)), f'(0)=eta w(0)d/4 >0. Therefore Lemma 7 cannot be invoked verbatim. A new complete explicit-formula derivation is necessary, with the correctly signed -f'(0) A'(s) term, plus remainder. This document has not independently justified all regularization and zero-sum interchanges.

## Error and scalar checks
The proposed elementary error envelope (subject to the generalized explicit formula's validity) is
|E_f(s)|/eta <= (5.7/48) I_3(a) +117 eta^2 (I_2(a)/2+I_3(a)/4),
I_n(a)<=n![a^(-n-1)+a^(-n)/(2n)], a>=2.993.
At a=2.993 and eta=0.007171 the right side is approximately 0.013868828322 <0.014. This estimate is conditional on the asserted pointwise Taylor bound on f and the complete formula's correct remainder.

Reexecuted the existing *unchanged* LOCAL_ARCHIVE/check_scalar_rational.py: worst-point M(0.206000000001,80)=-0.0026645826928710626 (displayed decimal). This is a conditional scalar contradiction ONLY, depending on the bulk lower bound, high-k archimedean estimates and full zero pairing. A numerical negative scalar margin is NOT a zeta zero-free theorem.

## One proof-critical question, no campaign yet
Can one establish a fully regularized explicit formula for this exact compactly supported C^2 logistic weight with nonzero f'(0), obtain the correct zero-sum/multiplicity pairing uniformly in the intended sigma/eta/t region, and enclose all high-k error terms strictly within the saved scalar budget? Source Lemma 7 does not automatically answer this. Remaining nontrivial gates also include independent interval verification of borrowed BTY bulk C1(mu) and exact height iteration. Until all gates pass, the proposed stronger boundary sigma>1-0.206/log t is UNVERIFIED.

## Status
RH open; Haglund k=2/k=3 unverified; previous moment estimate BLOCKED_NEW_MOMENT_ESTIMATE; historical provenance BLOCKED_UNWAIVED. The previous master handoff and audit files are preserved unchanged.
