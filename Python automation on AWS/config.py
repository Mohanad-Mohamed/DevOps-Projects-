# AWS Configuration
REGION = "us-east-1"
PROFILE_NAME = "dev_admin"

# VPC Configuration
VPC_CIDR = "10.0.0.0/16"
PUBLIC_SUBNET_CIDRS = ['10.0.10.0/24', '10.0.20.0/24']
PRIVATE_SUBNET_CIDRS = ['10.0.100.0/24', '10.0.200.0/24']
AVAILABILITY_ZONES = ['us-east-1a', 'us-east-1b']

# EC2 Configuration
AMI_ID = 'ami-0889a44b331db0194'
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'MyKey'

# RDS Configuration
DB_INSTANCE_CLASS = 'db.t3.micro'
DB_ENGINE = 'mysql'
DB_NAME = 'MyDB'
DB_USERNAME = 'admin'
DB_PASSWORD = 'your-password-here'  # Change this in production
