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

