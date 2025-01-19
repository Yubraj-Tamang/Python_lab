# Contact Management System Requirements: 
* Description: A program to add, search, update, and delete contact information.

1. **Features:**
    - Add a new contact (name, phone number, and email).
    - Search for a contact by name.
    - Update the details of an existing contact.
    - Delete a contact.
    - Display all saved contacts.

# Documentation: Contact Management System

## Overview
The Contact Management System is a simple Python program that allows users to manage contacts efficiently. Users can add, search, update, delete, and display contacts.

## Features
1. **Add Contact**: Add a new contact with name, phone number, and email.
2. **Search Contact**: Search for a contact by name.
3. **Update Contact**: Modify the phone number and email of an existing contact.
4. **Delete Contact**: Remove a contact by name.
5. **Display All Contacts**: List all saved contacts.

## Functionalities

### 1. Add Contact
- **Input**: Name, phone number, and email.
- **Output**: Confirmation of successful addition.

### 2. Search Contact
- **Input**: Name of the contact to search.
- **Output**: Contact details if found, otherwise an error message.

### 3. Update Contact
- **Input**: Name of the contact to update, new phone number, and new email.
- **Output**: Confirmation of successful update or an error message if the contact does not exist.

### 4. Delete Contact
- **Input**: Name of the contact to delete.
- **Output**: Confirmation of successful deletion or an error message if the contact does not exist.

### 5. Display All Contacts
- **Output**: A list of all saved contacts with their details.

## Sample Code
```python
# Contact Management System
contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact {name} added successfully!")

def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]['Phone']}, Email: {contacts[name]['Email']}")
    else:
        print("Contact not found!")

def update_contact():
    name = input("Enter the name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name] = {"Phone": phone, "Email": email}
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")

def display_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")
    else:
        print("No contacts to display.")

# Menu
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        update_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        display_contacts()
    elif choice == 6:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
```

## How to Run
1. Run the file or execute in python interpreter (`CMS_run.py`).
3. Use the menu to interact with the Contact Management System.

## Example Interaction
```
Contact Management System
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. Display All Contacts
6. Exit
Enter your choice: 1
Enter contact name: Yubraj Tamang
Enter phone number: 98000000000
Enter email: yt60015@gmail.com
Contact John Doe added successfully!