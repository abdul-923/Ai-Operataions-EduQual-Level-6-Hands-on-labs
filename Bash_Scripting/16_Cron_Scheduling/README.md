

# Cron Scheduling in Bash

## Lab Overview

In this lab, I learned how to automate the execution of a Bash script using Cron, Linux's built-in task scheduler. Instead of manually running a script every time, Cron executes it automatically based on a schedule. This is a fundamental skill in Linux administration, DevOps, cloud computing, and cybersecurity because many maintenance, monitoring, backup, and automation tasks rely on scheduled execution.

## Objective

The objective of this lab was to:

* Understand the purpose of Cron in Linux.
* Create a Bash script that writes output to a file.
* Make the script executable.
* Schedule the script to run automatically every minute using Cron.
* Verify that the scheduled job executes successfully.

## Commands Used

#!/bin/bash

echo "Cron test" >> /home/ubuntu/cron_output.txt

chmod +x script.sh

crontab -e

* * * * * /home/ubuntu/Ai-Operations-EduQual-Level-6-Hands-on-labs/Bash_Scripting/15_Cron_Scheduling/script.sh

crontab -l

cat /home/ubuntu/cron_output.txt

## Script Workflow

1. A Bash script is created to write the text "Cron test" into a file.
2. The >> operator appends the text instead of overwriting the existing file.
3. The script is made executable using chmod +x.
4. The crontab editor is opened using crontab -e.
5. A Cron schedule is added to execute the script every minute.
6. Cron automatically runs the script without manual intervention.
7. Every execution appends another "Cron test" line to cron_output.txt.
8. The scheduled Cron job is verified using crontab -l.
9. The output file is checked using cat to confirm that the script executed successfully.

## Main Commands Cheat Sheet

#!/bin/bash – Specifies that the script should be executed using the Bash shell.

echo – Prints text or writes text to a file.

> > – Appends output to a file without deleting existing content.

chmod +x – Makes a script executable.

crontab -e – Opens the user's Cron schedule for editing.

* * * * * – Schedules a task to run every minute.

crontab -l – Displays all scheduled Cron jobs.

cat – Displays the contents of a file.

## Output

After the Cron job runs:

* A file named cron_output.txt is created (if it does not already exist).
* Every minute, another line containing "Cron test" is appended to the file.
* The Cron schedule can be viewed using crontab -l.
* The contents of the output file can be verified using cat /home/ubuntu/cron_output.txt.

Example output:

Cron test

Cron test

Cron test

Cron test

## What I Learned

* The purpose of Cron in Linux automation.
* How to create a scheduled task using crontab.
* How Cron automatically executes scripts without user interaction.
* The difference between appending (>>) and overwriting (>) output.
* How to verify scheduled jobs using crontab -l.
* How to verify script execution by checking the output file.
* Why Cron is widely used for backups, monitoring, maintenance, reporting, and automation.

## The Whole Lab in One Picture

Create a Bash script → Make it executable using chmod +x → Open the Cron scheduler using crontab -e → Schedule the script to run every minute → Cron automatically executes the script → The script appends "Cron test" to cron_output.txt → Verify the scheduled job using crontab -l → Confirm execution by viewing cron_output.txt with cat.
