import os
from pathlib import Path

# User home directory 
home = str(Path.home())

# Some vars
ghrepoLocation = os.path.abspath('gh-repos.txt')
toolstxtLocation = os.path.abspath('tools.txt')
piplistLocation = os.path.abspath('pip.list')

# Check if /Tools/ Directory already exists on system
if os.path.isdir(home + '/Tools/'):
    print("\n[+] /Tools/ Directory already exists")
    os.system('cd ' + home + '/Tools/')
else:
    print("\n[+] /Tools/ Directory NOT exists")
    print("[+] creating..")
    os.system('mkdir ' + home + '/Tools/')
    if os.path.isdir(home + '/Tools/'):
        print("[+] Done")
        os.system('cd ' + home + '/Tools/')

# Update OS
os.system('sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y && sudo apt install curl -y')

# Check if tools.list exists
if os.path.isfile('tools.list'):
    print("\n\n[+] tools.list exists")
    print("[+] installing..")
    os.system('sudo apt install $(cat tools.list | tr "\n" " ") -y')
    print("[+] finished installing from tools.list")
else:
    print("ERROR: tools.list not exist")
    # Download tools.list from github repo
    print("[+] Downloading..")
    os.system('curl https://raw.githubusercontent.com/hrmnsio/kapow.py/master/tools.list -o tools.list')
    if os.path.isfile('tools.list'):
        print("[+] installing..")
        os.system('sudo apt install $(cat tools.list | tr "\n" " ") -y')
        print("[+] finished installing from tools.list")

# Check if gh-repos.txt exists
if os.path.isfile('gh-repos.txt'):
    print("\n\n[+] gh-repos.txt exists")
    print("[+] installing..")
    os.system('cd ' + home + '/Tools && pwd && xargs -n1 git clone < ' + ghrepoLocation)
    print("[+] finished downloading from gh-repos.txt")
else:
    print("\n[-] ERROR: gh-repos.txt does not exist")
    # Download gh-repos.txt from github repo
    print("[+] Downloading..")
    os.system('curl https://raw.githubusercontent.com/hrmnsio/kapow.py/master/gh-repos.txt -o gh-repos.txt')
    if os.path.isfile('gh-repos.txt'):
        print("[+] installing..")
        os.system('cd ' + home + '/Tools && pwd && xargs -n1 git clone < ' + ghrepoLocation)
        print("[+] finished downloading from gh-repos.txt")

# Check if tools.txt exists
if os.path.isfile('tools.txt'):
    print("\n\n[+] tools.txt exists")
    print("[+] installing..")
    os.system('cd ' + home + '/Tools && pwd && xargs -n1 wget < ' + toolstxtLocation)
    print("[+] finished downloading from tools.txt")
else:
    print("\n[-] ERROR: tools.txt does not exist")
    # Download tools.txt from github repo
    print("[+] Downloading..")
    os.system('curl https://raw.githubusercontent.com/hrmnsio/kapow.py/master/tools.txt -o tools.txt')
    if os.path.isfile('tools.txt'):
        print("[+] installing..")
        os.system('cd ' + home + '/Tools && pwd && xargs -n1 wget < ' + toolstxtLocation)
        print("[+] finished downloading from tools.txt")

# Check if pip.list exists
if os.path.isfile('pip.list'):
    print("\n\n[+] pip.list exists")
    print("[+] installing..")
    os.system('xargs -n1 pip3 install < ' + piplistLocation)
    print("[+] finished installing from pip.list")
    # Adding pywhat to PATH
    os.system('export PATH=' + home + '/.local/bin:$PATH')
else:
    print("\n[-] ERROR: pip.list does not exist")
    # Download pip.list from github repo
    print("[+] Downloading..")
    os.system('curl https://raw.githubusercontent.com/hrmnsio/kapow.py/master/pip.list -o pip.list')
    if os.path.isfile('pip.list'):
        print("[+] installing..")
        os.system('xargs -n1 pip3 install < ' + piplistLocation)
        print("[+] finished installing from pip.list")

