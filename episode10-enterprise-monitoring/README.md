# Episode 10 – Enterprise-Grade Monitoring

## Overview
The final episode assembles a realistic multi-tier system: a web frontend, a backend API, PostgreSQL, Node Exporter, and a Postgres exporter. Prometheus scrapes each component, alert rules cover application and database health, and Alertmanager fans out notifications per severity. This is the canonical “all the pieces together” environment.

## Stack Components
- `web/` & `api/` – Flask services with their own Dockerfiles and `/metrics` endpoints.
- `db/` – Postgres container plus `init.sql` for seed data and a simple load generator.
- `docker-compose.yml` – orchestrates application, database, exporters (`db-exporter`, `node-exporter`), Prometheus, Alertmanager, and Grafana.
- `prometheus/prometheus.yml` & `prometheus/alert_rules.yml` – scrape jobs for every tier plus alerts for web/api errors, DB connections, and instance liveness.
- `alertmanager/alertmanager.yml` – multi-receiver Slack routing similar to Episodes 8–9.
- `scripts/fire_errors.sh` – optional tool to drive load against the web entry point.

## Run the Demo
1. `docker compose up --build` (first launch can take a minute while Postgres initializes).
2. Verify scrape status at `http://localhost:9090/targets`; ensure `web`, `api`, `postgres`, and `node` jobs are all green.
3. Use Grafana (`http://localhost:3000`) to build per-tier dashboards or import existing ones for Postgres / Node Exporter.
4. Trigger traffic via the script or by curling `http://localhost:5000` and `http://localhost:5001`.

## Practice Exercises
1. Add recording rules that compute service-level indicators (error rate, latency) for both the web and API tiers, then build burn-rate alerts.
2. Extend the Docker Compose stack with a message queue or cache and figure out how you would monitor it (exporters, alerts, dashboards).
3. Secure secrets by replacing inline Slack webhooks with environment variables or a secrets manager.
4. Simulate a database connection storm and tune the `DatabaseHighConnections` alert to avoid false positives.
5. Document deployment/rollback steps plus a verification checklist for the entire stack.
