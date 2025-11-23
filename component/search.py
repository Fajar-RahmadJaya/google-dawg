from utility.constant import (output_folder)
from utility.utils import (google_search, queue_path)
from utility.logger import (error_logger, info_logger)

import subprocess
import os
import re
import json
import datetime
from colorama import init, Fore
init(autoreset=True)


class Search:
    def run_search(self, site):
        # Define logger
        info_log = info_logger(site)
        error_log = error_logger(site)

        # Set CMD current directory
        os.chdir(google_search)

        # Define queue json
        queue_json = queue_path(site)

        # Get all dork
        with open(queue_json, "r", encoding="utf-8") as f:
            alldork = json.load(f)

        for category, dorks in alldork.items():
            # Print and log category dork start
            print(f"\nStarting {category}:")

            # Result folder
            result_folder = os.path.join(output_folder, site, "result")
            os.makedirs(result_folder, exist_ok=True)

            # Create category file
            category_file = os.path.join(result_folder, f"{category}.txt")

            for dork in dorks:
                # Insert \ before " to make dork as single parameter
                single_param_dork = (dork.replace('"', r'\"'))

                # Get current time
                cur_time = datetime.datetime.now()
                date = cur_time.strftime("%Y-%m-%d %H:%M:%S")

                print(f"{Fore.GREEN}[{date}] {Fore.RESET}{dork}:", end=" ", flush=True) # noqa

                command = subprocess.run(
                    f'google-search --limit 10000 "{single_param_dork}"',
                    shell=True,
                    executable="C:\\WINDOWS\\system32\\cmd.exe",
                    capture_output=True,
                    text=True,
                    encoding='utf-8'
                )

                # Timeout if search failed and retry
                if "搜索失败" in command.stdout:
                    #print(Fore.RED + "Captcha or failed search detected. Retrying in 10 minutes") # noqa
                    # time.sleep(600)
                    print(Fore.RED + "Retrying . . .")
                    return

                # Find rough result from command output
                rough_result = re.search(r'"results":\s*(\[[\s\S]*)',
                                         command.stdout, re.DOTALL)

                # Print and log
                if rough_result:
                    # Get clean result
                    clean_result = self.clean_result(rough_result)

                    # Write and get link count
                    link_count = self.write_link(category_file, clean_result,
                                                 dork, site)

                    # Print and log how much link found
                    if link_count == 0:
                        print(f"{Fore.Yellow}{link_count} Found")
                    else:
                        print(f"{Fore.BLUE}{link_count} Found")
                    info_log.info(f"{single_param_dork}: {link_count} Found")

                    # Remove completed dork from queue
                    alldork[category].remove(dork)
                    with open(queue_json, "w", encoding="utf-8") as f:
                        json.dump(alldork, f, ensure_ascii=False, indent=2)
                else:
                    # If there is no result on command output
                    print(f"{Fore.RED}Search Failed\n{command.stderr}")
                    # Log error
                    error_log.error(f"{single_param_dork}:\n{command.stderr}")

    def clean_result(self, rough_result):
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

        return clean_result

    def write_link(self, category_file, clean_result, dork, site):
        # Count link with target site on it
        link_count = 0
        with open(category_file, "a", encoding="utf-8") as f:
            for item in clean_result:
                if 'link' in item and site in item['link']:
                    # Write result to output
                    f.write(f"{dork}: {item['link']}\n")
                    link_count += 1

        return link_count
