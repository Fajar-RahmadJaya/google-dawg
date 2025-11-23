from utility.constant import (config, output_folder)

import json
import os


def gs_path():
    try:
        with open(config, 'r', encoding='utf-8') as f:
            configs = json.load(f)
            if configs and isinstance(configs, list):
                google_search = configs[0].get("google-search", "")
                return google_search if google_search else ""
    except Exception:
        pass
    return ""


google_search = gs_path()


def get_site():
    # List everything inside otput_folder
    item_list = os.listdir(output_folder)
    site_list = []

    # Loop each item
    for item in item_list:
        site_folder = os.path.join(output_folder, item)
        queue_json = os.path.join(site_folder, "queue.json")

        # Make sure item is folder and there is queue.json on it
        if os.path.isdir(site_folder) and os.path.isfile(queue_json):
            # Inser folder into list
            site_list.append(item)
    return site_list


site_list = get_site()


def queue_path(site):
    return os.path.join(output_folder, site, "queue.json")
