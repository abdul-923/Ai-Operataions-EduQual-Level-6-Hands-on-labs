
# Red Hat Lab 3 – Monitoring and Managing Processes

## Overview

In this lab I practiced monitoring and managing processes in Red Hat Enterprise Linux.

I used commands to view running processes and system resource usage. I also practiced finding specific processes and terminating them. I worked with background and foreground jobs and learned how to stop and resume processes. 

## Files Included

* README.md
* Screenshots


## Commands Used

* mkdir "03_Monitoring_&_Managing_Processes"
* cd "03_Monitoring_&_Managing_Processes"
* ps aux
* ps aux | grep nginx
* top
* htop
* sudo dnf install -y htop
* ps aux | grep firefox
* pkill firefox
* jobs
* sleep 300 &
* fg %1
* Ctrl + Z
* bg %1
* nice
* renice

## Output

* Created the lab directory for process management.
* Viewed running processes using ps aux.
* Searched for specific processes using grep.
* Checked for nginx processes.
* Used top to monitor system processes and resource usage.
* Tried to install and use htop for interactive process monitoring.
* Found Firefox processes using ps aux and grep.
* Terminated Firefox processes using pkill.
* Created a background job using sleep 300 &.
* Checked running jobs using jobs.
* Brought a background job to the foreground using fg %1.
* Stopped the foreground job using Ctrl + Z.
* Resumed the stopped job in the background using bg %1.
* Practiced changing process priority using nice and renice.

## What I Learned

* I learned how to view running processes in RHEL.
* I learned how to monitor processes using ps.
* I learned how to monitor system activity using top.
* I learned about htop as an interactive process monitoring tool.
* I learned how to search for a specific process.
* I learned how to terminate processes using pkill.
* I learned how background jobs work in Linux.
* I learned how to check active jobs using jobs.
* I learned how to move a job to the foreground using fg.
* I learned how to stop a running foreground job using Ctrl + Z.
* I learned how to resume a stopped job using bg.
* I learned how to control processes from the command line.
* I learned how process priority works in Linux.
* I learned how nice can be used to start a process with a different priority.
* I learned how renice can be used to change the priority of an existing process.

## Conclusion

This lab gave me practical experience with monitoring and managing processes in Red Hat Enterprise Linux.

I learned how to view processes and system activity and how to search for and terminate processes. I also practiced managing background and foreground jobs and changing process priority.

These commands are important for Linux system administration troubleshooting and process management.

## The Whole Lab in One Picture

View Processes → Monitor System → Find Processes → Terminate Processes → Create Background Job → Check Jobs → Bring Job to Foreground → Stop Job → Resume Job → Adjust Process Priority
