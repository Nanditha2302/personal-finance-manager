from collections import defaultdict
from datetime import datetime
from pathlib import Path


def total_expenses(expenses):
    return sum(expense.amount for expense in expenses)


def average_expense(expenses):
    if not expenses:
        return 0
    return total_expenses(expenses) / len(expenses)


def category_summary(expenses):
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense.category] += expense.amount
    return dict(sorted(summary.items()))


def monthly_summary(expenses, month):
    """Return expenses for a month in YYYY-MM format."""
    return [e for e in expenses if e.date.startswith(month)]


def generate_monthly_report(expenses, month, output_dir):
    monthly = monthly_summary(expenses, month)
    total = total_expenses(monthly)
    average = average_expense(monthly)
    summary = category_summary(monthly)

    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    report_file = output_dir / f"monthly_report_{month}.txt"

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("PERSONAL FINANCE MANAGER - MONTHLY REPORT\n")
        file.write("=" * 55 + "\n")
        file.write(f"Month: {month}\n")
        file.write(f"Number of expenses: {len(monthly)}\n")
        file.write(f"Total expense: ₹{total:,.2f}\n")
        file.write(f"Average expense: ₹{average:,.2f}\n\n")

        file.write("CATEGORY-WISE EXPENSES\n")
        file.write("-" * 35 + "\n")
        for category, amount in summary.items():
            file.write(f"{category:<20} ₹{amount:,.2f}\n")

        file.write("\nEXPENSE DETAILS\n")
        file.write("-" * 55 + "\n")
        for expense in monthly:
            file.write(str(expense) + "\n")

    return report_file


def print_summary(expenses):
    print("\nREPORT SUMMARY")
    print("=" * 50)
    print(f"Number of expenses : {len(expenses)}")
    print(f"Total expense      : ₹{total_expenses(expenses):,.2f}")
    print(f"Average expense    : ₹{average_expense(expenses):,.2f}")

    print("\nCategory-wise expenses:")
    summary = category_summary(expenses)
    if not summary:
        print("No expenses available.")
    else:
        for category, amount in summary.items():
            print(f"{category:<20} ₹{amount:,.2f}")
