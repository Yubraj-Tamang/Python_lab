# Key Concepts:
# Parent Class (Base Class): The class whose properties and methods are inherited.
# Child Class (Derived Class): The class that inherits from the parent class.
# Overriding: The child class can override methods from the parent class.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):  # Method overriding
        print(f"{self.name} barks.")

# Another child class inheriting from Animal
class Cat(Animal):
    def speak(self):  # Method overriding
        print(f"{self.name} meows.")

# Using the classes
animal = Animal("Generic Animal")
dog = Dog("Rover")
cat = Cat("Whiskers")

# Calling methods
animal.speak() 
dog.speak()    
cat.speak()     

print("---------------------------------------------------------------")
# Explanation:
# Parent Class (Animal):
# Defines a constructor (__init__) and a method (speak).
# Child Classes (Dog and Cat):
# Inherit from the Animal class.
# Override the speak method to provide specific behavior.
# Method Overriding:
# Each child class has its own implementation of the speak method, which replaces the parent's version.


print("---------------------------------------------------------------")
# 1. Single Inheritance
# A child class inherits from a single parent class.
class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):  # Single inheritance
    def speak(self):
        print("Dog barks.")

# Example usage
dog = Dog()
dog.speak() 


print("---------------------------------------------------------------")
# 2. Multiple Inheritance
# A child class inherits from more than one parent class.
class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

class Manager(Person, Employee):  # Multiple inheritance
    def __init__(self, name, employee_id):
        Person.__init__(self, name)
        Employee.__init__(self, employee_id)

# Example usage
manager = Manager("Alice", 101)
print(f"Name: {manager.name}, ID: {manager.employee_id}")


print("---------------------------------------------------------------")
# 3. Multilevel Inheritance
# A class inherits from a child class, making a chain of inheritance.
class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Mammal(Animal):  # Inherits from Animal
    def speak(self):
        print("Mammal makes a sound.")

class Dog(Mammal):  # Inherits from Mammal
    def speak(self):
        print("Dog barks.")

# Example usage
dog = Dog()
dog.speak()  

print("---------------------------------------------------------------")
# 4. Hierarchical Inheritance
# Multiple child classes inherit from the same parent class.
class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):  # Inherits from Animal
    def speak(self):
        print("Dog barks.")

class Cat(Animal):  # Inherits from Animal
    def speak(self):
        print("Cat meows.")

# Example usage
dog = Dog()
cat = Cat()
dog.speak()  
cat.speak() 

print("---------------------------------------------------------------")
# 5. Hybrid Inheritance
# A combination of two or more types of inheritance. It usually involves multiple and hierarchical inheritance.
class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Mammal(Animal):
    def speak(self):
        print("Mammal makes a sound.")

class Bird(Animal):
    def speak(self):
        print("Bird chirps.")

class Bat(Mammal, Bird):  # Multiple and hierarchical inheritance
    def speak(self):
        print("Bat screeches.")

# Example usage
bat = Bat()
bat.speak()  



