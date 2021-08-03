import hashlib as hsh
from PIL import Image
import string
import random as r
from itertools import product
import binascii

def cipher(keyword,some_image):
    hash = hsh.sha256(str(keyword).encode('utf-8')).hexdigest()
    width, height = some_image.size
    
    coordinates = list(product(range(0,(width -5)), range(0,(height -5))))
    
    def character_number(symbol):
        characters = (list(string.ascii_lowercase) + (list(string.digits))) 
        return characters.index(symbol)

    r.seed(character_number(hash[11]) + character_number(hash[13]) + character_number(hash[17]))
    r.shuffle(coordinates)
    small_cordinates = coordinates[:5000]
    
    for i in list(hash):
        r.seed(character_number(i))
        r.shuffle(small_cordinates)
    
    return small_cordinates