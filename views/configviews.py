from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session
from private.config.name import name as nameconf
from static.gandalf.gandalf import gandalf
from flask_mysqldb import MySQL 
from app import db as mysql
import MySQLdb.cursors
import random
import time

configviews = Blueprint('configviews', __name__)


####################Training####################


@configviews.route('/config')
def config():
	if session.get('logged_in'):
		if session['admin'] > 2:
			
			typeconf = str(session['configtype'])
			name = str(session['config'])

			cur = mysql.connection.cursor()
			cur.execute("SELECT * FROM config WHERE name = %s AND type = %s ORDER BY value", (name, typeconf,))
			config = cur.fetchall()
			cur.close()

			unique = nameconf(typeconf)	
			
			return render_template('config.html', config=config, names=unique)

	return gandalf()


@configviews.route('/configconf', methods = ['POST'])
def configconf():
	if session.get('logged_in'):
		if session['admin'] > 2:
			session['config'] = request.form['name']
			return redirect(url_for('configviews.config'))

	return gandalf()


@configviews.route('/configconftype', methods = ['POST'])
def configconftype():
	if session.get('logged_in'):
		if session['admin'] > 2:
			session['configtype'] = "Unique" if session['configtype'] == "Pass" else "Pass"
			return redirect(url_for('configviews.config'))

	return gandalf()


@configviews.route('/addconfunique', methods=['POST'])
def addconfunique():
	if session.get('logged_in'):
		if session['admin'] > 2:
			if request.method == 'POST':
				
				typeconf = str(session['configtype'])
				name = request.form['name']
				value = request.form['value']
				descr = request.form['descr']

				cur = mysql.connection.cursor()
				cur.execute("INSERT INTO config (type, name, value, description) VALUES (%s,%s, %s, %s)",
					(typeconf, name, value, descr))
				mysql.connection.commit()

				return redirect(url_for('configviews.config'))
	
	return gandalf()


@configviews.route('/editconf/<id>', methods = ['POST', 'GET'])
def editconf(id):
	if session.get('logged_in'):
		if session['admin'] > 2:

			cur = mysql.connection.cursor()
			cur.execute('SELECT * FROM config WHERE id = %s', (id,))
			config = cur.fetchall()
			cur.close()

			typeconf = session['configtype']

			unique = nameconf(typeconf)	

			return render_template('editconfig.html', config = config[0], names = unique)

	return gandalf()


@configviews.route('/updateconfig/<id>', methods=['POST'])
def update_config(id):
	if session.get('logged_in'):
		if session['admin'] !=  0:
			if request.method == 'POST':
				typeconf = request.form['type']
				name = request.form['name']
				value = request.form['value']
				descr = request.form['descr']

				cur = mysql.connection.cursor()
				cur.execute("UPDATE config SET type = %s, name = %s, value = %s, description = %s WHERE id = %s", 
					(typeconf, name, value, descr, id))
				mysql.connection.commit()

				return redirect(url_for('configviews.config'))

	return gandalf()

@configviews.route('/deleteconf/<string:id>', methods = ['POST','GET'])
def deleteconf(id):
	if session.get('logged_in'):
		if session['admin'] > 2:
			cur = mysql.connection.cursor()
			cur.execute('DELETE FROM config WHERE id = {0}'.format(id))
			mysql.connection.commit()

			return redirect(url_for('configviews.config'))

	return gandalf()

