
def divide(a, b):
    try:
        if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
            raise TypeError("Only numbers allowed")
        z = a/b
    except ZeroDivisionError as ze:
        print(f"Error: {ze}. Cannot divide by zero")
    except TypeError as te:
        print(f"Error: {te}.")
    else:
        print(f"Division successful without any exception: {z}")
    finally:
        print("Operation Completed")

divide(10, 2)
# 5

divide(10, 0)
# Cannot divide by zero

divide(10, "2")
# Invalid datatype