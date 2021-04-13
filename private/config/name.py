from flask_mysqldb import MySQL 
from app import db as mysql
import MySQLdb.cursors

def name(typeconf):
	
	unique = []

	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM config WHERE type = %s ORDER BY value", (typeconf,))
	config = cur.fetchall()

	for conf in config:
		name = str(conf[2]) 
		unique.append(name) if name not in unique else 0

	return unique