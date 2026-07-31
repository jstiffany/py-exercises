print("------------- Expenses Tracker -------------")

expenses_log = {
    "Charger": {"price": 12.00}
}

def add_expenses(expense, price):
    print("\nAdding expense...")

    if price < 0:
        print("Price cannot be lower than 0!")
        return

    expenses_log[expense] = {"price": price}
    print("\nExpense added!")

def remove_expense(expense):
    # easier way
    del_expense = expenses_log.pop(expense, "Item not found!")

    if del_expense == "Item not found!":
        print(f"{expense} was not found. Please try again.")

    else:
        print(f"{expense} was deleted.")

    return

def edit_expense(expense, type):
    if type == "1":
        pass

def search_expense(expense):
    if not expenses_log:
        print("\nNo expenses found.")

    else:
        print("\nSearching for expense...")

        if expense in expenses_log:
            print("Expense found!\n")
            print(expenses_log[expense])

        else:
            print("\nExpense not found.")

def sum_expenses():
    if expenses_log:
        total_sum = sum([item["price"] for item in expenses_log.values()])

        print("\n------- Expenses -------\n")
        for i, item in enumerate(expenses_log, 1):
            price = expenses_log[item]["price"]
            print(f"\n{i}: {item} ; {price}")

        print("\n-----------------------------------")
        print(f"Total expenses: ${total_sum:.2f}")

    else:
        print("\nNo expenses found.")

while True:
    try:
        menuopt = int(input("How would you like to manage your expense tracker?\n1."))


    except ValueError:
        print("\nThat is not a proper value.")