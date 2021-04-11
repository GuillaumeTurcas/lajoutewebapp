from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session
from private.config.config import ecoleconf, anneeconf
from static.gandalf.gandalf import gandalf
from flask_mysqldb import MySQL 
from app import db as mysql
import MySQLdb.cursors
import datetime

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

adminviews = Blueprint('adminviews', __name__)


####################Admin####################


@adminviews.route('/adminpage', methods = ['POST','GET'])
def adminpage():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            return render_template('adminpage.html', date=date)
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


@adminviews.route('/deletecours/<string:edit>', methods = ['POST','GET'])
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


####################Sujets####################


@adminviews.route('/sujets')
def sujets():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM sujets ORDER BY sujet')
            data = cur.fetchall()
            cur.close()

            return render_template('sujets.html', sujets = data)

    return gandalf()


@adminviews.route('/add_sujet', methods=['POST'])
def add_sujet():
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                sujet = request.form['sujet']
                types = request.form['type']

                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO sujets (sujet, type) VALUES (%s,%s)",
                 (sujet,types,))
                mysql.connection.commit()

                flash('Sujet added successfully')
                return redirect(url_for('adminviews.sujets'))

    return gandalf()

@adminviews.route('/editsujet/<id>', methods = ['POST', 'GET'])
def editsujet(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM sujets WHERE id = %s', (id,))
            data = cur.fetchall()
            cur.close()

            return render_template('editsujet.html', sujet = data[0])

    return gandalf()


@adminviews.route('/<id>', methods=['POST'])
def update_sujet(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            if request.method == 'POST':
                sujet = request.form['sujet']
                types = request.form['type']

                cur = mysql.connection.cursor()
                cur.execute("UPDATE sujets SET sujet = %s, type = %s WHERE id = %s", 
                    (sujet, types, id))

                flash('Contact Updated Successfully')
                mysql.connection.commit()
                return redirect(url_for('adminviews.sujets'))

    return gandalf()


@adminviews.route('/deletesujet/<string:id>', methods = ['POST','GET'])
def delete_sujet(id):
    if session.get('logged_in'):
        if session['admin'] ==  1:
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM sujets WHERE id = {0}'.format(id))
            mysql.connection.commit()

            flash('Sujet removed Successfully')
            return redirect(url_for('adminviews.sujets'))

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
