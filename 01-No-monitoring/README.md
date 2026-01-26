#  1 – No Monitoring

## Overview
This episode is intentionally bare‑bones: a single Flask service (`app.py`) that randomly crashes to highlight how brittle life is without any monitoring or telemetry. There is no `/metrics`, no dashboards, and no alerting, so failures can only be spotted manually.

## Stack Components
- `app.py` – demo application with a random crash path and a `/health` probe.
- `Dockerfile` – containerizes the Flask app for parity with later episodes.
- `docker-compose.yml` – builds and runs the container on port `5000`.

## Run the Demo
1. From this directory run `docker compose up --build`.
2. Open `http://localhost:5000` several times to eventually trigger the simulated failure.
3. Use `docker compose logs -f web` (or the container name in your setup) to see how little context you have when it dies.

## Practice Exercises
1. Add basic structured logging (request id, timestamp, status) so you can at least correlate crashes manually.
2. Create a `/metrics` endpoint and expose a simple counter such as `app_requests_total`.
3. Extend the Docker Compose file to run two replicas behind a load balancer; observe how hard it is to keep track of failures without shared telemetry.
4. Draft the questions you would ask stakeholders before investing in a monitoring stack (SLIs, SLOs, alert channels, etc.).
