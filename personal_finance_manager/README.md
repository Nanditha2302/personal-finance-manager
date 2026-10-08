# Personal Finance Manager

A beginner-friendly Python command-line application for recording, storing and analysing personal expenses.

## Features

- Object-oriented Expense class
- CSV data persistence
- Input validation
- Add and view expenses
- Category-wise analysis
- Monthly reports
- Search functionality
- Backup and restore
- Unit tests
- Modular project structure

## Requirements

- Python 3.9 or later
- No external Python packages are required.

## Installation

1. Install Python.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run:

```bash
python main.py
```

## Testing

Run:

```bash
python -m unittest discover -s tests
```

## Project Structure

```text
personal_finance_manager/
├── main.py
├── requirements.txt
├── README.md
├── src/
├── data/
├── reports/
├── backups/
├── docs/
├── tests/
└── screenshots/
```

## Sample Usage

Add an expense:

- Amount: 1500
- Category: Food
- Date: 2026-10-08
- Description: Grocery shopping

The expense is saved automatically to `data/expenses.csv`.

## Troubleshooting

### Python is not recognized
Install Python and enable "Add Python to PATH" during installation.

### main.py cannot be found
Open the terminal inside the `personal_finance_manager` folder before running:

```bash
python main.py
```

### Invalid input
Read the validation message and enter the requested format again.

## License

This project is intended for educational use.
