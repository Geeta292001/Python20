# GENERATORS:
#         Generators are a way to create iterators in Python using functions and the yield keyword.
#         They allow you to generate values one at a time as needed, rather than computing and storing all values in memory upfront.
#
# ADVANTAGES:
#
#         Memory Efficient:
#                        They don’t store the entire sequence in memory; instead, they yield items one at a time.
#         Lazy Evaluation:
#                        Values are computed only when needed, which can improve performance for large datasets.
#         Readable Code:
#                        Simplifies implementation of iterators.
#
#
# DISADVANTAGES:
#
#         Single Iteration:
#                 Generators can only be iterated once. To re-iterate, you need to create a new generator.
#         Debugging:
#                 Difficult to debug as the state is not stored explicitly.
#         Limited Access:
#                 Cannot access elements by index or use slicing.



# USE CASES:
#         Reading large files line by line.
#         Generating infinite sequences (e.g., Fibonacci numbers).
#         Streaming data processing.


# EXAMPLES:

# def generate_numbers(n):
#     for i in range(n):
#         yield i
#
# # Usage
# for number in generate_numbers(5):
#     print(number)


# EXAMPLE 2:
#
# def infinite_counter():
#     count = 0
#     while True:
#         yield count
#         count += 1
#
# # Usage
# counter = infinite_counter()
# for _ in range(6):
#     print(next(counter))









                                                                 # ITERATORS

# ITERATORS:
#        An iterator is an object that allows traversal through all the elements of a collection (e.g., list, tuple) one at a time, without needing to use indexing.
#        It implements the __iter__() and __next__() methods.
#
# ADVANTAGES:
#         Memory Efficiency:
#                        They do not store the entire data in memory; instead, they generate items on the fly.
#         Lazy Evaluation:
#                        Useful for handling large datasets or infinite sequences without loading everything at once.
#         Improves Code Readability:
#                        Simplifies looping through data structures.
#
# DISADVANTAGES:
#
#         One-Time Use:
#                  Once traversed, they cannot be reused without reinitializing.
#         Lack of Indexing:
#                  Cannot directly access elements using indices.
#         Debugging Challenges:
#                  Traversing can make debugging more complex.
#
#
#
# EXAMPLES:


# my_list = [1, 2, 3, 4]
# iterator = iter(my_list)
#
# print(next(iterator))  # Output: 1
# print(next(iterator))  # Output: 2



# EXAMPLES 2:

# import itertools
#
# counter = itertools.count(start=1, step=2)  # Infinite odd numbers
# for _ in range(5):
#     print(next(counter))  # Output: 1, 3, 5, 7, 9













