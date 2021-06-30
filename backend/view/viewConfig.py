from backend.util.importFlask import *

viewConfig = Blueprint("viewConfig", __name__)


@viewConfig.route("/setConfig", methods = ["POST"])
def setConfig():
    if session.get('logged_in'):
        if session["admin"] > 2:
            session["config"] = request.form["name"]

            return redirect(url_for("viewBase.config"))

    return gandalf()


@viewConfig.route("/setConfigType", methods = ['POST'])
def setConfigType():
    if session.get("logged_in"):
        if session["admin"] > 2:
            session["configtype"] = "Unique" if session["configtype"] == "Pass" else "Pass"

            return redirect(url_for("viewBase.config"))

    return gandalf()


@viewConfig.route("/registConfig", methods=['POST'])
def registConfig():
    if session.get("logged_in"):
        if session["admin"] > 2:
            if request.method == 'POST':
                data = {
                    "typeconf" : str(session["configtype"]),
                    "name" : request.form["name"],
                    "value" : request.form["value"],
                    "descr" : request.form["descr"]
                }

                print(Request.post(f"/registConfig", data))
                
                return redirect(url_for("viewBase.config"))

    return gandalf()


@viewConfig.route("/updateConfig/<string:id>", methods = ["POST","GET"])
def updateConfig(id):
    if session.get("logged_in"):
        if session["admin"] > 2:
            config = Request.get(f"/getConfig/{id}")

            return render_template("updateConfig.html", 
                config = config["config"], names = config["name"])

    return gandalf()


@viewConfig.route("/updateConfigFun/<string:id>", methods = ["POST","GET"])
def updateConfigFun(id):
    if session.get("logged_in"):
        if session["admin"] > 2:
            data = {
                "typeconf" : request.form["type"],
                "name" : request.form["name"],
                "value" : request.form["value"],
                "descr" : request.form["descr"],
            }

            print(Request.post(f"/updateConfig/{id}", data))

            return redirect(url_for("viewBase.config"))

    return gandalf()


@viewConfig.route("/delConfig/<string:id>", methods = ["POST","GET"])
def delConfig(id):
    if session.get("logged_in"):
        if session["admin"] > 2:
            token = {
                "account" : session["account"],
                "id" : id
            }
            print(Request.delete(f"/delConfig/{id}"))

            return redirect(url_for("viewBase.config"))

    return gandalf()
