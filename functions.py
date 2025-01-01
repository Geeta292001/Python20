#A function in Python is a reusable block of code that performs a specific task.
# Functions are defined using the def keyword and can accept arguments, perform operations, and optionally return values.
#SYNTAX
#def function_name(parameters):
#   """Optional docstring"""
#      code block
#    return value  # Optional
#EXAMPLE
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

#ADVANTAGES
#Code Reusability:
#Functions can be called multiple times, reducing code duplication.
#Improved Readability and Maintainability:
#Code is easier to read, debug, and maintain when divided into smaller, modular functions.
#Encapsulation:
#Functions allow encapsulation of specific logic, hiding internal details.
#Ease of Testing:
#Functions can be tested individually to ensure correctness.
#Scalability:
#Functions enable writing scalable and modular code that can grow as requirements increase.
#Abstraction:
#Functions abstract complex operations into simple, reusable calls.


#DISADVANTAGES
#Overhead:
#Frequent function calls can add execution overhead, especially in performance-critical applications.
#Debugging Complexity:
#If functions are not designed properly, debugging interdependent functions can become challenging.
#Increased Complexity for Simple Tasks:
#For very straightforward code, using functions might add unnecessary complexity.
#Dependency Management:
#Functions that rely heavily on global variables or external states can lead to tightly coupled code.

#USE CASES
#Code Reuse:
#Functions can encapsulate common tasks like logging, validation, or calculations.
#Example:
def add(a, b):
    return a + b

print(add(3, 5))  # Output: 8

#Data Processing:
#Functions are ideal for performing operations like sorting, filtering, or transforming data.
#Example:
def square_list(numbers):
    return [x ** 2 for x in numbers]

print(square_list([1, 2, 3]))  # Output: [1, 4, 9]

#Encapsulation of Logic:
#Business rules, algorithms, or workflows can be encapsulated in functions for clarity.
#Automation:
#Automating repetitive tasks using functions in scripts or programs.
#Event Handling:
#Functions can handle specific events or inputs in GUI applications or web development.
#Mathematical Calculations:
#Complex mathematical or statistical operations can be modularized.
#Example:
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

print(area_of_circle(5))  # Output: 78.53981633974483
#File and Data Operations:
#Functions are useful for reading, writing, and manipulating files or databases.
#Web Development:
#Functions in frameworks like Flask or Django handle HTTP requests, database interactions, etc.
#Dynamic and Recursive Operations:
#Dynamic programming or recursive algorithms can be implemented using functions.
#Example of recursion:
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120


#TYPES OF FUNCTIONS
#Built-in Functions: Predefined functions like len(), type(), input().
#User-defined Functions: Custom functions defined using the def keyword.
#Anonymous (Lambda) Functions: Single-line functions created using the lambda keyword.
#Example:
square = lambda x: x ** 2
print(square(4))  # Output: 16


#EXAMPLE BASIC PROGRAM

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    """
    Calculates the area of a rectangle.
    :param length: Length of the rectangle
    :param width: Width of the rectangle
    :return: Area of the rectangle
    """
    return length * width


# Function to calculate the perimeter of a rectangle
def calculate_perimeter(length, width):
    """
    Calculates the perimeter of a rectangle.
    :param length: Length of the rectangle
    :param width: Width of the rectangle
    :return: Perimeter of the rectangle
    """
    return 2 * (length + width)


# Main program
def main():
    print("Rectangle Calculator")
    # Input: Length and Width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate area and perimeter using the functions
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    # Output: Display results
    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")


# Entry point of the program
if __name__ == "__main__":
    main()

#What is a Decorator in Python?
#A decorator in Python is a design pattern that allows you to modify or enhance the behavior of a function or method without changing its source code.
# It is a higher-order function that takes another function as an argument and returns a new function.

#Advantages of Decorators:
#Code Reusability: Allows adding functionality to multiple functions without code duplication.
#Separation of Concerns: Keeps core logic clean by separating additional functionality.
#Readability: Enhances code readability with a clean and concise syntax.

#Disadvantages of Decorators:
#Debugging Complexity: Makes debugging harder as it changes function behavior dynamically.
#Readability Issues: Can reduce readability if overused or not well-documented.
#Performance Overhead: May introduce slight overhead due to the wrapping.

#Common Use Cases:
#Logging function calls.
#Access control (e.g., authentication).
#Timing and profiling functions.
#Memoization (caching).
#Example 1: Logging

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with args: {args} kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

#Example 2: Timing

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def compute_square(n):
    return [i**2 for i in range(n)]

compute_square(1000000)



