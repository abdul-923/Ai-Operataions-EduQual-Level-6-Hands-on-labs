# Lab 3 – Running Docker Containers on AWS ECS

## Overview

In today's lab I learned how to run my Docker image on Amazon ECS using AWS Fargate.

I used Amazon ECR to store my Docker image and then created an ECS task definition to run the image. I also checked the container output using CloudWatch Logs.

## Files Included

* Dockerfile
* README.md
* Screenshots
* Commands History

## Commands Used

* aws sts get-caller-identity
* aws ecr describe-images --repository-name aws-ecr-lab --region us-east-1
* aws ecr list-images --repository-name aws-ecr-lab --region us-east-1
* aws ecr get-login-password --region us-east-1
* docker build -t aws-ecr-lab .
* docker run --rm aws-ecr-lab
* docker tag aws-ecr-lab ECR_REPOSITORY_URL/aws-ecr-lab:latest
* docker push ECR_REPOSITORY_URL/aws-ecr-lab:latest
* aws ecr delete-repository --repository-name aws-ecr-lab --region us-east-1 --force

## Output

The container successfully displayed:

Hello from my AWS ECR Docker container

The ECS task finished with exit code 0.

## Troubleshooting

The first ECS task failed because I used the wrong image tag in the task definition.

I used:

lates

The correct tag was:

latest

After creating a new task definition revision with the correct image tag the ECS task ran successfully.

## Cleanup

* Scaled the ECS service to 0 tasks
* Deleted the ECS service
* Deleted the ECS cluster
* Deregistered the ECS task definitions
* Deleted the ECR repository

## What I Learned

* ECS is used to run Docker containers
* ECR is used to store Docker images
* Fargate runs containers without managing EC2 servers
* Task definitions tell ECS how to run containers
* ECS pulls Docker images from ECR
* CloudWatch Logs can show container output
* Exit code 0 means the container completed successfully


## Lab Steps
Created an ECS cluster named aws-ecr-ecs-lab
Created an ECS task definition named aws-ecr-ecs-task
Configured Fargate as the launch type
Selected Linux X86_64
Configured CPU and memory
Added the ECR Docker image
Configured the ECS task execution role
Enabled CloudWatch logging
Created an ECS service
Started an ECS task
Fargate pulled the Docker image from ECR
Container started successfully
Verified the container output in CloudWatch Logs

## AWS Resources Used
Amazon ECS
Amazon ECR
AWS Fargate
CloudWatch Logs
IAM Task Execution Role
VPC

## The Whole Lab in One Picture

Dockerfile
↓
Docker Image
↓
Amazon ECR
↓
ECS Task Definition
↓
AWS Fargate
↓
ECS Task
↓
Docker Container
↓
CloudWatch Logs

## Conclusion

In this lab I successfully ran my Docker image on Amazon ECS using AWS Fargate. I also learned how ECR and ECS work together to deploy and run Docker containers.
