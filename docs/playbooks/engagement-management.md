# Operational Security Checklist

Operational security is one of the most important differentiators between weak and mature red-team execution.

## Core Controls

- [ ] Use approved infrastructure only
- [ ] Confirm all communications are encrypted and monitored
- [ ] Validate that test data does not contain real production secrets
- [ ] Review logging and evidence capture before execution
- [ ] Keep scope boundaries visible throughout the engagement
- [ ] Maintain a clear chain of custody for any artifacts

## Daily Hygiene

- [ ] Confirm current objective and stop conditions
- [ ] Record time, task, and tool use in a runbook
- [ ] Verify no out-of-scope assets are touched
- [ ] Ensure team members understand the engagement narrative
- [ ] Review any environment changes that may affect safety or detection

## Evidence Handling

- [ ] Capture screenshot, log, and note evidence in a controlled location
- [ ] Label findings by timestamp, asset, and severity
- [ ] Preserve original artifacts and document any transformations
- [ ] Keep internal notes separate from client-facing reports

## Risk Controls

- [ ] Maintain a fail-safe for emergency stop
- [ ] Validate escalation contact chain
- [ ] Avoid actions that may cause service degradation
- [ ] Segregate test traffic from normal operations where possible

## Final Check

If the engagement cannot be explained clearly, justified by policy, and defended by evidence, it is not ready to proceed.

