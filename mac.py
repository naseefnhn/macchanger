#! /usr/bin/env python3

import subprocess
import re
from optparse import OptionParser

# Function to change the MAC address
def macchange(interface, mac):
    print(f"[+] Changing MAC address of {interface} to {mac}...")
    subprocess.check_call(["ifconfig", interface, "down"])
    subprocess.check_call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.check_call(["ifconfig", interface, "up"])
    print("[+] MAC address changed successfully!")

# Function to get user input from command line
def get_arguments():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Network interface to change MAC address of (e.g., eth0)")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address (e.g., 00:11:22:33:44:55)")

    (options, arguments) = parser.parse_args()
    if not options.interface or not options.mac:
        parser.error("[-] Both interface (-i) and MAC address (-m) are required.")
    return options

# Function to get current MAC address
def get_current_mac(interface):
    try:
        result = subprocess.check_output(f"ifconfig {interface}", shell=True, text=True)
        mac_address = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", result)
        if mac_address:
            return mac_address.group(0)
        else:
            return None
    except subprocess.CalledProcessError:
        print("[-] Could not read MAC address. Check interface name.")
        return None

# Main execution
options = get_arguments()
current_mac = get_current_mac(options.interface)
print(f"[*] Current MAC address of {options.interface} is: {current_mac}")

macchange(options.interface, options.mac)

# Verify change
updated_mac = get_current_mac(options.interface)
if updated_mac == options.mac:
    print(f"[+] MAC address changed successfully to: {updated_mac}")
else:
    print("[-] MAC address did not change.")
