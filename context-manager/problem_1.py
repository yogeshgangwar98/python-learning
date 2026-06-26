# A File logger problem

class FileLogger:
    def __enter__(self):
        print("Opening resource")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing resource")

with FileLogger():
    print("Working...")