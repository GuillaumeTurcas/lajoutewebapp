from backend.util.importAPI import *

viewTest = Blueprint("viewTest", __name__)

@viewTest.route("/orders/<uuid>", methods=["GET", "POST"])
def order(uuid):
    print(uuid, json.loads(request.data))
    return json.dumps({"account":"oui"})

@viewTest.route("/grostest", methods=["GET", "POST"])
def test():
    response = jsonify()
    response.status_code = 418
    return response


@viewTest.route("/clement", methods=["GET", "POST"])
def clement():
    data ={
        "Association":"La Joute de Vinci",
        "isTheBestAsso": True
    }

    return json.dumps(data)
