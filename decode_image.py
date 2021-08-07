# Use this small tool when you need to decrypt a base64 image and write it to an image.
import base64
f=open('base64.txt', 'r')
string=f.read()
f.close()
image=base64.b64decode(string)
f=open('screenshot.jpg', 'wb')
f.write(image) # here the magic happens 
f.close()
