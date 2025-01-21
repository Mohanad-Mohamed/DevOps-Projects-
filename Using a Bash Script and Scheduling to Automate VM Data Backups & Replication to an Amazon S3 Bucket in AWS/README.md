# Automated Backup System with AWS S3 Integration

This project implements an automated backup system that creates local backups and uploads them to Amazon S3. It includes two versions of the backup script and instructions for setting up automated backups using cron.

## Features
- Local backup creation with timestamp
- Logging functionality
- AWS S3 integration
- Automated scheduling with cron

## Prerequisites
- Ubuntu/Linux system
- AWS CLI installed
- AWS IAM user with S3 access
- AWS IAM role configured for EC2 (if running on EC2)

## Setup Instructions
1. Install AWS CLI:
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install
```

2. Configure AWS CLI:
```bash
aws configure
```

3. Make the backup scripts executable:
```bash
chmod +x backup-script-local.sh
chmod +x backup-script-s3.sh
```

## Files Description
- `backup-script-local.sh`: Basic backup script with local storage
- `backup-script-s3.sh`: Advanced backup script with AWS S3 integration
- `crontab-example`: Example crontab configuration for automation

## Usage
1. For local backup only:
```bash
./backup-script-local.sh [directory_to_backup]
```

2. For backup with S3 upload:
```bash
./backup-script-s3.sh
```

## Automation
To set up automated backups, add the provided crontab entry to `/etc/crontab`

## Cleanup
To remove S3 bucket and contents:
```bash
aws s3 rb s3://[bucket-name] --force
```
