# WordPress with MySQL on Kubernetes

This repository contains Kubernetes configurations for deploying WordPress with MySQL database on AWS.

## Directory Structure

```
.
├── mysql/
│   ├── secret.yaml
│   ├── storage-class.yaml
│   ├── pvc.yaml
│   ├── deployment.yaml
│   └── service.yaml
├── wordpress/
│   ├── storage-class.yaml
│   ├── pv.yaml
│   ├── pvc.yaml
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```

## Components

### MySQL
- Secret configuration for database credentials
- Storage Class for AWS EBS
- Persistent Volume Claim for database storage
- Deployment configuration for MySQL
- Service configuration for MySQL

### WordPress
- Storage Class for WordPress files
- Persistent Volume for WordPress data
- Persistent Volume Claim for WordPress
- Deployment configuration for WordPress
- Service configuration for WordPress

## Usage

1. First apply the storage classes:
```bash
kubectl apply -f mysql/storage-class.yaml
kubectl apply -f wordpress/storage-class.yaml
```

2. Create the MySQL components:
```bash
kubectl apply -f mysql/
```

3. Create the WordPress components:
```bash
kubectl apply -f wordpress/
```

4. Wait for all pods to be ready:
```bash
kubectl get pods -w
```

5. Access WordPress through the service endpoint:
```bash
kubectl get svc wordpress
```

## Notes
- Make sure you have configured your AWS credentials properly
- The storage classes are configured for AWS EBS
- Adjust the resource requests/limits according to your needs
