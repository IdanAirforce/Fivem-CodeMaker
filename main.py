import os
import time
import colorama
from colorama import Fore

colorama.init(autoreset=True)


def credits():
    print(Fore.LIGHTCYAN_EX + r"""
   ____   __            ___          
  /  _/__/ /__ ____    / _ \___ _  __
 _/ // _  / _ `/ _ \  / // / -_) |/ /
/___/\_,_/\_,_/_//_/ /____/\__/|___/ 

Made by idandev.com - airforce
""")


def menu():
    print(Fore.LIGHTBLUE_EX + "\n[1] - Register Command || [2] - Register Event || [3] Resource Manifest || [0] - Exit")


def clear_screen():
    os.system('cls')
    credits()
    menu()


def register_command():
    clear_screen()
    command_name = input("Enter the command name: ")

    lua_code = f'RegisterCommand("{command_name}", function(source, args, rawCommand)\n\nend, false)\n'

    file_name = input("Enter the file name to save (without extension): ") + ".lua"

    with open(file_name, 'w') as file:
        file.write(lua_code)

    print(f'\nCommand "{command_name}" saved to {file_name}. Returning to main menu...')
    time.sleep(3)

    clear_screen()

def register_event():
    clear_screen()
    event_name = input("Enter the event name: ")

    lua_code = f'RegisterNetEvent("{event_name}")\nAddEventHandler("{event_name}", function()\n\nend)\n'

    file_name = input("Enter the file name to save (without extension): ") + ".lua"

    with open(file_name, 'w') as file:
        file.write(lua_code)

    print(f'\nCommand "{event_name}" saved to {file_name}. Returning to main menu...')
    time.sleep(3)

    clear_screen()

def create_fxmanifest():
    clear_screen()

    author = input("Enter the author's name (e.g., John Doe <email@example.com>): ")
    description = input("Enter the resource description: ")
    version = input("Enter the version (e.g., 1.0.0): ")

    fxmanifest_content = f"""fx_version 'cerulean'
games {{ 'rdr3', 'gta5' }}

author '{author}'
description '{description}'
version '{version}'

-- What to run
client_scripts {{
    -- Add client scripts here
}}
server_script ''
"""

    file_name = "fxmanifest.lua"

    with open(file_name, 'w') as file:
        file.write(fxmanifest_content)

    print(f'\nfxmanifest.lua saved to {file_name}. Returning to main menu...')
    time.sleep(3)

    clear_screen()

credits()
menu()

option = int(input("\n>> "))

while option != 0:
    if option == 1:
        register_command()
    elif option == 2:
        register_event()
    elif option == 3:
        create_fxmanifest()

    option = int(input("\n>> "))

print("Goodbye!")
