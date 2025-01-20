# AWS Infrastructure Setup Project

This project sets up a complete AWS infrastructure using Python and Boto3, including VPC, subnets, EC2 instances, load balancers, and RDS.

## Project Structure

- `vpc_setup.py`: VPC and networking components setup
- `security_groups.py`: Security group configurations
- `ec2_setup.py`: EC2 instance deployment
- `load_balancer.py`: Application Load Balancer setup
- `rds_setup.py`: RDS database setup
- `config.py`: Configuration variables

## Prerequisites

- Python 3.x
- Boto3 library
- AWS credentials configured with appropriate permissions
- AWS CLI profile named "dev_admin" with admin privileges

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Configure your AWS credentials and ensure you have a profile named "dev_admin"

## Usage

Run the main script to set up the complete infrastructure:
```bash
python main.py
```

## Infrastructure Components

- VPC with CIDR 10.0.0.0/16
- 2 Public Subnets (10.0.10.0/24, 10.0.20.0/24)
- 2 Private Subnets (10.0.100.0/24, 10.0.200.0/24)
- Internet Gateway
- NAT Gateway
- Application Load Balancer
- EC2 Instances in private subnets
- RDS Instance
- Security Groups for EC2, ALB, and RDS

## Security Groups

- WebSG: For EC2 instances (ports 22, 80, 443)
- ALB_SG: For Application Load Balancer (port 80)
- RDS_SG: For RDS instance (port 3306)
