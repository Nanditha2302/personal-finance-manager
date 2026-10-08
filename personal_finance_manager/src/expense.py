class Expense:
    """Represents a single personal expense."""

    def __init__(self, amount, category, date, description):
        self.amount = float(amount)
        self.category = category.strip().title()
        self.date = date
        self.description = description.strip()

    def to_list(self):
        """Return expense data as a list for CSV storage."""
        return [self.date, self.category, f"{self.amount:.2f}", self.description]

    def __str__(self):
        return (
            f"{self.date} | {self.category:<15} | "
            f"₹{self.amount:>10.2f} | {self.description}"
        )
