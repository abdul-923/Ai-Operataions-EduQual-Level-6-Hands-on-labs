
# 13 - Command Substitution in Bash

## Overview

This lab demonstrates how to use command substitution in Bash. Command substitution allows the output of a Linux command to be stored in a variable so it can be reused later in the script. Instead of displaying command output directly on the terminal, the script captures it and prints it whenever required.

## Files Included

* script.sh – Bash script demonstrating command substitution.
* README.md – Documentation for this lab.
* screenshots/ – Screenshots showing the script and terminal output.

## Lab Objectives

* Understand what command substitution is.
* Store command output inside variables.
* Display stored values using the echo command.
* Use commonly used Linux commands inside Bash scripts.


## Commands Used

* mkdir
* cd
* nano
* chmod +x
* bash
* ./script.sh
* date
* whoami
* pwd
* echo


## Script Workflow

The script performs the following tasks:

1. Executes the date command and stores its output in the current_date variable.
2. Displays the current date using the stored variable.
3. Executes the whoami command and stores the logged-in username in the user_name variable.
4. Displays the current username.
5. Executes the pwd command and stores the current working directory in the current_dir variable.
6. Displays the current working directory.

## Output

The script displays:

* Current date and time.
* Current logged-in user.
* Current working directory.

## What I Learned

* How command substitution works in Bash.
* How to store command output inside variables using the command substitution syntax.
* How to reuse stored values later in a script.
* The purpose of the date, whoami, and pwd commands.
* How variables make Bash scripts cleaner and easier to maintain.

## Key Concepts

* Command substitution executes a command and stores its output.
* Command substitution uses the dollar sign followed by parentheses.
* Variables can store the output of Linux commands.
* Stored values can be displayed multiple times without executing the command again.
* Command substitution improves script readability and reusability.

## The Whole Lab in One Picture

Run a Linux command → Capture its output using command substitution → Store the output in a variable → Use the variable later with the echo command → Display the stored information without running the command again.


