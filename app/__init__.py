from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api_root = Api(app)

app.config.from_object('config')

from app import api
