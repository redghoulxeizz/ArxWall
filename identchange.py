import os
import time
from colorama import Fore

try:
    
    secs = int(input("Change Identity X Seconds: "))
    while(True):
        os.system('sudo anonsurf change')
        os.system('date')
        time.sleep(secs)
except KeyboardInterrupt:
    print("\n")
    print(Fore.RED + "\nexiting the program")