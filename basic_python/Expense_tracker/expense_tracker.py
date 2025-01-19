# Expense Tracker
expenses = []

def add_expense():
    category = input("Enter the expense category (e.g., Food, Transport): ")
    amount = float(input("Enter the expense amount: "))
    expenses.append({"Category": category, "Amount": amount})
    print(f"Added expense: {category} - Rs {amount}")

def display_total_expenses():
    total = sum(expense["Amount"] for expense in expenses)
    print(f"Total expenses: Rs {total:.2f}")

def display_expenses_by_category():
    categories = {}
    for expense in expenses:
        if expense["Category"] in categories:
            categories[expense["Category"]] += expense["Amount"]
        else:
            categories[expense["Category"]] = expense["Amount"]
    for category, amount in categories.items():
        print(f"{category}: Rs {amount:.2f}")

# Menu
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
        print("Invalid choice! Try again.")
