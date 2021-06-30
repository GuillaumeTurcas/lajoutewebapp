from werkzeug.wrappers import response
from backend.util.importFlask import *

viewMembres = Blueprint("viewMembres", __name__)


@viewMembres.route("/registAccountAdmin", methods=["POST"])
def registAccountAdmin():
    if session.get("logged_in"):
        if session["admin"] > 1:
            if request.method == "POST":
                try :
                    data = {
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
                        "admin" : request.form["admin"],
                        "create" : True
                    }

                    response = Request.post(f"/registAccount/", data)

                    print(response)

                    if response["gandalf"]:
                        return gandalf()

                    return redirect(url_for("viewBase.membres"))

                except:
                    pass

    return gandalf()


@viewMembres.route("/updateAccountAdmin/<id>", methods = ["POST", "GET"])
def updateAccountAdmin(id):
    if session.get("logged_in"):
        if session["admin"] > 1:

            account = Request.get(f"/account/{id}")

            if account["get"] == True:
                if int(account["account"]["admin"]) <= int(session["admin"]):

                    return render_template("updateMembres.html", 
                        account = account["account"], 
                        ecole = ecoleconf, 
                        annee = anneeconf, 
                        specialite = speconf, 
                        admin = adminconf)

    return gandalf()


@viewMembres.route("/updateAccountAdminFun/<id>", methods=["POST"])
def updateAccountAdminFun(id):
    if session.get("logged_in"):
        if session["admin"] > 1:
           try : 
                if request.method == "POST":
                    data = {
                        "username" : request.form["username"].lower(),
                        "email" : request.form["email"],
                        "nom" : request.form["nom"],
                        "prenom" : request.form["prenom"],
                        "ecole" : request.form["ecole"],
                        "annee" : request.form["annee"],
                        "phone" : request.form["phone"],
                        "specialite" : request.form["specialite"],
                        "admin" : request.form["admin"],
                    }

                    if int(data["admin"]) <= int(session["admin"]):
                        print(Request.post(f"/updateAccount/{id}", data))

                        return redirect(url_for("viewBase.membres"))
            
           except :
                pass

    return gandalf()


@viewMembres.route("/resetPassword/<id>", methods = ["POST", "GET"])
def resetPassword(id):
    if session.get("logged_in"):
        if session["admin"] :
            try:
                if request.method == "POST":
                    data = {
                        "password" : "",
                        "newpassword" : "",
                        "forced" : True
                    }

                    print(Request.post(f"/updatePassword/{id}", data))

                    return redirect(url_for("viewBase.membres"))

            except :
                pass
        
    return gandalf()


@viewMembres.route("/delAccount/<string:id>", methods = ["POST","GET"])
def delAccount(id):
    if session.get("logged_in"):
        if session["admin"] > 1:
            try:
                print(Request.delete(f"/delAccount/{id}"))

                return redirect(url_for("viewBase.membres"))

            except:
                pass
    
    return gandalf()
