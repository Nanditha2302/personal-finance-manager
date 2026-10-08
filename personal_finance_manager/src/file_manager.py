import csv
import shutil
from pathlib import Path
from src.expense import Expense

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
BACKUP_DIR = BASE_DIR / "backups"
DATA_FILE = DATA_DIR / "expenses.csv"
BACKUP_FILE = BACKUP_DIR / "expenses_backup.csv"

HEADERS = ["Date", "Category", "Amount", "Description"]


def ensure_directories():
    DATA_DIR.mkdir(exist_ok=True)
    BACKUP_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(HEADERS)


def save_expenses(expenses):
    """Save all expenses to CSV."""
    ensure_directories()
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)
        for expense in expenses:
            writer.writerow(expense.to_list())


def load_expenses():
    """Load expenses from CSV and return Expense objects."""
    ensure_directories()
    expenses = []

    try:
        with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    expenses.append(
                        Expense(
                            row["Amount"],
                            row["Category"],
                            row["Date"],
                            row["Description"],
                        )
                    )
                except (ValueError, KeyError):
                    # Skip invalid records rather than crashing the application.
                    continue
    except OSError as error:
        print(f"Error reading data file: {error}")

    return expenses


def backup_data():
    """Create a backup copy of the expense CSV file."""
    ensure_directories()
    shutil.copy2(DATA_FILE, BACKUP_FILE)


def restore_data():
    """Restore the CSV file from the backup."""
    ensure_directories()

    if not BACKUP_FILE.exists():
        return False

    shutil.copy2(BACKUP_FILE, DATA_FILE)
    return True
