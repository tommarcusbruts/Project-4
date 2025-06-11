from flask import Flask, request
import time
import logging
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST


app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Prometheus metrics
REQUEST_COUNT = Counter(
    'app_requests_total', 'Total number of requests', ['method', 'endpoint']
)
REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds', 'Latency of requests in seconds', ['endpoint']
)

@app.before_request
def before_request_func():
    app.start_time = time.time()

@app.after_request
def after_request_func(response):
    latency = time.time() - app.start_time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
    REQUEST_LATENCY.labels(endpoint=request.path).observe(latency)
    return response

@app.route('/')
def index():
    app.logger.info("Request to /")
    return "Hello, World!"

@app.route('/slow')
def slow():
    app.logger.info("Request to /slow - simulating latency")
    time.sleep(2)
    return "This is a slow endpoint."

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
