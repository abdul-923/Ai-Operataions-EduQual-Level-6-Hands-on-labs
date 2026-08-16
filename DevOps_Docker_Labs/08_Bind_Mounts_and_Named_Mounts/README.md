
# Docker Bind Mounts and Named Volumes

## Overview

This lab demonstrates two common Docker storage methods:

* Bind mounts — connecting a specific host directory to a container directory.
* Named volumes — creating a Docker-managed volume and attaching it to a container.
* Verifying data access through Nginx.
* Copying files from the host into a container.
* Accessing container data through mapped ports.

## Files Included

* README.md
* Screenshots of commands and outputs

## Lab Objectives

* Understand bind mounts.
* Understand named volumes.
* Connect host storage to Docker containers.
* Serve host files through Nginx.
* Create and use a Docker named volume.
* Copy files from the host into a container.
* Verify the stored files through Nginx.

## Commands Used

* cd ..
* mkdir "08_Bind_Mounts_and_Named_Mounts"
* cd "08_Bind_Mounts_and_Named_Mounts"
* mkdir ~/host-directory
* echo "Hello from the Linux!" > ~/host-directory/host-file.txt
* docker run -d --name nginx-bind -v ~/host-directory:/usr/share/nginx/html:ro -p 8080:80 nginx
* docker ps
* docker images
* docker status
* docker --help
* curl [http://localhost:8080/host-file.txt](http://localhost:8080/host-file.txt)
* sudo snap install curl
* curl [http://localhost:8080/host-file.txt](http://localhost:8080/host-file.txt)
* docker volume create my-volume
* docker volumes
* docker volume
* docker inspect volume
* docker inspect volumes
* docker run -d --name nginx-volume -v my-volume:/usr/share/nginx/html -p 8081:80 nginx
* docker cp ~/host-directory/host-file.txt nginx-volume:/usr/share/nginx/html/
* curl [http://localhost:8081/host-file.txt](http://localhost:8081/host-file.txt)
* history

## Script Workflow

* Created a host directory named host-directory.
* Created host-file.txt inside the directory.
* Started an Nginx container using a bind mount.
* Connected the host directory to Nginx's HTML directory.
* Mapped host port 8080 to Nginx port 80.
* Tested the file using curl.
* Created a Docker named volume called my-volume.
* Started another Nginx container using the named volume.
* Copied host-file.txt into the container.
* Mapped port 8081 to Nginx port 80.
* Tested access to the copied file using curl.

## Output

* Nginx bind-mount container started successfully.
* docker ps displayed the nginx-bind container with port mapping 8080 → 80.
* The host file was created successfully.
* curl was installed successfully using Snap.
* Docker created the my-volume named volume successfully.
* The nginx-volume container started successfully.
* docker cp successfully copied 2.05kB to the Nginx container.
* Port 8081 was used to access the Nginx container with the named volume.
* Command history was recorded using history.

## What I Learned

* A bind mount connects an existing host directory directly to a container directory.
* A named volume is created and managed by Docker.
* The same volume can be attached to different containers.
* Nginx can serve files stored through a bind mount or named volume.
* Docker port mapping connects a host port to a container port.
* docker cp can copy files between the host and a container.
* Data storage can be separated from the container itself.

## Key Concepts

* Bind Mount
* Named Volume
* Docker Volume
* Nginx
* Port Mapping
* Container Storage
* Data Persistence
* docker cp
* curl

## The Whole Lab in One Picture

Host Directory → Bind Mount → Nginx Container → Port 8080 → curl

Docker Named Volume → Nginx Container → Port 8081 → curl

**Main idea:** Containers can use storage from the host through bind mounts or use Docker-managed storage through named volumes.
