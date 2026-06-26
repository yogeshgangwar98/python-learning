# Measure execution time of the function

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
    return wrapper

@measure_time
def process():
    time.sleep(4)

process()

