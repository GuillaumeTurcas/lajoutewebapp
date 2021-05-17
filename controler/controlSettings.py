from model.convenient.importflask import *

controlSettings = Blueprint("controlSettings", __name__)

@controlSettings.route("/setTheme", methods = ["POST"])
def setTheme():
    if session.get("logged_in"):
        theme = "dark" if session["theme"] == "light" else "light"
        session["theme"] = theme
        session["account"]["theme"] = theme

        token = {
            "account" : session["account"],
            "admin" : session["admin"],
            "updateAccount" : session["account"],
            "id" : session["account"]["id"]
        }
        
        print(decode(requests.post(URL + BASE + "/updateAccount/", 
        encode(token))))

        return redirect(url_for("controlBase.settings"))

    return gandalf()


@controlSettings.route("/updateAccount", methods=["GET", "POST"])
def updateAccount():
    if session.get("logged_in"):
        if request.method == "POST":
            session["account"]["email"] = request.form["email"]
            session["account"]["ecole"] = request.form["ecole"]
            session["account"]["annee"] = request.form["annee"]
            session["account"]["phone"] = request.form["phone"]

            token = {
                "account" : session["account"],
                "admin" : session["admin"],
                "updateAccount" : session["account"],
                "id" : session["account"]["id"]
            }

            print(decode(requests.post(URL + BASE + "/updateAccount/", 
            encode(token))))

            return redirect(url_for("controlBase.homepage"))

    return gandalf()


@controlSettings.route("/updatePassword/", methods=["GET", "POST"])
def updatePassword():
    if session.get("logged_in"):
        if request.method == "POST" :
            newpassword = request.form["newpassword"]
            confirmpassword = request.form["confirmpassword"]

            if newpassword == confirmpassword:
                token = {
                    "account" : session["account"],
                    "admin" : session["admin"],
                    "password" : request.form["password"],
                    "newpassword" : newpassword,
                    "id" : session["account"]["id"],
                    "forced" : False
                }

                password = decode(requests.post(URL + BASE + "/updatePassword/", 
                encode(token)))
                print(password)

                if password["update"]:
                    return redirect(url_for("controlBase.logout"))

            return redirect(url_for("controlBase.settings"))

    return gandalf()

