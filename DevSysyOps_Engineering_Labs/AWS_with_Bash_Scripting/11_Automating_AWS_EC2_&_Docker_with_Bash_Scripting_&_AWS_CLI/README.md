
# Lab 11 – Automating AWS EC2 and Docker with Bash Scripting and AWS CLI

## Overview

In this lab I learned how to automate AWS EC2 operations using Bash scripting and AWS CLI.

I created a Bash script to check AWS credentials and launch an EC2 instance.

The script retrieves the instance details and connects to the instance through SSH.

It then runs a Docker container on the EC2 instance.

## Files Included

- aws_docker_integration.sh
- README.md
- Command-history
- Screenshots

## Commands Used

- aws --version
- aws sts get-caller-identity
- aws ec2 describe-images
- aws ec2 describe-key-pairs
- aws ec2 describe-security-groups
- aws ec2 describe-subnets
- aws ec2 run-instances
- aws ec2 wait instance-status-ok
- aws ec2 describe-instances
- ssh
- chmod +x aws_docker_integration.sh
- ./aws_docker_integration.sh
- docker run --rm hello-world

## Output

- AWS CLI installation was verified.
- AWS credentials were checked.
- The Ubuntu AMI ID was retrieved.
- The EC2 key pair was identified.
- The security group and subnet were selected.
- The Bash script launched an EC2 instance.
- The script retrieved the public IP address.
- The script connected to EC2 through SSH.
- Docker was installed on the EC2 instance.
- The Docker Hello World container was executed.

## What I Learned

- I learned how to use AWS CLI with Bash scripting.
- I learned how to verify AWS credentials.
- I learned how to retrieve AWS resource information.
- I learned how to launch EC2 instances using a script.
- I learned the purpose of an AMI ID.
- I learned the purpose of an EC2 key pair.
- I learned how security groups control network traffic.
- I learned what a subnet is.
- I learned how to connect to EC2 through SSH.
- I learned how to automate Docker operations on EC2.
- I learned how to combine AWS CLI and Docker in one workflow.

## Conclusion

In this lab I explored how Bash scripting can automate AWS and Docker operations.

The script combines EC2 provisioning with SSH connectivity and Docker execution.

This helped me understand how cloud infrastructure and container operations can be automated using a single script.

Note: The README describes the intended successful workflow. Only mark every step as completed if your script actually finished successfully. Terminate the EC2 instance after testing if you no longer need it.
