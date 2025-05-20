# 🔍 DomHunt

**DomHunt** is an advanced subdomain enumeration and subdomain takeover detection tool.  
It combines powerful open-source tools and online services to provide deep visibility into a target's subdomains and identify takeover vulnerabilities.

---

## 🚀 Features

- Subdomain enumeration using:
  - [`subfinder`](https://github.com/projectdiscovery/subfinder)
  - [`assetfinder`](https://github.com/tomnomnom/assetfinder)
  - [`knockpy`](https://github.com/guelfoweb/knock)
  - Online services: `crt.sh`, `DNSDumpster`, `HackerTarget`
- Deduplication and filtering of results
- Alive subdomain check using [`dnsx`](https://github.com/projectdiscovery/dnsx)
- Subdomain takeover detection using [`subzy`](https://github.com/LukaSikic/subzy)
- Clean output in organized folders

---

## 📦 Installation

### 🐍 Python dependencies

Install required Python libraries:

```bash
pip install -r requirements.txt







### 🧪 Example Workflow
bash
Copy code
$ python3 domhunt.py

     ____                        _   _             
    |  _ \  ___  _ __ ___   ___ | |_| |_ ___  _ __ 
    | | | |/ _ \| '_ ` _ \ / _ \| __| __/ _ \| '__|
    | |_| | (_) | | | | | | (_) | |_| || (_) | |   
    |____/ \___/|_| |_| |_|\___/ \__|\__\___/|_|   
      🔍 Subdomain Finder + Takeover Checker
               by Vishal | DomHunt

[+] Enter target domain: example.com

[*] Running Subfinder...
[*] Running Assetfinder...
[*] Running Knockpy...
[*] Fetching from crt.sh...
[*] Fetching from DNSDumpster...
[*] Fetching from HackerTarget...

[+] Total collected: 134 subdomains (before deduplication)
[+] Unique subdomains saved to: output/all_subdomains.txt
[*] Filtering alive subdomains using dnsx...
[+] Alive subdomains saved to: output/live_subdomains.txt
[*] Running Subzy for takeover check...
[+] Vulnerable subdomains saved to: output/vulnerable_subdomains.txt

[✔] DomHunt completed.
