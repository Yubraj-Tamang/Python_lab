# 1. Creating a List
# Lists are created by placing elements inside square brackets [], separated by commas.
fruits = ["apple", "banana", "cherry"]
print(fruits)  

print("--------------------------------------------------------------")
# 2. Accessing List Elements
# You can access individual elements in a list using their index. Remember, Python indexing starts from 0.
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  
print(fruits[1])  

print("--------------------------------------------------------------")
# 3. Negative Indexing
# You can also use negative indexing to access elements from the end of the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])  
print(fruits[-2])  

print("--------------------------------------------------------------")
# 4. Slicing a List
# You can slice a list to get a part of it. The syntax for slicing is list[start:end], where start is the index to begin from (inclusive), and end is the index to stop (exclusive).
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[1:4]) 

print("--------------------------------------------------------------")
# 5. Changing List Elements
# Since lists are mutable, you can change the value of an element by accessing it through its index and assigning a new value.
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  

print("--------------------------------------------------------------")
# 6. Adding Elements to a List
# You can add elements to a list using append(), insert(), or extend().

# Using append() to add an element to the end
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  

# Using insert() to add an element at a specific index
fruits = ["apple", "banana"]
fruits.insert(1, "orange")  # Insert at index 1
print(fruits)  

# Using extend() to add multiple elements
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  

print("--------------------------------------------------------------")
# 7. Removing Elements from a List
# You can remove elements using methods like remove(), pop(), or del.

# Using remove() to remove the first occurrence of a value
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

# Using pop() to remove an element at a specific index (or the last element if no index is specified)
fruits = ["apple", "banana", "cherry"]
popped_fruit = fruits.pop(1)  # Remove element at index 1
print(fruits)  
print(f"Removed: {popped_fruit}")  

# Using del to remove an element by index or delete the whole list
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)  

# To delete the entire list:
del fruits
# print(fruits)  # This will raise an error because the list no longer exists

print("--------------------------------------------------------------")
# 8. List Comprehensions
# List comprehensions allow you to create new lists by applying an expression to each item in an existing list.
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers) 

print("--------------------------------------------------------------")
# 9. Nested Lists
# Lists can contain other lists as elements, creating a nested structure.
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[0][0])  
print(nested_list[1][0])  #(Accessing the first element of the second inner list)
print(nested_list[2][0])


print("--------------------------------------------------------------")
# 10. List Methods
# Some commonly used list methods include:
# len(): Returns the number of elements in the list.
# sort(): Sorts the list in ascending order.
# reverse(): Reverses the order of elements in the list.
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(numbers)) 

numbers.sort()
print(numbers)  

numbers.reverse()
print(numbers)  


print("--------------------------------------------------------------")
# Summary of Lists:
# Ordered and Indexed: Lists preserve the order of elements and use 0-based indexing.
# Mutable: Lists can be modified by adding, removing, or changing elements.
# Heterogeneous: Lists can store elements of different data types.
# Slicing and Accessing: You can access parts of a list using slicing or indexing, including negative indexing.
