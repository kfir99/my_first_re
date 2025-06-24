amount_list = []
description_list = []
expenses_list = []

while True:
    try:
        amount = float(input("Expense amount (enter 0 or negative to stop): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if amount <= 0:
        break

    amount_list.append(amount)

    description = input("Expense description: ")
    description_list.append(description)

    expenses = input("Amount of expenses: ")
    expenses_list.append(expenses)

print("Amounts:", amount_list)
print("Descriptions:", description_list)
print("Expenses:", expenses_list)
