# Key Concepts:
# Class: Defines the structure and behavior.
# Object: An instance of a class that follows the structure defined by the class.

# Defining the class
class Car:
    # Constructor method to initialize attributes
    def __init__(self, brand, model, year):
        self.brand = brand  # Attribute for the brand of the car
        self.model = model  # Attribute for the model of the car
        self.year = year    # Attribute for the manufacturing year
    
    # Method to display car details
    def display_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year})")

# Creating objects (instances of the class)
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)

# Accessing attributes and methods
car1.display_info()  
car2.display_info() 

print("----------------------------------------------------------------")
# Explanation:
# Class Declaration: The Car class is defined with attributes brand, model, and year.
# Constructor Method (__init__): Initializes the object's attributes when it is created.
# Objects: car1 and car2 are instances of the Car class with specific attributes.
# Method: display_info() is a method to print the details of the car.
