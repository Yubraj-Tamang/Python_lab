# 1. Creating a Dictionary
# Dictionaries are created using curly braces {} with key-value pairs separated by colons :.
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(my_dict)  

print("-------------------------------------------------------------------------------------")
# 2. Accessing Values
# Values in a dictionary can be accessed using their keys.
print(my_dict["name"])  
print(my_dict["age"])   

print("-------------------------------------------------------------------------------------")
# 3. Using the get() Method
# The get() method is another way to access values. It allows you to specify a default value if the key does not exist.
print(my_dict.get("city"))       
print(my_dict.get("country", "Unknown"))  

print("-------------------------------------------------------------------------------------")
# 4. Adding or Updating Elements
# You can add a new key-value pair or update the value of an existing key.
my_dict["country"] = "USA"  # Adding a new key-value pair
my_dict["age"] = 26         # Updating the value of an existing key
print(my_dict)

print("-------------------------------------------------------------------------------------")
# 5. Removing Elements
# You can remove elements from a dictionary using methods like pop(), popitem(), or del.

#  Using pop()
removed_value = my_dict.pop("city")  # Removes the key and returns the value
print(removed_value) 
print(my_dict)       

#  Using popitem() (removes the last inserted key-value pair in Python 3.7+)
my_dict.popitem()
print(my_dict)

# Using del
del my_dict["age"]  
print(my_dict)      

print("-------------------------------------------------------------------------------------")
# 6. Dictionary Methods
# Here are some commonly used dictionary methods:
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict.keys())    
print(my_dict.values())  
print(my_dict.items())  

print("-------------------------------------------------------------------------------------")
# 7. Iterating Over a Dictionary
# You can iterate through a dictionary using a for loop.
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25
# city: New York

print("-------------------------------------------------------------------------------------")
# 8. Nested Dictionaries
# Dictionaries can contain other dictionaries as values, creating a nested structure.
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(nested_dict["person1"]["name"])  
print(nested_dict["person2"]["name"])

print("-------------------------------------------------------------------------------------")
# 9. Checking for Keys
# You can check if a key exists in a dictionary using the in keyword.
if "name" in my_dict:
    print("Name exists in the dictionary.")

print("-------------------------------------------------------------------------------------")
# 10. Dictionary Comprehension
# You can create dictionaries dynamically using dictionary comprehension.
squares = {x: x**2 for x in range(5)}
print(squares)  

print("-------------------------------------------------------------------------------------")
# Summary of Dictionaries:
# Key-Value Pairs: Data is stored in the form of key-value pairs.
# Mutable: You can add, update, and remove key-value pairs.
# Keys Must Be Unique: No two keys can have the same value.
# Unordered: In Python 3.7+, dictionaries maintain insertion order by default.
# Efficient Lookup: Accessing values by key is fast and efficient.