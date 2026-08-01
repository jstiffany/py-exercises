print("------------- Expenses Tracker -------------")

expenses_log = {
    "Charger": {"price": 12.00}
}

def add_expenses(expense, price):
    if expense in expenses_log:
        print("Expense already in log!")
        return

    print("\nAdding expense...")

    if price < 0:
        print("Price cannot be lower than 0!")
        return

    expenses_log[expense] = {"price": price}
    print("\nExpense added!")

def remove_expense(expense):
    del_expense = expenses_log.pop(expense, "Item not found!")

    if del_expense == "Item not found!":
        print(f"{expense} was not found. Please try again.")

    else:
        print(f"{expense} was deleted.")

    return

def edit_expense(expense, update_type):
    if not expenses_log:
        print("\nNo expenses found.")
        return

    if expense not in expenses_log:
        print("\nExpense not found.")
        return

    print("\nExpense found!")

    if update_type == 1:
        new_name = input("\nWhat is the new name for this expense? ")
        old_price = expenses_log[expense]["price"]

        del expenses_log[expense]

        expenses_log[new_name] = {"price": old_price}
        print("\nName updated!")

    else:
        if expense in expenses_log:
            print("\nExpense found!")

            new_name = input("\nWhat is the new name for this expense?")

            expenses_log[expense] = new_name
            print("\nName updated!")

        elif type == 2:
            if not expenses_log:
                print("\nNo expenses found.")
                return

        else:
            print("Searching for expense...")

            if expense in expenses_log:
                print("Expense found!")

                new_price = float(input("\nWhat is the new price of this expense? "))

                expenses_log[expense]["price"] = new_price
                print("\nPrice updated!")

            else:
                print("Thats not a value.")
                return

def search_expense(expense):
    if not expenses_log:
        print("\nNo expenses found.")

    else:
        print("\nSearching for expense...")

        if expense in expenses_log:
            print("Expense found!\n")
            print(f"{expense}: ${expenses_log[expense]['price']}")

        else:
            print("\nExpense not found.")

def sum_expenses():
    if expenses_log:
        total_sum = sum(item["price"] for item in expenses_log.values())

        print("\n------- Expenses -------\n")
        for i, item in enumerate(expenses_log, 1):
            price = expenses_log[item]["price"]
            print(f"\n{i}: {item} ; ${price}")

        print("\n-----------------------------------")
        print(f"Total expenses: ${total_sum:.2f}")

    else:
        print("\nNo expenses found.")

while True:
    try:
        menuopt = int(input("\nHow would you like to manage your expense tracker?\n1. Add expense\n2. Update expense\n3. Remove expense\n4. Sum expenses\n5. Search/display expeses\n6. Exit\n"))

        if menuopt == 1:
            add_expense = input("\nWhat is the name of this expense? ")
            expense_price = float(input("What is the price of this expense? "))

            add_expenses(add_expense, expense_price)

        elif menuopt == 2:
            find_expense = input("\nWhat is the name of this expense? ")
            update_type = int(input("\nWould you either like to:\n1. Update name\n2. Update price\n"))

            edit_expense(find_expense, update_type)

        elif menuopt == 3:
            rem_expense = input("\nWhat is the name of this expense? ")

            remove_expense(rem_expense)

        elif menuopt == 4:
            sum_expenses()

        elif menuopt == 5:
            search_type = int(input("\nDo you want to:\n1. Search for an expense\n2. Display all expesnses\n"))

            if search_type == 1:
                expense_search = input("What is the expense you are searching for? ")
                search_expense(expense_search)

            elif search_type == 2:
                sum_expenses()

            else:
                print("Thats not a value.")

        elif menuopt == 6:
            print("\nExiting...")
            break


    except ValueError:
        print("\nThat is not a proper value.")