import jwt
from model.config.config import secret_key, algorithm
from model.model.Accounts import Accounts

def verifToken(token):
    try:
        account = Accounts.getAccount(token["id"])
        if account[1] == token["username"] :
            if account[4] == token["admin"]:
                return True

    except:
        return False
