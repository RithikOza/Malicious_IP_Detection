import time
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from block_ip import block_ip

LOG_FILE = "/var/log/auth.log"  # For Linux; use 'Security' event log for Windows
WHITELIST = set(open("whitelist.txt").read().split())

def load_malicious_ips():
    return set(open("malicious_ips.txt").read().split())

malicious_ips = load_malicious_ips()

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == LOG_FILE:
            with open(LOG_FILE, 'r') as f:
                lines = f.readlines()[-10:]
                for line in lines:
                    match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
                    if match:
                        ip = match.group(1)
                        if ip in malicious_ips and ip not in WHITELIST:
                            print(f"[!] Malicious IP Detected: {ip}")
                            block_ip(ip)

if __name__ == "__main__":
    event_handler = LogHandler()
    observer = Observer()
    observer.schedule(event_handler, path=LOG_FILE, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
