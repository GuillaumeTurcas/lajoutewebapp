from backend.util.importAPI import *

controlCours = Blueprint("controlCours", __name__)


@controlCours.route(f"{BASE}/registCours", methods=["POST"])
def registCours():

    response = {
        "add" : False
    }

    try:
        token = request.headers
        data = json.loads(request.data)
        
        if verifToken(token) and int(token["admin"]) > 0:
            cours = [data["titre"], data["datedb"],
                data["start"], data["end"],
                data["lien"], data["color"]]


            response["add"] = Cours.registCours(cours)

    except:
        pass

    return jsonify(response)


@controlCours.route(f"{BASE}/getCours", methods=["GET"])
def getCours():

    response = {
        "cours" : None, 
        "get" : "False"
    }

    try:
        token = request.headers

        if verifToken(token):
            response = {
                "cours" : Cours.getCours(),
                "get" : True
            }

    except:
        pass

    return json.dumps(response)


@controlCours.route(f"{BASE}/delCours/<id>", methods=["DELETE"])
def delCours(id):

    response = {
        "del" : False
    }

    try:
        token = request.headers

        if verifToken(token) and int(token["admin"]) > 0:
            Cours.delCours(token["id"])
            response["del"] = Cours.delCours(id)

    except:
        pass
    
    return json.dumps(response)
