from flask import render_template

def gandalf(msg=""):
	return render_template('gandalf.html', msg=msg)
