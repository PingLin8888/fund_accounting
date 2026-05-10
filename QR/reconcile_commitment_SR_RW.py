
# V1
# ✅ import reports
# ✅ write tabs
# ✅ compare totals
# ✅ generate PASS/MISMATCH
# ✅ list missing investors

# V2 later
# auto-categorize reasons
# color coding
# email summary
# dashboard
# historical logs

from pathlib import Path
import pandas as pd

import pandas as pd

# Read reports
share_register = pd.read_excel("share_register.xlsx")
rw_report = pd.read_excel("rw_report.xlsx")

# Calculate totals
sr_total = share_register["Commitment"].sum()
rw_total = rw_report["Commitment"].sum()

difference = sr_total - rw_total

status = "MATCH" if difference == 0 else "MISMATCH"

# Merge reports to identify missing investors
merged = share_register.merge(
    rw_report,
    on="Investor Name",
    how="left",
    suffixes=("_sr", "_rw"),
    indicator=True
)

# Investors missing from RW
missing = merged[merged["_merge"] == "left_only"].copy()

# Add suggested reason
def classify_reason(commitment):
    if commitment <= 25:
        return "Possible management shareholder"
    else:
        return "Investigate"

missing["Suggested Reason"] = missing["Commitment_sr"].apply(classify_reason)

# Summary sheet
summary = pd.DataFrame({
    "Check": [
        "Share Register Total",
        "RW Total",
        "Difference",
        "Status"
    ],
    "Value": [
        sr_total,
        rw_total,
        difference,
        status
    ]
})

# Write master reconciliation workbook
with pd.ExcelWriter("reconciliation_master.xlsx", engine="openpyxl") as writer:

    summary.to_excel(writer, sheet_name="Summary", index=False)

    share_register.to_excel(
        writer,
        sheet_name="Share Register",
        index=False
    )

    rw_report.to_excel(
        writer,
        sheet_name="RW Report",
        index=False
    )

    missing.to_excel(
        writer,
        sheet_name="Exceptions",
        index=False
    )

print("Reconciliation workbook created.")