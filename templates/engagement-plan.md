# MITRE ATT&CK Mapping Notes

This document provides a structured link between common red-team validation objectives and ATT&CK-aligned tactics.

## Core Tactics

- Reconnaissance
- Resource Development
- Initial Access
- Execution
- Persistence
- Privilege Escalation
- Defense Evasion
- Credential Access
- Discovery
- Lateral Movement
- Collection
- Command and Control
- Exfiltration
- Impact

## Example Mapping

| Objective | ATT&CK Tactic | Typical Validation Question |
|---|---|---|
| external reconnaissance | Reconnaissance | What is visible to an external threat actor? |
| identity validation | Credential Access | Are identity controls strong enough to resist common abuse paths? |
| server and account access review | Privilege Escalation | Are privilege boundaries effective and observable? |
| persistence and foothold review | Persistence | Can suspicious persistence be detected and contained? |
| movement across trust boundaries | Lateral Movement | Are trust relationships constrained and monitored? |
| exfiltration review | Exfiltration | Are suspicious data paths visible and attributable? |

## Senior Guidance

Map findings to both business impact and adversary tradecraft. This makes the output more credible, more useful to defenders, and more actionable for executive stakeholders.

