<img src="https://revise7.com/wp-content/uploads/2021/07/Logo2.svg" width="400">

# ViperVenom Spyware Tool for Pentesters

ViperVenom is an open-source cyber offensive tool developed by [Revise7 Security](https://revise7.com)
for pentesters, the tool has the ability to webcam record, screenshot, screenshare and
screen video record in high-quality.
ViperVenom is a great tool when it comes to pentesting assessments, as some sort of a proof
that you broke it to a computer and was able to install ViperVenom to capture the screen

Help us improve the tool by [contacting us](https://revise7.com/contacts/), or by sending an [issue](https://github.com/Revise7/ViperVenom/issues)

For additional information and troubleshooting tips about installing and running a Ghidra release, 
please refer to `docs/InstallationGuide.html` which can be found in your extracted Ghidra release 
directory. 
Keep in mind, the tool is currently in beta, bugs may happen.

## Build

To create the latest tool for your platform from this source repository:

##### Install Python Extensions:
* Socket
* Time
* platform
* os
* threading
* termcolor
* vidstream

##### Download and extract the source:
[Download Directly from GitHub][master]
```
$ unzip vipervenom-master
$ cd vipervenom-master
```
**NOTE:** Instead of downloading the compressed source, you may instead want to clone the GitHub 
repository:
```
https://github.com/Revise7/ViperVenom.git
cd ViperVenom
pip3 install -r requirements.txt
python3 vipervenom.py
```

##### ViperVenom's client.py file: 
```
$ gradle buildGhidra
```
In order to connect computer to the listener(you, most likely)

## Develop

### User Scripts and Extensions
Ghidra installations support users writing custom scripts and extensions via the *GhidraDev* plugin 
for Eclipse.  The plugin and its corresponding instructions can be found within a Ghidra release at
`Extensions/Eclipse/GhidraDev/`.

### Advanced Development
To develop the Ghidra tool itself, it is highly recommended to use Eclipse, which the Ghidra 
development process has been highly customized for.

##### Install build and development tools:
* Follow the above build instructions so the build completes without errors
* Install [Eclipse IDE for Java Developers][eclipse]

##### Prepare the development environment (Linux-only, see **NOTE** for Windows/macOS):
``` 
$ gradle prepdev eclipse buildNatives_linux64
```
**NOTE:** If you are on a Windows or macOS platform, change `buildNatives_linux64` to 
`buildNatives_win64` or `gradle buildNatives_osx64`. 

##### Import Ghidra projects into Eclipse:
* *File* -> *Import...*
* *General* | *Existing Projects into Workspace*
* Select root directory to be your downloaded or cloned ghidra source repository
* Check *Search for nested projects*
* Click *Finish*

When Eclipse finishes building the projects, Ghidra can be launched and debugged with the provided
**Ghidra** Eclipse *run configuration*.

For more detailed information on developing ViperVenom, please contact us at [our website][https://revise7.com/contacts/]. 


[Revise7]: https://revise7.com
[Download file]: https://github.com/Revise7/ViperVenom/archive/refs/heads/main.zip
