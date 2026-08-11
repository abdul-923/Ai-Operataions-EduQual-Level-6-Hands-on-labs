# List and List Methods Lab

## Objective

The purpose of this lab was to learn how to create and manipulate lists in Python. I practiced storing multiple values in a list and performing common operations such as adding, removing, sorting, and iterating through list elements.


## Topics Covered

* Creating a list
* Printing a list
* append()
* remove()
* sort()
* for loop
* Iterating through a list
* Debugging NameError
* Debugging SyntaxError


## Files

* `lists.py'


## Methods Used

### append()

Adds a new item to the end of the list.

Example:

- `numbers.append("23")



### remove()

Removes a specific value from the list.

Example:

- `numbers.remove("5")



### sort()

Sorts the list in ascending order.

Example:
- `numbers.sort()


### for Loop

Used to access each element of the list one by one.

Example:

- `for number in numbers:



## Output

The program performs the following operations:

* Creates a list
* Displays the original list
* Adds a new value
* Removes an existing value
* Sorts the list
* Prints every element individually



## Errors Faced During the Lab

### NameError

Problem:

- Used 'number.sort()' instead of 'numbers.sort()'.

Reason:

- 'number` variable did not exist.

Solution:

Changed it to:

`numbers.sort()'



### SyntaxError

Problem:

Forgot the comma in:

- bprint("after removal" numbers)

Solution:

Corrected it to:

- print("after removal", numbers)



## Skills Learned

* Working with Python lists
* Using built-in list methods
* Looping through list elements
* Reading and fixing Python error messages
* Understanding the difference between a list variable and a loop variable

---

## The Whole Lab in One Picture
'''
Create List
      │
      ▼
Print Original List
      │
      ▼
Append New Item
      │
      ▼
Remove Item
      │
      ▼
Sort List
      │
      ▼
Loop Through List
      │
      ▼
Print Each Item
'''



## Conclusion

This lab helped me understand how Python lists work and how to perform common operations such as adding, removing, sorting, and iterating over data. It also improved my debugging skills by identifying and fixing common Python errors like 'NameError' and `SyntaxError'.
