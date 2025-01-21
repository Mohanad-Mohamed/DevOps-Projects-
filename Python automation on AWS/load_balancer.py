import boto3
from config import *

def create_load_balancer(vpc_id, public_subnet_ids, security_group_id, instance_ids):
    session = boto3.session.Session(profile_name=PROFILE_NAME)
    elbv2_client = session.client(service_name='elbv2', region_name=REGION)
    
    # Create Application Load Balancer
    response = elbv2_client.create_load_balancer(
        Name='MyALB',
        Subnets=public_subnet_ids,
        SecurityGroups=[security_group_id],
        Scheme='internet-facing',
        Type='application',
        IpAddressType='ipv4'
    )
    
    alb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
    print(f"Application Load Balancer has been created successfully with ARN: {alb_arn}")
    
    # Create Target Group
    response = elbv2_client.create_target_group(
        Name='MyTargetGroup',
        Protocol='HTTP',
        Port=80,
        VpcId=vpc_id,
        HealthCheckProtocol='HTTP',
        HealthCheckPort='80',
        HealthCheckPath='/',
        HealthCheckIntervalSeconds=30,
        HealthCheckTimeoutSeconds=5,
        HealthyThresholdCount=2,
        UnhealthyThresholdCount=2,
        Matcher={'HttpCode': '200'},
        TargetType='instance'
    )
    
    target_group_arn = response['TargetGroups'][0]['TargetGroupArn']
    
    # Register targets
    elbv2_client.register_targets(
        TargetGroupArn=target_group_arn,
        Targets=[{'Id': instance_id} for instance_id in instance_ids]
    )
    
    # Create Listener
    elbv2_client.create_listener(
        LoadBalancerArn=alb_arn,
        Protocol='HTTP',
        Port=80,
        DefaultActions=[
            {
                'Type': 'forward',
                'TargetGroupArn': target_group_arn
            }
        ]
    )
    
    # Wait for ALB to be active
    waiter = elbv2_client.get_waiter('load_balancer_available')
    print("Waiting for ALB to be active...")
    waiter.wait(LoadBalancerArns=[alb_arn])
    print("ALB is now active")
    
    return alb_arn, target_group_arn
