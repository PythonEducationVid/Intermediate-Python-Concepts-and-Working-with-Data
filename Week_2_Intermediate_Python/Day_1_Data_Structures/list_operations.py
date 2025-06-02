"""
Advanced List Operations and List Comprehensions Tutorial

Lists are one of the most versatile and commonly used data structures in Python.
They can store multiple items of different types in a single variable.
This tutorial covers:
1. Creating and accessing lists
2. Basic list operations and methods
3. List slicing
4. List manipulation
5. Advanced operations
6. List comprehensions
"""

# Creating lists - different ways to create lists
print("\n=== Creating Lists ===")
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
mixed = [1, 'hello', 3.14, True]
empty_list = []

print("Numbers list:", numbers)
print("Fruits list:", fruits)
print("Mixed types list:", mixed)
print("Empty list:", empty_list)

# Accessing list elements
print("\n=== Accessing Elements ===")
print("First fruit:", fruits[0])  # Indexing starts at 0
print("Last number:", numbers[-1])  # Negative indexing starts from the end
print("Second number:", numbers[1])

# Basic list operations
print("\n=== Basic List Operations ===")
numbers.append(6)  # Add element to end
print("After append 6:", numbers)

numbers.insert(0, 0)  # Insert at beginning
print("After insert 0 at beginning:", numbers)

numbers.extend([7, 8, 9])  # Add multiple elements
print("After extend with [7, 8, 9]:", numbers)

# Removing elements
print("\n=== Removing Elements ===")
last_number = numbers.pop()  # Remove and return last element
print("Popped last element:", last_number)
print("After pop:", numbers)

numbers.remove(5)  # Remove first occurrence of 5
print("After removing 5:", numbers)

# List slicing
print("\n=== List Slicing ===")
"""
List slicing allows you to extract portions of a list
Syntax: list[start:end:step]
- start: starting index (inclusive)
- end: ending index (exclusive)
- step: how many elements to skip
"""
print("First three elements:", numbers[:3])
print("Last three elements:", numbers[-3:])
print("Every second element:", numbers[::2])
print("Reverse the list:", numbers[::-1])

# List operations
print("\n=== List Operations ===")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("List1 + List2:", list1 + list2)  # Concatenation
print("List1 * 3:", list1 * 3)  # Repetition

# List comprehensions
print("\n=== List Comprehensions ===")
"""
List comprehensions provide a concise way to create lists
Syntax: [expression for item in iterable if condition]
"""
# Create a list of squares from 0 to 9
squares = [x * x for x in range(10)]
print("Squares 0-9:", squares)

# Create a list of even numbers from 0 to 10
even_numbers = [x for x in range(11) if x % 2 == 0]
print("Even numbers 0-10:", even_numbers)

# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [((9/5) * temp + 32) for temp in celsius]
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)