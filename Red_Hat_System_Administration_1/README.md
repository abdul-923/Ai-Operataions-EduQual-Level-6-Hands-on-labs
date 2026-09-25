
# Red Hat Lab 1 – Logging into RHEL and Using the Shell

## Overview

In this lab, I practiced logging into a Red Hat Enterprise Linux system and working with the Linux shell.

I practiced local console login, checked the SSH service, found the RHEL system IP address, and used SSH for remote access. I also practiced basic shell commands such as pwd, ls, man, history, clear, and exit.

Finally, I learned about the PS1 variable and how it can be used to customize the shell prompt.

## Files Included

* README.md
* Screenshots
* history.txt

## Commands Used

* pwd
* ls
* ls -l
* ls -a
* ls -lh
* man ls
* exit
* history
* clear
* whoami
* whoami
* sestatus
* sudo systemctl status sshd
* ip a
* ipconfig
* ipconfig -a
* ifconfig -a
* echo $PS1
* PS1=[\u@\h \W \t]$ 
* nano ~/.bashrc
* export PS1=[\u@\h \W \t]$ 

## SSH Commands

* sudo systemctl status sshd
* ip a
* ssh username@rhel-system-ip

Example:

* ssh user@192.168.1.100

## Output

* Successfully accessed the RHEL system through the local console.
* Verified that the SSH service was running.
* Identified the active network interface and IP address using ip a.
* Practiced connecting to the RHEL system through SSH.
* Successfully used basic Linux shell commands.
* Viewed the current working directory with pwd.
* Listed directory contents using ls and its common options.
* Accessed the manual page for the ls command.
* Checked the current SELinux status using sestatus.
* Viewed the command history.
* Practiced clearing and exiting the shell.
* Learned how to view and customize the PS1 shell prompt.

## What I Learned

* How to log in to a RHEL system locally.
* How SSH provides remote access to a Linux system.
* How to check whether the SSH service is running.
* How to find the IP address of a RHEL system.
* How to use basic Linux navigation commands.
* How to use man pages to get information about commands.
* How to check command history.
* How to check the SELinux status.
* How the PS1 variable controls the appearance of the shell prompt.
* How to temporarily and permanently customize the shell prompt.

## Conclusion

This lab gave me practical experience with the RHEL command line and basic system access.

I learned how to work with the shell, check SSH and network information, use basic Linux commands, and customize the command prompt. These are important foundational skills for Linux system administration, DevOps, and AI Operations.

## The Whole Lab in One Picture

RHEL Login → SSH Service → Find IP Address → Remote SSH → Basic Shell Commands → pwd → ls → man → history → clear → exit → PS1 Customization

This lab helped me understand the basic workflow of accessing and working with a Red Hat Enterprise Linux system from the command line.
