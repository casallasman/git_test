CATEGORIES = {
    1: "Housing",
    2: "Transportation",
    3: "Food",
    4: "Utilities",
    5: "Medical & Healthcare",
    6: "Personal",
    7: "Other",
}


def main() -> None:  # prompts the user to choose an option
    print("-----------------------------------------------")
    print("\nWelcome to your Budget Analyzer and Planner! \n")
    expenses = []
    while True:
        print("What do you want to do? \n")
        print("1. Record expense")
        print("2. View expenses")
        print("3. Analyze expense")
        print("4. Exit this program \n")

        choice = int(input())
        if choice == 1:
            expense_recorder(expenses)
        elif choice == 2:
            view_expenses(expenses)
        elif choice == 3:
            analyzer(expenses)
        elif choice == 4:
            print("Exiting the program.")
            print("-----------------------------------------------")
            break
        else:
            print("Invalid choice. Pick a number between 1 and 4")


def expense_recorder(expenses): #first function
    """
    Expenses will be recorded
    Parametres:
    --expenses: list (to store expense transactions)
    """
    amount = float(input("\nAmount: "))
    if amount <= 0:
        raise ValueError("The amount should be a positive number")

    print("\nAvailable categories: \n")
    for code_number, cat in CATEGORIES.items():
        print(f"{code_number}. {cat}")
    category = int(input("\nWhich category? "))
    if category not in CATEGORIES:
        raise ValueError("Choice not valid \n")

    transaction = {"amount": amount, "category": category}
    expenses.append(transaction)

    print("\nExpense recorded. \n")
    return transaction


def view_expenses(expenses): #second f.
    """
    Expenses will be viewed and displayed
    """
    while True:
        print("What expenses would you like to view? \n")
        print(" A. From a specific category")
        print(" B. Total expenses")
        print(" C. Leave \n")

        view_choice = input().upper()

        if view_choice == "A":
            print("\nAvailable categories: \n")
            for code_number, cat in CATEGORIES.items():
                print(f"{code_number}. {cat}")
            category = int(input("\nWhich category would you like to view? "))
            if category not in CATEGORIES:
                raise ValueError("Choice not valid \n")
                continue
            specific_expenses = 0
            for (transaction) in (expenses):  # also: sum(transaction["amount"] for transaction in expenses if transaction["category"] == category)
                if transaction["category"] == category:
                    specific_expenses += transaction["amount"]
            print(f"\n Total expenses for {CATEGORIES[category]}: ${specific_expenses:.2f} \n")

        elif view_choice == "B":
            if not expenses:
                print("\nNo expenses recorded yet. ")
            else:
                total_overall_expenses = 0
                for transaction in expenses:
                    total_overall_expenses += transaction["amount"]
                print(f"\n Total overall expenses: ${total_overall_expenses:.2f} \n")

        elif view_choice == "C":
            break
        else:
            print("Invalid choice. Type a valid letter \n")


def analyzer(expenses): #third f.
    """
    this function will will provide some analysis of the expenses
    """
    if not expenses:
        print("\nNo expenses recorded yet. ")
        return

    while True:
        print("\nWhat expenses would you like to analyze? \n")
        print(" A. From a specific category")
        print(" B. Overall expenses (all categories)")
        print(" C. Leave \n")

        analyze_choice = input().upper()

        total_expenses = sum(transaction["amount"] for transaction in expenses)

        if analyze_choice == "A":
            print("\nAvailable categories: ")
            for code_number, cat in CATEGORIES.items():
                print(f"{code_number}. {cat}")
            category = int(input("\nWhich category would you like to analyze? "))
            if category not in CATEGORIES:
                raise ValueError("Choice not valid \n")
                continue
            else:
                specific_category = sum(
                    transaction["amount"]
                    for transaction in expenses if transaction["category"] == category
                )
                if total_expenses > 0:
                    category_percentage = (specific_category / total_expenses) * 100
                else:
                    category_percentage = 0
                print(f"\n Total expenses for {CATEGORIES[category]}: ${specific_category:.2f} \n")
                print(
                    f" Percentage of total expenses of {CATEGORIES[category]}: {category_percentage:.2f}% \n"
                )

        elif analyze_choice == "B":
            print(f"\nTotal overall expenses: ${total_expenses:.2f}\n")
            print("\n Expenses per category: \n")
            for code_number, cat in CATEGORIES.items():
                category_expenses = sum(
                    transaction["amount"]
                    for transaction in expenses if transaction["category"] == code_number
                )
                if category_expenses > 0:
                    category_percentage = (category_expenses / total_expenses) * 100
                    print(
                        f"{cat}: ${category_expenses:.2f}, {category_percentage:.2f}% of the total expenses \n"
                        )

        elif analyze_choice == "C":
            break

        else:
            print("Invalid choice. Type a valid letter \n")


if __name__ == "__main__":
    main()
#164 lines of code
