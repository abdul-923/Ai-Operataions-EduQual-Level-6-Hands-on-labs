

# Docker Volumes Lab

## Lab Title

Docker Volumes – Persistent Data Storage

## Overview

* Created a named Docker volume called myvolume.
* Attached the volume to a container at /data.
* Created a file inside the container and stored it in the volume.
* Verified that the file remained available after removing the container.
* Located the volume data directly on the host filesystem.

## Files Included

* README.md
* Screenshots

## Commands Used

* mkdir "07_Docker_Volumes"
* cd "07_Docker_Volumes"
* docker volume create myvolume
* ls
* docker volume inspect myvolume
* docker run --name volcontainer -v myvolume:/data -d alpine sh -c "echo 'Hello World' > /data/hello.txt"
* docker run --rm -v myvolume:/data alpine cat /data/hello.txt
* docker rm -f volcontainer
* docker ps
* cd /var/lib/docker/volumes
* ls
* cd myvolume
* ls
* cd _data
* ls
* cat hello.txt

## Output

* Docker volume myvolume was successfully created.
* Docker reported the volume mountpoint as /var/lib/docker/volumes/myvolume/_data.
* The Alpine container created hello.txt inside /data.
* The file contained: Hello World
* The file was successfully read after using a temporary container.
* The original container was removed successfully.
* The hello.txt file was still present inside the Docker volume.
* The same Hello World content was verified directly from the host filesystem.

## What I Learned

* A Docker volume provides persistent storage for container data.
* myvolume is managed by Docker and stored physically on the host disk.
* -v myvolume:/data connects the Docker volume to /data inside the container.
* Files written to /data are stored in the volume.
* Deleting the container does not delete the volume or its data.
* The same volume can be attached to another container to access the same data.
* Docker volume inspect shows the physical Mountpoint of a volume.
* Docker-managed volume data can be accessed from the host with appropriate root permissions.
* cd cannot be used with sudo because cd is a shell built-in; a root shell can be opened with sudo -i.
* docker containers is not a valid Docker command; docker ps is used to list running containers.
