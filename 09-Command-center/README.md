#  9 – Building a Command Center

## Overview
All of the earlier components (instrumented app, rich alerts, Grafana) are combined into an “operations command center.” The goal is to curate a single workspace where on-call engineers can see traffic, latency, error budgets, and alert status without hopping between tools. The code mirrors  8; the difference is in how you package and operationalize the experience.

## Stack Components
- `app/app.py` – same labeled counters and latency histogram as  8.
- `prometheus/*` – evaluates warning/critical alerts and feeds dashboards.
- `alertmanager/*` – routes alerts to Slack dev vs. on-call channels.
- `docker-compose.yml` – ensures every service (app, exporters, Prometheus, Alertmanager, Grafana) is up for the command center.
- `scripts/fire_errors.sh` – generate realistic signal to populate the dashboards.

## Run the Demo
1. `docker compose up --build`.
2. Seed the system with baseline traffic via `./scripts/fire_errors.sh`.
3. Assemble a Grafana home dashboard that embeds key panels (traffic, latency, alerts table) and links to detailed views.
4. Keep Alertmanager and Prometheus tabs open so you can practice incident triage from one “wallboard.”

## Practice Exercises
1. Publish a “Morning Ops Review” dashboard snapshot and share it with the team; document the metrics you expect every day.
2. Create a Grafana playlist or kiosk mode view suitable for big screens.
3. Use provisioning to auto-install alert list panels, runbook links, and incident status boards.
4. Add uptime-style black-box probes (e.g., `blackbox_exporter`) so external availability shows up next to internal metrics.
