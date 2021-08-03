import hashlib as hsh
from PIL import Image
import string
import random as r
from itertools import product
import binascii
from cipher import cipher

#put this all in a function

#message, keyword -> list of (binary, cordinates)
message_text = input("Message:")
keyword_text = input("Keyword:")
original_image = Image.open('Test.png')
image = original_image.copy()
pixels = image.load()
binary_text = bin(int(binascii.hexlify((message_text + "#^").encode('ascii')),16))[2:]
     
coordinate_list = cipher(keyword_text, image)[:len(binary_text)]
sequent_map = list(zip(binary_text,coordinate_list))

for i in sequent_map:
    if i[0] == "1":
        pixels[i[1]] = (255,30,200)

image.show()



        

       

