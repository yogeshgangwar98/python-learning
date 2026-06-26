# Decorator to demostrate functools

from functools import wraps

def add_stars(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("********")
        print(func(*args, **kwargs))
        print("********")
    return wrapper

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@add_stars
@uppercase
def greet():
    return "hello"
print(greet.__name__)
greet()