# MITRE ATT&CK Mapping Notes

This document provides a structured bridge between realistic adversary behavior and professional security validation objectives.

## Core ATT&CK Tactics

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

## Example Mapping to Security Validation

| Objective | ATT&CK Tactic | Business Relevance |
|---|---|---|
| external surface review | Reconnaissance | understand how a threat actor can discover exposed systems |
| identity and access posture | Credential Access | measure resilience of authentication and access controls |
| privilege abuse testing | Privilege Escalation | assess whether boundaries and controls are meaningful |
| persistence review | Persistence | evaluate whether suspicious changes can survive and persist |
| lateral movement review | Lateral Movement | assess segmentation, trust, and movement containment |
| exfiltration and data exposure | Exfiltration | determine whether sensitive dataflows are observable and constrained |
| detection quality | Defense Evasion / Discovery | validate whether malicious behavior is visible and actionable |

## Professional Use

When mapped correctly, ATT&CK becomes a way to connect:

- adversary behavior
- telecom and asset dependencies
- defensive visibility
- security control quality
- business consequence and remediation priority

## Operational Guidance

Use ATT&CK as a structure for threat-informed testing, not as a substitute for business context, evidence review, or practical control understanding.

