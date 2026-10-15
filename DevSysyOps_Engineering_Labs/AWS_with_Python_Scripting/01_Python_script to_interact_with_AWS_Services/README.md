
# Lab 2 – Basic Python Script to Interact with AWS Services

## Overview

Today I practiced using Python to interact with AWS services. I installed Boto3 in a Python virtual environment and used it to connect to AWS S3. I created a Python script to list my S3 buckets and verified that it was working using my AWS credentials.

## Files Included

- list_s3_buckets.py
- Screensghots
- Readme.md

## Commands Used

- python3 --version
- pip3 --version
- sudo apt update
- sudo apt install python3-venv -y
- python3 -m venv .venv
- source .venv/bin/activate
- python -m pip install boto3
- aws sts get-caller-identity
- nano list_s3_buckets.py
- python list_s3_buckets.py

## Output

- Python virtual environment created successfully
- Boto3 installed successfully
- AWS credentials verified successfully
- Python connected to AWS S3
- S3 bucket name displayed successfully

## What I Learned

- How to install and use Boto3
- How to create and activate a Python virtual environment
- How to connect Python to AWS S3
- How to list S3 buckets using Python
- How to use a for loop to print bucket names

## Conclusion

In this lab I learned how to use Python and Boto3 to interact with AWS S3. I successfully ran my script and retrieved my S3 bucket name from AWS.

Add the script contentsExplain the script workflowFix the plural bucket wording
