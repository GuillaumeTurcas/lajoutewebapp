from model.convenient.importAPI import *

apiInfos = Blueprint("apiInfos", __name__)


####################API ACCOUNT####################


@apiInfos.route(BASE + "/registInfos/", methods=["GET", "POST"])
def registInfos():
    tokenres = jwt.encode({"add" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]) and token["account"]["admin"] > 0:
            info = [token["datedb"], token["description"]]

            tokenres = jwt.encode({"add" : Infos.registInfos(info)}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiInfos.route(BASE + "/getInfos/", methods=["GET", "POST"])
def getInfos():
    tokenres = jwt.encode({"get" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token):
            info = Infos.getInfos()
            tokenres = jwt.encode({"infos": info, "get" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiInfos.route(BASE + "/delInfos/", methods=["GET", "POST"])
def delInfos():
    tokenres = jwt.encode({"del" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]) and token["account"]["admin"] > 0:
            Infos.delInfos(token["id"])

            tokenres = jwt.encode({"del" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))
