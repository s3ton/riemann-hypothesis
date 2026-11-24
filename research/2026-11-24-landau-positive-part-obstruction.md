# Landau positive-part window: verified bottleneck and sparse-scale obstruction

**Investigation date:** 2026-11-24  
**Status:** SOURCE-VERIFIED ANALYTIC BRIDGE; MATHEMATICAL CONTRAPOSITIVE; NO INDEPENDENT GRH ESTIMATE PROVED.  
**Source:** `main` declarations inspected via GitHub.  
**Lean check:** not run; this is a research note, not a typechecked Lean proof.

## 1. Exact smoothed character-family expressions (source-verified)

[`CharFamily.lean`](../src/Development/AutomorphicArithmetic/DedekindLFunctions/CharFamily.lean) defines:

```lean
def ramp (f : ℕ → ℂ) (y : ℝ) : ℂ :=
  ∑ n ∈ Finset.range (⌊y⌋₊ + 1), (Λ n : ℂ) * f n *
    ((max (y / n - 1) 0 : ℝ) : ℂ)
```

`Gchi χ y` is this ramp with the following centering:
- `χ = 1`: subtract `y * log y` and add `(1 + EulerMascheroniConstant) * y`;
- `χ ≠ 1`: add `y * (L'(1,χ) / L(1,χ))`.

A `Deduction.CharFamily` has a finite index type, positive real weights and the admissibility condition `N i = 1 ∨ χ i ≠ 1`. It defines

```lean
def Gm (F : CharFamily) (y : ℝ) : ℝ :=
  ∑ i, F.a i * (Gchi (F.χ i) y).re
```

The actual `WindowHyp F θ δ` quantifies over every `η > 0`, every real lower threshold `Y₀`, and asks for some `Y ≥ Y₀` with a nonnegative pointwise majorant `R ≥ Gm F` on `[Y,Y^(1+δ)]`, local integrability of `R(y)*y^(-θ-1)`, and

```text
∫ y in Set.Icc Y (Y ^ (1 + δ)), R y * y ^ (-θ - 1) ≤ Y ^ η
```

On positive compact windows the ramp and centering terms are continuous, hence `R(y) = max (Gm F y) 0` is locally integrable. This positive part is the pointwise smallest eligible nonnegative majorant. The positive-part formulation is equivalent to `WindowHyp` for sufficiently large `Y > 1` (the threshold is arbitrary).

**Important correction to earlier sketches:** the exponent `3/2` is the optional choice `δ = 1/2`; the source theorem accepts every fixed `δ > 0`. Do not discard the majorant's integrability or the quantifiers when copying the Lean statement.

## 2. Verified zero-exclusion bridge

[`LandauZeroFreeCriterion.lean`](../src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauZeroFreeCriterion.lean) defines `gm F u = Gm F (exp u)`, `WindowHypU` on logarithmic windows, and `PoleData` for a Laplace transform with meromorphic poles at zeros.

[`WindowHypUOfWindowHyp.lean`](../src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/WindowHypUOfWindowHyp.lean) proves `windowHypU_of_windowHyp` by the change of variables `y = exp u`.

[`landauWindow.lean`](../src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/landauWindow.lean) proves

```lean
theorem landau_window {g : ℝ → ℝ} {Φ : ℂ → ℂ} {Z : Set ℂ}
    (hP : PoleData g Φ Z) {θ δ : ℝ}
    (hθ : 0 < θ) (hθ1 : θ < 1) (hδ : 0 < δ)
    (hW : WindowHypU g θ δ) :
    ∀ ρ ∈ Z, ρ.re ≤ θ := by ...
```

[`lemmaL.lean`](../src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/lemmaL.lean) proves

```lean
theorem lemmaL (F : CharFamily) {θ δ : ℝ}
    (hθ : 0 < θ) (hθ1 : θ < 1) (hδ : 0 < δ)
    (h : WindowHyp F θ δ) :
    ZeroFree F θ := by ...
```

The proof calls `poleData F`, `landau_window`, and `windowHypU_of_windowHyp`, and handles `Re s ≥ 1` using classical L-function nonvanishing. No `HostExW`, `TopG`, `VWin` or `VVle` is a hypothesis of `lemmaL`.

[`Window.lean`](../src/Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/Window.lean) defines `Level.FormBAt` from arbitrarily late power windows to `Level.ZeroFreeAbove`. [`PrimitiveCosets/Imports.lean`](../src/Development/AutomorphicArithmetic/PrimitiveCosets/Imports.lean) proves `UpperTheory.Comparison₂.formB` using the analytic character-family route. The earlier [`ZeroFreeAllOfTopG.lean`](../src/Development/AutomorphicArithmetic/CharacterBoxes/ZeroFreeAllOfTopG.lean) still supplies its windows through `TopG` and `HostExW`, rather than through an independent analytic estimate.

## 3. Mathematical obstruction to sparse power windows (derived from the verified Landau theorem)

Fix an admissible family `F`, `0 < θ < 1`, and a fixed `δ > 0`. Define, for `Y > 1`,

```text
A(Y) = ∫_[Y,Y^(1+δ)] max (Gm F y) 0 * y^(-θ-1) dy.
```

**Proposition (mathematical deduction, not separately formalized):** If a member of the family has a zero `ρ` with `Re ρ > θ`, then

```text
∃ η > 0, ∃ Y₀ > 1, ∀ Y ≥ Y₀, A(Y) > Y^η.
```

**Proof:** Otherwise the negation gives, for every `η > 0` and arbitrarily large lower thresholds `Y₀`, a `Y ≥ Y₀` with `A(Y) ≤ Y^η`. Use `R(y)=max(Gm F y,0)` on each positive window, yielding `WindowHyp F θ δ`; then `lemmaL` excludes that zero, a contradiction.

Thus **even an arbitrarily sparse set of favorable full power windows is sufficient to exclude zeros**, but a hypothetical off-line zero forces *all sufficiently late such windows* to have polynomially large positive mass. Searching for favorable scales alone is not a mathematical escape.

A fixed `θ > 1/2` excludes only zeros to its right, not every off-line zero. For GRH one needs estimates for `θ` arbitrarily close to `1/2` (a countable cofinal sequence suffices), across the required characters. A single fixed `δ>0` is sufficient.

## 4. Zero contribution and failure of signed-integral shortcuts

[`poleData.lean`](../src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/poleData.lean) gives the pole coefficient for a zero of multiplicity `m`:

```text
c_ρ = m * (-1 / (ρ * (ρ - 1))) = m / (ρ * (1 - ρ)).
```

In the associated explicit formula the zero's ramp contribution is of order `y^β` for `ρ=β+iγ`; a nonreal conjugate pair has an oscillatory real part modeled by `2|A|y^β cos(γ log y + φ)`.

Its signed weighted integral contains the oscillatory boundary expression

```text
Re [ exp(iφ) *
     (Y^((1+δ)*(β-θ+iγ)) - Y^(β-θ+iγ))/(β-θ+iγ) ].
```

For `γ ≠ 0` this isolated contribution takes both signs on arbitrarily large scales. Thus a *signed* upper bound along selected scales does not control its positive part; one cannot infer zero exclusion solely from that cancellation.

Multiple zeros can also interfere, so the positive part of one zero contribution is not a rigorous lower bound for the positive part of the full sum. The repository's `landau_window_key` and `landau_window` address this with high-order derivatives and nearest-pole asymptotics, not by assuming one zero dominates pointwise.

In particular, `landau_window_key` bounds (schematically; `σ>2`, `k≥U`)

```text
|(-1)^k Φ^(k)(σ+iγ)/k!| + Re[(-1)^k Φ^(k)(σ)/k!]
    ≤ C exp(η U) / (σ-θ)^k.
```

This is a tighter *analytic interface*, but no independent method for proving it was obtained; merely assuming it also fails the shortcut standard.

## 5. Three proof avenues: status

| Attempt | Concrete observation | Outcome |
| --- | --- | --- |
| Euler product / positivity | Weighted von Mangoldt positivity is unconditional for `Re s > 1`; termwise positivity cannot be transferred to `Re s > 1/2` by analytic continuation. | B: no independent square-root control |
| Sparse or mean-square prime sums | The Landau contrapositive rules out avoiding the positive-part obligation by sparse **full power** windows. A mean-square bound strong enough for Cauchy–Schwarz to yield the window estimate is likewise GRH-hard; averages over moduli alone do not control each exceptional character. | B, or C for inadequate signed/pointwise variants |
| Direct cohomology replacement | `vvRecord` exports `ShaFinOdd`, summability and a scalar `vvTerm` budget. The use in `divinN_of_hypV` can in principle be replaced by an independently established `DIVinN` estimate on chosen families; no such estimate has been proved. | D: follow separate `DIVinN_at` note |

The full universal positive-part window statement is **GRH-equivalent under standard explicit-formula estimates**: its sufficiency follows from `lemmaL`; the GRH-to-bound direction is standard analytic reasoning and **was not formalized or separately verified here**. It is incorrect to claim that changing `HostExW` to this hypothesis independently proves GRH.

## 6. Lean and dependency status

- A proposed isolated singleton-family `MinimalAnalyticEstimate` module was sketched outside the repository; it was **not compiled or committed**.
- No `theorem minimalAnalyticEstimate : MinimalAnalyticEstimate` proof exists.
- No new axioms, `sorry`, changes to theorem signatures, or imports are included in this PR.
- Direct use of `lemmaL` provides a plausible **hypothetical** logical path avoiding `TopG` in the proof body, but no unconditional proof-constant or transitive-import reduction has been measured.

**Decision:** Do not promote the analytic window assumption to a completed shortcut. Keep the direct `DIVinN_at` arithmetic investigation separate and record its independent proof obligation in [the numerical bottleneck note](2026-11-24-divinn-arithmetic-bottleneck.md).

## Next decisive theorem for this route

An independently proved, uniform `WindowHyp F θ (1/2)` estimate for each needed primitive character and for `θ` arbitrarily close to `1/2`. This is currently **unproved** and GRH-hard in its universal form; no evidence from this investigation establishes it is easier than the existing Galois-cohomological input.
