import pandas as pd

# Share Register Report
share_register = pd.DataFrame({
    "Investor Name": [
        "ABC Capital",
        "XYZ Management",
        "Global Fund",
        "Blocked Investor"
    ],
    "Commitment": [
        500000,
        25,
        300000,
        1000
    ]
})

# RW Report
rw_report = pd.DataFrame({
    "Investor Name": [
        "ABC Capital",
        "Global Fund"
    ],
    "Commitment": [
        500000,
        300000
    ],
    "Email": [
        "abc@test.com",
        "global@test.com"
    ]
})

# Save reports
share_register.to_excel("share_register.xlsx", index=False)
rw_report.to_excel("rw_report.xlsx", index=False)

print("Test reports created.")