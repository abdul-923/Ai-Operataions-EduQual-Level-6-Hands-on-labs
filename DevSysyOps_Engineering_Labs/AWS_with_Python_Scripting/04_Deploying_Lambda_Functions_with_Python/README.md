


# Lab 4 – Deploying Lambda Functions with Python

## Overview

In this lab I practiced deploying a Python function to AWS Lambda using AWS CLI. I created an IAM role and deployed a simple function that returns Hello World.

## Files Included

- lambda_function.py
- policy.json
- my_lambda_function.zip
- output.txt
- Redame.md

- Screenshots
## Commands Used

- mkdir lab5-lambda
- nano lambda_function.py
- mkdir my_lambda_package
- cp lambda_function.py my_lambda_package/
- cd my_lambda_package
- zip my_lambda_function.zip lambda_function.py
- aws iam create-role
- aws iam attach-role-policy
- aws lambda create-function
- aws lambda invoke
- cat output.txt

## Output

- Created an IAM role for AWS Lambda
- Deployed the Python function successfully
- Invoked the Lambda function
- Received Hello World as the output

## What I Learned

- How AWS Lambda runs Python code in the cloud
- How to create and deploy a Lambda function
- How to create an IAM role and attach permissions
- How to package Python code into a ZIP file
- How to use AWS CLI to invoke a function

## Conclusion

In this lab I learned how to deploy and run a Python function using AWS Lambda. I also practiced using IAM roles and AWS CLI to manage serverless functions.
