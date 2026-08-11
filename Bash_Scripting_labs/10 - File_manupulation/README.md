o
# File Manipulation Using Bash Script

## Lab Overview

This lab demonstrates how to create a Bash script that copies a file from one location to another using command-line arguments. The script also validates user input, checks whether the source file exists, performs the copy operation, and displays a success or error message based on the result.


## Files Included

* script.sh
* README.md
* testfile.txt (Source File)
* newfile.txt (Destination File - Created by the script)
* Screenshots


## Commands Used

* mkdir "10 - File_manupulation"
* cd "10 - File_manupulation"
* nano script.sh
* echo "testing... tesing.. tesing" > testfile.txt
* bash script.sh testfile.txt newfile.txt
* ls


## Expected Output

When both source and destination files are provided and the source file exists:

File copied successfully to 'newfile.txt'.

When required arguments are missing:

Argument Missing

When the source file does not exist:

Error: Source file not exist.

## What I Learned

* Creating a Bash script for file manipulation.
* Using command-line arguments with $1 and $2.
* Storing arguments in variables.
* Validating user input using the -z operator.
* Checking whether a source file exists using the -f operator.
* Copying files using the cp command.
* Checking the status of the previous command using $?.
* Displaying success and error messages using if-else conditions.
* Testing a Bash script with different input scenarios.
