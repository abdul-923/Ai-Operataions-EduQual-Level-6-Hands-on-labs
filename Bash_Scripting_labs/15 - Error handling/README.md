
# Error Handling in Bash – Checking Directory Existence

## Lab Overview

In this lab, I learned how to implement basic error handling in a Bash script by checking whether a required directory exists before continuing execution. Instead of allowing the script to fail unexpectedly, it validates the directory, displays a meaningful message to the user, and terminates safely if the directory is missing. This is a fundamental practice in Linux administration, DevOps, automation, and cybersecurity because it helps create reliable and predictable scripts.

## Objective

The objective of this lab was to:

* Understand the importance of validating user input and resources before executing a script.
* Learn how to check whether a directory exists.
* Implement conditional statements using if and else.
* Display meaningful error messages to users.
* Stop script execution safely using exit codes.
* Understand the basics of Bash error handling.

## Commands Used

#!/bin/bash

directory="/home/ubuntu/Ai-Operations-EduQual-Level-6-Hands-on-labs/Bash_Scripting"

if [ -d "$directory" ]; then

echo "Directory Exists."

else

echo "Error: Directory not exist."

echo "Please Create a Directory first."

exit 1

fi

chmod +x script.sh

./script.sh

pwd

## Script Workflow

1. The script starts by using the Bash interpreter.
2. A directory path is stored inside the directory variable.
3. The if statement begins a conditional check.
4. The -d test verifies whether the specified path exists and is a directory.
5. If the directory exists, the script displays a success message.
6. If the directory does not exist, the else block executes.
7. An error message is displayed explaining the problem.
8. A second message guides the user on how to resolve the issue.
9. The script terminates using exit 1 to indicate unsuccessful execution.
10. The script is made executable using chmod +x.
11. The script is executed using ./script.sh.

## Output

If the directory exists:

* Directory Exists.

If the directory does not exist:

* Error: Directory not exist.
* Please Create a Directory first.

The script exits with status code 1 when the required directory is missing.

## What I Learned

* How to check whether a directory exists using the -d test.
* How to use if, else, and fi for decision making in Bash.
* How to store file system paths inside variables.
* How to display meaningful error messages to users.
* How to terminate a script safely using exit 1.
* Why input validation is important before performing operations.
* How error handling improves the reliability of Bash automation scripts.

## The Whole Lab in One Picture

Store directory path → Check directory using if and -d → If directory exists → Continue execution → If directory does not exist → Display error message → Show guidance to the user → Stop execution using exit 1 → Prevent invalid operations and unexpected failures
