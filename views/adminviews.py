from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session
from backports.pbkdf2 import pbkdf2_hmac
from static.gandalf.gandalf import gandalf
from flask_mysqldb import MySQL 
from app import db as mysql
import MySQLdb.cursors
import os, binascii
import re

adminviews = Blueprint('adminviews', __name__)
salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')


####################Members####################


@adminviews.route('/membres')
def membres():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM accounts ORDER BY nom')
            data = cur.fetchall()
            cur.close()

            return render_template('membres.html', contacts = data)

    return gandalf()


@adminviews.route('/add_contact', methods=['POST'])
def add_contact():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password'].encode("utf8")

                key = pbkdf2_hmac("sha256", password, salt, 50000, 32)
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
                return redirect(url_for('adminviews.membres'))

    return gandalf()

@adminviews.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM accounts WHERE id = %s', (id,))
            data = cur.fetchall()
            cur.close()

            return render_template('edit-contact.html', contact = data[0])

    return gandalf()


@adminviews.route('/update/<id>', methods=['POST'])
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
                return redirect(url_for('adminviews.membres'))

    return gandalf()


@adminviews.route('/resetpassword/<id>', methods = ['POST', 'GET'])
def resetpassword(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                passwd = session['username'].encode("utf8")
                key = pbkdf2_hmac("sha256", passwd, salt, 50000, 32)
                password = binascii.hexlify(key)

                cur = mysql.connection.cursor()
                cur.execute("UPDATE accounts SET password = %s WHERE id = %s", 
                (password, id))

                flash('Contact Updated Successfully')
                mysql.connection.commit()
                return redirect(url_for('adminviews.membres'))

    return gandalf()


@adminviews.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM accounts WHERE id = {0}'.format(id))
            mysql.connection.commit()

            flash('Contact Removed Successfully')
            return redirect(url_for('adminviews.membres'))

    return gandalf()


####################Admin####################


@adminviews.route('/adminpage', methods = ['POST','GET'])
def adminpage():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            return render_template('adminpage.html')
    return gandalf()


@adminviews.route('/add_cours', methods=['POST'])
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

                return redirect(url_for('usersviews.application'))

    return gandalf()


@adminviews.route('/deletecours/<string:id>', methods = ['POST','GET'])
def delete_cours(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM cours WHERE id = {0}'.format(id))
            mysql.connection.commit()

            return redirect(url_for('mainviews.home'))

    return gandalf()


####################Application####################


@adminviews.route('/appel', methods=['POST'])
def appel():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                cur = mysql.connection.cursor()
                cur.execute("UPDATE accounts SET present = %s", (False,))
                mysql.connection.commit()
                cur.close()

            return redirect(url_for('usersviews.application'))

    return gandalf()


####################Home####################


@adminviews.route('/addinfo', methods=['POST'])
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

                return redirect(url_for('mainviews.home'))

    return gandalf()


@adminviews.route('/deleteinfo/<string:id>', methods = ['POST','GET'])
def deleteinfo(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM infos WHERE id = {0}'.format(id))
            mysql.connection.commit()

            return redirect(url_for('mainviews.home'))

    return gandalf()


####################Index####################


@adminviews.route('/index')
def index():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM accounts ORDER BY nom')
            data = cur.fetchall()
            cur.close()

            return render_template('index.html', contacts = data)

    return gandalf()