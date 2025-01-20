# Types of Comprehensions
# List Comprehension
# Set Comprehension
# Dictionary Comprehension
# Generator Expression
print("------------------------------------------------------------------------------")
# 1. List Comprehension
# List comprehensions allow you to create a new list by applying an expression to each item in an iterable (like a list or range).

# Creating a List of Squares
# Creating a list of squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)
# List Comprehension with a Condition
# Creating a list of even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

print("------------------------------------------------------------------------------")
# 2. Set Comprehension
# Set comprehensions are similar to list comprehensions, but they create sets (which automatically remove duplicates).

# Creating a Set of Squares
# Creating a set of squares from 1 to 5
square_set = {x**2 for x in range(1, 6)}
print(square_set)


print("------------------------------------------------------------------------------")
# 3. Dictionary Comprehension
# Dictionary comprehensions allow you to create dictionaries by using key-value pairs.

# Creating a Dictionary with Square Values
# Creating a dictionary where the key is the number and the value is its square
square_dict = {x: x**2 for x in range(1, 6)}
print(square_dict)


print("------------------------------------------------------------------------------")
# 4. Generator Expression
# A generator expression creates an iterator that yields items one by one, which is more memory efficient for large datasets.

# Generator Expression for Squares
# Generator expression for squares of numbers from 1 to 5
square_gen = (x**2 for x in range(1, 6))

# Converting the generator to a list and printing
print(list(square_gen))

print("------------------------------------------------------------------------------")
# Advantages of Comprehensions:
# Concise: They make code shorter and more readable.
# Efficient: Comprehensions are often faster than equivalent for loops, especially for large datasets.
# Readable: They allow you to express the intent of the operation in a single line.

print("------------------------------------------------------------------------------")
# Combining Conditions and Expressions
# Creating a list of squares of even numbers from 1 to 10
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)