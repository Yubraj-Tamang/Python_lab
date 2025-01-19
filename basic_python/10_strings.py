# 1. Creating a String
# Strings can be created using single quotes ', double quotes ", or triple quotes ''' or """ (for multi-line strings).

# Single-line strings
string1 = 'Hello'
string2 = "World"

# Multi-line string
string3 = '''This is
a multi-line
string.'''

print(string1) 
print(string2)  
print(string3)

print("-----------------------------------------------------------------------")
# 2. Accessing String Characters
# You can access characters in a string using indexing (0-based). Negative indexing allows access from the end of the string.
my_string = "Python"
print(my_string[0])  
print(my_string[-1]) 

print("-----------------------------------------------------------------------")
# 3. Slicing Strings
# You can extract parts of a string using slicing. The syntax is string[start:end:step].
my_string = "Python"
print(my_string[0:3])   # Pyt (from index 0 to 2)
print(my_string[:4])    # Pyth (from start to index 3)
print(my_string[2:])    # thon (from index 2 to end)
print(my_string[::2])   # Pto (every 2nd character)

print("-----------------------------------------------------------------------")
# 4. String Immutability
# Strings are immutable, meaning you cannot change their characters directly.
my_string = "Hello"
# my_string[0] = "J"  # This will raise a TypeError

print("-----------------------------------------------------------------------")
# 5. String Concatenation and Repetition
# You can combine strings using + and repeat them using *.
string1 = "Hello"
string2 = "World"
print(string1 + " " + string2)  
print(string1 * 3)            

print("-----------------------------------------------------------------------")
# 6. String Methods
# Strings have several built-in methods for operations.
my_string = "  Hello, Python!  "

# Changing case
print(my_string.lower())       #"  hello, python!  "
print(my_string.upper())       #"  HELLO, PYTHON!  "
print(my_string.capitalize())  #"  hello, python!  "

# Removing spaces
print(my_string.strip())       #"Hello, Python!" (removes leading/trailing spaces)

# Finding and replacing
print(my_string.find("Python"))  #9 (index of "Python")
print(my_string.replace("Python", "World"))  #"  Hello, World!  "

# Splitting and joining
words = my_string.split(",")   # Splits at ","
print(words)                   # ['  Hello', ' Python!  ']

joined = " ".join(words)       # Joins list into a string
print(joined)                  #"  Hello  Python!  "

print("-----------------------------------------------------------------------")
# 7. String Formatting
# Python provides multiple ways to format strings.

# Using f-strings (Python 3.6+)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Using .format()
print("My name is {} and I am {} years old.".format(name, age))

# Using % formatting
print("My name is %s and I am %d years old." % (name, age))

print("-----------------------------------------------------------------------")
# 8. Checking String Membership
# You can use the in and not in operators to check for substrings.
my_string = "Python programming"
print("Python" in my_string)  
print("Java" not in my_string)  

print("-----------------------------------------------------------------------")
# 9. String Escape Characters
# Escape characters allow special characters in strings. They start with a backslash \.
print("Hello\nWorld")  # New line

print("Tab\tSpace")  # Tab space

print("Quote: \"Hello\"")  # Quote: "Hello"

print("-----------------------------------------------------------------------")
# 10. Iterating Through a String
# You can iterate through a string using a for loop.
my_string = "Python"
for char in my_string:
    print(char)

print("-----------------------------------------------------------------------")
# Summary of Strings:
# Immutable: Cannot be changed after creation.
# Indexed: Allows access to individual characters using indexing.
# Methods: Provides powerful tools for string manipulation.
# Versatile: Supports slicing, formatting, concatenation, and more.