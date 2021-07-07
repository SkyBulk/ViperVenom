import base64


f=open('base64.txt', 'r')
string=f.read()
f.close()
image=base64.b64decode(string)
f=open('screenshot.png', 'wb')
f.write(image)
f.close()