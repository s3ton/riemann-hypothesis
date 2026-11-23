#!/usr/bin/env python3
"""Static audit of local Lean import closures and potential entry-point simplifications.

Works with both Lean 4 module/public import syntax and ordinary import.
This is NOT a Lean checker; structural redundancy is only a candidate for
removal, since module visibility, elaboration, and transitive package imports
may still require a direct import.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
import re

IMPORT = re.compile(r"^\s*(public\s+)?import\s+(.+)$")
GOAL1 = re.compile(r"(?m)^\s*theorem\s+goal1\b")


def read_imports(source: str) -> list[tuple[str, bool]]:
    """Return (module name, public flag) for top-level import declarations."""
    found = []
    for line in source.splitlines():
        line = line.split("--", 1)[0]
        match = IMPORT.match(line)
        if match:
            found.extend((name, bool(match.group(1))) for name in match.group(2).split())
    return found


def scan(root: Path) -> dict[str, dict]:
    source_dir = root / "src"
    if not source_dir.is_dir():
        raise ValueError(f"No src/ folder at {root}")
    modules = {}
    for path in source_dir.rglob("*.lean"):
        module = ".".join(path.relative_to(source_dir).with_suffix("").parts)
        source = path.read_text(encoding="utf-8", errors="replace")
        imports = read_imports(source)
        modules[module] = {
            "path": str(path.relative_to(root)),
            "lines": len(source.splitlines()),
            "bytes": path.stat().st_size,
            "imports": imports,
            "goal1_count": len(GOAL1.findall(source)),
        }
    return modules


def closure(start: list[str], modules: dict, overrides: dict[str, list[str]] | None = None) -> set[str]:
    todo, seen = list(start), set()
    overrides = overrides or {}
    while todo:
        name = todo.pop()
        if name in seen or name not in modules:
            continue
        seen.add(name)
        imports = overrides.get(name)
        if imports is None:
            imports = [child for child, _ in modules[name]["imports"]]
        todo.extend(imports)
    return seen


def analyze(modules: dict, root: str, drop_import: str | None = None, limit: int = 20) -> dict:
    if root not in modules:
        raise ValueError(f"Root module {root!r} is not present under src/")
    direct = modules[root]["imports"]
    direct_names = [name for name, _ in direct]
    base = closure([root], modules)
    redundant = []
    for index, (name, public) in enumerate(direct):
        others = [n for j, (n, _) in enumerate(direct) if index != j]
        if name in closure(others, modules):
            redundant.append({"module": name, "public": public})
    by_import = Counter(name for info in modules.values() for name, _ in info["imports"])
    report = {
        "root": root,
        "total_local_modules": len(modules),
        "total_source_lines": sum(info["lines"] for info in modules.values()),
        "total_source_bytes": sum(info["bytes"] for info in modules.values()),
        "modules_with_goal1": sum(info["goal1_count"] > 0 for info in modules.values()),
        "root_direct_imports": [{"module": n, "public": p} for n, p in direct],
        "root_local_closure_modules": len(base),
        "structurally_transitive_direct_imports": redundant,
        "frequently_imported_local_modules": [
            {"module": name, "importers": count}
            for name, count in by_import.most_common() if name in modules
        ][:limit],
        "largest_local_modules": [
            {"module": name, "lines": info["lines"]}
            for name, info in sorted(modules.items(), key=lambda item: -item[1]["lines"])[:limit]
        ],
        "limitations": [
            "This is a line-based scanner, not a Lean parser or type checker.",
            "Only src/**/*.lean modules are traversed, not Mathlib or packages.",
            "Public import visibility and Lean elaboration are not modeled.",
            "Structurally transitive imports must NOT be removed without a Lean build.",
        ],
    }
    if drop_import is not None:
        if drop_import not in direct_names:
            raise ValueError(f"{drop_import!r} is not a direct import of {root}")
        candidate = closure([root], modules, {root: [n for n in direct_names if n != drop_import]})
        removed = sorted(base - candidate)
        report["proposed_drop"] = {
            "import": drop_import,
            "remaining_local_closure_modules": len(candidate),
            "excluded_local_modules": removed,
            "excluded_local_lines": sum(modules[name]["lines"] for name in removed),
        }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", type=Path, help="local checkout containing src/")
    parser.add_argument("--root", default="Main", help="module whose imports to analyze")
    parser.add_argument("--drop-import", help="simulate removing one root-level import")
    parser.add_argument("--json", type=Path, help="save full report to this JSON file")
    parser.add_argument("--top", type=int, default=20, help="max entries in rankings")
    args = parser.parse_args()
    report = analyze(scan(args.repository), args.root, args.drop_import, args.top)
    print(f"Local modules: {report['total_local_modules']:,}; lines: {report['total_source_lines']:,}")
    print(f"{args.root} closure: {report['root_local_closure_modules']:,} local modules")
    print(f"Structurally transitive direct imports: {len(report['structurally_transitive_direct_imports'])}")
    if "proposed_drop" in report:
        drop = report["proposed_drop"]
        print(f"Dropping {drop['import']} excludes {len(drop['excluded_local_modules'])} local modules")
        print(f"Excluded source lines: {drop['excluded_local_lines']:,}")
    if args.json:
        args.json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {args.json}")


if __name__ == "__main__":
    main()
