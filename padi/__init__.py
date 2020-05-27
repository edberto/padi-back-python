import os
from flask import Flask
from flask_pymongo import MongoClient

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KET='dev',
)
app.config.from_pyfile('config.py')

mongo_client = MongoClient(app.config['MONGO_URI'])
padi_db = mongo_client['padi']

try:
    os.makedirs(app.instance_path)
except Exception as ex:
    pass

from .routes import *

app.register_blueprint(routes)

