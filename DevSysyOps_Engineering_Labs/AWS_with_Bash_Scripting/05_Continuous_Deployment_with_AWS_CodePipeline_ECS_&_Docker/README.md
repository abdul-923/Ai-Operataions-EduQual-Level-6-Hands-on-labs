

# Lab 5 – Continuous Deployment with AWS CodePipeline ECS and Docker

## Overview

In today’s lab I learned how to implement Continuous Deployment using AWS CodePipeline.

I connected my GitHub repository with AWS CodePipeline.

CodePipeline automatically downloaded the source code and started the build process.

AWS CodeBuild built the Docker image and pushed it to Amazon ECR.

After the build was completed CodePipeline deployed the application to Amazon ECS.

The final pipeline successfully completed all three stages:

Source → Build → Deploy

The Docker container is now running on Amazon ECS using AWS Fargate.

## Files Included

- Dockerfile
- app.js
- package.json
- buildspec.yml
- README.md

## Commands Used

### Check Git Status

git status

### Add Files

git add .

### Commit Changes

git commit -m "Add Lab 5 files"

### Push to GitHub

git push origin main

### Docker Build

docker build -t aws-codepipeline-lab .

### Docker Run

docker run --rm aws-codepipeline-lab

### AWS Identity Check

aws sts get-caller-identity

### ECR Login

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

### Docker Tag

docker tag aws-codepipeline-lab AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/aws-codepipeline-lab:latest

### Push Docker Image to ECR

docker push AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/aws-codepipeline-lab:latest

### Check ECR Images

aws ecr describe-images --repository-name aws-codepipeline-lab --region us-east-1

## Output

The GitHub repository was successfully connected to AWS CodePipeline.

The Source stage successfully downloaded the latest code from GitHub.

The Build stage successfully started AWS CodeBuild.

AWS CodeBuild successfully built the Docker image.

The Docker image was successfully pushed to Amazon ECR.

The Deploy stage successfully deployed the application to Amazon ECS.

The ECS service successfully started the Docker container.

The final CodePipeline execution completed successfully.

## Troubleshooting

### CodePipeline Could Not Start CodeBuild

The CodePipeline service role did not have permission to pass the CodeBuild service role.

The required IAM permission was added to the AWS CodePipeline service role.

After adding the permission the Build stage was able to start successfully.

### Buildspec File Not Found

CodeBuild initially could not find the buildspec.yml file because the buildspec path was configured incorrectly.

The correct buildspec path was configured as:

DevSysyOps_Engineering_Labs/05_Continuous_Deployment_with_AWS_CodePipeline_ECS_&_Docker/buildspec.yml

After correcting the path CodeBuild successfully downloaded and processed the buildspec.yml file.

### Artifact Upload Error

The build itself completed successfully but the artifact upload failed because the generated imagedefinitions.json file was not being found from the configured artifact path.

The buildspec.yml was corrected so that imagedefinitions.json was created in the correct location.

After the correction the Build stage completed successfully.

## Cleanup

After completing the lab the following AWS resources can be removed to avoid unnecessary charges:

- CodePipeline
- CodeBuild project
- ECS service
- ECS cluster
- ECR repository
- ECR Docker images
- CloudWatch log groups if no longer required

IAM roles and policies do not have an hourly running charge.

## What I Learned

- I learned how Continuous Deployment works with AWS CodePipeline.
- I learned how GitHub can act as the source stage.
- I learned how CodePipeline connects different AWS services together.
- I learned how CodeBuild automatically builds a Docker image.
- I learned how Docker images are stored in Amazon ECR.
- I learned how ECS uses the Docker image from ECR.
- I learned how ECS Fargate runs containers without managing EC2 servers.
- I learned how an ECS service keeps the required number of containers running.
- I learned how imagedefinitions.json connects the Docker image with ECS deployment.
- I learned how IAM permissions allow CodePipeline to start CodeBuild and perform deployment actions.
- I learned how Continuous Deployment can automatically move an application from source code to a running container.

## The Whole Lab in One Picture

GitHub

↓

AWS CodePipeline

↓

Source Stage

↓

AWS CodeBuild

↓

Docker Build

↓

Amazon ECR

↓

Amazon ECS

↓

AWS Fargate

↓

Running Docker Container

## Conclusion

In this lab I successfully created a Continuous Deployment pipeline using AWS CodePipeline.

The pipeline automatically takes the application from GitHub and sends it to CodeBuild.

CodeBuild builds the Docker image and pushes it to Amazon ECR.

CodePipeline then deploys the image to Amazon ECS.

The final deployment was successful and the Docker container is running on ECS.

This lab helped me understand how CI/CD works in a real AWS environment and how different AWS services work together to automate application deployment.
