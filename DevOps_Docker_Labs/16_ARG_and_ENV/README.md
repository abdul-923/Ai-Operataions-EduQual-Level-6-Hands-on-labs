
# 16 - Docker ARG and ENV

## Overview

* This lab demonstrates Docker ARG and ENV variables.
* ARG is used during image build time.
* ENV is used when the container is running.
* A simple Python application reads the ENV variable.
* The lab builds and runs the Docker image with a custom APP_VERSION.

## Files Included

* README.md
* Dockerfile
* app.py
* Screenshots

## Lab Objectives

* Understand Docker ARG.
* Understand Docker ENV.
* Pass a build-time value using --build-arg.
* Set a runtime environment variable using ENV.
* Read an environment variable from Python.
* Build and run a Docker image.

## Commands Used

* mkdir "ARG and ENV"
* cd "ARG and ENV"
* nano Dockerfile
* echo 'print("Application environment:", os.environ.get("APP_ENV"))' > app.py
* nano app.py
* docker build --build-arg APP_VERSION=2.0.0 -t arg-env-demo .
* docker run --rm arg-env-demo


## Output

* Building version 2.0.0
* Application environment: production
* Docker image built successfully.
* Container ran successfully.

## What I Learned

* ARG stores values used during Docker image building.
* ENV stores values available inside the running container.
* --build-arg provides a value for ARG.
* Python can read Docker environment variables using os.environ.
* CMD defines the default application command.
* COPY places application files inside the image.
* docker build creates the image.
* docker run starts a container from the image.

## Key Concepts

* Dockerfile
* Docker Image
* Docker Container
* ARG
* ENV
* Build-time Variables
* Runtime Environment Variables
* Python Environment Variables
* CMD
* COPY
* WORKDIR
* Docker Build
* Docker Run

