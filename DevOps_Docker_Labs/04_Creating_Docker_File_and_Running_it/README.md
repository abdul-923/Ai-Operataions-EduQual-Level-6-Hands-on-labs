

# Lab 4: Creating Dockerfile and Running It

## Overview

* Created a custom Dockerfile for building a Docker image.
* Built a custom Ubuntu-based Docker image.
* Used Docker build commands with a custom Dockerfile name.
* Verified the newly created Docker image.
* Started the custom image in interactive mode.
* Performed a package/environment check inside the container.

## Files Included

* README.md
* Dockerfile.test
* Screenshots

## Commands Used

* cd ..
* mkdir "Creating_Docker_File_and_Runningt_it"
* cd "Creating_Docker_File_and_Runningt_it"
* nano Dockerfile.test
* docker build -t my-ubuntu .
* docker build -f Dockerfile.test -t my-ubuntu
* docker images
* docker run -it my-ubuntu
* curl --version
* git add .
* git commit -m
* git push origin main


## Output

* Created Dockerfile.test successfully.
* Built the custom my-ubuntu Docker image successfully.
* Verified the image using docker images.
* Started the custom Ubuntu container in interactive mode.
* Successfully accessed the container terminal.
* Verified curl and related environment information inside the container.

## What I Learned

* A Dockerfile contains instructions for building a Docker image.
* Dockerfiles normally do not require a file extension.
* A custom Dockerfile name can be specified using the -f option.
* The dot in docker build -t my-ubuntu . represents the current directory.
* docker build creates an image from a Dockerfile.
* docker run creates and starts a container from an image.
* The -it option allows interactive access to the container.
* Docker images can be verified using docker images.
* A custom Docker image can contain additional packages and configurations.
* Dockerfiles provide a repeatable way to build application environments.
