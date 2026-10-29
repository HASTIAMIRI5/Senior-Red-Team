#!/usr/bin/env python3
"""Create a structured adversary emulation dossier from JSON data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def render_dossier(data: dict) -> str:
    org = data.get("organization", "Organization")
    period = data.get("engagement_period", "[Date Range]")
    lead = data.get("assessment_lead", "Assessment Lead")
    scope = data.get("scope", "Approved security validation scope")
    objective = data.get("objective", "Assess resilience and control quality.")
    threat = data.get("threat_profile", "Realistic opportunistic adversary profile")
    risk = data.get("risk_rating", "Moderate")
    areas = data.get("areas", [])
    actions = data.get("priority_actions", [])

    lines = [
        "# Adversary Emulation Dossier",
        "",
        f"- Organization: {org}",
        f"- Engagement Period: {period}",
        f"- Assessment Lead: {lead}",
        f"- Scope: {scope}",
        f"- Objective: {objective}",
        f"- Threat Profile: {threat}",
        f"- Overall Risk: {risk}",
        "",
        "## Executive Overview",
        "This assessment reviewed defensive quality, detection usefulness, and control resilience against realistic adversary patterns within the approved scope.",
        "",
        "## Observed Results",
    ]

    for index, item in enumerate(areas, 1):
        title = item.get("area", f"Area {index}")
        observation = item.get("observation", "No observation recorded.")
        impact = item.get("impact", "No impact recorded.")
        recommendation = item.get("recommendation", "No recommendation recorded.")
        lines.append(f"### {index}. {title}")
        lines.append(f"- Observation: {observation}")
        lines.append(f"- Impact: {impact}")
        lines.append(f"- Recommendation: {recommendation}")
        lines.append("")

    lines.append("## Recommended Priorities")
    for idx, action in enumerate(actions, 1):
        lines.append(f"{idx}. {action}")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an adversary emulation dossier from JSON data.")
    parser.add_argument("input", help="Path to the JSON dossier data file.")
    parser.add_argument("--output", help="Path to the output markdown file.")
    args = parser.parse_args()

    source = Path(args.input)
    output = Path(args.output) if args.output else Path("dossier.md")
    payload = json.loads(source.read_text(encoding="utf-8"))
    output.write_text(render_dossier(payload), encoding="utf-8")
    print(f"Dossier created at {output}")


if __name__ == "__main__":
    main()

