# Safely closing a file, similar to open content manager
class CustomFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print(self.file.closed) 

with CustomFile("sample.txt", "w") as f:
    f.write("Hello World")