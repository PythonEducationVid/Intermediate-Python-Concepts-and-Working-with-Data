"""
Python Advanced Functions Tutorial

Advanced function concepts including:
1. *args and **kwargs
2. Lambda functions
3. Nested functions
4. Function as objects
5. Decorators basics
"""

# *args - Variable number of arguments
print("\n=== *args Example ===")
def sum_all(*args):
    """Accept any number of positional arguments and return their sum"""
    print("Received arguments:", args)
    return sum(args)

print("Sum of 1, 2, 3:", sum_all(1, 2, 3))
print("Sum of 1, 2, 3, 4, 5:", sum_all(1, 2, 3, 4, 5))

# **kwargs - Variable number of keyword arguments
print("\n=== **kwargs Example ===")
def print_info(**kwargs):
    """Accept any number of keyword arguments and print them"""
    print("Received key-word arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
print_info(title="Dr.", first_name="John", last_name="Smith")

# Both *args and **kwargs
print("\n=== Combined *args and **kwargs ===")
def super_function(*args, **kwargs):
    """Accept both positional and keyword arguments"""
    print("Positional args:", args)
    print("Keyword args:", kwargs)

super_function(1, 2, 3, name="Alice", age=25)

# Nested functions
print("\n=== Nested Functions ===")
def outer_function(x):
    """Function containing another function"""
    def inner_function(y):
        return x + y
    return inner_function

# Using nested function
add_five = outer_function(5)
print("Adding 5 to 3:", add_five(3))
print("Adding 5 to 7:", add_five(7))

# Functions as objects
print("\n=== Functions as Objects ===")
def square(x):
    return x * x

def cube(x):
    return x * x * x

# Store functions in a list
operations = [square, cube]
number = 3

print(f"Operations on {number}:")
for func in operations:
    print(f"{func.__name__}: {func(number)}")

# Basic decorator example
print("\n=== Basic Decorator ===")
def announce_operation(func):
    """Decorator that announces when a function is called"""
    def wrapper(*args, **kwargs):
        print(f"About to perform {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@announce_operation
def add_numbers(a, b):
    return a + b

print("Using decorated function:")
result = add_numbers(5, 3)
print("Result:", result)

# Higher-order functions
print("\n=== Higher-Order Functions ===")
def create_multiplier(factor):
    """Return a function that multiplies its argument by factor"""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print("Using double function:", double(5))
print("Using triple function:", triple(5))

# Practical example: Function composition
print("\n=== Function Composition Example ===")
def compose(*functions):
    """
    Create a function that is a composition of the given functions.
    compose(f, g, h)(x) is equivalent to f(g(h(x)))
    """
    def inner(x):
        result = x
        for f in reversed(functions):
            result = f(result)
        return result
    return inner

# Example usage of function composition
def add_one(x): return x + 1
def double(x): return x * 2
def square(x): return x * x

# Create a composed function
composed = compose(square, double, add_one)
print("Composed function result (square(double(add_one(5)))):", composed(5))
