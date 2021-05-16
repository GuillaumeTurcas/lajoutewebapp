from model.convenient.importflask import *

controlAdmin = Blueprint("controlAdmin", __name__)

@controlAdmin.route("/registInfos", methods=["GET", "POST"])
def registInfos():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            if request.method == "POST":
                token = {
                    "account" : session["account"],
                    "datedb" : request.form["datedb"],
                    "description" : request.form["description"]
                }

                print(decode(requests.post("http://0.0.0.0/api/registInfos/", 
                    encode(token))))

                return redirect(url_for("controlBase.homepage"))

    return gandalf()


@controlAdmin.route("/delInfos/<string:id>", methods = ["post","get"])
def delInfos(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:
            token = {
                "account" : session["account"],
                "id" : id
            }


            print(decode(requests.post("http://0.0.0.0/api/delInfos/", 
                encode(token))))

            return redirect(url_for("controlBase.homepage"))

    return gandalf()


@controlAdmin.route("/registCours", methods=["GET", "POST"])
def registCours():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            if request.method == "POST":
                token = {
                    "account" : session["account"],
                    "titre" : request.form["titre"],
                    "datedb" : request.form["datedb"],
                    "start" : request.form["start"],
                    "end" : request.form["end"],
                    "lien" : request.form["lien"],
                    "color" : request.form["color"],
                }

                print(decode(requests.post("http://0.0.0.0/api/registCours/", 
                    encode(token))))

                return redirect(url_for("controlBase.application"))

    return gandalf()


@controlAdmin.route("/delCours/<string:id>", methods = ["POST","GET"])
def delCours(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:
            token = {
                "account" : session["account"],
                "id" : id
            }

            print(decode(requests.post("http://0.0.0.0/api/delCours/", 
                encode(token))))

            return redirect(url_for("controlBase.application"))

    return gandalf()


@controlAdmin.route("/presentAccounts/", methods=["POST"])
def presentAccounts():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            if request.method == "POST":
                print(decode(requests.post("http://0.0.0.0/api/presentAccounts/", 
                    encode({"account" : session["account"]}))))

                return redirect(url_for("controlBase.application"))

    return gandalf()


@controlAdmin.route("/presentAccount/", methods=["POST"])
def presentAccount():
    if session.get("logged_in"):
        if request.method == "POST":
            print(decode(requests.post("http://0.0.0.0/api/presentAccount/", 
                encode({"account" : session["account"]}))))

            return redirect(url_for("controlBase.application"))

    return gandalf()
