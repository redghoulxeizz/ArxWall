import subprocess
import os
from colorama import Fore
import time
import sys
import shutil

subprocess.run('clear')
print("RUN IN ROOT!!! (sudo python3 arxwall.py)")
time.sleep(2)
subprocess.run('clear')


banner = """
 ░░░░░  ░░░░░░  ░░   ░░ ░░     ░░  ░░░░░  ░░      ░░      
▒▒   ▒▒ ▒▒   ▒▒  ▒▒ ▒▒  ▒▒     ▒▒ ▒▒   ▒▒ ▒▒      ▒▒      
▒▒▒▒▒▒▒ ▒▒▒▒▒▒    ▒▒▒   ▒▒  ▒  ▒▒ ▒▒▒▒▒▒▒ ▒▒      ▒▒      
▓▓   ▓▓ ▓▓   ▓▓  ▓▓ ▓▓  ▓▓ ▓▓▓ ▓▓ ▓▓   ▓▓ ▓▓      ▓▓      
██   ██ ██   ██ ██   ██  ███ ███  ██   ██ ███████ ███████ 
                                                     By xeizz
A Firewall behind TOR with extra                                                                                                                                       

"""

time.sleep(0.4)

def menu():
    
    options = ["Configure Linux OS","Tor + Firewall Setup","Check IP","Wallscan","Account Harden", 
               "Encryption", "AV/RK Scan", "Reveal Hidden Processes/Ports"]
    opts = 1
    print(banner)
    try:
    
        for option in options:
            print(f"[{opts}] {option}")
            opts+=1
        print("\n")
    
        choice = input(Fore.GREEN + "ArxWall ~> ")
        if int(choice) == 1:
            config()
        if int(choice) == 2:
            fwrules()
        if int(choice) == 3:
            ipcheck()
        if int(choice) == 4:
            wallscan()
        if int(choice) == 5:
            accharden()
        if int(choice) == 6:
            encryption()
        if int(choice) == 7:
            malware()
        if int(choice) == 8:
            unhide()
    
    except KeyboardInterrupt:
        print("\n")
        print(Fore.RED+"Goodbye")
    
def config():
    user = os.getlogin()
    usr = f"/home/{user}"
    os.chdir(usr)
    os.system("clear")
    print(banner)
    print(Fore.RED + "Updating...")
    os.system("sudo apt-get update;sudo apt-get upgrade -y")
    os.system("clear")
    print(banner)
    print(Fore.RED + "Tools to Install:")
    print("\n")
    tools = ["AnonSurf","Veracrypt","Tor","Proxychains4","gedit","ecryptfs-utils",
             "ClamAV","rkhunter","Unhide"]
    for tool in tools:
        print(tool)
    yorn = input("Y(yes)/N(no)? ~> ")
    if yorn == 'Y' or yorn == 'y':
        print(Fore.CYAN + "Installing Tools..\n")
        os.system('mkdir tools')
        os.chdir('tools')
        print(Fore.RED + "AnonSurf..")
        os.system("git clone https://github.com/Und3rf10w/kali-anonsurf")
        os.chdir('kali-anonsurf')
        os.system("sudo ./installer.sh")
        os.chdir(usr)
        os.chdir('tools')
        os.system('mkdir veracrypt')
        os.chdir('veracrypt')
        os.system('wget https://launchpad.net/veracrypt/trunk/1.26.7/+download/veracrypt-1.26.7-Debian-12-amd64.deb')
        os.system('sudo dpkg -i veracrypt-1.26.7-Debian-12-amd64.deb')
        os.system("sudo apt --fix-broken install -y")
        os.chdir(usr)
        print(Fore.RED + "Installing Rest")
        os.system("sudo apt-get install tor proxychains4 gedit rkhunter ecryptfs-utils clamav clamdscan clamav-freshclam  clamav-daemon  unhide python3-pip -y;pip install pyclamd;pip install --upgrade python-iptables")
        print("done..")
        time.sleep(1)
        menu()
    elif yorn == 'N' or yorn == 'n':
        print(Fore.RED + "Installing AnonSurf and Default Tools then.")
        os.system("sudo apt-get install tor proxychains4 gedit rkhunter ecryptfs-utils clamav clamdscan clamav-freshclam  clamav-daemon  unhide python3-pip -y;pip install pyclamd;pip install --upgrade python-iptables")
        os.system('mkdir tools')
        os.chdir('tools')
        print(Fore.RED + "AnonSurf..")
        os.system("git clone https://github.com/Und3rf10w/kali-anonsurf")
        os.chdir('kali-anonsurf')
        os.system("sudo ./installer.sh")
        os.system("clear")
        menu()
        
        

def fwrules():
    print("Setting up Firewall..\n")
    time.sleep(0.6)
    os.system("sudo anonsurf start")
    print("You are now tunnelling through Tor")
    extrafwr = input("would you like to setup extra firewall rules for extra security(y/n)? ")
    if extrafwr == 'y':
        print("adding Rules")
        # adding rules
        os.system("sudo iptables -A INPUT -m state --state INVALID -j DROP")
        os.system("sudo iptables -A OUTPUT -m state --state INVALID -j DROP")
        os.system("sudo iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT")
        os.system("sudo iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT")
        os.system("sudo iptables -A INPUT -i lo -j ACCEPT")
        print("done..")
        print("be sure to run the \"identchange.py\" file to switch identity")
        time.sleep(2.4)
        menu()
    else:
        print("you are Torified")
        print("be sure to run the \"identchange.py\" file to switch identity")
        time.sleep(2.5)
        subprocess.run('clear')
        menu()

def ipcheck():
    subprocess.run(['curl', 'ifconfig.me'])
    menu()
def wallscan():
    os.system("clear")
    os.system("sudo iptables -L")
    menu()

def accharden():
    subprocess.run(['clear'])
    print("Setting up Anti-Bruteforce for Accounts..")
    time.sleep(0.5)
    usr = os.getlogin()

    def candr(src, src2, src3, dest, dest2, dest3):
        if os.path.exists(dest):
            os.remove(dest)
        if os.path.exists(dest2):
            os.remove(dest2)
        if os.path.exists(dest3):
            os.remove(dest3)
        
        
        shutil.copy2(src, dest)
        shutil.copy2(src2, dest2)
        shutil.copy2(src3, dest3)
    srcpath1 = 'hardeningfiles/common-account'
    srcpath2 = 'hardeningfiles/common-auth'
    srcpath3 = 'hardeningfiles/faillock.conf'
    destpath1 = '/etc/pam.d/common-account'
    destpath2 = '/etc/pam.d/common-auth'
    destpath3 = '/etc/security/faillock.conf'
    
    candr(srcpath1, srcpath2, srcpath3, destpath1, destpath2, destpath3)
    menu()


def encryption():
    subprocess.run(["clear"])
    usr = os.getlogin()
    os.chdir(f"/home/{usr}")
    encfolder = input(f"name of desired folder to be encrypted(ex: /home/{usr}): ")
    def encrypted(dest):
        if os.path.exists(encfolder):
            print("Dir exists, configuring..")
            os.system(f"sudo mount -t ecryptfs {encfolder} {encfolder}")
        else:
            print("Dir doesnt exist, creating..")
            subprocess.run(['mkdir',f'{encfolder}'])
            os.system(f"sudo mount -t ecryptfs {encfolder} {encfolder}")
    encrypted(encfolder)
    menu()

def malware():
    username = os.getlogin()
    os.chdir(f"/home/{username}")

    
    subprocess.run(['clear'])
    print("updating Databases..")
    os.system("sudo rkhunter --update")
    os.system("sudo systemctl enable clamav-freshclam")
    os.system("sudo systemctl stop clamav-freshclam")
    os.system("sudo freshclam")
    os.system("sudo systemctl start clamav-freshclam")
    os.system("sudo systemctl start clamav-daemon")
    time.sleep(0.5)
    

    time.sleep(2.5)
    def clamscan():
        rm = input("remove infected files(y/n)? ")
        if rm == 'y':
            entsysscan = input("scan entire system(y/n)? ")
            if entsysscan == 'y':
                print("Scanning entire system and removing infected..")
                os.system("sudo clamscan -i -r --remove /")
            elif entsysscan == 'n':
                scanopt = ["Directory","File"]
                opt = 1
                
                for opts in scanopt:
                    print(f"{opt}. {opts}")
                    opt+=1
                chopt = int(input("choice: "))
                if chopt == 1:
                    dirscan = input("full path to directory to scan(ex: /path/to/dir): ")
                    os.system(f"sudo clamscan --infected --remove --recursive {dirscan}")
                elif chopt == 2:
                    filescan = input("full path to file to scan(ex: /path/to/file.ext): ")
                    os.system(f"sudo clamscan --infected --remove {filescan}")
        elif rm == 'n':
            entsysscan = input("scan entire system(y/n)? ")
            if entsysscan == 'y':
                print("Scanning entire system and removing infected..")
                os.system("sudo clamscan -i -r --remove /")
            elif entsysscan == 'n':
                scanopt = ["Directory","File"]
                opt = 1
                
                for opts in scanopt:
                    print(f"{opt}. {opts}")
                    opt+=1
                chopt = int(input("choice: "))
                if chopt == 1:
                    dirscan = input("full path to directory to scan(ex: /path/to/dir): ")
                    os.system(f"sudo clamscan --infected --recursive {dirscan}")
                elif chopt == 2:
                    filescan = input("full path to file to scan(ex: /path/to/file.ext): ")
                    os.system(f"sudo clamscan --infected {filescan}")
        time.sleep(2.5)
        menu()
    print("\n")        
    malscanopts = ["rkhunter","ClamAV"]
    malopts = 1
    for mal in malscanopts:
        print(f"{malopts}. {mal}")
        malopts+=1
    print("\n")
    scanmal = int(input("Scan Option: "))
    if scanmal == 1:
        print("Scanning System for RootKits..")
        os.system("sudo rkhunter -c")
        time.sleep(1.9)
    elif scanmal == 2:
        clamscan()
        

def unhide():
    subprocess.run(['clear'])
    print('Revealing everything hidden on the system, this will take 5-10 mins..')
    os.system("sudo unhide brute")   
    menu()
        
    
    
    
    

print(menu())
