import os, binascii

host = 'host'
user = 'user'
passwd = 'passwd'
db = 'db'
secret_key = 'secret_key'

salt = binascii.unhexlify('salt') #change the salt

hf_name = 'sha512'
iterations = 1 #change the number
dksize = 1 #change the number

hf_name_pepper = 'sha512'
iterations_pepper = 1 #change the number
dksize_pepper = 1 #change the number

defaultpass = 'mdp'