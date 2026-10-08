from pathlib import Path
from src.expense import Expense
from src.file_manager import (
    load_expenses,
    save_expenses,
    backup_data,
    restore_data,
)
from src.reports import (
    print_summary,
    generate_monthly_report,
    monthly_summary,
)
from src.utils import (
    get_positive_amount,
    get_category,
    get_date,
    get_non_empty,
    pause,
)

BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = BASE_DIR / "reports"


def add_expense(expenses):
    print("\nADD NEW EXPENSE")
    print("=" * 40)

    amount = get_positive_amount()
    category = get_category()
    date = get_date()
    description = get_non_empty("Enter description: ")

    expense = Expense(amount, category, date, description)
    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!")
    print(expense)
    pause()


def view_expenses(expenses):
    print("\nALL EXPENSES")
    print("=" * 75)

    if not expenses:
        print("No expenses found.")
        pause()
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"{number:>3}. {expense}")

    print("=" * 75)
    pause()


def search_expenses(expenses):
    print("\nSEARCH EXPENSES")
    print("=" * 40)
    keyword = get_non_empty("Enter search keyword: ").lower()

    results = [
        expense
        for expense in expenses
        if keyword in expense.category.lower()
        or keyword in expense.description.lower()
        or keyword in expense.date.lower()
    ]

    if not results:
        print("No matching expenses found.")
    else:
        print("\nMatching expenses:")
        for expense in results:
            print(expense)

    pause()


def monthly_report(expenses):
    print("\nMONTHLY REPORT")
    print("=" * 40)

    month = get_non_empty("Enter month (YYYY-MM): ")

    # Validate month.
    from datetime import datetime
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month. Use YYYY-MM, for example 2026-10.")
        pause()
        return

    monthly = monthly_summary(expenses, month)
    print(f"\nExpenses for {month}:")
    if not monthly:
        print("No expenses found for this month.")
    else:
        for expense in monthly:
            print(expense)

    report_file = generate_monthly_report(expenses, month, REPORT_DIR)
    print(f"\nReport saved to: {report_file}")
    pause()


def backup():
    try:
        backup_data()
        print("\nBackup created successfully.")
    except OSError as error:
        print(f"Backup failed: {error}")
    pause()


def restore():
    confirmation = input(
        "\nRestore backup? Current data will be replaced. (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("Restore cancelled.")
        pause()
        return

    if restore_data():
        print("Backup restored successfully.")
    else:
        print("No backup file found.")

    pause()


def run_menu():
    expenses = load_expenses()

    while True:
        print("\n" + "=" * 55)
        print("          PERSONAL FINANCE MANAGER")
        print("=" * 55)
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Category-wise Summary")
        print("4. Generate Monthly Report")
        print("5. Search Expenses")
        print("6. Backup Data")
        print("7. Restore Data")
        print("8. Exit")
        print("=" * 55)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print_summary(expenses)
            pause()
        elif choice == "4":
            monthly_report(expenses)
        elif choice == "5":
            search_expenses(expenses)
        elif choice == "6":
            backup()
        elif choice == "7":
            expenses = restore_and_reload()
        elif choice == "8":
            save_expenses(expenses)
            print("\nThank you for using Personal Finance Manager!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


def restore_and_reload():
    restore()
    return load_expenses()
