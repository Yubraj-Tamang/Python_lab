# 1. Arithmetic Operators
# These operators are used to perform basic arithmetic operations like addition, subtraction, multiplication, etc.
a = 5
b = 2

print(a + b)  
print(a - b)  
print(a * b)   
print(a / b)   
print(a // b) 
print(a % b)  
print(a ** b)  

print("-----------------------------------------------------------------------------")
#2. Comparison (Relational) Operators
# These operators are used to compare two values and return a boolean (True or False).
a = 5
b = 3

print(a == b) 
print(a != b) 
print(a > b)  
print(a < b)  
print(a >= b) 
print(a <= b) 

print("-----------------------------------------------------------------------------")
#3. Logical Operators
# These operators are used to combine conditional statements.
a = True
b = False

print(a and b)  
print(a or b)   
print(not a)    

print("-----------------------------------------------------------------------------")
# 4. Assignment Operators
# These operators are used to assign values to variables.
a = 5
a += 3  # a = a + 3
print(a)  

a *= 2  # a = a * 2
print(a)  

print("-----------------------------------------------------------------------------")
# 5. Identity Operators
# These operators are used to compare the memory locations of two objects.
a = [1, 2, 3]
b = a

print(a is b)      
print(a is not b)  

print("-----------------------------------------------------------------------------")
# 6. Membership Operators
# These operators are used to test if a value is found within a sequence (such as a list, tuple, or string).
my_list = [1, 2, 3, 4]

print(3 in my_list)   
print(5 not in my_list) 

print("-----------------------------------------------------------------------------")
# 7. Bitwise Operators
# These operators are used to perform bit-level operations on integers.
a = 5  # 101 in binary
b = 3  # 011 in binary

print(a & b)  #  1 (binary 001)
print(a | b)  #  7 (binary 111)

print("-----------------------------------------------------------------------------")
# Summary of Operators:
# Arithmetic Operators: +, -, *, /, //, %, **
# Comparison Operators: ==, !=, >, <, >=, <=
# Logical Operators: and, or, not
# Assignment Operators: =, +=, -=, *=, /=, //=, %= , **=
# Identity Operators: is, is not
# Membership Operators: in, not in
# Bitwise Operators: &, |, ^, ~, <<, >>