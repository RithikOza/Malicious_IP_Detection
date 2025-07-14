import requests
import json

THREAT_FEED_URL = "https://otx.alienvault.com/api/v1/indicators/export?type=IPv4&api_key=YOUR_API_KEY"

def fetch_malicious_ips():
    response = requests.get(THREAT_FEED_URL)
    if response.status_code == 200:
        ips = [line.strip() for line in response.text.split('\n') if line.strip() and not line.startswith('#')]
        with open('malicious_ips.txt', 'w') as f:
            for ip in ips:
                f.write(ip + '\n')
        print(f"[+] Fetched {len(ips)} malicious IPs.")
    else:
        print("[-] Failed to fetch IPs")

if __name__ == "__main__":
    fetch_malicious_ips()
