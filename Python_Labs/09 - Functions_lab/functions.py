

print("##Define Function")

def greet(name):
  return f"hello, {name}!"

print (greet("Alice"))
print (greet("Huda"))
print (greet("Amna"))


print("##usingDefault parameters")

def greet(name="Guest"):
  return f"Hello, {name}!"

print(greet())


print("##Utilizing keyword argument")

print(greet(name="Diana"))
