import os, binascii

host = 'host'
user = 'user'
passwd = 'passwd'
db = 'db'
secret_key = 'secret_key'

salt = binascii.unhexlify('salt') #change the salt

hf_name = 'sha512'
iterations = 1 #change the number (1, 50000)
dksize = 1 #change the number (1, 64)

hf_name_pepper = 'sha512'
iterations_pepper = 1 #change the number (1, 50000)
dksize_pepper = 1 #change the number (1, 64)

defaultpass = 'mdp'

ecoleconf = ['ESILV', 'IIM', 'EMLV', 'Autre']
anneeconf = ['A1', 'A2', 'A3', 'A4', 'A5', 'Autre']
speconf = ['Débat parlementaire', 'Plaidoirie', 'Débat libre', 'Autre']
adminconf = [['0', 'Utilisateur'], ['1', 'Admin']]

firstaccount = "firstaccount"
