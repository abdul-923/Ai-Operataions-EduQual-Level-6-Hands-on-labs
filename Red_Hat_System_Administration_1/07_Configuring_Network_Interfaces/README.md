# Red Hat Lab 07 – Configuring Network Interfaces

## Overview

In this lab I practiced managing network interfaces in Red Hat Enterprise Linux using NetworkManager and nmcli.

I learned how to view network devices and connection profiles. I configured a static IP address and modified network settings such as MTU and IPv6.

I also practiced restarting NetworkManager and configuring the hostname and DNS settings.

Finally I tested network connectivity and DNS resolution.

## Files Included

* README.md
* Screenshots
* Command history
* Lab notes

## Commands Used

* sudo systemctl status NetworkManager
* sudo systemctl start NetworkManager
* nmcli device status
* nmcli device show
* nmcli connection show
* ip link
* ip addr show
* nmcli connection modify
* nmcli connection up
* nmcli connection show
* nmcli connection modify 802-3-ethernet.mtu 1500
* nmcli connection modify ipv6.method disabled
* sudo systemctl restart NetworkManager
* systemctl status NetworkManager
* sudo hostnamectl set-hostname mylabhost
* hostnamectl
* nmcli connection modify ipv4.dns
* nmcli connection modify ipv4.ignore-auto-dns yes
* ping -c 4 8.8.8.8
* nslookup google.com
* sudo nmcli device disconnect
* sudo nmcli device connect
* cat /etc/resolv.conf
* dig example.com
* sudo nmcli device reapply

## Output

* Verified that NetworkManager was running.
* Listed available network devices using nmcli.
* Viewed detailed network interface information.
* Identified the active network connection profile.
* Configured a static IP address.
* Configured the network gateway.
* Configured DNS servers.
* Changed the IP configuration method from DHCP to manual.
* Modified the MTU setting.
* Disabled IPv6 for the connection.
* Restarted NetworkManager successfully.
* Verified the NetworkManager service status.
* Changed and verified the system hostname.
* Configured DNS settings.
* Tested network connectivity using ping.
* Tested DNS resolution using nslookup.
* Practiced troubleshooting network connections.

## What I Learned

* How to manage network interfaces in RHEL using nmcli.
* How NetworkManager manages network connections.
* How to view network devices and connection profiles.
* How DHCP automatically provides network configuration.
* How to configure a static IP address.
* How to configure a gateway and DNS servers.
* How to modify MTU settings.
* How to disable IPv6.
* How to restart and verify NetworkManager.
* How to configure a system hostname.
* How to test network connectivity.
* How to test DNS resolution.
* How to troubleshoot network configuration problems.

## Conclusion

This lab gave me practical experience with network configuration in Red Hat Enterprise Linux.

I learned how to inspect network interfaces and manage their connection profiles using nmcli.

I also learned how to configure static IP addresses and network settings and verify that the network is working correctly.

These skills are important for Linux system administration and container networking.

## The Whole Lab in One Picture

Check NetworkManager → List Network Devices → View Connection Profiles → Configure Static IP → Configure Gateway → Configure DNS → Modify MTU → Disable IPv6 → Restart NetworkManager → Set Hostname → Test Connectivity → Test DNS → Troubleshoot Network
