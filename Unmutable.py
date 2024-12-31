# SET :
#    A set is an unorderd collection of unique elements .
#    It do not allow dupicant elements and are commnly used for mathematical set operarions like union, intersection and difference.
#    It is defined using curly braces { } or the set( ) function.
#
#
# ADVANTAGES OF SET :
#
#             Unique Elements:
#                        Sets automatically remove duplicates, ensuring each element is unique.
#             Fast Membership Tests:
#                        Checking whether an element exists in a set is faster (O(1)) compared to lists.
#             Dynamic:
#                        Sets are mutable, so you can add or remove elements after creation.
#
# DISADVANTAGES OF SET:
#
#             Unordered:
#                     The elements in a set are unordered, so indexing and slicing are not possible.
#             Immutable Elements:
#                     Sets can only store hashable (immutable) elements like numbers, strings, and tuples, but not lists or dictionaries.
#             Memory Usage:
#                     Sets may use more memory compared to lists for storing the same number of elements.
#
#
#     EXAMPLES:
#
# Create a set
# numbers = {1, 2, 3, 4, 4, 5}
# print(numbers)  # Output: {1, 2, 3, 4, 5}




# Define two sets
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
#
# # Union
# print(set_a | set_b)  # Output: {1, 2, 3, 4, 5, 6}
#
# # Intersection
# print(set_a & set_b)  # Output: {3, 4}
#
# # Difference
# print(set_a - set_b)  # Output: {1, 2}


# TUPLE:
#
#      A tuple is a collection of ordered, immutable elements.
#      It is similar to list, but tuples cannot be modified after creation.
#      It is defined by enclosing elements in parentheses().
#
#
#
# ADVANTAGES OF TUPLE:
#                 Immutability:
#                          Once created, the elements of a tuple cannot be changed, which ensures data integrity.
#                 Faster than Lists:
#                          Operations on tuples are faster compared to lists, making them suitable for read-only operations.
#                 Can be Used as Keys:
#                          Tuples can be used as keys in dictionaries because they are hashable (unlike lists).
#                 Memory Efficient:
#                          Tuples consume less memory compared to lists.
#
#
# DISADVANTAGES OF TUPLE:
#                 Immutable:
#                        The immutability can be a disadvantage if you need to modify the data.
#                 Limited Functionality:
#                        Tuples lack some of the methods available to lists, such as .append() or .remove().

# EXAMPLES:


# Creating a tuple
# my_tuple = (10, 20, 30, 40)
#
# # Accessing elements
# print(my_tuple[0])  # Output: 10
# print(my_tuple[-1]) # Output: 40



# Using tuple as a key in a dictionary
coordinates = {
    (10.5, 20.3): "Point A",
    (15.2, 25.6): "Point B"
}

# Accessing value using tuple key
print(coordinates[(15.2, 25.6)])  # Output: "Point A"

