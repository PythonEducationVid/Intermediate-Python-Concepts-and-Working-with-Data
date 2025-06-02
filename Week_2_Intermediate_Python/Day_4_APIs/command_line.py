"""
Python Command Line Arguments Tutorial

This tutorial covers working with command line arguments using:
1. sys.argv
2. argparse module
3. click library
4. environment variables
5. Interactive input
"""

import sys
import argparse
import os
from getpass import getpass
import json

print("\n=== Basic Command Line Arguments (sys.argv) ===")
print("All arguments:", sys.argv)
print("Script name:", sys.argv[0])
if len(sys.argv) > 1:
    print("First argument:", sys.argv[1])

print("\n=== Argparse Example ===")
def create_parser():
    """Create an argument parser with various argument types"""
    parser = argparse.ArgumentParser(
        description='Example command line argument parser'
    )
    
    # Required argument
    parser.add_argument('filename', help='File to process')
    
    # Optional argument with short and long forms
    parser.add_argument('-o', '--output', 
                       help='Output file (default: output.txt)',
                       default='output.txt')
    
    # Flag (boolean argument)
    parser.add_argument('-v', '--verbose',
                       action='store_true',
                       help='Increase output verbosity')
    
    # Argument with choices
    parser.add_argument('--mode',
                       choices=['read', 'write', 'append'],
                       default='read',
                       help='File operation mode')
    
    # Numerical argument
    parser.add_argument('--num-lines',
                       type=int,
                       default=10,
                       help='Number of lines to process')
    
    # Multiple values
    parser.add_argument('--files',
                       nargs='+',
                       help='Multiple files to process')
    
    return parser

# Create parser and print help
parser = create_parser()
print("Help message:")
parser.print_help()

print("\n=== Handling Environment Variables ===")
def get_config():
    """Get configuration from environment variables"""
    config = {
        'api_key': os.environ.get('API_KEY', 'default_key'),
        'api_url': os.environ.get('API_URL', 'http://localhost:8000'),
        'debug': os.environ.get('DEBUG', 'False').lower() == 'true'
    }
    return config

print("Configuration from environment:")
print(json.dumps(get_config(), indent=2))

print("\n=== Interactive Input ===")
def get_user_input():
    """Demonstrate different ways to get user input"""
    # Basic input
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    
    # Password input (hidden)
    password = getpass("Enter password: ")
    print("Password length:", len(password))
    
    # Numeric input with validation
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 <= age <= 150:
                break
            print("Please enter a valid age (0-150)")
        except ValueError:
            print("Please enter a number")
    
    print(f"Age entered: {age}")

print("\n=== Command Line UI Example ===")
def progress_bar(iteration, total, prefix='Progress:', length=50):
    """Simple progress bar"""
    percent = (iteration / float(total)) * 100
    filled = int(length * iteration // total)
    bar = '=' * filled + '-' * (length - filled)
    print(f'\r{prefix} |{bar}| {percent:.1f}%', end='\r')
    if iteration == total:
        print()

# Example usage
print("Processing files...")
total = 10
for i in range(total + 1):
    progress_bar(i, total)
    # Simulate work
    import time
    time.sleep(0.1)

print("\n=== Error Handling Example ===")
def safe_file_operation(filename, mode='r'):
    """Demonstrate error handling with files"""
    try:
        with open(filename, mode) as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
    return None

# Example usage
print("Trying to read non-existent file:")
content = safe_file_operation('nonexistent.txt')

print("\n=== Example Command Line Script ===")
def main(args=None):
    """Main function for command line script"""
    parser = argparse.ArgumentParser(
        description='Process some files'
    )
    parser.add_argument('files', nargs='+', help='Files to process')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Print verbose output')
    
    args = parser.parse_args(args)
    
    for file in args.files:
        if args.verbose:
            print(f"Processing {file}...")
        content = safe_file_operation(file)
        if content and args.verbose:
            print(f"Content length: {len(content)} bytes")

print("Example command usage:")
print("python script.py file1.txt file2.txt --verbose")

print("\n=== Best Practices ===")
print("1. Use argparse for complex CLI applications")
print("2. Provide helpful error messages")
print("3. Use environment variables for configuration")
print("4. Implement proper error handling")
print("5. Add --help documentation")
print("6. Use appropriate argument types")
print("7. Validate user input")
print("8. Provide progress feedback")