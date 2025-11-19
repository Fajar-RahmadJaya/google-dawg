"""Experimental code to get dork queue with removing any 'site:' on dork"""

import json
import os

from utility.constant import (site, queue_json, dork_folder, categories)


class Dork:
    def get_queue(self):
        # Get dork on each category
        unsterilized_dork = {}
        for category in categories:
            category_file = os.path.join(dork_folder, f"{category}.txt")
            if os.path.exists(category_file):
                with open(category_file, 'r', encoding='utf-8') as f:
                    contents = [f"{line.strip()}" for line in f if line.strip()]
                    unsterilized_dork[category] = contents

        self.write_sterilize_queue(unsterilized_dork)

    def write_sterilize_queue(self, unsterilized_dork):
        # Sterilized dork dict
        all_sterilized_dork = {}

        for category, dorks in unsterilized_dork.items():
            # List of steril dork
            sterilized_dork = []
            for dork in dorks:
                steril_dork = self.sterilize_queue(dork)

                # Combine steril dork into list
                if steril_dork:
                    sterilized_dork.append(steril_dork)

            # Add list to dict
            all_sterilized_dork[category] = sterilized_dork

        # Write Sterilized dork dict to queue_json
        with open(queue_json, 'w', encoding='utf-8') as f:
            json.dump(all_sterilized_dork, f, indent=4, ensure_ascii=False)

    def sterilize_queue(self, dork):
        # Split line
        parts = dork.split()
        # Valid part, not contain site other than choosen site:
        valid_part = []
        # Sterilize parts
        for part in parts:
            # Skip unvalid part, contain site other than choosen site
            if (
                part.startswith('site:') or
                part.startswith('-site:') or
                part.startswith('+site:') or
                part.startswith('+-site:')
            ):
                continue
            # Other part (Not contain any site:)
            else:
                valid_part.append(part)

        # Join valid part adn add the site
        steril_dork = f"site:{site} " + ' '.join(valid_part)

        # Skip if dork empty
        if not valid_part:
            return ""
        # Return steril dork
        else:
            return steril_dork
