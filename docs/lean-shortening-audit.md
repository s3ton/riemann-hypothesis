# Static import audit for proof shortening

The earlier shortening proposal examined the `CocoSgt/riemann-hypothesis-lean` archive mirror, where `src/Main.lean` imported `Supplements.Kernels.MainTheoremsAll`. **That patch does not apply here:** this repository is based on `leanprover-community/riemann-hypothesis` and `src/Main.lean` already imports `Statements`, `ClaimStrip`, and `MainConclusion` directly. No change to the final Lean theorem is proposed by this PR.

This change adds a reusable analyzer that traverses a local checkout, recognizes Lean 4 `module`, `public import`, and ordinary `import` layouts, computes the local import closure of a selected root, and highlights candidate direct-import redundancies. The analyzer can simulate dropping a direct import and report the local files/lines no longer reachable. It does **not** prove that deleting an import is semantically valid, build the code, or inspect compiled proof terms.

## Run

```sh
python3 scripts/lean-shortening-audit.py . --root Main --json lean-shortening-audit.json
python3 scripts/lean-shortening-audit.py . --root Main --drop-import Mathlib.NumberTheory.Chebyshev
python3 -m unittest discover -s scripts -p 'test_lean_shortening_audit.py'
```

Do not interpret a proposed drop as validated merely because the static closure is unchanged. `public import` visibility, package imports, and Lean 4 elaboration are not modeled. Any actual Lean edit must be independently compiled (`lake build Main`) and accompanied by axiom checks. This PR is instrumentation toward later proof minimization, not a mathematical shortening claim.
