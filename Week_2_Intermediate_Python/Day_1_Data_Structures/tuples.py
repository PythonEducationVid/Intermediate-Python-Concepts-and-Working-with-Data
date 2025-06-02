

"""
Python Tuples Tutorial

Tuples are immutable sequences in Python, similar to lists but with key differences:
1. Tuples are immutable (cannot be changed after creation)
2. Tuples use parentheses () instead of square brackets []
3. Tuples are generally used for related pieces of data
4. Tuples are more memory efficient than lists
5. Tuples can be used as dictionary keys (lists cannot)
"""

# Creating tuples
print("\n=== Creating Tuples ===")
empty_tuple = ()
single_element = (1,)  # Note the comma - needed for single element tuples
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
nested = (1, (2, 3), (4, 5, 6))

print("Empty tuple:", empty_tuple)
print("Single element tuple:", single_element)
print("Numbers tuple:", numbers)
print("Mixed types tuple:", mixed)
print("Nested tuple:", nested)

# Accessing tuple elements
print("\n=== Accessing Elements ===")
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Nested element:", nested[1][0])  # Accessing element in nested tuple

# Tuple slicing
print("\n=== Tuple Slicing ===")
"""
Tuple slicing works exactly like list slicing
Syntax: tuple[start:end:step]
"""
print("First three elements:", numbers[:3])
print("Last three elements:", numbers[-3:])
print("Every second element:", numbers[::2])
print("Reverse the tuple:", numbers[::-1])

# Tuple operations
print("\n=== Tuple Operations ===")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Concatenated tuples:", tuple1 + tuple2)
print("Repeated tuple:", tuple1 * 3)

# Tuple methods
print("\n=== Tuple Methods ===")
repeated_tuple = (1, 2, 2, 3, 2, 4, 2, 5)
print("Count of 2:", repeated_tuple.count(2))  # Count occurrences of an element
print("Index of 3:", repeated_tuple.index(3))  # Find first occurrence of an element

# Tuple unpacking
print("\n=== Tuple Unpacking ===")
"""
Tuple unpacking allows you to assign tuple elements to variables
"""
coordinates = (3, 4)
x, y = coordinates
print(f"X coordinate: {x}, Y coordinate: {y}")

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print("First:", first)
print("Middle:", middle)
print("Last:", last)

# Practical applications
print("\n=== Practical Applications ===")
# Representing a point in 2D space
point = (10, 20)
print("Point coordinates (x, y):", point)

# Representing RGB color
color = (255, 128, 0)
print("RGB color values:", color)

# Returning multiple values from calculations
def calculate_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return (area, circumference)

# Multiple assignment with tuples
circle_radius = 5
circle_area, circle_circumference = calculate_circle(circle_radius)
print(f"Circle with radius {circle_radius}:")
print(f"Area: {circle_area:.2f}")
print(f"Circumference: {circle_circumference:.2f}")

