from backend.util.importflask import *

controlLogin = Blueprint("controlLogin", __name__)


@controlLogin.route("/")
def home(msg = ""):
    session["theme"] = "light"
    session["create"] = ""
    return render_template("login.html", msg = msg) if not session.get("logged_in") else redirect(url_for("controlBase.homepage"))



@controlLogin.route("/login",methods=["GET","POST"])
def login():
    msg = ""
    try:
        if request.method == "POST" and "username" in request.form and "password" in request.form:
            token = {
                "username" : request.form["username"].lower(),
                "password" : request.form["password"]
            }
            account = decode(requests.post(f"{URL}{BASE}/logAccount/", 
                encode(token)))
            if account["connect"] :

                account = account["account"]

                session["logged_in"] = True
                session["admin"] = account["admin"]
                session["theme"] = account["theme"]
                session["account"] = account

                session["play"] = "False"
                session["configtype"] = "unique"
                session["config"] = "Admin"
                session["configtype"] = "unique"
                session["equvsequ"] = False
                session["sujets"] = "Débat parlementaire"
                session["dparlementaire"] = "Match Amical"
                session["create"] = ""
            elif account["gandalf"]:
                try :
                    session["count"] += 1

                    if session["count"] == 3:
                        session["count"] = 0
                        return gandalf()

                except:
                    session["count"] = 1

                cnt = session["count"]
                msg = f"Je sais ce que tu cherches à faire. ({cnt} tentative(s))"

            else:
                msg = "Failed to login"
    except: 
        pass
        
    return home(msg = msg)


@controlLogin.route("/registAccount")
def registAccount():
    return render_template("registAccount.html", ecole = ecoleconf, 
                annee = anneeconf, specialite = speconf)


@controlLogin.route("/registAccountFun", methods=["POST"])
def registAccountFun():
    try :
        newaccount = {
            "username" : request.form["username"].lower(),
            "email" : request.form["email"],
            "nom" : request.form["nom"],
            "password" : request.form["password"],
            "prenom" : request.form["prenom"],
            "ecole" : request.form["ecole"],
            "annee" : request.form["annee"],
            "phone" : request.form["phone"],
            "specialite" : request.form["specialite"],
            "admin" : 0
        }

        token = {
            "account" : newaccount,
            "admin" : 0,
            "create" : False,
            "password" : request.form["password"],
            "confirmpassword" : request.form["confirmpassword"],
        }

        regist = decode(requests.post(f"{URL}{BASE}/registAccount/", 
                        encode(token)))

        print(regist)

        if regist["add"]:
            session["create"] = ""
            return home()
        
        elif regist["gandalf"] == False:
            session["create"] = "Il y a eu une erreur lors de la création du compte"
            return registAccount()

    except:
        pass

    return gandalf()
