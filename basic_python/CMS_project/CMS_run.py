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
