import jwt
import json

from backend.init.config import secret_key, algorithm
from backend.model.Accounts import *
from backend.util.dicoAccount import dicoAccount

def verifToken(token):
    getAccount = dicoAccount(Accounts.getAccount(token["id"]))
    try :
        if token["token"] == getAccount["token"]:
            if int(token["admin"]) == getAccount["admin"]:
                if int(token["id"]) == getAccount["id"] :

                    return True

    except:
        return False
