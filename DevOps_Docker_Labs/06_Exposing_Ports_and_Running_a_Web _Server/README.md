
# Lab 10: Exposing Ports and Running a Web Server

## Overview

This lab demonstrates how to run an Nginx web server inside a Docker container and expose it through a host port.

## Files Included

* README.md
* Screenshots of commands and lab work

## Commands Run

* mkdir "06_Exposing_Ports_and_Running_a_Web_Server"
* cd "06_Exposing_Ports_and_Running_a_Web_Server"
* docker pull nginx
* docker images
* docker ps
* docker run -d -p 8080:80 nginx
* docker ps

## What I Learned

* How to pull an Nginx Docker image.
* How to run Nginx inside a container.
* How Docker port mapping works.
* How host port 8080 connects to container port 80.
* How to verify a running container using docker ps.
* How to access the Nginx web server through the browser.
