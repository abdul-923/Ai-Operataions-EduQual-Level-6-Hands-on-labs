
# Docker Environment Variables Lab

## Overview

* Demonstrates how environment variables are passed into Docker containers.
* Uses Ubuntu 24.04 as the base image.
* Passes a variable from the host into the container at runtime.
* Verifies that the container can read and use the variable.

## Files Included

* Dockerfile 
* README.md 
* Screenshots

## Lab Objectives

* Understand Docker environment variables.
* Understand the difference between a Docker image and a running container.
* Learn how to pass values into a container using the Docker run command.
* Verify that the container can access the supplied variable.

## Dockerfile

* FROM ubuntu:24.04 — Uses Ubuntu 24.04 as the base image.
* CMD — Runs a shell command when the container starts.
* echo Hello $MY_NAME — Prints the value supplied through the MY_NAME environment variable.

## Commands Used

* mkdir 05_Environment_Variables — Creates the lab directory.
* cd 05_Environment_Variables — Enters the lab directory.
* nano Dockerfile — Creates and edits the Dockerfile.
* docker build -t my-env . — Builds the Docker image and tags it as my-env.
* docker run -e MY_NAME="ALICE" my-env — Runs the container and passes MY_NAME from outside the Dockerfile.

## Output

* Docker image successfully built and tagged as my-env:latest.
* Ubuntu 24.04 downloaded as the base image.
* MY_NAME successfully passed at runtime.
* Container successfully printed Hello ALICE.

## What I Learned

* FROM defines the base image.
* Environment variables can be supplied from outside the Dockerfile.
* The -e option passes an environment variable to a running container.
* Containers can use externally supplied configuration values.
* Environment variables allow configuration without modifying application code.

## Key Concept

* Host value → Docker run -e → Container environment variable → Application uses the value

## The Whole Lab in One Picture

* Create Dockerfile → Build image → Run container with -e → Container receives MY_NAME → Container prints the value

[
