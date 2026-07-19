

# Decorators in Python

## Objective

The objective of this lab was to understand how Python decorators work. I learned how a decorator can add extra functionality to a function without changing the original function's code.

## What I Practiced

* Creating a basic decorator using 'def'.
* Creating a nested 'wrapper()' function.
* Using '*args' and '**kwargs' to accept any arguments.
* Printing a message before and after a function executes.
* Applying a decorator using the '@' symbol.
* Running and testing the decorated function.
* Fixing syntax errors while writing the decorator.

## Code

'deco.py'

* Created 'log_decorator(func)'.
* Defined 'wrapper(*args, **kwargs)'.
* Printed '"Start"` before calling the original function.
* Executed the original function.
* Printed '"End"' after the function finished.
* Applied the decorator to 'say_hello(name)' using '@log_decorator'.
* Called the function with:

'say_hello("Kabir")'

## Commands Used

Create the project directory:

'mkdir "21 - Decorators"'

Go into the directory:

'cd "21 - Decorators"

Create the Python file:

'nano deco.py'

Run the program:

`python3 deco.py`

## Output

Start

Hello, Kabir!

End

## What I Learned

* A decorator is a function that wraps another function.
* The `@` symbol applies a decorator to a function.
* `func` is a parameter that receives the original function.
* `wrapper()` adds extra behavior before and after the original function runs.
* `*args` and `**kwargs` allow the decorator to work with functions that accept any number of arguments.
* Decorators help avoid repeating the same code in multiple functions.

## Files

* `deco.py`
* `README.md`
* Screenshots of the program execution
