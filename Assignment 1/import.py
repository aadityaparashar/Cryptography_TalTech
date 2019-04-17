import binascii
import os

filename = 'image.png'

with open(filename, 'rb') as f:
    content = f.read()

#print(binascii.hexlify(content))
image_hex = binascii.hexlify(content)

file = open("hex_file.txt","w")  
file.write(""+image_hex) 
file.close() 

os.system('python rsa.py')
