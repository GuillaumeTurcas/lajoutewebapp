from backend.util.importFlask import *

viewSujet = Blueprint("viewSujet", __name__)


@viewSujet.route("/setSujet", methods = ["POST"])
def setSujet():
    if session.get("logged_in"):
        session["sujets"] = request.form["type"]
        
        return redirect(url_for("viewBase.sujet"))

    return gandalf()


@viewSujet.route("/registSujets", methods=["GET", "POST"])
def registSujets():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            if request.method == "POST":
                data = {
                    "sujet" : request.form["sujet"],
                    "type" : request.form["type"]
                }

                print(Request.post(f"/registSujets", data))

                return redirect(url_for("viewBase.sujet"))

    return gandalf()


@viewSujet.route("/updateSujet/<string:id>", methods = ["POST","GET"])
def updateSujet(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:
            sujet = Request.get(f"/getSujet/{id}")

            return render_template("updateSujet.html", 
                sujet = sujet["sujet"], 
                sujetsconf = sujetsconf)

    return gandalf()


@viewSujet.route("/updateSujetFun/<string:id>", methods = ["POST","GET"])
def updateSujetFun(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:
            data = {
                "sujet" : request.form["sujet"],
                "type" : request.form["type"],
            }
            
            print(Request.post(f"/updateSujet/{id}", data))

            return redirect(url_for("viewBase.sujet"))

    return gandalf()


@viewSujet.route("/delSujet/<string:id>", methods = ["POST","GET"])
def delSujet(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:
            print(Request.delete(f"/delSujet/{id}"))

            return redirect(url_for("viewBase.sujet"))

    return gandalf()
