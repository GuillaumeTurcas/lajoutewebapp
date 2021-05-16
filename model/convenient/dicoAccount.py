import random

def dicoAccount(response):
    account = {
        "id" : response[0],
        "username" : response[1],
        "password" : response[2],
        "email" : response[3],
        "admin" : response[4],
        "present" : response[5],
        "nom" : response[6],
        "prenom" : response[7],
        "ecole" : response[8],
        "annee" : response[9],
        "phone" : response[10],
        "specialite" : response[11],
        "theme" : response[12]
    }

    return account
