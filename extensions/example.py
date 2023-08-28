import os

def example():
    input("This is an example file, press anything to go back.")
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('python menu.py')
example()