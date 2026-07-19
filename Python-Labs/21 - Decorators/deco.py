
##Writing a Basic Decorator

def log_decorator(func):
  def wrapper(*args, **kwargs):
     print("Start")
     result = func(*args, **kwargs)
     print("End")
     return result
  return wrapper


##Applying the Decorator

@log_decorator
def say_hello(name):
  print(f"hello, {name}!")


##Calling

say_hello("Kabir")
