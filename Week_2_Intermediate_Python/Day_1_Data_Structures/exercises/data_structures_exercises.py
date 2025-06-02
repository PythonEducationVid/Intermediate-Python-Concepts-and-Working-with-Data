"""
Python Data Structures Exercises

This file contains exercises to practice:
1. List operations and comprehensions
2. Tuple operations and unpacking
3. Dictionary manipulation
4. Set operations
5. Map, Filter, and Lambda functions

Instructions:
1. Try to solve each exercise without looking at the solutions
2. Run this file to check your answers
3. Remove the 'pass' statement and write your code
4. Compare your output with the expected output
"""

print("\n=== List Exercises ===")
# Exercise 1: Create a list of squares for numbers from 1 to 10
print("Exercise 1: Create a list of squares (1-10)")
squares = []  # Your code here
print("Your result:", squares)
print("Expected: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]")

# Exercise 2: Remove all duplicate numbers from the list
print("\nExercise 2: Remove duplicates")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = []  # Your code here
print("Your result:", unique_numbers)
print("Expected: [1, 2, 3, 4]")

print("\n=== Tuple Exercises ===")
# Exercise 3: Unpack the following tuple into 3 variables
print("Exercise 3: Tuple unpacking")
point3D = (10, 20, 30)
# Your code here (create x, y, z variables)
print("Your result: Coordinates:", "x =", 0, "y =", 0, "z =", 0)  # Replace 0s with your variables
print("Expected: Coordinates: x = 10 y = 20 z = 30")

# Exercise 4: Create a list of tuples containing number and its square
print("\nExercise 4: Number-Square pairs")
numbers = [1, 2, 3, 4, 5]
square_pairs = []  # Your code here
print("Your result:", square_pairs)
print("Expected: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]")

print("\n=== Dictionary Exercises ===")
# Exercise 5: Create a dictionary from two lists
print("Exercise 5: Create dictionary from lists")
keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']
person = {}  # Your code here
print("Your result:", person)
print("Expected: {'name': 'John', 'age': 25, 'city': 'New York'}")

# Exercise 6: Count word frequency in a sentence
print("\nExercise 6: Word frequency")
sentence = "the quick brown fox jumps over the lazy dog"
word_frequency = {}  # Your code here
print("Your result:", word_frequency)
print("Expected: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}")

print("\n=== Set Exercises ===")
# Exercise 7: Find common elements between two lists using sets
print("Exercise 7: Common elements")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []  # Your code here
print("Your result:", common)
print("Expected: {4, 5}")

# Exercise 8: Remove duplicates while maintaining order
print("\nExercise 8: Ordered unique elements")
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'kiwi']
unique_ordered = []  # Your code here
print("Your result:", unique_ordered)
print("Expected: ['apple', 'banana', 'orange', 'kiwi']")

print("\n=== Map/Filter/Lambda Exercises ===")
# Exercise 9: Convert temperatures from Celsius to Fahrenheit using map
print("Exercise 9: Temperature conversion")
celsius = [0, 10, 20, 30, 40]
fahrenheit = []  # Your code here: Use map and lambda
print("Your result:", fahrenheit)
print("Expected: [32.0, 50.0, 68.0, 86.0, 104.0]")

# Exercise 10: Filter out negative numbers using filter and lambda
print("\nExercise 10: Filter negative numbers")
numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
positive_numbers = []  # Your code here: Use filter and lambda
print("Your result:", positive_numbers)
print("Expected: [0, 1, 2, 3, 4]")

"""
Solutions:

# Exercise 1:
squares = [x**2 for x in range(1, 11)]

# Exercise 2:
unique_numbers = list(dict.fromkeys(numbers))  # or list(set(numbers))

# Exercise 3:
x, y, z = point3D

# Exercise 4:
square_pairs = [(n, n**2) for n in numbers]

# Exercise 5:
person = dict(zip(keys, values))

# Exercise 6:
word_frequency = {}
for word in sentence.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Exercise 7:
common = set(list1) & set(list2)

# Exercise 8:
unique_ordered = list(dict.fromkeys(items))

# Exercise 9:
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

# Exercise 10:
positive_numbers = list(filter(lambda x: x >= 0, numbers))
"""