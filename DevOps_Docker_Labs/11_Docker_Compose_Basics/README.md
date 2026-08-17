
# Docker Compose Basics

## Overview

A hands-on Docker lab demonstrating how Docker Compose is used to define and manage multiple containers from a single Compose file.

## Files Included

* Screenshots
* README
* docker-compose.yml

## Lab Objectives

* Learn Docker Compose basics
* Create a Docker Compose YAML file
* Define multiple services
* Run Nginx and Alpine containers
* Configure port mapping
* Start multiple containers together
* Run containers in detached mode
* Check container status
* Stop Docker containers

## Commands Used

* docker compose --version
* docker compose version
* clear
* ls
* mkdir "11_Docker_Compose_Basics"
* cd "11_Docker_Compose_Basics"
* nano docker-compose.yml
* docker-compose up
* docker --version
* docker-compose version
* docker compose up
* docker ps -a
* docker ps
* docker compose up -d
* docker stop 11e9788a9047
* history

## Output

* Docker Compose version v5.4.0
* Docker Compose successfully started 2 services
* web-1 started successfully
* app-1 started successfully
* Nginx container published port 8080
* Nginx web server accessed through localhost:8080
* Running containers verified
* Stopped containers verified
* Docker container successfully stopped

## What I Learned

* Docker Compose manages multiple containers together
* Docker Compose uses a YAML configuration file
* Multiple services can be defined in one Compose file
* Port mapping connects the host port to the container port
* docker compose up starts the services
* docker compose up -d runs services in the background
* docker ps shows running containers
* docker ps -a shows all containers
* Docker Compose simplifies multi-container application management

## Key Concepts

* Docker Compose
* YAML
* Services
* Nginx
* Alpine
* Port Mapping
* Multi-Container Applications
* Detached Mode
* Container Management

## The Whole Lab in One Picture

Docker Compose File → Multiple Services → Web + App Containers → Port Mapping → Running Application
