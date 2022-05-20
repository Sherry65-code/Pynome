from os import system, name
from time import sleep
print("Welcome to Pynome Setup")

def ins_win():
    print("Installing dependencies for Windows...")
    sleep(1)
    print("Downloading pip dependencies...")
    system("pip install pygame && cls && echo Done && exit")

def ins_lin():
    distro = input("Type ditro name: (d for debain, f for fedora, a for arch):")
    if (distro == "d"):
        system("echo 'Installing...' && sudo apt install python3-tk python3-pip --assume-yes &> /dev/null && sudo pip3 install pygame &> /dev/null && echo 'Installed'")
    elif (distro == "f"):
        print("Install Python3 tkinter and pip and from pip install pygame")
    elif (distro == "a"):
        system("echo 'Installing...'")
        system("sudo pacman -S python-tk python-pip --noconfirm &> /dev/null")
        system("sudo pip3 install pygame &> /dev/null")
        system("echo 'Done'")
    else:
        print("Wrong Prompt")

if (name == "nt"):
    ins_win()
else:
    ins_lin()