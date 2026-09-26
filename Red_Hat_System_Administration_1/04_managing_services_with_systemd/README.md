# Red Hat Lab 4 – Managing Services with systemd

## Overview

In this lab I practiced managing services in Red Hat Enterprise Linux using systemctl.

I learned how to view running services and check the status of individual services. I practiced starting and stopping services and enabling or disabling services at boot. I also inspected service unit files and checked service dependencies.

Finally I used journalctl to view service logs and monitor logs in real time.

## Files Included

* README.md
* Screenshots
* history.txt

## Commands Used

* systemctl list-units --type=service --state=running
* systemctl status sshd
* systemctl status ubuntu
* systemctl status rhsm
* systemctl stop sshd
* systemctl start sshd
* systemctl disable sshd
* systemctl enable sshd
* systemctl cat sshd
* systemctl list-dependencies sshd
* journalctl -u sshd
* journalctl -u sshd --since "1 hour ago"
* journalctl -u sshd -f

## Output

* Listed running services on the RHEL system.
* Checked the status of the sshd service.
* Checked the status of the rhsm service.
* Verified that ubuntu.service was not available on the RHEL system.
* Stopped the sshd service.
* Verified that the sshd service became inactive.
* Started the sshd service again.
* Disabled sshd from starting automatically at boot.
* Enabled sshd to start automatically at boot.
* Inspected the sshd service unit file.
* Viewed the configuration of the sshd service.
* Checked the dependencies of the sshd service.
* Viewed sshd service logs using journalctl.
* Filtered sshd logs by time.
* Followed sshd logs in real time.

## What I Learned

* I learned how systemd manages services in RHEL.
* I learned how to list currently running services.
* I learned how to check the status of a service.
* I learned how to start a service.
* I learned how to stop a service.
* I learned how to enable a service at boot.
* I learned how to disable a service at boot.
* I learned the difference between starting and enabling a service.
* I learned how to inspect service unit files.
* I learned how to check service dependencies.
* I learned how systemd stores service configuration.
* I learned how to view service logs using journalctl.
* I learned how to filter logs based on time.
* I learned how to monitor new log entries in real time.
* I learned how to use systemd for basic service administration and troubleshooting.

## Conclusion

This lab gave me practical experience with managing services in Red Hat Enterprise Linux using systemd.

I learned how to control services check their status configure their startup behavior inspect their configuration and monitor their logs.

These skills are important for Linux system administration service management and troubleshooting.

## The Whole Lab in One Picture

List Services → Check Service Status → Start Service → Stop Service → Enable Service → Disable Service → Inspect Unit File → Check Dependencies → View Logs → Filter Logs by Time → Follow Logs in Real Time
