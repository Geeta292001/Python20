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
