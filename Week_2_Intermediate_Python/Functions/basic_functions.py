"""
Python Basic Functions Tutorial

Functions are blocks of reusable code that perform a specific task.
Key concepts covered:
1. Function definition and calling
2. Parameters and arguments
3. Return values
4. Docstrings
5. Default parameters
"""

# Basic function definition
print("\n=== Basic Function Definition ===")
def greet():
    print("Hello, World!")

print("Calling greet function:")
greet()

# Function with parameters
print("\n=== Functions with Parameters ===")
def greet_person(name):
    print(f"Hello, {name}!")

print("Calling greet_person with parameter:")
greet_person("Alice")

# Function with multiple parameters
print("\n=== Multiple Parameters ===")
def add_numbers(a, b):
    print(f"Adding {a} + {b}")
    return a + b

result = add_numbers(5, 3)
print("Result:", result)

# Function with default parameters
print("\n=== Default Parameters ===")
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}")

print("Using default parameter:")
greet_with_title("Smith")
print("Overriding default parameter:")
greet_with_title("Johnson", "Dr.")

# Function with docstring
print("\n=== Function with Docstring ===")
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width

print("Function documentation:")
print(calculate_area.__doc__)
print("\nCalling calculate_area:")
area = calculate_area(5, 3)
print("Area:", area)

# Multiple return values
print("\n=== Multiple Return Values ===")
def get_dimensions():
    length = 10
    width = 5
    height = 3
    return length, width, height

l, w, h = get_dimensions()
print(f"Dimensions: length={l}, width={w}, height={h}")

# Print vs Return
print("\n=== Print vs Return ===")
def print_sum(a, b):
    print(a + b)  # Just prints, doesn't return

def return_sum(a, b):
    return a + b  # Returns value

print("Using print_sum:")
result1 = print_sum(3, 4)  # Returns None
print("Result1:", result1)

print("\nUsing return_sum:")
result2 = return_sum(3, 4)  # Returns 7
print("Result2:", result2)

# Practical example
print("\n=== Practical Example ===")
def calculate_total_cost(price, tax_rate=0.1, shipping=5.0):
    """
    Calculate the total cost including tax and shipping.
    
    Args:
        price (float): The base price of the item
        tax_rate (float): The tax rate (default 10%)
        shipping (float): Shipping cost (default $5.00)
    
    Returns:
        float: Total cost including tax and shipping
    """
    tax = price * tax_rate
    total = price + tax + shipping
    return total

# Using the function with different parameters
print("Shopping cart totals:")
print("Basic purchase:", calculate_total_cost(50))
print("With custom tax rate:", calculate_total_cost(50, 0.15))
print("With custom tax and shipping:", calculate_total_cost(50, 0.15, 7.50))
