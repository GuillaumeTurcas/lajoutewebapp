import json
import jwt
from backend.init.config import secret_key, algorithm

def decode(response):
    data = jwt.decode(response.json(), secret_key, algorithm = algorithm)
    return data

def encode(data):
    response = jwt.encode(data, secret_key, algorithm = algorithm)
    return response
	
