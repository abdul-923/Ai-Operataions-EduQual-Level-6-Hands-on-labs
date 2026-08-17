
# GitHub Actions – Beginner CI Automation Lab

## Overview

This lab demonstrates the basics of GitHub Actions by automatically running a Bash script whenever changes are pushed to the GitHub repository.

The lab shows how a GitHub Actions workflow:

* Detects a push to the repository
* Starts an Ubuntu runner
* Checks out the repository
* Finds and executes the Bash script
* Displays the script output in the Actions logs
* Reports whether the workflow succeeded or failed

This was my first practical GitHub Actions lab and helped me understand the relationship between the application/script and the workflow instructions.

## Files Included

* hello.sh 
* .github/workflows/test.yml
* Screenshots 
* ReadMe file

## Lab Objectives

* Understand what GitHub Actions is
* Create a basic GitHub Actions workflow
* Understand the purpose of a YAML workflow file
* Trigger a workflow using a Git push
* Run a Bash script automatically on GitHub
* Understand GitHub-hosted Ubuntu runners
* View workflow status and execution logs
* Understand successful and failed workflow runs
* Troubleshoot a basic GitHub Actions error

## Repository Structure

* .github/workflows/test.yml
* DevOps_Docker_Labs/14_GitHub_Actions/hello.sh

The workflow file is located under .github/workflows because GitHub automatically looks there for workflow definitions.

The Bash script remains inside the lab directory so the complete lab can stay organized with the other DevOps practice labs.

## GitHub Actions Workflow

The workflow was configured with:

* Workflow name: My First GitHub Action
* Trigger: push
* Runner: ubuntu-latest
* Job: test
* First step: Get repository
* Second step: Run Bash script

The workflow uses actions/checkout@v4 to bring the repository files into the GitHub runner.

It then executes the Bash script using the correct repository path.

## Commands Used

* mkdir -p .github/workflows — Created the hidden GitHub workflow directory structure.
* ls -la — Used to view hidden directories such as .github.
* git add . — Added the lab changes to Git.
* git commit -m "Changed" — Created a Git commit.
* git push origin main — Pushed changes to GitHub.
* gh auth login -h github.com — Attempted GitHub CLI authentication.
* git status — Used to check the repository state.

## Workflow Execution

The basic workflow process was:

* Create hello.sh
* Create test.yml
* Place test.yml inside .github/workflows
* Commit the changes
* Push the repository to GitHub
* GitHub detects the push
* GitHub starts an Ubuntu runner
* The runner checks out the repository
* The runner executes hello.sh
* The output appears in the workflow logs
* GitHub marks the workflow as successful or failed

## Output

The GitHub Actions page eventually showed:

* My First GitHub Action
* 3 workflow runs
* First run — Failed
* Second run — Failed
* Third run — Successful

The successful run was displayed with a green check mark.

The script output can be viewed through:

Actions → My First GitHub Action → Successful workflow run → test → Run Bash script

The terminal output from hello.sh is displayed inside the Run Bash script step.

## Errors Faced

### 1. Workflow Was Not Initially Appearing

The workflow was initially placed incorrectly.

GitHub Actions expects workflow files under:

.github/workflows/

Moving the workflow file to the correct location allowed GitHub to detect it.

### 2. Hidden Directory Confusion

The .github directory did not appear with a normal ls command because directories beginning with a dot are hidden in Linux.

Using ls -la displays hidden files and directories.

### 3. Personal Access Token Workflow Permission Error

While pushing the workflow, GitHub rejected the push because the Personal Access Token did not have the required workflow permission.

The error indicated that the token needed permission to create or update workflow files.

### 4. GitHub CLI Authentication Error

GitHub CLI authentication returned:

HTTP 401: Bad credentials

This was an authentication/token issue rather than a GitHub Actions workflow problem.

### 5. Invalid Workflow File

One workflow run failed because GitHub considered the workflow file invalid.

After correcting the YAML workflow, GitHub successfully recognized the workflow.

### 6. Incorrect Bash Script Path

The workflow initially attempted to run the script using an incorrect path.

The correct path from the repository root was:

DevOps_Docker_Labs/14_GitHub_Actions/hello.sh

After correcting the path, the workflow successfully executed.

## What I Learned

* GitHub Actions is an automation system built into GitHub.
* A workflow is simply a set of instructions written in YAML.
* The workflow file tells GitHub what to do with the repository.
* The actual application/script and the workflow are two different things.
* The workflow does not replace the script.
* The workflow tells GitHub how and when to execute the script.
* GitHub Actions can automatically start when code is pushed.
* GitHub can provide a temporary Ubuntu environment called a runner.
* The repository is checked out onto the runner before the script runs.
* Commands executed by the workflow produce terminal-style logs.
* The Actions page shows whether a workflow succeeded or failed.
* A green check mark means the workflow completed successfully.
* A red X means the workflow failed.
* The exact reason for failure can be found inside the individual job and step logs.
* GitHub workflow files must be stored under .github/workflows.
* Linux directories beginning with a dot are hidden.
* File paths in GitHub Actions are normally written relative to the repository root.
* GitHub Actions is especially useful for automation, testing, deployment, and server-related tasks rather than interactive scripts requiring a user to type input.


