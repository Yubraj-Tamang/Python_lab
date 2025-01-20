# arguments: The parameters you pass to the function (can be zero or more).
# expression: A single expression that is evaluated and returned.
# syntax
# lambda arguments: expression

# Basic Lambda Function
# A lambda function that adds two numbers
add = lambda x, y: x + y

# Using the lambda function
result = add(3, 5)
print("Result of addition:", result)

print("------------------------------------------------------------------------------")
# Lambda Function for Sorting
# You can use a lambda function for custom sorting, especially with lists of tuples.
# List of tuples
points = [(1, 2), (3, 4), (0, 1), (5, 6)]

# Sort points by the second element of each tuple
sorted_points = sorted(points, key=lambda x: x[1])

print("Sorted points:", sorted_points)


print("------------------------------------------------------------------------------")
# Lambda Function with map()
# The map() function applies a lambda function to all items in an iterable (like a list).
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Squared numbers:", squared_numbers)

print("------------------------------------------------------------------------------")
# Lambda Function with filter()
# The filter() function filters elements from an iterable based on a condition defined by a lambda function.
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)


print("------------------------------------------------------------------------------")
# Lambda Function with reduce()
# The reduce() function from the functools module can be used with a lambda to cumulatively apply a function to the elements in a sequence.
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4]

# Using reduce to multiply all numbers
product = reduce(lambda x, y: x * y, numbers)

print("Product of all numbers:", product)


print("------------------------------------------------------------------------------")
# Key Points:
# Lambda functions are anonymous and often used for short-term operations.
# They are mostly used in combination with functions like map(), filter(), and reduce(), or for quick operations that don’t require a full function definition.
# Unlike regular functions defined with def, lambda functions can only contain a single expression.