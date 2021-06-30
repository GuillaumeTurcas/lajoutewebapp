from backend.util.importFlask import *

viewTraining = Blueprint("viewTraining", __name__)


@viewTraining.route("/setTraining", methods = ["POST"])
def setTraining():
    if session.get("logged_in"):
        session["equvsequ"] = True if session["equvsequ"] == False else False
        return redirect(url_for("viewBase.training"))

    return gandalf()


@viewTraining.route("/trainingFun", methods = ["POST"])
def trainingFun():
    if session.get('logged_in'):
        data = {
            "type" :  str(request.form['type']),
            "equvsequ" : session["equvsequ"],
            "equ" :  None
        }

        session["sujets"] = data["type"]

        if session["equvsequ"]:
            data["equ"] = {
                "equipe1" : str(request.form["equipe1"]),
                "equipe2" : str(request.form["equipe2"])
            }

        response = Request.post(f"/funSujet", data)

        sujet, simul = response["training"]

        return render_template("training.html", 
            sujetsconf = sujetsconf, 
            sujet=sujet, 
            simul=simul)

    return gandalf()


