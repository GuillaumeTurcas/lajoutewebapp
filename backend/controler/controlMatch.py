from backend.util.importflask import *

controlMatch = Blueprint("controlMatch", __name__)


@controlMatch.route("/setMatch", methods = ["POST"])
def setMatch():
    if session.get("logged_in"):
        session["dparlementaire"] = request.form["type"]
        return redirect(url_for("controlBase.matchs"))

    return gandalf()

@controlMatch.route("/registMatchs", methods=["GET", "POST"])
def registMatchs():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            if request.method == "POST":
                token = {
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

                print(decode(requests.post(f"{URL}{BASE}/registMatchs/", 
                    encode(token))))

                return redirect(url_for("controlBase.matchs"))

    return gandalf()


@controlMatch.route("/updateMatch/<string:id>", methods = ["POST","GET"])
def updateMatch(id):
    if session.get("logged_in"):
        token = {
            "account" : session["account"], 
            "id" : id
        }

        match = decode(requests.post(f"{URL}{BASE}/getMatch/", 
            encode(token)))

        enable = "disabled" if session["admin"] == 0 else ""

        if match["get"] == True:
            return render_template("updateMatch.html", dbparl = match["match"], 
                dbpconf = dbpconf, enabled = enable)

        else :
            return redirect(url_for("controlBase.matchs"))

    return gandalf()

@controlMatch.route("/updateMatchFun/<string:id>", methods = ["POST","GET"])
def updateMatchFun(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:
            token = {
                "account" : session["account"],
                "id" : id,
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
            print(decode(requests.post(f"{URL}{BASE}/updateMatch/", 
                encode(token))))

            return redirect(url_for("controlBase.matchs"))

    return gandalf()


@controlMatch.route("/delMatch/<string:id>", methods = ["POST","GET"])
def delMatch(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:
            token = {
                "account" : session["account"],
                "id" : id
            }
            print(decode(requests.post(f"{URL}{BASE}/delMatch/", 
                encode(token))))

            return redirect(url_for("controlBase.matchs"))

    return gandalf()
