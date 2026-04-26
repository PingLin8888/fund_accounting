import pandas as pd
from pathlib import Path

# Load excel file
project_root = Path(__file__).parent.parent
bookings = pd.read_excel(project_root / "data/gl_posting.xlsx")

# Define rules
currency_rules = {
    "USD": ".01",
    "EUR": ".02",
    "CHF": ".13"
}

# Function to check each row
def check_currency_account(row):
    currency = row["Currency"]
    account = str(row["Account"])

    expected_suffix = currency_rules.get(currency)

    if expected_suffix:
        if not account.endswith(expected_suffix):
            return f"Mismatch: {currency} should end with {expected_suffix}"
    return "OK"

# Apply check(axis=1: Apply function row by row)
bookings["check_results"] = bookings.apply(check_currency_account, axis=1)

# Filter issues rows only
# bookings["check_results"] != "OK" → creates a True/False mask(mask: a list of True / False values used to filter data)
# bookings[...] → keeps only rows where condition is True
issues = bookings[bookings["check_results"] != "OK"]

# Save results
# index=False: Don’t write the row index into the Excel file
bookings.to_excel("./output/checked_output.xlsx",index=False)
issues.to_excel("./output/issues_bookings.xlsx", index=False)

print("Check completed!")