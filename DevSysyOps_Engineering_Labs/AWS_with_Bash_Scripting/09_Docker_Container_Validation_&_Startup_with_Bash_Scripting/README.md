
# Lab 9 – Docker Container Validation and Startup with Bash Scripting

## Overview

In this lab I learned how to create a Bash script that works with Docker containers.

The script asks the user for a container name.

It checks whether the container is available.

If the container exists the script starts it.

If the container does not exist the script pulls the Docker image and creates a new container.

## Files Included

- lab.sh
- README.md

## Commands Used

- vim lab.sh
- chmod +x lab.sh
- ./lab.sh
- docker ps -a
- docker pull nginx
- docker run -d --name nginx -p 8080:80 nginx
- docker start nginx

## Output

- The script asks the user to enter a container name.
- The script checks whether the container exists.
- An existing container is started successfully.
- If the container does not exist the required Docker image is pulled.
- A new Docker container is created and started.
- Available containers can be viewed using docker ps -a.

## What I Learned

- I learned how to use Bash with Docker commands.
- I learned how to take user input using Bash.
- I learned how to use variables in Bash.
- I learned how to use if else conditions.
- I learned how to check whether a Docker container exists.
- I learned how to start an existing Docker container.
- I learned how to pull a Docker image when it is not available.
- I learned how to create and run a new Docker container.
- I learned how to use grep inside a Bash script.
- I learned how Bash can automate Docker container management.

## Conclusion

In this lab I successfully created a Bash script that checks for a Docker container and starts it when available.

If the container does not exist the script pulls the required image and creates a new container.

This lab helped me understand how Bash scripting can be used to automate Docker operations.
