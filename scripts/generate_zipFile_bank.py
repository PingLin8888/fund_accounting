import os
import zipfile
import yaml
from datetime import datetime, timedelta 

# To be continued: add a bat file for non-dev to execute the code 
# lux non_lux. which is lux which is not


# __file__ the full path of the script that is currently running
# dirname takes a full path and returns the directory part, removing the filename.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(PROJECT_ROOT, "config", "config.yaml")

# Load file paths
# "r" → read mode
# with is a context manager: Ensures the file is automatically closed after the block finishes
# f is the file object, like a handle you use to read the file’s contents.
with open (config_file, "r") as f:
    config = yaml.safe_load(f)

allowed_files = config["files_from_investran"]

# print("config loaded: ")
# for key, value in config.items():
#     print(key, ":", value)

# Determine year and month
if config.get("year") and config.get("month"):
    year = config["year"]
    month = config["month"]
    # f"..." → evaluates expressions inside {}
    print()
    print(f"Using config date: {month}-{year}")
else:
    today = datetime.today()
    first_day_this_month = today.replace(day=1)
    # subtract 1 day from the 1st of this month
    last_month = first_day_this_month - timedelta(days=1)
    year = last_month.year
    # 02d formats an integer ( d ) to a field of minimum width 2 ( 2 ), with zero-padding on the left (leading 0 )
    month = f"{last_month.month:02d}"
    
    print()
    print(f"Using previous month automatically: {month}-{year}")


# Get funds from Investran folder
investran_folder = os.path.join(
    config["investran_reports_folder"],
    str(year),
    str(month)
)

# Extract fund name from file name
investran_funds = [
    f for f in os.listdir(investran_folder)
    if os.path.isdir(os.path.join(investran_folder, f))
]

print()
print("investran funds:", investran_funds)


# Get funds from Bank reports folder
bank_reports_folder = os.path.join(
    config["bank_reports_folder"],
    str(year),
    str(month)
)

# Extract fund name from file name
bank_reports_funds = []
for file in os.listdir(bank_reports_folder):
    if file.endswith(".xlsx"):
        file = os.path.basename(file)  # remove path
        name = os.path.splitext(file)[0]  # remove .xlsx
        fund_name = name.split("_")[3]
        bank_reports_funds.append(fund_name)

print()
print("bank_reports_funds:", bank_reports_funds)

# Compare the diff in the 2 lists
investran_set = set(investran_funds)
bank_set = set(bank_reports_funds)

common_funds = investran_set & bank_set
missing_in_investran = bank_set - investran_set
missing_in_bank = investran_set - bank_set

# Print warning 
if missing_in_investran:
    print()
    print("⚠️ Missing in Investran folder:")
    for fund in missing_in_investran:
        print("  ", fund)

if missing_in_bank:
    print()
    print("⚠️ Missing in bank folder:")
    for fund in missing_in_bank:
        print("  ", fund)


# Get files per fund
# [ RESULT  for f in ...  if condition ]
for fund in common_funds:
    print()
    print("Processing fund: " + fund)
    # Get Investran files
    fund_investran_folder = os.path.join(investran_folder, fund)

    allowed_keywords = [
        os.path.splitext(file)[0] # split extension ie xlsx
        for file in config["files_from_investran"]
    ]

    investran_files = [
        os.path.join(fund_investran_folder, f)
        for f in os.listdir(fund_investran_folder)
        if os.path.isfile(os.path.join(fund_investran_folder, f))
        and f.endswith(".xlsx")
        and any(keyword in f for keyword in allowed_keywords)
    ]

    print()
    print("investran_files:",investran_files)

    # Get Bank file
    bank_file = None

    for file in os.listdir(bank_reports_folder):
        if fund in file:
            bank_file = os.path.join(bank_reports_folder, file)
            break

    print()
    print("bank_file:", bank_file)

    # Combine files
    files_to_zip = investran_files.copy()

    if bank_file:
        files_to_zip.append(bank_file)
        print()
        print("files_to_zip: ",files_to_zip)
    else:
        print()
        print(f"⚠️ No bank file found for {fund}")
        continue

    # Build zip name
    zip_name = f"{fund}_{year}_{month}_BNP.zip"

    output_folder = config["output_folder"]
    os.makedirs(output_folder, exist_ok=True)

    output_zip = os.path.join(output_folder,zip_name)
    
    # Create zip
    # zipfile.ZipFile(output_zip, "w") → open a zip file in write mode
    # as zipf → gives you a variable zipf to work with inside the block
    with zipfile.ZipFile(output_zip, "w") as zipf:
        for f in files_to_zip:
            # f → full path to file
            # os.path.basename(f) → only the file name goes into zip, not the folders
            zipf.write(f, os.path.basename(f)) # → add file to zip

    print("zip created: ", output_zip)

# [os.path.join(..., f) for f in ...] → list comprehension
# os.path.join(config["investran_reports"], f) → combines folder + filename
