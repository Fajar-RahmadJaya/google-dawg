from utility.constant import (dork_folder)
from utility.utils import (queue_path)

import json
import os


class Queue:
    def get_queue(self, site, categories):
        # Dictionary to store dork list
        dorks_dict = {}

        # Get dork on each category
        for category in categories:
            category_file = os.path.join(dork_folder, f"{category}.txt")
            if os.path.exists(category_file):
                with open(category_file, 'r', encoding='utf-8') as dorks:
                    dork_list = self.format_dork(dorks, site)
                    dorks_dict[category] = dork_list
            else:
                print("Dork data not found")

        # Define queue json
        queue_json = queue_path(site)

        # Write to dictionary to queue_json
        with open(queue_json, 'w', encoding='utf-8') as f:
            json.dump(dorks_dict, f, indent=4, ensure_ascii=False)

    def format_dork(self, dorks, site):
        # List to store formatted dork
        dork_list = []
        for dork in dorks:
            # Split dork
            split_dork = dork.strip()
            # Exclude empty dork
            if not split_dork:
                continue
            # Insert | (OR operator) if there is 'site:' on dork
            if "site:" in split_dork:
                formatted_dork = f"{split_dork} | site:{site}"
            # Insert site on dork
            else:
                formatted_dork = f"{split_dork} site:{site}"
            dork_list.append(formatted_dork)

        return dork_list
