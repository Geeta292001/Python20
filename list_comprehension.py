#LIST COMPREHENSION
#List_comprehension is a concise and elegant way to create lists in Python by embedding a for-loop and optional conditions within square brackets.
# It allows for the transformation and filtering of items from an iterable in a single line of code.


#Advantages of List Comprehension
#Conciseness:
#Reduces the number of lines of code compared to traditional for-loops.
#Makes code cleaner and easier to read.
#Performance:
#Often faster than equivalent for-loops because they are optimized in Python.
#Readability:
#Provides a clear, declarative way to generate new lists.
#Flexibility:
#Can include conditions (if) to filter items directly during list creation.


#Disadvantages of List Comprehension
#Complexity in Long Expressions:
#If the logic becomes too complex, it may reduce readability and be hard to debug.
#Memory Usage:
#Generates the entire list in memory, which can be inefficient for very large datasets.
#Limited to List Creation:
#While powerful for lists, they are less versatile compared to general for-loops for tasks other than creating lists.
#Not Always Self-Explanatory:
#For beginners, the concise syntax can sometimes be difficult to understand.

#Use Cases of List Comprehension
#Creating a List of Squares:
squares=[x**2 for x in range(10)]
print(squares)

#Filtering Even Numbers:
even_numbers=[x for x in range(50) if x % 2 == 0]
print(even_numbers)

#Transforming Strings:
uppercase=[word.upper() for word in["geeta","bandela"]]
print(uppercase)

lowercase=[word.lower() for word in["RADHA","PALLIKELLA"]]
print(lowercase)

#Flattening a Nested List:
nested_list=[[1,2,3],[4,5,6],[7,8]]
flat_list=[num for sublist in nested_list for num in sublist]
print(flat_list)

#Generating a List of Tuples:
pairs=[(x,y) for x in range(3) for y in range(3)]
print(pairs)

points=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(points)

#Examples:
#Filter Odd Numbers
odd_numbers=[x for x in range(10) if x % 2 != 0]
print(odd_numbers)

#Transform Numbers into Strings
number_string=[str(x) for x in range(10)]
print(number_string)

#Conditional List Comprehension
result=["even" if x % 2 == 0 else "odd" for x in range(10)]
print(result)

#Reverse Strings in a list
reversed_string=[word[::-1] for word in ['apple','banana','orange']]
print(reversed_string)

#Replace Negatives with zero
numbers=[-1,-2,3,4,-5,-6,-7,8,9]
replaced=[x if x > 0 else 0 for x in numbers]
print(replaced)

#Create Multiplication Table
table=[f"{i} x {j} = {i * j}" for i in range(1,6) for j in range(1,6)]
print(table)

#Create list of Prime Numbers
primes=[x for x in range(2,50) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]
print(primes)

#Key Value Pair Conversion
keys=["Name","Age","City"]
values=["Raj",24,"AMP"]
dictionary={k: v for k, v in zip(keys,values)}
print(dictionary)

#Count  Word Occurrences
text="Samira is beautiful and samira speaks english very well"
word_count={word:text.split().count(word) for word in text.split()}
print(word_count)
