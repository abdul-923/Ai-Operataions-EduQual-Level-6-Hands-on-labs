

# Lab – Creating Dashboards on CloudWatch with Python

## Overview

In this lab I practiced automating AWS CloudWatch monitoring using Python and Boto3. I retrieved EC2 CPU utilization metrics and created a CloudWatch dashboard to visualize instance performance.

## Files Included

- cloudwatch_dashboard.py

## Commands Used

- python3 -m venv .venv
- source .venv/bin/activate
- python -m pip install boto3
- aws sts get-caller-identity
- aws ec2 describe-instances --region us-east-1 --query "Reservations[].Instances[].[InstanceId,State.Name]" --output table
- aws cloudwatch get-metric-statistics
- python3 cloudwatch_dashboard.py

## Output

- Connected Python to AWS using Boto3
- Retrieved EC2 CPU utilization metrics
- Created the MyDashboard CloudWatch dashboard
- Displayed CPU utilization in a CloudWatch metric widget

## What I Learned

- How to use Boto3 to interact with AWS CloudWatch
- How to retrieve EC2 CPU utilization metrics
- How to create CloudWatch dashboards using Python
- How to configure metric widgets with the correct instance ID and AWS region
- How to troubleshoot missing CloudWatch metric data

## Conclusion

In this lab I learned how to automate AWS monitoring by retrieving EC2 CPU utilization metrics and creating a CloudWatch dashboard using Python and Boto3.
