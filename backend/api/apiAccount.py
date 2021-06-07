from backend.util.importAPI import *

apiAccount = Blueprint("apiAccount", __name__)


####################API ACCOUNT####################


@apiAccount.route(BASE + "/registAccount/", methods=["GET", "POST"])
def registAccount():
    tokenres = jwt.encode({"add" : False, "gandalf" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, algorithm = algorithm)
        account = token["account"]

        if ishackme(username = account["username"], 
                    email = account["email"], 
                    nom = account["nom"], 
                    prenom = account["prenom"], 
                    ecole = account["ecole"], 
                    annee = account["annee"], 
                    specialite = account["specialite"]):

            tokenres = jwt.encode({"add" : False, "gandalf" : True}, 
                secret_key, algorithm = algorithm)

            return jsonify(tokenres.decode("UTF-8"))
    

        verifAccount = not Accounts.verifAccount(account["username"])
        verifPass = token["password"] == token["confirmpassword"]

        if verifAccount and verifPass:
            if int(token["admin"]) >= int(account["admin"]):
                account["password"] = defaultpass if token["create"] else account["password"]
                account["password"] = hashpassword(account["username"], account["password"])

                account["admin"] = 2 if account["username"] == firstaccount else account["admin"]

                newaccount = [account["username"].lower(), 
                    account["password"], account["email"], 
                    account["admin"], account["nom"], 
                    account["prenom"], account["ecole"], 
                    account["annee"], account["phone"], 
                    account["specialite"]]

                Accounts.registAccount(newaccount)   

                tokenres = jwt.encode({"add" : True, "gandalf" : False}, 
                    secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route(BASE + "/logAccount/", methods=["POST", "GET"])
def logAccount():
    tokenres = jwt.encode({"connect" : False, "gandalf" : False}, 
        secret_key, algorithm = algorithm)

    try :
        if (request.method == "POST"):
            token = jwt.decode(request.data, secret_key, algorithm = algorithm)
            username = token["username"].lower()
            password = hashpassword(username, token["password"])
            
            if ishackme(username = username):
                tokenres = jwt.encode({"connect" : False, "gandalf" : True}, 
                    secret_key, algorithm = algorithm)
                return jsonify(tokenres.decode("UTF-8"))
            
            account = Accounts.logAccount(username, password)
           
            if account :
                session = dicoAccount(account)
                tokenres = jwt.encode({"account": session, "connect" : True, 
                    "gandalf" : False}, 
                    secret_key, algorithm = algorithm)

    except:
        pass 

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route(BASE + "/getAccount/", methods=["GET", "POST"])
def getAccount():
    tokenres =  jwt.encode({"get" : False}, 
        secret_key, algorithm = algorithm)

    try :
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)
        
        if verifToken(token["account"]) :
            response = Accounts.getAccount(token["id"])
            if int(token["admin"]) > 1 or token["account"]["password"] == response[2]:
                account = dicoAccount(response)
                tokenres = jwt.encode({"account": account, "get" : True}, 
                    secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route(BASE + "/getAccounts/", methods=["GET", "POST"])
def getAccounts():
    tokenres =  jwt.encode({"get" : False}, 
        secret_key, algorithm = algorithm)

    try :
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token) :
            tokenres = jwt.encode({"accounts": Accounts.getAccounts(), "get" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route(BASE + "/updateAccount/", methods=["GET", "POST"])
def updateAccount():
    tokenres =  jwt.encode({"update" : False}, 
        secret_key, algorithm = algorithm)

    try :
        token = jwt.decode(request.data, secret_key, algorithm = algorithm)
        account = dicoAccount(Accounts.getAccount(token["id"]))
        newaccount = token["updateAccount"]

        if verifToken(token["account"]) and (int(token["admin"]) >= int(account["admin"]) or token["id"] == account[0]):
            updateAccount = []
            passw = False
            oldUsername = account["username"]
            newUsername = newaccount["username"]

            for key, value in account.items():
                for newkey, newvalue in newaccount.items():
                    if key == newkey:
                        account[key] = newaccount[key]
                    
                updateAccount.append(account[key])

            if oldUsername != newUsername:
                updateAccount[2] = hashpassword(updateAccount[1], defaultpass)
                passw = True

            if ishackme(username = updateAccount[1], 
                    email = updateAccount[3], 
                    nom = updateAccount[6], 
                    prenom = updateAccount[7], 
                    ecole = updateAccount[8], 
                    annee = updateAccount[9], 
                    specialite = updateAccount[11]):

                tokenres = jwt.encode({"add" : False, "gandalf" : True}, 
                    secret_key, algorithm = algorithm)

                return jsonify(tokenres.decode("UTF-8"))

            update = Accounts.updateAccount(updateAccount)

            tokenres =  jwt.encode({"update" : update, "password" : passw}, 
                secret_key, algorithm = algorithm)

        else :
            tokenres = jwt.encode({"add" : False, "gandalf" : True}, 
                    secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route(BASE + "/updatePassword/", methods=["GET", "POST"])
def updatePassword():
    tokenres =  jwt.encode({"update" : False, "gandalf" : True}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, algorithm = algorithm)

        if verifToken(token["account"]):
            account = token["account"]
            newaccount = dicoAccount(Accounts.getAccount(token["id"]))
            username = newaccount["username"]
            password = hashpassword(username, token["password"])

            if (token["forced"] and int(token["admin"]) > 1) or Accounts.logAccount(username, password):
                if (int(token["admin"]) >= int(newaccount["admin"]) or int(token["id"]) == int(account["id"])):
                    newpassword =  defaultpass if token["forced"] else token["newpassword"]
                    newpassword = hashpassword(username, newpassword)

                    tokenres = jwt.encode({"update" : 
                        Accounts.updatePassword(newpassword, username),
                        "gandalf" : False}, 
                        secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route(BASE + "/presentAccounts/", methods=["GET", "POST"])
def presentAccounts():
    tokenres = jwt.encode({"present" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, algorithm = algorithm)
        account = token["account"]

        if verifToken(account) and token["account"]["admin"] > 0:
            tokenres = jwt.encode({"present" : Accounts.presentAccounts()}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route(BASE + "/presentAccount/", methods=["GET", "POST"])
def presentAccount():
    tokenres = jwt.encode({"present" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, algorithm = algorithm)
        account = token["account"]

        if verifToken(account):
            tokenres = jwt.encode({"present" : Accounts.presentAccount(account["id"])}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route(BASE + "/delAccount/", methods=["GET", "POST"])
def delAccount():
    tokenres = jwt.encode({"del" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]):
            account = Accounts.getAccount(token["id"])

            if int(account[4]) <= int(token["account"]["admin"]):
                Accounts.delAccount(token["id"])

                tokenres = jwt.encode({"del" : True}, 
                    secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))
