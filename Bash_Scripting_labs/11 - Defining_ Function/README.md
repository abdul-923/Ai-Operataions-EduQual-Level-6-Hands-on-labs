
# Bash Scripting Lab 11 – Defining Functions

## Lab Overview

This lab introduces Bash functions and demonstrates how to organize reusable code inside a shell script. The script defines a function that prints different greetings based on the arguments passed from the command line.

## Files Included

* script.sh
* README.md
* Screenshots

## What This Lab Covers

* Creating a Bash function
* Passing arguments to a function
* Using function parameters ($1 and $2)
* Using an if-else statement inside a function
* Calling a function from the main script
* Running the script with different command-line arguments

## Commands Used

* mkdir "11 - Defining_Function"
* cd "11 - Defining_Function"
* nano script.sh
* chmod +x script.sh
* bash script.sh Alice Morning
* bash script.sh Alice jksdfhf
* bash script.sh AMNA

## Expected Output

When the second argument is "morning", the script prints:

Good Morning, Alice

When the second argument is anything else, the script prints:

Hello, Alice

Example:

* bash script.sh Alice Morning → Good Morning, Alice
* bash script.sh Alice Evening → Hello, Alice
* bash script.sh AMNA → Hello, AMNA

## What I Learned

* How to define a function in Bash
* How to call a function from the main script
* How to pass command-line arguments into a function
* How function parameters ($1 and $2) work
* How to use if-else statements inside a function
* How functions make Bash scripts reusable, organized, and easier to maintain
