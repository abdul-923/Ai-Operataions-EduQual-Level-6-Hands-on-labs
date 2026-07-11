Practicingfoor and while loop

#Python Commands

##For Loop
students = ["Ali", "Jhon", "Oliver", "Klevin"]

for student in students:
 print("Welcome Dear", student)


##Another Project

for number in range(1, 11):
 answer = 5 * number
 print("5 x", number, "=", answer)



###While Loop

correct_pass = "python123"

password = input("Enter Your password: ")

while password != correct_pass:
 print("wrong! try again")
 passwrod = input("enter your password: ")

print("login authenticated")



####Output####

Welcome Dear Ali
Welcome Dear Jhon
Welcome Dear Oliver
Welcome Dear Klevin
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Enter Your password: python123
login authenticated



