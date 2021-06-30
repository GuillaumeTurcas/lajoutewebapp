from backend.util.importAPI import *

controlAccount = Blueprint("controlAccount", __name__)


@controlAccount.route(f"{BASE}/registAccount/", methods=["POST"])
def registAccount():

    response = {
        "add" : False,
        "gandalf" : False
    }

    try:
        if (request.method == "POST"):
            account = json.loads(request.data)

            if ishackme(username = account["username"], 
                email = account["email"], 
                nom = account["nom"], 
                prenom = account["prenom"], ecole = account["ecole"], 
                annee = account["annee"], 
                specialite = account["specialite"]):

                response = {
                    "add" : False, 
                    "gandalf" : True
                }

            verifAccount = not Accounts.verifAccount(account["username"])

            if verifAccount :
                if int(request.headers["admin"]) >= int(account["admin"]):
                    tokenAccount = createToken(account["username"])
                    
                    account["password"] = defaultpass \
                        if account["create"] \
                        else account["password"]
                    
                    account["password"] = hashpassword( tokenAccount, 
                                                    account["password"])
                    
                    account["admin"] = 2 \
                        if account["username"] == firstaccount \
                        else account["admin"]

                    newaccount = [account["username"].lower(), 
                        account["password"], account["email"], 
                        account["admin"], account["nom"], 
                        account["prenom"], account["ecole"], 
                        account["annee"], account["phone"], 
                        account["specialite"], tokenAccount]
                    
                    response["add"] = Accounts.registAccount(newaccount)

    except:
        pass

    return json.dumps(response)


@controlAccount.route(f"{BASE}/logAccount", methods=["GET", "POST"])
def logAccount():

    response = {
        "account" : None,
        "connect" : False, 
        "gandalf" : False
    }

    try :
        if (request.method == "POST"):

            data = json.loads(request.data)
            username = data["username"]
            tokenAccount = Accounts.getToken(username)
            password = hashpassword(tokenAccount, data["password"])
            
            if ishackme(username = username):
                response["gandalf"] = True
            
            account = Accounts.logAccount(username, password)
           
            if account :
                session = dicoAccount(account)
                response = {
                        "account" : session,
                        "connect" : True
                }

    except:
        pass 

    return json.dumps(response)


@controlAccount.route(f"{BASE}/accounts", methods=["GET"])
def getAccounts():

    response =  {
        "account" : None,
        "get" : False
    }

    try :
        headers = request.headers

        if verifToken(headers) :
            accounts = Accounts.getAccounts()

            response = {
                "accounts": accounts, 
                "get" : True
            }

    except:
        pass

    return json.dumps(response)


@controlAccount.route(f"{BASE}/account/<id>", methods=["GET"])
def getAccount(id):
    
    response =  {
        "account" : None,
        "get" : False
    }

    try :
        token = request.headers

        if verifToken(token) :
            getAccount = Accounts.getAccount(id)

            if int(token["admin"]) > 1 or token["token"] == getAccount[13]:
                account = dicoAccount(getAccount)

                response = {
                    "account": account, 
                    "get" : True
                }

    except:
        pass

    return json.dumps(response)


@controlAccount.route(f"{BASE}/updateAccount/<id>", methods=["POST"])
def updateAccount(id):

    response = {
        "update" : False,
        "gandalf" : False
    }

    try :
        token = request.headers
        data = json.loads(request.data)

        account = dicoAccount(Accounts.getAccount(id))
        new_account = data

        if verifToken(token) \
            and (int(token["admin"]) >= int(account["admin"]) \
            or token["id"] == account[0]):

            update_account = []

            for key, value in account.items():
                for newkey, newvalue in new_account.items():
                    if key == newkey:
                        account[key] = new_account[key]
                    
                update_account.append(account[key])
            
            if ishackme(username = update_account[1], 
                    email = update_account[3], 
                    nom = update_account[6], 
                    prenom = update_account[7], 
                    ecole = update_account[8], 
                    annee = update_account[9], 
                    specialite = update_account[11]):

                response["gandalf"] = True

            response["update"] = Accounts.updateAccount(update_account)


    except:
        pass

    return json.dumps(response)


@controlAccount.route(f"{BASE}/updatePassword/<id>", methods=["POST"])
def updatePassword(id):

    response =  {
        "update" : False 
    }

    try:
        token = request.headers
        data = json.loads(request.data)

        if verifToken(token):
            newaccount = dicoAccount(Accounts.getAccount(id))
            username = newaccount["username"]
            password = hashpassword(newaccount["token"], data["password"])

            if (data["forced"] and int(token["admin"]) > 1) \
                or Accounts.logAccount(username, password):
                if (int(token["admin"]) >= int(newaccount["admin"]) \
                    or int(id) == int(token["id"])):

                    newpassword =  defaultpass if data["forced"] else data["newpassword"]
                    newpassword = hashpassword(newaccount["token"], newpassword)

                    response["update"] = Accounts.updatePassword(newpassword, username)
    except:
        pass

    return json.dumps(response)


@controlAccount.route(f"{BASE}/presentAccounts", methods=["POST"])
def presentAccounts():

    response = {
        "post" : False
    }

    try:
        token = request.headers

        if verifToken(token) and int(token["admin"]) > 0:
            
            response["post"] = Accounts.presentAccounts()

    except:
        pass

    return json.dumps(response)

@controlAccount.route(f"{BASE}/presentAccount", methods=["POST"])
def presentAccount():

    response = {
            "post" : False
    }

    try:
        token = request.headers

        if verifToken(token):
            response["post"] = Accounts.presentAccount(token["id"])

    except:
        pass

    return json.dumps(response)


@controlAccount.route(f"{BASE}/delAccount/<id>", methods=["DELETE"])
def delAccount(id):

    response = {
            "del" : False
    }

    try:
        token = request.headers

        if verifToken(token):
            account = Accounts.getAccount(id)

            if int(account[4]) <= int(token["admin"]):
                reponse["del"] = Accounts.delAccount(id)
    except:
        pass
    
    return json.dumps(response)
