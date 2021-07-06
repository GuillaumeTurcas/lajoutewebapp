from backend.util.importAPI import *

controlConfig = Blueprint("controlConfig", __name__)


@controlConfig.route(f"{BASE}/registConfig", methods=["POST"])
def registConfig():

    response = {
        "add": False
    }

    try:
        token = request.headers
        data = json.loads(request.data)

        if verifToken(token) and int(token["admin"]) > 2:
            config = [
                data["typeconf"], data["name"],
                data["value"], data["descr"]]

            response["add"] = Config.registConfig(config)

    except:
        pass

    return json.dumps(response)


@controlConfig.route(f"{BASE}/getConfigs/<name>/<typeConfig>", methods=["GET"])
def getConfigs(name, typeConfig):

    response = {
        "get": False
    }

    try:
        token = request.headers

        if verifToken(token) and int(token["admin"]) > 2:
            response = {
                "get": True,
                "config": Config.getConfigs(name, typeConfig),
                "name": nameconf(str(typeConfig))
            }

    except:
        pass

    return json.dumps(response)


@controlConfig.route(f"{BASE}/getConfig/<id>", methods=["GET"])
def getConfig(id):

    response = {
        "get": False
    }

    try:
        token = request.headers

        if verifToken(token) and int(token["admin"]) > 2:
            config = Config.getConfig(id)
            response = {
                "config": config,
                "name": nameconf(str(config[1])),
                "get": True
            }

    except:
        pass

    return json.dumps(response)


@controlConfig.route(f"{BASE}/updateConfig/<id>", methods=["POST"])
def updateConfig(id):

    response = {
        "update": False
    }

    try:
        token = request.headers
        data = json.loads(request.data)

        if verifToken(token) and int(token["admin"]) > 2:
            config = [
                data["typeconf"], data["name"],
                data["value"], data["descr"]]

            response["update"] = Config.updateConfig(id, config)

    except:
        pass

    return json.dumps(response)


@controlConfig.route(f"{BASE}/delConfig/<id>", methods=["DELETE"])
def delConfig(id):

    response = {
        "del": False
    }

    try:
        token = request.headers

        if verifToken(token) and int(token["admin"]) > 2:
            response["del"] = Config.delConfig(id)

    except:
        pass

    return json.dumps(response)
