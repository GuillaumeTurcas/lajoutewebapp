from model.convenient.importAPI import *

apiAccount = Blueprint("apiAccount", __name__)


####################API ACCOUNT####################


@apiAccount.route("/api/registAccount/", methods=["GET", "POST"])
def registAccount():
    tokenres = jwt.encode({"add" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, algorithm = algorithm)
        account = token["account"]

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

                tokenres = jwt.encode({"add" : True}, 
                    secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route("/api/logAccount/", methods=["POST", "GET"])
def logAccount():
    tokenres = jwt.encode({"connect" : False}, 
        secret_key, algorithm = algorithm)

    try :
        if (request.method == "POST"):
            token = jwt.decode(request.data, secret_key, algorithm = algorithm)
            username = token["username"].lower()
            password = hashpassword(username, token["password"])

            if ishackme(username = username):
                return jwt.encode({"message": "gandalf", "connect" : False}, 
                    secret_key, algorithm = algorithm)

            account = Accounts.logAccount(username, password)

            if account :
                session = dicoAccount(account)
                tokenres = jwt.encode({"account": session, "connect" : True}, 
                    secret_key, algorithm = algorithm)

    except:
        pass 

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route("/api/getAccount/", methods=["GET", "POST"])
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


@apiAccount.route("/api/getAccounts/", methods=["GET", "POST"])
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


@apiAccount.route("/api/updateAccount/", methods=["GET", "POST"])
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

            print(0, account)
            print(1, newaccount)

            for key, value in account.items():
                for newkey, newvalue in newaccount.items():
                    if key == newkey:
                        account[key] = newaccount[key]
                    
                updateAccount.append(account[key])

            if oldUsername != newUsername:
                updateAccount[2] = hashpassword(updateAccount[1], defaultpass)
                passw = True

            print(updateAccount)

            update = Accounts.updateAccount(updateAccount)

            print(1, update)

            tokenres =  jwt.encode({"update" : update, "password" : passw}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route("/api/updatePassword/", methods=["GET", "POST"])
def updatePassword():
    tokenres =  jwt.encode({"update" : False}, secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, algorithm = algorithm)

        if verifToken(token["account"]):
            account = token["account"]
            newaccount = dicoAccount(Accounts.getAccount(token["id"]))
            username = newaccount["username"]
            password = hashpassword(username, token["password"])

            if (token["forced"] and int(token["admin"]) > 1) or Accounts.logAccount(username, password):
                if (int(token["admin"]) <= int(account["admin"]) or int(token["id"]) == int(account["id"])):
                    newpassword =  defaultpass if token["forced"] else token["newpassword"]
                    newpassword = hashpassword(username, newpassword)

                    tokenres = jwt.encode({"update" : 
                        Accounts.updatePassword(newpassword, username)}, 
                        secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route("/api/presentAccounts/", methods=["GET", "POST"])
def presentAccounts():
    tokenres = jwt.encode({"present" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, algorithm = algorithm)
        account = token["account"]

        if verifToken(account):
            tokenres = jwt.encode({"present" : Accounts.presentAccounts()}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiAccount.route("/api/presentAccount/", methods=["GET", "POST"])
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


@apiAccount.route("/api/delAccount/", methods=["GET", "POST"])
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
