from backend.util.importAPI import *

apiMatch = Blueprint("apiMatch", __name__)


####################API ACCOUNT####################


@apiMatch.route(BASE + "/registMatchs/", methods=["GET", "POST"])
def registMatchs():
    tokenres = jwt.encode({"add" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]) and token["account"]["admin"] > 0:

            match = [token["datedb"], token["type"],
                token["sujet"], token["equipe"],
                token["gouvernement"], token["opposition"],
                token["morateur"], token["mequipe"],
                token["jury"]]
            
            tokenres = jwt.encode({"add" : Matchs.registMatchs(match)}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiMatch.route(BASE + "/getMatchs/", methods=["GET", "POST"])
def getMatchs():
    tokenres = jwt.encode({"get" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]):
            tokenres = jwt.encode({"matchs": Matchs.getMatchs(token["type"]), "get" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiMatch.route(BASE + "/getMatch/", methods=["GET", "POST"])
def getMatch():
    tokenres = jwt.encode({"get" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]):
            tokenres = jwt.encode({"match": Matchs.getMatch(token["id"]), "get" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiMatch.route(BASE + "/updateMatch/", methods=["GET", "POST"])
def updateMatch():
    tokenres = jwt.encode({"update" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]) and token["account"]["admin"] > 0:
            match = [token["datedb"], token["type"],
                token["sujet"], token["equipe"],
                token["gouvernement"], token["opposition"],
                token["morateur"], token["mequipe"],
                token["jury"]]
            
            tokenres = jwt.encode({"update" : 
                Matchs.updateMatchs(token["id"], match)}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiMatch.route(BASE + "/delMatch/", methods=["GET", "POST"])
def delMatch():
    tokenres = jwt.encode({"del" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]) and token["account"]["admin"] > 0:
            tokenres = jwt.encode({"del" : Matchs.delMatchs(token["id"])}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))
