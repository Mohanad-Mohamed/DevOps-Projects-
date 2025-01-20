import boto3
from config import *

def create_security_groups(vpc_id):
    session = boto3.session.Session(profile_name=PROFILE_NAME)
    ec2_cli = session.client(service_name="ec2", region_name=REGION)

    # Create Web Security Group
    web_sg = ec2_cli.create_security_group(
        Description='Private SG for EC2 Instances',
        GroupName='Private_SG',
        VpcId=vpc_id,
        TagSpecifications=[
            {
                'ResourceType': 'security-group',
                'Tags': [{'Key': 'Name', 'Value': 'WebSG'}]
            }
        ]
    )
    web_sg_id = web_sg['GroupId']

    # Configure Web Security Group rules
    ec2_cli.authorize_security_group_ingress(
        GroupId=web_sg_id,
        IpPermissions=[
            {
                'FromPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'SSH access'}],
                'ToPort': 22
            },
            {
                'FromPort': 80,
                'IpProtocol': 'tcp',
                'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'HTTP access'}],
                'ToPort': 80
            },
            {
                'FromPort': 443,
                'IpProtocol': 'tcp',
                'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'Secure HTTP access'}],
                'ToPort': 443
            }
        ]
    )

    # Add egress rule for Web Security Group
    ec2_cli.authorize_security_group_egress(
        GroupId=web_sg_id,
        IpPermissions=[
            {
                'FromPort': 0,
                'IpProtocol': 'tcp',
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
                'ToPort': 0
            }
        ]
    )

    # Create ALB Security Group
    alb_sg = ec2_cli.create_security_group(
        Description='Security Group for Application Load Balancer',
        GroupName='ALB_SG',
        VpcId=vpc_id,
        TagSpecifications=[
            {
                'ResourceType': 'security-group',
                'Tags': [{'Key': 'Name', 'Value': 'ALB_SG'}]
            }
        ]
    )
    alb_sg_id = alb_sg['GroupId']

    # Configure ALB Security Group rules
    ec2_cli.authorize_security_group_ingress(
        GroupId=alb_sg_id,
        IpPermissions=[
            {
                'FromPort': 80,
                'IpProtocol': 'tcp',
                'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'HTTP access'}],
                'ToPort': 80
            }
        ]
    )

    # Create RDS Security Group
    rds_sg = ec2_cli.create_security_group(
        Description='Security Group for RDS Instance',
        GroupName='RDS_SG',
        VpcId=vpc_id,
        TagSpecifications=[
            {
                'ResourceType': 'security-group',
                'Tags': [{'Key': 'Name', 'Value': 'RDS_SG'}]
            }
        ]
    )
    rds_sg_id = rds_sg['GroupId']

    # Configure RDS Security Group rules
    ec2_cli.authorize_security_group_ingress(
        GroupId=rds_sg_id,
        IpPermissions=[
            {
                'FromPort': 3306,
                'IpProtocol': 'tcp',
                'UserIdGroupPairs': [{'GroupId': web_sg_id}],
                'ToPort': 3306
            }
        ]
    )

    return {
        'web_sg_id': web_sg_id,
        'alb_sg_id': alb_sg_id,
        'rds_sg_id': rds_sg_id
    }
