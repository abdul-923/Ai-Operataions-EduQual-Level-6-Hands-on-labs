

# Lab 09 – Bash Case Statement

## Lab Overview

This lab demonstrates how to use the Bash `case` statement to perform different actions based on a command-line argument. The script checks whether an argument is provided and executes the corresponding task such as starting, stopping, or checking the status of a service.

## Files Attached
- case.sh file
- Screenshots
- README.md
## Commands Used

cd Bash_Scripting

mkdir "09 - Case Statement"

cd "09 - Case Statement"

nano case.sh

chmod +x case.sh

./case.sh

./case.sh start

./case.sh stop

./case.sh status

./case.sh jkns


## Output

No argument:

Usage : ./case.sh {Start | Stop | Status}

Argument: start

Starting Services...

Argument: stop

Stopping Services...

Argument: status

Checking Status...

Invalid argument:

Invalid Command

## What I Learned

* Created a Bash script using the `case` statement.
* Used command-line arguments to control script behavior.
* Checked whether an argument was provided before executing the script.
* Handled multiple options (`start`, `stop`, and `status`) in a single script.
* Displayed a usage message when no argument was supplied.
* Handled invalid arguments using the default `*` case.
* Made the script executable using `chmod +x`.
* Executed the script with different command-line arguments.

## The Whole Lab in One Picture

Create the script → Make it executable → Run the script with a command-line argument → The script checks the argument → Executes the matching case (`start`, `stop`, or `status`) → Displays the corresponding output → Shows **Invalid Command** if the argument does not match any case.
