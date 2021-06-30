from flask import Flask, Blueprint, jsonify, request
import jwt
import json

from backend.model.Accounts import Accounts
from backend.model.Config import Config
from backend.model.Cours import Cours
from backend.model.Infos import Infos
from backend.model.Matchs import Matchs
from backend.model.Sujets import Sujets

from backend.util.trainingFun import trainingFun
from backend.util.name import name as nameconf
from backend.util.dicoAccount import dicoAccount

from backend.init.config import *

from backend.controller.verifToken import verifToken

from backend.security.createToken import createToken
from backend.security.password import hashpassword 
from backend.security.ishackme import ishackme
