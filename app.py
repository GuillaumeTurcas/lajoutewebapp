from flask import Flask
import time
from model.config.config import secret_key
from static.gandalf.gandalf import gandalf

app = Flask(__name__)
app.secret_key = secret_key


''' Controler '''

from controler.controlAdmin import controlAdmin
from controler.controlBase import controlBase
from controler.controlConfig import controlConfig
from controler.controlLogin import controlLogin
from controler.controlMatch import controlMatch
from controler.controlMembres import controlMembres
from controler.controlSettings import controlSettings
from controler.controlSujet import controlSujet
from controler.controlTraining import controlTraining

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

from model.api.apiAccount import apiAccount
from model.api.apiConfig import apiConfig
from model.api.apiCours import apiCours
from model.api.apiInfos import apiInfos
from model.api.apiMatch import apiMatch
from model.api.apiSujet import apiSujet

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
