# 1. for Loop
# The for loop is used to iterate over a sequence (like a list, tuple, string, or range). It runs a block of code for each item in the sequence.

# Example 1: printing list uisng for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
print("-----------------------------------------------------------------------------")
# Example 2: Using range() function
# The range() function generates a sequence of numbers, which is often used with for loops.
print("Using range() function : ")
for i in range(5):  # Iterates over numbers 0 to 4
    print(i)

print("-----------------------------------------------------------------------------")
# 2. while Loop
# The while loop repeatedly executes a block of code as long as a condition is True.
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count by 1

print("-----------------------------------------------------------------------------")
# Example 2: Infinite while loop (with a break)
# If you forget to update the condition or add a way to break the loop, it will run indefinitely. You can use the break statement to exit the loop.
count = 0
while True:  # Infinite loop
    print(count)
    count += 1
    if count == 5:
        break  # Break the loop when count reaches 5


print("-----------------------------------------------------------------------------")
# 3. break and continue Statements
# break: Exits the loop entirely.
# continue: Skips the current iteration and moves to the next iteration.

# Using break
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)

print("-----------------------------------------------------------------------------")
# Using continue
for i in range(5):
    if i == 3:
        continue  # Skip the current iteration when i equals 3
    print(i)

print("-----------------------------------------------------------------------------")
# 4. Nested Loops
# You can also have loops inside loops. These are called nested loops.
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

print("-----------------------------------------------------------------------------")
# Summary of Loops:
# for loop: Best used when you know the number of iterations or want to iterate over a sequence.
# while loop: Best used when you don't know how many iterations you'll need, and you want the loop to continue while a condition is True.
# break: Exits the loop.
# continue: Skips the current iteration.
# Nested Loops: A loop inside another loop to handle more complex iteration scenarios.