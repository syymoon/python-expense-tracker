import tempfile
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

from expense_tracker import add_expense, parse_amount, read_expenses, totals_by_category


class ExpenseTrackerTests(unittest.TestCase):
    def test_amount_validation(self):
        self.assertEqual(parse_amount("12,50"), Decimal("12.50"))
        self.assertEqual(parse_amount("4.2"), Decimal("4.2"))
        for value in ("0", "-2", "abc", "12.345", "NaN", "Infinity", "1e2"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_amount(value)

    def test_save_load_and_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "expenses.csv"
            add_expense(path, "Food", Decimal("12.50"), "Lunch", date(2026, 10, 16))
            add_expense(path, "Food", Decimal("3.20"), "Coffee", date(2026, 10, 16))
            add_expense(path, "Transport", Decimal("10.00"), "Bus", date(2026, 10, 16))
            expenses = read_expenses(path)
            self.assertEqual(len(expenses), 3)
            self.assertEqual(totals_by_category(expenses), {
                "Food": Decimal("15.70"),
                "Transport": Decimal("10.00"),
            })


if __name__ == "__main__":
    unittest.main()
