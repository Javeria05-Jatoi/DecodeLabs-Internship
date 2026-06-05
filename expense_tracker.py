expenses = []
total = 0

print("--- Expense Tracker ---")

while True:
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Quit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        category = input("Enter category (Food/Transport/Shopping/Other): ")
        try:
            amount = float(input("Enter amount: "))
            expenses.append({"category": category, "amount": amount})
            total += amount
            print(f"Added! {category}: {amount:.2f}")
        except ValueError:
            print("Invalid amount! Please enter a number.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet!")
        else:
            print("\n--- All Expenses ---")
            for index, expense in enumerate(expenses, 1):
                print(f"{index}. {expense['category']}: {expense['amount']:.2f}")

    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses yet!")
        else:
            highest = max(expenses, key=lambda x: x["amount"])
            print(f"\n--- Summary ---")
            print(f"Total Expenses: {len(expenses)}")
            print(f"Total Spent: {total:.2f}")
            print(f"Highest Expense: {highest['category']} - {highest['amount']:.2f}")

    elif choice == "4":
        print(f"\nGoodbye! Total Spent: {total:.2f}")
        break

    else:
        print("Invalid choice! Try again.")