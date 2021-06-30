from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session, jsonify

from backend.init.config import *
from backend.view.Request import Request

from static.gandalf.gandalf import gandalf

import datetime
import requests
import random
import json
import jwt

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")



