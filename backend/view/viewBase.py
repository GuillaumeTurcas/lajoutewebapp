from backend.util.importFlask import *

viewBase = Blueprint("viewBase", __name__)


@viewBase.route("/homepage")
def homepage():
    if session.get("logged_in"):
        session["theme"] = session["account"]["theme"]

        account = Request.get(f"/account/{session['id']}")
        infos = Request.get("/infos")

        return render_template("home.html",
                               account=account["account"],
                               infos=infos["infos"])

    return redirect(url_for("viewLogin.home"))


@viewBase.route("/calendrier")
def calendrier():
    if session.get("logged_in"):
        cours = Request.get(f"/getCours")

        return render_template("calendrier.html", events=cours["cours"])

    return gandalf()


@viewBase.route("/application")
def application():
    if session.get("logged_in"):
        contacts = Request.get(f"/accounts")
        account = Request.get(f"/account/{session['id']}")
        cours = Request.get(f"/getCours")

        session["present"] = account["account"]["present"]

        return render_template("application.html",
                               contacts=contacts["accounts"],
                               account=account["account"],
                               cours=cours["cours"],
                               date=date)

    return gandalf()


@viewBase.route("/training")
def training(sujet="None", simul="None"):
    if session.get("logged_in"):

        return render_template("training.html",
                               sujetsconf=sujetsconf,
                               sujet=sujet,
                               simul=simul)

    return gandalf()


@viewBase.route("/matchs")
def matchs():
    if session.get("logged_in"):
        matchs = Request.get(f"/getMatchs/{session['dparlementaire']}")

        return render_template("matchs.html",
                               dbparl=matchs["match"],
                               dbpconf=dbpconf)

    return gandalf()


@viewBase.route("/settings")
def settings():
    if session.get("logged_in"):
        account = Request.get(f"/account/{session['id']}")

        return render_template("settings.html",
                               ecole=ecoleconf,
                               annee=anneeconf,
                               contact=account["account"])

    return gandalf()


@viewBase.route("/adminpage")
def admin():
    if session.get("logged_in"):
        if session["admin"] > 0:

            return render_template("adminpage.html", date=date)

    return gandalf()


@viewBase.route("/sujet")
def sujet():
    if session.get("logged_in"):
        if session["admin"] > 0:
            sujets = Request.get(f"/getSujets/{str(session['sujets'])}")

            return render_template("sujets.html",
                                   sujets=sujets["sujet"],
                                   sujetsconf=sujetsconf)

    return gandalf()


@viewBase.route("/partenariats")
def partenariats():
    if session.get("logged_in"):
        if session["admin"] > 0:
            return render_template("partenariats.html")


@viewBase.route("/events")
def events():
    if session.get("logged_in"):
        if session["admin"] > 0:
            return render_template("events.html")


@viewBase.route("/membres")
def membres():
    if session.get("logged_in"):
        if session["admin"] > 1:
            contacts = Request.get(f"/accounts")

            return render_template("membres.html",
                                   contacts=contacts["accounts"],
                                   ecole=ecoleconf,
                                   annee=anneeconf,
                                   specialite=speconf,
                                   admin=adminconf)

    return gandalf()


@viewBase.route("/config")
def config():
    if session.get("logged_in"):
        if session["admin"] > 2:
            config = Request.get(
                f"/getConfigs/{session['config']}/{session['configtype']}")

            return render_template("config.html",
                                   config=config["config"],
                                   names=config["name"])

    return gandalf()


@viewBase.route("/index")
def index():
    if session.get("logged_in"):
        if session["admin"] > 0:
            contacts = Request.get(f"/accounts")

            return render_template("index.html", contacts=contacts["accounts"])

    return gandalf()


@viewBase.route("/logout")
def logout():
    session["logged_in"] = False

    return redirect(url_for("viewLogin.home"))
