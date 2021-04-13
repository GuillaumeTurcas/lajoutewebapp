from flask import Flask, Blueprint, render_template,redirect,url_for, session
from static.gandalf.gandalf import gandalf

testviews = Blueprint('testviews', __name__)


####################Test####################


@testviews.route('/test')
def test():
    return redirect('https://www.youtube.com/watch?v=G1IbRujko-A')


@testviews.route('/chercheencore')
def chercheencore():
    return "<script>alert(\'À côté de gandalf, gandalf.txt !\');</script>"


@testviews.route('/letsplay')
def letsplay():
    return gandalf("Cherche !")


@testviews.route('/guillaumeestlemeilleur')
def guillaumeestlemeilleur():
	session['play'] = False if session['play'] == True else True
	return redirect(url_for('mainviews.home'))


@testviews.route('/jesuisnul')
def jesuisnul():
    return gandalf("2f 73 74 61 74 69 63 2f 67 61 6e 64 61 6c 66 2f 66 69 6e 2e 70 6e 67")


@testviews.route('/hAcKm3')
def hAcKm3():
    return "<script>alert(\'Tu as réussi ! Le code à renvoyer est 45_J3_Su15_F-rT\');</script>"