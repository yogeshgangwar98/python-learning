def natural_numbers():
    num = 1 
    while True:
        yield num
        num += 1

g = natural_numbers()
for _ in range(10):
    print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
