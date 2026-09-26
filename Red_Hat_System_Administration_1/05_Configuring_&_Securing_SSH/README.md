# Red Hat Lab 5 – Configuring and Securing SSH

## Overview

In this lab I practiced installing and configuring OpenSSH on a RHEL system.
I checked the SSH installation and verified the SSH service status. I created a backup of the SSH configuration file and modified sshd_config to improve SSH security.
I practiced changing the default SSH port. disabling direct root login. restricting authentication methods and allowing key based authentication.
I also generated SSH keys. configured the SSH firewall port and verified the SSH configuration and service.

## Files Included

* README.md
* Screenshots
* SSH configuration backup
* Command history

## Commands Used

* ssh -V
* sudo dnf install openssh-server -y
* sudo systemctl status sshd
* sudo systemctl start sshd
* sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
* sudo nano /etc/ssh/sshd_config
* sudo systemctl restart sshd
* ss -tulnp
* sudo journalctl -xe
* ssh-keygen -t ed25519
* ssh-copy-id
* ssh
* chmod 700 ~/.ssh
* chmod 600 ~/.ssh/authorized_keys
* sudo firewall-cmd --permanent --add-port=2222/tcp
* sudo firewall-cmd --reload
* sudo firewall-cmd --list-ports

## SSH Security Configuration

* Changed the default SSH port to 2222
* Disabled direct root login
* Disabled password authentication
* Enabled public key authentication
* Restricted SSH access to allowed users
* Configured the firewall to allow the SSH port

## SSH Key Authentication

I generated an Ed25519 SSH key pair on the client machine.

The public key was copied to the RHEL server and used for key based authentication.

This allows users to log in through SSH without using a normal account password.

## Firewall Configuration

The RHEL firewall was configured to allow TCP port 2222 for SSH connections.

The firewall rule was reloaded and verified after the configuration.

## Output

* Verified that OpenSSH was installed.
* Verified that the SSH service was running.
* Created a backup of the original SSH configuration.
* Modified the SSH configuration for better security.
* Changed the default SSH port.
* Disabled direct root login.
* Disabled password based SSH authentication.
* Enabled public key authentication.
* Generated an Ed25519 SSH key pair.
* Configured key based SSH login.
* Configured the RHEL firewall for the new SSH port.
* Verified the SSH listening port.
* Checked SSH service logs.
* Tested the SSH configuration.

## What I Learned

I learned how SSH works on a RHEL system and how the SSH server is managed through sshd.
I learned how to configure the SSH server through sshd_config.
I learned the difference between password authentication and public key authentication.
I learned how to prevent direct root login through SSH.
I learned how to change the default SSH port.
I learned how to generate SSH keys and use them for passwordless authentication.
I learned how to configure firewalld to allow SSH traffic.
I learned how to check SSH service status and troubleshoot SSH problems using systemctl and journalctl.
I also learned how SSH security settings work together to control remote access to a Linux system.

## Conclusion

This lab gave me practical experience with configuring and securing SSH on RHEL.

I learned how to manage the SSH service. configure authentication. secure root access. use SSH keys and configure the firewall for secure remote connections.

## The Whole Lab in One Picture

Install OpenSSH → Check SSH Service → Backup Configuration → Edit sshd_config → Change SSH Port → Disable Root Login → Disable Password Authentication → Enable Public Key Authentication → Generate SSH Keys → Copy Public Key → Test SSH Login → Configure Firewall → Verify SSH → Check Logs

This lab improved my practical understanding of secure remote administration on RHEL.
