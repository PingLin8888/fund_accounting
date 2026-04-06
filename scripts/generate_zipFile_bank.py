import os
import zipfile
import yaml

# __file__ the full path of the script that is currently running
# dirname takes a full path and returns the directory part, removing the filename.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # folder where script lives
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

# Build list of fiels to zip
files_to_zip = [os.path.join(config["input_folder_a"], f) for f in config["files_from_investran"]]
files_to_zip.append(os.path.join(config["input_folder_b"], config["extra_file"]))

# Output zip
output_zip = os.path.join(config["output_folder"], config["zip_name"])

with zipfile.ZipFile(output_zip, "w") as zipf:
    for f in files_to_zip:
        zipf.write(f, os.path.basename(f))

print("zip created: ", output_zip)