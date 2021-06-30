from backend.util.importAPI import *

viewTest = Blueprint("viewTest", __name__)

@viewTest.route("/orders/<uuid>", methods=["GET", "POST"])
def order(uuid):
    print(uuid, json.loads(request.data))
    return json.dumps({"account":"oui"})
 
