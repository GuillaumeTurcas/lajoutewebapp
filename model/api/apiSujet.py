from model.convenient.importAPI import *

apiSujet = Blueprint("apiSujet", __name__)


####################API ACCOUNT####################


@apiSujet.route("/api/registSujets/", methods=["GET", "POST"])
def registSujets():
    tokenres = jwt.encode({"add" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
        algorithm = algorithm)

        if verifToken(token["account"]):

            sujet = [token["sujet"], token["type"]]
            tokenres = jwt.encode({"add" : Sujets.registSujets(sujet)}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiSujet.route("/api/getSujets/", methods=["GET", "POST"])
def getSujets():
    tokenres = jwt.encode({"get" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]):
            sujets = Sujets.getSujets(token["sujet"])
            tokenres = jwt.encode({"sujets": sujets, "get" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiSujet.route("/api/getSujet/", methods=["GET", "POST"])
def getSujet():
    tokenres = jwt.encode({"get" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]):
            sujet = Sujets.getSujet(token["id"])
            tokenres = jwt.encode({"sujet": sujet, "get" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiSujet.route("/api/updateSujet/", methods=["GET", "POST"])
def updateSujet():
    tokenres = jwt.encode({"update" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]):
            sujet = [token["sujet"], token["type"]]

            tokenres = jwt.encode({"update" : 
                Sujets.updateSujet(token["id"], sujet)}, 
                    secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiSujet.route("/api/delSujet/", methods=["GET", "POST"])
def delSujet():
    tokenres = jwt.encode({"del" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]):
            Sujets.delSujet(token["id"])

            tokenres = jwt.encode({"del" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiSujet.route("/api/funSujet/", methods=["GET", "POST"])
def funSujet():
    tokenres = jwt.encode({"get" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]):
            sujets = Sujets.getSujets(token["sujet"])

            tokenres = jwt.encode({
                    "get" : True,
                    "training" : trainingFun(sujets, 
                        token["equvsequ"], token["equ"])
                },
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))
