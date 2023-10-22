#### Imports
import os
import time

#### Definitions

def list_python_files(directory):
    python_files = [file[:-3] for file in os.listdir(directory) if file.endswith(".py")]
    return python_files

def execute_python_file(filename):
    try:
        with open(filename, "r") as file:
            code = file.read()
            exec(code)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while executing '{filename}': {e}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#### Code

def menu():
    clear()
    print("""
   _____          __                 .__        
  /  _  \________/  |_  ____   _____ |__| ______
 /  /_\  \_  __ \   __\/ __ \ /     \|  |/  ___/
/    |    \  | \/|  | \  ___/|  Y Y  \  |\___ \ 
\____|__  /__|   |__|  \___  >__|_|  /__/____  >
        \/                 \/      \/        \/ """)
    extensions_directory = os.path.abspath("./extensions/")
    python_files = list_python_files(extensions_directory)
    
    print("Enter `info` for file information")
    print("Enter `check` to check for new files")
    print("Available Python files:")
    for index, filename in enumerate(python_files, start=1):
        print(f"{index}. {filename}")

    try:
        user_input = input("Enter the number of the file you want to run, or type 'info' for file information: ")

        if user_input.isdigit():
            choice = int(user_input) - 1
            if 0 <= choice < len(python_files):
                selected_filename = os.path.join(extensions_directory, python_files[choice] + ".py")
                execute_python_file(selected_filename)
            else:
                print("Invalid choice.")

        elif user_input.lower() == "info":
            print("")
            print("The only preset files are example.py and restart.py")
            print("example.py - gives you an example of how the file can look")
            print("restart.py - returns you to main.py, I wanted to make this an external file as an example")
            input("Press enter to continue!")
            clear()
            menu()
        elif user_input.lower() == "check":
            print("Reloading....")
            time.sleep(0.20)
            menu()
        else:
            print("Invalid input.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    menu()

#### made by github.com/vortexsys :)