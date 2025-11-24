import os

# Info (Change as needed)
category_list = [
              "files containing password",
              "error messages",
              "files containing juicy info",
              "files containing username",
              "footholds",
              "network or server vulnerability data",
              "pages containing login portals",
              "sensitive directories",
              "sensitive online shopping info",
              "various online devices",
              "vulnerable files",
              "vulnerable servers",
              "web server detection"
              ]


# Path
root = os.getcwd()
data_folder = os.path.join(root, "data")

# Dork data
dork_folder = os.path.join(data_folder, "dork")

# Config
config = os.path.join(data_folder, "config.json")

# Folder
output_folder = os.path.join(root, "output")
os.makedirs(output_folder, exist_ok=True)
