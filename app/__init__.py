from flask import Flask
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
api_root = Api(app)
CORS(app)

app.config.from_object('config')

@app.route('/')
def helloworld():
    return "hello world"

from app import resources