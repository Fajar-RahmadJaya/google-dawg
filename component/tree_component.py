from utility.utils import (result_folder_path)

import os
import webbrowser


class TreeComponent:
    def get_data(self, site):
        # Result Folder
        result_folder = result_folder_path(site)

        # Data list
        data = []

        # Get category from files name on result folder
        for categories in os.listdir(result_folder):
            category = (os.path.splitext(categories)[0]
                        .replace("_", " ").title())
            category_file = os.path.join(result_folder, categories)

            # Get link and dork
            link_dork = self.get_link_dork(category_file)

            # Insert category, link, dork on list
            for link, dork in link_dork:
                data.append({
                    "link": link,
                    "dork": dork,
                    "category": category
                })
        return data

    def get_link_dork(self, category_file):
        # Link and dork list
        link_dork = []

        # Get link and dork from the category file
        with open(category_file, "r", encoding="utf-8") as ctg_file:
            for line in ctg_file:
                # Split the line
                split_line = line.strip()
                # Dork and link format {dork}: {link}
                if ": " in split_line:
                    dork, link = line.split(": ", 1)
                    # Remove whitespace
                    dork = dork.strip()
                    link = link.strip()
                    # Append link and dork on list
                    link_dork.append((link, dork))
        return link_dork

    def open_link(self, item):
        # Link position
        link = item.text(1)
        if link:
            webbrowser.open(link)
