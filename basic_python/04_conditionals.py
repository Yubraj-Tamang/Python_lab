# 1. if Statement
# The if statement is used to test a condition and execute the code block if the condition is True.
age = 18
if age >= 18:
    print("You are an adult.")

print("---------------------------------------------------------------------------")
# 2. else Statement
# The else statement is used to define a block of code that will run if the condition in the if statement is False.
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

print("---------------------------------------------------------------------------")
# 3. elif Statement
# The elif (short for "else if") statement allows you to check multiple conditions. It is useful when you have more than two possible outcomes.
age = 20
if age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

print("---------------------------------------------------------------------------")
# 4. Nested Conditionals
# You can also nest if, elif, and else statements within each other to check multiple levels of conditions.
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")

print("---------------------------------------------------------------------------")
# 5. Conditional Expressions (Ternary Operator)
# Python supports a shorthand for if-else statements, known as the ternary operator or conditional expression. It allows you to choose between two values based on a condition.
age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)

print("---------------------------------------------------------------------------")
# Summary of Conditionals:
# if: Executes the block of code if the condition is True.
# else: Executes the block of code if the condition is False.
# elif: Checks additional conditions if the previous if or elif conditions are False.
# Nested Conditionals: Allows conditions inside other conditions.
# Ternary Operator: A shorthand for simple if-else expressions.
