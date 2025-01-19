# 1. Output in Python
# The print() function is used to display output on the console.

# Printing a string
print("Hello, World!")  

# Printing multiple items
name = "Alice"
age = 25
print("Name:", name, "Age:", age) 

# The sep parameter specifies how to separate multiple items.
print("Python", "is", "fun", sep="-")  

# The end parameter changes the string appended after the printed content (default is a newline).
print("Hello", end=" ")
print("World!") 

print("--------------------------------------------------------------------")
# 2. Input in Python
# The input() function allows the user to input data from the console as a string.

# Taking input as a string
name = input("Enter your name: ")
print("Hello, " + name + "!")

# By default, input() returns a string. You can convert it to another data type (e.g., int or float) if needed.

# Taking input as an integer
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Taking input as a float
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

print("--------------------------------------------------------------------")
# 3. Taking Multiple Inputs
# You can use split() to take multiple inputs in a single line.

# Taking two inputs separated by a space
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)

# Type Conversion:
# Taking multiple integers
x, y = map(int, input("Enter two numbers separated by space: ").split())
print("Sum:", x + y)

print("--------------------------------------------------------------------")
# 4. Formatted Output
# Python provides several ways to format strings for output.

# Using f-strings (Python 3.6+)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Using .format()
print("My name is {} and I am {} years old.".format(name, age))

# Using % Formatting
print("My name is %s and I am %d years old." % (name, age))

print("--------------------------------------------------------------------")
# 5. Reading from and Writing to Files
# Python allows reading input from and writing output to files.

# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, File!")

# Reading file
# Reading from a file
with open("output.txt", "r") as file:
    content = file.read()
    print(content) 

print("--------------------------------------------------------------------")
# Summary:
# Output: Use print() with optional parameters (sep, end) for customized output.
# Input: Use input() to take user input (always as a string). Convert to other data types if needed.
# File I/O: Use open() with modes (r, w, a) for reading and writing files.
# Formatting: Use f-strings, .format(), or % for formatted output.
