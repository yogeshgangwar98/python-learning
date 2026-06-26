# Decorator with arguments

def repeat(n):
    def inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return inner

@repeat(3)
def hello():
    print("Hello")

hello()