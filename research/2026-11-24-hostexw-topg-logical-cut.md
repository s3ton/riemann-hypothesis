# `HostExW` / `TopG` logical cut and remaining dependency audit

**Investigation date:** 2026-11-24  
**Status:** SOURCE-VERIFIED PROOF INTERFACE; CONDITIONAL ANALYTIC REPLACEMENT ONLY; NO INDEPENDENT ESTIMATE PROVED.  
**Source:** `main` files inspected through GitHub.  
**Lean check:** not run; no Lean code is introduced or claimed compiled.

## 1. Exact consumption of `HostExW` (verified from source)

[`CharacterBoxes/ZeroFreeAllOfTopG.lean`](../src/Development/AutomorphicArithmetic/CharacterBoxes/ZeroFreeAllOfTopG.lean) defines:

```lean
def TopG : Prop :=
  ∀ (la : ℝ) (G : FReq), 1 < la → HostExW la G.req →
    (∀ {eps : ℝ} (Fm : FamP eps), G.cls la Fm → HypV Fm.toFamCore) →
    FamilyClassConnected (G.cls la)
```

In the proof of `UpperTheory.Top.zeroFreeAll_of_topG`, the only invocation of the `HostExW` input is via `TopG`:

```lean
obtain ⟨eD, eL, ε₁, h1, h2⟩ :=
  h la (GChi ψ) hla (hS ψ) (hypV_of_cls ψ la)
```

This constructs the family/window witness consumed by `zeroFreeOn_of_tiedWin_cyc`. No host appears in the *final analytic zero-exclusion criterion*; the host is one way to supply its bound. This is an interface reduction, not an independent proof.

[`CharacterBoxes/Supply.lean`](../src/Development/AutomorphicArithmetic/CharacterBoxes/Supply.lean) defines
`GChi ψ` by the conjunction of `EAtH (Level.cyc ψ) ... 4` and `VVle H.E t (Real.sqrt s.b)`. The latter is the cohomological input inside the class. [`SupplyChi.lean`](../src/Development/AutomorphicArithmetic/CharacterBoxes/SupplyChi.lean) proves:

```lean
UpperTheory.Top.supplyChi :
  ∀ ψ : PChar, VWinAt ψ 401 → HostExW (3 / 2) (GChi ψ).req
```

The numbers `401`, `4`, and the upper restriction `eps < 1/52` belong to the upstream construction and are **not constants required by the Landau contradiction**.

## 2. Numerical bound used downstream (verified from source)

[`PrimitiveCosets/CoreGm.lean`](../src/Development/AutomorphicArithmetic/PrimitiveCosets/CoreGm.lean) proves `UpperTheory.Comparison₂.core_gm`, with the exponent

```lean
Λ.Gm x ≤ x ^ ((1 : ℝ) / 2 + (eD + eL + 7) * eps)
```

under `EAtH` and `CoreAtH` (and other stated scale hypotheses). [`TopWin.lean`](../src/Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/TopWin.lean) turns the resulting Chebyshev-on-family-windows statement into zero exclusion in `level_of_tiedWin`.

Given a hypothetical zero `s` with `Re s > 1/2`, that theorem defines

```text
m = min (Re s - 1/2) (1/2) > 0
θ = 1/2 + m/2
```

and chooses `eps > 0` with `eps < ε₁` and
`(eD + eL + 7) * eps ≤ m/2`. Hence

```text
Λ.Gm x ≤ x^(1/2 + (eD + eL + 7)*eps) ≤ x^θ
```

on arbitrarily late power windows, with `θ < Re s`.

[`Window.lean`](../src/Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/Window.lean) states the exact downstream criterion:

```lean
def Level.FormBAt (la : ℝ) : Prop :=
  ∀ θ : ℝ, 0 < θ → θ < 1 →
    HasWindows {x | Λ.Gm x ≤ x ^ θ} la →
    Λ.ZeroFreeAbove θ
```

The proved `UpperTheory.Comparison₂.formB` supplies this analytic implication. Thus the **pointwise logical cut** is a `HasWindows` inequality for `(Level.cyc ψ).Gm` for all needed characters and `θ` arbitrarily close to `1/2`; it requires no `HostExW` or `TopG` premise at the final step.

The **weaker integrated positive-part candidate**, including its integrability condition and quantifier caveats, is documented in [the Landau report](2026-11-24-landau-positive-part-obstruction.md). Neither candidate has been proved independently.

## 3. Why eliminating `HostExW` alone is insufficient (verified from source)

[`ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean`](../src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean) assembles:

```lean
UpperTheory.Top.zeroFreeAll_of_topG (la := 3 / 2) (by norm_num)
  (_root_.GlobalTheory.Fc.forall_goal_of_shape_of_hyps _ _ _ _
    (_root_.UpperTheory.Top.shape_closed_link_n_of_green hG)
    trivial trivial h)
  (fun ψ => UpperTheory.Top.supplyChi ψ (hV ψ))
```

Here `shape_closed_link_n_of_green` builds `TopG` from the geometric/automorphic family apparatus and `supplyChi` builds the separate `HostExW` inputs using `VWin`. The former is elaborated in [`TopShape.lean`](../src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopShape.lean) through `topDesWin`, which (as separately documented in the [`DIVinN_at` report](2026-11-24-divinn-arithmetic-bottleneck.md)) invokes `divinN_of_hypV`.

Therefore:
- Replacing `supplyChi` by another way of supplying `HostExW` does not remove the `TopG` machinery.
- Supplying the necessary `Gm` window bound **independently** would bypass both `HostExW` and `TopG` as premises in the zero-exclusion route.
- This is **not yet a demonstrated reduction** of either the actual Lean proof-constant graph or the transitive import graph. No counts are claimed.

## 4. Mathematical obstruction and next decisive obligation

The strongest direct *downstream* requirement found is a universal one-sided window estimate. For example, fixing the permissible window exponent `la = 3/2`, one could seek

```text
∀ primitive ψ, ∀ θ ∈ (1/2,1), ∀ Y₀,
  ∃ Y ≥ Y₀, ∀ y ∈ [Y,Y^(3/2)],
    (Level.cyc ψ).Gm y ≤ y^θ.
```

The integrated positive-part criterion in the Landau report is less demanding than this pointwise bound. Its universal form is effectively GRH-equivalent under standard explicit-formula estimates, and the GRH-to-estimate direction has **not** been formalized.

**First unproved mathematical step:** establish a square-root-threshold positive-part window estimate for the required character families *independently of* `VVle`, `VWin`, `HostExW`, `TopG`, or any comparably strong zero-location theorem. Extracting it as an additional axiom or premise does not count.

**Verification boundary:** no `sorry`/`admit`, Lean proof experiment, new axioms, existing Lean file changes, or CI were used. This note verifies the proof interfaces and identifies an unresolved analytic obligation; it does not provide a GRH shortcut.
