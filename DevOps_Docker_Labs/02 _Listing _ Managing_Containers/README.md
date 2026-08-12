

# Lab 2: Listing & Managing Docker Containers

## Overview

* Practiced basic Docker container lifecycle management.
* Pulled the Nginx image from Docker Hub.
* Created and ran Nginx containers.
* Listed running and stopped containers.
* Stopped, started, and removed containers.
* Checked available Docker images.

## Files Included

* README.md
* Screenshots

## Commands Used

* cd ..
* ls
* mkdir "Listing _ Managing_Containers"
* docker pull nginx
* docker run nginx
* docker run -d nginx
* docker ps
* docker stop nginx
* docker stop c61d4d95bb24
* docker start nginx
* docker images
* docker run -d --name Dnginx nginx
* docker stop Dnginx
* docker start Dnginx
* docker images -a
* docker ps -a
* docker rm Dnginx

## Output

* Successfully downloaded the Nginx Docker image.
* Created and ran Nginx containers.
* Verified running containers using docker ps.
* Stopped and restarted containers successfully.
* Verified stopped containers using docker ps -a.
* Removed the Dnginx container successfully.
* Verified the remaining Docker images using docker images.

## What I Learned

* Docker images are templates used to create containers.
* Containers are running instances created from images.
* docker ps shows running containers.
* docker ps -a shows running and stopped containers.
* docker stop stops a container without deleting it.
* docker start starts an existing stopped container.
* docker rm permanently removes a container.
* Container names and image names are different.
* A container can be given a custom name using --name.
* Docker container lifecycle: Create → Run → Stop → Start → Remove.

## Key Concepts

* Docker Image
* Docker Container
* Container ID
* Container Name
* Running Container
* Stopped Container
* Container Lifecycle
* Nginx

## The Whole Lab in One Picture

* Pull image → Create container → Run container → List containers → Stop container → Start container → Remove container
