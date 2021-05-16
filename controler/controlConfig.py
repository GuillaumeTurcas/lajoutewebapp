from model.convenient.importflask import *

controlConfig = Blueprint("controlConfig", __name__)


@controlConfig.route("/setConfig", methods = ["POST"])
def setConfig():
    if session.get('logged_in'):
        if session["admin"] > 2:
            session["config"] = request.form["name"]
            return redirect(url_for("controlBase.config"))

    return gandalf()


@controlConfig.route("/setConfigType", methods = ['POST'])
def setConfigType():
    if session.get("logged_in"):
        if session["admin"] > 2:
            session["configtype"] = "Unique" if session["configtype"] == "Pass" else "Pass"
            return redirect(url_for("controlBase.config"))

    return gandalf()


@controlConfig.route("/registConfig", methods=['POST'])
def registConfig():
    if session.get("logged_in"):
        if session["admin"] > 2:
            if request.method == 'POST':
                token = {
                    "account" : session["account"],
                    "typeconf" : str(session["configtype"]),
                    "name" : request.form["name"],
                    "value" : request.form["value"],
                    "descr" : request.form["descr"]
                }
                
                print(decode(requests.post("http://0.0.0.0/api/registConfig/", 
                    encode(token))))
                
                return redirect(url_for("controlBase.config"))

    return gandalf()


@controlConfig.route("/updateConfig/<string:id>", methods = ["POST","GET"])
def updateConfig(id):
    if session.get("logged_in"):
        if session["admin"] > 2:
            token = {
                "account" : session["account"],
                "id" : id
            }

            config = decode(requests.post("http://0.0.0.0/api/getConfig/", 
                encode(token)))

            return render_template("updateConfig.html", 
                config = config["config"], names = nameconf(session["configtype"]) )

    return gandalf()


@controlConfig.route("/updateConfigFun/<string:id>", methods = ["POST","GET"])
def updateConfigFun(id):
    if session.get("logged_in"):
        if session["admin"] > 2:
            token = {
                "account" : session["account"],
                "typeconf" : request.form["type"],
                "name" : request.form["name"],
                "value" : request.form["value"],
                "descr" : request.form["descr"],
                "id" : id,
            }

            print(decode(requests.post("http://0.0.0.0/api/updateConfig/", 
                encode(token))))

            return redirect(url_for("controlBase.config"))

    return gandalf()


@controlConfig.route("/delConfig/<string:id>", methods = ["POST","GET"])
def delConfig(id):
    if session.get("logged_in"):
        if session["admin"] > 2:
            token = {
                "account" : session["account"],
                "id" : id
            }

            print(decode(requests.post("http://0.0.0.0/api/delConfig/", 
                encode(token))))

            return redirect(url_for("controlBase.config"))

    return gandalf()