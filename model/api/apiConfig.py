from model.convenient.importAPI import *

apiConfig = Blueprint("apiConfig", __name__)


####################API ACCOUNT####################


@apiConfig.route("/api/registConfig/", methods=["GET", "POST"])
def registConfig():
    tokenres = jwt.encode({"add" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
        algorithm = algorithm)

        if verifToken(token["account"]) and token["account"]["admin"] > 2 :
            config = [
                token["typeconf"], token["name"],
                token["value"], token["descr"]]

            tokenres = jwt.encode({"add" : Config.registConfig(config)}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiConfig.route("/api/getConfigs/", methods=["GET", "POST"])
def getConfigs():
    tokenres = jwt.encode({"get" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]) and token["account"]["admin"] > 2 :
            tokenres = jwt.encode({"config": Config.getConfigs(token["name"], 
                token["type"]), "get" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))



@apiConfig.route("/api/getConfig/", methods=["GET", "POST"])
def getConfig():
    tokenres = jwt.encode({"get" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]) and token["account"]["admin"] > 2:
            tokenres = jwt.encode({"config": Config.getConfig(token["id"]), 
                "get" : True}, secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiConfig.route("/api/updateConfig/", methods=["GET", "POST"])
def updateConfig():
    tokenres = jwt.encode({"update" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"])  and token["account"]["admin"] > 2:
            config = [
                token["typeconf"], token["name"],
                token["value"], token["descr"]]
            print(config)

            tokenres = jwt.encode({"update" : 
                Config.updateConfig(token["id"], config)}, 
                    secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiConfig.route("/api/delConfig/", methods=["GET", "POST"])
def delConfig():
    tokenres = jwt.encode({"del" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]):
            Config.delConfig(token["id"])

            tokenres = jwt.encode({"del" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))
