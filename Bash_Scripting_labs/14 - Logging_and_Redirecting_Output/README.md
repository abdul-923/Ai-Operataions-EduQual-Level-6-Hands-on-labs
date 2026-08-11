
# Logging and Redirecting Output in Bash

## Lab Overview

In this lab, I learned how to display output on the terminal while simultaneously saving the same output into a log file using the tee command. This is a common practice in Linux administration, DevOps, and automation because it allows users to monitor a script in real time while keeping a permanent record for troubleshooting and auditing.

## Objective

The objective of this lab was to:

* Understand the purpose of logging in Bash scripts.
* Learn how the tee command works.
* Display output on the terminal and save it to a file at the same time.
* Verify the saved log file.

## Commands Used

#!/bin/bash

echo "Welcome to the Logging and Redirecting Output Lab!"
echo "This script demonstrates output management."
echo "Each message will be logged to a file and displayed on the console."

{
echo "Welcome to the Logging and Redirecting Output Lab!"
echo "This script demonstrates output management."
echo "Each message will be logged to a file and displayed on the console."
} | tee output.log

chmod +x script.sh

./script.sh

ls

cat output.log

## Script Workflow

1. The script prints three messages using the echo command.
2. The messages are grouped using curly braces { }.
3. The pipe | sends the grouped output to the tee command.
4. The tee command displays the output on the terminal.
5. The tee command also saves the same output into output.log.
6. The script is made executable using chmod +x.
7. The script is executed.
8. The output.log file is viewed using cat to verify the saved output.

## Output

The script displays:

* Welcome to the Logging and Redirecting Output Lab!
* This script demonstrates output management.
* Each message will be logged to a file and displayed on the console.

The file output.log contains the same messages.

## What I Learned

* How to use the tee command.
* How to display output on the terminal and save it to a file simultaneously.
* The purpose of logging in Bash scripts.
* How the pipe | sends output from one command to another.
* How to verify saved logs using the cat command.
* Why logging is important for automation, server administration, DevOps, and cybersecurity.

## The Whole Lab in One Picture

Print messages → Group output using { } → Send output through | → tee displays the output on the terminal → tee saves the same output into output.log → Verify the saved log using cat output.log
