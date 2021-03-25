from flask import Flask
from static.db.config import host, user, passwd, db
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.secret_key = '2#$$@1gwe2e!-e23'

app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = passwd
app.config['MYSQL_DB'] = db

db = MySQL(app)

from views.usersviews import usersviews
from views.adminviews import adminviews
from views.mainviews import mainviews

app.register_blueprint(usersviews, url_prefix="")
app.register_blueprint(adminviews, url_prefix="")
app.register_blueprint(mainviews, url_prefix="")


if __name__=="__main__":
    app.run(debug='True', host='0.0.0.0', port='80')