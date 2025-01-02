# An iterator is an object in Python that implements the __iter__() and __next__() methods.
# It allows you to traverse through all the elements in a collection (like a list or tuple) one at a time without needing to know the underlying structure.
# Iterable: An object capable of returning an iterator, such as lists, tuples, dictionaries, sets, and strings.
# It must implement the __iter__() method.
#Iterator: An object with a __next__() method that returns the next element in the sequence or raises StopIteration when there are no more items.
# Creating an iterator from a list
my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# Raises StopIteration error if called again

#ADVANTAGES
#Lazy Evaluation:
#Iterators do not compute all values at once, which is memory efficient for large data structures.
#Memory Efficiency:
#Since iterators generate elements one at a time, they are suitable for processing streams of data or infinite sequences.
#Simplified Loops:
#Using for loops with iterators abstracts the complexity of manually handling indices.
#Supports Infinite Data Streams:
#Iterators can be used to represent infinite sequences like those from the range() function or custom generators.
#Reusability:
#Iterator protocols are standard, so custom iterators integrate seamlessly with Python's iteration constructs.

#DISADVANTAGES
#One-Time Use:
#Once an iterator is exhausted (i.e., all elements are traversed), it cannot be reused. You need to recreate it if necessary.
#No Random Access:
#Unlike lists or arrays, iterators do not support indexing or slicing.
#Error Handling:
#Manually calling next() on an iterator raises a StopIteration error when the sequence ends, which must be handled explicitly.
#Debugging Challenges:
#Since iterators are consumed one element at a time, debugging issues related to them can be tricky.

#DISADVANTAGES
#No Random Access:
#Unlike lists or arrays, iterators do not support indexing or slicing.
#Error Handling:
#Manually calling next() on an iterator raises a StopIteration error when the sequence ends, which must be handled explicitly.
#Debugging Challenges:
#Since iterators are consumed one element at a time, debugging issues related to them can be tricky.

#USE CASES
#Data Streaming:
#Reading large files line-by-line using file objects (which are iterators).
#Processing Large Datasets:
#Iterators are ideal for datasets that are too large to fit into memory.
#Custom Data Structures:
#Create iterators to define custom traversal logic for complex data structures.


# EXAMPLES 2:

import itertools

counter = itertools.count(start=1, step=2)  # Infinite odd numbers
for _ in range(5):
   print(next(counter))  # Output: 1, 3, 5, 7, 9

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












#