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