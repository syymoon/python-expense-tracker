"""Simple text menu for the Expense Tracker."""

from datetime import date
from decimal import Decimal
from pathlib import Path

from expense_tracker import add_expense, parse_amount, read_expenses, totals_by_category

DATA_FILE = Path("data/expenses.csv")


def prompt_date() -> date:
    entered = input("Date (YYYY-MM-DD, Enter for today): ").strip()
    if not entered:
        return date.today()

    try:
        return date.fromisoformat(entered)
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")


def show_expenses(expenses: list[dict[str, str]]) -> None:
    if not expenses:
        print("No expenses recorded yet.")
        return

    for expense in expenses:
        amount = Decimal(expense["amount"])
        print(f"{expense['date']} | {expense['category']} | "
              f"{amount:.2f} EUR | {expense['description']}")


def show_summary(expenses: list[dict[str, str]]) -> None:
    if not expenses:
        print("No expenses to summarize.")
        return

    totals = totals_by_category(expenses)
    grand_total = Decimal("0")

    for category, amount in totals.items():
        print(f"{category}: {amount:.2f} EUR")
        grand_total += amount

    print(f"TOTAL: {grand_total:.2f} EUR")


def main() -> None:
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Show totals by category")
        print("4. Exit")
        try:
            choice = input("Choose an option: ").strip()
            if choice == "1":
                category = input("Category: ").strip()
                if not category:
                    print("Category cannot be empty.")
                    continue

                amount = parse_amount(input("Amount (EUR): "))
                description = input("Description (optional): ").strip()
                spent_on = prompt_date()
                add_expense(DATA_FILE, category, amount, description, spent_on)
                print("Expense saved.")
            elif choice == "2":
                show_expenses(read_expenses(DATA_FILE))
            elif choice == "3":
                show_summary(read_expenses(DATA_FILE))
            elif choice == "4":
                print("Goodbye!")
                return
            else:
                print("Please select 1 to 4.")
        except (ValueError, OSError) as error:
            print(f"Error: {error}")
        except EOFError:
            print("\nGoodbye!")
            return


if __name__ == "__main__":
    main()
