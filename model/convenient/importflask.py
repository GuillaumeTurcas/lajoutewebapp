from model.config.config import ecoleconf, anneeconf, speconf, sujetsconf, dbpconf, firstaccount, adminconf, algorithm, secret_key
from flask import Flask, Blueprint, render_template,request,flash,redirect,url_for,abort, session, jsonify
from model.convenient.name import name as nameconf
from model.security.code import decode, encode
from static.gandalf.gandalf import gandalf
import datetime
import requests
import random
import json
import jwt

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")


