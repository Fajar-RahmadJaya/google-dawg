 <div align="center">
   
# Google Dawg
</div>

 <br>

## Google Dorking
Google dorking is a technique that utilizes advanced search operators, also known as 'dorks,' to find public sensitive files on a website. This file can be an env file, error message containing password, etc., that shouldn't open in the first place. This sensitive file then can be exploited by attacker to hack your site. For example, if you search [filetype:env](https://www.google.com/search?q=filetype%3Aenv) Google will show link of env file. You can see dork database on [Google Hacking Database (GHDB)](https://www.exploit-db.com/google-hacking-database). 

You can scan your site and close open link if you find any. Better safe than sorry.

## Features
| **No** | **Feature**                                         | **Description** |
|--------|-----------------------------------------------------|-----------------|
| 1      | **Big Dork Database from GHDB**                  | Dork taken from Google Hacking Database (GHDB), grouped by category. |
| 2      | **Resume Dork Search**                  | Dork search might take a while, you can stop or resume search anytime. |
| 3      | **Show Dork Result in Treeview**                  | Dork result can be false positive. Show result in Pyside tree widget and double click to open link on browser. |
| 4      | **Human like behaviour**                  | [web-agent-master/google-search](https://github.com/web-agent-master/google-search) simulate  human like search. Do check it out if you are interested. |

## Requirements
- [Python](https://www.python.org/downloads/)
- [web-agent-master/google-search](https://github.com/web-agent-master/google-search) installed and working. Test it first and make sure it works before continue.

## Installation
```bash
# Clone repository
git clone https://github.com/Fajar-RahmadJaya/google-dawg
cd google-dawg

# Install required module
pip install -r requirements.txt
```

## Usage
1. Run `main.py`
2. Fill necessary input
3. Sit back and relax
> [!TIP]
> When searching, google-search might open Chromium when Google ask for captcha. In this case, just solve the captcha and let it be, it will close automatically.

## Output structure
```
└── output
    └── example.com                                  ; Target site
        └── result
            ├── files containing password.txt        ; Choosen category
        ├── error log.txt                            ; Log for error
        ├── log.txt                                  ; Log for success dork
        ├── queue.json                               ; Dork queue
```

## Contribute
Contibution is welcomed.
