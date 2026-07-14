numbers = ["1", "2", "3", "4", "5", "6"]
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
