
import hashlib as hsh
from PIL import Image
import string
import random as r
from itertools import product
import binascii
from cipher import cipher

#put this all in a function

#message, keyword -> list of (binary, cordinates)

keyword_text = input("Keyword:")
original_image = Image.open('result.png')
image = (original_image.copy()).convert('RGB')
pixels = image.load()

result = []
for i in cipher(keyword_text,image):
    if image.getpixel(i) == (255,30,200):
        result.append("1")
    else:
        result.append("0")

raw_output =  ''.join([str(elem) for elem in result])
end_binary = raw_output[0:raw_output.find("0010001101011110")]

n = int('0b' + end_binary, 2)
print(binascii.unhexlify('%x' % n))







        

       

