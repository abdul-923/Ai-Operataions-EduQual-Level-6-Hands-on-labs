
# Docker Lab 10 — Creating a Custom Networking Bridge

## Overview

This lab demonstrates how to create a **user-defined bridge network** in Docker and connect multiple containers to it.

The lab uses two Nginx containers connected to the same custom network and verifies that one container can communicate with the other using its **container name**.

## Files Included

* README.md
* Screenshots 


## Commands Used

* mkdir "10_Creating_a_Custom_Networking-Bridge"
* cd "10_Creating_a_Custom_Networking-Bridge"
* docker network create mynet
* docker run -d --name container1 --network mynet nginx
* docker run -d --name container2 --network mynet nginx
* docker exec -it container1 /bin/bash
* curl [http://container2](http://container2)
* docker ps -a
* docker stop container2
* docker stop nginx-volume
* docker rm -f $(docker ps -aq)
* docker images -a
* docker rmi -f $(docker images -aq)


## Output

* Custom network mynet was successfully created.
* Nginx image was pulled successfully when it was not available locally.
* container1 was successfully connected to mynet.
* container2 was successfully connected to mynet.
* curl [http://container2](http://container2) successfully reached the second container.
* Nginx returned its default HTML page.
* Container-to-container communication was successfully verified.

## What I Learned

* A Docker bridge network is a **virtual network that connects containers**.
* A user-defined bridge network gives better control over which containers communicate.
* Containers on the same user-defined network can communicate with each other.
* Docker provides automatic DNS-based name resolution on user-defined networks.
* Instead of using an IP address, container1 can access container2 using its name.
* Example: container1 → container2.
* The container name works as the hostname inside the Docker network.
* Containers on separate networks are isolated from each other unless explicitly connected.

## Key Concepts

* **Docker Network** — Provides networking between containers.
* **Bridge Network** — A virtual network used to connect Docker containers.
* **User-Defined Bridge** — A custom bridge network created and controlled by the user.
* **Container Name Resolution** — Docker allows containers to find each other using names.
* **Network Isolation** — Containers on different networks are separated by default.
* **Nginx** — Used in this lab as the web server inside the containers.
* **curl** — Used to test HTTP communication between containers.


