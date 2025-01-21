import boto3
from config import *

def get_user_data_scripts():
    script1 = '''#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
echo "This is server *1* in AWS Region US-EAST-1 in AZ US-EAST-1A" > /var/www/html/index.html
'''

    script2 = '''#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
echo "This is server *2* in AWS Region US-EAST-1 in AZ US-EAST-1B" > /var/www/html/index.html
'''
    return [script1, script2]

def launch_ec2_instances(private_subnet_ids, security_group_id):
    session = boto3.session.Session(profile_name=PROFILE_NAME)
    ec2_cli = session.client(service_name="ec2", region_name=REGION)
    
    user_data_scripts = get_user_data_scripts()
    instance_ids = []

    for subnet_id, user_data_script in zip(private_subnet_ids, user_data_scripts):
        response = ec2_cli.run_instances(
            ImageId=AMI_ID,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            MinCount=1,
            MaxCount=1,
            SubnetId=subnet_id,
            UserData=user_data_script,
            SecurityGroupIds=[security_group_id],
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/xvda',
                    'Ebs': {
                        'VolumeSize': 8,
                        'VolumeType': 'gp2'
                    }
                }
            ],
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': f'WebServer-{private_subnet_ids.index(subnet_id) + 1}'
                        }
                    ]
                }
            ]
        )
        instance_ids.append(response['Instances'][0]['InstanceId'])

    # Wait for instances to be running
    waiter = ec2_cli.get_waiter('instance_running')
    print("Waiting for instances to be running...")
    waiter.wait(InstanceIds=instance_ids)
    print("All instances are now running")

    return instance_ids
