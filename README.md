 <div align="center">
   
# Google Dawg
</div>

 <br>

## Requirements
- Python
- [web-agent-master/google-search](https://github.com/web-agent-master/google-search) installed and working. Test it first and make sure it works before continue.

## Usage
1. Go to utiliy/constant folder and change the info as needed
```
site = "example.com"                                         ; Target site
categories = [                                               ; GHDB category 
              "files containing password",
              "error messages",
              "files containing juicy info",
              "files containing username",
              "footholds",
              "network or server vulnerability data",
              "pages containing login portals",
              "sensitive directories",
              "sensitive online shopping info",
              "various online devices",
              "vulnerable files",
              "vulnerable servers",
              "web server detection"
              ]
google_search = r"Path/to/google-search"                       ; web-agent-master/google-search root path
```
2. Run main.py
