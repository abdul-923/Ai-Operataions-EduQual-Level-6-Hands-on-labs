
# Red Hat Lab 9 – Working with Network File Systems NFS & CIFS

## Overview

This lab focused on working with network file systems in Red Hat Linux. I learned how to connect RHEL to remote file shares using NFS and CIFS/SMB. I configured an Ubuntu system as an NFS server and accessed its shared folder from RHEL. I also tested CIFS/SMB connectivity between RHEL and Windows.

## Files Included

* README.md
* Screenshots

## Commands Used

### Install NFS and CIFS utilities

* sudo dnf update -y
* sudo dnf install -y nfs-utils cifs-utils
* rpm -q nfs-utils cifs-utils

### NFS Server on Ubuntu

* sudo apt install nfs-kernel-server
* sudo systemctl status nfs-kernel-server
* sudo systemctl start nfs-kernel-server
* sudo exportfs -v
* sudo showmount -e 192.168.8.128

### NFS Client on RHEL

* showmount -e 192.168.8.128
* sudo mkdir -p /mnt/nfs_share
* sudo mount -t nfs 192.168.8.128:/srv/nfs/share /mnt/nfs_share
* df -hT | grep nfs
* ls /mnt/nfs_share

### CIFS and Windows Connectivity

* ping 192.168.8.1
* Test-NetConnection 192.168.8.1 -Port 445
* Get-Service LanmanServer
* Get-NetTCPConnection -LocalPort 445 -State Listen
* ipconfig
* whoami
* smbclient -L //192.168.8.1 -U pc
* smbclient -L //192.168.8.1 -U core-i7-latest-pc

### CIFS Package

* sudo dnf install samba-client

## Output

* Installed NFS and CIFS utilities on RHEL.
* Configured an NFS share on Ubuntu.
* Successfully discovered the NFS export from RHEL.
* Successfully mounted the Ubuntu NFS share on RHEL.
* Verified the mounted NFS share and accessed its contents.
* Tested Windows SMB connectivity using port 445.
* Confirmed that the Windows Server service was running.
* Tested SMB authentication from RHEL.
* CIFS authentication was not completed because Windows rejected the supplied credentials.

## What I Learned

* NFS is commonly used for sharing files between Linux and Unix systems.
* CIFS/SMB is commonly used for file sharing between Windows and Linux.
* nfs-utils provides tools for working with NFS.
* cifs-utils provides tools for mounting and working with CIFS/SMB shares.
* An NFS server exports a directory so other systems can access it.
* RHEL can mount a remote NFS share as a local directory.
* Windows uses SMB and normally communicates through TCP port 445.
* Network connectivity and authentication are separate things.
* A system can successfully reach port 445 but still reject the SMB username or password.
* /etc/fstab can be used to configure network shares to mount automatically after reboot.

## Conclusion

In this lab I learned how Linux systems work with network file systems. I successfully configured and mounted an NFS share between Ubuntu and RHEL and tested CIFS/SMB connectivity between RHEL and Windows. This lab helped me understand how Linux can access remote storage from different operating systems.

## The Whole Lab in One Picture

Ubuntu → NFS Server → RHEL NFS Client → Mount Remote Share

Windows → SMB/CIFS Server → RHEL CIFS Client → Test Port 445 → Test Authentication
