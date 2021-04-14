from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session
from private.config.config import sujetsconf
from static.gandalf.gandalf import gandalf
from flask_mysqldb import MySQL 
from app import db as mysql
import MySQLdb.cursors
import random
import time

trainingviews = Blueprint('trainingviews', __name__)


####################Training####################


@trainingviews.route('/training')
def training(sujet = 'None', simul = 'None'):
	if session.get('logged_in'):
		return render_template('training.html', sujetsconf=sujetsconf, sujet=sujet, simul=simul)

	return gandalf()


@trainingviews.route('/entrainement', methods = ['POST'])
def entrainement():
	if session.get('logged_in'):

		types = str(request.form['type'])
		session['sujets'] = types
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM sujets WHERE type = %s ORDER BY sujet", (types,))
		sujets = cur.fetchall()
		cur.close()

		i = len(sujets)
		c = random.randint(0, i-1)
		sujet = str(sujets[c][1])
		simul = 'None'

		if types == "Conférence de presse":
			session['equvsequ'] = False

		if session['equvsequ']:
			equip1 = request.form['equip1']
			equip2 = request.form['equip2']

			eq = [equip1, equip2]
			c = random.randint(0, 1)
			simul = f"Positive : {eq[c]} | Négative : {eq[(c+1)%2]}"

		return training(sujet, simul)

	return gandalf()


@trainingviews.route('/equvsequ', methods = ['POST'])
def equvsequ():
	if session.get('logged_in'):
		session['equvsequ'] = True if session['equvsequ'] == False else False
		return redirect(url_for('trainingviews.training'))

	return gandalf()