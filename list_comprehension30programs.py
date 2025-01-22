#Flattend a nested list
nested_list = [[1,2,3],[4,5],[6,7,8],[9,10]]
#List comprehension to flatten the list
flattened = [num for sublist in nested_list for num in sublist]
print("Flattened list:", flattened)
#OUTPUT: Flattened list: [1,2,3,4,5,6,7,8,9,10]

nested_list =[[1,2,3],[4,5],6,7]  #The element 6 and 7 are integer, not a list so Python raises the error because for num in sublist attempts to iterate over it.
#Add a condition to handle non-iterable elements
flattened = [num for sublist in nested_list if isinstance(sublist, (list,tuple)) #This ensures that only lists or tuples within nested_list are processed.
 for num in sublist]
print("flattened list:", flattened)
#OUTPUT: flattened list: [1,2,3,4,5]

#Flatten a Nested list with conditions
nest_list = [[1,2,3],[4,5,6],[7,8,9]]
flatten = [num for sublist in nest_list for num in sublist if num % 2 ==0]
print("Flattened even list:",flatten)
#OUTPUT: Flattened even list: [2,4,6,8]

#Filter Even numbers
numbers = [10,22,24,25,37,39,40,80,50,60,79]
#List Comprehension to get even numbers
even_numbers = [num for num in numbers if num % 2 ==0]
print("Even Numbers:", even_numbers)
#OUTPUT: Even Numbers: [10,22,24,40,80,50,60]

#Numbers divisible by both 3 and 5
#list comprehension to find numbers divisible by 3 and 5
divisible_by_3_and_5 = [num for num in range(1,100) if num % 3 == 0 and num % 5 == 0]
print("The Numbers Divisible by 3 and 5: ",divisible_by_3_and_5)
#OUTPUT:The Numbers Divisible by 3 and 5: [15,30,45,60,75,90]

#Numbers divisible by 5 and not divisible by 7
numbers = [num for num in range(1,100) if num % 5 == 0 and num % 7 != 0]
print("The numbers divisible by 5 and not divisible by 7:", numbers)
#OUTPUT: The numbers divisible by 5 and not divisible by 7: [5,10,15,20,30,45,50,55,60,65,70,75,80,85,90,95]

#Cartesian Product
list1 = [1,2,3]
list2 = ['A','B','C']
#Cartesian Product using list comprehension
cartesian_product = [(x,y) for x in list1 for y in list2]
print("Cartesian Product:", cartesian_product)
#OUTPUT: Cartesian Product: [(1,'A'),(1,'B'),(1,'C'),(2,'A'),(2,'B'),(2,'C'),(3,'A'),(3,'B'),(3,'C')]

#Prime Numbers
#Check if a number is prime or not using list comprehension
prime_numbers = [num for num in range(2,50) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]
print("Prime Numbers:", prime_numbers)
#OUTPUT: Prime Numbers: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

#Transpose a Matrix
#given matrix
matrix =[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
#Transpose using list comprehension
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transposed Matrix:",transposed)
#OUTPUT: Transposed Matrix: [[1,4,7],[2,5,8],[3,6,9]]

#Conditional Transformation
#List with Negative Numbers
numbers = [-1,9,-2,8,-3,-4,7,6,-5]
#Replace negative with 0
non_negative = [num if num >= 0 else 0 for num in numbers]
print("Non-Negative List:",non_negative)
#OUTPUT: Non_Negative List: [0,9,0,8,0,0,7,6,0]

#Nested Conditions
#List of numbers
numbers = [0,1,2,4,5,6,7,8]
#Classification using nested conditions
classification = ["Even" if num % 2 == 0 and num != 0 else "Odd" if num % 2 != 0 else "zero" for num in numbers]
print("Number Classification:", classification)
#OUTPUT: Number Classification: ['zero','Odd','Even','Even','Odd','Even','Odd','Even']

#Convert strings to integers
#List of mixed strings
data = ["A1","B2","C3","D4"]
#Extract and Convert numeric parts
numbers = [int(item[1]) for item in data]
print("Extracted Numbers:",numbers)

#Generating pythagorean triples
triples = [(a,b,c) for a in range(1,21) for b in range(a,21) for c in range(b,21) if a**2 + b**2 == c**2]
print("Pythagorean Triples:",triples)
#OUTPUT: [(3,4,5),(5,12,13),(6,8,10),(8,15,17),(9,12,15),(12,16,20)]

#Count Vowels in words
words = ["Arjun","Geeta","Arya","Radha","Krishna","Rajesh","Tharuna"]
#count vowels in each word
vowel_count = [{word: sum(1 for char in word if char in "aeiou")} for word in words]
print("vowel count in words:",vowel_count)
#OUTPUT: vowel count in words: [{'Arjun': 1}, {'Geeta': 3}, {'Arya': 1}, {'Radha': 2}, {'Krishna': 2}, {'Rajesh': 2}, {'Tharuna': 3}]

#Reverse words
names = ["lucky","cherry","crunchy"]
#reverse each word
reversed_words = [word[::-1] for word in names]
print("Reversed words:", reversed_words)
#OUTPUT: Reversed words: ['ykcul', 'yrrehc', 'yhcnurc']

# Filter Palindromes
palin_words = ["madam","hello","you","racecar","level"]
palindromes = [word for word in palin_words if word == word[::-1]]
print("Filter Palindromes:",palindromes)
#OUTPUT: Filter Palindromes: ['madam', 'racecar', 'level']

#Convert Temperature
#list of temperatures in Celsius
Celsius = [0,20,30,40]
#convert to Fahrenheit
fahrenheit = [(temp * 9/5) +32 for temp in Celsius]
print("Temperatures in Fahrenheit:", fahrenheit)
#OUTPUT: Temperatures in Fahrenheit: [32.0,68.0,86.0,104.0]

#Fibonacci Sequence
fib = [0,1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print("First 10 fibonacci sequence:",fib)
#OUTPUT: First 10 fibonacci sequence: [0,1,1,2,3,5,8,13,21,34]

#calculate the square of numbers
nums = range(1,1001)
squares = [x**2 for x in nums]
print("Squares of numbers:",squares)

#Cleaning and Formatting data
data = ["Hello","World"," ","Python ","is great",""]
cleaned_data = [item.strip().lower() for item in data if item.strip()]
print("Cleaned data:",cleaned_data)
#OUTPUT: Cleaned data: ['hello','world','python','is great']

#Generating Combinations
colors = ["red","blue"]
sizes = ["small","medium","large"]
combinations = [(color,size) for color in colors for size in sizes]
print("Combinations:",combinations)

#Filtering Log Files
logs = [
 "INFO: Server Started",
 "ERROR: Unable to connect to database",
 "INFO: Request received",
 "ERROR: Timeout occurred"
]
errors = [log for log in logs if "ERROR" in log]
print("Errors:",errors)
#OUTPUT: Errors: ['ERROR: Unable to connect to database', 'ERROR: Timeout occurred']

#Using a loop
result = []
for i in range(10):
    result.append(i**2)
print(result)

#Using list Comprehension
result=[i**2 for i in range(10)]
print(result)