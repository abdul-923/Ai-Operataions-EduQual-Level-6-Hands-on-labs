
# Lab 8 – Listing Docker Containers and Images with Bash Scripting

## Overview

In this lab I learned how to use Bash scripting with Docker commands.

I created a Bash script that checks for available Docker containers and Docker images.

The script displays the available containers and images.

If no containers or images are available the script displays an appropriate message.

I also learned how to use variables and if else conditions in Bash.

## Files Included

- lab.sh
- README.md
- Screenshots

## Commands Used

### Check Docker Containers

docker ps -a

### Check Docker Images

docker images -a

### Make the Script Executable

chmod +x lab.sh

### Run the Bash Script

./lab.sh

## Bash Concepts Used

### Shebang

#!/bin/bash

This tells the system to use Bash to execute the script.

### Variables

containers=$(docker ps -a --format "{{.Names}}")

images=$(docker images --format "{{.Repository}}:{{.Tag}}")

### Check If a Variable Is Empty

if [ -z "$containers" ]; then

### Conditional Statements

if [ -z "$images" ]; then

else

fi

### Print Output

echo "Listing Available Containers"

echo "Listing Available Images"

## Output

The script successfully listed the available Docker containers.

The script displayed the container name and full container information.

The script successfully listed the available Docker images.

The script displayed the image name and full image information.

The script also checks whether containers or images are available.

## Troubleshooting

### Permission Denied

The script initially returned a permission denied error.

This was fixed by making the script executable.

chmod +x lab.sh

### Docker Container Format Error

The container formatter uses:

{{.Names}}

This returns the container names.

### Docker Image Format Error

Docker images do not use {{.Names}} or {{.IMAGE}}.

The image repository and tag can be displayed using:

{{.Repository}}:{{.Tag}}

## What I Learned

- I learned how to create a Bash script.
- I learned why the Bash shebang is required.
- I learned how to use echo in Bash.
- I learned how to store command output in a variable.
- I learned how to use Docker commands inside a Bash script.
- I learned how to list all Docker containers using docker ps -a.
- I learned how to list Docker images using docker images -a.
- I learned how to check whether a variable is empty.
- I learned how to use if else conditions in Bash.
- I learned the difference between Docker container format fields and Docker image format fields.
- I learned how to make a Bash script executable.
- I learned how Bash can be used to automate Docker operations.



## Conclusion

In this lab I successfully created a Bash script to check and display Docker containers and Docker images.

This lab helped me understand how Bash can work together with Docker commands to automate basic Docker operations.

I also practiced Bash variables and conditional statements which are important for creating more useful automation scripts.
