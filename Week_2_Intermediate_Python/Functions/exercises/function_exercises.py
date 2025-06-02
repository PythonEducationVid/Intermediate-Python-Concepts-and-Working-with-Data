"""
Python Functions Exercises

This file contains exercises to practice:
1. Basic function definition and usage
2. Advanced function concepts
3. Recursion
4. Function decorators
5. Real-world application scenarios

Instructions:
1. Try to solve each exercise without looking at the solutions
2. Run this file to check your answers
3. Remove the 'pass' statement and write your code
4. Compare your output with the expected output
"""

print("\n=== Basic Function Exercises ===")
# Exercise 1: Create a function that returns the maximum of three numbers
print("Exercise 1: Maximum of three numbers")
# Your code here
def max_of_three(a, b, c):
    pass

print("Your result:", max_of_three(10, 5, 8))
print("Expected: 10")

# Exercise 2: Create a function that counts vowels in a string
print("\nExercise 2: Count vowels")
# Your code here
def count_vowels(text):
    pass

print("Your result:", count_vowels("hello world"))
print("Expected: 3")

print("\n=== Advanced Function Exercises ===")
# Exercise 3: Create a function that accepts any number of strings and returns them concatenated
print("Exercise 3: String concatenation with *args")
# Your code here
def concatenate_strings(*args):
    pass

print("Your result:", concatenate_strings("Hello", " ", "World", "!"))
print("Expected: Hello World!")

# Exercise 4: Create a function that accepts key-value pairs and returns a formatted string
print("\nExercise 4: Format person info with **kwargs")
# Your code here
def format_person_info(**kwargs):
    pass

print("Your result:", format_person_info(name="John", age=30, city="New York"))
print("Expected: Person: name=John, age=30, city=New York")

print("\n=== Recursion Exercises ===")
# Exercise 5: Calculate the sum of digits in a number using recursion
print("Exercise 5: Sum of digits")
# Your code here
def sum_of_digits(n):
    pass

print("Your result:", sum_of_digits(123))
print("Expected: 6")

# Exercise 6: Calculate power using recursion
print("\nExercise 6: Power calculation")
# Your code here
def power(base, exponent):
    pass

print("Your result:", power(2, 3))
print("Expected: 8")

print("\n=== Decorator Exercises ===")
# Exercise 7: Create a decorator that measures function execution time
print("Exercise 7: Execution timer")
# Your code here
def timer_decorator(func):
    pass

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done!"

print("Your result: Call slow_function()")
print("Expected: Function slow_function took about 1 second to execute")

print("\n=== Real-World Exercises ===")
# Exercise 8: Create a simple calculator with basic operations
print("Exercise 8: Calculator")
# Your code here
def calculator(operation, a, b):
    pass

print("Your result:", calculator("add", 5, 3))
print("Expected: 8")
print("Your result:", calculator("multiply", 4, 2))
print("Expected: 8")

"""
Solutions:

# Exercise 1
def max_of_three(a, b, c):
    return max(a, max(b, c))

# Exercise 2
def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')

# Exercise 3
def concatenate_strings(*args):
    return ''.join(args)

# Exercise 4
def format_person_info(**kwargs):
    info = [f"{key}={value}" for key, value in kwargs.items()]
    return "Person: " + ", ".join(info)

# Exercise 5
def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

# Exercise 6
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

# Exercise 7
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.2f} seconds to execute")
        return result
    return wrapper

# Exercise 8
def calculator(operation, a, b):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    return operations.get(operation, lambda x, y: "Invalid operation")(a, b)
"""
