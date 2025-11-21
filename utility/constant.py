import os

# Info (Change as needed)
site = "example.com"
categories = [
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
google_search = r"Path/to/google-search"


# Path
root = os.getcwd()
data_folder = os.path.join(root, "data")
# Folder
# Output folder
output_folder = os.path.join(root, "output")
# Site folder
site_folder = os.path.join(output_folder, site)
os.makedirs(site_folder, exist_ok=True)
# Result folder
result_folder = os.path.join(site_folder, "result")
os.makedirs(result_folder, exist_ok=True)
# Queue
queue_json = os.path.join(site_folder, "queue.json")
# Log
log = os.path.join(site_folder, "log.txt")
with open(log, 'a') as f:
    pass
# Error log
error_log = os.path.join(site_folder, "error log.txt")
with open(error_log, 'a') as f:
    pass
# Dork data
dork_folder = os.path.join(data_folder, "dork")
