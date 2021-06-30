from backend.util.importAPI import *

controlSujet = Blueprint("controlSujet", __name__)


@controlSujet.route(f"{BASE}/registSujets", methods=["POST"])
def registSujets():
    
    response = {
        "add" : False
    }

    try:
        token = request.headers
        data = json.loads(request.data)

        if verifToken(token) and int(token["admin"]) > 0:
            sujet = [data["sujet"], data["type"]]
            response["add"] = Sujets.registSujets(sujet)

    except:
        pass

    return json.dumps(response)


@controlSujet.route(f"{BASE}/getSujets/<typeSujet>", methods=["GET"])
def getSujets(typeSujet):

    response = {
        "get" : False
    }

    try:
        token = request.headers
        if verifToken(token):
            response = {
                "get" : True,
                "sujet" : Sujets.getSujets(typeSujet)
            }

    except:
        pass

    return json.dumps(response)


@controlSujet.route(f"{BASE}/getSujet/<id>", methods=["GET"])
def getSujet(id):
    
    response = {
        "get" : True
    }

    try:
        token = request.headers

        if verifToken(token):
            response = {
                "get" : True,
                "sujet" : Sujets.getSujet(id)
            }

    except:
        pass

    return json.dumps(response)


@controlSujet.route(f"{BASE}/updateSujet/<id>", methods=["POST"])
def updateSujet(id):
    
    response = {
        "update" : False
    }

    try:
        token = request.headers
        data = json.loads(request.data)
        
        if verifToken(token) and int(token["admin"]) > 0:
            sujet = [data["sujet"], data["type"]]
            response["update"] = Sujets.updateSujet(id, sujet)
    
    except:
        pass

    return json.dumps(response)


@controlSujet.route(f"{BASE}/delSujet/<id>", methods=["DELETE"])
def delSujet(id):

    response = {
        "del" : False
    }

    try:
        token = request.headers

        if verifToken(token) and int(token["admin"]) > 0:
            response["del"] = Sujets.delSujet(id)

    except:
        pass

    return json.dumps(response)


@controlSujet.route(f"{BASE}/funSujet", methods=["POST"])
def funSujet():
    
    response = {
        "get" : False
    }

    try:
        data = json.loads(request.data)

        sujets = Sujets.getSujets(data["type"])
        training = trainingFun(sujets, data["equvsequ"], data["equ"])

        response = {
            "get" : True,
            "training" : training
        }

    except:
        pass

    return json.dumps(response)
