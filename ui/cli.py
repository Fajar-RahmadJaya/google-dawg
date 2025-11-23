from component.search import Search
from component.queue import Queue
from component.cli_component import CLIComponent
from utility.utils import (google_search, site_list)
from utility.constant import (output_folder)

import os


class CLI(Search, Queue, CLIComponent):
    def cli(self):
        print("---------- Google Dawg ----------")
        self.gs_path()

        # Check whether output folder is empty or not
        if not os.listdir(output_folder):
            site = self.new_site()
        else:
            site = self.next_action()

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

    def next_action(self):
        site = input("Target site: ")

        # Site folder
        site_folder = os.path.join(output_folder, site)
        os.makedirs(site_folder, exist_ok=True)

        # get queue
        self.get_queue(site)

        return site

    def resume(self):
        print("Choose next action:")

        # Ask which one need to resume
        for idx, site in enumerate(site_list, 1):
            print(f"{idx}. Resume {site}")
        print("0. Select new site")
        resume_input = input("Input: ")

        # Handle input
        if resume_input.lower() == "0":
            site = self.new_site()
        else:
            try:
                # Substract by one to start from 0
                site = site_list[int(resume_input) - 1]
            except (ValueError, IndexError):
                print("Invalid selection., please choose the number on the site list") # noqa
                return

        return site
