from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session
from private.config.config import sujetsconf, dbpconf
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


@trainingviews.route('/configtraining', methods = ['POST'])
def configtraining():
	if session.get('logged_in'):
		session['equvsequ'] = True if session['equvsequ'] == False else False
		return redirect(url_for('trainingviews.training'))

	return gandalf()


####################Débat parlementaire####################


@trainingviews.route('/debatparlementaire')
def debatparlementaire():
	if session.get('logged_in'):
		types = str(session['dparlementaire'])
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM dbparlementaire WHERE type = %s ORDER BY datedb", (types,))
		dbparl = cur.fetchall()
		cur.close()
		return render_template('debatparlementaire.html', dbparl = dbparl, dbpconf = dbpconf)

	return gandalf()


@trainingviews.route('/adddbp', methods=['POST'])
def adddbp():
	if session.get('logged_in'):
		if session['admin'] !=  0:
			if request.method == 'POST':
				datedb = request.form['datedb']
				types = request.form['type']
				sujet = request.form['sujet']
				equipe = request.form['equipe']
				gouvernement = request.form['gouvernement']
				opposition = request.form['opposition']
				morateur = request.form['morateur']
				mequipe = request.form['mequipe']
				jury = request.form['jury']

				cur = mysql.connection.cursor()
				cur.execute("""INSERT INTO dbparlementaire 
							(datedb, type, sujet, equipe, gouvernement, opposition, meilorateur, meilequipe, jury) 
							VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)""",
				 			(datedb, types, sujet, equipe, gouvernement, opposition, morateur, mequipe, jury))
				mysql.connection.commit()
				cur.close()

				flash('Match added successfully')

				return redirect(url_for('trainingviews.debatparlementaire'))

	return gandalf()


@trainingviews.route('/configdbp', methods = ['POST'])
def configdbp():
	if session.get('logged_in'):
		session['dparlementaire'] = request.form['type']
		return redirect(url_for('trainingviews.debatparlementaire'))

	return gandalf()


@trainingviews.route('/editdbp/<id>', methods = ['POST', 'GET'])
def editdbp(id):
    if session.get('logged_in'):
        if session['admin'] !=  0:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM dbparlementaire WHERE id = %s', (id,))
            dbparl = cur.fetchall()
            cur.close()

            return render_template('editdbp.html', dbparl = dbparl, dbpconf = dbpconf)

    return gandalf()


@trainingviews.route('/updatedbp/<id>', methods=['POST'])
def updatedbp(id):
    if session.get('logged_in'):
        if session['admin'] !=  0:
            if request.method == 'POST':
                sujet = request.form['sujet']
                types = request.form['type']

                cur = mysql.connection.cursor()
                cur.execute("UPDATE sujets SET sujet = %s, type = %s WHERE id = %s", 
                    (sujet, types, id))

                flash('Sujet updated Successfully')
                mysql.connection.commit()
                return redirect(url_for('adminviews.sujets'))

    return gandalf()


@trainingviews.route('/deletedbp/<string:id>', methods = ['POST','GET'])
def delete_sujet(id):
    if session.get('logged_in'):
        if session['admin'] !=  0:
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM dbparlementaire WHERE id = {0}'.format(id))
            mysql.connection.commit()

            flash('Match removed Successfully')
            return debatparlementaire()

    return gandalf()