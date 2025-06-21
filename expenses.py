amount_list = []
description_list = []
expenses = 0
while True:
    try:
        amount = float(input("Expense amount"))
    except ValueError:
        print("please enter a valid number")
        continue

    if amount<=0:
        break
    
    amount_list.append(amount)
    
    description = input ("Expense description")
    description_list.append(description)
    
    expenses = expenses + 1


print("Amounts:", amount_list)
print("Descriptions:", description_list)
print("Expenses:", expenses)

