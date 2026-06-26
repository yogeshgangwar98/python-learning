numbers = range(1,21)

evens = (x for x in numbers if x%2==0)
squares = (x**2 for x in evens)

for number in squares:
    print(number)