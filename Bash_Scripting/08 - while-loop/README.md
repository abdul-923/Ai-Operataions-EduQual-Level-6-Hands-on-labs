
# Lab 08 – While Loop (Bash Scripting)

## Overview

This lab demonstrates how to use a `while` loop in Bash. The script starts with a counter value of `1`, checks whether the counter is less than or equal to `5`, prints the counter value, increases it by `1`, and repeats until the condition becomes false.

## Files

* `lab.sh` – Bash script demonstrating a while loop.
* `README.md` – Documentation for this lab.
* Screenshots


## What I Practiced

* Creating a Bash script.
* Using a `while` loop.
* Initializing a variable.
* Using a loop condition with `-le`.
* Displaying output with `echo`.
* Incrementing a variable using arithmetic expansion.
* Executing a Bash script from the terminal.

## Commands Used

* `nano lab.sh`
* `chmod +x lab.sh`
* `./lab.sh`

## Script Logic

1. Initialize the counter with the value `1`.
2. Check whether the counter is less than or equal to `5`.
3. Print the current counter value.
4. Increase the counter by `1`.
5. Repeat until the condition becomes false.

## Sample Output

Counter: 1

Counter: 2

Counter: 3

Counter: 4

Counter: 5

## Learning Outcome

After completing this lab, I learned how to use a `while` loop in Bash, how loop conditions work, how to update a variable using arithmetic expansion, and how a loop stops automatically when its condition becomes false.

## The Whole Lab in One Picture

* `counter=1` initializes the loop variable.
* `while [ $counter -le 5 ]` checks the loop condition.
* `echo` prints the current counter value.
* `counter=$((counter + 1))` increases the counter by one.
* The loop repeats until the counter becomes greater than `5`, then the script exits.
