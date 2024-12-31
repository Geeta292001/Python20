#LIST
#A list in Python is a mutable, ordered collection of elements.
# Lists can hold items of any data type, including other lists, and allow duplicate values.
# They are created using square brackets [] or the list() constructor.
#ADVANTAGES
#Lists are dynamic: they can grow or shrink as needed, without the need to declare a fixed size.
#A list can hold different types of data (e.g., integers, strings, floats, etc.) in the same collection.
#Lists are easy to use for simple tasks like storing and accessing collections of items.
#Python lists have numerous built-in methods for manipulation, sorting, filtering, and more.
#Supports efficient indexing and slicing to access subparts of the list.
#Elements of a list can be updated or modified.
#DISADVANTAGES
#Lists consume more memory as they store references to the actual objects, not the objects themselves.
#Operations on lists can be slower compared to low-level arrays due to their dynamic and heterogeneous nature.
#Performance can degrade for large datasets since Python lists are not optimized for mathematical operations like NumPy arrays.
#While lists can store mixed data types, this can lead to errors or unexpected results if not handled carefully.
from typing import Tuple

fruits=['Apple','Banana','Pineapple','Custard Apple','Mango','kiwi']
print(fruits)
fruits.append('Orange')
print(fruits)
fruits.remove('kiwi')
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.extend('Leechi'.split(','))
print(fruits)
fruits2=['Strawberry','Guava','Blueberry']
fruits.extend(fruits2)
print(fruits)
fruits.insert(5,'Dragon fruit')
print(fruits)


#TUPLE
#A tuple in Python is an immutable, ordered collection of elements.
# Tuples can hold multiple items of various data types, and their immutability means their elements cannot be changed, added, or removed after creation.
#ADVANTAGES
#Ensures data integrity by preventing accidental modification.
#Makes tuples hashable, so they can be used as keys in dictionaries.
#Tuples are faster than lists due to their immutability and smaller memory footprint.
#Ideal for representing fixed collections of items (e.g., coordinates, database records).
#Can store different types of data, such as integers, strings, and booleans.
#Similar to lists but with added immutability, making them simple yet effective for certain tasks.
#DISADVANTAGES
#Cannot be modified (elements cannot be added, updated, or removed).
#If modifications are required, the tuple must be converted to a list and back.
#Fewer built-in methods compared to lists (e.g., no append, remove, or pop).
#Not suitable for scenarios where frequent updates to the data are needed.


things=('box','pen','ball','duster','pencil','books')
print(things)
print(things.count('pencil'))
print(things.index('ball'))
print(things[3])


# SET :
#    A set is an unorderd collection of unique elements .
#    It do not allow dupicant elements and are commnly used for mathematical set operarions like union, intersection and difference.
#    It is defined using curly braces { } or the set( ) function.
#
#
# ADVANTAGES OF SET :
#
# Sets automatically remove duplicates, ensuring each element is unique.
# Checking whether an element exists in a set is faster (O(1)) compared to lists.
# Sets are mutable, so you can add or remove elements after creation.
#
# DISADVANTAGES OF SET:
#
# The elements in a set are unordered, so indexing and slicing are not possible.
# Sets can only store hashable (immutable) elements like numbers, strings, and tuples, but not lists or dictionaries.
# Sets may use more memory compared to lists for storing the same number of elements.
colors={'Red','Yellow','Blue','Green'}
print(colors)
print('Yellow' in colors)
for x in colors:
    print(x)
