#  8 – Smart Alerting & Multi-Signal Telemetry

## Overview
The app now emits richer metrics: labeled error counters (`type=warning|critical`) and a latency histogram around the `/` and `/slow` endpoints. Prometheus alert rules differentiate minor vs. critical issues, and Alertmanager fans them out to different Slack channels. This demonstrates how to reduce noise while prioritizing real incidents.

## Stack Components
- `app/app.py` – introduces labeled counters and the `request_latency` histogram plus the `/slow` route.
- `prometheus/alert_rules.yml` – separate warning/critical alerts with different thresholds and `for` durations.
- `alertmanager/alertmanager.yml` – multi-route Slack configuration with grouping, batching, and dedicated receivers.
- `docker-compose.yml` – same monitoring stack as before, plus a persistent Grafana volume.
- `scripts/fire_errors.sh` – still available to cause bursts of traffic; also hit `/slow` manually to create latency data.

## Run the Demo
1. `docker compose up --build`.
2. Trigger warning noise with `./scripts/fire_errors.sh 20`; then simulate critical failures by touching `/tmp/fail_mode.flag`.
3. Hit `http://localhost:5000/slow` a few times to watch histogram buckets fill.
4. Inspect Alertmanager to confirm routing (different receivers for warning vs. critical).

## Practice Exercises
1. Convert the histogram into SLO burn-rate alerts (e.g., “P95 latency above 1.5s for 5 minutes”).
2. Add `service` or `environment` labels and route alerts to the correct team automatically.
3. Integrate Alertmanager webhooks to page an on-call rotation via PagerDuty or Opsgenie.
4. Use Grafana heatmaps to visualize the latency histogram and correlate it with error spikes.
