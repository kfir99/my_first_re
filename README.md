Sure! Here's a simple and clear README file for your expense tracker script:

---

# Expense Tracker

This Python script allows you to record your daily expenses interactively, store them in memory, display a summary, and save the data to an Excel file.

## Features

* Input multiple expenses with amount and description.
* Automatically records the date and time of each expense.
* Stops input when a zero or negative amount is entered.
* Calculates total expenses and number of entries.
* Saves all expenses to an Excel file (`expenses.xlsx`) with a total row at the end.

## Requirements

* Python 3.x
* `pandas` library

You can install `pandas` using pip if you don't have it already:

```bash
pip install pandas
```

## Usage

1. Run the script:

```bash
python expense_tracker.py
```

2. Enter your expense amounts and descriptions when prompted.
3. To stop adding expenses, enter `0` or a negative number as the amount.
4. After finishing input, the script will display a summary and save the data to `expenses.xlsx`.

## Output

* The console will show a list of all expenses with descriptions, amounts, and timestamps.
* Total expense amount and total number of expenses will be displayed.
* An Excel file named `expenses.xlsx` will be created in the same directory with all the recorded expenses plus a total row.

## Example

```
Expense amount (enter 0 or negative to stop): 15.50
Expense description: Lunch
Expense amount (enter 0 or negative to stop): 45.00
Expense description: Groceries
Expense amount (enter 0 or negative to stop): 0

Expenses recorded:
Expenses 1: Description: Lunch, Amount: 15.5, Time: 2025-06-24 14:32:10
Expenses 2: Description: Groceries, Amount: 45.0, Time: 2025-06-24 14:33:02
Total expenses: 60.5
Total number of expenses: 2

Expenses saved to 'expenses.xlsx' successfully.
```

---
