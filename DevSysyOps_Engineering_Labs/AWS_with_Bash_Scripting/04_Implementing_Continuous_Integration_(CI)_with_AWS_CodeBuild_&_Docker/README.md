# Lab 4 – Implementing Continuous Integration with AWS CodeBuild and Docker

## Overview

In today's ver beautiful lab I learned how Continuous Integration works with GitHub AWS CodeBuild Docker and Amazon ECR.

I created a simple application and Dockerfile in my GitHub repository. I then created an AWS CodeBuild project and connected it with GitHub.

When I pushed changes to GitHub CodeBuild automatically started the build. It read the buildspec.yml file built the Docker image and pushed the image to Amazon ECR.

## Files Included

- Dockerfile
- app.js
- package.json
- buildspec.yml
- README.md
- Screensghots

## Commands Used

- git add .
- git commit -m "Commit message"
- git push origin main
- aws sts get-caller-identity
- aws ecr get-login-password --region us-east-1
- docker build -t $REPOSITORY_URI:latest .
- docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG
- docker push $REPOSITORY_URI:latest
- docker push $REPOSITORY_URI:$IMAGE_TAG

## Output

The GitHub repository was successfully connected to AWS CodeBuild.

The CodeBuild project automatically detected the GitHub push.

CodeBuild successfully built the Docker image.

The Docker image was successfully pushed to Amazon ECR.

The ECR repository contained the image with the latest tag.

## Troubleshooting

The first build failed because the CodeBuild service role did not have permission to access Amazon ECR.

I fixed this by giving the CodeBuild service role the required ECR permissions.

The second build failed because CodeBuild could not find the Dockerfile.

The Dockerfile was inside the Lab 4 directory instead of the repository root.

I added the cd command in buildspec.yml to move into the Lab 4 directory before running the Docker build.

After pushing the updated buildspec.yml to GitHub the CodeBuild project successfully built and pushed the Docker image to Amazon ECR.

## Cleanup

- No ECS resources were created in this lab
- The Docker image was stored in Amazon ECR
- The CodeBuild project can be deleted after the lab if it is no longer needed
- The ECR repository can also be deleted after the lab if it is no longer needed

## What I Learned

- Continuous Integration automatically builds and tests code after changes are pushed
- GitHub can be used as the source repository for AWS CodeBuild
- AWS CodeBuild is a managed build service
- buildspec.yml contains instructions for CodeBuild
- IAM permissions control what CodeBuild can access
- CodeBuild can build Docker images automatically
- Amazon ECR stores Docker images
- GitHub webhooks can trigger CodeBuild automatically
- CI does not necessarily mean deployment
- Continuous Deployment is a separate step where the application is automatically deployed

## The Whole Lab in One Picture

GitHub 
↓ 
Git Push 
↓ 
GitHub Webhook 
↓ 
AWS CodeBuild 
↓ 
buildspec.yml 
↓ 
Docker Build 
↓ 
Docker Image 
↓ 
Amazon ECR

## Conclusion

In this lab I successfully implemented a basic Continuous Integration workflow using GitHub AWS CodeBuild Docker and Amazon ECR.

After pushing code to GitHub AWS CodeBuild automatically built the Docker image and pushed it to Amazon ECR.

This helped me understand how automation can reduce manual work in the software development process.
