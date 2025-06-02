"""
Python Sets Tutorial

Sets are unordered collections of unique elements in Python.
Key characteristics:
1. Unordered (elements have no index)
2. Mutable (can be modified)
3. Unique elements (no duplicates)
4. Can only contain immutable elements
5. Useful for removing duplicates and set operations
"""

# Creating sets
print("\n=== Creating Sets ===")
empty_set = set()  # Note: {} creates empty dict, not set
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}
mixed = {1, "hello", 3.14, True}

print("Empty set:", empty_set)
print("Numbers set:", numbers)
print("Fruits set:", fruits)
print("Mixed types set:", mixed)

# Removing duplicates with sets
print("\n=== Removing Duplicates ===")
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(numbers_with_duplicates)
print("Original list:", numbers_with_duplicates)
print("After removing duplicates:", unique_numbers)

# Adding and removing elements
print("\n=== Modifying Sets ===")
colors = {"red", "green", "blue"}
print("Original set:", colors)

colors.add("yellow")
print("After adding yellow:", colors)

colors.update(["purple", "orange"])
print("After updating with multiple colors:", colors)

colors.remove("red")  # Raises error if element not found
print("After removing red:", colors)

colors.discard("black")  # No error if element not found
print("After discarding black (not in set):", colors)

popped_color = colors.pop()  # Remove and return arbitrary element
print("Popped color:", popped_color)
print("After pop:", colors)

# Set operations
print("\n=== Set Operations ===")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union (all unique elements from both sets)
print("A union B:", A | B)  # Alternative: A.union(B)

# Intersection (elements common to both sets)
print("A intersection B:", A & B)  # Alternative: A.intersection(B)

# Difference (elements in A but not in B)
print("A difference B:", A - B)  # Alternative: A.difference(B)

# Symmetric difference (elements in either A or B, but not both)
print("A symmetric difference B:", A ^ B)  # Alternative: A.symmetric_difference(B)

# Set comparisons
print("\n=== Set Comparisons ===")
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}

print("set1 is subset of set2:", set1 <= set2)  # True
print("set1 is proper subset of set2:", set1 < set2)  # True
print("set1 equals set3:", set1 == set3)  # True

# Practical examples
print("\n=== Practical Examples ===")
# Finding unique characters in a string
text = "hello world"
unique_chars = set(text)
print("Unique characters in 'hello world':", unique_chars)

# Finding common elements between lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = set(list1) & set(list2)
print("Common elements between lists:", common_elements)

# Checking if all required skills are present
required_skills = {"Python", "SQL", "Git"}
candidate_skills = {"Python", "JavaScript", "Git", "SQL", "HTML"}
has_required_skills = required_skills <= candidate_skills
print("Candidate has all required skills:", has_required_skills)