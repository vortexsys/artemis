#### Imports
import os
import time
import ctypes
import json
import requests
import re

#### From Imports
from datetime import date
from colorama import Fore

#### Startup stuff
ctypes.windll.kernel32.SetConsoleTitleW("Artemis v1 | vortexsys")
today = date.today()

with open('./config.json') as f:
   config = json.load(f)

url = config["discord-webhook"]

### Definitions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def restart():
    os.system("python main.py")

#### Standalone Code
def artemis_help():
    clear()
    print("""
   _____          __                 .__        
  /  _  \________/  |_  ____   _____ |__| ______
 /  /_\  \_  __ \   __\/ __ \ /     \|  |/  ___/
/    |    \  | \/|  | \  ___/|  Y Y  \  |\___ \ 
\____|__  /__|   |__|  \___  >__|_|  /__/____  >
        \/                 \/      \/        \/ """)
    withwhat = input("""With what do you need help?
1. App Issue/Bug
2. How to use
3. Credits
4. Report bug via discord.
5. Go back
[>]""")
    
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
        print("What do you want to report?")
        content = input("[>]")
        spam_pattern = re.compile(r"(viagra|free|money|lottery|call now|fuck|lol|odwjada)", re.IGNORECASE)
        
        if spam_pattern.search(content):
            print("This message appears to be spam. Please use the report function for bug reports only.")
            time.sleep(0.50)
            artemis_help()
        else:
            data = {
                "content": content,
                "username": "Bug Report"}
            url2 = "https://discord.com/api/webhooks/1167414072917106720/dZRhbVLWP8uLJywWafYgZnlYMFqJgip7N4x5z3c3lMIb4epjZZXfoEhqzMrBSwoCIiM9"
            result = requests.post(url2, json=data)
            print("Report sent, thank you! Returning to main menu.")
            time.sleep(0.60)
            clear()
            artemis()

    elif withwhat == "5":
        clear()
        restart()
    else:
        print("Invalid input!")
        artemis_help()


def artemis():
     print(Fore.RED + "Logging in on:",today,", what a beautiful day!")
     whattodo = input("""What do you want to do today with this program?
1. Enter the menu
2. Get help
3. About
4. Exit the program
[>] """)
     
     if whattodo == "1":
         os.system('python ./python/menu.py')
         clear()

     elif whattodo == "2":
         artemis_help()

     elif whattodo == "3":
         input("Soon")

     elif whattodo == "4":
         exit()
artemis()

#### made by github.com/vortexsys :)