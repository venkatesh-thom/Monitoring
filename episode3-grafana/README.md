# Episode 3 – Visualizing with Grafana

## Overview
Prometheus data is powerful, but teams need friendly visualizations. This episode keeps the Prometheus + Node Exporter setup and adds Grafana so you can build dashboards, share panels, and experiment with alert annotations.

## Stack Components
- `docker-compose.yml` – runs Prometheus, Node Exporter, and Grafana (default creds `admin/admin`).
- `prometheus.yml` – same scrape config as Episode 2 so you can reuse the metrics.

## Run the Demo
1. `docker compose up -d`.
2. Visit `http://localhost:3000`, log in with `admin/admin`, and add Prometheus as a data source (`http://prometheus:9090`).
3. Build a basic dashboard charting CPU, memory, and filesystem metrics from Node Exporter.

## Practice Exercises
1. Import an official Grafana dashboard for Node Exporter (e.g., ID 1860) and compare it with your custom version.
2. Create dashboard variables (instance, job) so panels can be filtered without editing PromQL.
3. Add alert annotations to a panel so you can correlate spikes with alerts once Alertmanager is added later.
4. Configure Grafana to persist dashboards via provisioning files rather than in the built‑in SQLite DB.
