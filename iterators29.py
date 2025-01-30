# An Iterator in Python is an object that holds a sequence of values and provide sequential traversal through a collection of items such as lists, tuples, and dictionaries.
# The python iterators object is initialized using iter() method. It uses the next() method for iteration.
# __iter__() method initializes and returns the iterator object itself.
# __next__() method retrieves the next available item, throwing a StopIteration exception when no more items are not available.
#Creating an Iterator:
#Define a class: Start by defining a class that will act as the iterator.
#Initialize Attributes: In the __init__ method of the class, initialize any required attributes that will be used through out the iteration process.
#Implement __iter__(): This method should return the iterator object itself. This is usually as simple as returning self.
#Implement __next__(): This method should provide the next item in the sequence each time it's called.
class EvenNumbers:
    def __iter__(self):
        self.n = 2  # Start from the first even number
        return self

    def __next__(self):
        x = self.n
        self.n += 2  # Increment by 2 to get the next even number
        return x

# Create an instance of EvenNumbers
even = EvenNumbers()
it = iter(even)

# Print the first five even numbers
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#Why use iterators instead of loops?
#Iterators are Memory Efficient Loops store the entire collection in memory, while iterators fetch data only when needed.
#Example:Using Loop (Consumes more Memory)
numbers = [i for i in range(1000)]
for num in numbers:
    print(num)
#Example: Using Iterator(Consumes Less Memory)
def num_generator():
    num = 0
    while num < 1000:
        yield num
        num += 1
for num in num_generator():
    print(num)

#Solution: The 'yield' statement creates an iterator, generating one number at a time instead of storing all in memory.

#Ierators Work on Infinite Sequences Loops can't handle infinite sequences since they store values, but iterators generate values indefinitely.
#Example: Infinite Fibonacci Sequence
class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        num = self.a
        self.a, self.b = self.b, self.a + self.b
        return num
fib = Fibonacci()
for i in range(15):
    print(next(fib))

#No need to store infinite numbers, just generate when needed

#Iterators Can Process large files Efficiently.
#Example: reading a large log file
# def read_large_files(filename):
#     with open (filename, 'r') as file:
#         for line in file:
#             yield line.strip()
# for line in read_large_files("servers_logs.txt"):
#     print(line)

#Iterators allow Custom Iteration Logic loops iterate only over sequences, while iterators allow custom behaviour.
class StepCounter:
     def __init__(self,start,stop,step):
         self.current = start
         self.stop = stop
         self.step = step
     def __iter__(self):
         return self
     def __next__(self):
         if self.current >= self.stop:
             raise StopIteration
         value = self.current
         self.current += self.step
         return value
counter = StepCounter(1,100,2)
for num in counter:
    print(num)

#Custom Iterator:
class EvenNumbers():
    def __init__(self,max_num):
        self.max_num = max_num
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num > self.max_num:
            raise StopIteration
        result = self.num
        self.num += 2
        return result
even = EvenNumbers(20)
for num in even:
    print(num)

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


#Cycling through a list
import itertools
colors = ["Red","Green","Yellow"]
cycle_colors = itertools.cycle(colors)
for _ in range(8):
    print(next(cycle_colors))