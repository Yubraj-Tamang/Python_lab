# Key Concepts
# try: Block where you write code that might raise an exception.
# except: Block where you handle the exception if it occurs.
# else: Optional block executed if no exception occurs.
# finally: Optional block executed no matter what (useful for cleanup operations).

# Basic Exception Handling
try:
    num = int(input("Enter a number: "))
    print("The number you entered is:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")


print("--------------------------------------------------------------------------")
# Handling Multiple Exceptions
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

print("--------------------------------------------------------------------------")
#  Using else and finally
try:
    with open("sample.txt", "r") as file:
        data = file.read()
    print("File content:")
    print(data)
except FileNotFoundError:
    print("The file does not exist.")
else:
    print("File read successfully!")
finally:
    print("Execution of file operation complete.")

# else: Executes if no exception occurs.
# finally: Always executes, regardless of whether an exception occurs.

print("--------------------------------------------------------------------------")
# Raising Exceptions
def check_positive(number):
    if number < 0:
        raise ValueError("The number must be positive!")
    return f"Number is valid: {number}"

try:
    num = int(input("Enter a positive number: "))
    print(check_positive(num))
except ValueError as e:
    print("Error:", e)

print("--------------------------------------------------------------------------")
# Best Practices
# Handle specific exceptions instead of using a general except clause.
# Use finally for cleanup tasks, like closing files or releasing resources.
# Avoid overusing exceptions for control flow; use them for unexpected scenarios only.