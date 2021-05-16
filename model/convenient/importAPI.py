from flask import Flask, Blueprint, jsonify, request

from model.model.Accounts import Accounts
from model.model.Config import Config
from model.model.Cours import Cours
from model.model.Infos import Infos
from model.model.Matchs import Matchs
from model.model.Sujets import Sujets
from model.convenient.trainingFun import trainingFun

from model.convenient.dicoAccount import dicoAccount
from model.api.verifToken import verifToken
from model.security.password import hashpassword 
from model.security.ishackme import ishackme
from model.config.config import secret_key, firstaccount, algorithm, defaultpass
import jwt


