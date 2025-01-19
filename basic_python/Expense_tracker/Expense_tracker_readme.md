# Documentation: Expense Tracker

## Overview
The Expense Tracker is a Python program that helps users track and manage their daily expenses. Users can record expenses by category and amount, view the total expenses, and display expenses categorized for better understanding.

## Features
1. **Add Expense**: Record a new expense by specifying the category and amount.
2. **Display Total Expenses**: View the total amount spent.
3. **Display Expenses by Category**: See a breakdown of expenses grouped by categories.
4. **User-Friendly Interface**: Menu-driven program for easy interaction.

## Functionalities

### 1. Add Expense
- **Input**: Category (e.g., Food, Transport, Entertainment) and amount.
- **Output**: Confirms the addition of the expense.

### 2. Display Total Expenses
- **Output**: Displays the sum of all expenses recorded.

### 3. Display Expenses by Category
- **Output**: Shows the amount spent in each category.

## Sample Code
```python
# Expense Tracker
expenses = {}

def add_expense():
    category = input("Enter the expense category (e.g., Food, Transport): ")
    amount = float(input("Enter the expense amount: "))
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    print(f"Added expense: {category} - Rs {amount:.2f}")

def display_total_expenses():
    total = sum(expenses.values())
    print(f"Total expenses: Rs {total:.2f}")

def display_expenses_by_category():
    if expenses:
        for category, amount in expenses.items():
            print(f"{category}: Rs {amount:.2f}")
    else:
        print("No expenses recorded yet.")

# Menu
def expense_tracker():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Display Total Expenses")
        print("3. Display Expenses by Category")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_expense()
        elif choice == 2:
            display_total_expenses()
        elif choice == 3:
            display_expenses_by_category()
        elif choice == 4:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

expense_tracker()
```

## How to Run
1. Run the file or execute in python interpreter (`expense_tracker.py`).
3. Use the menu to interact with the Expense Tracker.

## Example Interaction
```
Expense Tracker
1. Add Expense
2. Display Total Expenses
3. Display Expenses by Category
4. Exit
Enter your choice: 1
Enter the expense category (e.g., Food, Transport): Food
Enter the expense amount: 25.50
Added expense: Food - Rs 25.50

Enter your choice: 2
Total expenses: Rs 25.50

Enter your choice: 3
Food: Rs 25.50

Enter your choice: 4
Exiting... Goodbye!
```

## Key Topics Covered
- **Dictionaries**: Used to store expenses categorized by type.
- **Loops**: For menu-driven interaction and processing user input.
- **Conditionals**: To handle user choices and ensure valid inputs.
- **Input/Output**: For user interaction.

## Customization Ideas
- Add date tracking for each expense.
- Allow editing or deleting specific expenses.
- Generate reports for weekly or monthly spending.
- Add a graphical interface using libraries like Tkinter or PyQt.

The Expense Tracker is a useful project for managing daily expenses while practicing Python programming concepts.
