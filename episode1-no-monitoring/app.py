from flask import Flask
import random, time

app = Flask(__name__)

@app.route("/")
def home():
    # Simulate random crash
    if random.random() < 0.3:
        raise Exception("Simulated crash!")
    return " App is running fine!"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(host="0.0.0.0", port=5000)
