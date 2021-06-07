from backend.init.config import salt, hf_name, iterations, dksize, hf_name_pepper, iterations_pepper, dksize_pepper, defaultpass
from backports.pbkdf2 import pbkdf2_hmac
import os, binascii


def hashpassword(username = '', password = defaultpass):

    salthex = binascii.unhexlify(salt)
    password = password.encode('utf-8')
    saltpepper = username.encode('utf-8')
    pepper = pbkdf2_hmac(hf_name_pepper, password, saltpepper, iterations_pepper, dksize_pepper)
    key = pbkdf2_hmac(hf_name, pepper, salthex, iterations, dksize)
    password = binascii.hexlify(key)

    return password
