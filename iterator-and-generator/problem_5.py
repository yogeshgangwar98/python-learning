# Iterator uses more code
class NumberIterator:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= self.number:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
number = NumberIterator(10)
for num in number:
    print(num)

# Same functionality with generator uses less code
def number_generator(n):
    for i in range(1, n+1):
        yield i
numbers = number_generator(5)
for i in numbers:
    print(i)


'''
1. Which requires less code?

Your Answer: Generator requires less code.

Interview Answer:

Generators require less code because Python automatically creates the iterator logic. We only need to write a function with yield, whereas a custom iterator requires implementing __iter__() and __next__() manually.

2. Which manages state automatically?

Your Answer: Generator manages state automatically.

Interview Answer:

Generators automatically preserve their execution state, local variables, and current position between yield statements. In a custom iterator, we must explicitly manage state using instance variables.

3. Which is easier to maintain?

Your Answer: Generator is easy to maintain.

Interview Answer:

Generators are usually easier to maintain because the code is shorter, more readable, and requires less boilerplate. Changes to iteration logic can often be made in a few lines.

4. Is every generator an iterator?

Your Answer: Yes every generator is iterator.

Interview Answer:

Yes. Every generator is an iterator because generator objects implement both __iter__() and __next__().

Example:

g = (x for x in range(5))

print(hasattr(g, "__iter__"))  # True
print(hasattr(g, "__next__"))  # True
5. Is every iterator a generator?

Your Answer: No every iterator cannot be generator.

Slight wording correction:

❌ "Every iterator cannot be generator"

✅ "No, every iterator is not a generator."

Interview Answer:

No. A generator is a special type of iterator created using yield. Custom iterator classes that implement __iter__() and __next__() are iterators but not generators.

Example:

class Counter:
    def __iter__(self):
        return self

    def __next__(self):
        ...

This is an iterator but not a generator.
'''