#                                                           LIST COMPREHENSION
#
# LIST COMPREHENSION:
#             List comprehension is a concise way to create lists in Python.
#             It allows for generating a new list by applying an expression to each element of an iterable.
#
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
from multiprocessing.pool import worker

from Tools.scripts.var_access_benchmark import trials

# Syntax:
#
# [expression for item in iterable if condition]

# EXAMPLES 1 :

# numbers = [x for x in range(6)]
# print(numbers)
# # Output: [1, 2, 3, 4, 5]



# EXAMPLE 2:
# squares = [x**2 for x in range(6)]
# print(squares)

#EXAMPLE 3:
# thriple =[x**3 for x in range(6)]
# print(thriple)

# # EXAMPLE 4:
# x=[1,2,3,4,5,6,7,8,9,10]
# greaterthan = [x for x in x if x>6]
# print(greaterthan)


# # EXAMPLE 5:
# x=[1,2,3,4,5,6,7,8,9,10]
# lessthan = [x for x in x if x<6]
# print(lessthan)


# EXAMPLE 6:
# x=[1,2,3,4,5,6,7,8,9,10]
# greaterthan_squares = [x**2 for x in x if x>6]
# print(greaterthan_squares)


# EXAMPLE 7:
# x=[1,2,3,4,5,6,7,8,9,10]
# lessthan_squares = [x**2 for x in x if x<6]
# print(lessthan_squares)

# EXAMPLES 8:
# s=[x for x in range(1,10) if x%2!=0]
# print(s)

# EXAMPLE 9:
# s=[x for x in range(1,10) if x%2==0]
# print(s)

# EXAMPLE 10:
# words=["pothuraju","satya","sai","krishna"]
# uppercase_name = [word.upper() for word in words]
# print(uppercase_name)

# EXAMPLE 11:
# words=["POTHURAJU","SATYA","SAI","KRISHNA"]
# lowercase_name = [word.lower() for word in words]
# print(lowercase_name)

# EXAMPLE 12:
# len_greaterthan = ["satya","sai","krishna","pothuraju"]
# s=[word for word in len_greaterthan if len(word) > 4 ]
# print(s)

# EXAMPLE 13:
# len_lessthan = ["satya","sai","krishna","pothuraju"]
# s=[word for word in len_lessthan if len(word) < 4 ]
# print(s)

# EXAMPLE 14:
# squares = [(x,x**2) for x in range(1,6)]
# print(squares)

# #EXAMPLE 15:
# numericss = [1,"a",2,"b",3,"c"]
# s=[x for x in numericss if isinstance(x,int)]
# print(s)

# EXAMPLE 16:
# matrix = [[1,2],[3,4],[5,6]]
# transpose = [[row[i] for row in matrix] for i in range(2)]
# print(transpose)

#EXAMPLE 17:

# s="hello"
# a=[z for z in s]
# print(a)

#EXAMPLE 18:
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# transpose = [[row[i] for row in matrix] for i in range(3)]
# print(transpose)

#EXAMPLE 19:

# a= [1,2,5]
# b= [4,5,6]
#
# result = [a[c] * b[c] for c in range (len(a))]
# print(result)

#EXAMPLE 20:
# celsius = [0,10,20,30,40]
# fahrenheit = [(x * 9/5)+32 for x in celsius ]
# print(fahrenheit)

#EXAMPLE 21:
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [x for x in a[::-1]]
# print(b)

#EXAMPLE 22:
# a = ["satya","sai","krishna"]
# b = [x[::-1] for x in a]
# print(b)

#EXAMPLE 23:
# matrix = [[1, 2], [3, 4], [5, 6]]
# flattened = [s for a in matrix for s in a]
# # Output: [1, 2, 3, 4, 5, 6]
# print(flattened)

#EXAMPLE 24:
# a = ["satya","sai","krishna"]
# b = [c[0] for c in a]
# print(b)

# EXAMPLE 25:
# a=[x**2 for x in range(1,11) if x % 2 == 0]
# print(a)

#EXAMPLE 26:
# a=[x for x in range(1,21) if x % 3 == 0]
# print(a)

# EXAMPLE 27:
# a = [1,2,3,4,5,6,7,8,9]
# b = ["Even" if x % 2==0 else "odd" for x in a]
# print(b)

#EXAMPLE 28:
# a = [3,5,1,6,8,2,9,7]
# b = sorted(a)
# print(b)

#EXAMPLE 29:
# a = [3,6,9,8,5,2,1,4,7]
# b = sorted(a,reverse=False)
# print(b)

# EXAMPLE 30:
# def squares(x):
#     return x**2
#
# n = [1,2,3,4,5]
# b = [squares(x) for x in n]
# print(b)

#EXAMPLE 31:
# def is_even(x):
#     return x%2==0
#
# f = [x for x in range(1,11) if is_even(x)]
# print(f)

# EXAMPLE 32:
# def case(x):
#     return x.upper()
#
# n = ["satya","sai","krishna"]
# m = [case(a) for a in n]
# print(m)

# EXAMPLE 33:
# def multi(x):
#     return a * b
#
# a = [1,2,3]
# b = [4,5,6]
#
# d = [a[i]*b[i] for i in range(len(a))]
# print(d)

# # EXAMPLE 34:
# def has_length(word,length):
#     return len(word) == length
#
# a = ["ab","sai","satya","shankar","krishna"]
# b = [word for word in a if has_length(word,7)]
# print(b)

# EXAMPLE 35:
# def is_reverse(x):
#     return x[::-1]
#
# words = ["satya","shankar","gowtham"]
# c = [is_reverse(word) for word in words]
# print(c)

#EXAMPLE 36:
# def celius_to_fahrenheit(x):
#     return (x * 9/5)+32
#
# a = [0,20,40,100]
# b = [celius_to_fahrenheit(x)  for x in a]
# print(b)

#EXAMPLE 37:
# def absolute_value(x):
#     return abs(x)
#
# c = [1,2,3,-4,-5,-7,-9]
# d = [absolute_value(x) for x in c]
# print(d)

#EXAMPLE 38:
# def changin(name):
#     return f"Mr.{name}"
#
# d = ["satya","sai","krishna"]
# e = [changin(name) for name in d]
# print(e)

#  EXAMPLE 39:
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# primes = [x for x in range(1,100) if is_prime(x)]
# print(primes)
# # Output: [2, 3, 5, 7, 11, 13, 17, 19]
