
# Red Hat Lab 10 – Monitoring System Performance and Resource Usage

## Overview

This lab focused on monitoring system performance and resource usage in Red Hat Enterprise Linux. I learned how to monitor CPU memory disk and network usage and how to identify processes that consume high resources. I also learned how to detect resource exhaustion using different Linux monitoring tools.

## Files Included

* README.md
* Screenshots
* lab_commands.txt

## Commands Used

* top
* sudo dnf install sysstat -y
* mpstat -P ALL 1 5
* free -h
* top -o %MEM
* df -h
* du -sh /var/log/*
* sudo dnf install iotop -y
* sudo iotop -o
* ss -tulnp
* sudo dnf install dstat -y
* dstat
* ps aux --sort=-%cpu | head -n 5
* ps aux --sort=-%mem | head -n 5
* podman stats
* journalctl -p err -b
* sudo dnf install stress-ng -y
* stress-ng --cpu 4 --vm 2 --timeout 30s

## Output

* Monitored CPU usage and identified high CPU processes
* Displayed CPU usage for each CPU core using mpstat
* Checked total used and available memory using free
* Identified memory hungry processes using top
* Checked filesystem disk usage using df
* Checked directory sizes under /var/log using du
* Monitored disk I/O using iotop
* Checked active network connections and listening ports using ss
* Monitored real time network traffic using dstat
* Identified processes consuming high CPU and memory resources
* Checked container resource usage using podman stats
* Checked critical system errors using journalctl
* Simulated high system load using stress-ng

## What I Learned

I learned how to monitor CPU memory disk and network resources in RHEL. I learned how to identify processes that use excessive CPU or memory and how to check disk I/O and network connections. I also learned how to use system logs to find critical errors and how to simulate high system load for testing.

## Conclusion

This lab gave me practical experience with Linux system performance monitoring. I learned how different tools can be used to find resource usage and troubleshoot performance problems. These skills are useful for system administration DevOps and AI Operations work.

## The Whole Lab in One Picture

Monitor CPU with top and mpstat → Check memory with free and top → Check disk with df and du → Monitor disk I/O with iotop → Check network with ss and dstat → Analyze processes with ps → Monitor containers with podman stats → Check errors with journalctl → Test high load with stress-ng.
