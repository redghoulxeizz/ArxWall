import subprocess
import os
from colorama import Fore
import time
import sys
subprocess.run('clear')
print("program is best running in root(sudo python3 arxwall.py)")
time.sleep(2)
subprocess.run('clear')


banner = """

                                                                                                                                                            
                                                                                                                                                      
               AAA                                                       WWWWWWWW                           WWWWWWWW                  lllllll lllllll 
              A:::A                                                      W::::::W                           W::::::W                  l:::::l l:::::l 
             A:::::A                                                     W::::::W                           W::::::W                  l:::::l l:::::l 
            A:::::::A                                                    W::::::W                           W::::::W                  l:::::l l:::::l 
           A:::::::::A           rrrrr   rrrrrrrrr   xxxxxxx      xxxxxxx W:::::W           WWWWW           W:::::W   aaaaaaaaaaaaa    l::::l  l::::l 
          A:::::A:::::A          r::::rrr:::::::::r   x:::::x    x:::::x   W:::::W         W:::::W         W:::::W    a::::::::::::a   l::::l  l::::l 
         A:::::A A:::::A         r:::::::::::::::::r   x:::::x  x:::::x     W:::::W       W:::::::W       W:::::W     aaaaaaaaa:::::a  l::::l  l::::l 
        A:::::A   A:::::A        rr::::::rrrrr::::::r   x:::::xx:::::x       W:::::W     W:::::::::W     W:::::W               a::::a  l::::l  l::::l 
       A:::::A     A:::::A        r:::::r     r:::::r    x::::::::::x         W:::::W   W:::::W:::::W   W:::::W         aaaaaaa:::::a  l::::l  l::::l 
      A:::::AAAAAAAAA:::::A       r:::::r     rrrrrrr     x::::::::x           W:::::W W:::::W W:::::W W:::::W        aa::::::::::::a  l::::l  l::::l 
     A:::::::::::::::::::::A      r:::::r                 x::::::::x            W:::::W:::::W   W:::::W:::::W        a::::aaaa::::::a  l::::l  l::::l 
    A:::::AAAAAAAAAAAAA:::::A     r:::::r                x::::::::::x            W:::::::::W     W:::::::::W        a::::a    a:::::a  l::::l  l::::l 
   A:::::A             A:::::A    r:::::r               x:::::xx:::::x            W:::::::W       W:::::::W         a::::a    a:::::a l::::::ll::::::l
  A:::::A               A:::::A   r:::::r              x:::::x  x:::::x            W:::::W         W:::::W          a:::::aaaa::::::a l::::::ll::::::l
 A:::::A                 A:::::A  r:::::r             x:::::x    x:::::x            W:::W           W:::W            a::::::::::aa:::al::::::ll::::::l
AAAAAAA                   AAAAAAA rrrrrrr            xxxxxxx      xxxxxxx            WWW             WWW              aaaaaaaaaa  aaaallllllllllllllll By xeizz
A Firewall behind TOR                                                                                                                                        

"""

time.sleep(0.4)

def menu():
    
    options = ["Configure Linux OS","Tor + Firewall Setup","Check IP","Wallscan","Exit"]
    opts = 1
    print(banner)
    try:
    
        for option in options:
            print(f"[{opts}] {option}")
            opts+=1
        print("\n")
    
        choice = input(Fore.GREEN + "ArxWall ~> ")
        if int(choice) == 1:
            subprocess.run('clear')
            print(banner)
            config()
        if int(choice) == 2:
            fwrules()
        if int(choice) == 3:
            ipcheck()
        if int(choice) == 4:
            wallscan()
        if int(choice) == 5:
            sys.exit()
    
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
    tools = ["AnonSurf","Veracrypt","Tor","Proxychains4","gedit",""]
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
        os.system("sudo apt-get install tor proxychains4 terminator gedit -y")
        print("done..")
        time.sleep(1)
        menu()
    else:
        print(Fore.RED + "Invalid choice so Installing AnonSurf")
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
    extrafwr = input("would you like to setup extra firewall rules for extra security(Y/N)? ")
    if extrafwr == 'Y' or extrafwr == 'y':
        print("adding Rules")
        # adding rules
        os.system("sudo iptables -A INPUT -m state --state INVALID -j DROP")
        os.system("sudo iptables -A OUTPUT -m state --state INVALID -j DROP")
        os.system("sudo iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT")
        os.system("sudo iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT")
        os.system("sudo iptables -A INPUT -i lo -j ACCEPT")
        print("done..")
        print("be sure to run the \"identchange.py\" file to switch identity")
        time.sleep(2.6)
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
    
        
    
    
    
    

print(menu())
