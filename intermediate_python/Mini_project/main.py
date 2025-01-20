import os
from datetime import datetime

# Function to add an expense
def add_expense(file_name, category, amount):
    date_today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, 'a') as file:
        file.write(f"{date_today},{category},{amount}\n")
    print(f"Expense of Rs {amount} for category '{category}' added.")

# Function to read all expenses
def view_expenses(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            expenses = file.readlines()
        if expenses:
            print("All Expenses:")
            for expense in expenses:
                print(expense.strip())
        else:
            print("No expenses logged yet.")
    else:
        print("No expense file found.")

# Function to filter expenses by category
def filter_by_category(file_name, category):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            expenses = file.readlines()
        filtered_expenses = [exp for exp in expenses if category.lower() in exp.lower()]
        if filtered_expenses:
            print(f"Expenses for category '{category}':")
            for expense in filtered_expenses:
                print(expense.strip())
        else:
            print(f"No expenses found for category '{category}'.")
    else:
        print("No expense file found.")

# Function to calculate total expenses for the day
def total_expenses(file_name, date_filter=None):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            expenses = file.readlines()
        total = sum(float(exp.split(',')[2]) for exp in expenses if (date_filter is None or date_filter in exp))
        print(f"Total expenses: {total}")
    else:
        print("No expense file found.")

# Main function to run the expense tracker
def main():
    file_name = "expenses.txt"
    
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses by Category")
        print("4. Total Expenses")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category (e.g., Food, Transport, Entertainment): ")
            amount = float(input("Enter amount: "))
            add_expense(file_name, category, amount)
        elif choice == '2':
            view_expenses(file_name)
        elif choice == '3':
            category = input("Enter category to filter by: ")
            filter_by_category(file_name, category)
        elif choice == '4':
            date_filter = input("Enter a date (yyyy-mm-dd) to filter by, or press Enter to skip: ")
            date_filter = date_filter.strip() if date_filter else None
            total_expenses(file_name, date_filter)
        elif choice == '5':
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
