import subprocess
import requests
from bs4 import BeautifulSoup
import os

# ------------------ Banner ------------------
def banner():
    print(r"""
     ____                        _   _             
    |  _ \  ___  _ __ ___   ___ | |_| |_ ___  _ __ 
    | | | |/ _ \| '_ ` _ \ / _ \| __| __/ _ \| '__|
    | |_| | (_) | | | | | | (_) | |_| || (_) | |   
    |____/ \___/|_| |_| |_|\___/ \__|\__\___/|_|   
          🔍 Subdomain Finder + Takeover Checker
                   by Vishal | DomHunt
    """)

# ------------------ Utilities ------------------

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL)
        return output.decode().splitlines()
    except:
        return []

def run_subfinder(domain):
    print("[*] Running Subfinder...")
    return run_command(f"subfinder -d {domain} -silent")

def run_assetfinder(domain):
    print("[*] Running Assetfinder...")
    return run_command(f"assetfinder --subs-only {domain}")

def run_knockpy(domain):
    print("[*] Running Knockpy...")
    knock_path = "tools/knockpy/knockpy.py"
    if not os.path.exists(knock_path):
        print("[!] knockpy not found at tools/knockpy/")
        return []
    return run_command(f"python3 {knock_path} {domain}")

def get_crtsh(domain):
    print("[*] Fetching from crt.sh...")
    try:
        r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json", timeout=10)
        return list({entry["name_value"].strip() for entry in r.json() if domain in entry["name_value"]})
    except:
        return []

def get_dnsdumpster(domain):
    print("[*] Fetching from DNSDumpster...")
    try:
        url = "https://dnsdumpster.com/"
        session = requests.Session()
        headers = {"User-Agent": "Mozilla/5.0"}
        session.get(url, headers=headers)
        r = session.post(url, data={"targetip": domain}, headers=headers)
        return list(set([line.split(">")[1].split("<")[0] for line in r.text.splitlines() if domain in line and "td class" in line]))
    except:
        return []

def get_hackertarget(domain):
    print("[*] Fetching from HackerTarget...")
    try:
        url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
        r = requests.get(url)
        return list({line.split(',')[0] for line in r.text.splitlines() if domain in line})
    except:
        return []

def save_list(filename, data):
    with open(filename, 'w') as f:
        f.write("\n".join(sorted(set(data))))

def run_dnsx(input_file, output_file):
    print("[*] Filtering alive subdomains using dnsx...")
    os.system(f"dnsx -l {input_file} -silent -o {output_file}")

def run_subzy(input_file, output_file):
    print("[*] Running Subzy for takeover check...")
    os.system(f"subzy run --targets {input_file} --vuln > {output_file}")

# ------------------ Main ------------------

def main():
    banner()
    domain = input("\n[+] Enter target domain: ").strip()

    # Output Directory Setup
    os.makedirs("output", exist_ok=True)
    raw_file = "output/all_subdomains.txt"
    alive_file = "output/live_subdomains.txt"
    vuln_file = "output/vulnerable_subdomains.txt"

    print(f"\n[+] Enumerating subdomains for: {domain}\n")
    subdomains = []
    subdomains += run_subfinder(domain)
    subdomains += run_assetfinder(domain)
    subdomains += run_knockpy(domain)
    subdomains += get_crtsh(domain)
    subdomains += get_dnsdumpster(domain)
    subdomains += get_hackertarget(domain)

    print(f"\n[+] Total collected: {len(subdomains)} subdomains (before deduplication)")
    save_list(raw_file, subdomains)
    print(f"[+] Unique subdomains saved to: {raw_file}")

    run_dnsx(raw_file, alive_file)
    print(f"[+] Alive subdomains saved to: {alive_file}")

    run_subzy(alive_file, vuln_file)
    print(f"[+] Vulnerable subdomains saved to: {vuln_file}")

    print("\n[✔] DomHunt completed.")

if __name__ == "__main__":
    main()
