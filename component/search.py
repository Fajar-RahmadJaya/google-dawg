import subprocess
import os
import re
import json
import datetime

from utility.constant import (queue_json, google_search, site,
                              result_folder)
from utility.logger import (error_log, info_log)


class Search:
    """def npm_link(self):
        # Run 'npm link'
        subprocess.run(
            'npm link',
            shell=True,
            executable="C:\\WINDOWS\\system32\\cmd.exe",
            check=True,
            stdout=subprocess.DEVNULL,
        )"""

    def run_scrapper(self):
        os.chdir(google_search)
        # Get all dork
        with open(queue_json, "r", encoding="utf-8") as f:
            alldork = json.load(f)

        for category, dorks in alldork.items():
            # Print and log category dork start
            print(f"\nStarting {category}:")
            info_log(f"\nStarting {category}:")

            # Create category file
            category_file = os.path.join(result_folder, f"{category}.txt")

            for dork in dorks:
                # Insert \ before " to make dork as single parameter
                single_param_dork = (dork.replace('"', r'\"')
                                     .replace('|', r'"|"'))

                # Get current time
                cur_time = datetime.datetime.now()
                date = cur_time.strftime("%Y-%m-%d %H:%M")

                print(f"[{date}] {dork}:", end=" ", flush=True)

                command = subprocess.run(
                    f'google-search --limit 10000 "{single_param_dork}"',
                    shell=True,
                    executable="C:\\WINDOWS\\system32\\cmd.exe",
                    capture_output=True,
                    text=True,
                    encoding='utf-8'
                )

                # Find rough result from command output
                rough_result = re.search(r'"results":\s*(\[[\s\S]*)',
                                         command.stdout, re.DOTALL)

                # Print and log
                if rough_result:
                    # Write result and get link count
                    link_count = self.write_result(category_file, rough_result)

                    # Print and log how much link found
                    print(f"{link_count} Found")
                    info_log(f"{dork}: {link_count} Found")

                    # Remove completed dork from queue
                    alldork[category].remove(dork)
                    with open(queue_json, "w", encoding="utf-8") as f:
                        json.dump(alldork, f, ensure_ascii=False, indent=2)
                else:
                    # If there is no result on command output
                    print("Search failed")
                    # Log error
                    error_log(f"{single_param_dork}: {command.stderr}")

    def write_result(self, category_file, rough_result):
        # Clean rough result
        # Split result
        split_result = rough_result.group(1).splitlines()
        # Remove last line until line with }
        while split_result and not split_result[-1].strip().endswith('}'):
            split_result.pop()
        # Remove } at the end of line
        if split_result and split_result[-1].strip().endswith('}'):
            split_result.pop()
        # Make result readable with adding space
        clean_result = json.loads("\n".join(split_result))

        # Count and write link from clean result
        link_count = 0
        with open(category_file, "a", encoding="utf-8") as f:
            for item in clean_result:
                # Only get link with target site on it
                if 'link' in item and site in item['link']:
                    # Write link to output
                    f.write(item['link'] + "\n")
                    link_count += 1

        return link_count
