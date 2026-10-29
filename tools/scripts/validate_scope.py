#!/usr/bin/env python3
"""Generate a concise engagement summary from a structured JSON payload."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_summary(data: dict) -> str:
    client = data.get("client", "[Client]")
    timeframe = data.get("timeframe", "[Date Range]")
    objective = data.get("objective", "Validate resilience and defensive control coverage.")
    risk = data.get("risk_rating", "Moderate")
    findings = data.get("findings", [])

    lines = [
        f"# Engagement Summary for {client}",
        "",
        f"- Timeframe: {timeframe}",
        f"- Objective: {objective}",
        f"- Risk Rating: {risk}",
        "",
        "## Overview",
        "This assessment reviewed operational resilience, control effectiveness, and the organization’s alignment with realistic adversary behavior within the approved scope.",
        "",
        "## Key Findings",
    ]

    if findings:
        for i, item in enumerate(findings, 1):
            title = item.get("title", f"Finding {i}")
            severity = item.get("severity", "Medium")
            summary = item.get("summary", "No summary provided.")
            lines.append(f"{i}. {title} ({severity}) - {summary}")
    else:
        lines.append("- No findings recorded in the supplied data set.")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a red-team engagement summary.")
    parser.add_argument("input", nargs="?", help="Path to a JSON file with engagement metadata.")
    parser.add_argument("--output", help="Output markdown path.")
    args = parser.parse_args()

    source = Path(args.input) if args.input else None
    output = Path(args.output) if args.output else Path("engagement_summary.md")

    if source is None:
        sample = {
            "client": "Example Organization",
            "timeframe": "2026-10-01 to 2026-10-15",
            "objective": "Assess security control coverage and adversary emulation readiness.",
            "risk_rating": "High",
            "findings": [
                {"title": "Identity and access validation", "severity": "High", "summary": "Access boundaries require stronger control validation and review."},
                {"title": "Detection engineering coverage", "severity": "Medium", "summary": "Key adversary patterns are present but alerting quality needs refinement."}
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

