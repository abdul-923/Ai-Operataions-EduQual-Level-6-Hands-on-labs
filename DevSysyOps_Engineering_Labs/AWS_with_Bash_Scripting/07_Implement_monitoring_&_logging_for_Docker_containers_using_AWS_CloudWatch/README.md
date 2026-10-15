

# Lab 7 – Monitoring Docker Containers with Amazon CloudWatch

## Overview

In this lab I learned how to monitor Docker containers using Amazon CloudWatch.

I created an EC2 instance and deployed an Nginx Docker container.

I installed and configured the CloudWatch Agent on the EC2 instance.

The CloudWatch Agent collected the Docker container logs and sent them to Amazon CloudWatch.

I also attached an IAM role to the EC2 instance so the CloudWatch Agent could send logs to CloudWatch.

Finally I viewed the Nginx Docker logs from the CloudWatch Console.

## Files Included

- README.md

## Commands Used

### SSH into EC2

ssh -i ./lab7.pem ubuntu@YOUR_EC2_PUBLIC_IP

### Install Docker

sudo apt update

sudo apt install -y docker.io

sudo systemctl enable --now docker

### Check Docker Version

sudo docker --version

### Run Nginx Container

sudo docker run -d --name nginx-container -p 80:80 nginx

### Check Running Container

sudo docker ps

### Test Nginx

curl http://localhost

### Download CloudWatch Agent

wget https://amazoncloudwatch-agent.s3.amazonaws.com/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb

### Install CloudWatch Agent

sudo dpkg -i -E ./amazon-cloudwatch-agent.deb

### Check CloudWatch Agent Status

sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status

### Create CloudWatch Configuration

nano cloudwatch-config.json

The configuration was created to collect Docker container logs from:

/var/lib/docker/containers/*/*.log

The logs were sent to the CloudWatch log group:

docker-logs

### Start CloudWatch Agent

sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:cloudwatch-config.json -s

### Check CloudWatch Agent

sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status

### Restart CloudWatch Agent

sudo systemctl restart amazon-cloudwatch-agent

### Check Docker Logs

sudo docker logs nginx-container

### Generate Nginx Requests

curl http://localhost

## Output

The EC2 instance was created successfully.

Docker was installed successfully.

An Nginx Docker container was deployed and running.

The CloudWatch Agent was installed and configured successfully.

An IAM role with CloudWatch permissions was attached to the EC2 instance.

Docker container logs were collected by the CloudWatch Agent.

The logs were sent to the docker-logs CloudWatch log group.

The Nginx logs were successfully viewed in Amazon CloudWatch.

## What I Learned

- I learned what Amazon CloudWatch is.
- I learned what the CloudWatch Agent does.
- I learned how Docker container logs are stored on an EC2 instance.
- I learned how to collect Docker logs using the CloudWatch Agent.
- I learned how to send EC2 logs to CloudWatch.
- I learned why an IAM role is required for the EC2 instance.
- I learned how to configure the CloudWatch Agent manually.
- I learned how to view Docker logs from the AWS Console.
- I learned what centralized monitoring means.
- I learned how centralized logging allows multiple servers and applications to be monitored from one place.
- I learned that CloudWatch can be used for monitoring and logging.
- I learned the difference between the CloudWatch service and the CloudWatch Agent.

## The Whole Lab in One Picture

EC2 Instance

↓

Docker

↓

Nginx Container

↓

Docker Logs

↓

CloudWatch Agent

↓

IAM Permissions

↓

Amazon CloudWatch

↓

CloudWatch Log Group

↓

View Logs

## Conclusion

In this lab I successfully deployed an Nginx Docker container on an EC2 instance and integrated its logs with Amazon CloudWatch.

The CloudWatch Agent collected the Docker logs and sent them to CloudWatch.

This demonstrated how centralized logging can be used to monitor Docker containers from one place instead of checking each EC2 instance separately.
