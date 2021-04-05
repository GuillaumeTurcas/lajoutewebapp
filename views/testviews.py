from flask import Flask, Blueprint, render_template,redirect,url_for
from static.gandalf.gandalf import gandalf

testviews = Blueprint('testviews', __name__)


####################Test####################


@testviews.route('/test')
def test(test):
    return redirect('https://www.youtube.com/watch?v=G1IbRujko-A')

@testviews.route('/<redirect>')
def redirect(redirect):
    return gandalf()
