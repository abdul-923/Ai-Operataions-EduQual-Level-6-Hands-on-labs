

# 24 - Python Style & PEP 8 Checks

## Objective

The objective of this lab was to understand the Python PEP 8 style guide and learn how to write clean, readable, and professional Python code. I also practiced checking code quality with Flake8 and automatically formatting code using Black.

## What I Practiced

* Understanding the purpose of PEP 8
* Installing Flake8 inside a Python virtual environment
* Installing Black inside a Python virtual environment
* Creating a Python file with intentional style mistakes
* Running Flake8 to detect coding style violations
* Understanding common Flake8 error codes
* Running Black to automatically format Python code
* Comparing code before and after formatting
* Learning the difference between code formatting and code analysis

## Commands Used

Create a virtual environment

* python3 -m venv venv

Activate the virtual environment

* source venv/bin/activate

Install Flake8

* pip install flake8

Install Black

* pip install black

Check Python style

* flake8 wrong.py

Automatically format the code

* black wrong.py

Display the file

* cat wrong.py

Check Flake8 version

* flake8 --version

## Expected Output

Flake8 reported style errors such as:

* E111 Indentation is not a multiple of 4
* E225 Missing whitespace around operator
* E231 Missing whitespace after comma
* E265 Block comment should start with "# "
* E305 Expected two blank lines after function definition

After running Black:

* File reformatted successfully
* Code spacing and indentation were corrected automatically
* The Python file became cleaner and easier to read

## What I Learned

* PEP 8 is the official Python coding style guide.
* Flake8 checks code quality and reports style violations.
* Black automatically reformats Python code according to PEP 8.
* Black changes formatting only. It does not change the logic of the program.
* Flake8 tells me what is wrong, while Black fixes most formatting issues automatically.
* Virtual environments allow me to install development tools without affecting the system Python installation.
* Professional Python developers usually run Black first and then Flake8 before committing their code.

## Files

* wrong.py
* right.py
* README.md
* screenshots/

## The Whole Lab in One Picture

Write Python Code

↓

Create a Virtual Environment

↓

Install Flake8

↓

Install Black

↓

Run Flake8

↓

Read Style Errors

↓

Fix Manually or Run Black

↓

Black Automatically Reformats the Code

↓

Run Flake8 Again

↓

Verify That the Code Follows PEP 8

↓

Commit Clean Code to GitHub

## Skills Gained

* Python
* PEP 8 Coding Standards
* Code Formatting
* Static Code Analysis
* Flake8
* Black
* Virtual Environments
* Linux Terminal
* pip Package Management
* Debugging
* Clean Code Practices

