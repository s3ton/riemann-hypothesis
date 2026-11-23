#!/usr/bin/env python3
"""Fixture tests for the static Lean import analyzer (no Lean installation needed)."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("lean-shortening-audit.py")


class AuditTests(unittest.TestCase):
    def test_public_and_regular_imports_and_drop(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "src").mkdir()
            (root / "src" / "Main.lean").write_text(
                "module\npublic import Statements\npublic import A\nimport B\n",
                encoding="utf-8",
            )
            (root / "src" / "Statements.lean").write_text("module\n", encoding="utf-8")
            (root / "src" / "A.lean").write_text("module\npublic import B\n", encoding="utf-8")
            (root / "src" / "B.lean").write_text(
                "module\nimport Mathlib.Data.Nat.Basic\ntheorem goal1 : True := trivial\n",
                encoding="utf-8",
            )
            report_file = root / "report.json"
            subprocess.run(
                [sys.executable, str(SCRIPT), str(root), "--drop-import", "B", "--json", str(report_file)],
                check=True, capture_output=True, text=True,
            )
            report = json.loads(report_file.read_text(encoding="utf-8"))
            self.assertEqual(report["root_local_closure_modules"], 4)
            self.assertEqual(report["proposed_drop"]["excluded_local_modules"], [])
            self.assertEqual(report["modules_with_goal1"], 1)
            self.assertIn({"module": "B", "public": False}, report["structurally_transitive_direct_imports"])

    def test_drop_excludes_unshared_dependency(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "src").mkdir()
            (root / "src" / "Main.lean").write_text("import A B\n", encoding="utf-8")
            (root / "src" / "A.lean").write_text("import C\n", encoding="utf-8")
            (root / "src" / "B.lean").write_text("", encoding="utf-8")
            (root / "src" / "C.lean").write_text("", encoding="utf-8")
            result_file = root / "result.json"
            subprocess.run(
                [sys.executable, str(SCRIPT), str(root), "--drop-import", "A", "--json", str(result_file)],
                check=True, capture_output=True, text=True,
            )
            self.assertEqual(json.loads(result_file.read_text())["proposed_drop"]["excluded_local_modules"], ["A", "C"])


if __name__ == "__main__":
    unittest.main()
