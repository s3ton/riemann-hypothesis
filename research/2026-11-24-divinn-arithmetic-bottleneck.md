# `DIVinN_at`: numerical bottleneck and candidate arithmetic replacement

**Investigation date:** 2026-11-24  
**Status:** SOURCE-VERIFIED REDUCTION; NO INDEPENDENT ARITHMETIC BOUND PROVED.  
**Repository branch inspected:** `main` at time of investigation.  
**Lean check:** not run; this file contains no Lean proof.

## Exact definitions (source-verified)

[`GlobalTheoremInputs.lean`](../src/Formalism/SharpRestriction/GlobalTheoremInputs.lean) defines:

```lean
open Classical in
def etaSum {D : D7} (L : SizeData₂ D) (j : ℕ) : ℝ :=
  ∑ w ∈ L.supp.filter (fun w => D.what₂.muAt w ≠ D.what₂.mu0),
    SizeData₂.lwP w * (D.what₂.places.ramIdx w : ℝ) * (D.what₂.etaJ j w : ℝ)

def DIVinN_at {D : D7} (L : SizeData₂ D) (j : ℕ) (C : ℝ) : Prop :=
  etaSum L j ≤ (D.what₂.D0 : ℝ) * (C * L.sc.x ^ L.sc.eps * (L.B0 + L.Nc))

def DIVinN {eps : ℝ} (Fm : FamP eps) : Prop :=
  ∃ C x0 : ℝ, ∀ x ≥ x0, ∀ i : Fm.Ix x,
    ∀ j ∈ SizeData₂.lifts (Fm.D x i), DIVinN_at (Fm.L x i) j C
```

The same file defines:
- `vvTerm D l`: zero off the rational primes; at primes, a finite sum of `D.what₂.shaLen l e` (as rationals/reals) multiplied by `Real.log l`.
- `ShaFinOdd D`: finite-length condition on `GaloisCohomology.shaLen` at all relevant primes and exponents.
- `LinkN_at L j C`: assuming `Summable (vvTerm D)`, bounds `etaSum` by `L.dZ0 j` times a term containing `C (f m b L² + (log x)² Nc)` and `∑' l, vvTerm D l`.
- `LinkN Fm`: ultimately requires `ShaFinOdd` at large family parameters before producing `LinkN_at`.
- `SmallLevelRankEq Fm`: eventually `L.dZ0 j = D.what₂.D0` on lifts.

[`DataParams₂.lean`](../src/Formalism/LocalRingCardinality/DataParams₂.lean) defines `SizeData₂`, with finite `supp` and `SizeData₂.lwP w = lw D.what₂.LL (D.plEq w)`. It defines:
- `Scale.L = x ^ eps`, `Scale.b = exp (Scale.L)`;
- `SizeData₂.B0 = sizeBudget D.R x eps`;
- `SizeData₂.Nc = budgetNc D.R x eps D.host.T2.card`;
- `SizeData₂.lifts D = Finset.Icc 1 D.R.m`.
The proof of `divinN_at` unfolds `B0` to `(D.R.f : ℝ) * D.R.m * b * x^eps`. The `SizeData₂` structure has a finite support field but does **not explicitly state a bound on its cardinality**; one must still check restrictions inherited from `D7` and upstream construction before claiming a counterexample.

## What cohomology actually supplies (source-verified)

[`ExistsPageN.lean`](../src/Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean) defines `VVle E t B` as a uniform assertion over algebraic closures and local data: finite `shaLen` and a bound by `B` for weighted sums over every finite set of rational primes.

[`DivinNOfHypV.lean`](../src/Development/AutomorphicArithmetic/CharacterBoxes/DivinNOfHypV.lean) proves:
```lean
vvRecord (D : D7) (B : ℝ) (h : VVle D.host.E D.R.t B) :
  ShaFinOdd D ∧ Summable (vvTerm D) ∧ ∑' l, vvTerm D l ≤ B
```
Its proof uses the finite-subset bounds from `VVle` plus nonnegativity of `vvTerm` to establish summability and the scalar bound. The theorem `divinN_of_hypV` invokes `vvRecord`, a large-`x` logarithm-vs-power estimate, `LinkN`, and `SmallLevelRankEq`, then applies `divinN_at`. The scalar `VVle` budget in `HypV` is `sqrt b`; the proof uses `sqrt b ≤ b` (for `b ≥ 1`).

**Precise conclusion:** `VVle` is stronger than the three facts exported by `vvRecord`. This alone does not show that any of those facts have an independent elementary proof.

## Verified numerical transfer

Source: `divinN_at` in [`DivinNOfHypV.lean`](../src/Development/AutomorphicArithmetic/CharacterBoxes/DivinNOfHypV.lean).

Let `y = x^eps`, `T = ∑' l, vvTerm D l`, and assume:
- `j ∈ SizeData₂.lifts D`;
- `LinkN_at L j C`;
- summability and `T ≤ b`;
- `L.dZ0 j = D.what₂.D0`;
- `(log x)^2 ≤ y`.

The repository proof supplies positivity `y ≥ 1`, `Nc ≥ 0`, `f ≥ 1`, `m ≥ 1`, and `B0 = f m b y`. Thus `b ≤ B0` and:

```text
f m b y²                 = y B0
(log x)² Nc              ≤ y Nc
T                        ≤ b ≤ B0 ≤ y (B0 + Nc)
C (y B0 + (log x)² Nc)   ≤ |C| y (B0 + Nc)
```

Together these yield `etaSum L j ≤ D0 (|C| + 1) y (B0 + Nc)`, i.e. `DIVinN_at L j (|C| + 1)`. This is an algebraic transfer, **not** a proof of an independent bound for `etaSum`.

## Where the result is used (source-verified)

[`DesWin.lean`](../src/Development/AutomorphicArithmetic/CharacterBoxes/DesWin.lean) defines `topDesWin`. It uses:

```lean
have hD := aD hT hDG aE
  (divinN_of_hypV Fm h0 (hV Fm (h2 Fm hc.1.1)) aN aZ)
```

The result `hD` is then used in constructing `GlobalTheoremInputs` and a `LinkMu` consequence. Hence directly supplying `DIVinN Fm` for the selected constructed family could remove **this invocation** of `divinN_of_hypV`. It does not yet establish a complete removal of the Galois branch or of other hypotheses.

## Primewise candidate (conditional mathematical reduction; not a verified Lean theorem)

For a rational prime `p`, let
```text
E(p,j,L) = ∑ {w ∈ L.supp | resChar(w)=p and muAt(w)≠mu0}
               lwP(w) * ramIdx(w) * etaJ(j,w).
```

The support is finite, so grouping by the finitely many residue characteristics is an elementary identity. `DataParams₂.lean` **states** `FactEtaMean` as a proposition, including (under `IsGalois ℚ D.what₂.LL`) the formula for all places above a prime `p`:

```text
∑ {w | resChar(w)=p} lwP(w) * ramIdx(w) = log p.
```

Its proof or applicability to the constructed families has **not** been established by this investigation. If the local weights are nonnegative, `FactEtaMean` holds, and `0 ≤ etaJ(j,w) ≤ M(p,j)` on the exceptional fiber, then:
```text
E(p,j,L) ≤ (log p) * M(p,j).
```

The difficult missing estimate is **not** this conditional finite-sum inequality. It is the independently justified, uniform family bound
```text
∑ {p in exceptional residue characteristics} (log p) * M(p,j)
    ≤ D0 * C * x^eps * (B0 + Nc).
```
The proof must identify `M`, establish its upper bound, control the prime set, and handle `D0 = 0` without assuming equivalent global input.

## Feasibility and limitations

**Established:** a source-level location where a genuinely independent arithmetic estimate could replace a numerical cohomological transfer; the conditional prime-fiber majorization above.

**Not established:** positivity and detailed interpretation of `etaJ`, proof of `FactEtaMean`, sparsity of exceptional support, conductor control, a uniform numerical budget bound, a concrete counterexample respecting all `D7`/`SizeData₂` hypotheses, or any compiled independent Lean lemma.

**No claim:** that `DIVinN_at` follows for arbitrary structures, that `VVle` is unnecessary elsewhere, or that the mathematical proof has been shortened.

## Exactly one next decisive theorem

**Arithmetic primewise budget theorem for the constructed families.**

For sufficiently large `x`, every selected family index `i` and lift `j`, prove *from independently verified local ramification/conductor properties* that the exceptional prime-fiber contributions admit an explicit majorant `M(p,j)` with

```text
∑ {p in exceptional residue characteristics}
  (log p) * M(p,j)
  ≤ D0 * C * x^eps * (B0 + Nc),
```

where `C` and the threshold are uniform over `x,i,j`, and `etaJ(j,w) ≤ M(p,j)` for each relevant `w`. Its proof must provide the actual arithmetic bounds, not assume either the displayed inequality or `DIVinN` under a new name.

**Classification:** D (a precise possible intermediate goal; its truth and relative difficulty remain unverified). Formalizing this statement as a conditional theorem alone is not sufficient.

## Next investigation

Locate exact definitions of `etaJ`/`muAt`/`D0`, prove or refute needed sign and rank properties, inspect whether `FactEtaMean` is proved, and identify arithmetic restrictions on exceptional residue characteristics in the constructed families. Stop at the first unproved majorant rather than inserting an equivalent assumption.
