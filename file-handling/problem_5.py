from constants import BASE_URL
from collections import deque
def tail(filename, lines):
    with open(filename,"r") as file:
        return list(deque((line.strip() for line in file), maxlen = lines))

print(tail(BASE_URL+"tail.txt", 4))