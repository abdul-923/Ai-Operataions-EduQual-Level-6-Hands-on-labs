
# 06 - Else and Elif Usage

## Overview

This lab demonstrates how to use `if`, `elif`, and `else` statements in a Bash script to make decisions based on a user's input. The script accepts a number from the user and determines whether it is greater than 10, exactly 10, less than 10, or if no input was provided.

## Files

* lab.sh
* README.md
* Screenshot 1 – Bash script (source code)
* Screenshot 2 – Terminal output

## What I Practiced

* Creating an interactive Bash script
* Reading user input using the `read` command
* Storing user input in a variable
* Checking for empty input using the `-z` operator
* Using `if`, `elif`, and `else` statements
* Comparing numbers using `-gt` and `-eq`
* Displaying different outputs based on user input
* Running an executable Bash script

## Commands Used

* mkdir "else_elif"
* cd "else_elif"
* nano lab.sh
* chmod +x lab.sh
* ./lab.sh

## Output

Example 1

* Enter Your Number:
* 34
* Above 10

Example 2

* Enter Your Number:
* 10
* Exactly 10

Example 3

* Enter Your Number:
* 5
* Below 10

Example 4

* Press Enter without typing a number
* Empty

## Learning Outcome

In this lab, I learned how to use conditional statements in Bash to make decisions based on user input. I practiced checking whether the user entered a value, comparing numbers using relational operators, and handling multiple conditions with `if`, `elif`, and `else`. This lab strengthened my understanding of decision-making logic and interactive Bash scripting.
