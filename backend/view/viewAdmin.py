from backend.util.importFlask import *

viewAdmin = Blueprint("viewAdmin", __name__)


@viewAdmin.route("/registInfos", methods=["GET", "POST"])
def registInfos():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            if request.method == "POST":
                data = {
                    "datedb" : request.form["datedb"],
                    "description" : request.form["description"]
                }

                print(Request.post(f"/registInfos", data))

                return redirect(url_for("viewBase.homepage"))

    return gandalf()


@viewAdmin.route("/delInfos/<string:id>", methods = ["post","get"])
def delInfos(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:

            print(Request.delete(f"/delInfos/{id}"))

            return redirect(url_for("viewBase.homepage"))

    return gandalf()


@viewAdmin.route("/registCours", methods=["GET", "POST"])
def registCours():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            if request.method == "POST":
                data = {
                    "titre" : request.form["titre"],
                    "datedb" : request.form["datedb"],
                    "start" : request.form["start"],
                    "end" : request.form["end"],
                    "lien" : request.form["lien"],
                    "color" : request.form["color"],
                }

                print(Request.post(f"/registCours", data))

                return redirect(url_for("viewBase.application"))

    return gandalf()


@viewAdmin.route("/delCours/<string:id>", methods = ["POST","GET"])
def delCours(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:
            print(Request.delete(f"/delCours/{id}"))

            return redirect(url_for("viewBase.application"))

    return gandalf()


@viewAdmin.route("/presentAccounts/", methods=["POST"])
def presentAccounts():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            if request.method == "POST":
                print(Request.post(f"/presentAccounts"))

                return redirect(url_for("viewBase.application"))

    return gandalf()


@viewAdmin.route("/presentAccount/", methods=["POST"])
def presentAccount():
    if session.get("logged_in"):
        if request.method == "POST":
            print(Request.post(f"/presentAccount"))

            return redirect(url_for("viewBase.application"))

    return gandalf()
