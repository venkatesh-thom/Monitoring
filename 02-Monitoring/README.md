#  2 – First Prometheus Scrape

## Overview
The first monitoring step adds Prometheus plus Node Exporter to collect host metrics. There is still no application telemetry, but you now have time‑series data for CPU, memory, filesystem, and networking to explore inside Prometheus.

## Stack Components
- `docker-compose.yml` – runs Prometheus (`9090`) and Node Exporter (`9100`).
- `prometheus.yml` – sets `scrape_interval: 15s` and registers the `node_exporter` target.

## Run the Demo
1. `docker compose up -d` from this folder.
2. Open `http://localhost:9090/targets` to confirm Prometheus can reach Node Exporter.
3. Use the Prometheus UI graph tab to query expressions such as `node_cpu_seconds_total` or `node_memory_MemAvailable_bytes`.

## Practice Exercises
1. Add a scrape job for Prometheus itself (`prometheus:9090`) so you can monitor scraper health.
2. Enable basic alerting rules (e.g., high CPU) even before Alertmanager is introduced in later episodes.
3. Tighten the `scrape_interval` to see the storage/precision trade‑offs firsthand.
4. Expose a custom exporter (perhaps a mock HTTP endpoint) and include it as another job to simulate multi‑target scraping.
