# A Timer to check the execution time
import time

class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Execution time: {time.time() - self.start:.4f}")

with Timer():
    time.sleep(2)