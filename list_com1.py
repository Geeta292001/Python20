# Advantages of List Comprehensions in Python:
# Concise Code: Reduces the need for multiple lines of code, making it more compact and readable.
# Faster Execution: List comprehensions are generally faster than traditional loops for creating lists due to internal optimizations.
# Readability: Makes the code more expressive and easier to understand at a glance, especially for simple transformations.
# Inline Filtering and Transformation: Allows filtering and transforming elements in a single line.
# Disadvantages of List Comprehensions in Python:
# Complexity with Nested Comprehensions: Can become hard to read and maintain with nested list comprehensions or complex logic.
# Memory Consumption: Creates the entire list in memory, which could be problematic for large datasets (use generators for large datasets).
# Overuse Can Decrease Clarity: If overused or used for complex logic, it can make the code less readable.
# Use
# CasesofListComprehensions in Python:
# Creating Lists: For creating new lists by applying expressions to an existing iterable.
#
# x=[2,4,5,6,6,8,9,98,90]
# squares = [x**2 for x in range(10)]
# Filtering Items: Filter items based on a condition.
# even_numbers = [x for x in range(10) if x % 2 == 0]
# Flattening Nested Lists: Flatten a list of lists into a single list.
# nested_list = [[1, 2], [3, 4], [5]]
# flattened = [item for sublist in nested_list for item in sublist]
# Applying Functions: Apply a function to each element of the iterable
# names = ["alice", "bob", "charlie"]
# capitalized_names = [name.upper() for name in names]  # Capitalize each name
# Combining Two Lists: Combining elements from multiple lists (zip).
# names = ['Alice', 'Bob', 'Charlie']
# scores = [85, 92, 78]
# combined = [f"{name}: {score}" for name, score in zip(names, scores)]
# Methods in List Comprehensions:
# Expression: Defines what to do with each item in the iterable (e.g., x**2, x.upper()).
# Iterable: The collection (list, range, etc.) being iterated over.
# Cond
#                                                           LIST COMPREHENSION
#
# LIST COMPREHENSION:
#             List comprehension is a concise way to create lists in Python.
#             It allows for generating a new list by applying an expression to each element of an iterable.
#
# Syntax:
#
# [expression for item in iterable if condition]
#
# Advantages:
#         Concise and Readable:
#                           Reduces the code length compared to traditional loops.
#         Faster Execution:
#                           More efficient than for loops for simple operations.
#         Easy to Write:
#                           Simplifies list creation logic.
#
# Disadvantages:
#         Complexity:
#                   Can become hard to read with nested comprehensions.
#         Memory Usage:
#                   Consumes more memory for large datasets compared to generators.
#
# USE CASES:
#         Filtering elements from a list.
#         Applying transformations to elements.
#         Flattening nested lists.


# EXAMPLES 1 :


# numbers = [1, 2, 3, 4, 5, 6]
# evens = [x for x in numbers if x % 2 == 0]
# print(evens)  # Output: [2, 4, 6]



# EXAMPLE 2:


# squares = [x**2 for x in range(1, 6)]
# print(squares)  # Output: [1, 4, 9, 16, 25]





#                                                      DICT COMPREHENSION
#
#
# DICT COMPREHENSION:
# A dict comprehension is a concise way to create dictionaries in Python by generating key-value pairs from an iterable or another dictionary in a single line of code.
#
# ADVANTAGES:
#             Conciseness:
#                      Reduces the need for verbose loops.
#             Performance:
#                      Often faster than traditional loops.
#             Readability:
#                      Easy to understand for simple operations.
#
# DISADVANTAGES:
#
#             Complexity:
#             Can become hard to read with complex logic.
#             Debugging:
#             Difficult to debug compared to a traditional loop.
#
# USE CASES:
#             Transforming or filtering an existing dictionary.
#             Creating dictionaries from other iterables (e.g., lists, sets).
#             Inverting keys and values of a dictionary.
#
#
#
# EXAMPLES 1:

# # Original dictionary
# prices = {'apple': 100, 'banana': 30, 'cherry': 150}
#
# # Comprehension: Filter items with price > 50
# filtered_prices = {key: value for key, value in prices.items() if value > 50}
# print(filtered_prices)  # Output: {'apple': 100, 'cherry': 150}



# EXAMPLE 2:

# List of numbers
# numbers = [1, 2, 3, 4, 5]
#
# # Comprehension: Square of each number as value
# squared_dict = {num: num ** 2 for num in numbers}
# print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}