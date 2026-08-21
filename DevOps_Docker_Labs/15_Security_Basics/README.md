
# 15 Security Basics

## Overview

This lab focuses on basic Docker container security and resource control.

The lab covers:

* Running containers as non-root users
* Dropping Linux capabilities
* Adding specific capabilities when required
* Limiting container memory
* Limiting CPU usage
* Checking containers and images

## Files Included

* README.md
* Dockerfile
* script.sh
* Screenshots

## Commands Used

* mkdir "15_Security_Basics"
* cd "15_Security_Basics"
* nano Dockerfile
* nano 1script.sh
* docker build -t nonroot-user .
* docker run --rm nonroot-user
* docker run --rm --cap-drop=NET_ADMIN alpine:latest ip link add dummy0 type dummy
* docker run --rm --cap-add=NET_ADMIN alpine:latest ip link add dummy0 type dummy
* docker run --rm --memory="256m" --cpus="1" nonroot-user
* docker run -d --memory="256m" --cpus="1" nonroot-user
* docker ps
* docker ps -a

## Commands Output

* Running as user: newuser
* NET_ADMIN dropped successfully
* Network administration command was denied
* Container ran with NET_ADMIN capability
* Container ran with 256 MB memory limit
* Container ran with 1 CPU limit
* Docker containers were listed successfully

## What I Learned

* Docker containers normally run as root unless another user is configured.
* useradd creates a new user.
* USER switches the container to that user.
* --cap-drop removes specific Linux capabilities.
* --cap-add gives a container a specific capability.
* NET_ADMIN controls network administration operations.
* --memory limits container RAM usage.
* --cpus limits container CPU usage.
* --rm automatically removes a container after it stops.
* Resource limits help prevent resource exhaustion.
* Running containers with minimum required privileges improves security.

## Key Security Concepts

* Non-root containers
* Least privilege
* Linux capabilities
* Resource limits
* Container isolation
* Attack surface reduction


