from vpc_setup import setup_vpc
from security_groups import create_security_groups
from ec2_setup import launch_ec2_instances
from load_balancer import create_load_balancer
from rds_setup import create_rds_instance

def main():
    try:
        # Step 1: Setup VPC and networking components
        print("Setting up VPC and networking components...")
        vpc_info = setup_vpc()
        vpc_id = vpc_info['vpc_id']
        public_subnet_ids = vpc_info['public_subnet_ids']
        private_subnet_ids = vpc_info['private_subnet_ids']
        
        # Step 2: Create security groups
        print("\nCreating security groups...")
        sg_info = create_security_groups(vpc_id)
        web_sg_id = sg_info['web_sg_id']
        alb_sg_id = sg_info['alb_sg_id']
        rds_sg_id = sg_info['rds_sg_id']
        
        # Step 3: Launch EC2 instances
        print("\nLaunching EC2 instances...")
        instance_ids = launch_ec2_instances(private_subnet_ids, web_sg_id)
        
        # Step 4: Create Application Load Balancer
        print("\nCreating Application Load Balancer...")
        alb_arn, target_group_arn = create_load_balancer(
            vpc_id, 
            public_subnet_ids, 
            alb_sg_id, 
            instance_ids
        )
        
        # Step 5: Create RDS instance
        print("\nCreating RDS instance...")
        rds_arn, rds_endpoint = create_rds_instance(
            vpc_id,
            private_subnet_ids,
            rds_sg_id
        )
        
        print("\nInfrastructure setup completed successfully!")
        print(f"VPC ID: {vpc_id}")
        print(f"ALB ARN: {alb_arn}")
        print(f"RDS Endpoint: {rds_endpoint}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()
