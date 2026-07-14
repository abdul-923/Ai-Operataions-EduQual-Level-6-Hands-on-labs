name = input("Enter name")
course = input("enter course")

with open("student.txt", "w") as file:
 file.write(f"students name: {name}/n")
 file.write(f"Course: {course}/n")

print("Student info saved")
