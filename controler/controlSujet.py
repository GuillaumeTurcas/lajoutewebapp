from model.convenient.importflask import *

controlSujet = Blueprint("controlSujet", __name__)


@controlSujet.route("/setSujet", methods = ["POST"])
def setSujet():
    if session.get("logged_in"):
        session["sujets"] = request.form["type"]
        return redirect(url_for("controlBase.sujet"))

    return gandalf()


@controlSujet.route("/registSujets", methods=["GET", "POST"])
def registSujets():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            if request.method == "POST":
                token = {
                    "account" : session["account"],
                    "sujet" : request.form["sujet"],
                    "type" : request.form["type"]
                }

                print(decode(requests.post("http://0.0.0.0/api/registSujets/", 
                    encode(token))))

                return redirect(url_for("controlBase.sujet"))

    return gandalf()


@controlSujet.route("/updateSujet/<string:id>", methods = ["POST","GET"])
def updateSujet(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:
            token = {
                "account" : session["account"], 
                "id" : id
            }

            sujet = decode(requests.post("http://0.0.0.0/api/getSujet/", 
                encode(token)))

            return render_template("updateSujet.html", 
                sujet = sujet["sujet"], sujetsconf = sujetsconf)

    return gandalf()

@controlSujet.route("/updateSujetFun/<string:id>", methods = ["POST","GET"])
def updateSujetFun(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:
            token = {
                "account" : session["account"],
                "sujet" : request.form["sujet"],
                "type" : request.form["type"],
                "id" : id
            }
            print(decode(requests.post("http://0.0.0.0/api/updateSujet/", 
                encode(token))))

            return redirect(url_for("controlBase.sujet"))

    return gandalf()


@controlSujet.route("/delSujet/<string:id>", methods = ["POST","GET"])
def delSujet(id):
    if session.get("logged_in"):
        if session["admin"] !=  0:
            token = {
                "account" : session["account"],
                "id" : id
            }

            print(decode(requests.post("http://0.0.0.0/api/delSujet/", 
                encode(token))))

            return redirect(url_for("controlBase.sujet"))

    return gandalf()
