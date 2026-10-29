# Adversary Emulation Roadmap

This roadmap helps teams align validation and testing to realistic threat behavior while maintaining discipline and operational safety.

## Stage 1: Reconnaissance

- Identify public-facing properties and exposed services
- Validate external attack surface and asset ownership
- Review publicly discoverable identity and infrastructure clues
- Establish a map of business-critical systems

## Stage 2: Initial Access and Credential Security

- Validate identity protections and MFA coverage
- Test password hygiene and account protection patterns
- Assess phishing-resistant controls
- Review authentication resilience to common user-targeting scenarios

## Stage 3: Post-Compromise Validation

- Evaluate endpoint visibility and telemetry
- Review privilege escalation pathways and security boundaries
- Validate the effectiveness of logging and containment controls
- Assess whether attacker paths are detectable and interruptible

## Stage 4: Lateral Movement and Persistence

- Validate lateral movement monitoring controls
- Review service account exposure and privilege segmentation
- Assess configuration drift and persistence opportunities
- Identify high-risk privilege and trust relationships

## Stage 5: Data Exposure and Behavioral Detection

- Measure how quickly suspicious behavior is detected
- Validate exfiltration indicators and anomaly alarm quality
- Review whether sensitive data flows are monitored and contained
- Determine the precision and usefulness of detections

## Stage 6: Reporting and Response

- Produce risk-ranked findings
- Align each finding to probable adversary behavior
- Prioritize mitigation based on operational and business impact
- Deliver actionable security recommendations

## Key Principle

Threat-informed testing works best when it reflects realistic adversary tradecraft, not just theoretical attack paths.

