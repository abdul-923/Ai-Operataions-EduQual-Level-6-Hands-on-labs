
# Docker Networking Lab

## Overview

This lab covers the basics of Docker container networking and demonstrates how Docker containers communicate through Docker networks.

The lab includes creating and running containers, checking container networking information, observing container status, and cleaning up Docker resources.

## Files Included

* README.md
* Screenshots

## Commands Used

* mkdir "09_Docker_Networking"
* cd "09_Docker_Networking"
* docker run -d --name container2 ubuntu
* docker run -d --name container3 ubuntu sleep 1000
* docker ps
* docker ps -a
* docker images
* docker stop container3
* docker stop container2
* docker rm -f $(docker ps -aq)
* docker rmi -f $(docker images -q)

## Output

* Ubuntu containers were successfully created.
* container2 was started with the Ubuntu image.
* container3 was started with Ubuntu and kept running using sleep 1000.
* docker ps displayed the active containers.
* docker ps -a displayed both running and stopped containers.
* Docker images were successfully listed.
* Containers were successfully stopped and removed.
* Unused Docker images were successfully removed.
* Final docker ps -a showed no containers remaining.

## What I Learned

* Docker containers have their own network environment.
* Docker automatically provides networking to containers.
* Containers can communicate through Docker networks.
* Docker networking provides isolation between different networks.
* docker ps shows running containers, while docker ps -a shows all containers.
* Container networking is separate from the physical network configuration of the Linux host.
* Docker uses network drivers such as bridge to provide container connectivity. ([Docker Documentation][1])
* User-defined bridge networks allow containers to communicate using container names and provide better isolation. ([Docker Documentation][1])
* Docker port publishing can connect a host port to a container port using the -p option. ([Docker Documentation][2])

## Key Concepts

* Container Networking
* Docker Bridge Network
* Container IP Address
* Network Isolation
* Container-to-Container Communication
* Port Mapping
* Docker Network Drivers
* Container Lifecycle


