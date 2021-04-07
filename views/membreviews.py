from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session
from private.config.config import hf_name, salt, iterations, dksize, hf_name_pepper, iterations_pepper, dksize_pepper, defaultpass
from static.gandalf.gandalf import gandalf
from backports.pbkdf2 import pbkdf2_hmac
from flask_mysqldb import MySQL 
from app import db as mysql
import MySQLdb.cursors
import os, binascii
import datetime
import re

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

membreviews = Blueprint('membreviews', __name__)


####################Members####################


@membreviews.route('/membres')
def membres():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM accounts ORDER BY nom')
            data = cur.fetchall()
            cur.close()

            return render_template('membres.html', contacts = data)

    return gandalf()


@membreviews.route('/add_contact', methods=['POST'])
def add_contact():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                username = request.form['username'].lower()
                
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
                 
                account = cursor.fetchone()
                
                if not account :
                
                    password = request.form['password'].encode("utf8")

                    saltpepper = username.encode('utf-8')

                    pepper = pbkdf2_hmac(hf_name_pepper, password, saltpepper, iterations_pepper, dksize_pepper)
                    key = pbkdf2_hmac(hf_name, pepper, salt, iterations, dksize)
                    password = binascii.hexlify(key)


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

                else :
                	flash('Username already exist')

                return redirect(url_for('membreviews.membres'))

    return gandalf()

@membreviews.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM accounts WHERE id = %s', (id,))
            data = cur.fetchall()
            cur.close()

            return render_template('edit-contact.html', contact = data[0])

    return gandalf()


@membreviews.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                username = request.form['username'].lower()
                 
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM accounts WHERE id = %s', (id,))
                account = cursor.fetchone()
                cursor.close()

                firstusername = str(account['username'])

                if firstusername != username:
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
                    account = cursor.fetchone()
                    cursor.close()

                    username = firstusername if account else username

                email = request.form['email']
                admin = int(request.form['admin'])
                nom = request.form['nom']
                prenom = request.form['prenom']
                ecole = request.form['ecole']
                annee = request.form['annee']
                phone = request.form['phone']
                specialite = request.form['specialite']
                
                cur = mysql.connection.cursor()
                cur.execute("UPDATE accounts SET username = %s, email = %s, admin = %s, nom = %s, prenom = %s, ecole = %s, annee = %s, phone = %s, specialite = %s WHERE id = %s", 
                    (username, email, admin, nom, prenom, ecole, annee, phone, specialite, id,))

                flash('Contact Updated Successfully')
                mysql.connection.commit()

                return redirect(url_for('membreviews.membres'))

    return gandalf()


@membreviews.route('/resetpassword/<id>', methods = ['POST', 'GET'])
def resetpassword(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':

                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT username FROM accounts WHERE id = %s', (id,))
                username = cursor.fetchone()
                cursor.close()

                username = username['username']

                password = defaultpass.encode('utf-8')
                saltpepper = username.encode('utf-8')

                pepper = pbkdf2_hmac(hf_name_pepper, password, saltpepper, iterations_pepper, dksize_pepper)
                key = pbkdf2_hmac(hf_name, pepper, salt, iterations, dksize)
                password = binascii.hexlify(key)

                cur = mysql.connection.cursor()
                cur.execute("UPDATE accounts SET password = %s WHERE id = %s", (password, id,))              


                flash('Password Updated Successfully')
                mysql.connection.commit()

                return redirect(url_for('membreviews.membres'))

    return gandalf()


@membreviews.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM accounts WHERE id = {0}'.format(id))
            mysql.connection.commit()

            flash('Contact Removed Successfully')
            return redirect(url_for('membreviews.membres'))

    return gandalf()
