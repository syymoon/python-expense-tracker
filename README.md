# Expense Tracker (Python)

A beginner-friendly command-line program for recording everyday expenses and reviewing spending by category.

## Features

- Add an expense with a date, category, amount and optional description
- List all recorded expenses
- Calculate totals by category and the overall total
- Save and load expenses automatically using a CSV file
- Check for invalid amounts and dates
- Use `Decimal` to avoid common floating-point rounding problems with money

## Requirements

- Python 3.10 or newer
- No third-party packages

## Run locally

Open a terminal **inside the project folder**:

```bash
python main.py
```

On Windows, `py main.py` also works if the Python Launcher is installed. On some Linux and macOS systems, use `python3 main.py`.

Example:

```text
=== EXPENSE TRACKER ===
1. Add expense
2. List expenses
3. Show totals by category
4. Exit
Choose an option: 1
Category: Food
Amount (EUR): 12,50
Description (optional): Lunch
Date (YYYY-MM-DD, Enter for today):
Expense saved.
```

Amounts must be positive and have at most two digits after the decimal separator (`.` or `,`). Scientific notation such as `1e2` is not accepted.

## Project files

- `main.py` — interactive menu, user input and printed results
- `expense_tracker.py` — input validation, CSV saving/loading and totals
- `tests/test_tracker.py` — automated checks
- `data/expenses.csv` — created automatically after the first saved expense; excluded from Git by `.gitignore`

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Concepts practiced

Functions, loops, `if` / `elif` / `else`, dictionaries, lists, f-strings, CSV files, exceptions, dates and basic automated testing.

## Possible next steps

- Filter expenses by month
- Add a monthly budget
- Show the highest expense

