import Std
open Std Lean.Grind
namespace MarkedGate
attribute [local instance] Semiring.natCast Ring.intCast
variable {R : Type u} [Field R] [LE R] [LT R]
  [LawfulOrderLT R] [IsLinearOrder R] [OrderedRing R]

-- The source's literal formal centers; no Poisson theorem is assumed here.
theorem initial_margin_identities (m r z G P : R) :
    let D := r+z-2*G
    let F := D-P
    let M := 2*D-m-2*P
    let Q := P+G
    let z0 := z-G
    F-M-Q-z0 = m-r-2*z+2*G ∧
    4*F-3*M-6*z0 = 3*m-2*r-8*z+10*G+2*P ∧
    F-M-Q = m-r-z+G := by dsimp; grind

-- Old positive margins imply the new ones; the converse is the disputed claim.
theorem old_implies_new (m r z : R) (hz : 0 ≤ z) (h : r+2*z < m) :
    r+z < m := by grind

theorem admissibility_counterexample :
    (4/5 : R)+(3/20) < 1 ∧
    2*(4/5 : R)+8*(3/20) < 3 ∧
    1-(4/5 : R)-2*(3/20) < 0 := by grind

-- Exact point of the actual supplied gate, delta=x=1/2; reconstruction is
-- checked independently in the Fraction certificate, not hidden in this theorem.
theorem gate_point_margin :
    let r : R := 467988598319/670130653625
    let z : R := 133631714876/670130653625
    1-r-z = 13702068086/134026130725 ∧
    1-r-2*z = -(65121374446/670130653625) ∧
    3-2*r-8*z = 1/125 ∧
    0 < 1-r-z ∧ 1-r-2*z < 0 ∧ 0 < 3-2*r-8*z := by dsimp; grind

-- Even allowing favorable clipping of at most 3 eta cannot repair a fixed
-- negative formal margin when eta is chosen small; row enlargement only hurts.
theorem clipping_does_not_repair (gap clip eta rowLoss : R)
    (hgap : gap < 0) (hc : clip ≤ 3*eta) (he : 3*eta < -gap)
    (hl : 0 ≤ rowLoss) : gap+clip-rowLoss < 0 := by grind

-- Normalizing a positive row width preserves both proposed conditions.
theorem positive_width_normalization (m r z : R) (hm : 0 < m) :
    (r+z < m ↔ r/m+z/m < 1) ∧
    (2*r+8*z < 3*m ↔ 2*(r/m)+8*(z/m) < 3) := by
  have hn : m ≠ 0 := by grind
  have hi := Field.IsOrdered.inv_pos_iff.mpr hm
  have eq1 : (m-r-z)*m⁻¹ = 1-r/m-z/m := by grind
  have eq2 : (3*m-2*r-8*z)*m⁻¹ = 3-2*(r/m)-8*(z/m) := by grind
  have eq3 : (1-r/m-z/m)*m = m-r-z := by grind
  have eq4 : (3-2*(r/m)-8*(z/m))*m = 3*m-2*r-8*z := by grind
  constructor
  · constructor
    · intro h
      have hp := OrderedRing.mul_pos (a := m-r-z) (b := m⁻¹) (by grind) hi
      rw [eq1] at hp; grind
    · intro h
      have hp := OrderedRing.mul_pos (a := 1-r/m-z/m) (b := m) (by grind) hm
      rw [eq3] at hp; grind
  · constructor
    · intro h
      have hp := OrderedRing.mul_pos (a := 3*m-2*r-8*z) (b := m⁻¹) (by grind) hi
      rw [eq2] at hp; grind
    · intro h
      have hp := OrderedRing.mul_pos (a := 3-2*(r/m)-8*(z/m)) (b := m) (by grind) hm
      rw [eq4] at hp; grind

-- Squarefree inverse and disjoint squarefree prime product give valuations <=2.
-- Equality modulo six therefore gives no distinct pure sixth-power aliases.
theorem no_sixth_power_alias (a b : Nat) (ha : a ≤ 2) (hb : b ≤ 2)
    (hmod : a % 6 = b % 6) : a=b := by omega

-- At one product index, fixing the number of prime slots fixes the parity
-- of the squarefree inverse length; a full-divisor Mobius cancellation is absent.
theorem same_mobius_sign (a b K total : Nat)
    (ha : a+K=total) (hb : b+K=total) : (-1 : Int)^a = (-1 : Int)^b := by
  have h : a=b := by omega
  rw [h]

-- Scalar exponent check for any capacity whose decrease is at most r's increase.
-- A genuine arithmetic moment bound is still needed before using this exponent.
theorem inverse_capacity_monotone (r s zr zs x delta : R)
    (hrs : r ≤ s) (hx : 0 ≤ x) (hu : 2*x ≤ 1) (hd : 0 ≤ delta)
    (hcap : zr-zs ≤ s-r) :
    1-delta*s-2*delta*x*zs ≤ 1-delta*r-2*delta*x*zr := by
  have h1 := OrderedRing.mul_nonneg (a := (s-r)-(zr-zs)) (b := 2*x)
    (by grind) (by grind)
  have h2 := OrderedRing.mul_nonneg (a := s-r) (b := 1-2*x)
    (by grind) (by grind)
  have hg : 0 ≤ s-r-2*x*(zr-zs) := by grind
  have h3 := OrderedRing.mul_nonneg (a := delta) (b := s-r-2*x*(zr-zs)) hd hg
  grind

-- Conditional endpoint arithmetic only, without a zero-free theorem premise.
theorem endpoint_and_license :
    (11/12 : R)-(21/125)/4 = 328/375 ∧
    (8748867/10000000 : R) < (1+29991/40000)/2 := by grind

end MarkedGate
#print MarkedGate.initial_margin_identities
#print axioms MarkedGate.initial_margin_identities
#print MarkedGate.old_implies_new
#print axioms MarkedGate.old_implies_new
#print MarkedGate.admissibility_counterexample
#print axioms MarkedGate.admissibility_counterexample
#print MarkedGate.gate_point_margin
#print axioms MarkedGate.gate_point_margin
#print MarkedGate.clipping_does_not_repair
#print axioms MarkedGate.clipping_does_not_repair
#print MarkedGate.positive_width_normalization
#print axioms MarkedGate.positive_width_normalization
#print MarkedGate.no_sixth_power_alias
#print axioms MarkedGate.no_sixth_power_alias
#print MarkedGate.same_mobius_sign
#print axioms MarkedGate.same_mobius_sign
#print MarkedGate.inverse_capacity_monotone
#print axioms MarkedGate.inverse_capacity_monotone
#print MarkedGate.endpoint_and_license
#print axioms MarkedGate.endpoint_and_license
