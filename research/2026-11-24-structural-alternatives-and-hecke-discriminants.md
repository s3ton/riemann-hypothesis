# Structural alternatives and a discriminant bound for the local Hecke defect

**Date:** 2026-11-24  
**Status:** NEW ALGEBRAIC LEMMA PROVED ON PAPER; FAMILY DISCRIMINANT BUDGET UNPROVED; NO GRH SHORTCUT.  
**Base audited:** `main`; this note is documentation on the existing research PR, not a Lean theorem.  
**Lean compilation / CI:** neither attempted. No imports, theorem signatures or proof files changed.

## 1. Actual endpoint and architectural boundary (source verified)

- [`src/Main.lean`](../src/Main.lean) obtains `LFunction_ne_zero_of_half_lt_re` from `UpperTheory.FinalTheorems.everyCharacter`; `src/Statements.lean` records its precise nonvanishing predicate.
- [`MainConclusion.lean`](../src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean) builds `everyCharacter` from `everyCharacter_of_row`, `every_character_of_literature_of_vWin`, and `vwin_of_row`. The immediate source-level proof depends on a Galois local-global statement.
- [`EveryCharacterOfLiteratureOfVWin.lean`](../src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean) assembles a large literature-input record and calls `UpperTheory.Lit.every_character_of_theta_integrals_local_matching`, passing `hV` as a separate input. The full transitive proof-constant graph was **not** enumerated.
- [`TopPlug.lean`](../src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean), [`TopShape.lean`](../src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopShape.lean), [`DesWin.lean`](../src/Development/AutomorphicArithmetic/CharacterBoxes/DesWin.lean), and [`ZeroFreeAllOfTopG.lean`](../src/Development/AutomorphicArithmetic/CharacterBoxes/ZeroFreeAllOfTopG.lean) exhibit two separate inputs: a family-connectivity `TopG` proof and a `HostExW` supply. `topDesWin` consumes `DIVinN` through `LinkDIVt` and `LinkMu`; the analytic Landau criterion consumes neither `DIVinN` nor local Hecke data directly.
- [`PrimitiveCosets/Imports.lean`](../src/Development/AutomorphicArithmetic/PrimitiveCosets/Imports.lean) proves `formB` via a concrete character family and `zeroFree_of_rpow_window`. It is an actual analytic endpoint; a universal power-window bound is not an independently proved shortcut.

**Dependency caution.** These are source-level applications, not a measured proof-constant cut, nor evidence that `src/Main.lean` can compile with the geometric imports removed. `src/Challenge.lean` has placeholder statements but is **not** an import of `src/Main.lean`; do not use that file to assess this endpoint.

## 2. New source fact: `etaLoc` is a projection-lattice defect (verified)

[`LevelLetterCocycles/DataN.lean`](../src/Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean) defines a local DVR `O i`, a finite nonempty eigenvalue set `X i`, a point-separating Hecke subalgebra `T i : Subalgebra (O i) (X i → O i)`, a finite free `T i`-module `Mt i`, and a subset `Zgood i`. In `NData`:

```lean
def MtIn (i : N.Loc) := ... -- integral lattice M in its fraction-space
def MtUp (i : N.Loc) :=
  (N.eigSum i ↑(N.Zgood i)).restrictScalars (N.O i) ⊓
    (N.MtIn i ⊔ (N.eigSum i (↑(N.Zgood i))ᶜ).restrictScalars (N.O i))
def MtLow (i : N.Loc) :=
  N.MtIn i ⊓ (N.eigSum i ↑(N.Zgood i)).restrictScalars (N.O i)
def etaLoc (i : N.Loc) : ℚ :=
  lenUnit (O := N.O i) (N.l i)
    (↥(N.MtUp i) ⧸ (N.MtLow i).comap (N.MtUp i).subtype)
```

Here `lenUnit O l Q = length_O(Q) / length_O(O/lO)` (with natural finite lengths cast to rationals). The eigenspace decomposition over the fraction field identifies `MtUp=e_Z M` and `MtLow=M∩e_Z V`, where `e_Z` is the idempotent for `Zgood` and `V=K⊗_O M`. The identification is an **independent mathematical deduction**, not a new compiled Lean equality.

## 3. Local discriminant lemma — mathematical proof, independent of cohomology

**Proposition.** Let `O` be a DVR with uniformizer `π`, fraction field `K`, and normalized valuation `v_π(π)=1`. Let `X` be a finite set and `T⊂O^X` an `O`-subalgebra containing constants and separating every two distinct points. Let `M` be a free `O`-module of rank `r<∞` with an `O`-linear `T`-action. Put `V=K⊗_O M`. For any `Z⊆X`, write `e_Z=1_Z∈K^X`, `V_Z=e_ZV`, and
```
  M_up   = V_Z ∩ (M + V_(X\Z)) = e_Z M,
  M_low  = M ∩ V_Z.
```
Then the quotient `Q_Z=M_up/M_low` is of finite length and
```
  length_O(Q_Z) ≤ r * h,
  h = length_O(O^X/T) = (1/2) v_π(disc(T)).
```
Here `disc(T)` is the discriminant for the multiplication-trace pairing on the split finite étale generic algebra `K^X`, computed from an `O`-basis of `T`.

**Proof.** Given `x≠y`, choose `f_xy∈T` with `f_xy(x)≠f_xy(y)`. The product `g_x=∏_(y≠x)(f_xy-f_xy(y))` lies in `T`, vanishes at all `y≠x`, and is nonzero at `x`; after division by `g_x(x)` in `K`, it is the coordinate idempotent `e_x`. Thus `K⊗_O T=K^X` and `O^X/T` has finite `O`-length `h`. Since `π^h` annihilates every finite-length `O`-module of length `h`, `π^hO^X⊆T`, in particular `π^he_Z∈T`. Applying the action to `M` gives `π^he_ZM⊆M∩V_Z`. Therefore `π^hQ_Z=0`. The `O`-module `e_ZM` is generated by at most `r` elements, giving `length_O(Q_Z)≤rh`. For the equality with discriminant, an `O`-basis of `T` has coordinate-change determinant of `π`-valuation `h` relative to `O^X`; the multiplication trace on `O^X` has determinant `1`, so `v_π(disc(T))=2h`. QED.

**Corollary for `NData` (conditional on the standard fraction-field identifications and finite normalized lengths):** for `r_i=rank_(O i)(Mt i)`, `e_i=length_(O i)((O i)/(l_i))>0`, and `d_i=v_(π_i)(disc(T i))`,
```
  0 ≤ N.etaLoc i ≤ r_i * d_i / (2 * e_i).
```
The field-extension and integral-identification assumptions are supplied by the local `NData` setup; a Lean theorem establishing this corollary has **not** been compiled.

**Rank-two obstruction sharpness.** For `T_n={(a,b)∈O²:a≡b mod π^n}` and `M=O²` with coordinate action, choose `Z={1}`. Then `e_ZM=O×0`, `M∩V_Z=O×0` for this *standard* lattice, so the defect is zero; **this example alone does not realize a deep lattice defect**. Instead choose the `T_n`-stable lattice `M=T_n⊂K²`. Then `e_ZM=O×0`, `M∩V_Z=π^nO×0`, hence `length(Q_Z)=n`. Also `h=length(O²/T_n)=n` and `disc(T_n)=π^{2n}` up to a unit. The discriminant estimate detects the correct growth while rank stays two. No claim is made that every such abstract order is realizable by the constructed `D7` families.

## 4. Structural alternatives and obstructions

| Idea | Finding | Classification for an independent GRH proof |
| --- | --- | --- |
| Weil explicit-formula positivity | Positivity on all suitable test functions is a known GRH criterion; no independent positivity proof identified. | **B** |
| Direct de Branges/Hilbert–Pólya space | Lagarias proves the required de Branges property of his explicit `E_χ` is equivalent to RH for the corresponding Dirichlet `L`. Postulating that property is circular. | **B** |
| Real-valued functorial `H^1` with Artin zero spectrum | Deninger (Theorem 2.13) proves a no-go theorem for an expected real-valued functorial cohomology carrying the exact central Artin multiplicities, using quaternionic root number `-1`. The theorem **does not** rule out complex/quaternionically graded cohomology or a Dirichlet-only construction. | **C for that specified real-valued model** |
| Existing Weil-étale theory | Morin constructs complexes computing expected Weil-étale cohomology for number fields. This alone supplies neither a self-adjoint zero-spectrum operator nor the requisite positivity. | **B as a zero-exclusion solution** |
| Boundary unitarity of a scattering function | `S_ρ(s)=(s-ρ)/(s-(1-conj(ρ)))` has modulus `1` on `Re(s)=1/2` (away from poles) but a zero at `ρ` off-line. Thus abstract boundary unitarity does not imply off-line zero exclusion. This is a toy counterexample, **not** a Dirichlet L-function. | **C for the bare unitarity claim** |
| Local Hecke discriminant | The proposition above proves a real local estimate from the *actual shape* of `NData.etaLoc`. Uniform family discrimination bounds remain unknown. | **A locally; D globally** |

External references: [Weil's positivity criterion](https://openmaths.org/courses/NT-EXPF/NT-EXPF-04.html); [Lagarias, *Hilbert Spaces of Entire Functions and Dirichlet L-Functions*](https://websites.umich.edu/lagarias/doc/debranges-houches.pdf); [Deninger, *There is no "Weil-"cohomology theory with real coefficients for arithmetic curves*](https://arxiv.org/abs/2204.02714); [Morin, *On the Weil-étale cohomology of number fields*](https://arxiv.org/abs/1006.0521).

## 5. Exactly one decisive next theorem — constructed-family discriminant budget

**Status: UNPROVED (D); not GRH-equivalent merely by definition, but its independent difficulty is unknown.**

Let `Fm : FamP eps` be a family actually constructed in the `TopShape` route, with `eps>0`, and write `D=Fm.D x i`, `L=Fm.L x i`, and `S={w∈L.supp | D.what₂.muAt w ≠ D.what₂.mu0}`. For `t∈D.nd.locs j w`, define
```
  R_t = rank_(O_t)(Mt_t),
  E_t = length_(O_t)(O_t/(l_t)) > 0,
  Δ_t = v_(π_t)(disc(T_t)).
```
Prove, using only independently established arithmetic properties of the *selected* families, that for this `Fm` there are uniform constants `C≥0`, `x0>1` such that for every `x≥x0`, `i : Fm.Ix x`, and `j∈[1,D.R.m]`,
```
  Σ_(w∈S) [lwP(w) * ramIdx(w)] *
       Σ_(t∈D.nd.locs j w) [R_t * Δ_t / (2*E_t)]
    ≤ (D.what₂.D0) * C * x^eps * (L.B0 + L.Nc).
```
Also verify from source the sign of each place weight, the `D7.etaJ_tie` identity (reported by preceding research), and all local finite-length identifications. With these established, the proposition yields `etaSum≤` left-hand side and the bound implies `DIVinN Fm`. It would replace the **specific** `VVle→vvRecord→divinN_of_hypV` numerical step in `topDesWin`, but it **does not bypass `TopG`, `HostExW`, family construction, or the final Landau criterion**.

**First independently unproved lemma:** a uniform, family-specific bound on the discriminants `Δ_t` of the *actual* Hecke orders summed over exceptional primes. The finite-rank hypothesis and the full `NData` structure do not imply this bound by themselves; no conductor/discriminant estimate sufficient for these families has been verified. The `D0=0` case forces the left-hand side to vanish and requires separate justification.

This is the most concrete *non-tautological arithmetic* candidate presently obtained; it is **not** evidence for the desired complete structural bypass. No proof-constant dependency reduction or Lean compilation is claimed.
