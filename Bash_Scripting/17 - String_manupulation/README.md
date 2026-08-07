
# String Manipulation in Bash

## Lab Overview

In this lab, I learned how to perform basic string manipulation in Bash scripting. The script accepts a string from the user, displays the entered text, calculates the total length of the string, extracts a specific substring, and replaces a portion of the string with another value. These operations are commonly used in Linux automation, DevOps, system administration, and text processing tasks.

---

## Objective

The objective of this lab was to:

* Accept string input from the user.
* Store user input in a variable.
* Display the entered string.
* Calculate the length of the string.
* Extract a substring from the entered text.
* Replace part of a string with another value.
* Understand the basics of Bash string manipulation.

## Commands Used

#!/bin/bash

echo

read

length=${#user_input}

substring=${user_input:2:4}

modified_string=${user_input//abc/xyz}

chmod +x string.sh

./string.sh

## Script Workflow

1. The script prompts the user to enter a string.
2. The entered string is stored in the user_input variable.
3. The script displays the original string entered by the user.
4. The total number of characters is calculated and stored in the length variable.
5. A substring is extracted starting from the third character for four characters.
6. The script replaces every occurrence of "abc" with "xyz".
7. The modified string is displayed on the terminal.


## What I Learned

* How to read string input from the user.
* How to store and display string values using variables.
* How to calculate the length of a string.
* How to extract a specific portion of a string.
* How to replace text within a string using Bash parameter expansion.
* Why string manipulation is useful for automation, log processing, configuration management, and Linux administration.


## The Whole Lab in One Picture

User enters a string → Store the input in a variable → Display the original string → Calculate the string length → Extract a substring → Replace matching text inside the string → Display the final modified string.
