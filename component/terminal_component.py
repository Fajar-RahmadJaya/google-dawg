from utility.constant import (config)

import json


class TerminalComponent:
    def write_gs_path(self, gs_input):
        try:
            with open(config, 'w', encoding='utf-8') as f:
                json.dump([{"google-search": gs_input}], f, indent=4)
            print("google-search path saved to config. You can change it on google-dawg/data/config.json.") # noqa
        except Exception as e:
            print(f"Failed to write google-search path: {e}")
