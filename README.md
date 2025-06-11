# CI/CD Flask App with Prometheus Monitoring

This project demonstrates a simple CI/CD pipeline using:
- Flask + Prometheus for metrics
- GitHub Actions for CI/CD
- Docker for containerization

## Endpoints
- `/` - Main page
- `/slow` - Simulated latency
- `/metrics` - Prometheus metrics

## Run Locally
```bash
docker build -t ci-cd-flask-app .
docker run -p 5000:5000 ci-cd-flask-app
