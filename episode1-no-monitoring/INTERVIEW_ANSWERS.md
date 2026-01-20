# Episode 1 – Interview Answers

1. **Risks without telemetry:** You cannot quantify availability, detect regressions, or prove SLAs, so outages linger until users complain; debugging also goes blind because there is no evidence to correlate failures with deployments or dependencies.
2. **Justifying observability early:** Frame it as insurance—calculate the cost of an hour of downtime, highlight regulatory/customer expectations, and demonstrate how minimal metrics/logging de-risk launches compared with the engineering effort.
3. **Minimum health signals:** Add structured logs, a `/metrics` endpoint with request/error counters, readiness/liveness probes, and basic tracing or correlation ids so you can quickly tie user impact to backend behavior.
4. **Synthetic traffic usage:** Great for smoke tests, edge-case reproduction, and pipeline validation, but it rarely mirrors real user behavior or load patterns, so it cannot replace production telemetry or true canary feedback.
5. **Measuring success:** Track MTTR/MTTD improvements, alert coverage versus incident backlog, and adoption metrics (dashboards created, alerts acknowledged) to show that observability investments change operational outcomes.
