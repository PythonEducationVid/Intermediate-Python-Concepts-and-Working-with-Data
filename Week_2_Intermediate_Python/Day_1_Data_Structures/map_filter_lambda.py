"""
Python Map, Filter, and Lambda Functions Tutorial

These are powerful tools for functional programming in Python:
1. map() - Apply a function to every item in an iterable
2. filter() - Create a list of elements that satisfy a condition
3. lambda - Create small anonymous functions
"""

print("\n=== Lambda Functions ===")
"""
Lambda functions are small anonymous functions that can have any number of arguments
but can only have one expression.
Syntax: lambda arguments: expression
"""

# Simple lambda functions
square = lambda x: x**2
add = lambda x, y: x + y

print("Square of 5:", square(5))
print("Add 3 and 4:", add(3, 4))

# Lambda with multiple arguments
multiply = lambda x, y, z: x * y * z
print("Multiply 2, 3, 4:", multiply(2, 3, 4))

print("\n=== Map Function ===")
"""
map() applies a function to every item in an input list
Syntax: map(function, iterable, ...)
"""

numbers = [1, 2, 3, 4, 5]

# Using map with regular function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print("Doubled numbers (using function):", doubled)

# Using map with lambda
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers (using lambda):", squared)

# Map with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
added = list(map(lambda x, y: x + y, list1, list2))
print("Adding two lists element-wise:", added)

print("\n=== Filter Function ===")
"""
filter() creates a list of elements for which a function returns True
Syntax: filter(function, iterable)
"""

numbers = range(-5, 6)  # -5 to 5

# Filter positive numbers
positive = list(filter(lambda x: x > 0, numbers))
print("Positive numbers:", positive)

# Filter even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# Practical examples
print("\n=== Practical Examples ===")

# Example 1: Processing a list of temperatures (C° to F°)
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

# Example 2: Filtering out None values
data = [1, None, 3, None, 5, None]
valid_data = list(filter(None, data))  # None is automatically filtered out
print("Original data:", data)
print("Valid data:", valid_data)

# Example 3: Processing strings
words = ['hello', 'world', 'python', 'programming']
# Get lengths of words
lengths = list(map(len, words))
print("Word lengths:", lengths)
# Filter words longer than 5 characters
long_words = list(filter(lambda word: len(word) > 5, words))
print("Words longer than 5 characters:", long_words)

# Example 4: Processing dictionaries
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 30},
    {'name': 'David', 'age': 15}
]

# Filter adults (age >= 18)
adults = list(filter(lambda person: person['age'] >= 18, people))
print("\nAdults:", adults)

# Extract names only
names = list(map(lambda person: person['name'], people))
print("Names:", names)