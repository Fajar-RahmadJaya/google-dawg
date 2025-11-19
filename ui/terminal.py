import os

from component.search import Search
from component.dork import Dork
from utility.constant import queue_json


class Terminal(Search, Dork):
    def run(self):
        # self.npm_link()
        if not os.path.exists(queue_json):
            self.get_queue()
        else:
            print("Resuming dork")
        self.run_scrapper()
