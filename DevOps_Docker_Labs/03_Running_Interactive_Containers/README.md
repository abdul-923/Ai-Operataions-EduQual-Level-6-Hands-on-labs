

# 03 Running Interactive Container Commands

## Overview

* Practiced running Ubuntu containers in interactive mode.
* Interacted with a container through the terminal.
* Exited an interactive container session.
* Compared interactive and detached container modes.
* Ran a container in detached mode using sleep 100.
* Checked container status using Docker commands.

## Files Included

* README.md
* Screenshots

## Commands Used

* mkdir "03_Running_Interactive_Containers"
* cd "03_Running_Interactive_Containers"
* docker pull ubuntu
* docker images
* docker run -it ubuntu
* exit
* docker ps
* docker ps -a
* docker run -d ubuntu sleep 100

## Output

* Successfully downloaded the Ubuntu Docker image.
* Started an Ubuntu container in interactive mode.
* Accessed the Ubuntu container terminal and exited the session.
* Verified running and stopped containers using docker ps and docker ps -a.
* Started an Ubuntu container in detached mode with sleep 100.
* Verified the container remained running while the sleep process was active.

## What I Learned

* Interactive mode allows direct interaction with a container through the terminal.
* The -it option provides an interactive terminal session.
* Exiting the interactive shell stops the container when the shell is its main process.
* Detached mode runs a container in the background.
* The main process determines how long a container remains running.
* sleep 100 can keep a container running temporarily for testing.
* docker ps shows running containers.
* docker ps -a shows running and stopped containers.
