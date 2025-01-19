# 1. Defining a Function
# You define a function using the def keyword, followed by the function name, parentheses (optionally with parameters), and a colon. The code inside the function must be indented.

# simple function that print greeting!
def greet():
    print("Hello, World!")

greet()  # Calling the function

print("---------------------------------------------------------------------------------")
# 2. Function with Parameters
# Functions can accept parameters (also called arguments) to work with data passed into them.

# A function that take two parameters
def add(a, b):
    result = a + b
    return result

sum_result = add(3, 5)
print(sum_result)

print("---------------------------------------------------------------------------------")
# 3. Default Parameters
# You can provide default values for parameters, which will be used if no argument is passed for that parameter.

# A function with default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

# calling function
greet()           
greet("Alice")  

print("---------------------------------------------------------------------------------")
# 4. Return Statement
# A function can return a value using the return keyword. Once return is executed, the function ends, and the value is returned to the caller.

# A function with return value
def multiply(a, b):
    return a * b

result = multiply(4, 6)
print(result)  

print("---------------------------------------------------------------------------------")
# 5. Variable Scope
# The scope of a variable refers to where it can be accessed in the code. Variables defined inside a function are local to that function and cannot be accessed outside of it. Variables defined outside of any function are global and can be accessed anywhere.

# local and global variable
x = 10  # Global variable

def show():
    x = 5  # Local variable
    print(f"Inside function: {x}")

show()  
print(f"Outside function: {x}")  
# 6. Keyword Arguments
# In Python, you can pass arguments to a function by explicitly naming them. This is useful when you want to pass arguments in a different order or make your code more readable.

# using keyword arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=25, name="John") 

print("---------------------------------------------------------------------------------")
# 7. Arbitrary Arguments (Varargs)
# Sometimes you may not know how many arguments will be passed to your function. You can use *args to pass a variable number of non-keyword arguments, or **kwargs to pass a variable number of keyword arguments.

# using args for non keyword argument
def add(*args):
    return sum(args)

result = add(1, 2, 3, 4)
print(result)  

print("---------------------------------------------------------------------------------")
# Using **kwargs for keyword arguments
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=30) 

print("---------------------------------------------------------------------------------")
# 8. Lambda Functions (Anonymous Functions)
# Lambda functions are small, anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have one expression.

# A lambda function for addition
add = lambda a, b: a + b
print(add(3, 5)) 

print("---------------------------------------------------------------------------------")
# 9. Recursion
# A function is recursive if it calls itself. Recursion is useful for problems that can be broken down into smaller, similar problems, such as calculating factorials.

# A recursive function to calculate factorial
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  

print("---------------------------------------------------------------------------------")
# Summary of Functions:
# Defining a function: Use the def keyword.
# Parameters: Functions can accept inputs via parameters.
# Return value: Functions can return results using the return keyword.
# Default parameters: Provide default values for parameters.
# Keyword arguments: Pass arguments explicitly by name.
# Arbitrary arguments: Use *args or **kwargs for a variable number of arguments.
# Lambda functions: Anonymous functions for simple operations.
# Recursion: Functions that call themselves to solve problems.
