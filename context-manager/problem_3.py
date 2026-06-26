# Context manager for a safe divison

class SafeDivision:
    def __enter__(self):
        print("Starting Division")

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is ZeroDivisionError:
            print("Cannot divide by zero")
        print("Division Completed")
        return True

with SafeDivision():
    print(10 / 2)

print("Program continues")