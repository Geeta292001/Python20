#GENERATORS:
#         Generators are a way to create iterators in Python using functions and the yield keyword.
#         They allow you to generate values one at a time as needed, rather than computing and storing all values in memory upfront.
#
# ADVANTAGES:
#
#         Memory Efficient:
#                        They don’t store the entire sequence in memory; instead, they yield items one at a time.
#         Lazy Evaluation:
#                        Values are computed only when needed, which can improve performance for large datasets.
#         Readable Code:
#                        Simplifies implementation of iterators.
#
#
# DISADVANTAGES:
#
#         Single Iteration:
#                 Generators can only be iterated once. To re-iterate, you need to create a new generator.
#         Debugging:
#                 Difficult to debug as the state is not stored explicitly.
#         Limited Access:
#                 Cannot access elements by index or use slicing.



# USE CASES:
#         Reading large files line by line.
#         Generating infinite sequences (e.g., Fibonacci numbers).
#         Streaming data processing.


#Basic Generator
def Square_numbers():
    for i in range(1,11):
        yield i * i
for square in Square_numbers():
    print(square)

#Fibonacci Sequence Generator
def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b,a+b
for num in fibonacci(20):
    print(num)



#Prime Number Generator
def is_prime(num):
    # Function to check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        # Check divisors from 2 to the square root of 'num' (inclusive)
        if num % i == 0:
            # If 'num' is divisible by any 'i', it's not a prime number
            return False
        return True
def prime_numbers(limit):
    # Generator function to yield prime numbers up to 'limit'
    for num in range(2, limit+1):
        # Iterate from 2 to 'limit' (inclusive)
        if is_prime(num):
            # Use the 'is_prime' function to check if 'num' is prime
            yield num
            # Yield the prime number and pause execution until the next iteration
    #Test the generator
for prime in prime_numbers(20):
    print(prime)


# File Line Reader
# Generator function to read a file line by line
def read_file(file_name):
    # Open the file in read mode
    with open(file_name, "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Yield the line after stripping leading/trailing whitespace
            yield line.strip()
# Open the file in write mode to create or overwrite 'sample.txt'
with open("sample.txt","w") as file:
    # Write sample lines into the file
    file.write("Line 1\nLine 2\nLine 3")
    # Lines are written with newline characters separating them

# Use the generator to read the file and print each line
for line in read_file("sample.txt"):
    # Iterate through lines yielded by the generator
    print(line)


#Reverse String Generator
def reverse_string(s):
    """Generates characters of a string in a reverse order"""
    for char in reversed(s): #use the built_in reversed() function to iterate backward
        yield char #yield each character
#usage
text = 'hello'
print(f"characters of '{text}' in reverse:")
for char in reverse_string(text):  #Generate and print each character in reverse order
    print(char)

#Custom Range Generator
def custom_range(start,stop,step=1):
    """Generates numbers from start to stop with a given step"""
    current = start #start from initial value
    while current < stop:  #continue until the current value reaches 'stop'
        yield current #yield the current value
        current += step  #Increment by the given step
#usage
print("Custom range from 1 to 10 with step 2:")
for num in custom_range(1,10,2): #Generates numbers from 1 to 10 with step 2
    print(num)




#Even Numbers Generator
def even_numbers(limit):
    """Generates even numbers up to a given limit."""
    for num in range(2, limit + 1, 2):  # Iterate through even numbers using a step of 2
        yield num  # Yield the current even number

# Usage
limit = 10
print(f"Even numbers up to {limit}:")
for even in even_numbers(limit):  # Generate and print even numbers up to the limit
    print(even)
