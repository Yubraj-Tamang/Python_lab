# Introduction to variables and data types.

# variables are container that store the values in different data types

name = "Yubraj Tamang" # 'name' variable storing string "Yubraj Tamang"
print(name)

# To check data type we use type() method
print(type(name))

#1. Here are the Numeric type of data type

# Integer
x = 5  # int
print("Output: ",x)
print(type(x))

# Float
y = 3.14  # float
print("Output: ",y)
print(type(y))  

# Complex
z = 2 + 3j  # complex
print("Output: ",z)
print(type(z))  

# Numeric Types
# int: Integer values (whole numbers).
# float: Floating-point numbers (decimal numbers).
# complex: Complex numbers (numbers with real and imaginary parts).

print("-------------------------------------------------------------------------------------------")
#2. Here are the Squence type of data types:

# List
my_list = [1, 2, 3, 4, 5]  # list
print("Output: ",my_list)
print(type(my_list))  

# Tuple
my_tuple = (1, 2, 3)  # tuple
print("Output: ",my_tuple)
print(type(my_tuple))  

# Range
my_range = range(0, 10)  # range
print("Output: ",my_range)
print(type(my_range))  

#3. Sequence Types
# list: A mutable (changeable) ordered collection of items.
# tuple: An immutable ordered collection of items.
# range: A sequence of numbers, typically used in loops.

print("-------------------------------------------------------------------------------------------")
#4. Text Type
# str: A string, which is a sequence of characters.

# String
my_string = "Hello, World!"  # str
print("Output: ",my_string)
print(type(my_string)) 

print("-------------------------------------------------------------------------------------------")
#5. Mapping Type
# dict: A collection of key-value pairs (dictionary).

# Dictionary
my_dict = {"name": "Alice", "age": 25}  # dict
print(my_dict)
print(type(my_dict))  

print("-------------------------------------------------------------------------------------------")
#6. Set Types
# set: An unordered collection of unique items.
# frozenset: An immutable set.

# Set
my_set = {1, 2, 3, 4}  # set
print("Output: ",my_set)
print(type(my_set))  

# Frozenset
my_frozenset = frozenset([1, 2, 3, 4])  # frozenset
print("Output: ",my_frozenset)
print(type(my_frozenset)) 

print("-------------------------------------------------------------------------------------------")
# 6. Boolean Type
# bool: Represents the truth values True and False.

# Boolean
is_valid = True  # bool
print("Output: ",is_valid)
print(type(is_valid))  

print("-------------------------------------------------------------------------------------------")
#7. Binary Types
# bytes: Immutable sequence of bytes.
# bytearray: Mutable sequence of bytes.
# memoryview: A view object that exposes an array's buffer interface.

# Bytes
my_bytes = b"Hello"  # bytes
print("Output: ",my_bytes)
print(type(my_bytes))  

# Bytearray
my_bytearray = bytearray([65, 66, 67])  # bytearray
print("Output: ",my_bytearray)
print(type(my_bytearray))  


# Summary of Data Types:
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Text Type: str
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
