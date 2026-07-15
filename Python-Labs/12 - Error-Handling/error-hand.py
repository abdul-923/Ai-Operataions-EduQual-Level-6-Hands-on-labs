
print("##Single except Block")

user_input = input("Enter Number: ")

try:
 number = int(user_input)
 print(f"the num is: {number}")

except ValueError:
 print("Error: Input the valid number. ")


print("##Multi except block")

user_input = input("Enter num: ")

try:
 result = 10 / int(user_input)
 print(f"result is: {result}")

except ValueError:
 print("value error")

except ZeroDivisionError:
 print("Error: division by zero is undefined")
