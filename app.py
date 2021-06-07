from flask import Flask
import time
from backend.init.config import secret_key
from static.gandalf.gandalf import gandalf

app = Flask(__name__)
app.secret_key = secret_key


''' Controler '''

from backend.controler.controlAdmin import controlAdmin
from backend.controler.controlBase import controlBase
from backend.controler.controlConfig import controlConfig
from backend.controler.controlLogin import controlLogin
from backend.controler.controlMatch import controlMatch
from backend.controler.controlMembres import controlMembres
from backend.controler.controlSettings import controlSettings
from backend.controler.controlSujet import controlSujet
from backend.controler.controlTraining import controlTraining

app.register_blueprint(controlAdmin)
app.register_blueprint(controlBase)
app.register_blueprint(controlConfig)
app.register_blueprint(controlLogin)
app.register_blueprint(controlMatch)
app.register_blueprint(controlMembres)
app.register_blueprint(controlSettings)
app.register_blueprint(controlSujet)
app.register_blueprint(controlTraining)


''' Model '''

from backend.api.apiAccount import apiAccount
from backend.api.apiConfig import apiConfig
from backend.api.apiCours import apiCours
from backend.api.apiInfos import apiInfos
from backend.api.apiMatch import apiMatch
from backend.api.apiSujet import apiSujet

app.register_blueprint(apiAccount)
app.register_blueprint(apiConfig)
app.register_blueprint(apiCours)
app.register_blueprint(apiInfos)
app.register_blueprint(apiMatch)
app.register_blueprint(apiSujet)


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
