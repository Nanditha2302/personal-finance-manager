import unittest
from src.expense import Expense
from src.reports import total_expenses, average_expense, category_summary


class TestExpense(unittest.TestCase):

    def test_expense_creation(self):
        expense = Expense(1500, "Food", "2026-10-08", "Groceries")
        self.assertEqual(expense.amount, 1500.0)
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.date, "2026-10-08")

    def test_total(self):
        expenses = [
            Expense(100, "Food", "2026-10-01", "Breakfast"),
            Expense(200, "Transport", "2026-10-02", "Bus"),
        ]
        self.assertEqual(total_expenses(expenses), 300)

    def test_average(self):
        expenses = [
            Expense(100, "Food", "2026-10-01", "Breakfast"),
            Expense(300, "Food", "2026-10-02", "Lunch"),
        ]
        self.assertEqual(average_expense(expenses), 200)

    def test_category_summary(self):
        expenses = [
            Expense(100, "Food", "2026-10-01", "Breakfast"),
            Expense(200, "Food", "2026-10-02", "Lunch"),
            Expense(300, "Transport", "2026-10-03", "Bus"),
        ]
        result = category_summary(expenses)
        self.assertEqual(result["Food"], 300)
        self.assertEqual(result["Transport"], 300)


if __name__ == "__main__":
    unittest.main()
