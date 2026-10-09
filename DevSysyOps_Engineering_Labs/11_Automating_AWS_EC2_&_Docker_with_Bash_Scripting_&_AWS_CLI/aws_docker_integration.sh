

#!/bin/bash

set -e

echo "===== AWS CLI and Docker Automation ====="

# Check AWS CLI
if ! command -v aws >/dev/null 2>&1; then
    echo "AWS CLI is not installed"
    exit 1
fi

if ! aws sts get-caller-identity >/dev/null 2>&1; then
    echo "AWS credentials are not configured or are invalid"
    exit 1
fi

# Collect AWS details
read -rp "Enter AWS region: " aws_region
read -rp "Enter Ubuntu AMI ID for this region: " ami_id
read -rp "Enter EC2 key pair name: " key_name
read -rp "Enter path to your PEM file: " key_file
read -rp "Enter security group ID: " security_group_id
read -rp "Enter subnet ID: " subnet_id

key_file="${key_file/#\~/$HOME}"

if [[ ! -f "$key_file" ]]; then
    echo "PEM file not found: $key_file"
    exit 1
fi

chmod 400 "$key_file"

# Verify the AWS resources
aws ec2 describe-key-pairs \
    --region "$aws_region" \
    --key-names "$key_name" >/dev/null

aws ec2 describe-security-groups \
    --region "$aws_region" \
    --group-ids "$security_group_id" >/dev/null

aws ec2 describe-subnets \
    --region "$aws_region" \
    --subnet-ids "$subnet_id" >/dev/null

# Launch EC2 and install Docker
echo "Launching EC2 instance..."

instance_id=$(aws ec2 run-instances \
    --region "$aws_region" \
    --image-id "$ami_id" \
    --instance-type t2.micro \
    --key-name "$key_name" \
    --security-group-ids "$security_group_id" \
    --subnet-id "$subnet_id" \
    --associate-public-ip-address \
    --user-data '#!/bin/bash
apt-get update
apt-get install -y docker.io
systemctl enable --now docker
usermod -aG docker ubuntu' \
    --tag-specifications \
    'ResourceType=instance,Tags=[{Key=Name,Value=aws-docker-lab}]' \
    --query 'Instances[0].InstanceId' \
    --output text)

echo "Instance ID: $instance_id"
echo "Waiting for EC2 status checks..."

aws ec2 wait instance-status-ok \
    --region "$aws_region" \
    --instance-ids "$instance_id"

public_ip=$(aws ec2 describe-instances \
    --region "$aws_region" \
    --instance-ids "$instance_id" \
    --query 'Reservations[0].Instances[0].PublicIpAddress' \
    --output text)

if [[ -z "$public_ip" || "$public_ip" == "None" ]]; then
    echo "No public IP found. Check your subnet configuration."
    exit 1
fi

echo "EC2 Public IP: $public_ip"
echo "Waiting for SSH and Docker to become ready..."

# Wait for Docker to be ready on EC2
for attempt in {1..36}; do
    if ssh -i "$key_file" \
        -o StrictHostKeyChecking=accept-new \
        -o ConnectTimeout=5 \
        -o BatchMode=yes \
        "ubuntu@$public_ip" \
        'sudo docker info >/dev/null 2>&1' 2>/dev/null; then
        break
    fi

    if [[ "$attempt" -eq 36 ]]; then
        echo "Docker did not become ready in time."
        echo "Check EC2 system logs and security group SSH rules."
        exit 1
    fi

    sleep 10
done

echo "Running Docker container on EC2..."

ssh -i "$key_file" \
    -o StrictHostKeyChecking=accept-new \
    "ubuntu@$public_ip" \
    'sudo docker run --rm hello-world'

echo "===== LAB COMPLETED SUCCESSFULLY ====="
echo "Instance ID: $instance_id"
echo "Public IP: $public_ip"
echo "Remember to terminate the EC2 instance when finished."

