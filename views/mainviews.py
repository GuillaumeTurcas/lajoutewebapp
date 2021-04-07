from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session
from private.config.config import salt, hf_name, iterations, dksize, hf_name_pepper, iterations_pepper, dksize_pepper
from static.gandalf.gandalf import gandalf
from backports.pbkdf2 import pbkdf2_hmac

from flask_mysqldb import MySQL 
from app import db as mysql
import MySQLdb.cursors
import os, binascii
import random
import time
import re

mainviews = Blueprint('mainviews', __name__)

####################Login####################


@mainviews.route('/')
def home(msg = ''):
    return render_template('login.html', msg = msg) if not session.get('logged_in') else homepage()



@mainviews.route("/login",methods=["GET","POST"])
def login():
    msg = ''
    error = 0

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password'].encode("utf8")

        saltpepper = username.encode('utf-8')

        pepper = pbkdf2_hmac(hf_name_pepper, password, saltpepper, iterations_pepper, dksize_pepper)
        key = pbkdf2_hmac(hf_name, pepper, salt, iterations, dksize)
        password = binascii.hexlify(key)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))

        """
        If you need to change the configuration in the config file, you  can unhide the line below to reset the password
        on your admin account. Your password will be the secure password you chose in the config file. 
        After that, return here and hide again the line.
        """
        #cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,)) 

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
        
        for hack in ('admin', 'test', '=', '%', '--', '\''):
        	if hack in username:
        		time.sleep(1)
        		return gandalf()

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
        password = request.form['password'].encode("utf8")

        saltpepper = username.encode('utf-8')

        pepper = pbkdf2_hmac(hf_name_pepper, password, saltpepper, iterations_pepper, dksize_pepper)
        key = pbkdf2_hmac(hf_name, pepper, salt, iterations, dksize)
        password = binascii.hexlify(key)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))

        account = cursor.fetchone()
        cursor.close()

        if account:
            password = request.form['newpassword'].encode("utf8")

            saltpepper = username.encode('utf-8')

            pepper = pbkdf2_hmac(hf_name_pepper, password, saltpepper, iterations_pepper, dksize_pepper)
            key = pbkdf2_hmac(hf_name, pepper, salt, iterations, dksize)
            password = binascii.hexlify(key)

            cur = mysql.connection.cursor()
            session['present'] = True
            cur.execute("UPDATE accounts SET password = %s WHERE username =%s", (password, username))
            mysql.connection.commit()
            cur.close()

            msg = 'Password successfully changed !'
        		
        else:
            sleep = random.randint(0, 100)
            time.sleep(10) if sleep < 10 else 0
            time.sleep(100) if sleep == 99 else 0
            msg = 'Erreur d\'authentification !'

            for hack in ('admin', 'test', '=', '%', '--', '\''):
                if hack in username:
                    time.sleep(1)
                    return gandalf()

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

                for forms in (email, ecole, annee, phone):
                    for hack in ('<', 'script', '--', "/"):
                        if hack in forms:
                            return gandalf()

                if annee not in ('A1', 'A2', 'A3', 'A4', 'A5', 'Autre') :
                    return gandalf()

                if ecole not in ('ESILV', 'IIM', 'EMLV', 'Autre') :
                    return gandalf()
				
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
