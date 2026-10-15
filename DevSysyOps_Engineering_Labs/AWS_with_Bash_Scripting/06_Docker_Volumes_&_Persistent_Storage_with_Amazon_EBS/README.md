
# Lab 6 – Docker Volumes and Persistent Storage with Amazon EBS

## Overview

In this lab I learned how to use Amazon EBS as persistent storage for a Docker container. I created an EC2 Ubuntu instance and attached a separate EBS volume to it. I formatted and mounted the EBS volume on the EC2 instance. I then connected the EBS storage to an Nginx Docker container.

The website files were stored on the EBS volume instead of inside the Docker container.

This means the container can be deleted and recreated while the data remains available on the EBS volume.

## Files Included

- README.md
* Screenshots
* Commands History

## Commands Used

### SSH into EC2

ssh -i ./lab7.pem ubuntu@YOUR_EC2_PUBLIC_IP

### Check Storage Devices

lsblk

### Format the EBS Volume

sudo mkfs -t ext4 /dev/nvme1n1

### Create Mount Point

sudo mkdir /docker-lab

### Mount EBS Volume

sudo mount /dev/nvme1n1 /docker-lab

### Check Mounted Storage

df -h /docker-lab

### Install Docker

sudo apt update

sudo apt install -y docker.io

sudo systemctl enable --now docker

### Check Docker Version

sudo docker --version

### Create Nginx Data Directory

sudo mkdir /docker-lab/nginx-data

### Run Nginx Container

sudo docker run -d --name nginx-ebs -p 80:80 -v /docker-lab/nginx-data:/usr/share/nginx/html nginx

### Create Test Web Page

echo "<h1>Hello from Nginx with AWS EBS Storage</h1>" | sudo tee /docker-lab/nginx-data/index.html

### Test Nginx

curl http://localhost

## Output

The EBS volume was successfully attached to the EC2 instance.

The volume was formatted with the ext4 filesystem.

The EBS volume was mounted at /docker-lab.

Docker was installed successfully.

An Nginx container was created and started.

The EBS backed directory was mounted to the Nginx website directory.

The test HTML file was successfully stored on the EBS volume.

The Nginx page was successfully accessed using localhost.

## What I Learned

- I learned what Amazon EBS is.
- I learned how to attach an EBS volume to an EC2 instance.
- I learned what a device name means in Linux.
- I learned how to identify storage devices using lsblk.
- I learned how to format an EBS volume with ext4.
- I learned what a mount point is.
- I learned how to mount an EBS volume on an EC2 instance.
- I learned how Docker volumes can provide persistent storage.
- I learned how to mount an EC2 directory into a Docker container.
- I learned how Nginx uses the mounted directory for website files.
- I learned that Docker containers are temporary while EBS storage can persist.
- I learned that deleting a Docker container does not delete data stored on the EBS volume.

## The Whole Lab in One Picture

AWS EBS Volume

↓

Attach to EC2

↓

Linux Device

↓

Format with ext4

↓

Mount at /docker-lab

↓

Docker Container

↓

Nginx

↓

Website Files Stored on EBS

## Conclusion

In this lab I successfully connected Amazon EBS storage to a Docker container running on an EC2 Ubuntu instance.

The Nginx container used the EBS backed directory for its website files.

This demonstrated how persistent storage can be used with Docker so that application data remains available even when the container is removed or recreated.
