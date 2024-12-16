import os
from colorama import Fore
import time

def banner():
        os.system('clear')
        print(Fore.BLUE + '''

    :::::::::: ::::::::::: :::::::::  
    :+:            :+:     :+:    :+: 
    +:+            +:+     +:+    +:+ 
    :#::+::#       +#+     +#++:++#+  
    +#+            +#+     +#+        
    #+#            #+#     #+#        
    ###            ###     ###        - CONNECT''')
        print("")
        print("")
        print("")
    
def main():
    while True:
        banner()
        username = input("Enter User: ")
        ip = input("Enter IP: ")

        if username == username and ip == ip:
            os.system(f'ftp {username}@{ip}')
            print("")
            input("[+] Press Enter To Continue...")
        else:
            print(Fore.YELLOW + "[-] NO USERNAME OR IP DETECTED!")
            time.sleep(1)

if __name__ == "__main__":
    main()