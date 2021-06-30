from backend.util.importAPI import *

controlInfos = Blueprint("controlInfos", __name__)


@controlInfos.route(f"{BASE}/registInfos", methods=["POST"])
def registInfos():
    response = {
        "add" : False
    }

    try:
        token = request.headers
        data = json.loads(request.data)

        if verifToken(token) and int(token["admin"]) > 0:
            info = [data["datedb"], data["description"]]
            
            response["add"] = Infos.registInfos(info)

    except:
        pass

    return json.dumps(response)


@controlInfos.route(f"{BASE}/infos", methods=["GET"])
def getInfos():

    response = {
        "get" : False
    }

    try:
        headers = request.headers

        if verifToken(headers):
            response = {
                "infos": Infos.getInfos(), 
                "get" : True
            }

    except:
        pass

    return json.dumps(response)


@controlInfos.route(f"{BASE}/delInfos/<id>", methods=["DELETE"])
def delInfos(id):
    
    response = {
            "del" : False
    }

    try:
        token = request.headers

        if verifToken(token) and int(token["admin"]) > 0:
            response["del"] = Infos.delInfos(id)

    except:
        pass

    return json.dumps(response)
