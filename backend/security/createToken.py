from backend.init.config import *
from backports.pbkdf2 import pbkdf2_hmac
import os, binascii
import datetime

def createToken(username =  ''):
    salthex = binascii.unhexlify(salt) 

    tokenpepper = username.encode('utf-8')
    saltpepper =  str(datetime.datetime.now()).encode('utf-8')
    pepper = pbkdf2_hmac(hf_name_pepper, tokenpepper, saltpepper, iterations_pepper, dksize_pepper)

    key = pbkdf2_hmac(hf_name, pepper, salthex, iterations, dksize)
    token = binascii.hexlify(key)

    return token.decode('utf-8')
