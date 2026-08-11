

## Defining A Class

class MyContext:


  def __enter__(self):
    print("Entering")
    return self



  def __exit__(self, exc_type, exc_value, traceback):
    print("Exiting")


with MyContext() as context:
    print("Running within the context block.")


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Using the FileManager context manager to handle file operations
with FileManager('sample.txt', 'w') as f:
    f.write("Hello, World!")
