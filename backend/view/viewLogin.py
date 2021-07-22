from backend.util.importFlask import *


viewLogin = Blueprint("viewLogin", __name__)


@viewLogin.route("/")
def home(msg=""):
    session["theme"] = "light"
    session["create"] = ""

    return render_template("login.html", msg=msg)\
        if not session.get("logged_in") \
        else redirect(url_for("viewBase.homepage"))


@viewLogin.route("/login", methods=["GET", "POST"])
def login():
    msg = ""

    try:
        if request.method == "POST" \
                and "username" in request.form \
                and "password" in request.form:

            data = {
                "username": request.form["username"].lower(),
                "password": request.form["password"]
            }

            account = requests.post(
                f"{URL}{BASE}/logAccount", json.dumps(data)).json()

            if account["connect"]:

                account = account["account"]

                session["logged_in"] = True
                session["admin"] = account["admin"]
                session["theme"] = account["theme"]
                session["token"] = account["token"]
                session["id"] = account["id"]
                session["account"] = account

                session["play"] = False
                session["config"] = "Admin"
                session["configtype"] = "unique"
                session["equvsequ"] = False
                session["sujets"] = "Débat parlementaire"
                session["dparlementaire"] = "Match Amical"
                session["create"] = ""

            elif account["gandalf"]:
                try:
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

    return home(msg=msg)


@viewLogin.route("/registAccount")
def registAccount():
    return render_template("registAccount.html",
                           ecole=ecoleconf,
                           annee=anneeconf,
                           specialite=speconf)


@viewLogin.route("/registAccountFun", methods=["POST"])
def registAccountFun():
    try:
        data = {
            "username": request.form["username"].lower(),
            "email": request.form["email"],
            "nom": request.form["nom"],
            "password": request.form["password"],
            "prenom": request.form["prenom"],
            "ecole": request.form["ecole"],
            "annee": request.form["annee"],
            "phone": request.form["phone"],
            "specialite": request.form["specialite"],
            "admin": 0,
            "create": False
        }

        print(data)

        if request.form["password"] == request.form["confirmpassword"]:
            regist = Request.post(f"/registAccount/", data)

        else:
            session["create"] = "Les mots de passe ne coïncident pas !"
            return registAccount()

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
