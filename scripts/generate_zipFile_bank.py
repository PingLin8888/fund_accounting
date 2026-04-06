import os
import zipfile
import yaml

# __file__ the full path of the script that is currently running
# dirname takes a full path and returns the directory part, removing the filename.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # folder where script lives
config_file = os.path.join(PROJECT_ROOT, "config", "config.yaml")

# load file paths
with open (config_file, "r") as f:
    config = yaml.safe_load(f)

print("config loaded: ")
for key, value in config.items():
    print(key, ":", value)