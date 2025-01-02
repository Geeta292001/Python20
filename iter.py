#Create a Custom Iterator
class SquareIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

# Using the custom iterator
n = 3
squares = SquareIterator(n)
for square in squares:
    print(square)

# Iterator with iter() and next()
numbers=[10,20,30,40,50,60]
iterator=iter(numbers)
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("End of the list.")

#Infinite Iterator with itertools
from itertools import count
for num in count(1):
    if num > 30:
        break
    print(num)

#Chaining Iterables with itertools.chain
from itertools import chain
list1=[1,2,3,4,5]
list2=['ant','ball','cat']
list3=[True,False]
for item in chain(list1,list2,list3):
    print(item)


#Fibonacci Sequence Iterator
class FibonacciIterator:
    def __init__(self, max_terms):
        self.max_terms = max_terms
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_terms:
            self.count += 1
            current = self.a
            self.a, self.b = self.b, self.a + self.b
            return current
        else:
            raise StopIteration

# Using the Fibonacci iterator
fib = FibonacciIterator(10)

# Iterate using a loop
for num in fib:
    print(num)


#Iterating over a File
with open("sample.txt","w") as file:
    file.write(r"line1\line2\line3")
with open ("sample.txt","r") as file:
    for line in iter(file):
        print(line.strip())



#Custom Iterable Class
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

# Using the custom iterable
for number in Countdown(10):
    print(number)


