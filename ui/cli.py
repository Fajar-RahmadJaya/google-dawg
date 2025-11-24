from component.search import Search
from component.queue import Queue
from component.cli_component import CLIComponent
from utility.utils import (google_search, site_list)
from utility.constant import (output_folder, category_list)

import os
import sys


class CLI(Search, Queue, CLIComponent):
    def cli(self):
        print("---------- Google Dawg ----------")
        self.gs_path()

        # Check whether output folder is empty or not
        if not os.listdir(output_folder):
            site = self.new_site()
        else:
            site = self.resume()

        # Run search
        while True:
            self.run_search(site)

    def gs_path(self):
        # Check whether the google-search path is empty or not
        if not os.path.isdir(google_search):
            print("google-search path invalid, please enter correct google-search path.") # noqa
            gs_input = input("Enter google-search path: ")
            # Write input to config
            self.write_gs_path(gs_input)

        # Check whether google-search is filled or not
        if not google_search:
            gs_input = input("Enter google-search path: ")

            # Make sure input is valid
            if not os.path.isdir(gs_input):
                print("google-search path invalid, please enter correct google-search path.") # noqa
                gs_input = input("Enter google-search path: ")

            # Write input to config
            self.write_gs_path(gs_input)
        # To do: option to change path

    def new_site(self):
        # Ask site
        site = input("Target site: ")

        # Ask category
        print("Select dork category:")
        for idx, category in enumerate(category_list, 1):
            print(f"{idx}. {category}")
        category_input = input("Input separated by comma (eg. 1, 2, 3): ")
        categories = self.get_category(category_input)

        # Site folder
        site_folder = os.path.join(output_folder, site)
        os.makedirs(site_folder, exist_ok=True)

        # get queue
        self.get_queue(site, categories)
        return site

    def get_category(self, category_input):
        # Category list
        categories = []
        # Get categories based on input
        for item in category_input.split(","):
            # Remove whitespace
            item = item.strip()
            if item.isdigit():
                idx = int(item)
                # Traverse the category list to get category based on input number # noqa
                if 1 <= idx <= len(category_list):
                    # Insert category to list
                    categories.append(category_list[idx - 1])
        return categories

    def resume(self):
        # If site just 1, ask for resume
        if len(site_list) == 1:
            single_resume = input("Unfinished dork detected! Would you like to resume it? (y/n): ") # noqa
            if single_resume.lower() == "y":
                site = site_list[0]
            else:
                # If n (No) ask what to do next
                print("Choose what to do next:")
                site = self.next_action()
        # If site more than one, ask what to do next
        else:
            site = self.next_action()
        return site

    def next_action(self):
        # Ask what to do
        for idx, site in enumerate(site_list, 1):
            print(f"{idx}. Resume {site}")
        print(f"{len(site_list) + 1}. Show result")
        print("0. Select new site")
        resume_input = input("Input: ")

        # Handle input
        if resume_input.lower() == "0":
            # Make new queue
            site = self.new_site()
        elif resume_input == str(len(site_list) + 1):
            # Show tree view
            self.show_result()
        else:
            try:
                # Substract by one to start from 0
                site = site_list[int(resume_input) - 1]
            except (ValueError, IndexError):
                print("Invalid selection., please choose the number on the site list") # noqa
                return
        return site

    def show_result(self):
        # If site is just 1, directly show result
        if len(site_list) == 1:
            site = site_list[0]
            self.open_tree(site)
            # Exit program
            sys.exit()
        # if site more than one, ask which site to show
        else:
            print("Select which result to show: ")
            for idx, site in enumerate(site_list, 1):
                print(f"{idx}.{site}")
            showres_input = input("Input: ")
            site = site_list[int(showres_input) - 1]
            self.open_tree(site)
            # Exit program
            sys.exit()
