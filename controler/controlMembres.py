from model.convenient.importflask import *

controlMembres = Blueprint("controlMembres", __name__)


@controlMembres.route("/registAccountAdmin", methods=["POST"])
def registAccountAdmin():
    if session.get("logged_in"):
        if session["admin"] > 1:
            if request.method == "POST":
                try :
                    newaccount = {
                        "username" : request.form["username"].lower(),
                        "password" : "",
                        "confirmpassword" : "",
                        "email" : request.form["email"],
                        "nom" : request.form["nom"],
                        "prenom" : request.form["prenom"],
                        "ecole" : request.form["ecole"],
                        "annee" : request.form["annee"],
                        "phone" : request.form["phone"],
                        "specialite" : request.form["specialite"],
                        "admin" : request.form["admin"]
                    }

                    token = {
                        "account" : newaccount,
                        "admin" : session["admin"],
                        "password" : "",
                        "confirmpassword" : "",
                        "create" : True
                    }

                    response = decode(requests.post("http://0.0.0.0/api/registAccount/", 
                        encode(token)))

                    print(response)

                    return redirect(url_for("controlBase.membres"))

                except:
                    pass

    return gandalf()


@controlMembres.route("/updateAccountAdmin/<id>", methods = ["POST", "GET"])
def updateAccountAdmin(id):
    if session.get("logged_in"):
        if session["admin"] > 1:
            token = {
                "account" : session["account"],
                "admin" : session["admin"],
                "id" : id
            }

            account = decode(requests.post("http://0.0.0.0/api/getAccount/", 
                encode(token)))

            return render_template("updateMembres.html", account = account["account"], ecole = ecoleconf, 
                annee = anneeconf, specialite = speconf, admin = adminconf)

    return gandalf()


@controlMembres.route("/updateAccountAdminFun/<id>", methods=["POST"])
def updateAccountAdminFun(id):
    if session.get("logged_in"):
        if session["admin"] > 1:
            if request.method == "POST":

                updateAccount = {
                    "username" : request.form["username"].lower(),
                    "email" : request.form["email"],
                    "nom" : request.form["nom"],
                    "prenom" : request.form["prenom"],
                    "ecole" : request.form["ecole"],
                    "annee" : request.form["annee"],
                    "phone" : request.form["phone"],
                    "specialite" : request.form["specialite"],
                    "admin" : request.form["admin"]
                }

                token = {
                    "account" : session["account"],
                    "admin" : session["admin"],
                    "updateAccount" : updateAccount,
                    "id" : id
                }

                print(decode(requests.post("http://0.0.0.0/api/updateAccount/", 
                    encode(token))))

    return redirect(url_for("controlBase.membres"))



@controlMembres.route("/resetPassword/<id>", methods = ["POST", "GET"])
def resetPassword(id):
    if session.get("logged_in"):
        if session["admin"] > 1:
            if request.method == "POST":
                token = {
                    "account" : session["account"],
                    "admin" : session["admin"],
                    "password" : "",
                    "newpassword" : "",
                    "id" : id,
                    "forced" : True
                }

                print(decode(requests.post("http://0.0.0.0/api/updatePassword/", 
                    encode(token))))		

                return redirect(url_for("controlBase.membres"))

    return gandalf()


@controlMembres.route("/delAccount/<string:id>", methods = ["POST","GET"])
def delAccount(id):
    if session.get("logged_in"):
        if session["admin"] > 1:
            try:
                token = {
                    "account" : session["account"],
                    "id" : id
                }

                print(decode(requests.post("http://0.0.0.0/api/delAccount/", 
                    encode(token))))

                return redirect(url_for("controlBase.membres"))

            except:
                pass
    
    return gandalf()
