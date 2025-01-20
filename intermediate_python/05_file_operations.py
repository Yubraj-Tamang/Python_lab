# Key Operations
# Open a file: Use open() with modes like r (read), w (write), a (append), etc.
# Read from a file: Use methods like read(), readline(), or readlines().
# Write to a file: Use write() or writelines().
# Close a file: Use close() or manage files with with to automatically close them.
# File modes:
# 'r': Read mode (default).
# 'w': Write mode (overwrites existing content).
# 'a': Append mode.
# 'rb'/'wb': Binary read/write.

# Reading a File
# Create a sample file for demonstration
with open("sample.txt", "w") as file:
    file.write("Hello, World!\nWelcome to Python file operations.")

# Reading the file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

print("----------------------------------------------------")
# Writing to a File
# Writing to a new file
with open("sample.txt", "w") as file:
    file.write("This is a new file created using Python.\n")
    file.write("You can write multiple lines using write().")

print("sample.txt")

print("----------------------------------------------------")
# Appending to a File
# Appending content to an existing file
with open("sample.txt", "a") as file:
    file.write("\nAppending this line to the file.")

print("Content appended to sample.txt")


print("----------------------------------------------------")
# Reading File Line by Line
with open("sample.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())
print("----------------------------------------------------")
#  Working with Binary Files
# Writing binary data
with open("binary_file.bin", "wb") as file:
    file.write(b'\x48\x65\x6c\x6c\x6f')

# Reading binary data
with open("binary_file.bin", "rb") as file:
    binary_content = file.read()
    print("Binary content:", binary_content)


print("----------------------------------------------------")
# Checking if a File Exists
import os

file_name = "sample.txt"

if os.path.exists(file_name):
    print(f"{file_name} exists.")
else:
    print(f"{file_name} does not exist.")

# Best Practices
# Always use with for file operations to ensure proper resource cleanup.
# Check if a file exists before performing operations using os.path.exists().
# Use exception handling (try-except) for robust error handling when working with files.
# Use binary mode ('b') for non-text files like images or videos.
