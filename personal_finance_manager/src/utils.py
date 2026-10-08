from datetime import datetime

CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Other"]


def get_positive_amount():
    """Read and validate a positive amount."""
    while True:
        value = input("Enter amount (₹): ").strip()
        try:
            amount = float(value)
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return round(amount, 2)
        except ValueError:
            print("Invalid amount. Please enter a number such as 1500 or 1500.50.")


def get_category():
    """Read and validate expense category."""
    print("Categories:", ", ".join(CATEGORIES))
    while True:
        value = input("Enter category: ").strip().title()
        if value in CATEGORIES:
            return value
        print("Invalid category. Choose one from the displayed list.")


def get_date():
    """Read and validate a date in YYYY-MM-DD format."""
    while True:
        value = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")


def get_non_empty(prompt):
    """Read a non-empty text value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def pause():
    input("\nPress Enter to continue...")


def format_currency(amount):
    return f"₹{amount:,.2f}"
