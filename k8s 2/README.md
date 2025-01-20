# MongoDB and Mongo Express Kubernetes Deployment

This repository contains Kubernetes configuration files for deploying MongoDB and Mongo Express.

## Files Structure

- `mongodb-secret.yaml`: Contains MongoDB credentials (username and password)
- `mongodb.yaml`: MongoDB deployment and service configuration
- `mongo-express.yaml`: Mongo Express deployment and service configuration

## Deployment Steps

1. First, apply the secret:
   ```bash
   kubectl apply -f mongodb-secret.yaml
   ```

2. Deploy MongoDB:
   ```bash
   kubectl apply -f mongodb.yaml
   ```

3. Deploy Mongo Express:
   ```bash
   kubectl apply -f mongo-express.yaml
   ```

## Accessing the Applications

- MongoDB runs internally on port 27017
- Mongo Express is accessible through NodePort 30000 (http://localhost:30000)

## Credentials

Default credentials (base64 encoded in secret):
- Username: username
- Password: password

## Verification

Check the status of your deployments:
```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

## Clean Up

To remove all resources:
```bash
kubectl delete -f mongo-express.yaml
kubectl delete -f mongodb.yaml
kubectl delete -f mongodb-secret.yaml
```
