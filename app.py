from flask import Flask
import time
from backend.init.config import secret_key
from static.gandalf.gandalf import gandalf

app = Flask(__name__)
app.secret_key = secret_key


''' Controler '''

from backend.view.viewAdmin import viewAdmin
from backend.view.viewBase import viewBase
from backend.view.viewConfig import viewConfig
from backend.view.viewLogin import viewLogin
from backend.view.viewMatch import viewMatch
from backend.view.viewMembres import viewMembres
from backend.view.viewSettings import viewSettings
from backend.view.viewSujet import viewSujet
from backend.view.viewTest import viewTest
from backend.view.viewTraining import viewTraining

app.register_blueprint(viewAdmin)
app.register_blueprint(viewBase)
app.register_blueprint(viewConfig)
app.register_blueprint(viewLogin)
app.register_blueprint(viewMatch)
app.register_blueprint(viewMembres)
app.register_blueprint(viewSettings)
app.register_blueprint(viewSujet)
app.register_blueprint(viewTest)
app.register_blueprint(viewTraining)


''' Model '''

from backend.controller.controlAccount import controlAccount
from backend.controller.controlConfig import controlConfig
from backend.controller.controlCours import controlCours
from backend.controller.controlInfos import controlInfos
from backend.controller.controlMatch import controlMatch
from backend.controller.controlSujet import controlSujet

app.register_blueprint(controlAccount)
app.register_blueprint(controlConfig)
app.register_blueprint(controlCours)
app.register_blueprint(controlInfos)
app.register_blueprint(controlMatch)
app.register_blueprint(controlSujet)


''' Errors '''

@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def error_server(e):
    time.sleep(1)
    return gandalf()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug="True")
