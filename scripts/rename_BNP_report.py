import pandas as pd
import os
from pathlib import Path

# Read mapping file
mapping = pd.read_excel("../data/legal_entity_mapping.xlsx")


def rename_file(file):
    try:
            
        #  Read downloaded file
        df = pd.read_excel(file)

        # Get legal entity
        legal_entity = df["Legal Entity"].iloc[0]

        # Match long name to short name
        short_name = mapping.loc[mapping["Legal Entity(long name)"] == legal_entity,
                                "Legal Entity(short name)"].iloc[0]

        # Rename file
        new_name = f"{short_name} BNP report.xlsx"
        new_path = file.parent / new_name
        file.rename(new_path)
        print(f"Renamed: {file.name} -> {new_name}" )
    
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Folder containing downloaded files
folder = Path("../reports/bank_reports")

# Loop through all excel files
for file in folder.glob("*.xlsx"):
    rename_file(file)