from backend.util.importFlask import *

viewSettings = Blueprint("viewSettings", __name__)


@viewSettings.route("/setTheme", methods = ["POST"])
def setTheme():
    if session.get("logged_in"):
        theme  = "dark" if session["theme"] == "light" else "light"

        session["theme"] = theme
        session["account"]["theme"] = theme
        
        data = {
            "theme" : session["theme"]
        }

        print(Request.post(f"/updateAccount/{session['id']}", data))

        return redirect(url_for("viewBase.settings"))

    return gandalf()


@viewSettings.route("/updateAccount", methods=["GET", "POST"])
def updateAccount():
    if session.get("logged_in"):
        if request.method == "POST":

            data = {
               "email" : request.form["email"],
               "ecole" : request.form["ecole"],
               "annee" : request.form["annee"],
               "phone" : request.form["phone"]
            }

            response = Request.post(f"/updateAccount/{session['id']}", data)

            if not response["gandalf"]:
                return redirect(url_for("viewBase.homepage"))

    return gandalf()


@viewSettings.route("/updatePassword/", methods=["GET", "POST"])
def updatePassword():
    if session.get("logged_in"):
        if request.method == "POST" :
            newpassword = request.form["newpassword"]
            confirmpassword = request.form["confirmpassword"]

            if newpassword == confirmpassword:
                data = {
                    "password" : request.form["password"],
                    "newpassword" : newpassword,
                    "forced" : False
                }

                password = Request.post(f"/updatePassword/{session['id']}", data)

                if password["update"]:
                    return redirect(url_for("viewBase.logout"))

            return redirect(url_for("viewBase.settings"))

    return gandalf()
