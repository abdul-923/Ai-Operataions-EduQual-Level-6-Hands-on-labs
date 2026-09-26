# Red Hat Lab 6 – Analyzing and Storing Logs

## Overview

In this lab I practiced working with system logs in Red Hat Enterprise Linux.

I explored log files in /var/log and used journalctl to view and filter system logs. I also practiced logrotate for automatic log management and used grep and awk to search and analyze log information.

## Files Included

* README.md
* Screenshots
* Command history
* Log configuration files

## Commands Used

* ls -l /var/log
* sudo cat /var/log/messages
* sudo cat /var/log/secure
* sudo journalctl
* sudo journalctl --since "2023-01-01" --until "2023-01-02"
* sudo journalctl -u sshd
* sudo journalctl -f
* ls /etc/logrotate.d/
* cat /etc/logrotate.conf
* sudo nano /etc/logrotate.d/mylogs
* sudo logrotate -d /etc/logrotate.conf
* sudo grep "error" /var/log/messages
* sudo grep -i "fail" /var/log/secure
* sudo grep -c "authentication failure" /var/log/secure
* sudo awk '/Failed password/ {print $1 $2 $3 $9 $11}' /var/log/secure
* sudo journalctl --disk-usage

## Output

* Explored system log files in /var/log
* Viewed system messages and authentication logs
* Viewed the system journal using journalctl
* Filtered journal logs by date
* Filtered logs by service
* Followed logs in real time
* Explored logrotate configuration
* Created a test log rotation configuration
* Tested log rotation settings
* Searched logs using grep
* Used awk to analyze log information
* Checked journal disk usage

## What I Learned

* How system logs are stored in RHEL
* How to use journalctl to read system logs
* How to filter logs by time and service
* How to follow logs in real time
* How logrotate manages log files automatically
* How grep can search specific information in logs
* How awk can extract useful information from log files
* How logs can help with troubleshooting and system monitoring

## Conclusion

This lab gave me practical experience with Linux log management and analysis.

I learned how to locate system logs and use journalctl logrotate grep and awk to manage and analyze log information.

## The Whole Lab in One Picture

Explore Logs → View Journal → Filter Logs → Monitor Logs → Configure Logrotate → Test Rotation → Search Logs → Analyze Logs → Check Journal Usage
