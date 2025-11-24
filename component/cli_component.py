from utility.constant import (config)
from ui.tree import Tree

import json
from PySide6.QtWidgets import QApplication


class CLIComponent:
    def write_gs_path(self, gs_input):
        try:
            with open(config, 'w', encoding='utf-8') as f:
                json.dump([{"google-search": gs_input}], f, indent=4)
            print("google-search path saved to config. You can change it on google-dawg/data/config.json.") # noqa
        except Exception as e:
            print(f"Failed to write google-search path: {e}")

    def open_tree(self, site):
        tree = QApplication.instance()
        if not tree:
            tree = QApplication([])
        window = Tree(site)
        window.show()
        tree.exec()
