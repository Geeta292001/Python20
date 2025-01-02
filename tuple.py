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