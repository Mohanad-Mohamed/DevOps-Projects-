import boto3
from config import *

def setup_vpc():
    session = boto3.session.Session(profile_name=PROFILE_NAME)
    ec2_cli = session.client(service_name="ec2", region_name=REGION)
    ec2_resource = session.resource(service_name="ec2", region_name=REGION)

    # Create VPC
    new_vpc = ec2_cli.create_vpc(CidrBlock=VPC_CIDR)
    vpc_id = new_vpc['Vpc']['VpcId']
    print(f"New VPC has been created successfully with id {vpc_id}")

    # Create public subnets
    public_subnet_ids = []
    for cidr, az in zip(PUBLIC_SUBNET_CIDRS, AVAILABILITY_ZONES):
        response = ec2_cli.create_subnet(CidrBlock=cidr, VpcId=vpc_id, AvailabilityZone=az)
        public_subnet_ids.append(response['Subnet']['SubnetId'])
        
    # Enable auto-assign public IP
    for subnet_id in public_subnet_ids:
        ec2_cli.modify_subnet_attribute(SubnetId=subnet_id, MapPublicIpOnLaunch={'Value': True})

    # Create private subnets
    private_subnet_ids = []
    for cidr, az in zip(PRIVATE_SUBNET_CIDRS, AVAILABILITY_ZONES):
        response = ec2_cli.create_subnet(CidrBlock=cidr, VpcId=vpc_id, AvailabilityZone=az)
        private_subnet_ids.append(response['Subnet']['SubnetId'])

    # Create and attach Internet Gateway
    igw_response = ec2_cli.create_internet_gateway()
    internet_gateway_id = igw_response['InternetGateway']['InternetGatewayId']
    ec2_cli.attach_internet_gateway(InternetGatewayId=internet_gateway_id, VpcId=vpc_id)

    # Create and setup public route table
    public_rt = ec2_cli.create_route_table(VpcId=vpc_id)
    public_route_table_id = public_rt['RouteTable']['RouteTableId']
    
    for subnet_id in public_subnet_ids:
        ec2_cli.associate_route_table(RouteTableId=public_route_table_id, SubnetId=subnet_id)
    
    route_table = ec2_resource.RouteTable(public_route_table_id)
    route_table.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internet_gateway_id)

    # Create NAT Gateway
    allocation = ec2_cli.allocate_address(Domain='vpc')
    nat_response = ec2_cli.create_nat_gateway(
        AllocationId=allocation['AllocationId'],
        SubnetId=public_subnet_ids[0]
    )
    nat_gateway_id = nat_response['NatGateway']['NatGatewayId']

    # Wait for NAT Gateway to be available
    waiter = ec2_cli.get_waiter('nat_gateway_available')
    print("NAT Gateway is being started......")
    waiter.wait(NatGatewayIds=[nat_gateway_id])
    print("NAT Gateway is now up and available")

    # Create and setup private route table
    private_rt = ec2_cli.create_route_table(VpcId=vpc_id)
    private_route_table_id = private_rt['RouteTable']['RouteTableId']
    
    for subnet_id in private_subnet_ids:
        ec2_cli.associate_route_table(RouteTableId=private_route_table_id, SubnetId=subnet_id)
    
    route_table = ec2_resource.RouteTable(private_route_table_id)
    route_table.create_route(DestinationCidrBlock='0.0.0.0/0', NatGatewayId=nat_gateway_id)

    return {
        'vpc_id': vpc_id,
        'public_subnet_ids': public_subnet_ids,
        'private_subnet_ids': private_subnet_ids,
        'internet_gateway_id': internet_gateway_id,
        'nat_gateway_id': nat_gateway_id
    }
