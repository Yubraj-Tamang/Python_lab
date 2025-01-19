# 1. Creating a Tuple
# Tuples are created by placing elements inside parentheses (), separated by commas.
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)  

print("-----------------------------------------------------------------------------")
# 2. Accessing Tuple Elements
# You can access elements in a tuple using their index. Python indexing starts from 0.
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])  
print(my_tuple[1])  

print("-----------------------------------------------------------------------------")
# 3. Negative Indexing
# Negative indexing can be used to access elements from the end of the tuple.
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[-1])  
print(my_tuple[-2])  

print("-----------------------------------------------------------------------------")
# 4. Slicing a Tuple
# You can slice a tuple to get a part of it. The syntax for slicing is tuple[start:end], where start is the index to begin from (inclusive), and end is the index to stop (exclusive).
my_tuple = ("apple", "banana", "cherry", "date", "elderberry")
print(my_tuple[1:4])  

print("-----------------------------------------------------------------------------")
# 5. Concatenating Tuples
# You can concatenate two or more tuples using the + operator.
tuple1 = ("apple", "banana")
tuple2 = ("cherry", "date")
combined_tuple = tuple1 + tuple2
print(combined_tuple)  

print("-----------------------------------------------------------------------------")
# 6. Repeating Elements in a Tuple
# You can repeat the elements in a tuple by multiplying the tuple using the * operator.
my_tuple = ("apple", "banana")
repeated_tuple = my_tuple * 3
print(repeated_tuple) 

print("-----------------------------------------------------------------------------")
# 7. Immutability of Tuples
# Tuples are immutable, meaning their elements cannot be changed after they are created.
my_tuple = ("apple", "banana", "cherry")
# Trying to change an element will raise an error
# my_tuple[1] = "blueberry"  # This will raise a TypeError

print("-----------------------------------------------------------------------------")
# 8. Tuple with One Element
# To create a tuple with only one element, you must include a trailing comma.
single_element_tuple = ("apple",)
print(single_element_tuple) 

# Without the comma, it will be treated as a string:
not_a_tuple = ("apple")
print(type(not_a_tuple))

print("-----------------------------------------------------------------------------")
# 9. Tuple Packing and Unpacking
# Packing: When you create a tuple by grouping values together.
# Unpacking: When you assign values from a tuple to individual variables.

# Tuple Packing
my_tuple = ("apple", "banana", "cherry")

# Tuple Unpacking
my_tuple = ("apple", "banana", "cherry")
a, b, c = my_tuple  # Unpacking the tuple into variables
print(a)  
print(b) 
print(c)  

print("-----------------------------------------------------------------------------")
# 10. Nested Tuples
# A tuple can contain other tuples as elements, creating a nested structure.
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0][0]) 
print(nested_tuple[1][0])  # (Accessing the first element of the second tuple)
print(nested_tuple[2][0])

print("-----------------------------------------------------------------------------")
# 11. Tuple Methods
# Some commonly used tuple methods include:
# count(): Returns the number of occurrences of a specified element in the tuple.
# index(): Returns the index of the first occurrence of a specified element.
my_tuple = ("apple", "banana", "cherry", "banana")
print(my_tuple.count("banana"))  
print(my_tuple.index("cherry"))  


print("-----------------------------------------------------------------------------")
# Summary of Tuples:
# Ordered and Indexed: Tuples maintain the order of elements and use 0-based indexing.
# Immutable: Once a tuple is created, its elements cannot be modified, added, or removed.
# Heterogeneous: Tuples can store elements of different data types.
# Slicing and Accessing: You can access parts of a tuple using slicing or indexing, including negative indexing.
# Packing and Unpacking: You can pack multiple elements into a tuple and unpack them into variables.
