
##Practicing Modules in python

## Commands:
print("##Defining Function")

print("##Filename:mymodules.py")

def add(a, b):
 return a + b

print("##Created another file named main.py")

print("##Inport newly created module in main.py and usethe add function")

print("##Filename: main.py")

print("##Importing module from mymodules.py")

import mymodules

print("##calling the add function from mymodules.py")

result = mymodules.add(5, 6)
print(f"the sum:", {result})


##Output

##Filename: main.py
##Importing module from mymodules.py
##Defining Function
##Filename:mymodules.py
##Created another file named main.py
##Inport newly created module in main.py and usethe add function
##calling the add function from mymodules.py
the sum: {11}


