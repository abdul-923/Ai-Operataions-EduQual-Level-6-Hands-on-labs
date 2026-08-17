# Docker Logs and Debugging

## Overview

This lab focuses on managing and troubleshooting Docker containers using container status, logs, interactive shell access, filesystem inspection, environment variables, and container lifecycle commands.

## Files Included

* README.md
* Screenshots

## Lab Objectives

* Run and manage Docker containers
* Check running and stopped containers
* Access a running container interactively
* Inspect container filesystem usage
* Check container environment variables
* View and follow Docker container logs
* Stop containers and verify their status
* Inspect Docker images

## Commands Used

* docker run -d nginx
* docker run -it nginx /bin/bash
* docker ps
* docker exec -it 66b03c3c832c /bin/bash
* df -h
* whoami
* env
* exit
* docker logs -f nginx
* docker logs -f 66b03c3c832c
* docker stop 66b03c3c832c
* docker ps -a
* docker images -a

## Script Workflow

* Started an Nginx container in detached mode
* Verified the running container with docker ps
* Entered the container using an interactive Bash shell
* Checked disk usage with df -h
* Checked the current container user with whoami
* Viewed container environment variables with env
* Exited the container shell
* Viewed Nginx container logs
* Followed live container logs
* Stopped the running container
* Verified the stopped container with docker ps -a
* Listed available Docker images with docker images -a

## Output

* Nginx container started successfully
* Container appeared as Up in docker ps
* Interactive shell opened successfully
* Container filesystem showed approximately 98G total, 16G used, and 78G available
* Container environment variables were displayed
* Nginx startup and runtime logs were displayed
* Container logs showed Nginx worker processes and signals
* Container stopped successfully with exit code 0
* docker ps -a displayed the stopped Nginx containers
* Docker images included nginx, alpine, and mysql images

## What I Learned

* How to check running Docker containers
* How to inspect stopped containers
* How to enter a running container
* How to inspect disk usage inside a container
* How to view container environment variables
* How to read Docker logs
* How to follow logs in real time
* How to stop and verify containers
* How to inspect locally available Docker images

## Key Concepts

* Docker Containers
* Docker Images
* Container Logs
* Docker Debugging
* Interactive Containers
* Container Filesystems
* Environment Variables
* Container Lifecycle
* Nginx
* Docker CLI


