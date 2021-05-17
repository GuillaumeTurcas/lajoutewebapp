''' The config file ! '''

host = "localhost"
user = "root"
passwd = "lajoute"
db = "lajoute"
firstaccount = ""

''' The Data base '''

import os, binascii
import mysql.connector

mydb = mysql.connector.connect(
    host = host,
    user = user,
    password = passwd,
    database = db
)

mycursor = mydb.cursor()


''' Here is the magic ! '''


secret_key, salt, hf_name, iterations, dksize, algorithm = '', '', '', 1, 1, ''
hf_name_pepper, iterations_pepper, dksize_pepper, defaultpass = '', 1, 1, ''
ecoleconf, anneeconf, adminconf, sujetsconf, speconf, dbpconf = [], [], [], [], [], []
BASE, URL = '', ''


mycursor.execute("SELECT * FROM config") 
config = mycursor.fetchall()

for config in config:

    ''' Secret Key '''

    if config[3] == "secret_key":
        secret_key = config[4]

    ''' Password '''

    if config[3] == "salt":
        salt = str(config[4])

    if config[3] == "hf_name":
        hf_name = config[4]

    if config[3] == "iterations":
        iterations = int(config[4])

    if config[3] == "dksize":
        dksize = int(config[4])

    ''' Password Pepper '''

    if config[3] == "hf_name_pepper":
        hf_name_pepper = config[4]

    if config[3] == "iterations_pepper":
        iterations_pepper = int(config[4])

    if config[3] == "dksize_pepper":
        dksize_pepper = int(config[4])

    ''' Defaultpass '''

    if config[3] == "defaultpass":
        defaultpass = config[4]

    ''' Token '''
    if config[3] == "algorithm":
        algorithm = config[4]

    if config[3] == "BASE":
        BASE = config[4]

    if config[3] == "URL":
        URL = config[4]

    ''' Config '''

    if config[2] == "École":
        ecoleconf.append(config[3]) 

    if config[2] == "Année":
        anneeconf.append(config[3]) 

    if config[2] == "Spécialité":
        speconf.append(config[3]) 

    if config[2] == "Admin":
        adminprov = [config[3], config[4]]
        adminconf.append(adminprov) 

    if config[2] == "Sujet":
        sujetsconf.append(config[3])

    if config[2] == "Débat parlementaire":
        dbpconf.append(config[3]) 


    ''' First account '''

    if config[3] == "firstaccount":
        firstaccount = config[4]
