from flask import Flask
from prometheus_client import Counter, generate_latest
import random, os

app = Flask(__name__)

# Prometheus counter for errors
error_counter = Counter("app_errors_total", "Total simulated application errors")

@app.route("/")
def home():
    fail_mode_file = "/tmp/fail_mode.flag"
    fail_mode_env = os.getenv("FAIL_MODE", "false").lower() == "true"
    fail_mode = fail_mode_env or os.path.exists(fail_mode_file)

    # 🔥 Force only 500 errors when fail mode is active
    if fail_mode:
        error_counter.inc()
        return "Simulated application failure (forced 500)", 500

    # Otherwise, randomly simulate occasional 500s
    if random.random() < 0.3:
        error_counter.inc()
        return "Simulated random error (500)", 500

    # Healthy response
    return "App is healthy!", 200


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain; charset=utf-8"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
