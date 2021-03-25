from flask import Flask
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.secret_key = '2#$$@1gwe2e!-e23'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'lajoute'
app.config['MYSQL_DB'] = 'lajoute'

db = MySQL(app)

from views.usersviews import usersviews
from views.adminviews import adminviews
from views.mainviews import mainviews

app.register_blueprint(usersviews, url_prefix="")
app.register_blueprint(adminviews, url_prefix="")
app.register_blueprint(mainviews, url_prefix="")


if __name__=="__main__":
    app.run(debug='True', host='0.0.0.0', port='80')