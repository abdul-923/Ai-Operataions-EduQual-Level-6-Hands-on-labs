

print("##Take Input")

name = input("Enter Name")
age = input ("Enter Age")

print("#Define Class: ")

class Student:
 def __init__(self, name, age):
   self.name = name
   self.age = age

 def study(self):
    print(f"{self.name} is studying. ")
 def exam(self):
    print(f"{self.name} is taking exam. ")


print("#Creating student object")
student1 = Student(name, age)

##Call Methods

student1.study()
student1.exam()


