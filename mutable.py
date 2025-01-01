# LIST :
#        A list is a mutable, and allow duplicate elements.
#        It is a ordered collection of elements that can store items of different data types.
#        It is defined by square
#        EXAMPLE:
#               [1,2,20.12,"Apple",66.44]
#
#
# ADVANTAGES OF LIST:
#
#      Versatility
#               They can store heterogeneous data types  (sring,interger,etc.)
#      Dynamic Size
#               List can grow shrink dynamically without requring a fixed size.
#
# DISADVANTAGES OF LIST:
#
#     Memory Overhead
#               Lists consume more memory as they store additional metadata like type inforamtion and size.
#     Slower for some operation
#               Accessing and modifying elements can be slower compared to arrays in other languages due to dynamic typing.
#
#     EXAMPLES:

# # Create a list of mixed data types
# my_list = [10, "Python", 3.14, True]
#
# # Access elements using indexing
# print(my_list[0])  # Output: 10
# print(my_list[-1]) # Output: True



# # Create a list of numbers
# numbers = [1, 2, 3, 4, 5]
#
# # Add an element to the list
# numbers.append(6)  # List becomes [1, 2, 3, 4, 5, 6]
#
# # Remove an element
# numbers.remove(3)  # List becomes [1, 2, 4, 5, 6]
#
# # Sort the list
# numbers.sort()  # List becomes [1, 2, 4, 5, 6]
#
# print(numbers)







# DICTIONARY:
#          A dictionary is an unorderd, mutable collection of key-value pairs.
#          Each key is unique and it maps to a value.
#          Dictionaries are defines by curly braces { } and use a colon : to seperate keys and values.
#
# ADVANTAGES OF DICTIONARY :
#          Fast Lookups:
#                      Accessing data by key is fast due to the underlying hash table implementation.
#          Flexible Key Types:
#                      Keys can be of various immutable types (e.g., strings, numbers, tuples)
#
#
# DISADVANTAGES OF DICTIONARY:
#         Memory Usage:
#                      Dictionaries consume more memory due to their hash table structure.
#         Unordered:
#                      Until Python 3.7 (where insertion order is preserved as an implementation detail), dictionaries were unordered collections.
#         Not Suitable for Large Sorted Data:
#                      Inefficient for tasks requiring ordered data or sequential access.
#
# EXAMPLES:

# Dictionary to store student information
# student = {
#     "name": "John Doe",
#     "age": 20,
#     "grades": [88, 92, 95]
# }
#
# # Accessing data
# print(f"Name: {student['name']}")
# print(f"Grades: {student['grades']}")




# Word frequency counter using a dictionary
text = "hello world hello python"
word_counts = {}

for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
