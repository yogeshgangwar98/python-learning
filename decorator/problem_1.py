# Logging a function call

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args,**kwargs)
        print("Function executed")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

print(add(10, 20))