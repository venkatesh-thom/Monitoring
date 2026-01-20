from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest
import random, os, time

app = Flask(__name__)

# Metrics
error_counter = Counter("app_errors_total", "Total number of simulated application errors", ["type"])
request_latency = Histogram("app_request_latency_seconds", "Request latency")

@app.route("/")
@request_latency.time()
def home():
    fail_mode_file = "/tmp/fail_mode.flag"
    fail_mode = os.path.exists(fail_mode_file)

    # Random soft errors (warning level)
    if random.random() < 0.2:
        error_counter.labels(type="warning").inc()
        return "Minor app issue occurred", 400

    # Hard failures (critical level)
    if fail_mode or random.random() < 0.1:
        error_counter.labels(type="critical").inc()
        return "Simulated application error!", 500

    return "App is healthy!"

@app.route("/slow")
@request_latency.time()
def slow():
    # Simulate latency spike
    time.sleep(random.uniform(1.0, 3.0))
    return "Slow response simulated"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain; charset=utf-8"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
