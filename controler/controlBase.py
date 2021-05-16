from model.convenient.importflask import *

controlBase = Blueprint("controlBase", __name__)


@controlBase.route("/homepage")
def homepage():
    if session.get("logged_in"):
        token = {
            "account" : session["account"],
            "admin" : session["admin"],
            "id" : session["account"]["id"]
        }

        session["theme"] = session["account"]["theme"]

        account = decode(requests.post("http://0.0.0.0/api/getAccount/", 
            encode(token)))

        infos = decode(requests.post("http://0.0.0.0/api/getInfos/",
            encode(session["account"])))

        return render_template("home.html", account=account["account"], infos=infos["infos"])

    return redirect(url_for("controlLogin.home"))


@controlBase.route("/calendrier")
def calendrier():
    if session.get("logged_in"): 
        cours = decode(requests.post("http://0.0.0.0/api/getCours",
            encode(session["account"])))

        return render_template("calendrier.html", events = cours["cours"])

    return gandalf()


@controlBase.route("/application")
def application():
    if session.get("logged_in"):
        token = {
            "account" : session["account"],
            "admin" : session["admin"],
            "id" : session["account"]["id"]
        }

        contacts = decode(requests.post("http://0.0.0.0/api/getAccounts/", 
            encode(session["account"])))

        account = decode(requests.post("http://0.0.0.0/api/getAccount/", 
            encode(token)))

        cours = decode(requests.post("http://0.0.0.0/api/getCours",
            encode(session["account"])))

        session["present"] = account["account"]["present"]

        return render_template("application.html", contacts = contacts["accounts"], 
            account = account["account"], cours = cours["cours"], date = date)

    return gandalf()


@controlBase.route("/training")
def training(sujet = "None", simul = "None"):
    if session.get("logged_in"):
        return render_template("training.html", sujetsconf=sujetsconf, sujet=sujet, simul=simul)

    return gandalf()


@controlBase.route("/matchs")
def matchs():
    if session.get("logged_in"):
        token = {
            "account" : session["account"],
            "type" : session["dparlementaire"]
        }

        matchs = decode(requests.post("http://0.0.0.0/api/getMatchs/", 
            encode(token)))

        return render_template("matchs.html", dbparl = matchs["matchs"], dbpconf = dbpconf)

    return gandalf()


@controlBase.route("/settings")
def settings():
    if session.get("logged_in"):
        token = {
            "account" : session["account"],
            "admin" : session["admin"],
            "id" : session["account"]["id"]
        }

        account = decode(requests.post("http://0.0.0.0/api/getAccount/", 
            encode(token)))

        return render_template("settings.html", ecole = ecoleconf, 
            annee = anneeconf, contact = account["account"])

    return gandalf()


@controlBase.route("/admin")
def admin():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            return render_template("adminpage.html", date=date)

    return gandalf()


@controlBase.route("/sujet")
def sujet():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            token = {
                "account" : session["account"], 
                "sujet" : str(session["sujets"])
            }

            sujets = decode(requests.post("http://0.0.0.0/api/getSujets/", 
                encode(token)))

            return render_template("sujets.html",
                sujets = sujets["sujets"], sujetsconf = sujetsconf)

    return gandalf()


@controlBase.route("/membres")
def membres():
    if session.get("logged_in"):
        if session["admin"] > 1:
            contacts = decode(requests.post("http://0.0.0.0/api/getAccounts/", 
                encode(session["account"])))

            return render_template("membres.html", contacts = contacts["accounts"], 
                ecole = ecoleconf, annee = anneeconf, 
                specialite = speconf, admin = adminconf)

    return gandalf()


@controlBase.route("/config")
def config():
    if session.get("logged_in"):
        if session["admin"] > 2:
            token = {
                "account" : session["account"], 
                "type" : str(session["configtype"]),
                "name" : str(session["config"])
            }        

            config = decode(requests.post("http://0.0.0.0/api/getConfigs/", 
                encode(token)))

            return render_template("config.html", config = config["config"], 
                names = nameconf(str(session["configtype"])))
    
    return gandalf()


@controlBase.route("/index")
def index():
    if session.get("logged_in"):
        if session["admin"] !=  0:
            contacts = decode(requests.post("http://0.0.0.0/api/getAccounts/", 
                encode(session["account"])))

            return render_template("index.html", contacts = contacts["accounts"])
    
    return gandalf()


@controlBase.route("/logout")
def logout():
    session["logged_in"] = False
    
    return redirect(url_for("controlLogin.home"))
