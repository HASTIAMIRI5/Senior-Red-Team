# MITRE ATT&CK Mapping Notes

This file provides a high-level mapping between common red-team validation objectives and ATT&CK-aligned tactics.

## Common Tactics

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
| External discovery | Reconnaissance | What assets are discoverable and exposed? |
| Credential testing | Credential Access | Are identity controls resilient to common abuse patterns? |
| Privilege abuse | Privilege Escalation | Are boundaries and protections effective? |
| Persistence | Persistence | Can suspicious persistence survive system resets or reboots? |
| Lateral movement | Lateral Movement | Are trust relationships monitored and constrained? |
| Exfiltration review | Exfiltration | Are suspicious data flows visible and attributable? |

## Operator Guidance

Map every test to both business impact and tactical understanding. Reporting is stronger when a finding connects code, control, and attacker behavior in a single narrative.

