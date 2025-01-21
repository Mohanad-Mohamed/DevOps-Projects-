import boto3
from config import *

def create_rds_instance(vpc_id, private_subnet_ids, security_group_id):
    session = boto3.session.Session(profile_name=PROFILE_NAME)
    rds_client = session.client(service_name='rds', region_name=REGION)
    
    # Create DB subnet group
    rds_client.create_db_subnet_group(
        DBSubnetGroupName='MyDBSubnetGroup',
        DBSubnetGroupDescription='Subnet group for RDS instance',
        SubnetIds=private_subnet_ids
    )
    
    # Create RDS instance
    response = rds_client.create_db_instance(
        DBName=DB_NAME,
        DBInstanceIdentifier='my-database',
        AllocatedStorage=20,
        DBInstanceClass=DB_INSTANCE_CLASS,
        Engine=DB_ENGINE,
        MasterUsername=DB_USERNAME,
        MasterUserPassword=DB_PASSWORD,
        VpcSecurityGroupIds=[security_group_id],
        DBSubnetGroupName='MyDBSubnetGroup',
        PubliclyAccessible=False,
        MultiAZ=False,
        AutoMinorVersionUpgrade=True,
        Port=3306,
        EngineVersion='8.0.28'
    )
    
    # Wait for RDS instance to be available
    waiter = rds_client.get_waiter('db_instance_available')
    print("Waiting for RDS instance to be available...")
    waiter.wait(DBInstanceIdentifier='my-database')
    print("RDS instance is now available")
    
    # Get RDS instance details
    response = rds_client.describe_db_instances(DBInstanceIdentifier='my-database')
    rds_arn = response['DBInstances'][0]['DBInstanceArn']
    rds_endpoint = response['DBInstances'][0]['Endpoint']['Address']
    
    return rds_arn, rds_endpoint
