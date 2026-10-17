"""Read, save, and summarize expenses in a CSV file."""

import csv
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

FIELDS = ["date", "category", "amount", "description"]


def parse_amount(value: str) -> Decimal:
    """Turn text into a positive money amount with up to 2 decimal places."""
    text = value.strip().replace(",", ".")

    try:
        amount = Decimal(text)
    except InvalidOperation:
        raise ValueError("Please enter a valid amount.")

    if not amount.is_finite() or amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    # Scientific notation (e.g. 1e2) is not needed for everyday expenses.
    if "e" in text.lower():
        raise ValueError("Please enter a normal number, e.g. 12.50.")

    # After the decimal point there may be no more than two digits.
    if "." in text:
        decimal_part = text.split(".")[1]
        if len(decimal_part) > 2:
            raise ValueError("Use at most two decimal places.")

    return amount


def read_expenses(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []

    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != FIELDS:
            raise ValueError("The CSV file does not have the expected columns.")
        return list(reader)


def add_expense(path: Path, category: str, amount: Decimal, description: str,
                spent_on: date) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    needs_header = not path.exists() or path.stat().st_size == 0

    with path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if needs_header:
            writer.writeheader()

        writer.writerow({
            "date": spent_on.isoformat(),
            "category": category,
            "amount": str(amount),
            "description": description,
        })


def totals_by_category(expenses: list[dict[str, str]]) -> dict[str, Decimal]:
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = Decimal(expense["amount"])

        if category not in totals:
            totals[category] = Decimal("0")

        totals[category] += amount

    return totals
