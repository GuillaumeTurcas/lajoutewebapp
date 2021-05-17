from model.convenient.importAPI import *

apiCours = Blueprint("apiCours", __name__)


####################API ACCOUNT####################


@apiCours.route(BASE + "/registCours/", methods=["GET", "POST"])
def registCours():
    tokenres = jwt.encode({"add" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]) and token["account"]["admin"] > 0:
            cours = [token["titre"], token["datedb"],
                token["start"], token["end"],
                token["lien"], token["color"]]
            
            tokenres = jwt.encode({"add" : Cours.registCours(cours)}, 
            secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiCours.route(BASE + "/getCours/", methods=["GET", "POST"])
def getCours():
    tokenres = jwt.encode({"get" : False}, 
        secret_key, algorithm = algorithm)

    try:

        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token):
            cours = Cours.getCours()
            tokenres = jwt.encode({"cours": cours, "get" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))


@apiCours.route(BASE + "/delCours/", methods=["GET", "POST"])
def delCours():
    tokenres = jwt.encode({"del" : False}, 
        secret_key, algorithm = algorithm)

    try:
        token = jwt.decode(request.data, secret_key, 
            algorithm = algorithm)

        if verifToken(token["account"]) and token["account"]["admin"] > 0:
            Cours.delCours(token["id"])

            tokenres = jwt.encode({"del" : True}, 
                secret_key, algorithm = algorithm)

    except:
        pass

    return jsonify(tokenres.decode("UTF-8"))
