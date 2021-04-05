from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session
from backports.pbkdf2 import pbkdf2_hmac
from static.gandalf.gandalf import gandalf
from flask_mysqldb import MySQL 
from app import db as mysql
import MySQLdb.cursors
import os, binascii
import re

mainviews = Blueprint('mainviews', __name__)
salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')

####################Login####################


@mainviews.route('/')
def home():
    return render_template('login.html') if not session.get('logged_in') else homepage()



@mainviews.route("/login",methods=["GET","POST"])
def login():
    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password'].encode("utf8")

        key = pbkdf2_hmac("sha256", password, salt, 50000, 32)
        password = binascii.hexlify(key)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))

        account = cursor.fetchone()

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

        else:
            msg = 'Erreur d\'authentification!'

    return home()


@mainviews.route("/password", methods=["GET", "POST"])
def password():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'newpassword' in request.form:
        username = request.form['username']
        password = request.form['password'].encode("utf8")

        key = pbkdf2_hmac("sha256", password, salt, 50000, 32)
        password = binascii.hexlify(key)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))

        account = cursor.fetchone()
        cursor.close()

        if account:
            newpassword = request.form['newpassword'].encode("utf8")
            key = pbkdf2_hmac("sha256", newpassword, salt, 50000, 32)
            newpassword = binascii.hexlify(key)

            cur = mysql.connection.cursor()
            session['present'] = True
            cur.execute("UPDATE accounts SET password = %s WHERE username =%s", (newpassword, username))
            mysql.connection.commit()
            cur.close()

            msg = 'Password successfully changed !'

        else:
            msg = 'Erreur d\'authentification!'

    return render_template('login.html', msg1=msg)   


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

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM infos ORDER BY datedb')
        infos = cur.fetchall()
        cur.close()

        # Show the profile page with account info
        return render_template('home.html', account=account, infos=infos)

    return home()


@mainviews.route('/edituser', methods = ['POST', 'GET'])
def edituser():
    if session.get('logged_in'):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        data = cur.fetchall()
        cur.close()

        return render_template('edit.html', contact = data[0])

    return gandalf()


@mainviews.route('/edituser/<id>', methods=['POST'])
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

                return redirect(url_for('mainviews.home'))

    return gandalf()


####################Logout####################


@mainviews.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
