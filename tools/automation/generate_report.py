#!/usr/bin/env python3
"""Validate a list of in-scope systems or assets.

This script is designed to help security teams check whether asset names and
hostnames follow a consistent format before they are used in an engagement plan.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def validate_lines(raw: str) -> list[str]:
    accepted = []
    rejected = []

    for line in raw.splitlines():
        entry = line.strip()
        if not entry or entry.startswith("#"):
            continue
        # Basic host validation: allow letters, digits, dots, hyphens, and underscores.
        if all(ch.isalnum() or ch in ".-_" for ch in entry):
            accepted.append(entry)
        else:
            rejected.append(entry)

    return accepted, rejected


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a scope list for asset naming consistency.")
    parser.add_argument("input", help="Path to a newline-delimited list of assets or hostnames.")
    args = parser.parse_args()

    path = Path(args.input)
    content = path.read_text(encoding="utf-8")
    accepted, rejected = validate_lines(content)

    print("Valid entries:")
    for item in accepted:
        print(f"- {item}")

    if rejected:
        print("\nRejected entries:")
        for item in rejected:
            print(f"- {item}")

    print(f"\nSummary: {len(accepted)} accepted, {len(rejected)} rejected.")


if __name__ == "__main__":
    main()

