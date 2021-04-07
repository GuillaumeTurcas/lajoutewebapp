from flask import Flask, Blueprint, render_template,redirect,url_for
from static.gandalf.gandalf import gandalf

errorviews = Blueprint('errorviews', __name__)


####################Errors####################


@errorviews.errorhandler(403)
def page_forbid(e):
    return gandalf()


@errorviews.errorhandler(404)
def page_not_found(e):
    return gandalf()


@errorviews.errorhandler(405)
def method_forbid(e):
    return gandalf()


@errorviews.errorhandler(500)
def error_server(e):
    return gandalf()

