class EvenNumbers:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        self.even  = 2
        return self
    
    def __next__(self):
        if self.even <= self.number:
            x = self.even
            self.even += 2
            return x
        else:
            raise StopIteration
        
even = EvenNumbers(10)

myiter = iter(even)

for i in range(20):
    print(next(myiter))