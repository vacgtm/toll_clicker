### fully coded by vac ###
## Credits to the creators of the modules below ##


## Modules ##
from pynput.mouse import Controller, Button
import keyboard
import asyncio
from modules.readjson import read_json
from modules.writejson import update_json_value
import random
import os
from colorama import Fore, init
import time



init()

enabled = False 
right_enabled = False 
mouse = Controller() 


### Banner ### 

def toll_banner():
    return """ 
████████╗ ██████╗ ██╗     ██╗     
╚══██╔══╝██╔═══██╗██║     ██║     
██║   ██║   ██║██║     ██║     
██║   ██║   ██║██║     ██║     
██║   ╚██████╔╝███████╗███████╗
╚═╝    ╚═════╝ ╚══════╝╚══════╝
                                 
"""


### Autoclicker Functions ###
async def clicker():
    global enabled
    while enabled:
        if read_json("configuration/config.json", "randomizationLeft") == "n":
            mouse.click(button=Button.left)
            await asyncio.sleep(read_json("configuration/config.json", "delay_left"))
        elif read_json("configuration/config.json", "randomizationLeft") == "y":
            rand_rngstart = read_json("configuration/config.json", "randomizationLeft-starting_range")
            rand_rngend = read_json("configuration/config.json", "randomizationLeft-ending_range")
            rand_val = random.randrange(int(rand_rngstart), int(rand_rngend))
            mouse.click(button=Button.left)
            await asyncio.sleep(rand_val / 100)
            
async def toggle_clicker():
    global enabled
    if enabled:
        enabled = False
        os.system("cls")
        print(Fore.GREEN + toll_banner())
        print("stopping | left")
    else:
        enabled = True
        os.system("cls")
        print(Fore.GREEN + toll_banner())
        print("starting | left")
        asyncio.create_task(clicker())

async def right_clicker():
    global right_enabled
    while right_enabled:
        if read_json("configuration/config.json", "randomizationRight") == "n":
            mouse.click(button=Button.right)
            await asyncio.sleep(read_json("configuration/config.json", "delay_right"))
        elif read_json("configuration/config.json", "randomizationRight") == "y":
            rand_rngstart = read_json("configuration/config.json", "randomizationRight-starting_range")
            rand_rngend = read_json("configuration/config.json", "randomizationRight-ending_range")
            rand_val = random.randrange(int(rand_rngstart), int(rand_rngend))
            mouse.click(button=Button.right)
            await asyncio.sleep(rand_val / 100)


async def toggle_right_clicker():
    global right_enabled
    if right_enabled:
        right_enabled = False
        os.system("cls")
        print(Fore.GREEN + toll_banner())
        print("stopping | right")
    else:
        right_enabled = True
        os.system("cls")
        print(Fore.GREEN + toll_banner())
        print("starting | right")
        
        asyncio.create_task(right_clicker())


### Key Detection ###


def on_key_event(e):
    if e.name == read_json("configuration/config.json", "left_key") and e.event_type == keyboard.KEY_DOWN:
        asyncio.run_coroutine_threadsafe(toggle_clicker(), loop)

def on_key_event_r(e):
    if e.name == read_json("configuration/config.json", "right_key") and e.event_type == keyboard.KEY_DOWN:
        asyncio.run_coroutine_threadsafe(toggle_right_clicker(), loop)


async def main():
    
    keyboard.hook(on_key_event)
    keyboard.hook(on_key_event_r)
    await asyncio.Event().wait()


### Run Asyncio Loops/Threads ###

if __name__ == "__main__":
    os.system('cls')
    print(Fore.GREEN + toll_banner())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
