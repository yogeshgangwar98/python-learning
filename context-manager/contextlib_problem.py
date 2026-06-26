from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()  # this is treated as __enter__
    try:
        yield # this is the where the operation in with is working
    finally:
        print(time.perf_counter() - start) # this is the __exit__ operation

with timer():
    time.sleep(2)
'''
Whole point is that contextlib gives you a privilage to create a context manager with a geneator that has less code __enter__ -> yield -> __exit__
'''