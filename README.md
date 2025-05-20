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
