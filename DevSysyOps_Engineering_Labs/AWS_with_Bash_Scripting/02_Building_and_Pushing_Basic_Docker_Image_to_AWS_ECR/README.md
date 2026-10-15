

# Lab 02 – Building and Pushing Basic Docker Image to AWS ECR

## Overview

In this lab I built a basic Docker image and pushed it to AWS Elastic Container Registry.

I configured AWS CLI and created an IAM user for AWS CLI access.

I created an ECR repository and authenticated Docker with AWS ECR.

I then tagged the Docker image and pushed it to the ECR repository.

## Files Included

* Dockerfile
* README.md
* Screenshots

## Commands Used

### Check Docker

* docker --version
* sudo docker run hello-world

### Install AWS CLI

* aws --version
* curl -fsSL [https://awscli.amazonaws.com/v2/install.sh](https://awscli.amazonaws.com/v2/install.sh) | sudo bash -s -- --system

### Configure AWS CLI

* aws configure
* aws sts get-caller-identity

### Create Dockerfile

* vim Dockerfile
* cat Dockerfile

### Build Docker Image

* docker build -t aws-ecr-lab .
* docker images
* docker run --rm aws-ecr-lab

### Create ECR Repository

* aws ecr create-repository --repository-name aws-ecr-lab --region us-east-1

### Authenticate Docker with ECR

* aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

### Tag Docker Image

* docker tag aws-ecr-lab ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/aws-ecr-lab:latest

### Push Docker Image to ECR

* docker push ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/aws-ecr-lab:latest

### Verify Image in ECR

* aws ecr describe-images --repository-name aws-ecr-lab --region us-east-1
* aws ecr list-images --repository-name aws-ecr-lab --region us-east-1

### Delete ECR Repository

* aws ecr delete-repository --repository-name aws-ecr-lab --region us-east-1 --force

## Output

Docker was installed and tested successfully.

AWS CLI was installed and configured successfully.

An IAM user was created for AWS CLI access.

An IAM group was created and permissions were assigned to the user.

An ECR repository was created successfully.

Docker was authenticated with AWS ECR.

The Docker image was successfully built.

The Docker image was successfully tagged.

The Docker image was successfully pushed to AWS ECR.

The Docker image was verified in the ECR repository.

## What I Learned

* ECR stands for Elastic Container Registry
* ECR is used to store Docker container images
* An ECR registry is the registry provided by AWS
* An ECR repository stores Docker images
* IAM controls access to AWS resources
* IAM users provide an identity for accessing AWS
* IAM groups are used to manage permissions
* AWS CLI allows AWS services to be managed from the terminal
* aws configure sets up AWS CLI credentials
* Docker login authenticates Docker with ECR
* Docker tag connects a local image with an ECR repository
* Docker push uploads an image to ECR
* ECR can be used as a private container registry

## The Whole Lab in One Picture

Dockerfile

↓

Docker Build

↓

Docker Image

↓

AWS CLI Configuration

↓

IAM User

↓

IAM Group and Permissions

↓

ECR Repository

↓

Docker Login

↓

Docker Tag

↓

Docker Push

↓

AWS ECR

↓

Docker Image Stored in ECR

## Conclusion

In this lab I learned how to build a Docker image and push it to AWS ECR.

I also learned how IAM and AWS CLI work together to authenticate and access AWS services.

This lab helped me understand how Docker images can be stored in a cloud container registry and later pulled by other systems such as EC2.

