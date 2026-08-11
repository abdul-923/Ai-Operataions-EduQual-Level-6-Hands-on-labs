

04 - Command Line Arguments

Overview

This lab demonstrates how to pass command-line arguments to a Bash script. It covers accepting a single argument, handling multiple arguments, validating user input, and greeting multiple users using a loop.

Files

- greet.sh
- greet2.sh
- README.md
- Screenshots

What I Practiced

- Passing command-line arguments to a Bash script
- Using $1 to access the first argument
- Using $# to count the number of arguments
- Displaying a usage message when no arguments are provided
- Using for loop with "$@" to process multiple arguments
- Running executable Bash scripts


Commands Used

- nano greet.sh
- nano greet2.sh
- chmod +x greet.sh
- chmod +x greet2.sh
- ./greet.sh Alice
- ./greet2.sh Amna Ali

Output
- Hello, Alice!
- Hello, Amna!
- Hello, Ali!


Learning Outcome

In this lab, I learned how to pass command-line arguments to a Bash script instead of asking the user for input using the read command. I also learned how to access the first argument using $1, count the number of arguments using $#, validate user input, and process multiple arguments using a for loop with "$@". These concepts are useful for creating reusable and automated Bash scripts.
