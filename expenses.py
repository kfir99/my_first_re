from datetime import datetime
import pandas as pd

expenses_dict= {}
expense_count = 0
total_expense = 0

while True:
    try:
        amount = float(input("Expense amount (enter 0 or negative to stop): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if amount <= 0:
        break

    description = input("Expense description: ")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_expense += amount


    expenses_dict[f"Expenses {expense_count+1}"]={
        "description": description,
        "amount": amount,
        "time": time
    }
    expense_count += 1


print("Expenses recorded:")
for key, value in expenses_dict.items():
    print(f"{key}: Description: {value['description']}, Amount: {value['amount']}, Time: {value['time']}")
print(f"Total expenses: {total_expense}")
print(f"Total number of expenses: {expense_count}")

expenses_data = {
    "Description": [v["description"] for v in expenses_dict.values()],
    "Amount": [v["amount"] for v in expenses_dict.values()],
    "Time": [v["time"] for v in expenses_dict.values()]
}
df = pd.DataFrame(expenses_data)

# Add total row
total_row = pd.DataFrame([{
    "Description": "TOTAL",
    "Amount": total_expense,
    "Time": ""
}])
df = pd.concat([df, total_row], ignore_index=True)

# Save to Excel
excel_filename = "expenses.xlsx"
df.to_excel(excel_filename, index=False)

print(f"\nExpenses saved to '{excel_filename}' successfully.")
