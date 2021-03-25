from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session
from static.gandalf.gandalf import gandalf
from flask_mysqldb import MySQL 
import MySQLdb.cursors
import os, binascii
import datetime
import re

usersviews = Blueprint('usersviews', __name__)

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

from app import db as mysql


####################Calendar####################


@usersviews.route('/about')
def calendar():
    if session.get('logged_in'): 
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM cours')
        events = cur.fetchall()
        cur.close()
        return render_template('calendar.html', events = events)

    return gandalf()


####################Application####################


@usersviews.route('/application')
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


@usersviews.route('/presence', methods=['POST'])
def presence():
    if session.get('logged_in'):
        if request.method == 'POST':
            cur = mysql.connection.cursor()
            session['present'] = True
            cur.execute("UPDATE accounts SET present = %s WHERE id =%s", (session['present'], session['id']))
            mysql.connection.commit()
            cur.close()

        return application()

    return gandalf()
