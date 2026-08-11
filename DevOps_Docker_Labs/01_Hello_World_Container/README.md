

# Lab 01 — Docker Hello World Container

## Overview

This lab introduced the fundamentals of Docker by installing Docker on Ubuntu, configuring Docker permissions, verifying the Docker service, pulling the Hello World image from Docker Hub, and running the first Docker container.

## Files Included

* README.md 
* Screenshots 

## Commands Used

* docker.io --version
* docker --version
* sudo apt install docker.io
* docker images
* sudo usermod -aG docker $USER
* sudo apt install util-linux-extra
* newgrp docker
* docker ps
* docker pull hello-world
* docker run hello-world
* docker search ubuntu
* systemctl status docker

## Output

* Docker version 29.1.3 installed successfully.
* Docker service showed Active: active (running).
* hello-world image was successfully pulled from Docker Hub.
* Hello from Docker! message was displayed successfully.
* First Docker container executed successfully.

## Key Concepts Learned

* Docker Images
* Docker Containers
* Docker Hub
* Docker Daemon
* Docker CLI
* Docker Groups and Permissions
* Docker Service Management
* Image Pulling and Container Execution

## What I Learned

* How to install and verify Docker on Ubuntu.
* How to configure Docker permissions.
* How to search and pull images from Docker Hub.
* How to create and run a Docker container.
* How to check the Docker service status.
