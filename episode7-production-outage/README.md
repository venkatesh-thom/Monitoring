# Episode 7 – Simulating a Production Outage

## Overview
Incidents rarely follow the “random blip” pattern. This episode introduces a deterministic failure mode so you can practice runbooks and incident response. Setting `FAIL_MODE=true` (or dropping `/tmp/fail_mode.flag` inside the container) forces 500s, letting you rehearse detection, triage, rollback, and confirmation.

## Stack Components
- `app/app.py` – adds a fail mode flag that guarantees errors plus the usual random failures.
- `prometheus/*` & `alertmanager/*` – same plumbing as Episode 5, so alert fidelity can be evaluated under stress.
- `scripts/fire_errors.sh` – still useful for baseline noise.
- `docker-compose.yml` – orchestrates the app, exporters, Prometheus, Alertmanager, and Grafana.

## Run the Demo
1. `docker compose up --build`.
2. Toggle fail mode: `docker compose exec web touch /tmp/fail_mode.flag` (remove the file to recover).
3. Watch alert timelines and Grafana dashboards to confirm you can detect, mitigate, and verify the outage.

## Practice Exercises
1. Write a short runbook describing exactly how to confirm, escalate, mitigate, and close this outage.
2. Add a dedicated alert (or Slack message) that distinguishes forced outages from organic failures.
3. Use recording rules to compute error percentages, then alert on both rate and absolute errors.
4. Experiment with automated remediation (e.g., script removes the flag once SLOs are met) and discuss pros/cons.
