# Node.js Monitoring Application with Prometheus and Kubernetes

This project demonstrates a Node.js application instrumented with Prometheus metrics, deployed on Kubernetes with monitoring and alerting capabilities.

## Project Structure

```
.
├── src/
│   └── index.js              # Main Node.js application
├── kubernetes/
│   ├── deployment.yaml       # Kubernetes deployment configuration
│   ├── service.yaml          # Kubernetes service configuration
│   ├── service-monitor.yaml  # Prometheus ServiceMonitor configuration
│   ├── alert-rules.yaml      # Prometheus alert rules
│   └── alert-manager.yaml    # AlertManager configuration
├── Dockerfile                # Docker configuration for the application
└── scripts/
    └── send.sh              # Load testing script
```

## Components

1. **Node.js Application**
   - Express.js server with Prometheus metrics
   - Custom metrics for root path requests
   - Metrics endpoint at `/metrics`

2. **Docker Configuration**
   - Uses Node.js LTS base image
   - Exposes port 3000

3. **Kubernetes Resources**
   - Deployment with 3 replicas
   - NodePort service for external access
   - ServiceMonitor for Prometheus integration

4. **Monitoring & Alerting**
   - Prometheus ServiceMonitor configuration
   - Alert rules for high request rates
   - Slack integration for alerts

## Setup Instructions

1. **Build and Push Docker Image**
   ```bash
   docker build -t nodejs-app .
   docker tag nodejs-app:latest your-registry/nodejs-app:v1
   docker push your-registry/nodejs-app:v1
   ```

2. **Deploy to Kubernetes**
   ```bash
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml
   kubectl apply -f kubernetes/service-monitor.yaml
   kubectl apply -f kubernetes/alert-rules.yaml
   kubectl apply -f kubernetes/alert-manager.yaml
   ```

3. **Configure Slack Alerts**
   - Create a Slack webhook
   - Create a Kubernetes secret with the webhook URL
   - Update the AlertManager configuration

## Testing

Use the provided `send.sh` script to generate test load:
```bash
chmod +x scripts/send.sh
./scripts/send.sh
```

## Monitoring

- Application metrics are available at `/metrics`
- Monitor alerts in Prometheus UI
- Check Slack channel for notifications
