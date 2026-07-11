Practicing lists and list types in Python

#Commands Used

umbers = ["1", "2", "3", "4", "5", "6"]
print("numbers are: ", numbers)

##Append

numbers.append("23")
print("after append:", numbers)


##Remove

numbers.remove("5")
print("after removal", numbers)


##Sort
numbers.sort()
print("sorted list: ", numbers)

##Iterate over the list

for number in numbers:
 print("number:", number)







###Output

numbers are:  ['1', '2', '3', '4', '5', '6']
after append: ['1', '2', '3', '4', '5', '6', '23']
after removal ['1', '2', '3', '4', '6', '23']
sorted list:  ['1', '2', '23', '3', '4', '6']
number: 1
number: 2
number: 23
number: 3
number: 4
number: 6
