> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `576eb8ffb7543ea2b249b1b056e6d5277ed9762e75471be28b3ca9de145b4a9d`.

# Project Riemann — exact logistic prime-detector gate (October 19, 2026)

**Verdict:** `BOUNDED_LEMMA_PASSED / NO_NEW_RH_FRONTIER_ADVANCE`. This is a precise partial analytic lemma for an existing **prime-sensitive** method, *not* a new zeta zero-free region and *not* a proof of RH. The calculations are a candidate improvement to an arXiv v1 zero-detector argument; its last explicit-formula / scalar gate is **UNVERIFIED**. No Codex, Git, WSL, systemd or historical artifacts were changed.

**Controlling paper (primary text, exact version read):** Chiara Bellotti, Tim Trudgian, Andrew Yang, *Zero-free regions inspired by work of Heath-Brown*, arXiv:2603.21490v1 (23 March 2026), https://arxiv.org/pdf/2603.21490 . Relevant Definition 1, pp. 6–7; proposed exact logistic smoothing equation (14), p. 6; Lemma 5, pp. 8–10; prime lower bound Lemmas 10–11, pp. 16–18; Lemma 9, p. 15. Their stated Theorem 1 is `sigma>1−1/(4.896 log t)`, `t>=3`. This packet has not reproduced its proof or verified its final constant.

## 1. Exact objects and hypotheses

Set theta = 5669/5000 = 1.1338, and let `w(v)` be the *exact* Heath-Brown function in their Definition 1, supported on `[0,U]`, `U=2 theta cot(theta)`. In their notation `W(z)=int_0^U exp(-zv) w(v) dv`. We use the **published** classical properties `w(v)>=0`, `w'(v)<=0`, `Re W(iy)>=0` for all real y, and the explicit elementary formula for `w` (the rational verifier independently encloses its derivatives where used). From that formula, `w'(0)=0` and `w(U)=w'(U)=0` by trigonometric identities.

Let `0 < eta <= 0.0072`, `0.9869 <= d <= 1`, and `f(u)=eta w(eta u)/(1+exp(-d u))` for `u>=0`, `F(z)=int_0^infty exp(-zu) f(u) du`. The zero-detector case is `d=2sigma-1`. Fix `a in [-eta,d+eta]`, `y in R`, and define

`B(a,y) = Re F(a+iy) + Re F(d-a+iy)`.

The opposite imaginary sign in the second `F` is irrelevant under `Re`, since `f` is real.

## 2. Proven paired-positivity and uniform error lemma

**Theorem (conditional only on the explicitly stated published w-input).**

(A) For `0 <= a <= d`, **`B(a,y)>=0` for all real y**.

(B) For `-eta <= a <= d+eta` and `y!=0`, **`|B(a,y)| < 38 eta/y^2`**.

*Proof of A.* Let `G(z)=F(z)+F(d-z)`. On the line `Re z=0`, exactly

`Re G(iy)=int_0^infty eta w(eta u) cos(yu)du=Re W(iy/eta)>=0`.

By reflection the same holds on `Re z=d`. On the closed strip `0<=Re z<=d`, `G` is bounded and analytic (finite-support f; both Laplace factors have modulus <=1). Thus `exp(-G(z))` is bounded analytic with boundary modulus <=1. Hadamard's three-lines theorem gives modulus <=1 inside, hence `Re G(z)>=0`. This is the desired `B(a,y)>=0`.

*Proof of B.* Write

`q_a(u) = (exp(-au)+exp(-(d-a)u))/(1+exp(-du)) = cosh((a-d/2)u)/cosh(du/2)`;
`g_a(u)=eta w(eta u)q_a(u)`.

Then `B(a,y)=int_0^(U/eta) g_a(u) cos(yu)du`. Because `q_a'(0)=0`, `w'(0)=0`, `w(U)=w'(U)=0`, the boundary terms in twice integrating by parts vanish. Therefore

`|B(a,y)| <= y^(-2) int_0^(U/eta) |g_a''(u)|du`.

For the stated `a`-range, `q_a(0)=1`, `0<q_a(u)<=exp(eta u)`, and `q_a` is monotone in `u`: decreasing when `0<=a<=d`, increasing otherwise. (Differentiate the logarithm of the cosh quotient and use that `r*tanh(ru)` increases with `r>=0`.) As `U<1.06` and `exp(U)<3`, this gives `q_a<=3` on the support and `int_0^(U/eta)|q_a'|du <= 2`.

The exact trigonometric bounds verified by the bundled **rational-interval** program (not by float rounding) are

`0<=w<=w(0)<5.7`, `|w'|<99`, `|w''|<234` on `[0,U]`.

The bounds on `w'` and `w''` follow directly from differentiated formulae and the certified simple inequalities `sec^2 theta<5.59`, `tan theta<2.141`, `theta cot theta<0.53`, `csc theta<1.11`, `csc(2theta)<1.31`. Positivity/decreasing on the *entire* `[0,U]` are the published input noted above.

Product differentiation bounds the first two pieces of `g_a''` by

`eta^3 int |w''(eta u) q_a(u)|du <= eta*(eta0 *234*1.06*3) < 5.358 eta`,

`2 eta^2 int |w'(eta u) q_a'(u)|du <= eta*(4 eta0*99) < 2.852 eta`,

with `eta0=0.0072`. For the last piece put `h(u)=1/(1+exp(-du))`, `c1=a`, `c2=d-a`, so `q_a=h(e^(-c1u)+e^(-c2u))`. Each `ci>=-eta`, `c1+c2=d`, and at most one `ci` is negative. Use `h<=1`, `h'<=d exp(-du)` and `|h''|<=d^2 exp(-du)`. Then, over `u in [0,U/eta]`,

`int|q_a''|du <= I1+I2+I3`, where

`I1<=1+3eta0=1.0216`,
`I2<=2(1+2eta0)/(1-eta0/0.9869)<2.044`,
`I3<=2/(0.9869-eta0)<2.042`.

Hence `eta int w(eta u)|q_a''(u)|du < 5.7*(1.0216+2.044+2.042)eta`. The sum of all three contributions is **strictly below `38 eta`**, by the bundled rational checker. This proves B. No zeta-zero assumptions occur.

## 3. Independent rational certification of the prime-length floor

**Theorem.** In the more restrictive range `eta<=0.007163` and `d>=0.9869`, the exact logistic f satisfies **`f(u)>=f(0)=eta w(0)/2` for every `0<=u<=59`**.

Proof: On `[0,0.423]`, `w>0` and `K(v):=w(v)w''(v)-w'(v)^2<0`. The supplied standard-library-only `check_exact_logistic.py` verifies this by **424 exact-rational interval evaluations** at `v=k/1000`, an explicit global derivative bound `|K'|<26500`, and a width `1/1000`; the certified worst remaining negative-sign margin is >49.47. All sin/cos enclosures use rational Taylor series and exact remainder inequalities; the verifier uses no floating point in pass/fail gates.

Thus `log w` is strictly concave on `[0,0.423]`. Also `log[(1+exp(-d u))^-1]` is concave on `[0,59]`. Hence `log f` is concave on `[0,59]`. Its minimum is at an endpoint. With `eta0=0.007163`, `d0=0.9869`, monotonicity in eta and d and the certified endpoint bound give

`f(59)/f(0) >= 2w(59eta0)/(w(0)(1+1/1000)) >1.0015`.

Here `exp(-d*59)<1/1000` is elementary for `d>=0.9869`. Therefore the minimum is `f(0)`, proving the claim. The result is completely separate from the location of zeta zeros.

**Genuine prime-arithmetic consequence, with explicit source dependence:** Since all `Lambda(n)` are nonnegative and Bellotti–Trudgian–Yang's selected trigonometric polynomial `P(theta)` is nonnegative, their published lower bound `sum_{p<100} log p m_p > 0.23545` (paper Lemma 10, Table 1) now implies

`sum_{n>=1} Lambda(n) n^(-sigma) f(log n) P(t log n) >0.23545 f(0)`,

provided `0.99345<=sigma<1`, `eta<=0.007163`, `d=2sigma-1>=0.9869`, and their `P` and table hypotheses are used. This prime sum bound is *conditional on their published finite-prime table*, not independently re-certified here. **Do not compare `0.23545 f(0)` to their `0.1186 f(0)` without correcting their base-kernel notation; these `f(0)` symbols do not have consistent meaning in the printed proof.** The actual raw lower floors in units `eta w(0)` are ~`0.5` (logistic) and `433/859≈0.504` (polynomial), nearly equal, not twice different.

## 4. Two source-specific notation/sign issues (arXiv v1)

**(i) Printed Lemma 9 normalization.** For the *polynomial* source weight `f_poly(u)=g(u)sum_{m=0}^6 kappa_m exp(-mdu)` with `g(u)=eta w(eta u)`, it is an elementary exact identity that

`f_poly(0)=g(0) kappa`, `kappa=sum kappa_m=433/859`.

Line-by-line application of the general explicit formula to shifted `g` gives the gamma term

`g(0) sum kappa_m gamma_function(s+md)`, **not** `f_poly(0) sum kappa_m gamma_function(s+md)` as literally printed in the v1 Lemma 9 display and its proof (PDF page 15). That displayed replacement inserts an extra factor `kappa`. Crucial qualification: several subsequent numerical formulas behave **as though `f(0)` denotes `g(0)`**, so this may be a consistent repairable *notation* error rather than a fatal flaw in the announced zero-free theorem. The paper has not been completely reverified here. Do not claim that its theorem is disproved.

**(ii) Printed single-transform top-edge asymptotic.** The paper's PDF page 10 states that `Re F_poly(x+iT) = eta w(0)(kappa+o(1))/T^2>0` uniformly for `0<=x<=d`. But using `w'(0)=0` and its own `W(z)=w(0)/z+O(|z|^-3)` at large imaginary argument yields exactly

`lim_{T->infty} T^2 Re F_poly(x+iT) = eta w(0)[kappa*x + d*S1]`,

where `S1=sum m*kappa_m = -216/859` by exact rational calculation. At `x=0` this limit is **negative**. So the printed *individual-F* positive-top-edge argument is incorrect. However, the *paired* transform has the different limit

`lim_{T->infty} T^2 [Re F_poly(x+iT)+Re F_poly(d-x+iT)] = eta w(0)*d*(kappa+2S1) = eta w(0)*d/859 >0`.

That gives a plausible repair to the top-edge positivity needed for the theorem: apply the maximum principle to the paired function, not the individual F. It does **not** automatically validate all remaining paper estimates. The source's exact polynomial coefficients and both rational identities were independently checked.

## 5. RH frontier, stop/go, and required next theorem

- **Passed:** exact logistic paired central-strip positivity, an explicit `38 eta/y^2` offstrip error bound, and rationally certified prime-length floor, all within the stated parameter range.
- **Qualified:** the authors' published finite-prime Table 1 was used but not independently rerun; source v1 has repairable-looking formula/notation problems. No RH claim from the source has been fully validated in this work.
- **Not proved:** effective Guinand–Weil explicit-formula remainder and full finite-height scalar inequality for the **exact logistic weight**. Without them, there is **no new zero-free region and no exclusion beyond the accepted published baseline**.
- **Specific future GO condition:** Derive an explicit formula directly for `f(u)=eta w(eta u)/(1+exp(-du))`, with archimedean coefficient exactly `f(0)` (not an extra `kappa`) and explicit uniform error in the range `t>=3*10^12`, `eta<=0.007163`, `d=2sigma-1`. Then rigorously check the complete scalar contradiction at a specified A greater than the verified literature constant, including all finite errors and real σ-range. **STOP** if the corrected gamma term or error budget prevents any strictly stronger A. Do not launch an open-ended Codex campaign to repeat scalar parameter fitting.
- **Status:** RH OPEN, complete Haglund Conjecture 4 k=2/k=3 UNVERIFIED, marked moment `BLOCKED_NEW_MOMENT_ESTIMATE`, historical provenance `BLOCKED_UNWAIVED`.

The exact verifier prints all pass conditions, interval margins, and the rational sums; no `sorry`/custom axioms are involved. Lean 4 is not installed in this container, so none of these continuous analytic results is claimed Lean-checked. The finite arithmetic is checked with a deterministic rational program, not Arb or Lean. These artifacts are held separately from the original master ZIP and historical WSL materials.
