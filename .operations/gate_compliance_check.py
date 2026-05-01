#!/usr/bin/env python3
"""
gate_compliance_check.py
DGAF-Framework .operations — P-24 (Canonical Practice Unit) compliance scanner
Owner: Agent COLLEEN | Pattern: P-02 (COLLEEN-Trigger-Chain), P-03 (BLG-Surface-and-Defer)

Scans docs/gates/ and docs/protocols/ for the 6 required CPU fields.
Non-compliant files are BLG-class gaps — surface to SWEEP_LOG per P-03.

Usage: python .operations/gate_compliance_check.py [--path docs/gates]
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

REQUIRED_FIELDS = [
    "## Rationale",
    "## Trigger Condition",
    "## Passing State",
    "## Failing State",
    "## Recovery Protocol",
    "## References",
]

SKIP_FILES = {"GATE_UNIT_TEMPLATE.md", "GATE_SPECS.md"}

STATUS_HEADER = "Status:"


def check_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    missing = [f for f in REQUIRED_FIELDS if f not in text]
    has_status = STATUS_HEADER in text
    certified = "CERTIFIED" in text
    return {
        "file": path.name,
        "missing_fields": missing,
        "field_score": f"{len(REQUIRED_FIELDS) - len(missing)}/{len(REQUIRED_FIELDS)}",
        "has_status_header": has_status,
        "certified": certified,
        "compliant": len(missing) == 0 and has_status,
    }


def scan_directory(scan_path: str) -> list[dict]:
    results = []
    p = Path(scan_path)
    if not p.exists():
        print(f"[WARN] Path not found: {scan_path}", file=sys.stderr)
        return results
    for md_file in sorted(p.glob("*.md")):
        if md_file.name in SKIP_FILES:
            continue
        results.append(check_file(md_file))
    return results


def render_table(results: list[dict]) -> str:
    lines = []
    lines.append(f"\n# Gate Compliance Report — {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append(f"Pattern: P-24 (Canonical Practice Unit) | P-10 (1-1-1-1 Gate)\n")
    lines.append(f"{'File':<35} {'Fields':>8} {'Status':>6} {'Certified':>10} {'Missing'}")
    lines.append("-" * 90)
    blg_list = []
    for r in results:
        status = "✅" if r["compliant"] else "❌"
        cert = "✅" if r["certified"] else "—"
        missing_str = ", ".join(r["missing_fields"]) if r["missing_fields"] else "none"
        lines.append(f"{r['file']:<35} {r['field_score']:>8} {status:>6} {cert:>10}   {missing_str}")
        if not r["compliant"]:
            blg_list.append(r["file"])
    lines.append("-" * 90)
    compliant_count = sum(1 for r in results if r["compliant"])
    lines.append(f"\nScore: {compliant_count}/{len(results)} compliant")
    if blg_list:
        lines.append(f"\n⚠️  BLG-class gaps (P-03 surface to SWEEP_LOG):")
        for f in blg_list:
            lines.append(f"  - {f}")
    else:
        lines.append("\n✅ All gate/protocol docs P-24 compliant.")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="P-24 gate compliance checker")
    parser.add_argument(
        "--path",
        nargs="+",
        default=["docs/gates", "docs/protocols"],
        help="Directories to scan (default: docs/gates docs/protocols)",
    )
    args = parser.parse_args()
    all_results = []
    for scan_path in args.path:
        all_results.extend(scan_directory(scan_path))
    if not all_results:
        print("[INFO] No markdown files found in scan paths.")
        return
    print(render_table(all_results))
    blg_count = sum(1 for r in all_results if not r["compliant"])
    sys.exit(1 if blg_count > 0 else 0)


if __name__ == "__main__":
    main()
