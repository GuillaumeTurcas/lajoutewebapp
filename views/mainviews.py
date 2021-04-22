from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session
from private.config.config import ecoleconf, anneeconf, speconf, firstaccount, adminconf
from private.security.password import hashpassword as hashpassword
from private.security.ishackme import ishackme
from static.gandalf.gandalf import gandalf
from flask_mysqldb import MySQL 
from app import db as mysql
import MySQLdb.cursors
import random
import time

mainviews = Blueprint('mainviews', __name__)


####################Login####################


@mainviews.route('/')
def home(msg = ''):
    session['theme'] = 'light'
    return render_template('login.html', msg = msg) if not session.get('logged_in') else homepage()



@mainviews.route("/login",methods=["GET","POST"])
def login():
    msg = ''
    error = 0

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username'].lower()
        password = request.form['password']

        if ishackme(username = username):
            return gandalf()

        password = hashpassword(username, password)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        cursor.close()

        if account:

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
            session['play'] = "False"
            session['config'] = "Admin"
            session['config'] = "Admin"
            session['configtype'] = "unique"
            session['equvsequ'] = False
            session['sujets'] = "Débat parlementaire"
            session['dparlementaire'] = "Match Amical"

        else:
            sleep = random.randint(0, 100)
            time.sleep(10) if sleep < 10 else 0
            time.sleep(100) if sleep == 99 else 0
            msg = 'Erreur d\'authentification !' 

    return home(msg)


@mainviews.route("/password", methods=["GET", "POST"])
def password():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'newpassword' in request.form:
        username = request.form['username'].lower()
        password = request.form['password']

        if ishackme(username = username):
            return gandalf()

        password = hashpassword(username, password)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        cursor.close()

        password = request.form['newpassword']
        confirmpassword = request.form['confirmpassword']

        if account and password == confirmpassword:

            password = hashpassword(username, password)

            cur = mysql.connection.cursor()
            session['present'] = True
            cur.execute("UPDATE accounts SET password = %s WHERE username =%s", (password, username))
            mysql.connection.commit()
            cur.close()

            msg = 'Password successfully changed !'
        		
        else:
            time.sleep(1)
            msg = 'Une erreur s\'est produite !'

    return render_template('login.html', msg1=msg)   


####################Home####################


@mainviews.route('/createaccount')
def createaccount():
    return render_template('createaccount.html', ecole = ecoleconf, 
                annee = anneeconf, specialite = speconf)


@mainviews.route('/createaccount_', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        username = request.form['username'].lower()
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
         
        account = cursor.fetchone()

        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        
        if not account and password == confirmpassword:

            password = hashpassword(username, password)

            email = request.form['email']
            nom = request.form['nom']
            prenom = request.form['prenom']
            ecole = request.form['ecole']
            annee = request.form['annee']
            phone = request.form['phone']
            specialite = request.form['specialite']

            admin = 2 if username == firstaccount else 0

            if ishackme(username, email, nom, prenom, ecole, annee, phone, specialite):
                time.sleep(1)
                return gandalf()

            cur = mysql.connection.cursor()
            cur.execute(""" INSERT INTO accounts 
                            (username, password, 
                            admin, email, present, 
                            nom, prenom, ecole, annee, 
                            phone, specialite, theme) 
                            VALUES (%s,%s, %s, %s, 0, %s, 
                            %s, %s, %s, %s, %s, 'light')""",

                        (username, password, admin, email, 
                        nom, prenom, ecole, annee, phone, 
                        specialite,))

            mysql.connection.commit()

            flash('Contact Added successfully')

        else :
            flash('Error to add contact')

            return createaccount()

        return home()

    return gandalf()
    

####################Home####################


@mainviews.route('/home')
def homepage():
    if session.get('logged_in'):
        prenom = session['prenom']
        nom = session['nom']
        print(f'{prenom} {nom}')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        cursor.close()

        if not account:
            session['logged_in'] = False

        else :
            session['admin'] = account['admin']
            session['configtype'] = "unique"
            session['theme'] = account['theme']

            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM infos ORDER BY datedb')
            infos = cur.fetchall()
            cur.close()

            return render_template('home.html', account=account, infos=infos)

    return home()


####################Edit####################


@mainviews.route('/edituser', methods = ['POST', 'GET'])
def edituser():
    if session.get('logged_in'):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        data = cur.fetchall()
        cur.close()

        session['configtype'] = "unique"

        return render_template('edituser.html', ecole = ecoleconf, annee = anneeconf, contact = data[0])

    return gandalf()


@mainviews.route('/updateuser/<id>', methods=['POST'])
def updateuser(id):
    if session.get('logged_in'):
        if int(session['id']) ==  int(id):
            if request.method == 'POST':
                email = request.form['email']
                ecole = request.form['ecole']
                annee = request.form['annee']
                phone = request.form['phone']

                if ishackme(email = email, ecole = ecole, annee = annee, phone = phone):
                    time.sleep(1)
                    return gandalf()
				
                cur = mysql.connection.cursor()
                cur.execute("UPDATE accounts SET email = %s, ecole = %s, annee = %s, phone = %s WHERE id = %s", 
                    (email, ecole, annee, phone, id))
                mysql.connection.commit()

                return redirect(url_for('mainviews.home'))

    return gandalf()


@mainviews.route('/configtheme', methods = ['POST'])
def configtheme():
    if session.get('logged_in'):
        theme = "dark" if session['theme'] == "light" else "light"
        session['theme'] = theme
        cur = mysql.connection.cursor()
        cur.execute("UPDATE accounts SET theme = %s WHERE id = %s", (theme, session['id']))
        mysql.connection.commit()
        return redirect(url_for('mainviews.edituser'))

    return gandalf()


####################Logout####################


@mainviews.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
