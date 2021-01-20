from flask import Flask, render_template,request,flash,redirect,url_for,abort, session
from flask_mail import Mail, Message
from flask_mysqldb import MySQL 
from static.pi2.model import main as model
import MySQLdb.cursors

import datetime
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

import re

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra prot	ection)
app.secret_key = '2#$$@1gwe2e!-e23'


# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'lajoute'
app.config['MYSQL_DB'] = 'lajoute'

# Intialize MySQL
mysql = MySQL(app)

#-----------------------------------------


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return homepage()
        

@app.route('/home')
def homepage():
    if session.get('logged_in'):
        print(session['prenom'] + ' ' + session['nom'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        cursor.close()
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM infos ORDER BY datedb')
        infos = cur.fetchall()
        cur.close()
        # Show the profile page with account info
        return render_template('home.html', account=account, infos=infos)
    else:
        return gandalf()


@app.route('/edituser', methods = ['POST', 'GET'])
def edituser():
    if session.get('logged_in'):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        data = cur.fetchall()
        cur.close()
        print(data[0])
        return render_template('edit.html', contact = data[0])
    return gandalf()

@app.route('/edituser/<id>', methods=['POST'])
def updateuser(id):
    if session.get('logged_in'):
        if int(session['id']) ==  int(id):
            if request.method == 'POST':
                email = request.form['email']
                ecole = request.form['ecole']
                annee = request.form['annee']
                phone = request.form['phone']
                cur = mysql.connection.cursor()
                cur.execute("UPDATE accounts SET email = %s, ecole = %s, annee = %s, phone = %s WHERE id = %s", 
                    (email, ecole, annee, phone, id))
                mysql.connection.commit()
                return redirect(url_for('home'))
    return gandalf()

@app.route('/addinfo', methods=['POST'])
def addinfo():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                datedb = request.form['datedb']
                description = request.form['description']
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO infos (datedb, description) VALUES (%s, %s)",
                 (datedb, description,))
                mysql.connection.commit()
                return redirect(url_for('home'))
    return gandalf()

@app.route('/deleteinfo/<string:id>', methods = ['POST','GET'])
def deleteinfo(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM infos WHERE id = {0}'.format(id))
            mysql.connection.commit()
            return redirect(url_for('home'))
    return gandalf()


@app.route("/login",methods=["GET","POST"])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['logged_in'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            session['admin'] = account['admin']
            session['present'] = account['present']
            session['nom'] = account['nom']  
            session['prenom'] = account['prenom']
            session['ecole'] = account['ecole']
            session['annee'] = account['annee']
            session['specialite'] = account['specialite']
            # Redirect to home page
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Erreur d\'authentification!'
    # Show the login form with message (if any)
    return home()


@app.route("/password", methods=["GET", "POST"])
def password():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'newpassword' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        cursor.close()
        # If account exists in accounts table in out database
        if account:
            newpassword = request.form['newpassword']
            cur = mysql.connection.cursor()
            session['present'] = True
            cur.execute("UPDATE accounts SET password = %s WHERE username =%s", (newpassword, username))
            mysql.connection.commit()
            cur.close()
            msg = 'Password successfully changed !'
        else:
            msg = 'Erreur d\'authentification!'
    return render_template('password.html', msg=msg)            

@app.route('/application')
def application():
    if session.get('logged_in'):
        cur = mysql.connection.cursor()
        cur.execute('SELECT present FROM accounts WHERE id = %s', (session['id'],))
        session['present'] = cur.fetchone()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM accounts ORDER BY nom')
        data = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM cours ORDER BY datedb')
        cours = cur.fetchall()
        cur.close()
        return render_template('application.html', contacts = data, account = account, cours = cours, date = date)
    return gandalf()

@app.route('/presence', methods=['POST'])
def presence():
    if session.get('logged_in'):
        if request.method == 'POST':
            cur = mysql.connection.cursor()
            session['present'] = True
            cur.execute("UPDATE accounts SET present = %s WHERE id =%s", (session['present'], session['id']))
            mysql.connection.commit()
            cur.close()
        return application()
    return login()

@app.route('/appel', methods=['POST'])
def appel():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                cur = mysql.connection.cursor()
                cur.execute("UPDATE accounts SET present = %s", (False,))
                mysql.connection.commit()
                cur.close()
            return application()
    return gandalf()

@app.route('/add_cours', methods=['POST'])
def add_cours():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                titre = request.form['titre']
                datedb = request.form['datedb']
                start = request.form['horairedebut']
                end = request.form['horairefin']
                colors = request.form['colors']
                lien = request.form['lien']
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO cours (titre, datedb, start, end, lien, color) VALUES (%s, %s,%s, %s, %s, %s)",
                 (titre, datedb, start, end, lien, colors,))
                mysql.connection.commit()
                return redirect(url_for('application'))
    return gandalf()

@app.route('/deletecours/<string:id>', methods = ['POST','GET'])
def delete_cours(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM cours WHERE id = {0}'.format(id))
            mysql.connection.commit()
            return redirect(url_for('application'))
    return gandalf()

@app.route('/about')
def about():
    if session.get('logged_in'): 
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM cours')
        events = cur.fetchall()
        cur.close()
        return render_template('calendar.html', events = events)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/index')
def index():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM accounts ORDER BY nom')
            data = cur.fetchall()
            cur.close()
            return render_template('index.html', contacts = data)
    return admin()

@app.route('/membres')
def Membres():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM accounts ORDER BY nom')
            data = cur.fetchall()
            cur.close()
            return render_template('membres.html', contacts = data)
    return gandalf()

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                email = request.form['email']
                admin = request.form['admin']
                nom = request.form['nom']
                prenom = request.form['prenom']
                ecole = request.form['ecole']
                annee = request.form['annee']
                phone = request.form['phone']
                specialite = request.form['specialite']
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO accounts (username, password, email, admin, present, nom, prenom, ecole, annee, phone, specialite) VALUES (%s,%s,%s, %s, 0, %s, %s, %s, %s, %s, %s)",
                 (username, password, email, admin,  nom, prenom, ecole, annee, phone, specialite,))
                mysql.connection.commit()
                flash('Contact Added successfully')
                return redirect(url_for('Membres'))
    return gandalf()

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM accounts WHERE id = %s', (id,))
            data = cur.fetchall()
            cur.close()
            return render_template('edit-contact.html', contact = data[0])
    return gandalf()

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                username = request.form['username']
                email = request.form['email']
                admin = request.form['admin']
                present = request.form['present']
                nom = request.form['nom']
                prenom = request.form['prenom']
                ecole = request.form['ecole']
                annee = request.form['annee']
                phone = request.form['phone']
                specialite = request.form['specialite']
                cur = mysql.connection.cursor()
                cur.execute("UPDATE accounts SET username = %s, email = %s, admin = %s, present = %s, nom = %s, prenom = %s, ecole = %s, annee = %s, phone = %s, specialite = %s WHERE id = %s", 
                    (username, email, admin, present, nom, prenom, ecole, annee, phone, specialite, id))
                flash('Contact Updated Successfully')
                mysql.connection.commit()
                return redirect(url_for('Membres'))
    return gandalf()

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM accounts WHERE id = {0}'.format(id))
            mysql.connection.commit()
            flash('Contact Removed Successfully')
            return redirect(url_for('Membres'))
    return gandalf()

@app.route('/adminpage', methods = ['POST','GET'])
def adminpage():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            return render_template('adminpage.html')
    return gandalf()

#-----------TESTS---------------------

@app.route("/test")
def test():
    return redirect("https://www.youtube.com/watch?v=Qo7Em3Uo4cw")

@app.route("/root")
def root():
	return redorect("https://www.youtube.com/watch?v=oHg5SJYRHA0&list=LL&index=46")

@app.route("/pi2")
def pi2():
    newmodel = model()
    return render_template("pi2.html", model = newmodel)

@app.route("/admin")
def admin():
    return gandalf()

@app.route("/manager")
def manager():
    return gandalf()

@app.route("/manager/html")
def managerhtml():
    return gandalf()

@app.route("/gandalf")
def gandalf():
    return render_template("gandalf.html")

#-----------MAIN-----------------------

if __name__=="__main__":
    #testconnect()
    app.run(debug = 'true', host='0.0.0.0', port='80')


