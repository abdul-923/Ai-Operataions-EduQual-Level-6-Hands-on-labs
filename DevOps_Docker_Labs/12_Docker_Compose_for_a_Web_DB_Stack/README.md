

# Docker Compose for a Web + MySQL Stack

## Overview

A hands-on Docker Compose lab demonstrating how to deploy a simple Web + MySQL application stack using multiple Docker containers, environment variables, persistent volumes, service dependencies, and Docker Compose commands.

## Files Included

* docker-compose.yml
* README.md
* Screenshots

## Commands Used

* mkdir "12_Docker_Compose_for_a_Web_DB_Stack"
* cd "12_Docker_Compose_for_a_Web_DB_Stack"
* nano docker-compose.yml
* docker compose up
* docker compose up -d
* docker ps
* docker compose exec db mysql -u root -p
* SHOW DATABASES;
* exit
* docker compose down
* history
* nano README.md
* git add .
* git commit -m "Build Docker Lab Repo"
* git push origin main

## Output

* Docker Compose pulled the required images.
* Docker Compose created the default network.
* Docker Compose created the db_data volume.
* MySQL container started successfully.
* Nginx web container started successfully.
* docker ps confirmed the running containers.
* MySQL command-line monitor opened successfully.
* SHOW DATABASES; displayed information_schema, exampledb, mysql, performance_schema, and sys.
* docker compose down successfully removed the web and database containers.

## What I Learned

* Docker Compose can manage multiple containers as one application stack.
* Services can communicate within the Compose environment.
* depends_on controls service startup order.
* Environment variables can configure containerized applications.
* Docker volumes provide persistent database storage.
* docker compose exec allows commands to be executed inside a running service.
* docker compose up starts the application stack.
* docker compose down stops and removes the Compose containers.
* Docker Compose makes multi-container application management easier.

## Key Concepts

* Docker Compose
* Multi-container Applications
* Nginx
* MySQL
* Environment Variables
* Docker Volumes
* Persistent Storage
* Service Dependencies
* Container Networking
* Docker Compose CLI


