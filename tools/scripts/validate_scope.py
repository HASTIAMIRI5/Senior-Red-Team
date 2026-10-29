#!/usr/bin/env python3
"""Generate a concise engagement summary from structured input.

This script is intentionally lightweight and safe; it is designed to help
security teams summarize engagement metadata, business context, and findings.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_summary(data: dict) -> str:
    client = data.get("client", "[Client]")
    timeframe = data.get("timeframe", "[Date Range]")
    objective = data.get("objective", "Validate defensive controls and adversary emulation readiness.")
    risk = data.get("risk_rating", "Moderate")
    findings = data.get("findings", [])

    lines = [
        f"# Engagement Summary for {client}",
        "",
        f"- Timeframe: {timeframe}",
        f"- Objective: {objective}",
        f"- Risk Rating: {risk}",
        "",
        "## Summary",
        "This assessment reviewed the organization’s operational resilience, defensive coverage, and alignment to realistic adversary behavior within the approved scope.",
        "",
        "## Key Findings",
    ]

    if findings:
        for idx, item in enumerate(findings, 1):
            title = item.get("title", f"Finding {idx}")
            severity = item.get("severity", "Medium")
            summary = item.get("summary", "No summary provided.")
            lines.append(f"{idx}. {title} ({severity}) - {summary}")
    else:
        lines.append("- No findings recorded in the provided data set.")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a red-team engagement summary.")
    parser.add_argument("input", nargs="?", help="Path to JSON file with engagement metadata.")
    parser.add_argument("--output", help="Output markdown path.")
    args = parser.parse_args()

    source = Path(args.input) if args.input else None
    output = Path(args.output) if args.output else Path("engagement_summary.md")

    if source is None:
        sample = {
            "client": "Example Organization",
            "timeframe": "2026-10-01 to 2026-10-15",
            "objective": "Assess defensive detection coverage and adversary validation readiness.",
            "risk_rating": "High",
            "findings": [
                {"title": "Credential and access boundary review", "severity": "High", "summary": "Identity protections require further validation and hardening."},
                {"title": "Detection engineering coverage", "severity": "Medium", "summary": "Key attack patterns require clearer visibility and alerting logic."}
            ],
        }
        content = build_summary(sample)
    else:
        with source.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        content = build_summary(data)

    output.write_text(content, encoding="utf-8")
    print(f"Summary written to {output}")


if __name__ == "__main__":
    main()

