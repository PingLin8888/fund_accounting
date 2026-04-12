import os
import zipfile
import yaml
from datetime import datetime, timedelta 

# To be continued: add a bat file for non-dev to execute the code 


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


# print("config loaded: ")
# for key, value in config.items():
#     print(key, ":", value)

# Determine year and month
if config.get("year") and config.get("month"):
    year = config["year"]
    month = config["month"]
    # f"..." → evaluates expressions inside {}
    print(f"Using config date: {month}-{year}")
else:
    today = datetime.today()
    first_day_this_month = today.replace(day=1)
    # subtract 1 day from the 1st of this month
    last_month = first_day_this_month - timedelta(days=1)
    year = last_month.year
    # 02d formats an integer ( d ) to a field of minimum width 2 ( 2 ), with zero-padding on the left (leading 0 )
    month = f"{last_month.month:02d}"
    
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
        fund_name = name.split("_")[2]
        bank_reports_funds.append(fund_name)

print("bank_reports_funds:", bank_reports_funds)

# Compare
# Process intersection
# Print warnings



# Build list of fiels to zip for each fund
# [os.path.join(..., f) for f in ...] → list comprehension
# os.path.join(config["investran_reports"], f) → combines folder + filename
# files_to_zip = [os.path.join(config["investran_reports_folder"], f) for f in config["files_from_investran"]]
# files_to_zip.append(os.path.join(config["bank_reports_folder"], config["extra_file"]))

# Output zip
# output_zip = os.path.join(config["output_folder"], config["zip_name"])

# zipfile.ZipFile(output_zip, "w") → open a zip file in write mode
# as zipf → gives you a variable zipf to work with inside the block
# with zipfile.ZipFile(output_zip, "w") as zipf:
#     for f in files_to_zip:
#         # zipf.write(f, os.path.basename(f)) → add file to zip
#         # f → full path to file
#         # os.path.basename(f) → only the file name goes into zip, not the folders
#         zipf.write(f, os.path.basename(f))

# print("zip created: ", output_zip)