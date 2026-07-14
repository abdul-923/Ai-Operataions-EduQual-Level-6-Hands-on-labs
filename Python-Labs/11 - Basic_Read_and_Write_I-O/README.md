## Practicng basic python read and write or Input output in python

##Write File:

  GNU nano 8.7.1                                                          save_student.py                                                                   
name = input("Enter name")
course = input("enter course")

with open("student.txt", "w") as file:
 file.write(f"students name: {name}/n")
 file.write(f"Course: {course}/n")

print("Student info saved")


##Read File:

with open("student.txt", "r") as file:
 information = file.read()

print("Saved info: ")
print(information)



##Saving txt File:

Enter name kali
enter course linux
Student info saved


##oUTPUT:

Saved info: 
students name:  kali/nCourse:  linux/n

