import modules_packages

result = modules_packages.add(5, 3)
print("Addition:", result)  

print("PI:", modules_packages.PI)  

print("---------------------------------------------------------")
# also import specific items from a module:
from modules_packages import subtract

result = subtract(10, 4)
print("Subtraction:", result)  

# Benefits:
# Code Reusability: Import modules and packages into multiple projects.
# Organization: Helps in structuring large projects.
# Namespace Management: Prevents name conflicts.