
# Red Hat Lab – Using Red Hat Customer Portal and Cockpit

## Overview

This lab focused on using the Red Hat Customer Portal and Cockpit for RHEL system administration. The lab covered accessing Red Hat support resources creating support cases installing and configuring Cockpit and managing the RHEL system through a web based interface.

## Files Included

* README.md
* Screenshots
* history.txt

## Commands Used

* sudo dnf install cockpit
* sudo dnf install cockpit cockpit-podman -y
* sudo systemctl enable --now cockpit.socket
* systemctl status cockpit.socket
* sudo firewall-cmd --add-service=cockpit --permanent
* sudo firewall-cmd --reload
* sudo ss -tulnp | grep 9090
* [https://access.redhat.com](https://access.redhat.com)
* [https://192.168.8.131:9090](https://192.168.8.131:9090)

## Output

* Accessed the Red Hat Customer Portal
* Reviewed Red Hat knowledgebase resources
* Installed Cockpit on RHEL
* Enabled and started cockpit.socket
* Verified that Cockpit was listening on port 9090
* Configured the firewall to allow Cockpit
* Accessed the Cockpit web interface
* Viewed system overview and resource usage
* Explored system logs
* Reviewed networking and system information
* Explored Podman container management

## What I Learned

* The Red Hat Customer Portal provides documentation support resources and support case management.
* Cockpit is a web based administration tool for managing Linux systems.
* cockpit.socket starts the Cockpit web service when required.
* Cockpit normally uses port 9090.
* The firewall must allow the Cockpit service for remote web access.
* Cockpit provides a graphical view of CPU memory storage networking services logs and other system information.
* Cockpit can also provide Podman container management when the Cockpit Podman package is installed.
* The Cockpit dashboard provides a unified interface for common RHEL administration tasks.

## Conclusion

In this lab I learned how to use the Red Hat Customer Portal and Cockpit for RHEL system administration. I installed and configured Cockpit verified its service and port and accessed the web interface to monitor and manage the RHEL system.

## The Whole Lab in One Picture

Red Hat Customer Portal → Support Resources → Support Cases → Install Cockpit → Enable cockpit.socket → Allow Firewall Service → Port 9090 → Open Cockpit Web Interface → Monitor RHEL → View Logs → Manage System
