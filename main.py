#### Imports
import os
import json
import time
import ctypes

#### From Imports
from datetime import date

#### Startup stuff
ctypes.windll.kernel32.SetConsoleTitleW("Artemis v1")
today = date.today()


with open('./config.json') as f:
   config = json.load(f)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#### Standalone Code
def restart():
    os.system("python main.py")


def artemis_help():
    print("")
    withwhat = input("""With what do you need help?
1. App Issue/Bug
2. How to use
3. Credits
4. Go back""")
    
    if withwhat == "1":
        print("Please report any bug at https://github.com/vortexsys/artemis/issues")
        input("Press enter to continue")
        clear()
        artemis_help()

    elif withwhat == "2":
        print("")
        print("Soon")
        input("Press enter to continue")
        clear()
        artemis_help()

    elif withwhat == "3":
        print("Made by https://github.com/vortexsys/")
        print("Official Project repository: https://github.com/vortexsys/artemis")
        
    elif withwhat == "4":
        clear()
        restart()


def artemis():
     print("Logging in on:",today,", what a beautiful day!")
     whattodo = input("""What do you want to do today with this program?
1. Enter the menu
2. Get help
3. About
4. Exit the program
[>] """)
     
     if whattodo == "1":
         os.system('python menu.py')
         clear()

     elif whattodo == "2":
         artemis_help()

     elif whattodo == "3":
         input("Soon")

     elif whattodo == "4":
         exit()
artemis()