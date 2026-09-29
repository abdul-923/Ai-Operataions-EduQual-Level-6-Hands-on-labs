
# Lab 01 – Setting Up an AWS EC2 Instance for Docker

## Overview

In this lab I created an AWS EC2 instance and connected to it from my local Ubuntu system using SSH. I configured the private key permissions and successfully accessed the Ubuntu EC2 instance. I practiced basic Linux system administration commands and checked the system resources network configuration running processes and internet connectivity. The instance was prepared as a Linux environment for future Docker and DevOps work.

## What I Learned

* How to connect to an AWS EC2 instance using SSH
* How to protect an AWS private key using chmod
* How to identify the operating system
* How to check CPU resources
* How to check memory usage
* How to check disk usage
* How to check the hostname
* How to check the current user
* How to inspect network interfaces
* How to test internet connectivity
* How to view running processes
* How to monitor system resources using top
* How to update Ubuntu packages
* How to upgrade installed packages
* How to safely shut down an EC2 instance
* How to troubleshoot basic Linux command errors

## Files Included

* README.md
* Screenshots
* commands_history.txt

## Commands Used

* chmod 400 my-test-aws.pem
* ssh -i my-test-aws.pem [ubuntu@ec2-44-214-180-16.compute-1.amazonaws.com](mailto:ubuntu@ec2-44-214-180-16.compute-1.amazonaws.com)
* hostname -I
* sudo apt-get update
* sudo apt-get upgrade -y
* nproc
* free -h
* df -f
* df --help
* df -l
* whoami
* hostname
* ip addr
* ifconfig
* ping -c 4 google.com
* ps aux
* top
* sudo shutdown -h now

## Output

The AWS EC2 instance was successfully accessed through SSH from the local Ubuntu system.

The instance was running Ubuntu 26.04 LTS.

The system detected 2 CPU cores.

The instance had approximately 908 MiB of memory.

The root filesystem had approximately 6.6 GB of storage.

The logged in user was ubuntu.

The hostname was ip-172-31-1-30.

The private IP address was 172.31.1.30.

The network interface ens5 was active.

Internet connectivity was successfully tested using Google.

The ping test returned 4 packets transmitted and 4 packets received with 0% packet loss.

The running processes were inspected using ps aux and top.

The Ubuntu package repositories were successfully updated using apt-get update.

The system was successfully upgraded using apt-get upgrade -y.

The private key permission issue was identified and fixed using chmod 400.

The EC2 instance was successfully shut down using sudo shutdown -h now.


## The Whole Lab in One Picture

AWS Console → Create EC2 instance → Select Ubuntu → Create and download PEM key → Launch instance → Get the public IP or DNS → Connect from local Ubuntu using SSH → Fix PEM permissions using chmod 400 → Successfully access the EC2 Ubuntu server → Update the system → Check CPU and memory → Check disk storage → Check user and hostname → Check network configuration → Test internet connectivity → Monitor running processes → Shut down the instance

## Conclusion

This lab provided practical experience with AWS EC2 and Linux system administration. The EC2 instance is now ready to be used for future Docker and DevOps hands-on labs.
