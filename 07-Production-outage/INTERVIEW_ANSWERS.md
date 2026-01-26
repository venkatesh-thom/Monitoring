#  7 – Interview Answers

1. **Runbook essentials:** Include trigger conditions, escalation contacts, diagnostic steps, mitigation actions, rollback commands, and verification checks; update runbooks after every incident review to keep them accurate.
2. **Testing paging workflows:** Use game days or chaos simulations with dummy alerts routed to training channels, clearly mark test alerts, and ensure approvals so real incidents aren’t drowned out.
3. **Noise vs outage detection:** Combine error counts with ratios, apply `for` durations, and use canary signals (synthetics, regional splits) to confirm that issues persist across multiple indicators before paging.
4. **Telemetry for replay:** Capture timelines (alerts, dashboards), structured logs, traces, and configuration changes so you can reconstruct what happened once the forced failure is lifted.
5. **Coordinating communication:** Maintain an incident commander, run a shared war room, update status pages regularly, and document postmortems with action items to keep stakeholders aligned during and after the event.
