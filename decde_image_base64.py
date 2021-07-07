# This is probably the easiest Python script I've ever made, really, all it does is to decrypt your base64 string on base64.txt and write the decrypted string to a photo, magic!

import base64
f=open('base64.txt', 'r')
string=f.read()
f.close()
image=base64.b64decode(string)
f=open('screenshot.png', 'wb')
f.write(image) # here the magic happens 
f.close()
