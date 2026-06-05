#This is a script that will look up MAC address and match the vendor given they own the first 3 bytes
#I seen a lot of different websites being used while training while having 20+ tabs open and tabs within some of those tabs. So I thought why not consolidate them. What can I say I'm a coder, I like stacks.
#Never really cared for tabs unless I was putting something on them. Did you get it?
#Day 7
#Author: RuckusXL

import os
from colorama import init, Fore, Style

init(autoreset=True)

# This function opens and reads the file line by line
def read_file(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    macbook = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if "(hex)" in line:
                macaddr = line.split("(hex)")
                prefix = macaddr[0].replace("-", "").strip()
                suffix = macaddr[1].strip()
                macbook[prefix] = suffix

    return macbook

#This function matches user input to a value in the MAC Address book
def macaddr_lookup(macbook):
    
    while True:
        dirtymac = input(Fore.CYAN +"\nType or paste MAC address (or 'q' to quit): ").strip()
                          
        if dirtymac.lower() == "q":
            print(Fore.MAGENTA +"\nSad to see you go, you were my favorite.\n")
            break

        cleanmac = dirtymac.upper().replace("-", "").replace(":", "")[:6]

        if len(cleanmac) < 6:
            print(Fore.RED +"\nInput 6 or more hex characters please.")
            continue
        
        if cleanmac in macbook:
            print(Fore.GREEN + f"\nVendor -> {macbook[cleanmac]}")
            continue
        else:
            print(Fore.YELLOW +"\nVendor not found, sorry.")

macbook = read_file("oui.txt")
macaddr_lookup(macbook)