"""
Python Dictionaries Tutorial

Dictionaries are key-value pair data structures in Python.
They are:
1. Mutable (can be changed after creation)
2. Unordered (in Python < 3.7)
3. Indexed by keys instead of numbers
4. Keys must be immutable (strings, numbers, tuples)
5. Values can be any Python object
"""

# Creating dictionaries
print("\n=== Creating Dictionaries ===")
empty_dict = {}
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
grades = {"math": 90, "science": 85, "history": 88}

print("Empty dictionary:", empty_dict)
print("Person dictionary:", person)
print("Grades dictionary:", grades)

# Accessing dictionary values
print("\n=== Accessing Values ===")
print("Person's name:", person["name"])
print("Math grade:", grades["math"])

# Using get() method (safer way to access values)
print("Person's age:", person.get("age"))
print("Person's email:", person.get("email", "Not found"))  # Default value if key doesn't exist

# Modifying dictionaries
print("\n=== Modifying Dictionaries ===")
person["age"] = 31  # Change existing value
person["email"] = "john@example.com"  # Add new key-value pair
print("Updated person:", person)

# Dictionary methods
print("\n=== Dictionary Methods ===")
# Get all keys
print("Keys:", list(person.keys()))

# Get all values
print("Values:", list(person.values()))

# Get all key-value pairs (items)
print("Items:", list(person.items()))

# Remove items
removed_age = person.pop("age")  # Remove and return value
print("Removed age:", removed_age)
print("After removing age:", person)

# Clear dictionary
grades.clear()
print("Cleared grades dictionary:", grades)

# Dictionary comprehension
print("\n=== Dictionary Comprehension ===")
# Create a dictionary of number:square pairs
squares = {x: x*x for x in range(5)}
print("Number squares:", squares)

# Create a dictionary of string:length pairs
words = ["hello", "world", "python"]
word_lengths = {word: len(word) for word in words}
print("Word lengths:", word_lengths)

# Nested dictionaries
print("\n=== Nested Dictionaries ===")
students = {
    "student1": {
        "name": "Alice",
        "grades": {"math": 95, "science": 98}
    },
    "student2": {
        "name": "Bob",
        "grades": {"math": 85, "science": 88}
    }
}
print("Students data:", students)
print("Student1's math grade:", students["student1"]["grades"]["math"])

# Practical examples
print("\n=== Practical Examples ===")
# Counting frequency of items
text = "hello world hello python world python python"
word_frequency = {}
for word in text.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1
print("Word frequency:", word_frequency)

# Converting two lists into a dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = dict(zip(keys, values))
print("Combined lists into dictionary:", combined)

# Advanced dictionary operations
print("\n=== Advanced Dictionary Operations ===")
# Copying a dictionary
person_copy = person.copy()
print("Copied person dictionary:", person_copy)

# Using fromkeys() to create a new dictionary
new_dict = {}.fromkeys(["a", "b", "c"], 0)
print("New dictionary with fromkeys():", new_dict)

# Using defaultdict from collections for default values
from collections import defaultdict
dd = defaultdict(int)
dd["apple"] += 1
print("Default dictionary (int):", dd)

# Using OrderedDict from collections (remembers order of insertion)
from collections import OrderedDict
od = OrderedDict()
od["first"] = 1
od["second"] = 2
print("Ordered dictionary:", od)

# Using Counter from collections to count hashable objects
from collections import Counter
counter = Counter("hello world")
print("Character count with Counter:", counter)

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}  # Merges dict1 and dict2
print("Merged dictionary:", merged)

# Set default values for missing keys
person.setdefault("name", "Unknown")
person.setdefault("country", "USA")  # Adds key 'country' with value 'USA' as it doesn't exist
print("Person dictionary with defaults:", person)

# Dictionary views - dynamic views of dictionary's keys, values, and items
print("Keys view:", person.keys())
print("Values view:", person.values())
print("Items view:", person.items())

# Sorting a dictionary by keys and by values
sorted_by_keys = dict(sorted(person.items()))
sorted_by_values = dict(sorted(person.items(), key=lambda item: item[1]))
print("Sorted by keys:", sorted_by_keys)
print("Sorted by values:", sorted_by_values)

# Using a dictionary in a loop
print("Looping through dictionary:")
for key, value in person.items():
    print(key, ":", value)

# Dictionary as a switch-case statement
def switch_case(argument):
    switcher = {
        0: "Zero",
        1: "One",
        2: "Two"
    }
    return switcher.get(argument, "Invalid")  # Default case

print("Switch case for 1:", switch_case(1))
print("Switch case for 4:", switch_case(4))