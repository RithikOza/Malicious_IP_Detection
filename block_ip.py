import platform
import subprocess

def block_ip(ip):
    os_type = platform.system()
    if os_type == "Linux":
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
    elif os_type == "Windows":
        subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule", f"name=Block {ip}", "dir=in", f"remoteip={ip}", "action=block"])
    else:
        print("Unsupported OS")
