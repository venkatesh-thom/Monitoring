# Episode 6 – Storytelling with Dashboards

## Overview
With instrumentation and alerts in place, this episode focuses on visualization best practices. The stack mirrors Episode 5, but the emphasis is on curating Grafana dashboards that help on‑call engineers reason about incidents quickly (golden signals, drill‑downs, and annotations).

## Stack Components
- `app/app.py` – same simulated failure service exposing `app_errors_total`.
- `prometheus/*` & `alertmanager/*` – identical scrape/alert plumbing so you can reuse earlier lessons.
- `docker-compose.yml` – spins up the full monitoring toolchain plus Grafana.
- `scripts/fire_errors.sh` – still handy for creating demo data.

## Run the Demo
1. `docker compose up --build`.
2. Import or build dashboards in Grafana (`http://localhost:3000`) using Prometheus as the data source.
3. Trigger traffic with `./scripts/fire_errors.sh` and observe how panels react.

## Practice Exercises
1. Design a “Golden Signals” dashboard (latency, traffic, errors, saturation) for this service.
2. Use Grafana’s `transformations` to aggregate per‑instance metrics into fleet views.
3. Add dashboard annotations that are created automatically when alerts fire.
4. Document dashboard links or drill‑downs to guide responders during outages.
