"""
Python File System Operations Tutorial

This tutorial covers working with the file system using:
1. os module
2. pathlib module
3. shutil module
4. glob module
5. File operations and patterns
"""

import os
import pathlib
import shutil
import glob
import json
from datetime import datetime

print("\n=== Basic Path Operations ===")
# Current working directory
print("Current directory:", os.getcwd())

# Join paths (cross-platform)
data_path = os.path.join('data', 'files', 'example.txt')
print("Joined path:", data_path)

# Absolute path
abs_path = os.path.abspath(data_path)
print("Absolute path:", abs_path)

# Path components
print("Directory name:", os.path.dirname(abs_path))
print("File name:", os.path.basename(abs_path))
print("Split path:", os.path.split(abs_path))

print("\n=== Pathlib Usage ===")
# Create Path object
path = pathlib.Path('data/files/example.txt')
print("Path object:", path)
print("Parent directory:", path.parent)
print("File name:", path.name)
print("Stem:", path.stem)
print("Suffix:", path.suffix)

# Path operations
new_path = path.with_suffix('.json')
print("Changed suffix:", new_path)

print("\n=== Directory Operations ===")
# Create a temporary directory for demonstration
temp_dir = 'temp_demo'
os.makedirs(temp_dir, exist_ok=True)
print(f"Created directory: {temp_dir}")

# Create some files
for i in range(3):
    file_path = os.path.join(temp_dir, f'file_{i}.txt')
    with open(file_path, 'w') as f:
        f.write(f"Content of file {i}")

# List directory contents
print("\nDirectory contents:")
print(os.listdir(temp_dir))

# Walk directory tree
print("\nWalking directory tree:")
for root, dirs, files in os.walk(temp_dir):
    print(f"Root: {root}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")

print("\n=== File Operations ===")
# File existence
file_path = os.path.join(temp_dir, 'file_0.txt')
print(f"Does {file_path} exist?", os.path.exists(file_path))
print(f"Is it a file?", os.path.isfile(file_path))
print(f"Is it a directory?", os.path.isdir(file_path))

# File properties
print("\nFile properties:")
stat = os.stat(file_path)
print(f"Size: {stat.st_size} bytes")
print(f"Created: {datetime.fromtimestamp(stat.st_ctime)}")
print(f"Modified: {datetime.fromtimestamp(stat.st_mtime)}")

print("\n=== Pattern Matching ===")
# Create some files for pattern matching
patterns = ['test.txt', 'test.jpg', 'data.csv', 'config.json']
for file in patterns:
    path = os.path.join(temp_dir, file)
    with open(path, 'w') as f:
        f.write("dummy content")

# Using glob
print("\nGlob patterns:")
print("All files:", glob.glob(os.path.join(temp_dir, '*')))
print("Text files:", glob.glob(os.path.join(temp_dir, '*.txt')))
print("All test files:", glob.glob(os.path.join(temp_dir, 'test.*')))

print("\n=== File Copying and Moving ===")
# Copy file
src = os.path.join(temp_dir, 'test.txt')
dst = os.path.join(temp_dir, 'test_backup.txt')
shutil.copy2(src, dst)
print(f"Copied {src} to {dst}")

# Move file
new_name = os.path.join(temp_dir, 'test_renamed.txt')
os.rename(dst, new_name)
print(f"Moved {dst} to {new_name}")

print("\n=== Directory Operations with shutil ===")
# Copy directory
src_dir = temp_dir
dst_dir = f"{temp_dir}_backup"
shutil.copytree(src_dir, dst_dir)
print(f"Copied directory {src_dir} to {dst_dir}")

# Get directory size
def get_dir_size(path):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

print(f"Directory size: {get_dir_size(temp_dir)} bytes")

print("\n=== Cleanup ===")
# Remove directories and their contents
shutil.rmtree(temp_dir)
shutil.rmtree(dst_dir)
print("Cleaned up temporary directories")

print("\n=== Best Practices ===")
print("1. Use os.path.join() for paths")
print("2. Check file existence before operations")
print("3. Use context managers for file operations")
print("4. Handle permissions and exceptions")
print("5. Use pathlib for modern path operations")
print("6. Clean up temporary files")
print("7. Use appropriate file modes")
print("8. Consider platform differences")