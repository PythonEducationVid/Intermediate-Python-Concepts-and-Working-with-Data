"""
Python Recursion Tutorial

Recursion is when a function calls itself.
Key concepts covered:
1. Basic recursion
2. Recursive vs iterative solutions
3. Base cases and recursive cases
4. Stack depth and memory considerations
5. Common recursive patterns
"""

# Basic recursion example: Factorial
print("\n=== Factorial Example ===")
def factorial(n):
    """Calculate factorial using recursion"""
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print("Factorial of 3:", factorial(3))

# Fibonacci sequence
print("\n=== Fibonacci Sequence ===")
def fibonacci(n):
    """Generate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("First 6 Fibonacci numbers:")
for i in range(6):
    print(f"fibonacci({i}) = {fibonacci(i)}")

# Recursive vs Iterative
print("\n=== Recursive vs Iterative ===")
def sum_recursive(numbers):
    """Sum a list using recursion"""
    if not numbers:  # Base case: empty list
        return 0
    return numbers[0] + sum_recursive(numbers[1:])

def sum_iterative(numbers):
    """Sum a list using iteration"""
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)
print("Recursive sum:", sum_recursive(numbers))
print("Iterative sum:", sum_iterative(numbers))

# Recursive binary search
print("\n=== Recursive Binary Search ===")
def binary_search(arr, target, low=0, high=None):
    """
    Perform binary search recursively
    Returns index of target if found, -1 otherwise
    """
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid-1)
    else:
        return binary_search(arr, target, mid+1, high)

sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
print("Array:", sorted_numbers)
print("Searching for 7:", binary_search(sorted_numbers, 7))
print("Searching for 10:", binary_search(sorted_numbers, 10))

# Tree-like recursion example
print("\n=== Tree Recursion Example ===")
def print_binary_tree(n, prefix=""):
    """Print a visual representation of a binary tree of depth n"""
    if n == 0:
        return
    print(prefix + "│")
    print(prefix + "├── Left")
    print_binary_tree(n-1, prefix + "│   ")
    print(prefix + "└── Right")
    print_binary_tree(n-1, prefix + "    ")

print("Binary Tree of depth 2:")
print_binary_tree(2)

# Practical example: Directory traversal
print("\n=== Directory Structure Example ===")
def print_directory_structure(structure, prefix=""):
    """
    Print a directory structure recursively
    structure should be a dictionary where:
    - keys are names of files/folders
    - values are None for files, or another dictionary for folders
    """
    for name, contents in structure.items():
        print(prefix + "├── " + name)
        if contents:  # If it's a directory
            print_directory_structure(contents, prefix + "│   ")

# Example directory structure
directory = {
    "project": {
        "src": {
            "main.py": None,
            "utils.py": None
        },
        "tests": {
            "test_main.py": None
        },
        "README.md": None
    }
}

print("Directory structure:")
print_directory_structure(directory)
