
# Lab 10 – Scheduling Docker Workloads with Bash and Cron

## Overview

In this lab I learned how to automate Docker backups using Bash and Cron.

I created a custom Docker image that contains test files and copies them to a backup directory.

I wrote a Bash script to run the Docker backup tool and store the backup files on my Ubuntu system.

## Files Included

- Dockerfile
- lab.sh
- README.md
- Commands History

## Commands Used

- vim Dockerfile
- vim lab.sh
- chmod +x lab.sh
- docker build -t backup_tool .
- docker images backup_tool
- bash lab.sh
- ls -l \~/backup_data
- cat \~/backup_data/file1.txt
- cat \~/backup_data/file2.txt
- crontab -e

## Output

- Docker image was built successfully.
- Bash script executed the backup workflow.
- Backup directory was created.
- File1.txt and file2.txt were copied successfully.
- Backup file contents were verified.

## What I Learned

- I learned how to create a Docker image using a Dockerfile.
- I learned how to write a Bash script for Docker automation.
- I learned how to use Bash variables and functions.
- I learned how to mount a host directory into a Docker container.
- I learned how to copy files using Docker.
- I learned how to verify backup files on Ubuntu.
- I learned how Cron can schedule scripts to run automatically.

## Conclusion

In this lab I successfully created a Docker backup tool and automated the backup workflow using Bash. I also learned how Cron can be used to schedule recurring tasks.

Add the actual Cron scheduleShow the sample command output
