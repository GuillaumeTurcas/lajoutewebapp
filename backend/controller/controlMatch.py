from backend.util.importAPI import *

controlMatch = Blueprint("controlMatch", __name__)


@controlMatch.route(f"{BASE}/registMatchs/", methods=["POST"])
def registMatchs():
    
    response = {
        "add" : False
    }
    print(1)
    
    try:
        token = request.headers
        print(token)
        data = json.loads(request.data)
        print(data)
        if verifToken(token) and int(token["admin"]) > 0:

            match = [data["datedb"], data["type"],
                data["sujet"], data["equipe"],
                data["gouvernement"], data["opposition"],
                data["morateur"], data["mequipe"],
                data["jury"]]
            print(match)
            response["add"] = Matchs.registMatchs(match)

    except:
        pass

    return json.dumps(response)


@controlMatch.route(f"{BASE}/getMatchs/<typeMatch>", methods=["GET"])
def getMatchs(typeMatch):
    
    response = {
        "get" : False
    }

    try:
        token = request.headers

        if verifToken(token):
            response = {
                "get" : True,
                "match" : Matchs.getMatchs(typeMatch)
            }

    except:
        pass

    return json.dumps(response)


@controlMatch.route(f"{BASE}/getMatch/<id>", methods=["GET"])
def getMatch(id):
    
    response = {
        "get" : False,
        "match" : None
    }

    try:
        token = request.headers

        if verifToken(token):
            response = {
                "get" : True,
                "match" : Matchs.getMatch(id)
            }

    except:
        pass

    return json.dumps(response)


@controlMatch.route(f"{BASE}/updateMatch/<id>", methods=["POST"])
def updateMatch(id):

    response = {
        "update" : False
    }

    try:
        token = request.headers
        data = json.loads(request.data)

        if verifToken(token) and int(token["admin"]) > 0:
            match = [data["datedb"], data["type"],
                data["sujet"], data["equipe"],
                data["gouvernement"], data["opposition"],
                data["morateur"], data["mequipe"],
                data["jury"]]
            response["update"] = Matchs.updateMatch(id, match)

    except:
        pass

    return json.dumps(response)


@controlMatch.route(f"{BASE}/delMatch/<id>", methods=["DELETE"])
def delMatch(id):

    response = {
        "del" : False
    }

    try:
        token = request.headers

        if verifToken(token) and int(token["admin"]) > 0:
            response["delete"] = Matchs.delMatchs(id)

    except:
        pass

    return jsonify(response)
