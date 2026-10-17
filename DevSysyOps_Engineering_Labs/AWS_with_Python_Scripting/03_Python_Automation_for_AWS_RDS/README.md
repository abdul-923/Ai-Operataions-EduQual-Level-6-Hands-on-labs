
# Lab 3 – Python Automation for AWS RDS

## Overview

In this lab I practiced automating AWS RDS using Python and Boto3. I created a menu-driven script to list databases monitor database status and delete a database with confirmation.

## Files Included

- rds_lab.py
- Screenshots
- Readme.md
- Commangs History

## Commands Used

- mkdir lab4-rds
- cd lab4-rds
- python3 -m venv .venv
- source .venv/bin/activate
- python -m pip install boto3
- nano rds_lab.py
- python rds_lab.py

## Output

- Listed available RDS databases
- Displayed database status and storage information
- Requested database deletion with confirmation
- Displayed a message when no databases were available

## What I Learned

- How to use Boto3 to interact with AWS RDS
- How to list databases using Python
- How to monitor database status
- How to request database deletion safely
- How to use functions and a menu in Python
- How to handle AWS errors

## Conclusion

In this lab I learned how to automate basic AWS RDS management tasks using Python and Boto3. I also practiced using functions and error handling to manage AWS resources.
