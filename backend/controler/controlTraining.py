from backend.util.importflask import *
from backend.util.trainingFun import trainingFun as training

controlTraining = Blueprint("controlTraining", __name__)


@controlTraining.route("/setTraining", methods = ["POST"])
def setTraining():
    if session.get("logged_in"):
        session["equvsequ"] = True if session["equvsequ"] == False else False
        return redirect(url_for("controlBase.training"))

    return gandalf()


@controlTraining.route("/trainingFun", methods = ["POST"])
def trainingFun():
    if session.get('logged_in'):
        token = {
            "account" : session["account"], 
            "sujet" :  str(request.form['type']),
            "equvsequ" : session["equvsequ"],
            "equ" :  None
        }

        session["sujets"] = token["sujet"]

        if session["equvsequ"]:
            token["equ"] = {
                "equipe1" : str(request.form["equipe1"]),
                "equipe2" : str(request.form["equipe2"])
            }

        response = decode(requests.post(f"{URL}{BASE}/funSujet/", 
                    encode(token)))

        sujet, simul = response["training"]

        return render_template("training.html", 
            sujetsconf = sujetsconf, sujet=sujet, simul=simul)

    return gandalf()


