from flask import Flask
from private.config.config import host, user, passwd, db, secret_key
from static.gandalf.gandalf import gandalf
from flask_mysqldb import MySQL
import time

app = Flask(__name__)
app.secret_key = secret_key

app.config["MYSQL_HOST"] = host
app.config["MYSQL_USER"] = user
app.config["MYSQL_PASSWORD"] = passwd
app.config["MYSQL_DB"] = db

db = MySQL(app)

from views.usersviews import usersviews
from views.adminviews import adminviews
from views.trainingviews import trainingviews
from views.membreviews import membreviews
from views.configviews import configviews
from views.mainviews import mainviews
from views.testviews import testviews

app.register_blueprint(usersviews)
app.register_blueprint(adminviews)
app.register_blueprint(trainingviews)
app.register_blueprint(membreviews)
app.register_blueprint(configviews)
app.register_blueprint(mainviews)
app.register_blueprint(testviews)
'''
@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def error_server(e):
    time.sleep(1)
    return gandalf()
'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug="True")
