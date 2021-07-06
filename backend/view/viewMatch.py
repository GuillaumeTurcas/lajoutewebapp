from backend.util.importFlask import *

viewMatch = Blueprint("viewMatch", __name__)


@viewMatch.route("/setMatch", methods = ["POST"])
def setMatch():
    if session.get("logged_in"):
        session["dparlementaire"] = request.form["type"]

        return redirect(url_for("viewBase.matchs"))

    return gandalf()


@viewMatch.route("/registMatchs", methods=["GET", "POST"])
def registMatchs():
    if session.get("logged_in"):
        if session["admin"] >  0:
            if request.method == "POST":
                data = {
                    "account" : session["account"],
                    "datedb" : request.form["datedb"],
                    "type" : request.form["type"],
                    "sujet" : request.form["sujet"],
                    "equipe" : request.form["equipe"],
                    "gouvernement" : request.form["gouvernement"],
                    "opposition" : request.form["opposition"],
                    "morateur" : request.form["morateur"],
                    "mequipe" : request.form["mequipe"],
                    "jury" : request.form["jury"]
                }
                
                print(Request.post(f"/registMatchs/", data))

                return redirect(url_for("viewBase.matchs"))

    return gandalf()


@viewMatch.route("/updateMatch/<string:id>", methods = ["POST","GET"])
def updateMatch(id):
    if session.get("logged_in"):

        match = Request.get(f"/getMatch/{id}")
        enable = "disabled" if session["admin"] == 0 else ""

        if match["get"] == True:
            return render_template("updateMatch.html", 
                dbparl = match["match"], 
                dbpconf = dbpconf, 
                enabled = enable)

        else :
            return redirect(url_for("viewBase.matchs"))

    return gandalf()


@viewMatch.route("/updateMatchFun/<string:id>", methods = ["POST","GET"])
def updateMatchFun(id):
    if session.get("logged_in"):
        if session["admin"] >  0:
            data = {
                "account" : session["account"],
                "datedb" : request.form["datedb"],
                "type" : request.form["type"],
                "sujet" : request.form["sujet"],
                "equipe" : request.form["equipe"],
                "gouvernement" : request.form["gouvernement"],
                "opposition" : request.form["opposition"],
                "morateur" : request.form["morateur"],
                "mequipe" : request.form["mequipe"],
                "jury" : request.form["jury"]
            }

            print(Request.post(f"/updateMatch/{id}", data))

            return redirect(url_for("viewBase.matchs"))

    return gandalf()


@viewMatch.route("/delMatch/<string:id>", methods = ["POST","GET"])
def delMatch(id):
    if session.get("logged_in"):
        if session["admin"] >  0:
            print(Request.delete(f"/delMatch/{id}"))

            return redirect(url_for("viewBase.matchs"))

    return gandalf()
