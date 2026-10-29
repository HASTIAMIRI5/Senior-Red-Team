#!/usr/bin/env python3
"""Create a lightweight markdown report from a JSON payload."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def render_report(data: dict) -> str:
    client = data.get("client", "Client")
    title = data.get("title", "Security Assessment Report")
    summary = data.get("summary", "No summary provided.")
    findings = data.get("findings", [])

    lines = [
        f"# {title}",
        "",
        f"**Client:** {client}",
        "",
        "## Summary",
        summary,
        "",
        "## Findings",
    ]

    if findings:
        for index, item in enumerate(findings, 1):
            lines.append(f"### {index}. {item.get('title', 'Finding')}")
            lines.append(f"- Severity: {item.get('severity', 'Medium')}")
            lines.append(f"- Impact: {item.get('impact', 'Unspecified')}")
            lines.append(f"- Recommendation: {item.get('recommendation', 'Review and remediate')}")
            lines.append("")
    else:
        lines.append("No findings were supplied in the source data.")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a markdown report from JSON data.")
    parser.add_argument("input", help="Path to the input JSON file.")
    parser.add_argument("--output", help="Path to the markdown output file.")
    args = parser.parse_args()

    source = Path(args.input)
    output = Path(args.output) if args.output else Path("generated_report.md")
    payload = json.loads(source.read_text(encoding="utf-8"))
    output.write_text(render_report(payload), encoding="utf-8")
    print(f"Report created at {output}")


if __name__ == "__main__":
    main()

